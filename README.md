# DiscordServerJoiner
## This Github is not my Main Account

If you see english spelling mistakes in this readme, commit/pull request rather opening issues.


Big Thanks to those guys who created that hacptcha solver.


### How to setup this bot ?

Open this link to download Models for hcaptcha Solver.
```
https://github.com/QIN2DIM/hcaptcha-challenger/releases/tag/model
```
Download All Models, then copy and paste all these models in 'models' Folder. Where is Models Folder?? I cant See, 'create new folder in DiscordServerJoiner'

You must have pip installed on your Windows/Linux
#### Command 1:
```
pip install -r requirements.txt
```
Requirements are only installed for the hcaptcha solver.

#### Now Install Stuff for the Script.
  Add servers to 1.txt e.g discord.com/invite/pepeSwagXDancingBlob

### How to open Chrome Borwser in debugger mode. So, you can login your account and sync with script/bot.
1. Open Notepad and paste the following

#### Linux:
```
ECHO ON
cd /opt/google/chrome/
google-chrome --remote-debugging-port=8989 --user-data-dir="/home/ubuntu/Desktop/DiscordProfile"
```

#### Windows:
```
ECHO ON
cd C:\Program Files\Google\Chrome\Application\
chrome.exe --remote-debugging-port=8989 --user-data-dir="F:\chromeProfile1"
```

The above are just examples. I dont know where you installed Chrome, you gotta find that on your own. 
Change Chrome Profle location to the one of your choice.

##### Save the notepad as runme.bat or runme.
For linux users, you know how to run it lol --> ./runme in ternminal <Enter key>.
For windows users,  right click on rume.bat and run as adminsitrator. 
Hopefully, Chrome Browser will open.

Now Login your discord account, 

After login, DO NOT CLOSE CHROME.

Run the script. 

Any issues, Try Stackoverflow.

if solution not in stackoverflow:
  Create Issue in github repository


## DiscordServerJoiner.py --> If you wish to join specific number of servers
Line 257:  If you want to add specific number of server e.g added 60 but got error. 
Wanna add 40 but dont want to monitor the bot.
So, this line helps you in specifying number of servers to be Joined.
Replace that 100 by the number of servers you wanna join. e.g 10

## LowMembers.txt
This file stores discord links with low members e.g members below 250
or Link was invalid maybe.

```
Edit Line 85: If you want to join servers with specific number of members. Otherwise, leave replace 250 by 0 if you want to join server by any number of members.
```
