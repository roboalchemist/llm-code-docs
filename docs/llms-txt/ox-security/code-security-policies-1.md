# Source: https://docs.ox.security/ox-policies/code-security-policies-1.md

# Dynamic App Security Policies

Dynamic App Security policies identify security vulnerabilities in running web applications by testing them from an external attacker’s perspective.

The policies focus on issues that only appear during execution, such as injection flaws or insecure authentication, which may not be detected through static analysis or dependency scanning. Addressing dynamic application security issues helps reduce the risk of real-world exploitation before applications are exposed to users.

The article describes the policies in this category, configuration options, and the impact of policy violations. For an overview of policies and policy management, see the [Policies](https://docs.ox.security/ox-policies)article.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-9a7735ecd7f43a3c5aa661dc6f084f6855c4529c%2FDynamic%20app%20security%20summary%20(2).png?alt=media" alt=""><figcaption></figcaption></figure>

## **View and manage Dynamic App Security policies** <a href="#view-and-manage-code-security-policies" id="view-and-manage-code-security-policies"></a>

Open each policy to view the business impact and optional settings.

<details>

<summary><mark style="color:purple;">DAST issue</mark></summary>

**Purpose:** Identifies security vulnerabilities in running web applications by simulating external attacks against exposed interfaces using dynamic application security testing (DAST).

**Business impact:** Undetected vulnerabilities in web applications can be exploited by attackers to gain unauthorized access, expose sensitive data, or disrupt services.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-526d1126697d344b2c2659de056f3ae20e899f9a%2Fdynamic%20app%20security%20DAST%20issue%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="235.3333740234375">Setting</th><th width="290">Description</th><th>Default</th></tr></thead><tbody><tr><td>ON/OFF (toggle)</td><td>Enable/disable the policy.</td><td>ON</td></tr><tr><td>Show issues of severity (dropdown)</td><td>Limits which severities appear as issues.</td><td>All (including Info)</td></tr></tbody></table>

</details>

## View policy issues

1. Open the Active Issues page.
2. Use the **Category** filter and select the policy category to view related active issues.
3. Use the **Policy** filter to narrow the list to a specific policy.
4. Apply the Category and Policy filters separately or together, depending on how specific you want the results to be.
5. Use the search box to refine results, such as filtering by file name, keyword, or rule identifier.

You can also view code-related issues on the Application page, where the Issues tab shows findings linked to that application.

## Create or save policy profiles

When you change a policy’s severity, ON/OFF toggle or any other setting, you must save the current profile or create a new one.

* To save the current profile, click **SAVE** in the page header.
* To create a new profile, click **SAVE AS** in the page header. For instructions, see the section [Create or edit policy profiles](https://open-2c.gitbook.com/url/preview/site_RHimt/~/revisions/esBak1HVuTgsCEeNbzHE/policies?theme=light#create-or-edit-policy-profiles)in the [Policies](https://docs.ox.security/ox-policies/policies)article.
