# The TF2 AI Generator
Using ChatGPT and some Python code, I've created this TF2 AI generator, which can currently generate a new TF2 weapon card. It's a bit harder to set up than most, but I can assure you it'll be worth it. Scroll down to the setup section for setup instructions. Currently, it can only generate new weapon cards, but in the future, it'll be able to generate more, so keep an eye out!

# Examples
If you don't believe how good this is, here are some examples of the weapon generation (these aren't cherry-picked; I just used the first 5 weapon cards it generated): <br />
<img src="https://github.com/FatalError418/TF2-AI-Generator/assets/139549531/29dce63f-49f9-4aa5-a2fa-7bf092ce471c" width="300"/> <br />
<img src="https://github.com/FatalError418/TF2-AI-Generator/assets/139549531/5deff458-d79c-4315-85ae-4a73a33340e9" width="300"/> <br />
<img src="https://github.com/FatalError418/TF2-AI-Generator/assets/139549531/b5e08907-67d8-4aa0-82bd-85e37114bd9e" width="300"/> <br />
<img src="https://github.com/FatalError418/TF2-AI-Generator/assets/139549531/049d760b-0ca8-4209-9f60-81aea1216ddb" width="300"/> <br />
<img src="https://github.com/FatalError418/TF2-AI-Generator/assets/139549531/737e84ba-061c-4bf4-ae89-7c08d7c26aa9" width="300"/> <br />

# Upcoming Updates
- Patch Notes Generator
- GPT-4 (a much better version of ChatGPT; GPT-4 is currently in closed beta but will be publicly available later this month)
- AI-Generated Icons
- Map Idea Generator
- Mac and Linux Support

# Setup
To use the generator, there are two ways to install it. It is recommended that you use the auto-setup, as it is much simpler, but if you prefer, you can set it up manually.

### Automatic Setup (Recommended)
To automatically set up the generator, go [here](https://github.com/FatalError418/TF2-AI-Generator/releases) and download the latest version. Next, run the exe file and go through the setup. You can leave all the settings at default. The generator should be running, and you can go to the section below and get an OpenAI API Key.

### Manual Setup (Not Recommended)
This is quite complicated; I'll go through everything quite quickly. First, scroll up and tap on 'Code'. Press download zip and extract it. Double-click 'compile.bat', tap 'More Info;, then 'Run Anyway', then wait for it to finish. You can now run the generator by going into the 'compile' folder and running 'app.exe'. If you want to generate a setup file, right-click on 'setup_script' and press compile, then go into the newly created 'setup' folder, and you'll get an exe setup file (the same file that can be downloaded in the automatic setup tutorial). Run 'app.exe'. You now need an OpenAI API Key, so go to the section below to get one.

# How to get an OpenAI API Key
To use this tool, you'll need an OpenAI API Key (OpenAI owns ChatGPT). To do that, go [here](https://platform.openai.com/account/api-keys), and assuming you don't have an account (if you do, just log in), tap 'Sign Up'. Enter your email address, enter a password (must be over 8 characters), verify the email, enter your name and birthday (you can use an alias/fake details if you want), and then enter your phone number, which is used to verify you are a human. Once that is done, click on 'Create new secret key'. Enter the key name, for example, 'tf-ai-generator'. Next, copy the key and paste it into a new Notepad file. Save the file as 'api_key' and place it in the TF2 AI Generator folder, by default 'C:\\Users\\{user}\\AppData\\Local\\Programs\\TF2 AI Generator' (or 'TF2-AI-Generator-main\\compile' file if you did manual setup). Make sure to replace {user} with your actual username. This isn't required, as you can just paste in the key once the app has started by putting it in the API Key field, but by placing your key in that file, you don't need to keep pasting the key in every time as the script accesses the file and grabs the API key from there.

# Usage
You've installed the generator, but how do you use it?

### Weapon Generation
To generate a weapon, launch the generator and go to the Weapon Generation tab. Make sure you supply a valid API key in the API key tab or inside the api_key.txt file as seen in the 'How to get an OpenAI API Key' section. You can now click on 'Generate Weapon Card'. This will generate a new .weaponcard file. By default, it is located in 'C:\\Users\\{user}\\AppData\\Local\\Programs\\TF2 AI Generator\\weaponcards' (or 'TF2-AI-Generator-main\\compile\\weaponcards' file if you did manual setup), with {user} being your username. You now have this new file, but what do you do with it? Well, to start, go to [the tf2 weapon card creator website](https://gamepro5.com/programs/tf2_weapon_card_creator/) and scroll down to the 'Load' button. Click on it, and go to the above mentioned folder. You can then sort by date, and select the latest weapon card to get the newly generated weapon. You should see a weapon card appear. If not, try regenerating the weapon card. You can also modify the generated weapon card if you want. You can also set the values in the generator to whatever you want. You can refer to the tooltips on what the values mean.

# Troubleshooting
If you run into a problem, first go through the list of steps below before reporting an issue:
1. Remember that this can only run on Windows for the time being!
2. Check for a valid OpenAI API Key (you can get one by following the 'How to get an OpenAI API Key' section)
3. Regenerating the weapon a few times (sometimes the AI fails generating it, if so, try again)
4. Checking the values you set (if they aren't clear or strangely worded it may fail)
5. Checking if you still have API credits left (if you don't have any left, you can buy some more at [OpenAI](https://platform.openai.com)
6. Restarting the app
7. Restarting your computer
   
If all those steps fail, report an issue and I'll try to fix it quickly.
