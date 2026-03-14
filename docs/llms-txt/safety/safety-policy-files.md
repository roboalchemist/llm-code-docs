# Source: https://docs.safetycli.com/safety-docs/administration/safety-policy-files.md

# Safety Policy Files

{% hint style="warning" %}
With the introduction of Safety Platform, our web-based Safety experience, local policy files will no longer be applied (even if specified in the CLI arguments). Instead, the Project policy that is defined in Platform will be used. Learn more about [Project Policies.](https://docs.safetycli.com/safety-docs/administration/project-policies)
{% endhint %}

Safety CLI scan settings are configured using Safety policy files. These `.safety-policy.yml` files can be defined for each of your project's or codebases.

{% hint style="info" %}
**Note**: the older **`safety check`** command uses an older policy file format. See [Safety 2's policy file format](https://docs.safetycli.com/safety-2/safety-cli-2-scanner/policy-file) to configure the policies for the `safety check` command.&#x20;
{% endhint %}

### Why use a policy file?

Using a policy file is recommended as a way to standardize your security policy for each project, and allows your development team to centrally share and configure rules, settings, and exceptions for your Safety scans. Some examples are:

* Setting vulnerability severity threshold to only report vulnerabilities above a certain severity threshold
* Ignoring specific vulnerabilities your team knows do not impact your project
* suppressing exit codes in scenarios in which you don't want to stop a build or test

These policy files should be checked into your source control at the root of your Python project alongside other policy files such as `.gitignore`, `requirements.txt`, `setup.py`, etc.

### Generating a Safety CLI policy file

To generate a new policy file, run the following command:

```
safety generate policy_file
```

The resulting policy file will be placed in the current directory with the name **`.safety-policy.yml`**. Please note that the file is hidden when viewing in Windows or Finder, but is visible when connected to a folder using an IDE.

### Safety Policy File Structure

Below is an example of a Safety policy file:

```yaml
version: '3.0'

scanning-settings:
  max-depth: 6
  exclude:
    - "node_modules"
    - "lib/other/**"
    - "**/*.js"
  include-files:
    - path: inside_target_dir/requirements-docs.txt
      file-type: requirements.txt
    - path: inside_target_dir/requirements-dev.txt
      file-type: requirements.txt

report:
  dependency-vulnerabilities:
    enabled: true
    auto-ignore-in-report:
      python:
        environment-results: true
        unpinned-requirements: true
      cvss-severity: []
      vulnerabilities:
        59901:
          reason: We are not impacted by this vulnerability
          expires: '2024-03-15'
        62044:
          reason: No upstream python images provide updated pip yet
          expires: '2024-06-01'

fail-scan-with-exit-code:
  dependency-vulnerabilities:
    enabled: true
    fail-on-any-of:
      cvss-severity:
        - critical
        - high
        - medium

security-updates:
  dependency-vulnerabilities:
    auto-security-updates-limit:
      - patch
```

We will now look at each section of the policy file, the items it controls, and available options.

#### Scanning Settings

The **`scanning-settings`** section of the policy file define where Safety CLI should scan in the target directory. These settings configure the **`safety scan`** command.

* **`max-depth`**: an integer that sets the maximum folder depth Safety CLI should scan to in the target directory.
* **`exclude`**: A list of paths and files that Safety CLI should exclude from the scan. This supports Python's [pathlib glob pattern matching](https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob), which are the same as for [fnmatch](https://docs.python.org/3/library/fnmatch.html#module-fnmatch), with the addition of `**` which indicates "this directory and all subdirectories, recursively". This supports Unix shell-style wildcards only, and not general regex patterns.
* **`include-files`**: The `Safety Scan` command does not allow single files to be targeted. If, however, files that you wish to be scanned are not included in the scan (e.g. because of non-standard naming conventions used), it is possible to use the `include-files` option of the policy file to include those files in your scan. See the code block above for an example of how to include such files.

#### Report

The **`report`** section of the policy file defines rules for which types and specific vulnerabilities Safety CLI should report on. This includes:&#x20;

* **`dependency-vulnerabilities`**: true/false value, set to false if you want to completely disable dependency vulnerability reporting.&#x20;
* **`auto-ignore-in-report`**: Everything defined under this key will be automatically ignored by Safety CLI and not included in reports or outputs.&#x20;
  * **`python:environment-results`**: true/false - sets whether Safety should report on the dependencies found in the current Python environment.&#x20;
  * **`python:unpinned-requirements`**: true/false - sets whether results should be returned for unpinned packages in requirements files, i.e. packages without a specified version.
  * **`cvss-severity`**: A list of CVSS severity values to ignore, options include: critical, high, medium,  low, and unknown. Any vulnerabilities found that match any of these severity values will be ignored and not included in Safety's scan report.
  * **`vulnerabilities`**: A list of specific vulnerabilities Safety should ignore, using Safety's vulnerability IDs, and including **`reason`** string and **`expires`** datetime properties for logging and audit purposes.

#### Fail Scan with Exit Code

**`fail-scan-with-exit-code`** section of the policy file defines rules for when Safety CLI should return non-zero (failing) exit codes, for running Safety CLI within build and integration pipelines such as GitHub Actions, Azure Pipelines, GitLab Pipelines, Jenkins, and CircleCI pipelines.

This gives you the flexibility to set different rules for what to report, and when to fail builds or pipelines.

* **`dependency-vulnerabilities`**: enabled/disabled
  * **`enabled`**:  true/false
  * **`fail-on-any-of`**: rules defining when Safety CLI should fail critical, high, meduim, low and unknown.&#x20;
    * **`cvss-severity`**: A list of CVSS severity values, options include: critical, high, medium,  low, and unknown. Any vulnerabilities Safety CLI reports on that match these CVSS severity labels will result in a failing exit code.
    * **`exploitability`**: A list of exploitability labels which should result in a failing exit code. This is a stub for the upcoming vulnerability EPSS score filtering feature.

{% hint style="info" %}
Note that some vulnerabilities do not have a CVSS severity score. To fail a scan when these vulnerabilities are detected, make sure to include a `cvss-severity` match for "unknown".
{% endhint %}

#### Security Updates

* **`auto-security-updates-limit`**: - patch/minor/major to determine the upper threshold for automatic application of fixes when Safety CLI is updating packages in a requirements.txt file. Note that if "major" is used, Safety will automatically apply fixes for all vulnerabilities, even if the next secure version is a major upgrade with breaking changes. \
  Additional information is available in the [Applying Fixes documentation](https://docs.safetycli.com/safety-docs/vulnerability-remediation/applying-fixes).

### Using a Safety CLI policy file&#x20;

Safety CLI will automatically use the `.safety-policy.yml` file in the root of the target directory being scanned by either `safety check` or `safety scan`.

If you want to reference a policy file that is not in your project root or scan target directory, set the policy file's path in the scan command using the `--policy-file` when running a scan.&#x20;

```
safety scan --policy-file path-to-custom-location-and-name.yml
```

You can confirm a local policy file is being found and used by Safety CLI in the top report section of the output.

### Validating a Safety CLI policy file&#x20;

Safety CLI's **`validate`** command can validate the correctness of a Safety CLI policy file.&#x20;

For example:

```
safety validate policy_file --path .safety-policy.yml
```

ensures Safety CLI is parsing your policy file correctly.
