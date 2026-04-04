# Source: https://docs.ox.security/ox-policies/sbom-policies.md

# SBOM Policies

SBOM policies control the quality, safety, and compliance of third party libraries. The policies validate dependency and artifact metadata including completeness, accuracy and licensing compliance across the supply chain.

The article describes the policies in this category, configuration options, and the impact of policy violations. For an overview of policies and policy management, see the [Policies](https://docs.ox.security/ox-policies)article.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-9dd81619e8926c81ceb36fabd341d39394fa9fb1%2FLicense%20SBOM%20section%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

## **SBOM policy categories**

<table><thead><tr><th width="144" valign="top">Category</th><th width="215" valign="top">Policy</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top">License</td><td valign="top">Unapproved license detected by 3rd party security app</td><td valign="top">Detects components identified by an integrated third-party security tool as using licenses that are not approved by your organization.</td></tr><tr><td valign="top">License</td><td valign="top">Unapproved license used by direct dependency in code</td><td valign="top">Checks direct dependencies in the codebase for licenses that are not approved by your organization.</td></tr><tr><td valign="top">License</td><td valign="top">Unapproved license used by indirect dependency in code</td><td valign="top">Checks indirect (transitive) dependencies for licenses that are not approved by your organization.</td></tr><tr><td valign="top">License</td><td valign="top">Unapproved license used in forked open source</td><td valign="top">Checks forked open-source projects for licenses that are not approved by your organization.</td></tr><tr><td valign="top">Maintenance</td><td valign="top">Deprecated direct dependency in code</td><td valign="top">Identifies direct dependencies in the codebase that are marked as deprecated by their maintainers.</td></tr><tr><td valign="top">Maintenance</td><td valign="top">Deprecated indirect dependency in code</td><td valign="top">Identifies indirect dependencies that are marked as deprecated by their maintainers.</td></tr><tr><td valign="top">Maintenance</td><td valign="top">Outdated direct dependency in code</td><td valign="top">Detects direct dependencies that do not use the latest available versions.</td></tr><tr><td valign="top">Maintenance</td><td valign="top">Outdated indirect dependency in code</td><td valign="top">Detects indirect dependencies that do not use the latest available versions.</td></tr><tr><td valign="top">Maintenance</td><td valign="top">Unpopular direct dependency in code</td><td valign="top">Identifies direct dependencies with low adoption or usage signals in the ecosystem.</td></tr><tr><td valign="top">Maintenance</td><td valign="top">Unpopular indirect dependency in code</td><td valign="top">Identifies indirect dependencies with low adoption or usage signals in the ecosystem.</td></tr><tr><td valign="top">Maintenance</td><td valign="top">Unused direct dependency in code</td><td valign="top">Detects direct dependencies that are declared but not referenced in the codebase.</td></tr><tr><td valign="top">Malware</td><td valign="top">Dependency confusion: organization scope in code</td><td valign="top">Detects dependency confusion risks where public packages may override organization-scoped packages.</td></tr><tr><td valign="top">Malware</td><td valign="top">Dependency confusion: private package in code</td><td valign="top">Detects dependency confusion risks involving private packages that may be shadowed by public packages.</td></tr><tr><td valign="top">Malware</td><td valign="top">Malicious dependency in code</td><td valign="top">Identifies dependencies that are known or suspected to contain malicious code.</td></tr><tr><td valign="top">Malware</td><td valign="top">Typosquatting dependency in code</td><td valign="top">Detects dependencies with names that closely resemble popular packages and may indicate typosquatting.</td></tr><tr><td valign="top">Malware</td><td valign="top">Untrusted source for dependency in code</td><td valign="top">Identifies dependencies that are downloaded from sources not approved or trusted by your organization.</td></tr></tbody></table>

## License policies

For license policies, see the article [License policies<mark style="color:$primary;">.</mark>](https://docs.ox.security/ox-policies/license-policies)

## Maintenance policies

Open each policy to view the business impact and optional settings.

<details>

<summary><mark style="color:purple;">Deprecated direct dependency in code</mark></summary>

**Purpose:** Identifies transitive dependencies in the codebase that are marked as deprecated by their maintainers.

**Business impact:** Utilizing libraries that are deprecated increases security and compatibility risks because they are no longer maintained.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-72ab71797eb978598a2bae6aa81bf3894cc7e4ec%2Fsbom%20maintenance%20Deprecated%20direct%20dependency%20in%20code.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th valign="top">Setting</th><th valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">OX severity setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Deprecated indirect dependency in code</mark></summary>

**Purpose:** Identifies transitive dependencies in the codebase that are marked as deprecated by their maintainers.

**Business impact:** Unused dependencies in code add risk and waste resources. Remove them to reduce your attack surface. Removal lowers maintenance effort, avoids hidden vulnerabilities, and improves build performance.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-f02afb41aeecbf0aba8e401b065a55ecb3267c65%2Fsbom%20maintenance%20Deprecated%20indirect%20dependency%20in%20code%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="191" valign="top">Setting</th><th width="327" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">OFF</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">OX severity setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Outdated direct dependency in code</mark></summary>

**Purpose:** Identifies direct dependencies in the codebase that are outdated.

**Business impact:** Outdated libraries block access to security fixes and improvements. Open source projects update their packages often, and older versions may contain known vulnerabilities. Update your dependencies regularly to keep your code secure and stable.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-437e9d1a0ee2ae49d25d8e52478a1f9b71699eb6%2Fsbom%20maintenance%20Outdated%20direct%20dependency%20in%20code%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="178" valign="top">Setting</th><th width="345" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">OFF</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">OX severity setting</td></tr><tr><td valign="top">Compare (dropdown)</td><td valign="top">Major version: When selected there is no violation if the latest version of a library is just a minor version change.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Major version draft</td><td valign="top">A violation occurs only if the difference between the latest major version and the deployed major version is greater than or equal to the drift.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Days since update</td><td valign="top">Days that a library that has a newer version can remain without being updated.</td><td valign="top">Calculation</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Outdated indirect dependency in code</mark></summary>

**Purpose**: Identifies transitive dependencies in the codebase that are outdated based on either drift from the latest major version or the number of days since the last update was released.

**Business impact:** Outdated libraries block access to security fixes and improvements. Open source projects update their packages often, and older versions may contain known vulnerabilities. Update your dependencies regularly to keep your code secure and stable.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-ccac1f74b5fb8fe4b77a5b3a6fe202f13d0d5993%2Fsbom%20maintenance%20Outdated%20indirect%20dependency%20in%20code%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="189" valign="top">Setting</th><th width="330" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">OFF</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">OX severity setting</td></tr><tr><td valign="top">Compare (dropdown)</td><td valign="top">Major version: When selected there is no violation if the latest version of a library is just a minor version change.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Major version draft</td><td valign="top">A violation occurs only if the difference between the latest major version and the deployed major version is greater than or equal to the drift.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Days since update</td><td valign="top">Days that a library that has a newer version can remain without being updated.</td><td valign="top">Calculation</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Unpopular direct dependency in code</mark></summary>

**Purpose:** Identifies direct dependencies in the codebase that have low adoption or limited community usage.

**Business impact:** Libraries with very few users increase risk because the libraries receive less review and slower updates. Choose popular libraries to reduce security and reliability risks. Widely used libraries tend to be more stable and better maintained.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-22bd73e8d42f9a7094153f5176af5efdbfd7106d%2Fsbom%20maintenance%20Unpopular%20direct%20dependency%20in%20code.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="175" valign="top">Setting</th><th width="340" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">OFF</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">OX severity setting</td></tr><tr><td valign="top">Stars count</td><td valign="top">Minimum number of stars. A violation occurs only when all arguments (forks, stars, downloads if available) are violated.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Downloads count</td><td valign="top">Minimum number of downloads. A violation occurs only when all arguments (forks, stars, downloads if available) are violated.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Forks count</td><td valign="top">The minimum number of forks. A violation occurs only when all arguments (forks, stars, downloads if available) are violated.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Unpopular indirect dependency in code</mark></summary>

**Purpose:** Identifies indirect dependencies with low adoption or usage signals in the ecosystem.

**Business impact:** Libraries with very few users increase risk because the libraries receive less review and slower updates. Choose popular libraries to reduce security and reliability risks. Widely used libraries tend to be more stable and better maintained.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-29deb6ce6094750345b8a480a395a729f75405ac%2Fsbom%20maintenance%20Unpopular%20indirect%20dependency%20in%20code%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="185" valign="top">Setting</th><th width="357" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">OFF</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">OX severity setting</td></tr><tr><td valign="top">Stars count</td><td valign="top">Minimum number of stars. A violation occurs only when all arguments (forks, stars, downloads if available) are violated.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Downloads count</td><td valign="top">Minimum number of downloads. A violation occurs only when all arguments (forks, stars, downloads if available) are violated.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Forks count</td><td valign="top">The minimum number of forks. A violation occurs only when all arguments (forks, stars, downloads if available) are violated.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Unused direct dependency in code</mark></summary>

**Purpose:** Detects direct dependencies that are declared but not referenced in the codebase.

**Business impact:** Unused dependencies increase security and maintenance risk. Remove them to reduce your attack surface, lower maintenance effort, avoid hidden vulnerabilities, and improve build performance.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-d726f50414c6565f6fec616c6139235b47e84a0c%2Fsbom%20maintenance%20Unused%20direct%20dependency%20in%20code%20(2).png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="189" valign="top">Setting</th><th width="331" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">OX severity setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr></tbody></table>

</details>

## Malware policies

Open each policy to view the business impact and optional settings.

<details>

<summary><mark style="color:purple;">Dependency confusion: organization scope in code</mark></summary>

**Purpose:** Detects dependency confusion risks where public packages may override organization-scoped packages.

**Business impact:** A violation increases the chance that builds install a public package that impersonates an internal one. This can lead to unauthorized code execution, data exposure, service disruption, and full compromise of internal workloads. It also weakens supply chain controls and increases the effort needed to detect and recover from malicious package substitution.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-5c1f55d2bac62c4799bf1443b02b1a94da3d6c75%2Fsbom%20malware%20Dependency%20confusion%20organization%20scope%20in%20code%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

| Setting                                                                  | Description                                                           | Default             |
| ------------------------------------------------------------------------ | --------------------------------------------------------------------- | ------------------- |
| ON/OFF (toggle)                                                          | Enable/disable the policy.                                            | ON                  |
| Show issues of severity (dropdown)                                       | Limits which severities appear as issues.                             | OX severity setting |
| Ignore internal package scopes                                           | Add package names                                                     | Current setting     |
| Ignore Application Business Priority for severity calculation (checkbox) | When enabled, severity is not adjusted based on application priority. | OFF                 |

</details>

<details>

<summary><mark style="color:purple;">Dependency confusion: private package in code</mark></summary>

**Purpose:** Detects dependency confusion risks involving private packages that may be shadowed by public packages.

**Business impact:** A violation increases the risk that builds install a public package that uses your internal organization scope. Attackers use this naming collision to run unauthorized code, leak sensitive data, or disrupt services. As your organization increases the use of open source, the negative impact from attacks increases.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-bcd4972ebb5d77648cd0666ea48a442bfb877e57%2Fsbom%20malware%20Dependency%20confusion%20private%20package%20in%20code%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="191" valign="top">Setting</th><th width="331" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">OX severity setting</td></tr><tr><td valign="top">Ignore internal package scopes</td><td valign="top">Add package names</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Malicious dependency in code</mark></summary>

**Purpose:** Identifies dependencies that are known or suspected to contain malicious code.

**Business impact:** A violation increases the risk that your codebase includes a dependency that contains harmful or hostile code. A malicious dependency can steal data, execute unauthorized commands, move laterally inside your environment, or take over VMs and workloads. It also weakens supply chain security and increases the effort needed to detect, contain, and recover from an intrusion.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-3787b7771a24ada0f6b002ecae82780b16b61562%2Fsbom%20malware%20Malicious%20dependency%20code%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="180" valign="top">Setting</th><th width="336" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">OX severity setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">ON</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Typosquatting dependency in code</mark></summary>

**Purpose:** Detects dependencies with names that closely resemble popular packages and may indicate typosquatting.

**Business impact:** A violation increases the chance that developers install a package that impersonates a trusted dependency. A typosquatting package can run malicious code, steal data, move laterally inside your environment, or take over workloads. It also weakens supply chain security and raises the risk of unnoticed compromise during development or build processes.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-6025d2fb054e23d088a1718c0dea6768396abb6f%2Fsbom%20malware%20Typosquatting%20dependency%20in%20code%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

| Setting                                                                  | Description                                                           | Default             |
| ------------------------------------------------------------------------ | --------------------------------------------------------------------- | ------------------- |
| ON/OFF (toggle)                                                          | Enable/disable the policy.                                            | ON                  |
| Show issues of severity (dropdown)                                       | Limits which severities appear as issues.                             | OX severity setting |
| Ignore internal package scopes                                           | Add package names                                                     | Current setting     |
| Ignore Application Business Priority for severity calculation (checkbox) | When enabled, severity is not adjusted based on application priority. | OFF                 |

</details>

<details>

<summary><mark style="color:purple;">Untrusted source for dependency in code</mark></summary>

**Purpose:** Identifies dependencies that are downloaded from sources not approved or trusted by your organization.

**Business impact:** A violation exposes applications to malicious code, data theft, and unauthorized access. Untrusted sources can introduce harmful dependencies into the supply chain and compromise systems or disrupt services. Use only verified and trusted repositories to protect the integrity of your builds.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-0bbcc3fbafccc09857d7d26811d886942defe6fb%2Fsbom%20malware%20Untrusted%20source%20for%20dependency%20code%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

| Setting                                                                  | Description                                                           | Default             |
| ------------------------------------------------------------------------ | --------------------------------------------------------------------- | ------------------- |
| ON/OFF (toggle)                                                          | Enable/disable the policy.                                            | OFF                 |
| Show issues of severity (dropdown)                                       | Limits which severities appear as issues.                             | OX severity setting |
| Whitelisted sources                                                      | Click to add a URL.                                                   | Current setting     |
| Ignore Application Business Priority for severity calculation (checkbox) | When enabled, severity is not adjusted based on application priority. | OFF                 |

> Java and JS/TS projects are supported.

</details>

## View policy issues

1. Open the Active Issues page.
2. Use the **Category** filter and select the policy category to view related active issues.
3. Use the **Policy** filter to narrow the list to a specific policy.
4. Apply the Category and Policy filters separately or together, depending on how specific you want the results to be.
5. Use the search box to refine results, such as filtering by file name, keyword, or rule identifier.

## Create or save policy profiles

You can also use the **Issues** filter on the SBOM page.

When you change a policy’s severity, ON/OFF toggle or any other setting, you must save the current profile or create a new one.

* To save the current profile, click **SAVE** in the page header.
* To create a new profile, click **SAVE AS** in the page header. For instructions, see the section [Create or edit policy profiles](https://open-2c.gitbook.com/url/preview/site_RHimt/~/revisions/esBak1HVuTgsCEeNbzHE/policies?theme=light#create-or-edit-policy-profiles)in the [Policies](https://docs.ox.security/ox-policies/policies)article.
