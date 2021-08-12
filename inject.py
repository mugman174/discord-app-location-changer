"""
    The Fosscord Injector injects json into a Discord client's settings file,
    so it may connect to a Fosscord instance.
    Copyright (C) 2021  mugman174

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import sys, os, json


try:
	DRY_RUN = bool(os.environ["DRY_RUN"])
except KeyError:
	DRY_RUN = False

print(f"""
 _____                               _
|  ___|__  ___ ___  ___ ___  _ __ __| |
| |_ / _ \/ __/ __|/ __/ _ \| '__/ _` |
|  _| (_) \__ \__ \ (_| (_) | | | (_| |
|_|  \___/|___/___/\___\___/|_|  \__,_|

Fosscord Injector v0.0.1 by mugman

{"[Dry Run]" if DRY_RUN else ''}
""")


end_url = input("Enter your Fosscord instance IP (e.x. '127.0.0.1:3001', 'myvps.com:3001', or 'app.fosscord.com'): ")
https = input("Does the instance support HTTPS? (Does it have a valid HTTP cert?) [yes,no]: ")
https = 'https' if https else 'http'
print("1 - Discord Stable\n2 - Discord PTB\n3 - Discord Canary\n4. Discord Development")
ver_in = int(input("Choose your version [1,2,3,4]: "))


if ver_in == 1:
	version = "discord"
elif ver_in == 2:
	version = "discordptb"
elif ver_in == 3:
	version = "discordcanary"
elif ver_in == 4:
	version = "discorddevelopment"
else:
	raise Exception("Invalid Choice/Number. Choose from the options [1,2,3,4].")

os_ver = sys.platform
if "linux" in os_ver:
	confpath = f"""{os.environ["HOME"]}/.config/{version}/"""
elif "win32" in os_ver:
	confpath = f"""{os.environ["APPDATA"]}\\{version}"""
elif "darwin" in os_ver:
	confpath = f"""{os.environ["HOME"]}/Library/Application Support/{version}/"""
else:
	raise Exception(f"{os_ver} is not a supported platform.")
try:
	os.chdir(confpath)
except FileNotFoundError:
	raise FileNotFoundError("The Discord version you have inputted is invalid, or your config directory is different from the default. Please report this problem to mugman#5453 on Discord.")

inject_json = {"API_ENDPOINT": f"{https}://{end_url}/api/v8","WEBAPP_ENDPOINT": f"{https}://{end_url}","UPDATE_ENDPOINT": "https://updates.goosemod.com/goosemod","NEW_UPDATE_ENDPOINT": "https://updates.goosemod.com/goosemod/"}

if not DRY_RUN:
	print("Writing Files...")
	with open("settings.json", "w") as settings_file:
		json.dump(inject_json, settings_file)
		print(f"Injected! Please restart your Discord client ({version}), and enjoy!")
else:
	print("Dry Run Complete.")
