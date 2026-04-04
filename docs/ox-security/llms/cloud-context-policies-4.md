# Source: https://docs.ox.security/ox-policies/cloud-context-policies-4.md

# Security Tool Coverage Policies

Security Tool Coverage policies detect missing or incomplete use of required security scanning tools in code repositories and CI/CD pipelines. These policies cover Static Application Security Testing (SAST), Software Composition Analysis (SCA), and secrets detection.

Proper coverage ensures consistent identification of code, dependency, and credential risks before software reaches production.

The article describes the policies in this category, configuration options, and the impact of policy violations. For an overview of policies and policy management, see the [Policies](https://docs.ox.security/ox-policies)article.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-7c9dc1ac6051fde68820a83b9fa3b44b7d8bf06b%2FSecurity%20tool%20summary.png?alt=media" alt=""><figcaption></figcaption></figure>

## View and manage Security Tool Coverage policies

Open each policy to view the business impact and optional settings.

<details>

<summary><mark style="color:purple;">SAST missing in CI/CD pipeline</mark></summary>

**Purpose:** Detect code repositories that do not include an approved Static Application Security Testing (SAST) tool in the CI/CD pipeline.

**Business impact:** Missing SAST coverage allows preventable vulnerabilities to reach production. Common issues such as injection flaws or insecure code patterns may remain undetected. This increases the likelihood of security incidents and raises remediation costs later in the development lifecycle.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-41680a9d42c21dd1594c3e303b2c7d5898eeac12%2FSecurity%20tool%20SAST%20missing%20in%20CICD%20pipeline.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="228.333251953125" valign="top">Setting</th><th width="300.6666259765625" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">SAST (dropdown)</td><td valign="top">Select one or more approved SAST applications</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr><tr><td valign="top">Ignore if OX SAST is enabled</td><td valign="top">Enable/disable.</td><td valign="top">ON</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Open Source Security disabled</mark></summary>

**Purpose:** Detect code repositories where an approved Software Composition Analysis (SCA) tool is configured but not enabled.

**Business impact:** Disabled SCA prevents detection of known vulnerabilities in third-party dependencies. Insecure or outdated components may remain in use without visibility. This increases exposure to widely exploited flaws and supply chain security incidents.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-62a36a0205d9ae5448f87ad02fb6a3bdba626b31%2FSecurity%20tool%20Open%20Source%20Security%20disabled.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="232.666748046875">Setting</th><th width="344.6666259765625">Description</th><th>Default</th></tr></thead><tbody><tr><td>ON/OFF (toggle)</td><td>Enable/disable the policy.</td><td>ON</td></tr><tr><td>SCA (dropdown)</td><td>Select one or more approved SCA applications.</td><td>Current setting</td></tr><tr><td>Ignore Application Business Priority for severity calculation (checkbox)</td><td>When enabled, severity is not adjusted based on application priority.</td><td><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Open Source Security missing in CI/CD pipeline</mark></summary>

**Purpose:** Detect code repositories that do not include an approved Software Composition Analysis (SCA) tool in the CI/CD pipeline.

**Business impact:** Missing SCA coverage allows vulnerable third-party dependencies to enter production without detection. Known flaws in open-source components may remain unpatched and exploitable. This increases the risk of supply chain attacks and large-scale incidents similar to widely exploited dependency vulnerabilities.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-680efed08eb5d7b71e6513b55edb559843d282e4%2FSecurity%20tool%20Open%20Source%20Security%20missing%20in%20CICD%20pipeline.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="239.3333740234375" valign="top">Setting</th><th width="297.3333740234375" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">SCA (dropdown)</td><td valign="top">Select one or more approved SCA applications.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr><tr><td valign="top">Ignore if OX SCA is enabled</td><td valign="top">Enable/disable.</td><td valign="top">ON</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Open Source Security unsupported language</mark></summary>

**Purpose:** Detect code repositories that contain dependencies written in languages not supported by the approved Software Composition Analysis (SCA) tool.

**Business impact:** Unsupported languages create blind spots in dependency vulnerability detection. Vulnerable third-party components may remain undiscovered and exploitable. This increases the risk of supply chain attacks and security incidents similar to widely abused dependency flaws..

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-317294d8a90156e58299f2b23caa70a2edd9ab93%2FSecurity%20tool%20Open%20Source%20Security%20unsupported%20language.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="263.9998779296875" valign="top">Setting</th><th width="282.666748046875" valign="top">Description</th><th valign="top">Defau</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">SAST disabled</mark></summary>

**Purpose:** Detect code repositories where an approved Static Application Security Testing (SAST) tool is configured but not enabled.

**Business impact:** Disabled SAST removes a core security control from the development process. Vulnerabilities such as injection flaws or insecure coding patterns may go undetected. This increases exposure to application compromise and raises the cost of fixing issues after deployment.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-3af418bd97f4645010ef6f793edbb4940b7dea98%2FSecurity%20tool%20SAST%20disabled.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="252.6666259765625" valign="top">Setting</th><th width="296.0001220703125" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">SAST (dropdown)</td><td valign="top">Select one or more approved SAST applications.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">SAST unsupported language</mark></summary>

**Purpose:** Detect code repositories that contain source files written in languages not supported by the approved Static Application Security Testing (SAST) tool.

**Business impact:** Unsupported languages create gaps in application security coverage. Vulnerabilities in unscanned code may reach production without detection. This increases the risk of exploitable weaknesses and inconsistent security enforcement across the codebase.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-074eb1aecf8264b63933ab0f9321ab64108a42fc%2FSecurity%20tool%20SAST%20unsupported%20language.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="260.6666259765625" valign="top">Setting</th><th width="297.3333740234375" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Secrets detection missing in CI/CD pipeline</mark></summary>

> **Note:** This capability is currently in Early Access (EA) and is not generally available. To request access, please contact OX technical support.

**Purpose:** Detect code repositories that do not include an approved secrets scanning tool in the CI/CD pipeline.

**Business impact**: Missing secrets scanning allows hardcoded credentials, tokens, or keys to reach source control and production. Exposed secrets can lead to unauthorized access to systems or cloud resources. This increases the risk of data breaches and infrastructure compromise

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-faa9e3181c5074e37e1c683368abed6ad804edf1%2FSecurity%20tool%20Secrets%20detection%20in%20CICD%20pipeline.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="230.6666259765625" valign="top">Setting</th><th width="297.3333740234375" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Secrets (dropdown)</td><td valign="top">Select one or more approved SAST applications.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr><tr><td valign="top">Ignore if OX Secret Scan is enabled</td><td valign="top">Enable/disable.</td><td valign="top">ON</td></tr></tbody></table>

</details>

## View policy issues

1. Open the Active Issues page.
2. Use the **Category** filter and select the policy category to view related active issues.
3. Use the **Policy** filter to narrow the list to a specific policy.
4. Apply the Category and Policy filters separately or together, depending on how specific you want the results to be.
5. Use the search box to refine results, such as filtering by file name, keyword, or rule identifier.

## Create or save policy profiles

When you change a policy’s severity, ON/OFF toggle or any other setting, you must save the current profile or create a new one.

* To save the current profile, click **SAVE** in the page header.
* To create a new profile, click **SAVE AS** in the page header. For instructions, see the section [Create or edit policy profiles](https://open-2c.gitbook.com/url/preview/site_RHimt/~/revisions/esBak1HVuTgsCEeNbzHE/policies?theme=light#create-or-edit-policy-profiles)in the [Policies](https://docs.ox.security/ox-policies/policies)article.
