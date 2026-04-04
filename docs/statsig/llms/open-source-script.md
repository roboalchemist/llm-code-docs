# Source: https://docs.statsig.com/guides/open-source-script.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Open Source Script

[This package](https://github.com/statsig-io/migrations) is designed to help automate migration of feature flags from LaunchDarkly to Statsig. It fetches feature flags from LaunchDarkly, translates them into Statsig's format, and creates corresponding feature gates in Statsig.

## Considerations

This script should work out of the box. It's recommended you start with a test environment of 5-10 flags. However, before running the script on a large scale, consider the following:

* **IMPORTANT**: If you don't need to customize this import script, you can just use [Statsig's in-console tool](/guides/ui-based-tool)

* The script uses a tag `Imported from LaunchDarkly` to identify migrated flags in Statsig. Ensure this tag is unique and recognizable.

* The script includes a function to delete all Statsig feature gates with a specific tag. Use this with caution to clean up after a test or failed migration.

* The script requires API keys for both LaunchDarkly and Statsig, which should be kept secure.

## Installation

To run the script, you need Node.js and npm installed on your system. You can execute directly:

```bash  theme={null}
npx @statsig/migrations --from launchdarkly --launchdarkly-project-id default <more-arguments>
```

## Configuration

* Provide your [LaunchDarkly API key](https://docs.launchdarkly.com/home/account/api) and [Statsig Console API key](/console-api/introduction) in the script
* Map LaunchDarkly environments to Statsig environments that aren't already the same by using `--environment-name-mapping` to the script.
* Map LaunchDarkly context kind to Statsig's custom unit ids and custom fields.

You can find the detailed instructions for these steps on the [Github repo](https://github.com/statsig-io/migrations).

## Running the Script

To execute the migration script, run the following command in your terminal:

```bash  theme={null}
node index.js
```

The script will perform the following actions:

1. Fetch all feature flags from LaunchDarkly.
2. Translate each flag into Statsig's format.
3. Create feature gates in Statsig.
4. Write the migration status and details to a CSV file named `flag_migration_tracker.csv`

## Example Translations

The following examples show how LaunchDarkly feature flags are translated into Statsig feature gates:

**Example 1:** LaunchDarkly flag with email and name targeting conditions

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/FgOG_BgUe6iyJQUI/images/tutorials/migration-launchdarkly/open-source/example-translation-1.png?fit=max&auto=format&n=FgOG_BgUe6iyJQUI&q=85&s=77ea397c709534ec7b253e0ebf264e0b" alt="Example 1 - LaunchDarkly to Statsig translation" width="2048" height="1160" data-path="images/tutorials/migration-launchdarkly/open-source/example-translation-1.png" />
</Frame>

**Example 2:** LaunchDarkly flag with country-based targeting (off flag)

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/FgOG_BgUe6iyJQUI/images/tutorials/migration-launchdarkly/open-source/example-translation-2.png?fit=max&auto=format&n=FgOG_BgUe6iyJQUI&q=85&s=ca87890d5184f0348484ae9c48680514" alt="Example 2 - LaunchDarkly to Statsig translation" width="2048" height="1162" data-path="images/tutorials/migration-launchdarkly/open-source/example-translation-2.png" />
</Frame>

## Troubleshooting

If you encounter issues during the migration, check the following:

* Ensure that the API keys are correct and have the necessary permissions.
* Review the error messages in the console for clues on what might have gone wrong.

Pull requests and feedback welcome!


Built with [Mintlify](https://mintlify.com).