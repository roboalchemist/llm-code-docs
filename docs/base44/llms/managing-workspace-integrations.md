# Source: https://docs.base44.com/documentation/integrations/managing-workspace-integrations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing workspace API integrations

> Connect shared APIs once and reuse them across every app in your shared workspace.

Workspace integrations let you register shared external APIs at the workspace level from an OpenAPI specification. You import a spec (URL or JSON), select up to 30 operations, and connect the API once in your shared workspace. Any app in that workspace can then call those approved operations via `base44.integrations.custom.call()`, instead of setting up its own connection. This works for both internal APIs and partner APIs that your team depends on.

These integrations are designed to be secure and reliable. Sensitive auth headers are stored as encrypted workspace secrets and are never sent back to the browser. At runtime, calls are proxied server side with protections against server side request forgery (SSRF), and workspace headers take precedence so apps cannot override them. Editing an integration uses the stored specification rather than the live URL, and saving is blocked if headers fail to load so you do not lose them by mistake.

<Frame caption="Integrations in a shared workspace in Base44">
    <img src="https://mintcdn.com/base44/pXMR2fd6LoL4mN_A/images/intgs.png?fit=max&auto=format&n=pXMR2fd6LoL4mN_A&q=85&s=e3d535ce0a0ba4ac282d03c1059660d7" alt="Integrations in a shared workspace in Base44" width="1439" height="373" data-path="images/intgs.png" />
</Frame>

<Warning>
  **Important:**

  * Workspace integrations are only available in **shared workspaces**.
  * Access to workspace integrations is restricted to workspace admins and owners on a **Builder** plan or higher.
  * Any teammate in the shared workspace can use an existing workspace integration in their apps, even on a free plan.
</Warning>

***

## Understanding workspace integrations

A workspace integration is a shared connection from your workspace to an external or internal API, such as a CRM, support system or custom backend. You define it once in your shared workspace from an OpenAPI or Swagger specification, choose which operations are allowed, and any compatible app in that workspace can call those operations. This keeps configuration in one place and makes it easier to manage the external systems your team relies on.

**Workspace integrations are useful when you want to:**

* Use the same external or internal API across multiple apps in the same shared workspace
* Keep sensitive details such as API keys and tokens in one secure place, managed as workspace secrets
* Limit which endpoints are available so apps only call approved, spec defined operations
* Keep a clear separation from one click OAuth connectors, as workspace integrations are workspace managed and spec driven
* Make it clear which external systems your shared workspace relies on

***

## Creating an integration

Create a custom workspace integration when you want to expose a new external API to your apps and that API has an OpenAPI or Swagger specification. Base44 reads the specification, lets you choose the endpoints you want to expose, and creates a reusable integration for your shared workspace.

<Note>
  **Before you begin:** Make sure you have access to a valid OpenAPI or Swagger specification for the API you want to use. You can either host it at a public URL or copy the JSON.
</Note>

### Step 1 | Add a new integration

1. Click your **profile** icon at the top right of your workspace.
2. Click **Settings.**
3. Click **Integrations**.
4. Click **New Integration**.
5. Choose how you want to provide your API specification:
   * **From URL:** Enter the public URL of your OpenAPI or Swagger file in the **OpenAPI Specification URL** field, for example `https://api.example.com/openapi.json`.
   * **Paste JSON:** Paste the full JSON definition of your OpenAPI or Swagger specification into the editor.
6. Click **Continue**.

<Frame caption="Adding a custom integration in a shared workspace">
  <img src="https://mintcdn.com/base44/dZzytOu9j0oe_U9j/images/step1again.png?fit=max&auto=format&n=dZzytOu9j0oe_U9j&q=85&s=998a5ac6f68d97d2a6e7883276070548" alt="Adding a custom integration in a shared workspace" title="Adding a custom integration in a shared workspace" className="mx-auto" style={{ width:"67%" }} width="1186" height="976" data-path="images/step1again.png" />
</Frame>

### Step 2 | Select endpoints to expose

Select up to 30 endpoints for your integration.

**To select endpoints:**

1. Review the list of endpoints that Base44 discovers from your specification. You can use the search box to find specific paths or operations by method or path name.
2. Select the checkboxes for the endpoints you want to expose to your workspace.
3. Click **Continue**.

<Frame caption="Selecting the endpoints to expose for your workspace integration">
  <img src="https://mintcdn.com/base44/dZzytOu9j0oe_U9j/images/step2.png?fit=max&auto=format&n=dZzytOu9j0oe_U9j&q=85&s=2c9e579cce16c3c548443170416c9fc3" alt="Selecting the endpoints to expose for your workspace integration" title="Selecting the endpoints to expose for your workspace integration" className="mx-auto" style={{ width:"72%" }} width="1190" height="984" data-path="images/step2.png" />
</Frame>

### Step 3 | Configure your integration

Configure your integration details, set the base URL, and add any custom headers that your API needs. Sensitive header values stay protected. Common auth headers such as `authorization`, `x-api-key`, `api-key`, `x-auth-token`, `x-access-token`, `x-secret-key`, `bearer`, `secret`, `password` and `credential` are always treated as secrets. Their values are stored as encrypted workspace secrets, never sent back to the browser, and show as “sensitive – delete to change” when you edit the integration.

**To configure your integration:**

1. Set the details for your integration:
   * **Slug**: Enter a URL friendly identifier for the integration, for example my-api.
   * **Name**: Enter the display name that appears in your workspace integrations list.
   * **Description**: Describe what the integration does so teammates know when to use it.
   * **Base URL**: Confirm or update the base URL for your API.
