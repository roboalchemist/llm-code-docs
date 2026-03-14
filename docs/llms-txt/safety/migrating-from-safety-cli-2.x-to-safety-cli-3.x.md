# Source: https://docs.safetycli.com/safety-docs/safety-cli/introduction-to-safety-cli-vulnerability-scanning/migrating-from-safety-cli-2.x-to-safety-cli-3.x.md

# Migrating from Safety CLI 2.x to Safety CLI 3.x

Safety CLI 3 is a significant update from Safety CLI 2.x versions, including enhancements to core features, new capabilities, and [breaking changes](https://docs.safetycli.com/safety-docs/miscellaneous/release-notes/breaking-changes-in-safety-3).&#x20;

Here's a step-by-step guide covering everything you need to know when upgrading.

## Installing Safety 3.x

1. Start by opening your Terminal and uninstall the current version of Safety CLI installed in your environment:&#x20;

```
pip uninstall safety
```

2. Install the latest version of Safety using the following command:&#x20;

```
pip install safety
```

Safety CLI 3.x should now be installed on your machine. To check which version is currently installed:

```
safety --version
```

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2F48dCdeGq4nev7MsoWukZ%2FCLI%20Version.png?alt=media&#x26;token=c9414bd9-69bc-4f29-be5e-de6db00e0a82" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="success" %}
If this returns a version other than 3.x, there could be more than one installation of Safety on your machine. To check where Safety is being run from, run the **`which safety`** command.&#x20;
{% endhint %}

## Switching to the new \`scan\` command:

The most significant change is Safety CLI 3's `scan` command, which replaces the old `safety check` command as the main security scanning command. `safety scan` is more powerful, configurable, and easier to use compared to `safety check`, and differs in the following key ways:

* it searches the target directory being scanned recursively, finding and reporting all Python dependency manifest files and virtual environments automatically, without any need for specifying where these files are
* it natively supports requirements.txt, poetry.lock, and Pipfile.lock files as well as Python virtual environment directories
* it is configured with a differently structured .safety-policy.yml file, which is incompatible with the .safety-policy.yml file used with the older \`safety check\` command, and visa versa. This new configuration file is more flexible and powerful
* it can be configured for how it searches the project directory, which vulnerabilities it reports on, and separately defines rules for which vulnerabilities will return a failing (non-zero) exit code, for use within CI/CD pipelines and build scripts

We highly recommend switching to `safety scan` as soon as possible.&#x20;

## Configuration files: Convert to the new policy file format

{% hint style="info" %}
If you are not currently using a `.safety-policy.yml` file with safety check, you can skip this section!
{% endhint %}

Safety CLI 3's `scan` and `system-scan` commands are configured using a new and updated configuration file. See [Safety 3's policy file documentation page](https://docs.safetycli.com/safety-docs/administration/safety-policy-files) for full details on the new structure and features of this policy file.

If you have been using a `.safety-policy.yml` file with `safety check`, you'll need to convert this to safety scan's new policy file format to use it to maintain the same policies with `safety scan`. To do this:&#x20;

* Navigate to the root of your existing project
* Move your existing policy file to a different location within your project, so that you can reference it later. (If you want to continue using safety check while also the new safety scan command, see instructions below \[link])
* Using Safety CLI 3 (run `safety --version` to confirm your Safety CLI version), run `safety generate policy_file` to generate a new policy file with the updated format.&#x20;
* Open both policy files, and translate the relevant parts from your old policy file into the new one. The key configurations that move are:
  * Any specific vulnerabilities you have ignored in `security:ignore-vulnerabilities` move to `report:auto-ignore-in-report:vulnerabilities` which contains the same list of ignores.
  * `security:ignore-cvss-severity-below` and `security:ignore-cvss-unknown-severity` move to a combined `report:auto-ignore-in-report:cvss-severity` which is now a YAML list with options: `critical`, `high`, `medium`, `low`, and `unknown`.
  * The boolean `security:continue-on-vulnerability-error:True` property is now removed. To suppress exit codes in the new policy file, use the `fail-scan-with-exit-code:dependency-vulnerabilities:enabled:False` property.&#x20;
  * The alert section of the old policy file is no longer supported and must be removed. This functionality is being replaced by Safety Platform.&#x20;
* With these changes your policies are now translated to the new policy format, ready to be used with `safety scan`
* When using the `validate` command, Safety CLI 3 will validate a 3.0 policy file by default.

## Updating your scan target(s)

If you were using Safety check with the -r flag to specify requirements.txt files to scan, you no longer need these with `safety scan` - they should be found automatically.

If `safety scan` is finding dependency files or virtual environments you do not want to include in your reports, use the new `scanning-settings:exclude` property in your `.safety-policy.yml` file to exclude specific files, file types or folders from the scan. [See more details on excluding here.](https://docs.safetycli.com/safety-docs/administration/safety-policy-files)

## New JSON output format

Safety scan has a new [JSON output](https://docs.safetycli.com/safety-docs/output/json-output) format that differs substantially from the JSON output of safety check.

## Upgrading from safety 2.x to safety 3.x while using safety check's JSON output

Safety CLI 3 still supports the safety check command, which is almost identical to safety check from Safety 2.x. If you are upgrading from Safety CLI 2 to Safety CLI 3, you can do so without needing to make any changes. The only breaking changes in this case may be the JSON output structure. Safety 3.0's JSON output from `safety check` uses the same structure as Safety CLI 2.4.0b. If you are upgrading from safety<=2.3.5 to safety>=3.x the JSON output from `safety check` will differ.

## Using both safety check and safety scan in the same project

You can use Safety CLI 3 to run both `safety check` and `safety scan` commands, each with their own policy files. To achieve this, keep your old `safety check` policy file in your project directory under a new name, for example `.safety-check-policy.yml`, and run the check command using `safety check --policy-file .safety-check-policy.yml` to specify the policy file's path. This will allow you to shift to using `safety scan` and the new policy file format at the default `.safety-policy.yml` location.
