# Source: https://docs.asapp.com/agent-desk/virtual-agent/surveys.md

# Surveys

> Collect customer satisfaction feedback after interactions with agents and AI systems.

Surveys allow you to gather customer satisfaction (CSAT) feedback following interactions with Virtual Agents or Generative Agents. This feature helps you evaluate and improve your support quality by capturing structured feedback directly from customers.

With surveys, you can:

* **Capture structured feedback** on agent and AI interactions
* **Use survey data** for reporting and automation optimization
* **Reduce manual feedback collection** or disjointed tools
* **Improve CSAT** without disrupting the user experience

## Survey Types

ASAPP supports three types of surveys:

* **Virtual Agent Surveys**: Collect feedback after interactions with automated Virtual Agent flows.
  * These surveys are triggered only at the end of Virtual Agent interactions.

* **Generative Agent Surveys**: Collect feedback after interactions with AI-powered Generative Agents.
  * These surveys are triggered only at the end of Generative Agent interactions, not when escalating from Virtual Agent to Generative Agent, to avoid redundant feedback collection.

## Setting up Surveys

Each survey type has a different setup process:

<Tabs>
  <Tab title="Virtual Agent Surveys">
    Virtual Agent surveys must be configured and are then triggered at the end of the Virtual Agent interaction when the final flow ends with SRS options and the customer selects the positive outcome.

    <Steps>
      <Step title="Enable Virtual Agent Surveys">
        Work with your ASAPP account team to enable Virtual Agent surveys for your organization.

        <Warning>
          Virtual Agent surveys are disabled by default and require ASAPP assistance to enable.
        </Warning>
      </Step>

      <Step title="Customize Form">
        Once enabled, you can edit the survey form which determines what information is collected from the customer.

        1. Navigate to Company Resources > Library > Forms
        2. Select Virtual AgentFeedback Survey Form
        3. Modify the form according to your business needs
        4. Save the form
      </Step>

      <Step title="Customize Survey Settings">
        Once the form is created, you can customize the survey settings.

        1. Navigate to VirtualAgent > Core Dialog
        2. Select "VirtualAgentCSATSurveyFlow"
        3. Modify the settings according to your business needs
        4. Save and deploy the settings
      </Step>

      <Step title="Test the Survey">
        Once the survey is enabled and configured, you can test it by walking through a flow that ends with SRS options. Preview the flow, follow through the flow, and select the positive outcome.

        The survey should appear at the end of the flow.
      </Step>
    </Steps>
  </Tab>

  <Tab title="Generative Agent Surveys">
    Generative Agent surveys must be configured and are then triggered at the end of the Generative Agent interaction when GenerativeAgent returns control to VirtualAgent with a specific system transfer.

    <Steps>
      <Step title="Enable Generative Agent Surveys">
        Work with your ASAPP account team to enable Generative Agent surveys for your organization.

        <Warning>
          Generative Agent surveys are disabled by default and require ASAPP assistance to enable.
        </Warning>
      </Step>

      <Step title="Create Survey Intent">
        Create an intent that maps to a flow that opens the Generative Agent survey form.

        1. Navigate to VirtualAgent > Intents
        2. Create a new intent (e.g., "survey\_feedback")
        3. Map this intent to a flow that opens the survey form
        4. Save the intent configuration
      </Step>

      <Step title="Create System Transfer Function">
        Create or modify a system transfer function to return a key/value pair for survey triggering.

        1. Navigate to GenerativeAgent > Functions
        2. Create or modify a system transfer function
        3. Configure the function to return in the output variables:
           * Key: `external_intent`
           * Value: The intent name you created in the previous step
        4. Save the function configuration
      </Step>

      <Step title="Modify Generative Agent Tasks">
        Add the system transfer function to relevant Generative Agent tasks to enable survey triggering.
      </Step>

      <Step title="Test the Survey">
        Once the survey is enabled and configured, you can test it by walking through a flow that engages GenerativeAgent and follow the conversation to trigger the return of control to VirtualAgent.

        The survey should appear after the GenerativeAgent returns control to VirtualAgent.
      </Step>
    </Steps>
  </Tab>
</Tabs>

## Third-Party Survey Support

You can use third-party survey providers to collect feedback from your customers, such as Qualtrics. This results in displaying a survey link for the user to click into the third-party survey tool.

Results from external surveys are integrated into your reporting.

To use a third-party survey provider, work with your ASAPP account team to configure the survey settings to display the survey link.

## Survey Results and Reporting

Survey results are automatically stored and viewable in Conversation Manager.

<Warning>
  Results are not available in Conversation Manager for third-party surveys.
</Warning>

Events will be created for when a survey is displayed and when a survey is submitted. This data is available via the [ASAPP Messaging Feeds](/reporting/retrieve-messaging-data).

## Next Steps

<CardGroup>
  <Card title="Flows" href="/agent-desk/virtual-agent/flows">
    Learn how to build and configure flows for your Virtual Agent interactions.
  </Card>

  <Card title="Intent Routing" href="/agent-desk/virtual-agent/intent-routing">
    Understand how to route customer intents to appropriate flows and surveys.
  </Card>
</CardGroup>
