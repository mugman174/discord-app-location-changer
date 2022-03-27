# Fosscord Injector
Inject Fosscord into your Discord client :)

```
 _____                               _
|  ___|__  ___ ___  ___ ___  _ __ __| |
| |_ / _ \/ __/ __|/ __/ _ \| '__/ _` |
|  _| (_) \__ \__ \ (_| (_) | | | (_| |
|_|  \___/|___/___/\___\___/|_|  \__,_|

Fosscord Injector v0.5 by mugman
```
# Usage
- Install Python 3
- Run injector.py

1. Fosscord Instance IP
	```
	Enter your Fosscord instance IP (e.x. '127.0.0.1:3001', 'myvps.com:3001', or 'app.fosscord.com'): 
	```
	Type in your Fosscord instance's IP and Port (`[ip]:[port]`). If the port is 80 or 443, you do not need to put it. (`[ip]`)
2. HTTPS
	```
	Does the instance support HTTPS? (Does it have a valid HTTP cert?) [yes,no]: 
	```
	If the Fosscord Instance port is 443 (and the browser shows a secure connection), then enter yes. Otherwise, enter no.
3. Discord Version
	```
    1 - Discord Stable
    2 - Discord PTB
    3 - Discord Canary
    4. Discord Development
    Choose your version [1,2,3,4]: 
    ```
    Choose your Discord Version. If you do not know, you can find out how to get it [here](https://support.discord.com/hc/en-us/articles/360052735334-How-do-I-find-my-client-info).
4. Erlpack
	```
	[Confirmation] Fosscord instances do not work with erlpack. Disable erlpack [y/n]?
	```
	Unless you have a reason for keeping erlpack support, just put `yes`.
6. Complete!
    You can now restart your Discord client and it'll use Fosscord instead of Discord. Enjoy!
    For any problems, head to [Troubleshooting](#troubleshooting).

# Troubleshooting

Create an issue on this Github repo or ping mugman in the Fosscord server for any issues. Please redact any personal information if posting logs or errors.
