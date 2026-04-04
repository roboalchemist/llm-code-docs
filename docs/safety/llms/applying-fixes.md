# Source: https://docs.safetycli.com/safety-docs/vulnerability-remediation/applying-fixes.md

# Applying Fixes

When performing a **`safety scan`**,  Safety provides a list of the vulnerabilities detected and, where available, recommended fixes for each.

Safety CLI can automatically update requirements files based on these recommendations by using the **`safety scan --apply-fixes`**  command.

{% hint style="info" %}
**Summary**

* Where possible, updates to requirements files are applied automatically using the closest package version in which the detected vulnerability has been resolved.&#x20;
* Upgrades are performed in accordance with the [Policy File](#policy-file), which limits automatic upgrades to patch, minor, or major updates. Any upgrades beyond the policy-defined threshold will result in a prompt (Y/N/Skip) that must be responded to by the user.
* When no fixes are available, a message is displayed to that effect.
* Safety CLI does not download or install packages. Instead, requirements files are updated.
  {% endhint %}

## 1. Applying Security Updates Automatically

Safety can apply recommended security updates by including the **`--apply-fixes`** command.

#### **Example**

**`safety scan --apply-fixes`**

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2FdEvYdTnQOh8guEQ3L9fR%2Fimage.png?alt=media&#x26;token=bf20f4bf-c244-4f9d-8b95-a7ea12e8acd6" alt=""><figcaption></figcaption></figure>

In this example, Safety has automatically updated the package versions in the requirements.txt file.  Our policy file has a threshold limiting automatic upgrades to patches and minor upgrades only. As a result, the user is asked whether or not they wish to upgrade to the new version of the last package.

### Threshold for Applying Fixes Automatically

#### Policy File

The Safety policy file referenced when performing the scan includes the automatic update threshold, beyond which the user will be prompted to confirm whether or not they wish to update packages with known vulnerabilities.

This threshold is necessary to prevent Safety from applying updates that could impact projects, e.g. by upgrading to a new major version with breaking changes.

#### Terminal

To set the maximum version change that Safety will apply without user input, append that limit to the command, e.g. **`safety scan --apply-fixes requirements.txt`` `**<mark style="color:blue;">**`minor`**</mark>. Possible values are: `major, minor, patch`. The default is value `patch`.

{% hint style="info" %}
In both cases, the value used is an upper limit. Using **`major`** is equivalent to automatically applying all the fixes without user input.
{% endhint %}

**Examples:**

```
safety scan --apply-fixes requirements.txt minor
```

This will update the requirements.txt file (and any other requirements files it references) with all the security remediations that are `minor` or `patch` updates. If remediation requires a `major` version update, then Safety will ask for user input if they want to make this change.

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2Fz2xQILFfuWD2TBnwwVjE%2Fimage.png?alt=media&#x26;token=f96687a5-d582-408e-a4fd-16f813058211" alt=""><figcaption><p>Patch and Minor Updates Applied Automatically. Major updates require user input.</p></figcaption></figure>

`safety scan --apply-fixes requirements.txt major`

In this case, as `major` was used, all the remediations will be automatically applied in the file, and any of its recursive include files.

## Skipping Update Prompts

If you want to ensure that Safety will not wait for user input, the `--no-prompt` flag will apply all automatic fix updates that fall within the `--auto-security-updates-limit` limit, and ignore those that require user input.

`safety scan -r requirements.txt --apply-fixes -afl minor --no-prompt`

This will apply all `patch` and `minor` version security updates to `requirements.txt` and ignore any `major` version updates, with no user input prompt.
