# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/alexa.md

# Amazon Alexa

Amazon Alexa, known simply as Alexa, is a virtual assistant AI technology developed by Amazon. It is capable of voice interaction, music playback, making to-do lists, setting alarms, streaming podcasts, playing audiobooks, and providing weather, traffic, sports, and other real-time information, such as news. Alexa can also control several smart devices using itself as a home automation system. Users are able to extend the Alexa capabilities by installing "skills".

{% hint style="info" %}
**Note**: You can connect to a channel only if it is enabled for your account or company. If you wish to enable a channel, then contact Avaamo Support for further assistance. Note that only the web channel is enabled by default.&#x20;
{% endhint %}

The agents developed on the Avaamo platform can be deployed on Amazon Alexa. In this article, the following steps are detailed:

1. [Before you begin](#before-you-begin)
2. [Creating an Alexa skill in the Amazon Developer Console](#creating-an-alexa-skill-in-the-amazon-developer-console)
3. [Connecting your Alexa skill to an Avaamo agent](#connecting-your-alexa-skill-to-an-avaamo-agent)
4. [Testing Integration](#test-integration)
5. [Publishing Alexa Skills](#publish-alexa-skills)
6. [Manage channel settings](#manage-channel-settings)

## Before you begin

Ensure you have the following information that is required for connecting your Alexa skill to your agent:

* **Invocation Name** – This phrase is usually just the name of the company and it is used for invoking the agent through Alexa. For example, you can say, "Alexa, ask \[invocation name]."
* **Endpoint URL** – This is used to connect Alexa to the agent. To get the endpoint URL:&#x20;
  * Select the "Channels" tab on the navigation bar
  * Find the Amazon Alexa channel
  * Click View
  * Copy the Endpoint URL that is displayed in the pop-up window.
* **JSON text (or .json file)** – You can copy and paste the following JSON text. Ensure you change the invocation name (replace "tutorial" with "\[your invocation name]").

{% hint style="success" %}
**Key Point**: The following example is a CATCH\_ALL scenario just for demonstration purposes. Ideally, you must define specific intents that must be used in the Alexa skill. See [Create the Interaction Model for Your Skill](https://developer.amazon.com/en-US/docs/alexa/custom-skills/create-the-interaction-model-for-your-skill.html), for more information.
{% endhint %}

```json
{
  "interactionModel": {
    "languageModel": {
      "invocationName": "tutorial",
      "intents": [
        {
          "name": "AMAZON.FallbackIntent",
          "samples": []
        },
        {
          "name": "AMAZON.PauseIntent",
          "samples": []
        },
        {
          "name": "AMAZON.StopIntent",
          "samples": []
        },
        {
          "name": "AMAZON.CancelIntent",
          "samples": []
        },
        {
          "name": "AMAZON.HelpIntent",
          "samples": []
        },
        {
          "name": "AMAZON.ResumeIntent",
          "samples": []
        },
        {
          "name": "CATCH_ALL",
          "slots": [
            {
              "name": "sentence",
              "type": "ANYTHING"
            }
          ],
          "samples": [
            "{sentence}"
          ]
        },
        {
          "name": "AMAZON.NavigateHomeIntent",
          "samples": []
        }
      ],
      "types": [
        {
          "name": "ANYTHING",
          "values": [
            {
              "name": {
                "value": "x"
              }
            },
            {
              "name": {
                "value": "x x"
              }
            },
            {
              "name": {
                "value": "x x x"
              }
            },
            {
              "name": {
                "value": "x x x x"
              }
            },
            {
              "name": {
                "value": "x x x x x"
              }
            },
            {
              "name": {
                "value": "x x x x x x"
              }
            },
            {
              "name": {
                "value": "x x x x x x x"
              }
            },
            {
              "name": {
                "value": "x x x x x x x x"
              }
            },
            {
              "name": {
                "value": "x x x x x x x x x"
              }
            },
            {
              "name": {
                "value": "x x x x x x x x x x"
              }
            },
            {
              "name": {
                "value": "x x x x x x x x x x x"
              }
            },
            {
              "name": {
                "value": "x x x x x x x x x x x x"
              }
            },
            {
              "name": {
                "value": "x x x x x x x x x x x x x"
              }
            },
            {
              "name": {
                "value": "x x x x x x x x x x x x x x"
              }
            },
            {
              "name": {
                "value": "x x x x x x x x x x x x x x x"
              }
            },
            {
              "name": {
                "value": "x x x x x x x x x x x x x x x x"
              }
            },
            {
              "name": {
                "value": "x x x x x x x x x x x x x x x x x"
              }
            },
            {
              "name": {
                "value": "x x x x x x x x x x x x x x x x x x"
              }
            },
            {
              "name": {
                "value": "x x x x x x x x x x x x x x x x x x x"
              }
            },
            {
              "name": {
                "value": "x x x x x x x x x x x x x x x x x x x x"
              }
            },
            {
              "name": {
                "value": "x x x x x x x x x x x x x x x x x x x x x"
              }
            },
            {
              "name": {
                "value": "x x x x x x x x x x x x x x x x x x x x x x"
              }
            },
            {
              "name": {
                "value": "x x x x x x x x x x x x x x x x x x x x x x x"
              }
            },
            {
              "name": {
                "value": "x x x x x x x x x x x x x x x x x x x x x x x x"
              }
            },
            {
              "name": {
                "value": "x x x x x x x x x x x x x x x x x x x x x x x x x"
              }
            }
          ]
        }
      ]
    }
  }
}
```

## Creating an Alexa skill in the Amazon Developer Console

Visit the [Alexa Skills Kit Developer Console](https://developer.amazon.com/alexa/console/ask) and sign in if necessary. If you do not already have an Amazon Developer Account, you must first create an account [here](https://developer.amazon.com/).

**To create an Alexa skill in the Amazon Developer Console**:

* Open [Alexa Skills Kit Developer Console](https://developer.amazon.com/alexa/console/ask) and click **Create Skill**. Note that if you wish to update a skill that you have already created, click the required skill in the list and skip to Step 4.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M239yjy0vArsjQhpZNY%2F-M23AlfyqlMC_sI5bfwg%2Falexa-step-1.png?alt=media\&token=65a6ec33-89ea-4abc-a7ec-b353ad1442fc)

* In the **Create new skill** page, specify the skill name, select **Custom** model, and click **Create Skill**.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M239yjy0vArsjQhpZNY%2F-M23CY3NkJOjawPew1AJ%2Fagent-deploy-alexa-2.png?alt=media\&token=8fe0b0dd-4cbf-4b6d-a108-32278d3c3358)

* In the Template page, select **Start from scratch** template and click **Choose**.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M239yjy0vArsjQhpZNY%2F-M23DY5bpev2Gzof5pne%2Fagent-deploy-alexa-3.png?alt=media\&token=75eba0a7-763b-4c73-87af-e1f7a609dc06)

* In the **Custom template** page, click **JSON Editor**. Paste the JSON code as specified in the Before you begin a section and click **Build Model**. Note that the invocation name in the JSON must be unique.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M239yjy0vArsjQhpZNY%2F-M23F7x_z5olTm2MCsrW%2Fagent-deploy-alexa-4.png?alt=media\&token=f6fa9864-86e5-4c34-8049-c39b9d9f51df)

* After the build is successful, a notification message is displayed. The next step is to configure the endpoint to connect your Alexa skill with the Avaamo agent.

## Connecting your Alexa skill to an Avaamo agent

In the **Custom Template** page, click **EndPoint.** Select **HTTPS** and specify the following details:

* Specify the endpoint URL from the Amazon Alexa channel in the Avaamo Platform. See Before you begin, for more information.
* In the SSL certificate, select "My development endpoint is a sub-domain of a domain that has a wildcard certificate from a certificate authority" option.
* Click **Save Endpoints**. Your integration is now ready for testing.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M239yjy0vArsjQhpZNY%2F-M23HazfIUtWaE2HUPMo%2Fagent-deploy-alexa-5.png?alt=media\&token=33556802-2edc-43d2-858c-3bffb952cc7e)

## Test integration

You can test integration in the console and using an Alexa device. If you want to immediately test your agent from an Alexa Enabled device (such as an Echo Dot), you can skip testing from the console. See [Test with an Alexa device](#test-with-an-alexa-device), to directly test on any Alexa enabled device.

* Click **Test** tab and choose **Development** option in "Skill testing is enabled in:" dropdown.
* Click and hold the microphone and then say the invocation phrase to begin the conversation. You can also type the invocation phrase.

{% hint style="info" %}
**Notes**:

* Alexa only hears you when you click and hold the microphone
* You can always type or say reset if you wish to restart the conversation.&#x20;
* If you want to immediately test your agent from an Alexa Enabled device (such as an Echo Dot), you can skip testing from the console.
  {% endhint %}

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M239yjy0vArsjQhpZNY%2F-M23gmHzzgNyS9bO_dUB%2Fagent-deploy-alexa-6.png?alt=media\&token=477d87d8-edb7-4c15-80bd-4be1479345f2)

#### Test with an Alexa Device

1. Download the Amazon Alexa app.
2. Log in with your Amazon account username and password (use the same account that you were just using to build your Alexa Skill).
3. In the **Skills & Games** menu option, verify if your skill is listed under **Dev**.
4. Make sure the Amazon Alexa app is open and you are connected to Wi-Fi.
5. Use the invocation phrase of your skill to begin the conversation with your virtual assistant. You can say, “Alexa, ask \[invocation phrase]”).
6. Engage in conversation and experience the future of conversational assistance. Note that you can always say "reset" if you wish to restart the conversation.

## Publish Alexa skills

When you are done with the testing, you can publish your Alexa Skill. A private skill is published live but is not available in the Alexa skill store. See [Create and Publish Private Skills (Developer Console)](https://developer.amazon.com/en-US/docs/alexa/alexa-for-business/create-and-publish-private-skills-devconsole.html), for more information on how to publish Alexa skills.

## Manage channel settings

After you configure the channel settings, you can view, edit, disconnect and delete the channel settings as per your requirements. See [Manage channel settings](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/manage-channel-settings), for more information.
