# Source: https://pipedream.com/docs/workflows/building-workflows/code/nodejs/ai-code-generation.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Using AI To Generate Code

<Frame>
  <iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/gPk26iWDCb8" title="Generate Pipedream Node.js code with A.I." frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</Frame>

Tell Pipedream the code you want, we generate it for you.

<Frame>
  <img src="https://res.cloudinary.com/pipedreamin/image/upload/v1710515666/docs/workflows/building-workflows/code/nodejs/ai-code-generation/CleanShot_2024-03-15_at_11.13.07_mjgmdc.gif" />
</Frame>

Pipedream’s [built-in actions](/workflows/building-workflows/actions/) are great for running common API operations without having to write code, but sometimes you need code-level control in a workflow. You can [write this code yourself](/workflows/building-workflows/code/), or you can let Pipedream generate it for you with AI.

This feature is new, and [we welcome feedback](https://pipedream.com/support). Please let us know what we can improve or add to make this more useful for you.

## Getting Started

Access the feature either from within a Node.js code cell or from any app in the step selector.

<Frame>
  <img src="https://mintcdn.com/pipedream/Acz4Z1ch6TM7-aI8/images/a305491c-image.png?fit=max&auto=format&n=Acz4Z1ch6TM7-aI8&q=85&s=526875a9bf935d5c9c9ba72471b3536e" width="1345" height="798" data-path="images/a305491c-image.png" />
</Frame>

A window should pop up and ask for your prompt. Write exactly what you want to do within that step. **Be verbose** and see our tips for [getting the best results](/workflows/building-workflows/code/nodejs/ai-code-generation/#getting-the-best-results).

* **Bad**: “Send a Slack message”
* **Good**: “Send a Slack message in the following format: `Hello, ${name}`. Let me select the channel from a list of available options.”

Once you’re done, hit **Enter** or click **Generate**.

Code will immediately start streaming to the editor. You can modify the prompt and re-generate the code if it doesn’t look right, or click **Use this code** to add it to your code cell and test it.

Pipedream will automatically refresh the step to show connected accounts and any input fields (props) above the step.

<Frame>
  <img src="https://mintcdn.com/pipedream/nKh6d_6A4aXFb6xD/images/feabc2db-ai-generated-code_uzsr8q.png?fit=max&auto=format&n=nKh6d_6A4aXFb6xD&q=85&s=58793275e673a9f6816131d0ce7fbfd6" width="1786" height="1330" data-path="images/feabc2db-ai-generated-code_uzsr8q.png" />
</Frame>

Edit the code however you’d like. Once you’re done, test the code. You’ll see the option to provide a :+1: or :-1: on the code, which helps us learn what’s working and what’s not.

## Editing existing code

You can also edit existing code with AI. Click the **Edit with AI** button at the top-right of any Node.js code step. You’ll see the code gen window appear with the original code from your step. Enter a prompt to suggest an edit, and we’ll give you the modified code.

<Frame>
  <img src="https://res.cloudinary.com/pipedreamin/image/upload/v1710515922/docs/workflows/building-workflows/code/nodejs/ai-code-generation/CleanShot_2024-03-15_at_11.17.20_pumcgn.gif" />
</Frame>

## Getting the best results

**Generating code works best with clear, precise, and detailed instructions of what you want to do in your step.** The code gen service understands the [Pipedream component API](/components/contributing/api/) and references the API docs of [integrated apps](https://pipedream.com/apps). For example, you can tell it to include specific [props](/components/contributing/api/#props) (input) or [async options](/components/contributing/api/#async-options-example), and reference specific API endpoints you want to use for the selected app.

### Examples

#### Slack

Send a message to the `#general` channel that says, “This message was sent with AI-generate code!” Format it as a Slack block, with a header named, “Hello, world!”

**Output**:

```php  theme={null}
import { axios } from "@pipedream/platform";
 
export default defineComponent({
  props: {
    slack: {
      type: "app",
      app: "slack",
    },
  },
  async run({ steps, $ }) {
    return await axios($, {
      method: "POST",
      url: `https://slack.com/api/chat.postMessage`,
      headers: {
        Authorization: `Bearer ${this.slack.$auth.oauth_access_token}`,
      },
      data: {
        channel: "#general",
        blocks: [
          {
            type: "header",
            text: {
              type: "plain_text",
              text: "Hello, world!",
            },
          },
          {
            type: "section",
            text: {
              type: "mrkdwn",
              text: "This message was sent with AI-generated code!",
            },
          },
        ],
      },
    });
  },
});
```

#### Stripe

Get the subscription information about a specific customer based on their email address

**Output:**

```php  theme={null}
import { axios } from "@pipedream/platform";
 
export default defineComponent({
  props: {
    stripe: {
      type: "app",
      app: "stripe",
    },
    email: {
      type: "string",
      label: "Email Address",
      description:
        "The email address of the customer to get subscription information for",
    },
  },
  async run({ steps, $ }) {
    const customerResponse = await axios($, {
      method: "GET",
      url: `https://api.stripe.com/v1/customers`,
      headers: {
        Authorization: `Bearer ${this.stripe.$auth.api_key}`,
      },
      params: {
        email: this.email,
      },
    });
 
    if (customerResponse.data.length === 0) {
      throw new Error("Customer not found");
    }
 
    const customerId = customerResponse.data[0].id;
 
    return await axios($, {
      method: "GET",
      url: `https://api.stripe.com/v1/subscriptions`,
      headers: {
        Authorization: `Bearer ${this.stripe.$auth.api_key}`,
      },
      params: {
        customer: customerId,
      },
    });
  },
});
```

## Current limitations, and what we’re working on next

* Currently supports Pipedream actions, not triggers
* Only supports Node.js output. Python coming soon.
* It supports single steps, and not entire workflows (also coming soon)

Built with [Mintlify](https://mintlify.com).