2. If your API requires headers that must be sent with every request, add them in the **Custom Headers** section:
   1. Click **Add Header**.
   2. Enter the header name, such as Authorization or X API Key.
   3. Enter the header value, such as your API key or token.
   4. Use the visibility icon to hide or reveal the header value as needed.
3. Review the list of selected endpoints at the bottom of the dialog.
4. Click **Create Integration**.

<Frame caption="Configuring your workspace integration">
  <img src="https://mintcdn.com/base44/vGj5ZIaYUxXljz-f/images/configure.png?fit=max&auto=format&n=vGj5ZIaYUxXljz-f&q=85&s=56883c536d3042bc22ba14c5043ab207" alt="Configuring your workspace integration" className="mx-auto" style={{ width:"81%" }} width="1166" height="986" data-path="images/configure.png" />
</Frame>

***

## Managing workspace integrations

After you create a workspace integration, it appears in the Integrations tab of your shared workspace. From there, you can view its details, edit settings or remove it if you no longer need it.

### Viewing integration details

1. Click your **profile** icon at the top right of your workspace.
2. Click **Settings.**
3. Click **Integrations**.
4. View the integration you want to inspect and expand the endpoints.

### Editing an integration

1. Click your **profile** icon at the top right of your workspace.
2. Click **Settings.**
3. Click **Integrations**.
4. Click the **More Actions** icon <Icon icon="ellipsis-vertical" /> on the integration card.
5. Click **Edit**.
6. Update the fields you need and save your changes.

<Frame caption="Editing a workspace integration">
    <img src="https://mintcdn.com/base44/Gl7XCv8esPzAOeqF/images/editint.png?fit=max&auto=format&n=Gl7XCv8esPzAOeqF&q=85&s=ae8362746fc747c68c52a26b07d24e4f" alt="Editing a workspace integration" width="1445" height="462" data-path="images/editint.png" />
</Frame>

<Tip>
  **Tip:** If you need to expose additional endpoints from the same API, consider creating a new integration or updating the existing one based on how you want apps to use it.
</Tip>

### Deleting an integration

1. Click your **profile** icon at the top right of your workspace.
2. Click **Settings.**
3. Click **Integrations**.
4. Click the **More Actions** icon <Icon icon="ellipsis-vertical" />on the integration card.
5. Click **Delete**.
6. Click **Delete** again to confirm that you want to remove it from the shared workspace.

<Frame caption="Deleting a workspace integration">
    <img src="https://mintcdn.com/base44/Gl7XCv8esPzAOeqF/images/deleteint.png?fit=max&auto=format&n=Gl7XCv8esPzAOeqF&q=85&s=926253d2eb08ecf5447ef69435a2a5c0" alt="Deleting a workspace integration" width="1460" height="459" data-path="images/deleteint.png" />
</Frame>

<Warning>
  **Important:** Deleting a workspace integration can break any app level integrations that depend on it. Make sure you review active apps before you remove a shared integration.
</Warning>

***

## FAQs

Click a question below to learn more about workspace integrations.

<AccordionGroup>
  <Accordion title="How do I use a workspace integration in my app?">
    After you create a workspace integration in a shared workspace, any new apps you build in that workspace can use it.

    When you create a new app, Base44 checks your workspace integrations. If you mention one of those systems in your first prompt, it automatically uses the matching workspace integration. For example, if you already added a GitHub API integration and you say “Create an app based on my GitHub issues,” Base44 uses the GitHub integration that is configured for the workspace without you needing to select it.

    You can then review and adjust how the app uses that integration from the app’s integrations settings.
  </Accordion>

  <Accordion title="Who can create and manage workspace integrations?">
    To create or manage workspace integrations, you need to be in a shared workspace, have a Builder plan or higher, and have access to the **Integrations** tab in the workspace. If you do not see the **Add Integration** button or edit options, contact your workspace admin and ask them to either update your role or create the integration for you.
  </Accordion>

  <Accordion title="What happens if the OpenAPI specification changes?">
    If the API owner updates the specification at the URL you used, the details that Base44 reads from it can change the next time you update or recreate the integration. When you know the spec changed, review your workspace integration and check that the exposed endpoints still match what your apps expect.
  </Accordion>

  <Accordion title="Are header values stored securely and who can see them?">
    Header values such as API keys and tokens are stored as part of the workspace integration configuration. Only teammates with permission to manage workspace integrations in a shared workspace can view or edit these values. Use the visibility icon in the Configure step to hide values on screen when you work in shared spaces.
  </Accordion>

  <Accordion title="Can I have more than one workspace integration for the same API?">
    Yes. You can create multiple workspace integrations that point to the same external API. For example, you might create separate integrations for sandbox and production environments, or for different sets of endpoints that are used by different apps.
  </Accordion>

  <Accordion title="How should I rotate API keys or other secrets used by a workspace integration?">
    When you need to rotate a key or token, generate the new credential in the external system first. Then edit the workspace integration, update the relevant header value with the new key or token and save your changes. After you update the workspace integration, apps that use it start sending the new value automatically.
  </Accordion>

  <Accordion title="What should I do if my OpenAPI specification gives a parsing error?">
    Check that the URL points directly to a valid OpenAPI or Swagger JSON or YAML file and that it is publicly accessible from your browser. If the file is behind authentication or served as HTML, Base44 cannot parse it.

    If you still see errors, switch to the Paste JSON option, copy the raw JSON of your specification and try again.

    For a quick test, you can also try a known valid spec such as a public sample API to confirm that the flow works.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).