# Source: https://www.courier.com/docs/platform/workspaces/environments-api-keys.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Environments, API Keys, and Assets

> Courier provides isolated Test and Production environments with distinct API keys, enabling safe template development, testing, asset migration, and integration management without affecting live data or configurations.

Every Courier workspace has two environments: **Production** and **Test**. The two environments are fully isolated; all assets within them (templates, brands, tags, subscription topics, integrations, API keys, log data) belong only to that environment.

## Production and Test Environments

Any changes made to a template and its associated assets are only applied within the current environment until you migrate the template and overwrite any changes to the corresponding `Notification ID` and assets in the other environment.

## Switching Between Environments

Use the environments toggle in the lower-left settings menu to switch between your Production and Test environments. Look for the `Test Environment` indicator at the top of the application window to confirm that you're in the test environment.

<Frame caption="Use the Environments Toggle to Switch Between Environments">
  <img src="https://mintcdn.com/courier-4f1f25dc/4A6zrFrERiXvAT84/assets/platform/content/environments-switch-toggle.png?fit=max&auto=format&n=4A6zrFrERiXvAT84&q=85&s=75f5cfc97c0cc94689e66f740d2b1304" alt="Use the Environments Toggle to Switch Between Environments" width="1796" height="1014" data-path="assets/platform/content/environments-switch-toggle.png" />
</Frame>

<Info>
  Simply switching from **Production** to **Test** does not impact your notifications in either environment in any way. It just changes the environment you are viewing.
</Info>

## API Keys and Environments

