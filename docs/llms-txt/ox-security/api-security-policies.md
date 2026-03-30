# Source: https://docs.ox.security/ox-policies/api-security-policies.md

# API Security Policies

API Security policies identify security weaknesses in APIs that may expose applications to unauthorized access or data leakage. The policies focus on configuration and design issues in API definitions and implementations, helping teams detect risks early as APIs become a critical interface for applications and services.

The article describes the policies in this category, configuration options, and the impact of policy violations. For an overview of policies and policy management, see the [Policies](https://docs.ox.security/ox-policies)article.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-0961387081f7f26d52528ed5a11ea4be9741e69c%2FApi%20security%20summary%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

## View and manage API Security policies

Open each policy to view the business impact and optional settings.

<details>

<summary><mark style="color:purple;">API security issue</mark></summary>

**Purpose:** Detects misconfigurations and security weaknesses in APIs in source code (not in runtime/cloud-deployed environments). Examples are insecure endpoints or insufficient access controls.

**Business impact:** Security lapses in APIs can allow attackers to access data, bypass authorization, or disrupt services. As organizations rely more heavily on APIs for integration and functionality, unresolved API security issues can lead to widespread data exposure and system compromise.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-9d085c1a58e0dc9643a52f161dedda2eeeb55fa7%2FAPI%20security%20API%20security%20issue.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="228.333251953125" valign="top">Setting</th><th width="282.6666259765625" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">All (including Info)</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">OpenAPI security issue</mark></summary>

**Purpose:** Validates OpenAPI specifications to identify misconfigurations, insecure definitions, and gaps in authentication or access control.

**Business impact:** Misconfigured OpenAPI definitions can expose sensitive endpoints or weaken security controls, increasing the risk of unauthorized access and data breaches. As OpenAPI specifications often drive API implementation and client behavior, security gaps at this level can propagate across services and amplify overall system risk.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-b13e0adc1e0dc907c84ecddcf5ad2388cfc1dfbf%2FAPI%20Security%20OpenAPI%20security%20issue.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="231.666748046875" valign="top">Setting</th><th width="294.666748046875" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">All (including Info)</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

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
