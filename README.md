<h1 align="center">FileStreamBot</h1>
<p align="center">
  <a href="https://github.com/Avipatilpro/FileStreamBot">
    <img src="https://graph.org/file/80d1f94e81bbc1acadb36.jpg" alt="Cover Image" width="550">
  </a>
</p>  
  <p align="center">
   </strong></a>
    <br><b>
    <a href="https://github.com/Avipatilpro/FileStreamBot/issues">Report a Bug</a>
    |
    <a href="https://github.com/Avipatilpro/FileStreamBot/issues">Request Feature</a></b>
  </p>



### 🍁 About :

<p align="center">
    <a href="https://github.com/Avipatilpro/FileStreamBot">
        <img src="https://i.ibb.co/ZJzJ9Hq/link-3x.png" height="100" width="100" alt="FileStreamBot Logo">
    </a>
</p>
<p align='center'>
  This bot provides stream links for Telegram files without the necessity of waiting for the download to complete, offering the ability to store files.
</p>


### ♢ How to Deploy :

<i>Either you could locally host, VPS, or deploy on [Heroku](https://heroku.com)</i>

#### ♢ Click on This Drop-down and get more details

<br>
<details>
  <summary><b>Deploy on Heroku (Paid)  :</b></summary>

- Fork This Repo
- Click on Deploy Easily
- Press the below button to Fast deploy on Heroku


   [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
- Go to <a href="#mandatory-vars">variables tab</a> for more info on setting up environmental variables. </details>

<details>
  <summary><b>Deploy Locally :</b></summary>
<br>

```sh
git clone https://github.com/avipatilpro/FileStreamBot
cd FileStreamBot
python3 -m venv ./venv
. ./venv/bin/activate
pip install -r requirements.txt
python3 -m FileStream
```

- To stop the whole bot,
 do <kbd>CTRL</kbd>+<kbd>C</kbd>

- If you want to run this bot 24/7 on the VPS, follow these steps.
```sh
sudo apt install tmux -y
tmux
python3 -m FileStream
```
- now you can close the VPS and the bot will run on it.

  </details>

<details>
  <summary><b>Deploy using Docker :</b></summary>
<br>
* Clone the repository:
```sh
git clone https://github.com/avipatilpro/FileStreamBot
cd FileStreamBot
```
* Build own Docker image:
```sh
docker build -t file-stream .
```

* Create ENV and Start Container:
```sh
docker run -d --restart unless-stopped --name fsb \
-v /PATH/TO/.env:/app/.env \
-p 8000:8000 \
file-stream
```
- if you need to change the variables in .env file after your bot was already started, all you need to do is restart the container for the bot settings to get updated:
```sh
docker restart fsb
```

  </details>

<details>
  <summary><b>Setting up things :</b></summary>


If you're on Heroku, just add these in the Environmental Variables
or if you're Locally hosting, create a file named `.env` in the root directory and add all the variables there.
An example of `.env` file:

```sh
API_ID = 789456
API_HASH = ysx275f9638x896g43sfzx65
BOT_TOKEN = 12345678:your_bot_token
ULOG_CHANNEL = -100123456789
FLOG_CHANNEL = -100123456789
DATABASE_URL = mongodb://admin:pass@192.168.27.1
FQDN = 192.168.27.1
HAS_SSL = False
MULTI_TOKEN1 = 12345678:bot_token_multi_client_1
MULTI_TOKEN2 = 12345678:bot_token_multi_client_2
OWNER_ID = 987456321
PORT = 8080
```
</details>


<details>
  <summary><b>Vars and Details :</b></summary>

#### 📝 Mandatory Vars :

* `API_ID`: API ID of your Telegram account, can be obtained from [My Telegram](https://my.telegram.org). `int`
* `API_HASH`: API hash of your Telegram account, can be obtained from [My Telegram](https://my.telegram.org). `str`
* `OWNER_ID`: Your Telegram User ID, Send `/id` to [@missrose_bot](https://telegram.dog/MissRose_bot) to get Your Telegram User ID `int`
* `BOT_TOKEN`: Telegram API token of your bot, can be obtained from [@BotFather](https://t.me/BotFather). `str`
* `FLOG_CHANNEL`: ID of the channel where bot will store all Files from users `int`.
* `ULOG_CHANNEL`: ID of the channel where bot will send logs of New Users`int`.
* `BOT_WORKERS`: Number of updates bot should process from Telegram at once, by default to 10 updates. `int`
* `DATABASE_URL`: MongoDB URI for saving User Data and Files List created by user. `str`
* `FQDN`: A Fully Qualified Domain Name if present without http/s. Defaults to `BIND_ADDRESS`. `str`

#### 🗼 MultiClient Vars :
* `MULTI_TOKEN1`: Add your first bot token or session strings here. `str`
* `MULTI_TOKEN2`: Add your second bot token or session strings here. `str`

#### 🪐 Optional Vars :

* `UPDATES_CHANNEL`: Channel Username without `@` to set channel as Update Channel `str`
* `FORCE_SUB_ID`: Force Sub Channel ID, if you want to use Force Sub. start with `-100` `int
* `FORCE_SUB`: Set to True, so every user have to Join update channel to use the bot. `bool`
* `AUTH_USERS`: Put authorized user IDs to use bot, separated by <kbd>Space</kbd>. `int`
* `SLEEP_THRESHOLD`: Set global flood wait threshold, auto-retry requests under 60s. `int`
* `SESSION_NAME`: Name for the Database created on your MongoDB. Defaults to `FileStream`. `str`
* `FILE_PIC`: To set Image at `/files` command. Defaults to pre-set image. `str`
* `START_PIC`: To set Image at `/start` command. Defaults to pre-set image. `str`
* `VERIFY_PIC`: To set Image at Force Sub Verification. Defaults to pre-set image. `str`
* `WORKERS`: Number of maximum concurrent workers for handling incoming updates. Defaults to `6`. `int`
* `PORT`: The port that you want your webapp to be listened to. Defaults to `8080`. `int`
* `BIND_ADDRESS`: Your server bind adress. Defauls to `0.0.0.0`. `int`
* `MODE`: Should be set to `secondary` if you only want to use the server for serving files. `str`
* `NO_PORT`: (True/False) Set PORT to 80 or 443 hide port display; ignore if on Heroku. Defaults to `False`.
* `HAS_SSL`: (can be either `True` or `False`) If you want the generated links in https format. Defaults to `False`. 

</details>

<details>
  <summary><b>How to Use :</b></summary>

:warning: **Before using the  bot, don't forget to add the bot to the `LOG_CHANNEL` as an Admin**
 
#### ‍☠️ Bot Commands :

```sh
/start      : To check the bot is alive or not.
/help       : To Get Help Message.
/about      : To check About the Bot.
/files      : To Get All Files List of User.
/del        : To Delete Files from DB with FileID. [ADMIN]
/ban        : To Ban Any Channel or User to use bot. [ADMIN]
/unban      : To Unban Any Channel or User to use bot. [ADMIN]
/status     : To Get Bot Status and Total Users. [ADMIN]
/broadcast  : To Broadcast any message to all users of bot. [ADMIN]
```

#### 🍟 Channel Support :

*Bot also Supported with Channels. Just add bot Channel as Admin. If any new file comes in Channel it will edit it with **Get Download Link** Button.*

</details>

### ❤️ Thanks To :

- [**Me**](https://github.com/AvishkarPatil) : Owner of This FileStreamBot
- [**Deekshith SH**](https://github.com/DeekshithSH) : for some modules.
- [**EverythingSuckz**](https://github.com/EverythingSuckz) : for his [FileStreamBot](https://github.com/EverythingSuckz/FileStreamBot)
- [**Biisal**](https://github.com/biisal) : for Stream Page UI

---
<h4 align='center'>© 2024 Aνιѕнкαя Pαтιℓ</h4>



