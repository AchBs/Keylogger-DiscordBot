# Advanced Keylogger with Discord Integration

## Overview

This project is an advanced keylogger application built using Python, designed to capture and log keystrokes in real-time. The logged data is sent to a Discord server via a bot, providing a centralized way to monitor keystrokes.

## Ethical Considerations

**Important**: This application must be used responsibly and ethically. Ensure you have explicit permission from the user before running the keylogger. Unauthorized use of keyloggers is illegal and unethical.

## Features

- **Real-time Keystroke Logging**: Captures every keystroke, including special keys like Ctrl, Alt, Tab, etc.
- **Discord Integration**: Sends logged data to a Discord server in real-time.
- **Automatic Channel Creation**: The bot creates a new Discord channel named after the PC where the keylogger is running.
- **User Interface**: Simple GUI using Tkinter with a start/stop button.
- **Warning Message**: Displays a warning message to the user before starting the keylogger.

## Requirements

- Python 3.x
- `discord.py` library
- `keyboard` library
- `tkinter` library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/Keylogger-DiscordBot.git
    cd Keylogger-DiscordBot
    ```

2. Install the required libraries:
    ```bash
    pip install discord.py keyboard
    ```

3. Replace the placeholder with your Discord bot token in the code:
    ```python
    BOT_TOKEN = 'YOUR_DISCORD_BOT_TOKEN'
    ```

## Usage

1. **Run the Application**:
    ```bash
    python keylogger.py
    ```

2. **Warning Message**: The application will display a warning message asking the user if they wish to continue. If the user clicks "Yes," the keylogger will start. If "No," the program will exit.

3. **Discord Bot**: The bot will automatically create a channel named after the PC and start sending logged keystrokes to this channel.

## Code Description

### Key Components:

- **Discord Bot Integration**: 
    - Connects to Discord using the bot token.
    - Checks if a channel exists with the PC name and creates one if it doesn't.
    - Sends logged keystrokes to the channel.

- **Keylogger Functionality**:
    - Captures keystrokes using the `keyboard` library.
    - Logs every keystroke, including special keys.
    - Sends logged data to the Discord channel.

- **User Interface**:
    - Simple GUI with Tkinter.
    - "Stop" button to terminate the keylogger.
    - Warning message displayed at the start.

### Main Functions:

- `create_channel_if_not_exists(client, channel_name)`: Checks if a channel exists and creates it if not.
- `start_key_logger(channel)`: Captures keystrokes and logs them.
- `on_ready()`: Event handler for when the bot is ready.
- `start_discord_bot()`: Starts the Discord bot.
- `show_message()`: Displays the keylogger GUI.
- `stop_key_logger()`: Stops the keylogger.
- `show_initial_message()`: Displays the initial warning message.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Disclaimer

This project is intended for educational purposes only. The misuse of this software can lead to severe legal consequences. Always ensure you have permission before using any kind of monitoring software.
