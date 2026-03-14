# Source: https://docs.safetycli.com/safety-docs/miscellaneous/release-notes/breaking-changes-in-safety-3.md

# Breaking Changes in Safety 3

As a major version upgrade, Safety 3.x includes several breaking changes over versions 2.x, which are summarized below. For more information on migrating from Safety CLI 2.x to Safety CLI 3.x, please refer to our [migration guide.](https://docs.safetycli.com/safety-docs/safety-cli/introduction-to-safety-cli-vulnerability-scanning/migrating-from-safety-cli-2.x-to-safety-cli-3.x)

| Breaking Change Category                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Command Update                                       | `safety check` command is replaced by `safety scan`. The new command is more powerful and configurable, providing recursive search in the target directory, native support for various dependency files, and customizable scan settings.                                                                                                                                                                                                                                                                                     |
| Configuration File                                   | The `.safety-policy.yml` file structure has changed. The new format is incompatible with the old one used by `safety check`. Users need to convert their existing policy files to the new format for compatibility with `safety scan`.                                                                                                                                                                                                                                                                                       |
| Policy File Changes                                  | Specific configurations in the old policy file need to be translated to the new format. Notably, `security:ignore-vulnerabilities` moves to `report:auto-ignore-in-report:vulnerabilities`, `security:ignore-cvss-severity-below` and `security:ignore-cvss-unknown-severity` combine into `report:auto-ignore-in-report:cvss-severity`, and `security:continue-on-vulnerability-error:True` is replaced by `fail-scan-with-exit-code:dependency-vulnerabilities:enabled:False`. The `alert` section is no longer supported. |
| Scan Target Settings                                 | The `-r` flag for specifying `requirements.txt` files in `safety check` is no longer needed in `safety scan` as it finds these files automatically. The `scanning-settings:exclude` property in the new policy file can be used to exclude specific files or folders from scans.                                                                                                                                                                                                                                             |
| JSON Output Format                                   | Safety CLI 3 introduces a new JSON output format for `safety scan` that is substantially different from `safety check`’s JSON output. If upgrading from Safety CLI 2.x and using JSON output, users may face breaking changes in the JSON structure if upgrading from versions earlier than 2.4.0b.                                                                                                                                                                                                                          |
| Using Both `Safety Check` and `Safety Scan` Commands | Safety CLI 3 allows running both `safety check` and `safety scan` commands, each with their separate policy files. To continue using both, the old policy file must be renamed (e.g., `.safety-check-policy.yml`) and specified when using `safety check`.                                                                                                                                                                                                                                                                   |
| Validate Command                                     | When using the `validate` command, Safety CLI 3 will validate a 3.0 policy file by default.                                                                                                                                                                                                                                                                                                                                                                                                                                  |

{% hint style="info" %}
**Targeting Specific Requirements Files**

In Safety CLI 2, it was possible to target specific requirements files. The new Safety Scan command is designed to allow you to scan all files in a project directory (or sub-directory) simultaneously rather than running separate scans targeted on each file.

The [Policy File](https://docs.safetycli.com/safety-docs/administration/safety-policy-files) enables you to control the depth of those scans to detect nested requirements files, e.g. six folders deep within the current directory.

If you wish to specify a target directory for the Safety Scan, you can do so using the **`--target`** option, e.g. `safety scan`` `**`--target /path/to/project`**. Safety Scan does not allow you to target single files, but the include-files section of the Policy File does allow you to include specific files in your scan if these are not detected in a normal scan.&#x20;

Example:

**`include-files:`**

**`- path: inside_target_dir/requirements-docs.txt`**&#x20;

**`file-type: requirements.txt`**

**`- path: inside_target_dir/requirements-dev.txt`**

**`file-type: requirements.txt`**

When running a new Safety Scan, the new CLI output will separate findings and recommendations by requirements file, e.g. requirements.txt will have its own set of recommendations, requirements-dev.txt will have its own, etc. This means that instead of running separate scans for each file, you can now run one simple scan and see all findings and recommendations in one output.
{% endhint %}
