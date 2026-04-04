# Source: https://docs.ox.security/ox-policies/cloud-context-policies-3.md

# Secret and PII Scan Policies

Secret and PII Scan policies detect exposure of sensitive information within source code, version history, and application logs. These policies focus on identifying hardcoded secrets, personally identifiable information, and unsafe logging practices. Effective detection reduces the risk of data breaches, privacy violations, and regulatory non-compliance.

The article describes the policies in this category, configuration options, and the impact of policy violations. For an overview of policies and policy management, see the [Policies](https://docs.ox.security/ox-policies)article.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-4bcb453d75b80b4eda84fb999a378ee09f949fed%2FSecret%20PII%20scan%20summary.png?alt=media" alt=""><figcaption></figcaption></figure>

## View and manage Secret and PII Scan policies

Open each policy to view the business impact and optional settings.

<details>

<summary><mark style="color:purple;">PII in code</mark></summary>

**Purpose:** Detects personally identifiable information (PII) embedded directly in application source code.

**Business impact:** Hardcoded PII exposes sensitive user data and increases the risk of privacy violations. This can result in non-compliance with data protection regulations and associated legal penalties. Disclosure of PII also harms user trust and organizational reputation.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-2f1aea1f91750fe0273b3490d3157f4609ff568e%2FSecret%20PII%20scan%20PII%20in%20code.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th valign="top">Setting</th><th valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">All (including Info)</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">PII in Git history</mark></summary>

**Purpose:** Detects personally identifiable information (PII) present in Git commit history.

**Business impact:** PII in version history exposes sensitive user data even after code changes remove it. This increases the risk of privacy violations and regulatory non-compliance. Persistent exposure in history can also damage user trust and organizational reputation.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-09d19a72c2bc875a22db65da1edccfd60fa8c9b8%2FSecret%20PII%20scan%20PII%20in%20Git%20history.png?alt=media" alt=""><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th valign="top">Setting</th><th valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">All (including Info)</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">PII logging in code</mark></summary>

**Purpose:** Detects application code that logs personally identifiable information (PII) during execution.

**Business impact:** Logged PII can be exposed to users or systems with access to log data. This increases the risk of privacy violations and unauthorized data access. Improper logging can also lead to regulatory non-compliance and reputational damage.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-519e82bf00c0dda8123c147d53403965b89ebb2f%2FSecret%20PII%20scan%20PII%20logging%20in%20code.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="239.3333740234375" valign="top">Setting</th><th width="297.3333740234375" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">All (including Info)</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Secret in code</mark></summary>

**Purpose:** Detects secrets such as credentials, tokens, or keys embedded directly in application source code.

**Business impact:** Hardcoded secrets can be exposed through source code access or repository leaks. Compromised credentials may allow unauthorized access to systems, services, or data. This increases the likelihood of security breaches and operational impact.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-5db6b6ed78439b5993d563f5c1f0787eefe75170%2FSecret%20PII%20scan%20Secret%20in%20code.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="263.9998779296875" valign="top">Setting</th><th width="282.666748046875" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">All (including Info)</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">ON</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Secret in Git history</mark></summary>

**Purpose:** Detects secrets present in Git commit history, including values removed from the current codebase.

**Business impact:** Secrets in version history remain accessible and can be exploited even after remediation. Active credentials may allow unauthorized access to internal systems or services. This increases the risk of long-term compromise and data breaches.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-0c8ce3abec106ffc8cc271823e1d98013124f54e%2FSecret%20PII%20Secret%20in%20Git%20history.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="263.9998779296875" valign="top">Setting</th><th width="282.666748046875" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">All (including Info)</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">ON</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Secret logging in code</mark></summary>

**Purpose:** Detects application code that writes secrets such as credentials, tokens, or keys to logs.

**Business impact:** Logged secrets can be accessed by users or systems with log visibility. Exposed credentials may enable unauthorized access to applications, infrastructure, or data. This increases the risk of security breaches and compliance violations.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-b66637623030e03298b0e680ab0163febafdc1b2%2FSecret%20PII%20scan%20Secret%20logging%20in%20code.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="260.6666259765625" valign="top">Setting</th><th width="297.3333740234375" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">All (including Info)</td></tr></tbody></table>

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
