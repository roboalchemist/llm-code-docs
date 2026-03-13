# Source: https://docs.safetycli.com/safety-docs/safety-cli/scanning-for-vulnerable-and-malicious-packages.md

# Scanning for Vulnerable and Malicious Packages

## Scanning a Python project

Once Safety CLI is installed and you have authenticated, let's **scan a Python project.**&#x20;

In your terminal, navigate to the root folder of a Python project, e.g. **`cd /my/project/`**. (This root folder would normally contain files such as **`composer.lock`**, **`requirements.txt`**, **`READMEs`**, **`Pipfile.lock`**,  **`pyproject.toml`**, **`.gitignores`** etc.)

Once you have navigated your terminal to your Python project's root directory, run:

```
safety scan
```

{% hint style="info" %}
If this is the first time Safety has scanned this project, you may be prompted to set the project's name for tracking within Safety Platform.
{% endhint %}

Running `safety scan` will:

* Scan your Python project's entire directory for Python package files and Python virtual environments, indexing all the packages found.
* Conduct a security analysis of these packages against known security vulnerabilities and malicious package lists.
* Identify known vulnerabilities in these packages, including their location and version
* Provide fix recommendations.

{% hint style="info" %}
Safety CLI is a powerful and flexible command-line tool. It can be used in a variety of use cases, environments and stages of the development lifecycle. It can output scan reports into different formats like JSON, and it can be integrated into any CI/CD pipeline or testing system. To learn more, refer to [Safety CLI Documentation](https://docs.safetycli.com/safety-docs/safety-cli/introduction-to-safety-cli-vulnerability-scanning).
{% endhint %}

Once complete, your terminal will show a summary of the vulnerable packages that were found and recommended actions.

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2FzwND8F6sZdeeLdTxsVjG%2Fimage.png?alt=media&#x26;token=c735a841-153c-4b88-a638-872e0228440f" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
If the `safety scan` command is not found, **or your safety version is less than 3.0,** you need to [install Safety version 3](https://docs.safetycli.com/safety-docs/safety-cli/installation-and-authentication) before continuing below.
{% endhint %}

{% hint style="info" %}
**Targeting/Including Specific Requirements Files**

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
