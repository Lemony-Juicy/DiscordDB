# DiscordDB
Simple package for storing and retrieving data from discord using SQL-like querying. DiscordBD was inspired by the pre-existing DiscordDatabase package, However it lacked the functionalities to retrieve data in a similar fashion to SQL, where multiple items could be selected through filtering. This package allows for storing atomic level data and quicker querying.

## Setting up
DiscordDB works by creating an object from the DataBase class found in the package. The DataBase class inherits from commands.Bot class in the [discord.py](https://pypi.org/project/discord.py/) API Wrapper. 

After installing the [discord.py](https://pypi.org/project/discord.py/) python package by `pip install discord.py` in command prompt:  
- Create 
- Ensure you have the right version of **chrome driver installed** for the Google Chrome version you have, and that it is in the same folder as the Bot.py file.  
- Ensure you have python 3.7+ and the **selenium package installed**. To install selenium enter `pip install selenium` in Command Prompt.  
  
> **Note**  
> You can download [Chrome Driver Here](https://chromedriver.chromium.org/downloads)  
