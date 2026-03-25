# Source: https://docs.ox.security/ox-policies/code-security-policies.md

# Code Security Policies

Code Security policies identify security vulnerabilities or flaws in your source code early in the CI:CD and before runtime. Addressing these issues can prevent security breaches, data leaks, and system compromises. OX evaluates source code using static analysis and pattern detection (SAST).

The article describes the policies in this category, configuration options, and the impact of policy violations. For an overview of policies and policy management, see the [Policies](https://docs.ox.security/ox-policies)article.

## **View and manage Code Security policies** <a href="#view-and-manage-code-security-policies" id="view-and-manage-code-security-policies"></a>

Open each policy to view the business impact and optional settings.

<details>

<summary><mark style="color:purple;">SAST issue</mark></summary>

**Purpose:** Analyzes application source code using static analysis to identify security vulnerabilities and insecure coding patterns.

**Business impact:** SAST findings indicate security vulnerabilities in your source code that attackers may exploit. Addressing these issues early prevents data exposure, unauthorized access, and costly remediation later in the development cycle.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-dbf7a3f5612a819a6b4d91510a213b947edeafdd%2Fcode%20security%20SAST%20screen.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="235.3333740234375">Setting</th><th width="290">Description</th><th>Default</th></tr></thead><tbody><tr><td>ON/OFF (toggle)</td><td>Enable/disable the policy.</td><td>ON</td></tr><tr><td>Show issues of severity (dropdown)</td><td>Limits which severities appear as issues.</td><td>All (including Info)</td></tr><tr><td>Ignore Application Business Priority for severity calculation (checkbox)</td><td>When enabled, severity is not adjusted based on application priority.</td><td>OFF</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Unapproved SaaS in code</mark></summary>

**Purpose:** Detects references in application code to SaaS services or APIs that are not approved for use by the organization.

**Business impact:** SAST findings indicate security vulnerabilities in your source code that attackers may exploit. Addressing these issues early prevents data exposure, unauthorized access, and costly remediation later in the development cycle.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-676501a01c61e055c9d8089224fb1e0531c591e4%2Fcode%20security%20unapproved%20Saas%20code%20screen.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="218" valign="top">Setting</th><th width="306" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">OFF</td></tr><tr><td valign="top">Show issues of severity<br>(dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">All (including Info)</td></tr><tr><td valign="top">Category (checkboxes)</td><td valign="top"><p>This policy enables organizations to:</p><ul><li>Define which SaaS categories are unapproved</li><li>Establish a list of approved services</li><li>Configure the severity level for violations</li></ul><p>Select SaaS categories to monitor:</p><p><br>Database, Ticketing, Messaging, Logging, Development Tool, Marketing, AI, CRM, Monitoring, Cloud, Email Service, Fintech, IaC, Data Service, Auth, Social Media, Ecommerce, File Hosting, Data Analytics</p></td><td valign="top">OFF</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr></tbody></table>

**Worked example**

The image below shows a policy configuration where the **Database** and **Ticketing SaaS** categories are set as unapproved. Within these categories, **MongoDB Atlas**, **SnowflakeDB**, and **Asana** are marked as approved services.

Use of other database services triggers a **critical** severity issue, while use of other ticketing services triggers a **high** severity issue.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-5979e5eaf252743676b1f64a0eb4c3f121e68db8%2Fcode%20security%20worked%20example.png?alt=media" alt=""><figcaption></figcaption></figure>

</details>

<details>

<summary><mark style="color:purple;">Code Smell issue</mark></summary>

**Purpose:** Identifies poor or inefficient coding patterns that may affect code quality, maintainability, or long-term reliability.

**Business impact:** Code smells indicate poor coding practices that increase technical debt, reduce maintainability, and slow development. They can lead to performance issues, hidden bugs, and costly refactoring as the system grows. Over time, unmanaged code smells reduce productivity and create instability in applications.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-892df9ba90b46d2cf3213d82d14642e9c5279a49%2Fcode%20security%20code%20smell.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="197" valign="top">Setting</th><th width="325" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity<br>(dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">All (including Info)</td></tr><tr><td valign="top">Always set to Info severity<br>(checkbox)</td><td valign="top">Forces all code smell findings to be created as Info severity only.</td><td valign="top">OFF</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr></tbody></table>

</details>

## View policy issues

1. Open the Active Issues page.
2. Use the **Category** filter and select the policy category to view related active issues.
3. Use the **Policy** filter to narrow the list to a specific policy.
4. Apply the Category and Policy filters separately or together, depending on how specific you want the results to be.
5. Use the search box to refine results, such as filtering by file name, keyword, or rule identifier.

## Create or save policy profiles

You can also view code-related issues on the Application page, where the Issues tab shows findings linked to that application.

When you change a policy’s severity, ON/OFF toggle or any other setting, you must save the current profile or create a new one.

* To save the current profile, click **SAVE** in the page header.
* To create a new profile, click **SAVE AS** in the page header. For instructions, see the section [Create or edit policy profiles](https://open-2c.gitbook.com/url/preview/site_RHimt/~/revisions/esBak1HVuTgsCEeNbzHE/policies?theme=light#create-or-edit-policy-profiles)in the [Policies](https://docs.ox.security/ox-policies/policies)article.
