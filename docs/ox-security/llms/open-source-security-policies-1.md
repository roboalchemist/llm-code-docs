# Source: https://docs.ox.security/ox-policies/open-source-security-policies-1.md

# Open Source Security Policies

Open Source Security policies identify vulnerabilities and risks in open-source and third-party components that your applications rely on. Addressing these issues early in the CI/CD process can prevent supply chain attacks, data exposure, and system compromise.

The article describes the policies in this category, configuration options, and the impact of policy violations. For an overview of policies and policy management, see the [Policies](https://docs.ox.security/ox-policies)article.

## **View and manage Open Source Security policies** <a href="#view-and-manage-code-security-policies" id="view-and-manage-code-security-policies"></a>

Open each policy to view the business impact and optional settings.

<details>

<summary><mark style="color:purple;">Vulnerable dependency (CVE) in code</mark></summary>

**Purpose:** Detects known vulnerabilities (CVEs) in third-party dependencies used by the application code.

**Business impact:** Using dependencies with known CVEs exposes applications to breaches, unauthorized access, and system failures. OSS/SCA scanning identifies these vulnerabilities early and reduces supply-chain risk. Incidents such as Log4Shell show how a single vulnerable library can impact many applications.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-07cda60001df165e498faca069b49932b7bdf6cb%2Fopen%20source%20security%20vulnerable%20dependency%20cve%20in%20code.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="215" valign="top">Setting</th><th width="298" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">All (including Info)</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Vulnerable base image (CVE) in Dockerfile</mark></summary>

**Purpose:** Detects known vulnerabilities (CVEs) in base images referenced in Dockerfiles.

**Business impact:** Scanning Dockerfiles for vulnerable base images identifies security flaws at the source, before they appear in the final container image. This helps remediate issues at the foundational level and prevents weaknesses from spreading across all containers built from the same image. Addressing base-image CVEs early reduces the risk of unauthorized access, data breaches, and other security incidents.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-a828cce56df6fbe2918aed7879d38d9e2ade8af9%2Fopen%20source%20security%20vulnerable%20base%20image%20cve%20dockerfile.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="215" valign="top">Setting</th><th width="298" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">All (including Info)</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr></tbody></table>

</details>

## View policy issues

1. Open the Active Issues page.
2. Use the **Category** filter and select the policy category to view related active issues.
3. Use the **Policy** filter to narrow the list to a specific policy.
4. Apply the Category and Policy filters separately or together, depending on how specific you want the results to be.
5. Use the search box to refine results, such as filtering by file name, keyword, or rule identifier.

## Create or save policy profiles

You can also view affected dependencies on the SBOM page or in an application’s Issues tab.

When you change a policy’s severity, ON/OFF toggle or any other setting, you must save the current profile or create a new one.

* To save the current profile, click **SAVE** in the page header.
* To create a new profile, click **SAVE AS** in the page header. For instructions, see the section [Create or edit policy profiles](https://open-2c.gitbook.com/url/preview/site_RHimt/~/revisions/esBak1HVuTgsCEeNbzHE/policies?theme=light#create-or-edit-policy-profiles)in the [Policies](https://docs.ox.security/ox-policies/policies)article.
