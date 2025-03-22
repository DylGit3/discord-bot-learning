Simple Discord Bot
  This is a basic Discord bot that responds to messages and offers a few interactive features like rolling dice and greeting users. It uses a set of predefined responses in response to various inputs from users.

Tools Used
  Python: The main programming language used for the bot.
  discord.py: A Python wrapper for the Discord API, allowing interaction with Discord’s messaging system.
  dotenv: Used to manage environment variables securely, particularly the bot's token.
  random: For generating random responses, such as dice rolls.
  Intents: Utilized to enable message content access.
Features
  Responds to basic greetings
  Rolls a dice when the user types “roll dice”
  Provides random responses for unknown inputs
Code Overview
  main.py: The core of the bot. It handles the connection to Discord, listening for messages, and sending responses. The bot uses Intents to read the message content, and sends a message either publicly or privately based on the content.
  responses.py: Contains a function (get_response) to handle different user inputs. It responds to specific commands such as greetings and dice rolling, and returns a random message for unrecognized input.
What I Learned
  How to create a basic bot using discord.py and Python.
  The use of environment variables for sensitive data (like the bot token).
  Handling user input and generating dynamic responses.
  Managing private vs. public messages in Discord channels.
Moving Forward
  I plan to add more responses and features to the bot, such as handling more commands, implementing a user database, or adding interactive games.
  I will also consider adding a better error-handling mechanism for when the bot encounters unexpected inputs or failures.
