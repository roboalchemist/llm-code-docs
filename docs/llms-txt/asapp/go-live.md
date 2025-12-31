# Source: https://docs.asapp.com/generativeagent/go-live.md

# Go Live

After configuring GenerativeAgent and connecting to ASAPP's servers, you can go live into your production environments.

These are the steps to take to go live:

<Steps>
  <Step title="Launch Pre-check" />

  <Step title="Validate Your Integration" />

  <Step title="Launch GenerativeAgent into Production" />

  <Step title="Post Launch Maintenance" />
</Steps>

## Step 1: Validate your Configuration

Review that the following sections of the Configuration Phase are working as expected or have been signed off:

* **Functional requirements**: Confirm your Tasks and Function Requirements were addressed by your ASAPP Team and are correctly set up in GenerativeAgent. You can use the Previewer to test task and functions.

* **Functional and UAT Testing**: Validate individual components and end-to-end functionality between the GenerativeAgent and your customers. Your organization and your ASAPP Team must have signed off acceptance for the functionality of tasks, requirements, and user interactions before going live.

* **Human-In-the-Loop Set-up**: Confirm the Human-In-the-Loop definitions are properly defined in the GenerativeAgent's Tasks

  You can use the Previewer to test Human-in-the-Loop.

* **Credentials Verification**: Verify all your ASAPP Credentials and API Keys are obtained and that all key connections and calls to GenerativeAgent return data without any issue.

* **API Connections**: Ensure your APIs are connected to GenerativeAgent and your applications are calling GenerativeAgent and ASAPP to send messages and analyze them

* **Knowledge Base ingestion**: Ensure the Tasks and Functions you previously defined align with the responses that reference your Knowledge Base as Source-of-Truth.

## Step 2: Validate your Integration

Separated from GenerativeAgent functional configuration, you need to ensure your voice or chat applications are fully integrated with Generative Agent to go live.

<Note>
  Your method of integration determines the steps to go live
</Note>

To validate your integration is working smoothly, remember the following:

**Event Handling**

Ensure you are handling all events. GenerativeAgent communicates back to you via events.

These events are sent via Server-Sent-Event stream.

**API Integration**

Test your APIs exposure in the GenerativeAgent UI: Test how GenerativeAgent calls your APIs when performing Functions

You can do this in the previewer.

**Audio Integration**

Audio Integrations need a consistent flow of incoming and outcoming audio streams. Ensure that your organization opens, stops, and ends audio streams in every interaction between a customer and an agent.

**AutoTranscribe Websocket Integration**

* **Real-time Messaging**: Ensure that the URL Websocket connections are continuously provided by the ASAPP Server.

* **WebSocket protocol**: Request messages in the sequence must be formatted as text (UTF-8 encoded string data); only the audio stream should be formatted in binary. All response messages must also be formatted as text.

**Third Party Connectors**

Follow the integration procedure for the Third Party Connectors of your choice:

<Card title="UniMRCP Pluggin" href="/generativeagent/integrate/unimrcp-plugin-for-asapp" />

After the integration, ensure that your Third Party Connector is receiving and sending audio streams to the ASAPP Servers. This is done outside of the ASAPP applications.

**Text-only Integration**

Text conversations with GenerativeAgent can be ensured via the Previewer. Ensure messages are sent, analyzed, and that the GenerativeAgent replies with expected outputs

### Substep: Test the Integration

Test your integration to ensure that GenerativeAgent

> **Performance Testing**: Simulate expected traffic or high-traffic scenarios to determine any breaking-point or requirements meeting.

## Step 3: Launch GenerativeAgent to Production

Now you are ready to deploy GenerativeAgent into your Production environments.

### Deploy GenerativeAgent

Deploy GenerativeAgent into your Production environments without further effort.

You can do this from the GenerativeAgent UI.

<Card title="Deploy Generative Agent" href="/generativeagent/configuring/deploying-to-generativeagent" />

### Talk with GenerativeAgent

Now that GenerativeAgent is live in your Organization's environments, you can talk to the GenerativeAgent and receive LLM support.

> If your Integration has a Voice Channel, call your internal phone numbers and ask for issues or inquiries your customers would ask.
>
> If your integration with GenerativeAgent has a (message) Chat Integration, use the GenerativeAgent UI to continuously review how the GenerativeAgent helps with customer support and other issues.
>
> If your Integration involves Voice applications, you can also gather insights from GenerativeAgent's analyze calls in the GenerativeAgent UI.

## Step 4: Post Launch Maintenance

There are still some things you can do after GenerativeAgent is deployed.

Here are some things that your organization can do to continuously monitor GenerativeAgent while it is live.

Your ASAPP team is at your disposal to check anything else!

**Performance Monitoring**

* **Analytics**: Continuously analyze user interactions and system logs to make the better of analytics that can make GenerativeAgent perform better.
* **Alerts**: Use your internal monitoring tools to check on GenerativeAgent's Performance.
* **Enhancement**: ASAPP is continuously enhancing its AI products, so feel free to address your ASAPP Team for new features or improvements.

**Feedback**

Feedback Sessions: Your ASAPP team is always ready to receive feedback either from customer satisfaction surveys or from internal auditions.

**Internal Training**

Provide comprehensive training sessions for your internal staff in the scenarios where GenerativeAgent performs.

In the case that your Organization uses Human-in-the-Loop, train your staff for the scenarios when your human agents help GenerativeAgent in tasks.

**Support Plan**

Establish with your ASAPP team a support plan for post-launch assistance. This can work either by Helpdesk queries or direct support from your ASAPP Team.
