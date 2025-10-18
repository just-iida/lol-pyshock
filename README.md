# ⚡ LoL-PyShock
LoL-PyShock currently serves one function: shocking you when you die in League of Legends. It is the successor of [LoL-PiShock](https://github.com/just-iida/lol-pishock/), this time with a GUI and a cleaner codebase with better comments.
<br></br>
I am still busy with my studies and cannot promise consistent updates, if something breaks I can probably have the time to fix it, but beyond that it's up to my schedule and free time.
<br></br>
It has only a few improvements on the previous version:
- Ease of use
 - Operation load can be tested and changed mid-game 


It does not improve on the following features:
- API, it still uses the legacy PiShock API.
###### ~~I've gotten better at programming since the initial version, but I've not had the opportunity to work with the new PiShock APIs, the legacy still works, so I found it redundant to try and "fix" what already works. Feel free to do a pull request if you wish to update it yourself.~~
‼️ During the making of this, someone has made an update on the previous version, I'll test it and see if it can also be implemented here with ease.
- Amount of features, it still only detects deaths, however if someone wishes for more use-cases, pull requests are open and feature suggestion issues can be created.


### ‼️ Disclaimer
LoL-PyShock is not responsible for any harm caused by misuse of the shock collar sold along with the PiShock device. We do not recommend putting any kind of electrical device near the heart or use if you have a heart condition. Shock collars are not meant for use on humans and can cause serious injury including cardiac events.
### ☕ Buy me coffee
https://ko-fi.com/mooniebuns
Giving money is completely optional and has the only purpose of motivating me to keep creating more.
## Installation and setup
**LoL-PyShock was developed using Python 3.12, there is no official support for other versions.**
### Requirements
* [Python 3.12](https://www.python.org/)
### Installation
* ``git clone https://github.com/just-iida/lol-pyshock.git``
* ``pip install -r requirements.txt``
### Setup
* Run ``py .\lol_pyshock.py``
* Generate an API Key at https://pishock.com/#/account
* Get the device code at https://pishock.com/#/control, by clicking Share on your specific shocker and clicking **+ CODE**
* Fill in your username, API Key and Device Code.
* Click save config.
* Click Test(Beep), if your device lets out a beep, you have configured it successfully.
* Alternatively, set up an Operation and use the Test Current.
* Press Start to have the app detect the game.

## Future Plans
* ❓ Use [Python-PiShock](https://python-pishock.readthedocs.io/) API instead of PiShock API (Need to test first, might make another branch for it.)
* ❓ Support for more than just shocking you on death.
* ❓ Support for multiple shockers.

# Legal
LoL-PyShock was created under Riot Games' "Legal Jibber Jabber" policy using assets owned by Riot Games.  Riot Games does not endorse or sponsor this project.
LoL-PyShock was created using the PiShock API. PiShock does not endorse or sponsor this project.
