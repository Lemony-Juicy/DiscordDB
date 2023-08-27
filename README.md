# DiscordDB
Simple package for storing/retrieving data from discord using SQL-like querying. DiscordBD was inspired by the pre-existing DiscordDatabase package, However it lacked the functionalities to retrieve data in a similar fashion to SQL, where multiple items could be selected through filtering. This package allows for storing atomic level data and quicker querying.

## Setting Up
DiscordDB works by creating an object from the `DataBase` class found in the package. The DataBase class inherits from `commands.Bot` class in the [discord.py](https://pypi.org/project/discord.py/) API Wrapper. 

After installing the [discord.py](https://pypi.org/project/discord.py/) python package:  
- Import `Database, TableHeading` from `DiscordDB` and also import `discord` since we will be needing intents.
- Create the database object. Ensure you also pass in the `command_prefix` and `intents` parameters like in the `example.py` file.
- Create asynchronous function(s) where you can create, add and do basic CRUD operations on the database object.
- Now just run your token at the end of the script. Ensure this is at the end since it's a blocking method call.
  
> **Note**  
> Since the database class inherits from bot class, you can create your bot with the database class as well.
