# Source: https://jam.dev/docs/jam-for-customer-support/intercom-fin-ai.md

# Intercom Fin AI

### Requirements

✅ This is a feature for paid plans\
✅ [Jam Intercom App](https://www.intercom.com/app-store/?app_package_code=jam-recorder) installed in the Intercom workspace\
✅ Web channel only (mobile not supported)\
✅ Fin workflow configuration required

### How the Integration Works

The integration works by adding the [Jam Intercom App](https://www.intercom.com/app-store/?app_package_code=jam-recorder) directly to your Fin workflows, allowing you to prompt users for screen recordings at specific points in your customer support process. For example, you could place Jam before Fin starts to gather context, or before handing off the conversation to a human agent.

### Adding Jam to Your Fin Workflow

You can add Jam as a step to prompt customers for screen recordings at the right moment in the conversation. This can be done with a simple drop-in app step for quick setup, or combined with webhooks if you need more control and want Intercom to branch the workflow depending on whether the customer recorded or opted out.

#### Step 1: Access Your Fin Workflow

Navigate to your Fin workflow where you want to add Jam integration.<br>

<figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FLqQlXmbxYFhsBcdZ7m3j%2FScreen%20Cast%202025-06-10%20at%2011.23.55%20AM.gif?alt=media&#x26;token=c4de56d5-04dd-43fb-8a68-104b0ff5d922" alt=""><figcaption></figcaption></figure>

#### Step 2: Set Channel to Web

Ensure your workflow channel is set to "Web".&#x20;

<figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FvMBOT8eXcwg3TeWBLs4Q%2FScreenshot%202025-06-10%20at%2011.23.06.png?alt=media&#x26;token=821db5fe-98f2-4b53-bef8-a71e8331ad11" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Jam for Intercom currently doesn't support mobile devices. Make sure to set your workflow channel to Web, otherwise Jam will not work as expected.
{% endhint %}

#### Step 3: Add Jam Step

At any point in your Fin workflow, you can add a new step:

1. Click "**Add step**"
2. Select "**Send an app**"
3. Choose "Jam" from the list of available apps
4. When adding the Jam step, you’ll need to **configure** some fields:

* **Message**:t his is the standard message that will accompany every Jam link. Consider how you want to introduce this request to your end customer so that they understand the purpose of recording their screen with Jam.
* **Opt out**: Check Yes or No. Clicking Yes will provide your end customer with two paths to move forward: one will be to record a Jam. The other will be to provide more issue detail by typing their response. Jam provides two options to ensure your end customers can pursue a solution through their preferred method of communication. If you prefer that end customers only have the option to record a Jam, select No.

{% hint style="info" %}
ℹ️ *Only select **Yes** if you plan to configure Jam with webhooks — otherwise, this setting will have no impact.*
{% endhint %}

1. Click "**Request screen recording**" to add the app to the workflow

<figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FzHQThcQOK4Z444eCQNrb%2FScreen%20Cast%202025-09-12%20at%2010.30.15%20AM.gif?alt=media&#x26;token=d9b9015d-ebe8-4384-8df9-3635ecae136d" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
If you don't see Jam in the available apps list, please go back to [Jam for Customer support documentation ](https://jam.dev/docs/jam-for-customer-support/broken-reference)install Jam in your Intercom workspace.
{% endhint %}

### (Optional): Configure Webhooks for More Control

By default, Intercom doesn’t know whether a customer recorded a Jam or opted out. If you want to branch your workflow based on the customer’s choice, you can configure [webhooks](https://jam.dev/docs/integrations/webhooks).

#### **1. Add Wait for Webhook**

* After the Jam step, click **Add step → Wait for Webhook**.

<figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FRNUXJ5INLRfcLe2K254b%2FScreenshot%202025-09-12%20at%2010.14.04.png?alt=media&#x26;token=5f0bcd49-e22c-4f3f-9141-c255f9ea9edb" alt=""><figcaption></figcaption></figure>

* In the resulting menu that opens, you should see an Example Request.
* Edit the example text in the following:
  * `“example_key”` -> `“event”`
  * `“example value (please edit)”` -> `“intercom.recorder.opted_out”`
  * add `"payload"` inside `"data"` with an empty curly brackets `{}`

Here's is the full example request if you want to just copy/paste:

```
{
  "event": "some string",
  "payload": {}
}
```

* Next, provide a title for your webhook for easier reference later on. You can edit it by clicking into the bolded text in the view you’re currently in. It should be directly to the left of the Save and Close button.&#x20;
* Lastly, copy the Webhook URL. Copy everything except for the ending characters: “/\<Conversation ID>”.&#x20;

Click Save and Close. Note: your view should look like the below screenshot.

<figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FdH1SMrzhPEtmQLo9xguz%2FScreenshot%202025-09-29%20at%2019.11.10.png?alt=media&#x26;token=189aa53e-ba8b-451e-83f2-67cd5c7acf97" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
the above webhook will only apply to this specific Intercom Workflow. You will need to set up a separate webhook for each Workflow you create.
{% endhint %}

#### **2. Register the Webhook in Jam**

* Once you have the Webhook URL, you’ll need to register it in Jam so the events can flow correctly.
* Follow the instructions in the[ Jam Webhooks documentation](https://jam.dev/docs/integrations/webhooks#id-2.-using-connectors) to configure your endpoint and paste this URL into the **Endpoint URL** field.

<figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FtHHbwzFTWlrVbdE295kM%2FScreenshot%202025-09-12%20at%2010.18.52.png?alt=media&#x26;token=e4497fc8-7c6d-49c2-9f5f-cbf156dfe2ce" alt=""><figcaption></figcaption></figure>

#### **3. Add Branching Logic**

Return to Intercom. At this point, we are ready to tell the workflow what next step should be taken based on the choice your end customer makes (either they Recorded a Jam, or opted to explain via text).

* Under the Wait for Webhook step you added, click Add Step.
* Type Branches and select the resulting option as shown below.

<figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FeqJeB8ZGEbi9HrP7Y7tr%2FScreenshot%202025-09-12%20at%2010.17.50.png?alt=media&#x26;token=a23ad268-5d8f-4142-acfc-abcea54b5de9" alt=""><figcaption></figcaption></figure>

* Under Branches, we will create two branches.
* Click on the **Missing Condition**, then **Add condition**.
  * Type Event in the **Search data** box. Then, select your “> event”. It should appear as an option with the webhook you created earlier.&#x20;
  * Select **“Is”**, then type the following in the open box: `intercom.recorder.recorded`.&#x20;
  * Click **Done -> Save and Continue**.
* Click **Add branch**.&#x20;
  * Repeat the same process starting with clicking into **Missing Condition**.&#x20;
  * When you set the **“Is”** value, type `intercom.recorder.opted_out`.&#x20;
  * Click **Done -> Save and Continue**.

### Design what happens after Jam

Now that Intercom can understand what your customer chose to do when prompted with Jam, you must decide what action we should take next. Our recommendation is as follows:

#### **If the customer recorded a Jam, assign a team member to review.**

* Click the red arrow next to the branch entitled `intercom.recorder.recorded`.
* Select **Message**.&#x20;

Include a message that signifies your team is reviewing the Jam recording and that you will respond shortly.

{% hint style="info" %}
Jam sends automatic messages when your customer begins recording, and when they submit a recording. The below is not customizable. Adjust your personalized message to follow the “Screen recorded succesfully” message.
{% endhint %}

<figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FvPY8MKAcMWeBOz9M1N6i%2Fimage.png?alt=media&#x26;token=4e5be734-a771-4187-801a-4f213be5fe83" alt=""><figcaption></figcaption></figure>

**If the customer opts to submit their issue via text instead of recording a Jam.**

* Click the red arrow next to the branch entitled `intercom.recorder.opted_out`.&#x20;
* Select **Message**.
* Include a message that signifies the customer will need to explain the issue.&#x20;
* Then, click **Add Step**.
* Click **Collect customer reply**.
* Next, click the red arrow to add another step in your workflow. At this stage, we’d advise that you Assign a team member, like shown in the first workflow outlined above.

![](https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2F6umqdtyuQQuXU6a3c6HC%2FScreenshot%202025-09-12%20at%2010.26.32.png?alt=media\&token=1dd47c45-d061-4567-a736-032208144fd3)

### Current Limitations

For now, Jam for Intercom can only be activated with Fin Workflows, integration via Fin Tasks is currently not possible.

###
