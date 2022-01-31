# Telepurger

**Telepurger** is the Python script for deleting all your messages in **Telegram**.

Telegram Auth is based on [Telethon](https://github.com/LonamiWebs/Telethon) library.


## Configuration

<ol>
<li>Open <a>my.telegram.org/apps</a> and create your <b>App configuration</b>
<img src="https://user-images.githubusercontent.com/83237609/151797417-8f303ad5-7909-4e7a-a1b7-e3911c409c75.png" alt=""/>
</li>
<li>
Then fill the <i>configuration info</i> <i>(<b>api_id</b>, <b>api_hash</b>)</i> in <b>main.py</b> with your data
<img width="468" alt="Screenshot 2022-01-31 at 15 06 36" src="https://user-images.githubusercontent.com/83237609/151797983-11ea5aa4-c2e4-4aae-8934-b8b5d7f100ef.png">
</li>
<li>
Install <b>Python dependences</b> from <i><b>requirements.txt</b></i>:
</li>
<code>pip3 install -r requirements.txt</code>
<li>Run <b>main.py</b>:<br>
<code>python3 main.py</code>
</li>
<li>Authorize using your phone number</li>
</ol>
<img width="612" alt="purrr" src="https://user-images.githubusercontent.com/83237609/151797789-4d74cc7e-f3bb-4bf1-b7bd-937faf4227ee.png">

## Notes
Сurrently, this script only deletes messages sent by you. Initially, I conceived it as a tool for quick deleting messages in public chats.

