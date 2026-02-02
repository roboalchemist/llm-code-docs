# AI Code Assistant with Hugging Face

In this tutorial, we will create an [app that has platform AI features enabled](/ai/developing-ai-apps) with the Bolt framework and integrate a [Hugging Face](https://huggingface.co/) model to assist the user with coding questions. We'll also make this functionality available as a step in a workflow to use in Workflow Builder.

Hugging Face is an open-source community best known for its transformers library and platform for machine learning models. Hugging Face's model hub is an online repository where you can find thousands of pre-trained models for natural language processing, computer vision, speech recognition, and more. The platform is open-source, so anyone can contribute to the models and browse the models others have started. Here, we will be using the [Qwen2.5-Coder-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct) model to create an app that can answer coding questions.

## Prerequisites

Before getting started, you will need the following:

- a development workspace where you have permissions to install apps. If you don’t have a workspace, go ahead and set that up now—you can [go here](https://slack.com/get-started#create) to create one, or you can join the [Developer Program](https://api.slack.com/developer-program) and provision a sandbox with access to all Slack features for free.
- a Hugging Face account in which you can generate an access token.

## Creating your app

1. Navigate to the [app creation page](https://api.slack.com/apps/new) and select **From a manifest**.
2. Select the workspace you want to install the application in and click **Next**.
3. Copy the contents below and paste it into the text box that says **Paste your manifest code here** (within the **JSON** tab), replacing the placeholder text, and click **Next**.

```json
{
  "display_information": {
    "name": "Code Assistant"
  },
  "features": {
    "app_home": {
      "home_tab_enabled": false,
      "messages_tab_enabled": true,
      "messages_tab_read_only_enabled": false
    },
    "bot_user": {
      "display_name": "Code Assistant",
      "always_online": false
    },
    "assistant_view": {
      "assistant_description": "An Assistant to help you with coding questions and challenges!",
      "suggested_prompts": []
    }
  },
  "oauth_config": {
    "scopes": {
      "bot": [
        "assistant:write",
        "channels:join",
        "im:history",
        "channels:history",
        "groups:history",
        "chat:write"
      ]
    }
  },
  "settings": {
    "event_subscriptions": {
      "bot_events": [
        "assistant_thread_context_changed",
        "assistant_thread_started",
        "message.im",
        "function_executed"
      ]
    },
    "interactivity": {
      "is_enabled": true
    },
    "org_deploy_enabled": true,
    "socket_mode_enabled": true,
    "function_runtime": "remote",
    "token_rotation_enabled": false
  },
  "functions": {
    "code_assist": {
      "title": "Code Assist",
      "description": "Get an answer about a code related question",
      "input_parameters": {
        "message_id": {
          "type": "string",
          "title": "Message ID",
          "description": "The message the question was asked in.",
          "is_required": true
        },
        "channel_id": {
          "type": "slack#/types/channel_id",
          "title": "Channel ID",
          "description": "The channel the question was asked in",
          "is_required": true
        }
      },
      "output_parameters": {
        "message": {
          "type": "string",
          "title": "Answer",
          "description": "The response from the Code Assistant LLM",
          "is_required": true
        }
      }
    }
  }
}
```

4. Review the configuration and click **Create**. Clicking around in these settings, you can see what the manifest has created for us. Some highlights:

- Within **App Home**, we've enabled the **Chat Tab**. This will allow users to access your app both in the split-view container as well as within a chat tab of the app.
- **Agents & AI Apps** is enabled. With this toggled on, the split-view container is available for your app.
- A custom step has been added to **Workflow Steps**. A workflow step is a custom step that can be used in Workflow Builder. Setting up information about that step here (its name, input parameters, and output parameters) lets Slack know what data to collect from the workflow to send to the function. We'll implement the logic step for this in code.
- **Org Level Apps** has been enabled. This means that your app will be installed at the organization level. Upon installation, it is not added to any workspaces, but the workspace admin can choose which workspaces in the org to add the app to.
- Within **OAuth & Permissions**, you will find several bot scopes have been added.
- Within **Event Subscriptions**, you will find several events this app subscribes to, which allow it to respond to user requests appropriately.

5. Navigate to the **Install App** page in the left nav and click **Install to Workspace**, then **Allow** on the screen that follows.

### Obtaining your environment variables

In order to connect this configuration with the app we are about to code, you'll need to first obtain and set some environment variables.

1. **Bot token**: On the **Install App<