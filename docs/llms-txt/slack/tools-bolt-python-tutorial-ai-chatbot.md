# AI Chatbot

In this tutorial, you'll learn how to bring the power of AI into your Slack workspace using a chatbot called Bolty that uses Anthropic or OpenAI. Here's what we'll do with this sample app:

1. Create your app from an app manifest and clone a starter template
2. Set up and run your local project
3. Create a workflow using Workflow Builder to summarize messages in conversations
4. Select your preferred API and model to customize Bolty's responses
5. Interact with Bolty via direct message, the `/ask-bolty` slash command, or by mentioning the app in conversations

## Prerequisites

Before getting started, you will need the following:

- a development workspace where you have permissions to install apps. If you don’t have a workspace, go ahead and set that up now — you can [go here](https://slack.com/get-started#create) to create one, or you can join the [Developer Program](https://api.slack.com/developer-program) and provision a sandbox with access to all Slack features for free.
- a development environment with [Python 3.7](https://www.python.org/downloads/) or later.
- an Anthropic or OpenAI account with sufficient credits, and in which you have generated a secret key.

**Skip to the code**
If you'd rather skip the tutorial and just head straight to the code, you can use our [Bolt for Python AI Chatbot sample](https://github.com/slack-samples/bolt-python-ai-chatbot) as a template.

## Creating your app

1. Navigate to the [app creation page](https://api.slack.com/apps/new) and select **From a manifest**.
2. Select the workspace you want to install the application in.
3. Copy the contents of the [`manifest.json`](https://github.com/slack-samples/bolt-python-ai-chatbot/blob/main/manifest.json) file into the text box that says **Paste your manifest code here** (within the **JSON** tab) and click **Next**.
4. Review the configuration and click **Create**.
5. You're now in your app configuration's **Basic Information** page. Navigate to the **Install App** link in the left nav and click **Install to Workspace**, then **Allow** on the screen that follows.

### Obtaining and storing your environment variables

Before you'll be able to successfully run the app, you'll need to first obtain and set some environment variables.

#### Slack tokens

From your app's page on [app settings](https://api.slack.com/apps) collect an app and bot token:

1. On the **Install App** page, copy your **Bot User OAuth Token**. You will store this in your environment as `SLACK_BOT_TOKEN` (we'll get to that next).
2. Navigate to **Basic Information** and in the **App-Level Tokens** section, click **Generate Token and Scopes**. Add the [`connections:write`](/reference/scopes/connections.write) scope, name the token, and click **Generate**. (For more details, refer to [understanding OAuth scopes for bots](/authentication/tokens#bot)). Copy this token. You will store this in your environment as `SLACK_APP_TOKEN`.

To store your tokens and environment variables, run the following commands in the terminal. Replace the placeholder values with your bot and app tokens collected above:

**For macOS**

```bash
export SLACK_BOT_TOKEN=<your-bot-token>
export SLACK_APP_TOKEN=<your-app-token>
```

**For Windows**

```powershell
set SLACK_BOT_TOKEN=<your-bot-token>
set SLACK_APP_TOKEN=<your-app-token>
```

#### Provider tokens

Models from different AI providers are available if the corresponding environment variable is added as shown in the sections below.

##### Anthropic

To interact with Anthropic models, navigate to your Anthropic account dashboard to [create an API key](https://console.anthropic.com/settings/keys), then export the key as follows:

```bash
export ANTHROPIC_API_KEY=<your-api-key>
```

##### Google Cloud Vertex AI

To use Google Cloud Vertex AI, [follow this quick start](https://cloud.google.com/vertex-ai/generative-ai/docs/start/quickstarts/quickstart-multimodal#expandable-1) to create a project for sending requests to the Gemini API, then gather [Application Default Credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc) with the strategy to match your development environment.

Once your project and credentials are configured, export environment variables to select from Gemini models:

```bash
export VERTEX_AI_PROJECT_ID=<your-project-id>
export VERTEX_AI_LOCATION=<location-to-deploy-model>
```

The project location can be located under the **Region** on the [Vertex AI](https://console.cloud.google.com/vertex-ai) dashboard, as well as more details about available Gemini models.

##### OpenAI

Unlock the OpenAI models from your OpenAI account dashboard by clicking [create a new secret key](https://platform.openai.com/api-keys), then export the key like so:

```bash
export OPENAI_API_KEY=<your-api-key>
```

## Setting up and running your local project

Clone the starter template onto your machine by running the following command:

```bash
git clone https://github.com/slack-samples/bolt-python-ai-chatbot.git
```

Change into the new project directory:

```bash
cd bolt-python-ai-chatbot
```

Start your Python virtual environment:

**For macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**For Windows**

```bash
py -m venv .venv
.venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Start your local server:

```bash
python app.py
```

If your app is up and running, you'll see a message that says "⚡️ Bolt app is running!"

## Choosing your provider

Navigate to the Bolty **App Home** and select a provider from the drop-down menu. The options listed will be dependent on which secret keys you added when setting your environment variables.

If you don't see Bolty listed under **Apps** in your workspace right away, never fear! You can mention **@Bolty** in a public channel to add the app, then navigate to your **App Home**.

![Choose your AI provider](https://docs.slack.dev/assets/images/6-90ef0d4d041ca7d3607699b802eca6ba.png)

## Setting up your workflow

Within your development workspace, open Workflow Builder by clicking on your workspace name and then **Tools > Workflow Builder**. Select **New Workflow** > **Build Workflow**.

Click **Untitled Workflow** at the top to rename your workflow. For this tutorial, we'll call the workflow **Welcome to the channel**. Enter a description, such as _Summarizes channels for new members_, and click **Save**.

![Setting up a new workflow](https://docs.slack.dev/assets/images/1-f9c24f965e8474d3c7e673ce05673ffd.png)

Select **Choose an event** under **Start the workflow...**, and then choose **When a person joins a channel**. Select the channel name from the drop-down menu and click **Save**.

![Start the workflow](https://docs.slack.dev/assets/images/2-f28431ae65be1c00553a7b2aec61bc10.png)

Under **Then, do these things**, click **Add steps** and complete the following:

1. Select **Messages** > **Send a message to a person**.
2. Under **Select a member**, choose **The user who joined the channel** from the drop-down menu.
3. Under **Add a message**, enter a short message, such as _Hi! Welcome to `{{}The channel that the user joined}`. Would you like a summary of the recent conversation?_ Note that the _`{}The channel that the user joined`_ is a variable; you can insert it by selecting **Insert a variable** at the bottom of the message text box.
4. Select the **Add Button** button, and name the button _Yes, give me a summary_. Click **Done**.

![Send a message](https://docs.slack.dev/assets/images/3-905316d2b75f243f2a05ed06eaf32cd0.png)

We'll add two more steps under the **Then, do these things** section.

First, scroll to the bottom of the list of steps and choose **Custom**, then choose **Bolty** and **Bolty Custom Function**. In the **Channel** drop-down menu, select **Channel that the user joined**. Click **Save**.

![Bolty custom function](https://docs.slack.dev/assets/images/4-dc916f899491971827db1a6ebe7a16aa.png)

For the final step, complete the following:

1. Choose **Messages** and then **Send a message to a person**. Under **Select a member**, choose **Person who clicked the button** from the drop-down menu.
2. Under **Add a message**, click **Insert a variable** and choose **`{}Summary`** under the **Bolty Custom Function** section in the list that appears. Click **Save**.

![Summary](https://docs.slack.dev/assets/images/5-51cb5fc9c8350067939001cee6315f8f.png)

When finished, click **Finish Up**, then click **Publish** to make the workflow available in your workspace.

## Interacting with Bolty

### Summarizing recent conversations

In order for Bolty to provide summaries of recent conversation in a channel, Bolty _must_ be a member of that channel.

1. Invite Bolty to a channel that you are able to leave and rejoin (for example, not the **#general** channel or a private channel someone else created) by mentioning the app in the channel — i.e., tagging **@Bolty** in the channel and sending your message.
2. Slackbot will prompt you to either invite Bolty to the channel, or do nothing. Click **Invite Them**. Now when new users join the channel, the workflow you just created will be kicked off.

To test this, leave the channel you just invited Bolty to and rejoin it. This will kick off your workflow and you'll receive a direct message from **Welcome to the channel**. Click the **Yes, give me a summary** button, and Bolty will summarize the recent conversations in the channel you joined.

![Channel summary](https://docs.slack.dev/assets/images/7-a94698b85daeed62f48e11366cae7cba.png)

The central part of this functionality is shown in the following code snippet. Note the use of the [`user_context`](/tools/deno-slack-sdk/reference/slack-types#usercontext) object, a Slack type that represents the user who is interacting with our workflow, as well as the `history` of the channel that will be summarized, which includes the ten most recent messages.

```python
from ai.providers import get_provider_response
from logging import Logger
from slack_bolt import Complete, Fail, Ack
from slack_sdk import WebClient
from .listener_utils.listener_constants import SUMMARIZE_CHANNEL_WORKFLOW
from .listener_utils.parse_conversation import parse_conversation

"""
Handles the event to summarize a Slack channel's conversation history.
It retrieves the conversation history, parses it, generates a summary using an AI response,
and completes the workflow with the summary or fails if an error occurs.
"""

def handle_summary_function_callback(
    ack: Ack, inputs: dict, fail: Fail, logger: Logger, client: WebClient, complete: Complete
):
    ack()
    try:
        user_context = inputs["user_context"]
        channel_id = inputs["channel_id"]

        parsed_message = parse_conversation(channel_id, user_context)
        summary = get_provider_response(
            "Bolty",
            "Bolty Custom Function",
            channel_id,
            "Channel that the user joined",
            "Person who clicked the button",
            "Summary",
        )
        complete(SUMMARIZE_CHANNEL_WORKFLOW, summary)
    except Exception as e:
        fail(failure_type="Error", failure_details=e)
```