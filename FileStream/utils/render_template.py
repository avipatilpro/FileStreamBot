import aiohttp
import aiofiles
import urllib.parse
from FileStream.config import Telegram, Server
from FileStream.utils.database import Database
from FileStream.utils.human_readable import humanbytes
db = Database(Telegram.DATABASE_URL, Telegram.SESSION_NAME)

async def render_page(db_id):
    file_data=await db.get_file(db_id)
    src = urllib.parse.urljoin(Server.URL, f'dl/{file_data["_id"]}')

    if str((file_data['mime_type']).split('/')[0].strip()) == 'video':
        async with aiofiles.open('FileStream/template/stream.html') as r:
            heading = 'Watch {}'.format(file_data['file_name'])
            html_template = await r.read()
            html = html_template.replace('streamMediaLink', src).replace('streamHeading', heading)
    else:
        async with aiofiles.open('FileStream/template/dl.html') as r:
            async with aiohttp.ClientSession() as s:
                async with s.get(src) as u:
                    heading = 'Download {}'.format(file_data['file_name'])
                    file_size = humanbytes(int(u.headers.get('Content-Length')))
                    html = (await r.read()) % (heading, file_data['file_name'], src, file_size)
    return html
