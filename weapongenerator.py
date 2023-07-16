import os
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

    log = ""

    if api_key == "" or api_key == "":
        log += "Please provide an API Key. For instructions on how to get an API key, go to my\nGitHub repo at https://github.com/FatalError418/TF2-Auto-Generator and scroll down to the\n'How to get an OpenAI API Key' section."
        return log

    openai.api_key = api_key

    def getRequirments():
        string = ""

        if weapon_idea:
            string += f"You must use the following weapon idea: {weapon_idea}. "

        if class_:
            string += f"You must use the following class: {class_}. "
        elif (weapon_idea == "" or weapon_idea == None) and (type == "" or type == None):
            string += f"Use the randomly picked class " + random.choice(["Scout", "Soldier", "Pyro", "Demoman", "Heavy", "Engineer", "Medic", "Sniper", "Spy"]) + ", or one that fits with other metioned requirements. "

        if slot:
            string += f"You must use the following slot: {slot}. Don't say it's a secondary weapon when it acts like a primary one, instead make it act like a secondary weapon (assuming it is set as secondary)."
        elif (weapon_idea == "" or weapon_idea == None) and (type == "" or type == None):
            string += f"Use the randomly picked slot " + random.choice(["Primary", "Secondary", "Melee"]) + ", or one that fits with other metioned requirements. Don't say it's a secondary weapon when it acts like a primary one, instead make it act like a secondary weapon (assuming it is set as secondary)."

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
    Generate a new TF2 weapon that is unique with an interesting idea with this format:
    {
      "weapon_idea": "Weapon idea, for example 'a medi gun which damages the medic when healing in exchange for a much higher heal speed and faster ubercharge.'. Don't use that exactly, however."
      "classes": ["Class 1", "Optional Class 2, only if both classes can normally use the weapon type."],
      "slot": "Item slot, so primary, secondary, or melee.",
      "name": "The name of the item",
      "level": "Level x Item Type (Slot), for example: 'Level 25 Medi Gun (Primary)'.",
      "attributes": {
        "0": {
            "name": "This is an example of an attribute. You can haved neutral, positive, and negative attributes. 
            TIP: You can use neutral attributes to describe abilities, 
            the item, or how to use it. If there is a clear positive or negative side to an attribute, 
            don't label it as neutral. Have as many of these attributes as you want.",
            "type": "type"
        }
      },
      "icon": "Already existing weapon. This will go into the file, so for example don't go Medi Gun or tf_medi_gun do Medi_Gun.",
      "rarity": "Item rarity, for example Normal (for stock items), Unique, Genuine, Strange, Vintage, Unusual, etc. 
      If it's something other than unique, add the rarity before the item name, for example 'Strange Item Name'",
    }
    Make sure to stick to the format, don't stray from it. Generate a new weapon. Attributes should order: Positive, then negative, then neutral. From top to bottom in that order. 
    Remember to not use the attribute example templates I provided in the above formatting tutorial, those are just examples on what you can do.
    You don't always need to use neutral Attributes, but do use neutral descriptions from time to time (describing something you do with it, or a little joke: NOT A CATCHLINE JOKE, HOWEVER!!!, also only do a description / joke if it really works well and is not cringey. Only use a joke if it won't make people cringe.).
    Try to use numbers not something general like instead of 'Lower Max Health' it'd be '-10 max health'. It should be very specific. Also, instead of just '50% slower movement speed' go '50% slower
    movement speed while active', aka be REALLY specific. 
    Don't just recreate valve's weapon abilities. 
    Also, instead of going '-20% damage to players' you might go '20% less damage to players'. Everything should start with a capital letter except for the attribute types, those MUST be lowercase.
    ALSO, only use " for the formatting, so for example in the attributes DO NOT do 'attributes', do "attributes". And inside (for example the name value), use '. For example don't go 'name': 'Example "item"', do "name": "Example 'item'"
    If you need a small negative, use 'No random critical hits'.
    Make the weapon decently new, by that I mean it spices up the gameplay a little with it, so not just a fancy reskin.
    Make sure this is competely unique, therefore don't copy already existing weapons. Make sure to never stray from json formatting. Here is an example:

    {
      "weapon_idea": "A wrench which generates metal when hitting enemies, but buildings have less health and can have more status effects inflicted upon them."
      "classes": ["Engineer"],
      "slot": "Melee",
      "name": "Strange Frankinwrench",
      "level": "Level 25 Nightmare Wrench (Melee)",
      "attributes": {
        "0": {
            "name": "All damage dealt (including turrets) is converted to metal",
            "type": "positive"
        }
        "1": {
            "name": "Buildings can have bleed and other similar status effects inflicted upon them",
            "type": "negative"
        }
        "2": {
            "name": "Buildings have 33% less health",
            "type": "negative"
        }
        "3": {
            "name": "Who needs metal, electronic turrets when you have sentient living flesh abominations stitched together from your enemies flesh?",
            "type": "neutral"
        }
      },
      "icon": "Southern_Hospitality",
      "rarity": "Strange"
    }

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
            log += f"Failed to retrieve page: {response.status_code}. Using default icon."

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
            log += f"Failed to retrieve image: {response.status_code}"
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
        "level": "''' + data["level"] + '''",
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

    log += "Weapon generated successfully."

    return log