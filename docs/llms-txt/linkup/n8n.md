# Source: https://docs.linkup.so/pages/integrations/n8n/n8n.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# n8n

> Connect your n8n workflow to an internet search

## Overview

We are actively working on creating a Linkup node for [n8n](https://n8n.io).
In the meantime, follow this tutorial to get contextual information from the internet.

## Configuration Steps

<Steps>
  <Step title="Open your n8n account and create a workflow">
    Go to Workflows > Create Workflows
    <img src="https://mintcdn.com/linkup-8b5c238e/ht3XJF6azWwbELaV/pages/integrations/n8n/assets/create_workflow.png?fit=max&auto=format&n=ht3XJF6azWwbELaV&q=85&s=b076f86d61c8c110a851fcc3e419cfc4" alt="n8n" width="2946" height="1480" data-path="pages/integrations/n8n/assets/create_workflow.png" />
  </Step>

  <Step title="Add a trigger">
    Click on the + button to add a trigger
    <img src="https://mintcdn.com/linkup-8b5c238e/ht3XJF6azWwbELaV/pages/integrations/n8n/assets/create_trigger.png?fit=max&auto=format&n=ht3XJF6azWwbELaV&q=85&s=dae4043fed14bddf8ad8d0ba0a7144e5" alt="n8n" width="3004" height="1546" data-path="pages/integrations/n8n/assets/create_trigger.png" />
  </Step>

  <Step title="Select your trigger">
    Choose your trigger (Trigger Manually is selected in this example)
    <img src="https://mintcdn.com/linkup-8b5c238e/ht3XJF6azWwbELaV/pages/integrations/n8n/assets/add_trigger.png?fit=max&auto=format&n=ht3XJF6azWwbELaV&q=85&s=d067dd9dd523bf2d4dd6a095d7e7f15c" alt="n8n" width="2720" height="1392" data-path="pages/integrations/n8n/assets/add_trigger.png" />
  </Step>

  <Step title="Add HTTP Request node">
    Click on the + button > Core > HTTP Request
    <img src="https://mintcdn.com/linkup-8b5c238e/ht3XJF6azWwbELaV/pages/integrations/n8n/assets/step1_action.png?fit=max&auto=format&n=ht3XJF6azWwbELaV&q=85&s=3536b149aebf5a1e6de5c637184c6a83" alt="n8n" width="2618" height="1290" data-path="pages/integrations/n8n/assets/step1_action.png" />
    <img src="https://mintcdn.com/linkup-8b5c238e/ht3XJF6azWwbELaV/pages/integrations/n8n/assets/add_action.png?fit=max&auto=format&n=ht3XJF6azWwbELaV&q=85&s=95fff7553b0bf33fb225afcaa2f6efc8" alt="n8n" width="2618" height="1366" data-path="pages/integrations/n8n/assets/add_action.png" />
  </Step>

  <Step title="Configure HTTP method">
    Select POST as Method
    <img src="https://mintcdn.com/linkup-8b5c238e/ht3XJF6azWwbELaV/pages/integrations/n8n/assets/select_post.png?fit=max&auto=format&n=ht3XJF6azWwbELaV&q=85&s=535b345f1a50b0d1009a010ca1a57bc5" alt="n8n" width="889" height="834" data-path="pages/integrations/n8n/assets/select_post.png" />
  </Step>

  <Step title="Enter API endpoint">
    Enter `https://api.linkup.so/v1/search` in URL
    <img src="https://mintcdn.com/linkup-8b5c238e/ht3XJF6azWwbELaV/pages/integrations/n8n/assets/enter_url.png?fit=max&auto=format&n=ht3XJF6azWwbELaV&q=85&s=153e67a3390d610479a73621aecb95ce" alt="n8n" width="824" height="512" data-path="pages/integrations/n8n/assets/enter_url.png" />
  </Step>

  <Step title="Set up authentication">
    In Authentication, select "Predifined Credential Type"
    <img src="https://mintcdn.com/linkup-8b5c238e/ht3XJF6azWwbELaV/pages/integrations/n8n/assets/choose_auth.png?fit=max&auto=format&n=ht3XJF6azWwbELaV&q=85&s=40713b0d306cd6201e5a163a6530650a" alt="n8n" width="892" height="524" data-path="pages/integrations/n8n/assets/choose_auth.png" />
  </Step>

  <Step title="Credential Type">
    In Credential Type, select "Bearer Auth"
    <img src="https://mintcdn.com/linkup-8b5c238e/ht3XJF6azWwbELaV/pages/integrations/n8n/assets/bearer_auth.png?fit=max&auto=format&n=ht3XJF6azWwbELaV&q=85&s=f1aa15c15b7c9a8b52bfc1cf4cd43d09" alt="n8n" width="810" height="354" data-path="pages/integrations/n8n/assets/bearer_auth.png" />
  </Step>

  <Step title="Create new credential">
    In Bearer Auth, click on "+ Create new credential"
    <img src="https://mintcdn.com/linkup-8b5c238e/ht3XJF6azWwbELaV/pages/integrations/n8n/assets/create_cred.png?fit=max&auto=format&n=ht3XJF6azWwbELaV&q=85&s=fcaf5a1e583fa66f64db749e607a42ab" alt="n8n" width="692" height="236" data-path="pages/integrations/n8n/assets/create_cred.png" />
  </Step>

  <Step title="Add Bearer Token">
    Copy your Linkup API key in the Bearer Token field, click save and close the window

    <Card title="Get your API key" icon="key" href="https://app.linkup.so" horizontal="True">
      Create a Linkup account for free to get your API key.
    </Card>

        <img src="https://mintcdn.com/linkup-8b5c238e/ht3XJF6azWwbELaV/pages/integrations/n8n/assets/bearer.png?fit=max&auto=format&n=ht3XJF6azWwbELaV&q=85&s=c913c10473e91c0a9fa58fa491ca965e" alt="n8n" width="2092" height="1288" data-path="pages/integrations/n8n/assets/bearer.png" />
  </Step>

  <Step title="Enable request body">
    Toggle on "Send Body"
    <img src="https://mintcdn.com/linkup-8b5c238e/ht3XJF6azWwbELaV/pages/integrations/n8n/assets/swipe_button.png?fit=max&auto=format&n=ht3XJF6azWwbELaV&q=85&s=b333d1e44a5e4b1338b5e60de0997487" alt="n8n" width="878" height="301" data-path="pages/integrations/n8n/assets/swipe_button.png" />
  </Step>

  <Step title="Body Content Type">
    Select "JSON" as the Content Type
    <img src="https://mintcdn.com/linkup-8b5c238e/ht3XJF6azWwbELaV/pages/integrations/n8n/assets/json_content_type.png?fit=max&auto=format&n=ht3XJF6azWwbELaV&q=85&s=b8b2b7017253009de46adcc013314bb8" alt="n8n" width="738" height="372" data-path="pages/integrations/n8n/assets/json_content_type.png" />
  </Step>

  <Step title="Specify Body">
    Select "Using JSON" as the Specify Body option
    <img src="https://mintcdn.com/linkup-8b5c238e/ht3XJF6azWwbELaV/pages/integrations/n8n/assets/using_json.png?fit=max&auto=format&n=ht3XJF6azWwbELaV&q=85&s=25b5cdbefad4f1141d321af1c86433d4" alt="n8n" width="722" height="308" data-path="pages/integrations/n8n/assets/using_json.png" />
  </Step>

  <Step title="JSON Body">
    Use JSON to specify your search parameters

    ```json  theme={null}
    {
      "q": "How's the weather in Paris today?",
      "depth": "standard",
      "outputType": "sourcedAnswer"
    }
    ```

    <img src="https://mintcdn.com/linkup-8b5c238e/ht3XJF6azWwbELaV/pages/integrations/n8n/assets/json_body.png?fit=max&auto=format&n=ht3XJF6azWwbELaV&q=85&s=58a800dcf65f40c813b8002262b4f92c" alt="n8n" width="750" height="252" data-path="pages/integrations/n8n/assets/json_body.png" />
    Save and run your workflow.
  </Step>
</Steps>

You are all set to use Linkup in your n8n workflow! Visit the [Concepts](/pages/documentation/get-started/concepts) page to learn more about the different Linkup parameters.

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


Built with [Mintlify](https://mintlify.com).