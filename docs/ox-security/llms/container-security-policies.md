# Source: https://docs.ox.security/ox-policies/container-security-policies.md

# Container Security Policies

Container Security policies identify security risks in container images and their underlying components. The policies evaluate dependencies introduced through base images, operating system layers, user code, and build instructions, as well as configuration settings and sensitive data embedded in containers.

Identifying vulnerabilities, misconfigurations, and policy violations early helps reduce supply chain risk and limits the likelihood of insecure images being deployed into runtime environments.

The article describes the policies in this category, configuration options, and the impact of policy violations. For an overview of policies and policy management, see the [Policies](https://docs.ox.security/ox-policies)article.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-0316183859bb4a85da0a6e041d144c9d86115d5d%2FContainer%20security%20summary.png?alt=media" alt=""><figcaption></figcaption></figure>

## View and manage Container Security policies

Open each policy to view the business impact and optional settings.

<details>

<summary><mark style="color:purple;">Deprecated dependency in container from user code or instruction</mark></summary>

> **Note:** This capability is currently in Early Access (EA) and is not generally available. To request access, please contact OX technical support.

**Purpose:** Identifies deprecated libraries introduced into container images through user code or build instructions.

**Business impact:** Deprecated libraries are no longer maintained and may not receive security fixes, increasing the risk of vulnerabilities and instability. Continuing to use deprecated dependencies can expose containerized applications to known security issues and operational risk.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-341afbe88f176454f325956b7d4d9c138dc03d44%2Fcontainer%20security%20Deprecated%20dependency%20in%20container%20from%20user%20code%20or%20instruction%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="228.333251953125" valign="top">Setting</th><th width="282.6666259765625" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Malicious dependency in container</mark></summary>

**Purpose:** Detects third-party libraries or packages embedded in container images that contain malicious code.

**Business impact:** Malicious dependencies can be exploited to steal data, execute remote code, enable lateral movement, or take over underlying systems. These dependencies may be introduced through techniques such as typosquatting, dependency confusion, or compromised repositories, increasing the risk of severe security breaches in containerized environments.

For more on this policy, see the article [Malicious Dependencies](https://docs.ox.security/ox-policies/malicious-dependencies).

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-4bca788181f69e37d313f20eed89931a54e1a1dc%2Fcontainer%20security%20Malicious%20dependency%20in%20container%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="231.666748046875" valign="top">Setting</th><th width="294.666748046875" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">OFF</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Misconfiguration in container</mark></summary>

**Purpose:** Identifies insecure or non-compliant configuration settings in container images and container runtime settings.

When enabling this policy, any container misconfiguration with a severity higher than the set limit triggers a security issue.

**Business impact:** Container misconfigurations can introduce security vulnerabilities that expose applications and infrastructure to attack. Issues related to base images, user permissions, network access, or file system settings can be exploited to gain unauthorized access or compromise running services, leading to severe business and security impacts.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-45f6feb051c3eaf2c345b0be8290006ba1a95c3e%2Fcontainer%20security%20Misconfiguration%20in%20container.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="231.666748046875" valign="top">Setting</th><th width="294.666748046875" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">All (including Info)</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Outdated dependency in container from user code or instruction</mark></summary>

**Purpose:** Identifies libraries introduced into container images through user code or build instructions that are not using current versions.

When enabling this policy, any container misconfiguration with a severity higher than the set limit triggers a security issue.

**Business impact:** Outdated libraries may miss important security fixes and improvements available in newer versions. Continuing to use outdated dependencies increases exposure to known vulnerabilities and reduces the overall security and reliability of containerized applications.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-5cf761be9634e397b62b98b84d2b4437e9cb6732%2Fcontainer%20security%20Outdated%20dependency%20in%20container%20from%20user%20code%20or%20instruction.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th valign="top">Setting</th><th valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">OFF</td></tr><tr><td valign="top">Compare</td><td valign="top">When a major version is selected, there will be no violation if the latest version of a library is just a minor version change.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Major version draft</td><td valign="top"><p>Major Version Drift<br></p><p>A violation will occur only if the difference between the latest major version and the deployed major version is more than or equal to the drift.</p></td><td valign="top">Current setting</td></tr><tr><td valign="top">Days since update</td><td valign="top">Days that a library that has a newer version can remain without being updated.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Pll in container</mark></summary>

**Purpose:** Detects hardcoded personally identifiable information (PII) present within container images.

**Business impact:** Storing PII in container images increases the risk of data exposure and privacy violations. If container images are shared, reused, or accessed without proper controls, exposed PII may lead to regulatory non-compliance and loss of user trust.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-c64b82a673eaff189d0c25c1bf737d4563647fd1%2Fcontainer%20security%20PII%20in%20container.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="231.666748046875" valign="top">Setting</th><th width="294.666748046875" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">All (including Info)</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Secret in container</mark></summary>

**Purpose:** Detects hardcoded secrets in container images or exposed through insecure container configuration.

**Business impact:** Embedded or misconfigured secrets in container environments can expose sensitive information and enable unauthorized access. If secrets are included directly in images or improperly protected, attackers may exploit them to access systems or data, increasing the risk of breaches and loss of confidentiality.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-033d140b309d360f5fa647d3c631b24e5356692b%2Fcontainer%20security%20Secret%20in%20container.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="231.666748046875" valign="top">Setting</th><th width="294.666748046875" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">All (including Info)</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr><tr><td valign="top">Generate issue for base image secrets (toggle)</td><td valign="top">Enable/disable</td><td valign="top">ON</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Unapproved dependency license in container from user code or instruction</mark></summary>

**Purpose:** Sets specific licenses that are approved for usage in open-source libraries. This policy will detect if any open-source library introduced into container images through user code or build instructions violates these settings.

* Users can configure a list of approved licenses OR unapproved licenses
* When this policy is enabled, any license not in the approved list is considered unapproved.

**Business impact: Using** dependencies with unapproved licenses in containers can create legal and compliance risks. License terms may conflict with organizational policies or legal obligations, potentially leading to intellectual property disputes or financial liability.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-f3295581e58a8f1e71593e476b14b8bb1c409472%2Fcontainer%20security%20Unapproved%20dependency%20license%20in%20container%20from%20user%20code%20or%20instruction.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="255.666748046875" valign="top">Setting</th><th width="282.666748046875" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">OFF</td></tr><tr><td valign="top">Approved licenses<br>(SPDX format)</td><td valign="top"><p>Add/remove licenses.</p><p>Use the SPDX format to add.</p></td><td valign="top">Current setting</td></tr><tr><td valign="top">Not approved licenses<br>(SPDX format)</td><td valign="top"><p>Add/remove licenses.</p><p>Use the SPDX format to add.</p></td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Unpopular dependency in container from user code or instruction</mark></summary>

**Purpose:** Sets minimal popularity metrics (stars/downloads/forks) for libraries introduced into container images through user code or build instructions. When enabling this policy, any library detected with less than the set limit will trigger a security issue.

**Business impact:** Libraries with very few users are less likely to be actively reviewed, maintained, or tested, which can increase security and stability risks. Using widely adopted libraries is generally safer, as they tend to be more stable and receive more frequent updates and community scrutiny.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-8cb7f116ffb729ed4c6d4767ab4a40c9d91b5ba5%2Fcontainer%20security%20Unpopular%20dependency%20in%20container%20from%20user%20code%20or%20instruction.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="231.666748046875" valign="top">Setting</th><th width="294.666748046875" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">OFF</td></tr><tr><td valign="top">Stars count</td><td valign="top"><p>Minimum number of stars.<br></p><p>Policy violation occurs only when all arguments (forks, stars, and downloads, if available) are violated.</p></td><td valign="top">Current setting</td></tr><tr><td valign="top">Downloads count</td><td valign="top"><p>Minimum number of downloads.</p><p><br>Policy violation occurs only when all arguments (forks, stars, and downloads if available) are violated.</p></td><td valign="top">Current setting</td></tr><tr><td valign="top">Forks counts</td><td valign="top"><p>Minimum number of forks.</p><p><br>Policy violation occurs only when all arguments (forks, stars, and downloads, if available) are violated.</p></td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Vulnerable dependency (CVE) in container from base image</mark></summary>

**Purpose**: Detects known vulnerabilities in dependencies inherited from the container base image. When enabled, any CVE detected in a base image’s dependency with a severity higher than the set limit triggers a security issue.

**Business impact: Base** images often include operating system components and libraries that applications rely on to run. Vulnerabilities in these foundational components can be inherited by all containers built from the image, increasing the attack surface and risk of exploitation. Identifying base image vulnerabilities early helps ensure containers are built on secure, up-to-date foundations.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-1b788e6eb696d64344bb3fcb7c1cdb6c80bacf14%2Fcontainer%20security%20Vulnerable%20dependency%20(CVE)%20in%20container%20from%20base%20image.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="231.666748046875" valign="top">Setting</th><th width="294.666748046875" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">All (including Info)</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Vulnerable dependency (CVE) in container from operating system</mark></summary>

**Purpose:** Detects known operating system vulnerabilities present in the operating system layer of container images. When enabling this policy, any CVE detected in the container’s operating system with a severity higher than the set limit will trigger a security issue.

**Business impact:** Containers rely on an underlying operating system layer that may include outdated, vulnerable, or misconfigured components. Vulnerabilities at the OS level can increase the attack surface and be exploited to compromise containerized workloads. Identifying and addressing OS-level vulnerabilities helps reduce risk and strengthens the security posture of container environments.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-d7ddc185a02090df83688c93d2b1e588bc54b3d9%2Fcontainer%20security%20Vulnerable%20dependency%20(CVE)%20in%20container%20from%20operating%20system.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="231.666748046875" valign="top">Setting</th><th width="294.666748046875" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">All (including Info)</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Vulnerable dependency (CVE) in container from user code</mark></summary>

**Purpose:** Detects known vulnerabilities in open-source libraries introduced into container images through user application code.

**Business impact:** Containers often include open-source libraries that may contain known vulnerabilities. If these vulnerabilities are not identified, they can be exploited to gain unauthorized access, expose data, or compromise systems. As the use of containers and open-source components increases, unaddressed vulnerabilities can significantly raise security risk.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-3d3ccbf0fe30dc77bc45268d3dc272aae5f4ae7a%2Fcontainer%20security%20Vulnerable%20dependency%20(CVE)%20in%20container%20from%20user%20code.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="231.666748046875" valign="top">Setting</th><th width="294.666748046875" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">All (including Info)</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Vulnerable dependency (CVE) in container from user instruction</mark></summary>

**Purpose:** Detects known vulnerabilities in open-source libraries introduced into container images through user-defined build instructions in the Dockerfile. When enabling this policy, any CVE detected in the container’s dockerfile instructions with a severity higher than the set limit will trigger a security issue.

**Business impact:** Dependencies added through Dockerfile instructions may include open-source libraries with known vulnerabilities. If these vulnerabilities are not identified, they can be exploited to gain unauthorized access, expose data, or compromise containerized workloads. As container builds increasingly rely on custom instructions, unscanned dependencies can significantly increase security risk.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-5c43538554cccf1cc7390cd9f503f500ac84a69c%2Fcontainer%20security%20Vulnerable%20dependency%20(CVE)%20in%20container%20from%20user%20instruction.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="231.666748046875" valign="top">Setting</th><th width="294.666748046875" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">All (including Info)</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Vulnerable dependency (CVE) in Java archive package</mark></summary>

**Purpose:** Detects known vulnerabilities in Java archive (JAR) packages included in container images.

When enabled, any CVE detected in a dependency located in a JAR artifact with a severity higher than the set limit triggers a security issue.

**Business impact:** Java archive packages may contain critical security flaws that can be exploited if left unaddressed. Failing to identify vulnerabilities in these components can lead to unauthorized access, data exposure, and broader application compromise.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-2bbcd09f0283183f9a14d3f36b2627f3d0918f03%2Fcontainer%20security%20Vulnerable%20dependency%20(CVE)%20in%20Java%20archive%20package.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="231.666748046875" valign="top">Setting</th><th width="294.666748046875" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">All (including Info)</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Vulnerable dependency (CVE) in public image hosted in private registry</mark></summary>

**Purpose: Detects** known vulnerabilities in public container images that are hosted or mirrored in private registries.

When enabled, any CVE detected in a privately hosted public image with a severity higher than the set limit triggers a security issue.

**Business impact: Public** images hosted on private registries may contain vulnerable dependencies that can be exploited. Failing to identify these vulnerabilities increases the risk of security breaches and operational disruption, even when images are stored in internal registries.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-3ec379aea8fbd7455cd101cbf0515266555c8453%2Fcontainer%20security%20Vulnerable%20dependency%20(CVE)%20in%20public%20image%20hosted%20in%20private%20registry%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="231.666748046875" valign="top">Setting</th><th width="294.666748046875" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">All (including Info)</td></tr></tbody></table>

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