Each environment has its own [API keys](https://app.courier.com/settings/api-keys) that determine which environment and state your requests target.

### New workspaces

New workspaces receive keys with the `token_` prefix. By default you get two keys:

* **Production (published)** - targets live, published templates and data
* **Test (published)** - targets test environment published templates and data

You can generate additional keys (including draft keys) from [Settings > API Keys](https://app.courier.com/settings/api-keys). Each key is scoped to a specific environment and state.

### Legacy workspaces

Older workspaces use prefix-based keys that encode the environment and state:

* **pk\_prod\_** - published data in the Production environment
* **dk\_prod\_** - draft data in the Production environment
* **pk\_test\_** - published data in the Test environment
* **dk\_test\_** - draft data in the Test environment

<Note>
  Both key formats work the same way. The scope (environment + state) is stored server-side; the prefix is a convenience for identifying which key you're using.
</Note>

<Frame caption="Your Test Environment API Keys">
  <img src="https://mintcdn.com/courier-4f1f25dc/4A6zrFrERiXvAT84/assets/platform/content/environments-api-keys.png?fit=max&auto=format&n=4A6zrFrERiXvAT84&q=85&s=c9cd3f3333e3090c1654e5e12163feec" alt="Your Test Environment API Keys" width="3454" height="1922" data-path="assets/platform/content/environments-api-keys.png" />
</Frame>

### Define the Routing Behavior of Custom API Keys

Business Tier customers can also define the routing behavior of their API keys. A `mock` key simulates the full notification lifecycle without invoking the downstream provider, so you can see how a request flows through Courier without incurring any send cost.

<Frame caption="Define Routing Behavior for Custom API Keys">
  <img src="https://mintcdn.com/courier-4f1f25dc/chScP2cd3sUGw2yg/assets/platform/workspaces/environments-api-routing.png?fit=max&auto=format&n=chScP2cd3sUGw2yg&q=85&s=0c943d99f5bf052b0e51658b73466e57" alt="Define Routing Behavior for Custom API Keys" width="1814" height="1288" data-path="assets/platform/workspaces/environments-api-routing.png" />
</Frame>

## Notifications, Assets and Environments

You can move a template and its associated assets (brands, tags, subscription topics) between environments in either direction. You can also select a destination workspace when migrating assets.

To copy a template between environments, Courier also copies all dependencies attached to it so functionality is preserved. After you've copied associated assets once (e.g. a brand or category), you can choose to overwrite them in future migrations.

<Info>
  Courier will copy the current template. All other assets copied will be their most recent published version.
</Info>

### Migrating Templates and Assets Between Environments

1. Open the notification you wish to migrate.
2. Open the dropdown menu in the 'Publish Changes' button.
3. Select 'Migrate Assets'.

<Frame caption="Migrate Your Template and Assets">
  <img src="https://mintcdn.com/courier-4f1f25dc/ocKTSyLlc6Ky9Ivc/assets/platform/workspaces/environments-migrate-assets.png?fit=max&auto=format&n=ocKTSyLlc6Ky9Ivc&q=85&s=f4378611567920d81f9aca5bb01d30dd" alt="Migrate Your Template and Assets" width="2866" height="1438" data-path="assets/platform/workspaces/environments-migrate-assets.png" />
</Frame>

<Frame caption="Click the 'Copy Assets' Button to be Prompted by a Confirmation Modal">
  <img src="https://mintcdn.com/courier-4f1f25dc/ocKTSyLlc6Ky9Ivc/assets/platform/workspaces/environments-copy-assets.png?fit=max&auto=format&n=ocKTSyLlc6Ky9Ivc&q=85&s=5dcface643a675e972cea6bc6e609412" alt="Click the 'Copy Assets' Button to be Prompted by a Confirmation Modal" width="498" height="256" data-path="assets/platform/workspaces/environments-copy-assets.png" />
</Frame>

4. **Select either 'Copy Assets' or 'Copy And Publish' option.**

<Frame caption="Copy Templates and Assets Confirmation Modal">
  <img src="https://mintcdn.com/courier-4f1f25dc/ocKTSyLlc6Ky9Ivc/assets/platform/workspaces/environments-publish-assets.png?fit=max&auto=format&n=ocKTSyLlc6Ky9Ivc&q=85&s=52127d270c4132fbf6fe15bb431dc980" alt="Copy Templates and Assets Confirmation Modal" width="2318" height="1454" data-path="assets/platform/workspaces/environments-publish-assets.png" />
</Frame>

<Frame caption="Confirm by Selecting 'Copy And Publish'">
  <img src="https://mintcdn.com/courier-4f1f25dc/ocKTSyLlc6Ky9Ivc/assets/platform/workspaces/environments-copy-publish.png?fit=max&auto=format&n=ocKTSyLlc6Ky9Ivc&q=85&s=7f64343cf1e7955b8f37ff5e20aac657" alt="Confirm by Selecting 'Copy And Publish'" width="826" height="238" data-path="assets/platform/workspaces/environments-copy-publish.png" />
</Frame>

### Migrating Templates to Another Workspace

If you have multiple workspaces, you can migrate a template to another workspace from the same modal.

1. In the migrate assets modal, choose a `Destination Workspace` from the dropdown menu.

<Frame caption="Select Destination Workspace From Dropdown">
  <img src="https://mintcdn.com/courier-4f1f25dc/ocKTSyLlc6Ky9Ivc/assets/platform/workspaces/environments-workspace-copy.png?fit=max&auto=format&n=ocKTSyLlc6Ky9Ivc&q=85&s=6730c2d7b3ed460bce7ce41c3950c040" alt="Select Destination Workspace From Dropdown" width="364" height="97" data-path="assets/platform/workspaces/environments-workspace-copy.png" />
</Frame>

2. Select the workspace you wish to migrate your template to.

<Frame caption="Choose the Destination Workspace">
  <img src="https://mintcdn.com/courier-4f1f25dc/ocKTSyLlc6Ky9Ivc/assets/platform/workspaces/environments-workspace-dropdown.png?fit=max&auto=format&n=ocKTSyLlc6Ky9Ivc&q=85&s=9b665a78a6ea6f0de756931baa530bc6" alt="Choose the Destination Workspace" width="318" height="368" data-path="assets/platform/workspaces/environments-workspace-dropdown.png" />
</Frame>

3. The template will be migrated to the selected workspace and environment.

### Event Mapping and Template Migration

If you have an event mapped to a template that you are migrating between environments, the event and its mapping will automatically migrate as well.

If the associated event is already mapped to a different template in the destination environment, then you will receive an error:

<Frame caption="Event Mapping Error">
  <img src="https://mintcdn.com/courier-4f1f25dc/ocKTSyLlc6Ky9Ivc/assets/platform/workspaces/environments-migration-error.png?fit=max&auto=format&n=ocKTSyLlc6Ky9Ivc&q=85&s=d1fac92ad4e92abde6c83d4828290c56" alt="Event Mapping Error" width="1120" height="480" data-path="assets/platform/workspaces/environments-migration-error.png" />
</Frame>

## Integrations and Environments

Integrations are shared across environments; you only need to add an integration once and it works in both Production and Test.

### Adding a Test Environment Configuration

By default, all integrations work in both environments. If you want to isolate test traffic, you can add a test-specific API key for any integration. Courier will use that configuration for any notification sent with a test API key.

<Frame caption="Courier Integrations Allow Users to Set An Integration for Both Environments">
  <img src="https://mintcdn.com/courier-4f1f25dc/ocKTSyLlc6Ky9Ivc/assets/platform/workspaces/environments-test-integration.jpeg?fit=max&auto=format&n=ocKTSyLlc6Ky9Ivc&q=85&s=0bf2c0ca1cc9ae4461454f7612765dd1" alt="Courier Integrations Allow Users to Set An Integration for Both Environments" width="1464" height="886" data-path="assets/platform/workspaces/environments-test-integration.jpeg" />
</Frame>

## Data Logs, Metrics, and Environments

[Data Logs](/platform/analytics/message-logs) and Metrics are environment-specific. Sends made with a test API key only appear in the Test environment dashboard, and sends made with a production key only appear in the Production dashboard. This applies regardless of whether your keys use the `token_` or `pk_`/`dk_` prefix format.

## Segment and Environments

To use Courier environments with Segment, create multiple Courier destinations in Segment with different environment API keys:

1. Send production data from Segment using your production API key.
2. Set up a second destination using your test API key for development and QA.

See the [Segment integration guide](/platform/automations/segment) for setup details.

## Content Promotion Best Practices

Courier's environment model is designed to give you confidence when moving notification changes to production. Here's a recommended workflow:

1. **Build and test in Test.** Create or edit templates, brands, and subscription topics using your test API key. Test sends only appear in the Test dashboard and never reach real users (unless you use real contact info).

2. **Validate with draft keys.** If your workspace has draft keys, use them to preview unpublished template changes against real send payloads before publishing. This lets you catch rendering issues before they affect live notifications.

3. **Migrate to Production.** Use the "Migrate Assets" flow to copy templates and their dependencies (brands, tags, subscription topics) from Test to Production. Courier copies all dependencies automatically so nothing breaks.

4. **Verify after promotion.** Check [Message Logs](/platform/analytics/message-logs) in the Production environment to confirm sends are rendering and delivering as expected.

<Tip>
  Use separate provider configurations for Test and Production (e.g., a sandbox SendGrid key for Test) to prevent test sends from reaching real inboxes. Configure this under each integration's Test Configuration.
</Tip>

## Environments and Billing

Billing takes both test and production sends into account.
