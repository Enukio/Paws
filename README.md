> [!WARNING]
> ⚠️ I make every effort to avoid bot detection, but using bots is prohibited in all airdrops. I cannot guarantee that you won't be flagged as a bot. Use this software at your own risk. I am not liable for any consequences that may arise from its use.


# 🔥🔥 Use PYTHON 3.11.5 🔥🔥

## Features  
| Feature                                                       | Supported        |
|---------------------------------------------------------------|:----------------:|
| Multithreading                                                |        ✅        |
| Proxy binding to session                                      |        ✅        |
| Support for pyrogram .session / Query                         |        ✅        |
| Auto connect wallet                                           |        ✅        |
| Auto reff                                                     |        ✅        |
| Auto tasks                                                    |        ✅        |

## [Settings](https://github.com/Enukio/Paws/blob/main/.env-example)
| Settings | Description |
|-----------------------------|:-------------------------------------------------------------------------------------------------------------:|
| **API_ID / API_HASH**       | Platform data from which to run the Telegram session (default - android)                                      |       
| **REF_LINK**                | Put your ref link here (default: my ref link)                                                                 |
| **AUTO_TASK**               | Auto do tasks (default: True)                                                                                 |
| **AUTO_CONNECT_WALLET**     | Auto connect wallet in wallet.json file (default: False)                                                      |
| **IGNORE_TASKS**            | List of tasks to ignore (default: ["telegram"])                                                               |
| **DELAY_EACH_ACCOUNT**      | Random delay bewteen accounts (default: [20, 30])                                                             |
| **ADVANCED_ANTI_DETECTION** | Add more protection for your account (default: True)                                                          |
| **USE_PROXY_FROM_FILE**     | Whether to use a proxy from the bot/config/proxies.txt file (True / False)                                    |
|-----------------------------|:-------------------------------------------------------------------------------------------------------------:|


## Quick Start 📚

To install libraries and run bot - open run.bat on Windows

## Prerequisites
Before you begin, make sure you have the following installed:
- [Python](https://www.python.org/downloads/) **IMPORTANT**: Make sure to use **3.11.5**. 

## Obtaining API Keys
1. Go to my.telegram.org and log in using your phone number.
2. Select "API development tools" and fill out the form to register a new application.
3. Record the API_ID and API_HASH provided after registering your application in the .env file.

## Wallet
- You can fill custom wallet in wallet.json like this format:
```
{
  "Wallet address": "random string"
},
{
  "Wallet address2": "random string"
}
```

## Installation
You can download the [**repository**](https://github.com/Enukio/Paws) by cloning it to your system and installing the necessary dependencies:
```shell
git clone https://github.com/Enukio/Paws.git
```
```shell
cd Paws
```

Then you can do automatic installation by typing:

Windows:
```shell
run.bat
```

Linux:
```shell
run.sh
```

# Linux manual installation
```shell
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
cp .env-example .env
nano .env  # Here you must specify your API_ID and API_HASH, the rest is taken by default
python3 main.py
```

You can also use arguments for quick start, for example:
```shell
~/Paws >>> python3 main.py --action (1/2)
# Or
~/Paws >>> python3 main.py -a (1/2)

# 1 - Run clicker
# 2 - Creates a session
```

# Windows manual installation
```shell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env-example .env
# Here you must specify your API_ID and API_HASH, the rest is taken by default
python main.py
```
You can also use arguments for quick start, for example:
```shell
~/Paws >>> python3 main.py --action (1/2)
# Or
~/Paws >>> python3 main.py -a (1/2)

# 1 - Run clicker
# 2 - Creates a session
```

# Termux manual installation
```
> pkg update && pkg upgrade -y
> pkg install python rust git -y
> git clone https://github.com/Enukio/Paws.git
> cd Memelabs
> pip install -r requirements.txt
> python main.py
```

You can also use arguments for quick start, for example:
```termux
~/Paws > python main.py --action (1/2)
# Or
~/Paws > python main.py -a (1/2)

# 1 - Run clicker
# 2 - Creates a session 
```
