# Source: https://docs.statsig.com/guides/using-environments.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Environment-based Evaluation

Statsig SDKs allow you to set the environment tier for your app during initialization. This helps you evaluate feature gates, dynamic configs, and experiments differently in non-production environments like development or staging. All you need to do is configure the appropriate environment in your code and adjust feature rules in the Statsig Console.

Here's a step-by-step guide on how to configure and use environments effectively.

***

## SDK Usage

There are two key ways to set up environments within your app:

1. **Environment-specific SDK keys**: These determine which rule sets are downloaded by the SDK based on the environment.
2. **Environment tier at SDK initialization**: This defines how rules are evaluated for the app.

### 1. Environment-specific SDK Keys

Setting up environment-specific SDK keys allows you to control which rules are sent to the SDK. For instance, if an SDK is initialized with a key for the development environment, it will not receive rules set for staging or production environments. For more information, see [Per-Environment API Keys](#per-environment-api-keys) below.

### 2. Environment Tier Parameter

SDK keys can correspond to multiple environments. Therefore, it's important to explicitly set the environment tier during SDK initialization to ensure the correct rules are applied.

All SDKs accept an `SDK Key` and an optional `StatsigOptions` dictionary. The `StatsigOptions` parameter includes the `environment` key, which has a `tier` field. This tier corresponds to one of your pre-configured environments (e.g., development, staging).

<Note>
  If the environment tier is unset, all checks and event logs will default to "production."
</Note>

Here's an example of setting the environment tier in your code for the **development** environment:

#### Example (JS Client SDK):

```javascript  theme={null}
const client = new StatsigClient(<SDK_KEY>, user, { environment: { tier: 'development' } });
```

#### Example (Node Server SDK):

```javascript  theme={null}
await statsig.initialize(<SDK_KEY>, { environment: { tier: 'development' } });
```

Refer to your language-specific SDK documentation for further details.

***

## Using Environments in Feature Gates

To configure environment-specific rules for a **Feature Gate**, follow these steps:

1. **Create a new Feature Gate**: In the Statsig Console, create a new Feature Gate. For example, name it "development mode" to target only your development environment.

   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/FgOG_BgUe6iyJQUI/images/tutorials/environments/environments-feature-gate.png?fit=max&auto=format&n=FgOG_BgUe6iyJQUI&q=85&s=2bbac8723688fe714969e5fe1e4f96e5" alt="Feature Gate" width="972" height="1364" data-path="images/tutorials/environments/environments-feature-gate.png" />
   </Frame>

2. **Specify Environments**: When configuring the rule, check the **Specify Environments** box and select the environments you want to target. By default, rules are enabled for all environments unless specified otherwise.

   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/FgOG_BgUe6iyJQUI/images/tutorials/environments/environments-specify.png?fit=max&auto=format&n=FgOG_BgUe6iyJQUI&q=85&s=4addaca17c1626c598c1b02510c260cb" alt="Specify Environment" width="980" height="1492" data-path="images/tutorials/environments/environments-specify.png" />
   </Frame>

3. **Save your settings**: After saving, the environment(s) for which the rule is enabled will be displayed below the rule name.

   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/FgOG_BgUe6iyJQUI/images/tutorials/environments/environments-enabled.png?fit=max&auto=format&n=FgOG_BgUe6iyJQUI&q=85&s=c4cbf371788edcd4a368a978e8b22a8b" alt="Enabled Environments" width="2994" height="1210" data-path="images/tutorials/environments/environments-enabled.png" />
   </Frame>

You can also filter rules by environment using the filter in the upper-right corner of the Feature Gate UI.

To edit the target environments of a rule, click the "..." next to the rule name and select **Edit Rule**.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/FgOG_BgUe6iyJQUI/images/tutorials/environments/environments-edit-rule.png?fit=max&auto=format&n=FgOG_BgUe6iyJQUI&q=85&s=68556189db06281ec033fff8b19c5e62" alt="Edit Rule" width="2996" height="1210" data-path="images/tutorials/environments/environments-edit-rule.png" />
</Frame>

***

## Configuring Environments

By default, Statsig provides three environments: **Development**, **Staging**, and **Production**. You can add more environments or rename the default ones, but the **Production** environment cannot be deleted or modified.

### Steps to Add or Edit Environments:

1. Navigate to **Project Settings** → [**Environments & Keys**](https://console.statsig.com/api_keys).

   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/FgOG_BgUe6iyJQUI/images/tutorials/environments/environments-project-settings.png?fit=max&auto=format&n=FgOG_BgUe6iyJQUI&q=85&s=57b243308110e46b172315985738d3ed" alt="Project Settings" width="3098" height="2074" data-path="images/tutorials/environments/environments-project-settings.png" />
   </Frame>

2. Click **Edit** to add new environments or reorder the existing ones using drag-and-drop.

   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/FgOG_BgUe6iyJQUI/images/tutorials/environments/environments-edit-environments.png?fit=max&auto=format&n=FgOG_BgUe6iyJQUI&q=85&s=d99283ea81ec6de14aec5884c75f930e" alt="Edit Environments" width="978" height="1008" data-path="images/tutorials/environments/environments-edit-environments.png" />
   </Frame>

<Note>
  Reordering environments doesn't affect any rule logic, but it helps convey the rollout hierarchy (e.g., development → staging → production) to your teams.
</Note>

***

## Per-Environment API Keys

To enhance security and privacy, Statsig allows you to create per-environment API keys. This ensures that SDKs initialized with specific environment keys will only access the rules relevant to that environment.

### Steps to Generate Environment-Specific API Keys:

1. Go to **Project Settings** → [**Environments & Keys**](https://console.statsig.com/api_keys).

2. Click **Generate New Key**, and specify the environment for which you want to generate the API key.

   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/FgOG_BgUe6iyJQUI/images/tutorials/environments/environments-generate-key.png?fit=max&auto=format&n=FgOG_BgUe6iyJQUI&q=85&s=0392e055721ae79c595750fe85d09af8" alt="Generate API Key" width="3068" height="2078" data-path="images/tutorials/environments/environments-generate-key.png" />
   </Frame>

<Note>
  The default environments—Development, Staging, and Production—share the same server and client-side API keys. You can generate new keys for custom environments as needed.
</Note>

***


Built with [Mintlify](https://mintlify.com).