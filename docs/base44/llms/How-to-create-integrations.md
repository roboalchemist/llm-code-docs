# Source: https://docs.base44.com/Integrations/How-to-create-integrations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom integrations

> Build, test, and use your own custom integrations in Base44 without backend coding.

<Warning>
  **Important:** You can no longer create custom integrations. After March 1, 2026 you will not be able to add existing custom integrations from the catalog to your apps. Any apps that already use a custom integration will continue to work as before.
</Warning>

## Troubleshooting

Click a topic to troubleshoot.

<AccordionGroup>
  <Accordion title="The integration returns a 'missing prompt' or 'missing input' error" icon="wrench">
    Most API-powered integrations require some input to process requests, such as a text prompt. Make sure you’ve entered a prompt or other required input before sending the request to the integration.

    **OpenAI example:** For an image generator, a prompt like `Generate an image of...`
  </Accordion>

  <Accordion title="The integration returns an 'invalid API key' error" icon="wrench">
    This usually means the API key or secret entered is incorrect, expired, or missing. Make sure you’ve copied the API key correctly and that it is still valid.

    **OpenAI example:** OpenAI keys start with `sk-`. Get a new key from [platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys) if needed.
  </Accordion>

  <Accordion title="Integration does not appear in the catalog" icon="wrench">
    Make sure you clicked **Save Integration** and set the visibility to **Public** if you want it reviewed for the catalog. Private integrations only show in your workspace’s **private catalog**.
  </Accordion>

  <Accordion title="I get a generic API error or nothing happens" icon="wrench">
    Some APIs have rate limits, temporary failures, or maintenance windows. Wait a few minutes and try again, or check the provider’s status page for any issues on their end.
  </Accordion>

  <Accordion title="The integration returns an error from the provider." icon="wrench">
    Confirm the secret value, the endpoint URL, required headers, and request body. Check provider status and rate limits. Review responses in your backend function for error messages.
  </Accordion>
</AccordionGroup>

## FAQs

Click on a question below to learn more about creating custom integrations in Base44.

<AccordionGroup>
  <Accordion title="Where do I put my actual API keys?">
    Enter the real values **per app** in **Dashboard** → **Secrets**, or when prompted during app setup. The catalog never stores your secret values.
  </Accordion>

  <Accordion title="Can I use the same secret across multiple apps?">
    Yes. Add the secret to each app that uses the integration. You can reuse an existing value in the app or paste a new one.
  </Accordion>

  <Accordion title="Can I edit an integration after publishing?">
    Yes, you can update your custom integration at any time. Open it in the **My Integrations** tab to make any changes. For public integrations, updates may be reviewed again.

        <img src="https://mintcdn.com/base44/ZzpPpL_KXd9Ncr9W/images/ManageCustomIntegration.png?fit=max&auto=format&n=ZzpPpL_KXd9Ncr9W&q=85&s=b890afa347b4eee02afd9c2ad1dae3ac" alt="Managing your custom integration in Base44." width="823" height="193" data-path="images/ManageCustomIntegration.png" />
  </Accordion>

  <Accordion title="Can my teammates use my private integration?">
    Yes. Anyone in your workspace can use custom integrations in your **private catalog** once they have access to the app that uses it.
  </Accordion>

  <Accordion title="Does the custom integration expose my API key to end users?">
    No. Keys are stored per app and accessed only by the backend function. They are not shown in the UI or client.
  </Accordion>

  <Accordion title="Can I update an API key after I've added it to an app?">
    Yes, you can update your keys anytime in your app's **Dashboard** → **Secrets**.
  </Accordion>

  <Accordion title="What happens if my integration isn't approved for the catalog?">
    It stays in your **private catalog**. You can update the description, instructions, or code, and then resubmit for review.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).