"""
	The Fosscord Injector injects json into a Discord client's settings file,
	so it may connect to a Fosscord instance.
	Copyright (C) 2022 mugman174

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


import sys
import os
import json
import re

DRY_RUN = bool(os.environ.get("DRY_RUN", False))
ENDPOINT_URL = os.environ.get("FOSSCORD_ENDPOINT", None)
HTTPS_SUPPORT = os.environ.get("FOSSCORD_HTTPS", None)
API_VERSION = os.environ.get("FOSSCORD_API_VER", "v9")

print(
	f"""
 _____                               _
|  ___|__  ___ ___  ___ ___  _ __ __| |
| |_ / _ \/ __/ __|/ __/ _ \| '__/ _` |
|  _| (_) \__ \__ \ (_| (_) | | | (_| |
|_|  \___/|___/___/\___\___/|_|  \__,_|


Fosscord Injector v1 by mugman

{"[Dry Run]" if DRY_RUN else ''}
"""
)


end_url = ENDPOINT_URL or input(
	"Enter your Fosscord instance IP (e.x. '127.0.0.1:3001', 'myvps.com:3001', or 'app.fosscord.com'): "
)
https = HTTPS_SUPPORT or input(
	"Does the instance support HTTPS? (Does it have a valid HTTP cert?) [yes,no]: "
)
https = "https" if (https == "yes") else "http"
print(
	"1 - Discord Stable\n2 - Discord PTB\n3 - Discord Canary\n4 - Discord Development"
)
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
	raise FileNotFoundError(
		"The Discord version you have inputted is invalid, or your config directory is different from the default. Please report this problem to mugman#5453 on Discord."
	)

print("Reading from current settings file...")
try:
    with open("settings.json") as settings_file:
	    settings = json.load(settings_file)
except FileNotFoundError:
    print("No settings file found. Continuing...")
    settings = {}

inject_json = {
	"API_ENDPOINT": f"{https}://{end_url}/api/{API_VERSION}",
	"WEBAPP_ENDPOINT": f"{https}://{end_url}",
	"UPDATE_ENDPOINT": "https://discord.com/api",
	"NEW_UPDATE_ENDPOINT": "https://discord.com/api",
}

settings |= inject_json

if not DRY_RUN:
	print("Writing Files...")
	with open("settings.json", "w") as settings_file:
		json.dump(settings, settings_file)
	print("Some Fosscord instances do not have '@yukikaze-bot/erlpack' installed.\nIf you know the instance you are using has erlpack, you can safely enter 'no'.\nOtherwise, you should probably enter 'y'.")
	version_reg = re.compile("\d\.\d\.[0-9]+")
	ver_search = version_reg.search(" ".join(os.listdir()))
	confirm = input(
		"[Confirmation] Disable erlpack [y/n]? "
	)
	if not ver_search:
		if not ver_search: print(
			"You will need to disable erlpack manually from your Discord client for this to work."
		)
	elif "y" in confirm:
		print("Disabling erlpack...")
		ver = ver_search[0]
		dir = os.path.join(ver, "modules/discord_erlpack")
		os.chdir(dir)
		manifest_json = {"files": ["index.js", "manifest.json"]}
		with open("manifest.json", "w") as manifest_file:
			json.dump(manifest_json, manifest_file)
		with open("index.js", "w") as erlpack:
			erlpack.write("module.exports = {e.pack: (e) => e}")
	print(f"Injected! Please restart your Discord client ({version}), and enjoy!")

else:
	print(f"Dry Run Complete. Settings: {settings}")
