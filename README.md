# The TF2 AI Generator
Using ChatGPT and some Python code, I've created this TF2 AI generator, which can currently generate a new TF2 weapon card. It's a bit harder to set up than most, but I can assure you it'll be worth it. Scroll down to the setup section for setup instructions. Currently, it can only generate new weapon cards, but in the future, it'll be able to generate more, so keep an eye out!

# Examples
If you don't believe how good this is, here are some examples of the weapon generation (these aren't cherry-picked; I just used the first 5 weapon cards it generated): <br />
<img src="https://github.com/FatalError418/TF2-Auto-Generation/assets/139549531/1942f080-9f01-4e0b-9c23-8dbe5b27d012" width="400"/> <br />
<img src="https://github.com/FatalError418/TF2-Auto-Generation/assets/139549531/34ae155f-c418-4def-8aef-9fdccdfc13e4" width="400"/> <br />
<img src="https://github.com/FatalError418/TF2-Auto-Generation/assets/139549531/9c5be52d-6f5d-41d3-bf85-d8fc71f799f1" width="400"/> <br />
<img src="https://github.com/FatalError418/TF2-Auto-Generation/assets/139549531/65e7a6b6-90db-4cab-b7e9-91c80186ac7e" width="400"/> <br />
<img src="https://github.com/FatalError418/TF2-Auto-Generation/assets/139549531/51572c94-e077-47aa-80bc-a2822cc69dfa" width="400"/> <br />

# Upcoming Updates
- Patch Notes Generator
- GPT-4 (a much better version of ChatGPT; GPT-4 is currently in closed beta but will be publicly available later this month)
- AI-Generated Icons
- Map Idea Generator

# Setup
To use the generator, there are two ways to install it. It is recommended that you use the auto-setup, as it is much simpler, but if you prefer, you can set it up manually.

## Automatic Setup (Recommended)
To automatically set up the generator, go here and download the latest version. Next, run the exe file and go through the setup. You can leave all the settings at default. The generator should be running, and you can go to the section below and get an OpenAI API Key.

## Manual Setup (Not Recommended)
This is quite complicated; I'll go through everything quite quickly. First, scroll up and tap on 'Code'. Press download zip and extract it. Double-click 'compile.bat', tap 'More Info;, then 'Run Anyway', then wait for it to finish. You can now run the generator by going into the 'compile' folder and running 'app.exe'. If you want to generate a setup file, right-click on 'setup_script' and press compile, then go into the newly created 'setup' folder, and you'll get an exe setup file (the same file that can be downloaded in the automatic setup tutorial). Run 'app.exe'. You now need an OpenAI API Key, so go to the section below to get one.

# How to get an OpenAI API Key
To use this tool, you'll need an OpenAI API Key (OpenAI owns ChatGPT). To do that, go [here](https://platform.openai.com/account/api-keys), and assuming you don't have an account (if you do, just log in), tap 'Sign Up'. Enter your email address, enter a password (must be over 8 characters), verify the email, enter your name and birthday (you can use an alias/fake details if you want), and then enter your phone number, which is used to verify you are a human. Once that is done, click on 'Create new secret key'. Enter the key name, for example, 'tf-ai-generator'. Next, copy the key and paste it into a new Notepad file. Save the file as 'api_key' and place it in the TF2 AI Generator folder, by default 'C:\\Users\\{user}\\AppData\\Local\\Programs\\TF2 AI Generator' (or 'TF2-AI-Generator-main\\compile' file if you did manual setup). Make sure to replace {user} with your actual username. This isn't required, as you can just paste in the key once the app has started by putting it in the API Key field, but by placing your key in that file, you don't need to keep pasting the key in every time as the script accesses the file and grabs the API key from there.

# Usage
You've installed the generator, but how do you use it?

## Weapon Generation
To generate a weapon, launch the generator and go to the Weapon Generation tab. Make sure you supply a valid API key in the API key tab or inside the api_key.txt file as seen in the 'How to get an OpenAI API Key' section. You can now click on 'Generate Weapon Card'. This will generate a new .weaponcard file
