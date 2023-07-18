import os
import subprocess
import openai
import json
import requests
import base64
import random
import io
from PIL import Image
import argparse
from bs4 import BeautifulSoup

def create_weapon(api_key="", weapon_idea="", class_="", slot="", level="", type="", attributes="", icon="", rarity="", power=""):

    log = []

    if api_key == "" or api_key == "":
        if os.path.isfile("api_key.txt"):
            with open("api_key.txt", "r") as file:
                txt_api_key = file.read().strip()
                # Use the api_key variable to access the datas
                api_key = txt_api_key
                log.append("API Key Has Been Provided Through The Last Saved API Key (api_key.txt file.)")
        else:
            log.append("Please provide an API Key. For instructions on how to get an API key, go to my") 
            log.append("GitHub repo at https://github.com/FatalError418/TF2-AI-Generator#how-to-get-an-openai-api-key.")
            return "\n".join(log)

    openai.api_key = api_key

    def getRequirments():
        string = ""

        if weapon_idea:
            string += f"You must use the following weapon idea: {weapon_idea}. "

        if class_:
            string += f"You must use the following class: {class_}. "
        elif (weapon_idea == "" or weapon_idea == None) and (type == "" or type == None):
            string += f"Use the randomly picked class " + random.choice(["Scout", "Soldier", "Pyro", "Demoman", "Heavy", "Engineer", "Medic", "Sniper", "Spy"])

        if slot:
            string += f"You must use the following slot: {slot}. Don't say it's a secondary weapon when it acts like a primary one, instead make it act like a secondary weapon (assuming it is set as secondary)."
        elif (weapon_idea == "" or weapon_idea == None) and (type == "" or type == None):
            string += f"Use the randomly picked slot " + random.choice(["Primary", "Secondary", "Melee"]) + ". Don't say it's a secondary weapon when it acts like a primary one, instead make it act like a secondary weapon (assuming it is set as secondary)."

        if level:
            string += f"You must use the following level: {level}. "

        if type:
            string += f"You must use the following weapon type: {type}. "

        if attributes:
            string += f"You must use the following attributes: {attributes}. "

        if icon:
            string += f"You must use the following icon: {icon}. "

        if rarity:
            string += f"You must use the following rarity: {rarity}. "

        if power:
            string += f"The weapon tier and power must be: {power}. "

        return string

    prompt = '''
    Generate a new fictional TF2 weapon card that is unique with an interesting idea. You should format your output in json format. Here is an example on how to do it, but do not however directly copy this.
    {
      "weapon_idea": "A shotgun for the engineer which repairs you and all buildings by amount of damage dealt on hit, but buildings cost extra metal to repair and you have less max health."
      "classes": ["Engineer"],
      "slot": "Primary",
      "name": "The Rampager",
      "level": "Level 25 Shotgun",
      "attributes": {
        "0": {
            "name": "On Hit: Damage dealt is returned as health and any extra health evenly distributed to all buildings currently built",
            "type": "positive"
        },
        "1": {
            "name": "+33% clip size",
            type: "positive"
        },
        "2": {
            "name": "+25% metal cost to repair buildings"
            "type": "negative"
        },
        "3": {
            "name": "50% slower repair speed",
            "type": "negative"
        },
        "4": {
            "name": "25 less max health",
            "type": "negative"
        },
        "5": {
            "name": "Our previous motto was 'Shoot to kill'. Now it's 'Shoot to survive'.",
            "type": "neutral"
        }
      },
      "icon": "Frontier_Justice",
      "rarity": "Unique"
    }
    Make sure to stick to the format, don't stray from it.
    Remember to not use the attribute example templates I provided in the above formatting tutorial, those are just examples on what you can do.
    Try to use numbers not something general like instead of 'Lower Max Health' it'd be '-10 max health'. It should be very specific. Also, instead of just '50% slower movement speed' go '50% slower
    movement speed while active', aka be REALLY specific. 
    Don't just recreate valve's weapon abilities. 
    Also, instead of going '-20% damage to players' you might go '20% less damage to players'. Everything should start with a capital letter except for the attribute types, those MUST be lowercase.
    So instead of saying 'dealing extreme damage' you might go 'dealing 250% more damage'. Do not ever be vauge.
    Make the weapon decently new, by that I mean it spices up the gameplay a little with it, so not just a fancy reskin.
    Use neutral attributes to explain what the weapon does in more detail.
    For the icon, don't go 'Southern Hospitality' or 'tf_sothern_hospitality', use 'Southern_Hospititality'.
    Don't go 'Positive' or 'Negative' or 'Neutral', instead go 'positive' or 'negative' or 'neutral'.
    Make sure to use uncommon items, but still ones that actually exist!
    If the slot is a secondary weapon, MAKE SURE TO ACTUALLY MAKE IT A SECONDARY WEAPON. It should not ever be like a primary weapon if it is a secondary.
    On the example, that final neutral one is a description of how to use it, what it can be used for, or just a funny joke. For example, another one for heavy gloves which deal crits to airborn enemies could be: 'With these boxing gloves you can finally pop helium balloons. DISCLAIMER: Popping said balance may have some legal implications, such as accusation of murder.'
    Be unqiue, don't copy what I did in my example.
    You should only output the JSON.
    Make sure this is competely unique, therefore don't copy already existing weapons. Make sure to never stray from json formatting. Here is an example:

    Now create a weapon. Some things to note: ''' + getRequirments() + '''Remember to be extremely clear with the attributes.'''

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        messages=[
            {
                "role": "system",
                "content": "You are a tf2 weapon generator which can generate unique TF2 weapons with expertly crafted Attributes with fine-tuned numbers.",
            },
            {
                "role": "user", 
                "content": prompt
            },
        ],
    )

    data = json.loads(response.choices[0].message.content)

    def getIconFromItemName(item_name):
        url = "https://wiki.teamfortress.com/wiki/File:Item_icon_" + item_name.replace(" ", "_") + ".png"
        response = requests.get(url)
        
        # Check if the response was successful
        if response.status_code != 200:
            log.append(f"Failed to retrieve page: {response.status_code}. Using default icon.")

            url = "https://wiki.teamfortress.com/wiki/File:Item_icon_Counterfeit_Billycock.png"
            response = requests.get(url)

        # Parse the HTML of the page
        soup = BeautifulSoup(response.content, "html.parser")

        # Try to find the image URL.
        img_url = soup.find("div", {"class": "fullImageLink"}).find("a").get("href")

        # Add the base URL if the image URL is relative
        if img_url.startswith("/"):
            img_url = "https://wiki.teamfortress.com" + img_url

        response = requests.get(img_url)

        # Check if the response was successful
        if response.status_code != 200:
            log.append(f"Failed to retrieve image: {response.status_code}")
            return None

        img = Image.open(io.BytesIO(response.content))

        buffered = io.BytesIO()
        img.save(buffered, format="PNG")

        img_str = base64.b64encode(buffered.getvalue())
        img_str = img_str.decode('utf-8')

        return img_str


    def getHexFromRarityString(rarity):
        if rarity == "Unique":
            return "#FFD700"
        if rarity == "Vintage":
            return "#474C49"
        if rarity == "Normal":
            return "#B2B2B2"
        if rarity == "Genuine":
            return "#4D7455"
        if rarity == "Strange":
            return "#CF5220"
        if rarity == "Unusual":
            return "#8650AC"
        else:
            return "#FFD700"

    def canClassUseWeapon(class_name):
        for avaliable_class_name in data["classes"]:
            if class_name == avaliable_class_name:
                return True
            
        return False

    new_card_data = '''
    {
        "version": 1,
        "image": "data:image/png;base64,''' + getIconFromItemName(data["icon"]) + '''",
        "name": "''' + data["name"] + '''",
        "rarity": "''' + getHexFromRarityString(data["rarity"]) + '''",
        "level": "''' + data["level"] + ''' (''' + data["slot"] + ''')",
        "limitedEdition": false,
        "strangeParts": {},
        "showStrangeCounter": false,
        "isFestivized": false,
        "showUnusualEffect": false,
        "unusualEffect": "",
        "halloweenRestricted": false,
        "pyrovisionRestricted": false,
        "isLimitedConsumable": false,
        "consumableCharges": "",
        "restrictions": {
            "active": false,
            "reason": "",
            "value": "Not tradeable or Marketable"
        },
        "gift": {
            "active": false,
            "giver": "",
            "date": ""
        },
        "classList": {
            "scout": ''' + str(canClassUseWeapon("Scout")).lower() + ''',
            "soldier": ''' + str(canClassUseWeapon("Soldier")).lower() + ''',
            "pyro": ''' + str(canClassUseWeapon("Pyro")).lower() + ''',
            "demoman": ''' + str(canClassUseWeapon("Demoman")).lower() + ''',
            "heavy": ''' + str(canClassUseWeapon("Heavy")).lower() + ''',
            "engineer": ''' + str(canClassUseWeapon("Engineer")).lower() + ''',
            "medic": ''' + str(canClassUseWeapon("Medic")).lower() + ''',
            "sniper": ''' + str(canClassUseWeapon("Sniper")).lower() + ''',
            "spy": ''' + str(canClassUseWeapon("Spy")).lower() + '''
        },
        "attributes": ''' + json.dumps(data["attributes"]) + ''',
        "itemSet": {
            "active": false,
            "name": "Destroys",
            "bonus": {
                "active": false,
                "name": "",
                "completed": false
            },
            "list": {
                "0": {
                    "name": "Item set member name",
                    "completed": false
                }
            }
        },
        "credits": "Automatically Generated By ChatGPT"
    }
    '''

    # Get the current directory
    current_dir = os.getcwd()

    # Create a new folder named "weaponcards" if it doesn't exist
    folder_path = os.path.join(current_dir, "weaponcards")
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    # Create the file path for the new .weaponcard file
    file_path = os.path.join(folder_path, data["name"] + ".weaponcard")

    # Write the weapon card data to the .weaponcard file
    with open(file_path, "w") as file:
        file.write(new_card_data)

    log.append("Weapon generated successfully.")
    log.append(f"Go to '{os.getcwd()}.weaponcard'")
    log.append("to access the newly created .weaponcard.")
    log.append("You can then tap 'Load' in the TF2 weapon card creator and open the newly created file!")
    subprocess.Popen(f'explorer "{os.getcwd()}\\weaponcards"')

    return "\n".join(log)
