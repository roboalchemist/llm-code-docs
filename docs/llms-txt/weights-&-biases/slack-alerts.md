# Source: https://docs.wandb.ai/platform/hosting/monitoring-usage/slack-alerts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Configure Slack alerts

> Create and configure a Slack application to receive W&B Server alerts, notifications, and monitoring updates.

Integrate W\&B Server with [Slack](https://slack.com/).

<Note>
  Watch a [video demonstrating setting up Slack alerts on W\&B Dedicated Cloud deployment](https://www.youtube.com/watch?v=JmvKb-7u-oU) (6 min).
</Note>

## Create the Slack application

Follow the procedure below to create a Slack application.

1. Visit [https://api.slack.com/apps](https://api.slack.com/apps) and select **Create an App**.

   <Frame>
     <img src="https://mintcdn.com/wb-21fd5541/88iR80mZ8tuFCZUU/images/hosting/create_an_app.png?fit=max&auto=format&n=88iR80mZ8tuFCZUU&q=85&s=e790aa728101296c330a1574f8a66e67" alt="Create an App button" width="1442" height="686" data-path="images/hosting/create_an_app.png" />
   </Frame>

2. Provide a name for your app in the **App Name** field.

3. Select a Slack workspace where you want to develop your app in. Ensure that the Slack workspace you use is the same workspace you intend to use for alerts.

   <Frame>
     <img src="https://mintcdn.com/wb-21fd5541/7mSicW8MfO9qZmb2/images/hosting/name_app_workspace.png?fit=max&auto=format&n=7mSicW8MfO9qZmb2&q=85&s=3fcf56357f3e21b1cc3c49ee663c1fd8" alt="App name and workspace selection" width="1160" height="1106" data-path="images/hosting/name_app_workspace.png" />
   </Frame>

## Configure the Slack application

1. On the left sidebar, select **OAth & Permissions**.

   <Frame>
     <img src="https://mintcdn.com/wb-21fd5541/88iR80mZ8tuFCZUU/images/hosting/add_an_oath.png?fit=max&auto=format&n=88iR80mZ8tuFCZUU&q=85&s=e17e33ef2247fc600b3562f05c98d4c5" alt="OAuth & Permissions menu" width="218" height="324" data-path="images/hosting/add_an_oath.png" />
   </Frame>

2. Within the Scopes section, provide the bot with the **incoming\_webhook** scope. Scopes give your app permission to perform actions in your development workspace.

   For more information about OAuth scopes for Bots, see the Understanding OAuth scopes for Bots tutorial in the Slack API documentation.

   <Frame>
     <img src="https://mintcdn.com/wb-21fd5541/7mSicW8MfO9qZmb2/images/hosting/save_urls.png?fit=max&auto=format&n=7mSicW8MfO9qZmb2&q=85&s=1a2ee73aa9b53970ca75523388dae6ac" alt="Bot token scopes" width="656" height="291" data-path="images/hosting/save_urls.png" />
   </Frame>

3. Configure the Redirect URL to point to your W\&B installation. Use the same URL that your host URL is set to in your local system settings. You can specify multiple URLs if you have different DNS mappings to your instance.

   <Frame>
     <img src="https://mintcdn.com/wb-21fd5541/7mSicW8MfO9qZmb2/images/hosting/redirect_urls.png?fit=max&auto=format&n=7mSicW8MfO9qZmb2&q=85&s=a7b850c1c7b541481f34f6bf6a96a6be" alt="Redirect URLs configuration" width="650" height="321" data-path="images/hosting/redirect_urls.png" />
   </Frame>

4. Select **Save URLs**.

5. You can optionally specify an IP range under **Restrict API Token Usage**, allow-list the IP or IP range of your W\&B instances. Limiting the allowed IP address helps further secure your Slack application.

## Register your Slack application with W\&B

1. Navigate to the **System Settings** or **System Console** page of your W\&B instance, depending on your deployment

2. Depending on the System page you are on follow one of the below options:

   * If you are in the **System Console**: go to **Settings** then to **Notifications**

     <Frame>
       <img src="https://mintcdn.com/wb-21fd5541/7mSicW8MfO9qZmb2/images/hosting/register_slack_app_console.png?fit=max&auto=format&n=7mSicW8MfO9qZmb2&q=85&s=9ec3027a055b9eea2c3eef8dac1d551b" alt="System Console notifications" width="1134" height="477" data-path="images/hosting/register_slack_app_console.png" />
     </Frame>

   * If you are in the **System Settings**: toggle the **Enable a custom Slack application to dispatch alerts** to enable a custom Slack application

     <Frame>
       <img src="https://mintcdn.com/wb-21fd5541/7mSicW8MfO9qZmb2/images/hosting/register_slack_app.png?fit=max&auto=format&n=7mSicW8MfO9qZmb2&q=85&s=00df6348253222c461f63e069fb925f6" alt="Enable Slack application toggle" width="667" height="187" data-path="images/hosting/register_slack_app.png" />
     </Frame>

3. Supply your **Slack client ID** and **Slack secret** then click **Save**. Navigate to Basic Information in Settings to find your application’s client ID and secret.

4. Verify that everything is working by setting up a Slack integration in the W\&B app.
