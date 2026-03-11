# Source: https://docs.ox.security/ox-policies/cloud-context-policies-1.md

# Cloud Context Policies

Cloud Context policies identify security risks, hardcoded secrets and PII, and misconfigurations in your cloud environments. OX evaluates cloud assets using cloud provider metadata and configuration data to identify risk and exposures.

The article describes the policies in this category, configuration options, and the impact of policy violations. For an overview of policies and policy management, see the [Policies](https://docs.ox.security/ox-policies)article.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-c19ce1b842fe0dc739b291dd90f483904c5ba026%2Fcloud%20context%20summary.png?alt=media" alt=""><figcaption></figcaption></figure>

## View and manage Cloud Context policies

Open each policy to view the business impact and optional settings.

<details>

<summary><mark style="color:purple;">CSPM issue</mark></summary>

**Purpose:** Detects cloud environment misconfigurations.

**Business impact:** Misconfigured cloud environments increase the risk of unauthorized access, data exposure, and compliance violations. CSPM evaluates cloud configurations against security benchmarks to identify risky settings early. Addressing these findings reduces the likelihood of security incidents and regulatory issues.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-c8c499e7656e54743e01e034d8baebb709af9292%2Fcloud%20contet%20cspm%20issue.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="228.333251953125" valign="top">Setting</th><th width="300.6666259765625" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">All (including Info)</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">CSPM secret</mark></summary>

**Purpose:** Detects hardcoded secrets stored in cloud environments.

**Business impact:** Storing secrets insecurely in cloud environments increases the risk of unauthorized access, data breaches, and broader infrastructure compromise. Secrets such as API keys, tokens, and credentials that are exposed or misconfigured in cloud services can be exploited by attackers. Identifying and securing these secrets early helps protect cloud environments and reduce the impact of security incidents.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-49e37c561fa02590a6d5665a003a198f3f3c4301%2Fcloud%20context%20cspm%20secret.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="231.666748046875" valign="top">Setting</th><th width="294.666748046875" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">All (including Info)</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">PII in Runtime</mark></summary>

**Purpose:**&#x44;etects exposure of personally identifiable information in applications, workloads, and cloud storage during runtime execution.

**Business impact:** Exposed personally identifiable information (PII) during runtime increases the risk of privacy violations and regulatory impact. Runtime PII, such as email addresses or credit card numbers, may be processed by applications and can be exploited if exposed. Protecting PII during runtime helps maintain user trust and supports compliance with data protection regulations.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-2e657232776d6a24fa3e6235d053bd8adfa8a9c7%2Fcloud%20context%20PII%20in%20Runtime.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="230.6666259765625" valign="top">Setting</th><th width="297.3333740234375" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">All (including Info)</td></tr><tr><td valign="top">Report PII On<br>(dropdown)</td><td valign="top"><p>Resource locations that OX scans to detect exposed secrets.<br></p><p>Use the checkboxes to change the selection.</p></td><td valign="top">Current selection</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Runtime open source vulnerability</mark></summary>

**Purpose:** Detects known open-source vulnerabilities (CVEs) in components used at runtime.

**Business impact:** Failing to scan applications for vulnerabilities at runtime can leave security flaws undetected and increase the risk of breaches. Runtime vulnerability scanning identifies exploitable weaknesses while applications are running. Addressing these findings early reduces the likelihood of unauthorized access, data exposure, and system compromise.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-9f054c34648b30838d6935547052c2b910e0310d%2Fcloud%20context%20runtime%20open%20source%20vulnerability.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
This policy is only available via third-party integrations like Prisma Cloud, Wiz, Orca, Oligo, and Microsoft Defender for Cloud.
{% endhint %}

<table><thead><tr><th width="230.6666259765625" valign="top">Setting</th><th width="318.666748046875" valign="top">Description</th><th valign="top">Defau</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">All (including Info)</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Runtime operating system vulnerability</mark></summary>

**Purpose:** Detects known operating system vulnerabilities (CVEs) in runtime environments.

**Business impact:** Failing to scan operating systems for vulnerabilities at runtime allows security gaps to persist and increases the risk of system compromise. Runtime scanning identifies exploitable flaws in operating systems while they are in use. Addressing these findings early reduces the likelihood of breaches, unauthorized access, and exposure of sensitive data.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-dd8a94d84ae07157422ae03aee41a2dab80ed1d3%2Fcloud%20context%20runtime%20operating%20system%20vulnerability.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
This policy is only available via third-party integrations like Prisma Cloud, Wiz, Orca, Oligo, and Microsoft Defender for Cloud.
{% endhint %}

<table><thead><tr><th width="230.6666259765625" valign="top">Setting</th><th width="297.3333740234375" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">All (including Info)</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">SAST in cloud functions</mark></summary>

> **Note:** This capability is currently in Early Access (EA) and is not generally available. To request access, please contact OX technical support.

**Purpose:** Analyzes cloud function source code to detect security vulnerabilities using static analysis.

**Business impact:** Failing to analyze cloud function source code, such as AWS Lambdas, for security flaws allows insecure coding patterns to reach production. SAST identifies vulnerabilities in function code before runtime, reducing the risk of unauthorized access, data exposure, and logic-based attacks. Addressing these issues early improves the security of serverless workloads.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-7a5d64bde67f5c27cdad12688fb0bc1e312aaf3e%2Fcloud%20context%20SAST%20in%20cloud%20functions.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
This policy is only available via third-party integrations like Prisma Cloud, Wiz, Orca, Oligo, and Microsoft Defender for Cloud.
{% endhint %}

<table><thead><tr><th width="230.6666259765625" valign="top">Setting</th><th width="297.3333740234375" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">All (including Info)</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">SAST in runtime</mark></summary>

> **Note:** This capability is currently in Early Access (EA) and is not generally available. To request access, please contact OX technical support.

**Purpose:** Analyzes application code to detect security vulnerabilities using static analysis before runtime.

**Business impact:** Failing to analyze application code for security flaws allows insecure coding patterns to persist and increases the risk of breaches and system compromise. SAST identifies vulnerabilities in code before runtime, reducing the likelihood of unauthorized access, data exposure, and logic-based attacks. Addressing these issues early improves application security as systems evolve.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-304e4e5aa38e2be4b6a408ad76bcef274a8abd88%2Fcloud%20contet%20SAST%20in%20Runtime.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
This policy is only available via third-party integrations like Prisma Cloud, Wiz, Orca, Oligo, and Microsoft Defender for Cloud.
{% endhint %}

<table><thead><tr><th width="230.6666259765625" valign="top">Setting</th><th width="297.3333740234375" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">All (including Info)</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Secrets in cloud functions</mark></summary>

> **Note:** This capability is currently in Early Access (EA) and is not generally available. To request access, please contact OX technical support.

**Purpose:** Detects exposed secrets in cloud function code or configuration.

**Business impact:** Failing to detect exposed secrets in cloud functions, such as AWS Lambdas, increases the risk of unauthorized access and system compromise. Hardcoded or misconfigured secrets, including API keys and credentials, can be exploited to access cloud resources or sensitive data. Identifying and securing these secrets early reduces the risk of breaches and limits the impact of security incidents in serverless environments.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-8f65bae852840ff3d304d038fddf498c41777436%2Fcloud%20context%20Secrets%20in%20cloud%20functions.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
This policy is only available via third-party integrations like Prisma Cloud, Wiz, Orca, Oligo, and Microsoft Defender for Cloud.
{% endhint %}

<table><thead><tr><th width="230.6666259765625" valign="top">Setting</th><th width="297.3333740234375" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">All (including Info)</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Secrets in runtime</mark></summary>

**Purpose:** Detects exposed secrets in applications, workloads and cloud storage during runtime execution.

**Business impact:** Exposed secrets during runtime increase the risk of unauthorized access and data breaches. Runtime secrets such as API keys, tokens, and credentials are required for application operation, but if mishandled or exposed, they can be exploited by attackers. Detecting and securing runtime secrets early reduces the risk of compromise and limits the impact of security incidents.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-a394b87751932b14bc9ec09bed17b2807c5e082f%2Fcloud%20context%20Secret%20in%20Runtime%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="230.6666259765625" valign="top">Setting</th><th width="297.3333740234375" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">All (including Info)</td></tr><tr><td valign="top">Report Secrets On<br>(dropdown)</td><td valign="top"><p>Cloud resource locations that OX scans to detect exposed secrets.<br></p><p>Use the checkboxes to change the selection.</p></td><td valign="top">Current selection</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Unscanned image in Kubernetes cluster</mark></summary>

**Purpose:** Detects container images in Kubernetes clusters that have not been scanned for vulnerabilities.

**Business impact:** Running container images that have not been scanned at runtime introduces unknown security risks into Kubernetes environments. Unverified images may contain critical vulnerabilities or malicious code that attackers can exploit. Scanning images before or during runtime helps enforce security standards, reduce the attack surface, and prevent untrusted images from compromising the cluster.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-befdecc4c82a47ef866450778aff183ba598aeeb%2Fcloud%20context%20Unscanned%20image%20in%20Kubernetes%20cluster.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="230.6666259765625" valign="top">Setting</th><th width="297.3333740234375" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">OFF</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">All (including Info)</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Vulnerable dependency (CVE) in cloud functions</mark></summary>

> **Note:** This capability is currently in Early Access (EA) and is not generally available. To request access, please contact OX technical support.

**Purpose:** Detects known CVE vulnerabilities in third-party dependencies used by cloud functions.

**Business impact:** Using cloud functions that rely on third-party libraries with known CVEs exposes serverless workloads to security risks. Vulnerable dependencies can be exploited to gain unauthorized access, execute malicious code, or compromise data. Identifying and addressing these issues early reduces supply chain risk and prevents inherited vulnerabilities from reaching production.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-cb395466e170e36ec81c9125395d9bc314e40b3a%2Fcloud%20context%20Vulnerable%20dependency%20(CVE)%20in%20cloud%20functions.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
This policy is only available via third-party integrations like Prisma Cloud, Wiz, Orca, Oligo, and Microsoft Defender for Cloud.
{% endhint %}

<table><thead><tr><th width="230.6666259765625" valign="top">Setting</th><th width="297.3333740234375" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">All (including Info)</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Vulnerable dependency (CVE) in VM</mark></summary>

> **Note:** This capability is currently in Early Access (EA) and is not generally available. To request access, please contact OX technical support.

**Purpose:** Detects known CVE vulnerabilities in third-party dependencies installed on virtual machines.

**Business impact:** Using virtual machines that contain dependencies with known CVEs exposes systems to exploitation and compromise. Vulnerable third-party libraries installed on VMs can be abused to gain unauthorized access, escalate privileges, or disrupt workloads. Identifying and addressing these vulnerabilities early reduces supply chain risk and helps protect running virtual machine environments.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-7d995a1f5dcb94492ff430f1028c4e52374d6a7d%2Fcloud%20context%20Vulnerable%20dependency%20(CVE)%20in%20VM%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
This policy is only available via third-party integrations like Prisma Cloud, Wiz, Orca, Oligo, and Microsoft Defender for Cloud.
{% endhint %}

<table><thead><tr><th width="230.6666259765625" valign="top">Setting</th><th width="297.3333740234375" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">All (including Info)</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Vulnerability management</mark></summary>

**Purpose:** Detects security issues across the environment, including obsolete software, misconfigurations, and system vulnerabilities.

**Business impact:** Unmanaged vulnerabilities increase the risk of unauthorized access, data breaches, and operational disruption. The Vulnerability Management policy identifies security issues such as end-of-life software, insecure configurations, and system weaknesses across the environment. Addressing these findings reduces overall risk exposure and helps maintain a secure and compliant infrastructure.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-3e3f8fe668006232cbc98a82edb4ea9ab4465d91%2Fcloud%20context%20Vulnerability%20Management.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
This policy is only available via third-party integrations like Qualys.
{% endhint %}

<table><thead><tr><th width="230.6666259765625" valign="top">Setting</th><th width="297.3333740234375" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">All (including Info)</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Vulnerable public image (CVE) in Kubernetes cluster</mark></summary>

**Purpose:** Detects Kubernetes workloads that use public container images with known CVEs.

**Business impact**: Using public container images without vulnerability scanning introduces security risks into Kubernetes clusters. Images from public registries may contain known vulnerabilities that attackers can exploit to gain unauthorized access or compromise data. Scanning public images before deployment helps block high-risk images and reduces the risk of cluster compromise.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-3de0f14001d9c9fdbb5e49068ce3b7449f84c2e0%2Fcloud%20context%20Vulnerable%20public%20image%20(CVE)%20in%20Kubernetes%20cluster.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="228.333251953125" valign="top">Setting</th><th width="300.6666259765625" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">All (including Info)</td></tr></tbody></table>

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
