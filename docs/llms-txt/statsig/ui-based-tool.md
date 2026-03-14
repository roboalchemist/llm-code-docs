# Source: https://docs.statsig.com/guides/ui-based-tool.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# UI-Based Tool

You can follow this guide to use Statsig's built in LaunchDarkly migration tool. Please note that this UI-based tool only imports the "production" environment at the moment.

## What you need

Review the full checklist in the [LaunchDarkly Migration Guide](/guides/migrate-from-launchdarkly#what-you-need), then gather:

1. You will need your project key. Projects in LaunchDarkly have a Name (e.g. "My Mobile App") and a Key (e.g.my\_mobile\_app).
2. You'll need a read-only access token for this project. You can create one in LaunchDarkly -> Account Settings -> Authorization and limit scope to be read-only.
3. A Statsig project to use. We recommend trying this in a test project first.

## How it works

These screens mirror the [console walkthrough](/guides/migrate-from-launchdarkly#how-it-works):

1. You will be prompted to Import Feature Gates if you don't have any feature gates in your project.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/OOITRwHOw8MJe6vk/images/tutorials/migration-launchdarkly/ui-tool/ui-based-tool1.png?fit=max&auto=format&n=OOITRwHOw8MJe6vk&q=85&s=78290e39557bfb65d440f286703c6f1b" alt="Import Feature Gates prompt" width="2000" height="1344" data-path="images/tutorials/migration-launchdarkly/ui-tool/ui-based-tool1.png" />
</Frame>

2. Select LaunchDarkly as the platform you want to migrate from.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/OOITRwHOw8MJe6vk/images/tutorials/migration-launchdarkly/ui-tool/ui-based-tool2.png?fit=max&auto=format&n=OOITRwHOw8MJe6vk&q=85&s=c52136466c256bf6f582968e7436fc8e" alt="Platform selection interface" width="2000" height="1344" data-path="images/tutorials/migration-launchdarkly/ui-tool/ui-based-tool2.png" />
</Frame>

3. Enter your LaunchDarkly Project Key and API Key/access token.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/OOITRwHOw8MJe6vk/images/tutorials/migration-launchdarkly/ui-tool/ui-based-tool3.png?fit=max&auto=format&n=OOITRwHOw8MJe6vk&q=85&s=5f5b9d7f9684c991a7966f1d101ca91a" alt="LaunchDarkly credentials input form" width="2000" height="1344" data-path="images/tutorials/migration-launchdarkly/ui-tool/ui-based-tool3.png" />
</Frame>

4. Preview the migration summary. We'll highlight what gates we can and can't migrate. Gates we don't migrate include gates with segments (coming soon) and gates with non-Boolean flags.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/OOITRwHOw8MJe6vk/images/tutorials/migration-launchdarkly/ui-tool/ui-based-tool4.png?fit=max&auto=format&n=OOITRwHOw8MJe6vk&q=85&s=62bb7515e0b32b81a767436f60a37bc6" alt="Migration summary preview screen" width="2000" height="1344" data-path="images/tutorials/migration-launchdarkly/ui-tool/ui-based-tool4.png" />
</Frame>

5. Finish migration of the gates. All your migrated gates will be tagged "Migrated" so you can identify them.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/OOITRwHOw8MJe6vk/images/tutorials/migration-launchdarkly/ui-tool/ui-based-tool5.png?fit=max&auto=format&n=OOITRwHOw8MJe6vk&q=85&s=48db4796a3a31e68045f7ddb83520efb" alt="Migration completion confirmation" width="2000" height="1344" data-path="images/tutorials/migration-launchdarkly/ui-tool/ui-based-tool5.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).