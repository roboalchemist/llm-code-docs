# Source: https://docs.statsig.com/release-pipeline/create-and-manage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create and Manage Release Pipelines

> Learn how to create, configure, and manage Release Pipelines for controlled feature rollouts

## Creating a New Pipeline

To create a new Release Pipeline:

1. Log into the [Statsig console](https://console.statsig.com)
2. Navigate to **Settings** > **Feature Management**
3. Under Release Pipelines, click the **Create** button
4. Enter a descriptive name for your pipeline
5. Click **Create** to proceed to the configuration page

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/MVGh1601-syUdAtS/images/release-pipeline/create.png?fit=max&auto=format&n=MVGh1601-syUdAtS&q=85&s=f4a1014fab0e0e9d04b450da432aa7e1" alt="Create release pipeline interface" width="3022" height="1592" data-path="images/release-pipeline/create.png" />
</Frame>

## Configuring Phases

Each pipeline consists of one or more phases, with each phase representing a distinct release target.

### Adding Phases

For each phase in your pipeline:

1. Add one or more release rules
2. Select a required **Environment** for the rule
3. Optionally add custom field conditions for more precise targeting

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/MVGh1601-syUdAtS/images/release-pipeline/phases.png?fit=max&auto=format&n=MVGh1601-syUdAtS&q=85&s=63ee982399f76816009db1878c97a718" alt="Phase configuration" width="3024" height="1522" data-path="images/release-pipeline/phases.png" />
</Frame>

### Setting Phase Transitions

Control how your phases progress with these transition options:

| Transition Type    | Description                                                                      |
| ------------------ | -------------------------------------------------------------------------------- |
| **Require Review** | Requires manual approval from an authorized user before starting the phase       |
| **Time Interval**  | Automatically proceeds to the next phase after a specified duration (in minutes) |

:::note
You can combine both options in a single phase. When both are used, the time interval will only begin counting down after the required approval is given.
:::

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/MVGh1601-syUdAtS/images/release-pipeline/condition.png?fit=max&auto=format&n=MVGh1601-syUdAtS&q=85&s=6184284fcb3799c8b281debe2bb8c30f" alt="Phase transition conditions" width="3022" height="1514" data-path="images/release-pipeline/condition.png" />
</Frame>

## Managing Existing Pipelines

### Updating a Pipeline

To modify an existing pipeline:

1. Click on the pipeline name from the list
2. Make your desired edits to any section
3. Click **Save** to apply your changes

**Important:** Pipelines with active rollouts currently in progress cannot be modified until those rollouts complete or are aborted.

### Viewing Pipeline References

There are two ways to see which feature gates and dynamic configs are currently using a pipeline:

1. Project Settings

   * Navigate to Project Settings
   * Click on the Feature Management menu in the left-rail
   * Navigate to Release Pipelines section
   * Click on the **References** column against each Release Pipeline
   * This will show all feature gates and dynamic configs that are currently attached to a specific pipeline

   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/MVGh1601-syUdAtS/images/release-pipeline/reference.png?fit=max&auto=format&n=MVGh1601-syUdAtS&q=85&s=fc09d8fe502f5c7211f6cdb358e5f01c" alt="Reference" width="2118" height="632" data-path="images/release-pipeline/reference.png" />
   </Frame>

2. Feature Gates / Dynamic Configs Page

   * Navigate to Feature Gates / Dynamic Config list view
   * Filter by 'Release Pipeline' current status
   * This will show all feature gates and dynamic configs with an ongoing release pipeline

   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/coJ2eMxW1gm97LH6/images/release-pipeline/create-and-manage/23a3199f-4710-40ed-9bd3-14d2ae5edb49.png?fit=max&auto=format&n=coJ2eMxW1gm97LH6&q=85&s=33b98e134c097bce1ab14af8ff09659f" alt="Feature gates and dynamic configs with release pipeline status" width="2734" height="720" data-path="images/release-pipeline/create-and-manage/23a3199f-4710-40ed-9bd3-14d2ae5edb49.png" />
   </Frame>

## Opting Out Environments from Release Pipelines

By default, all environments will trigger Release Pipelines when changes are made. However, you can configure specific environments to be exempt from this behavior.

When an environment is opted out from Release Pipelines:

* Changes made exclusively to that environment will not trigger a Release Pipeline
* This allows for quick environment-specific adjustments without initiating the full release process

### How to Opt Out an Environment

To exclude an environment from triggering Release Pipelines:

1. Navigate to **Settings** in the Statsig console
2. Under **Keys & Environments**, select **Environments**
3. Click on the environment you wish to opt out
4. Unselect the **Pipeline-required Environment** option
5. Click **Save** to apply your changes

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/MVGh1601-syUdAtS/images/release-pipeline/environment-opt-out.png?fit=max&auto=format&n=MVGh1601-syUdAtS&q=85&s=fe6a2f1332a1f3850496a761e0752164" alt="Environment opt-out setting" width="3014" height="1578" data-path="images/release-pipeline/environment-opt-out.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).