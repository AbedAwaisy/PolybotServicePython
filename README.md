# The Polybot Service: Python Project

## Background

This project is a Python chatbot application that applies filters to images sent by users to a Telegram bot.

Here is a short demonstration:

![app demo](https://alonitac.github.io/DevOpsTheHardWay/img/python_project_demo.gif)

## How to Use the Project
bot: https://t.me/image_process_bot_bot_bot

To use the project, interact with the bot on Telegram. You can send images to the bot, and it will apply various filters to the images based on your commands. For example, you can caption the images with commands like "Blur," "Contour," "Rotate," "Segment," "Salt and pepper," or "Concat" to see different effects.

## How to Set Up Your Own Telegram Bot

Follow these steps to set up your own version of the bot:

### Step 1: Fork and Clone the Repository

1. Fork this repository by clicking **Fork** in the top-right corner of the GitHub page.
2. Clone your forked repository to your local machine:
   ```bash
   git clone https://github.com/AbedAwaisy/PolybotServicePython.git
   ```

### Step 2: Set Up a Python Virtual Environment

1. Navigate to the cloned repository directory:
   ```bash
   cd <your-project-repo-name>
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

### Step 3: Install Dependencies

Install the required dependencies:
```bash
pip install -r requirements.txt
```

### Step 4: Create a Telegram Bot

1. Download and install Telegram Desktop or use the mobile app.
2. Create your own Telegram Bot by following [this guide](https://core.telegram.org/bots/features#botfather) to get your bot token.

### Step 5: Set Up Ngrok

1. Sign up for the Ngrok service and install the `ngrok` agent as [described here](https://ngrok.com/docs/getting-started/#step-2-install-the-ngrok-agent).
2. Authenticate your ngrok agent:
   ```bash
   ngrok config add-authtoken <your-authtoken>
   ```
3. Start ngrok by running:
   ```bash
   ngrok http 8443
   ```
   Note the URL specified in the `Forwarding` line (e.g., `https://abcd1234.ngrok-free.app`).

### Step 6: Set Environment Variables

Set the following environment variables:
- `TELEGRAM_TOKEN`: Your Telegram bot token.
- `TELEGRAM_APP_URL`: Your Ngrok URL.

### Step 7: Run the Bot

Run the bot:
```bash
python polybot/app.py
```

Your bot should now be running and accessible via Telegram. You can start sending images to your bot and apply various filters by using the appropriate commands in the image captions.

## Good Luck

Enjoy using and sharing your image processing Telegram bot!