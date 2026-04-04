# Source: https://docs.ox.security/ox-policies/cloud-context-policies-2.md

# Git Posture Policies

Git Posture policies assess repository, organization, and user configurations that affect source control security and governance. These policies focus on access control, branch protection, review practices, authentication, ownership, and repository hygiene. Proper Git posture reduces the risk of unauthorized changes, account compromise, supply chain attacks, and loss of control over source code.

The article describes the policies in this category, configuration options, and the impact of policy violations. For an overview of policies and policy management, see the [Policies](https://docs.ox.security/ox-policies)article.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-c19ce1b842fe0dc739b291dd90f483904c5ba026%2Fcloud%20context%20summary.png?alt=media" alt=""><figcaption></figcaption></figure>

## Source control policy coverage

Open the accordion to view the list of Git Posture policies supported for each source control.

<details>

<summary><mark style="color:purple;">Policies supported for each source control manager</mark></summary>

<table data-full-width="true"><thead><tr><th width="203.073974609375">Policy (A-Z)</th><th width="113.926025390625" align="center" valign="top">GitHub</th><th width="108.7408447265625" align="center" valign="top">GitLab</th><th width="136.1480712890625" align="center" valign="top">Azure Repos</th><th width="166.836669921875" align="center" valign="top">Bitbucket Cloud</th></tr></thead><tbody><tr><td>Bot user is a repo admin</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td></tr><tr><td>Bot user is an org owner</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td></tr><tr><td>Branch protection not enforced</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td></tr><tr><td>Branch protection code review can be ignored by developer</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td></tr><tr><td>Branch protection code review can be ignored by outside collaborator</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td></tr><tr><td>Branch protection push restriction can be ignored by developer</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td></tr><tr><td>Branch protection push restriction can be ignored by outside collaborator</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td></tr><tr><td>Branch protection allows unsigned commits</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td></tr><tr><td>CODEOWNERS file missing in repo</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">—</td><td align="center" valign="top">✓</td></tr><tr><td>External user has access to repo</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td></tr><tr><td>Missing 2FA in organization</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td></tr><tr><td>Outside collaborator not using 2FA</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td></tr><tr><td>Protected branch can be deleted by a non-admin</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td></tr><tr><td>Repo admin with no admin activity</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td></tr><tr><td>Org owner with no admin activity</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td></tr><tr><td>Single owner in org</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td></tr><tr><td>Too many org owners</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td></tr><tr><td>Too many repo admins</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td></tr><tr><td>Developer did not write code in repo</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td></tr><tr><td>Outside collaborator is a repo admin</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td></tr><tr><td>Outside collaborator is repo maintainer</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td></tr><tr><td>Outside collaborator with no activity</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td></tr><tr><td>Unreviewed code change</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td></tr><tr><td>Veteran developer review required</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td></tr><tr><td>Security Policy file missing in repo</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">—</td><td align="center" valign="top">✓</td></tr><tr><td>Repo wiki publicly available</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">—</td><td align="center" valign="top">✓</td></tr><tr><td>Personal public repo detected</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">—</td><td align="center" valign="top">✓</td></tr><tr><td>Public repo detected</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">—</td><td align="center" valign="top">✓</td></tr><tr><td>Private personal repo fork detected</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">—</td><td align="center" valign="top">✓</td></tr><tr><td>Private repo forking is enabled</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">—</td><td align="center" valign="top">✓</td></tr><tr><td>Unarchived stale repo</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td><td align="center" valign="top">✓</td></tr></tbody></table>

</details>

## View and manage Git Posture policies

Open each policy to view the business impact and optional settings.

<details>

<summary><mark style="color:purple;">Bot user is a repo admin</mark></summary>

**Purpose:** Detects repositories where a bot account is assigned administrator-level permissions.

**Supported source control managers:**

* GitHub
* GitLab
* Azure
* Bitbucket Cloud

**Business impact:** Bot accounts are not tied to individual users and compromises may go unnoticed for extended periods. Administrative access allows broad control over repository settings and code. This increases the risk of unauthorized changes, persistent access, and supply chain compromise.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-8b79ef73c95d793c4e3760e60d465e246b8928b7%2Fgit%20Posture%20Bot%20user%20is%20a%20repo%20admin.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="188.6295166015625">Setting</th><th width="366.5184326171875">Description</th><th>Default</th></tr></thead><tbody><tr><td>ON/OFF (toggle)</td><td>Enable/disable the policy.</td><td>ON</td></tr><tr><td>Ignore Application Business Priority for severity calculation (checkbox)</td><td>When enabled, severity is not adjusted based on application priority.</td><td><p>OFF</p><p><br></p></td></tr><tr><td>Bot Identification Settings</td><td>Strings used to identify bots in your organization.<br><br>Click to add strings.</td><td>Current setting</td></tr><tr><td>Ignore if admin activity seen<br>(toggle)</td><td>Ignores all bots that have known admin activity.<br><br>The setting is ignored if Audit Log permissions are not available.</td><td>ON</td></tr><tr><td>Ignore if a user is admin in multiple repos</td><td>This will ignore all bots that are admins of more than the selected number of repos</td><td>Current setting</td></tr><tr><td>Audit log access</td><td>Grant Ox access to your source control platform's audit logs. This enables the detection of admin activity across all repositories. The access is required for Ox to accurately evaluate policies related to administrative functions.</td><td>Required</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Bot user is an org owner</mark></summary>

**Purpose: Detects** organizations where a bot account is assigned the organization owner role.

**Supported Source Control Managers:**

* GitHub
* GitLab
* Azure
* Bitbucket Cloud

**Business impact:** Organization owner privileges grant full administrative control across all repositories and settings. A compromised bot account may remain undetected and enable persistent, unrestricted access. This significantly increases the risk of large-scale unauthorized changes and organizational compromise.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-28cb73b84cbc218ebf9d8455302962f897f114d1%2Fgit%20Posture%20Bot%20user%20is%20an%20org%20owner.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="248.703857421875" valign="top">Setting</th><th width="335.4073486328125" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr><tr><td valign="top">Bot Identification Settings</td><td valign="top">Strings used to identify bots in your organization.<br><br>Click to add strings.</td><td valign="top">Current setting</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Branch protection allows unsigned commits</mark></summary>

**Purpose:** Detects repositories where branch protection does not require commits to be signed.

**Supported Source Control Managers:**

* GitHub
* GitLab

**Business impact:** Unsigned commits make it easier to spoof commit authorship. Attackers can introduce code that appears to come from trusted developers. This weakens code provenance and increases the risk of unauthorized or malicious changes.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-9c1328949ab9f9c5c55f8e41847015db5b3a21e6%2FGit%20posture%20Branch%20Protection%20allows%20unsigned%20commits.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="229.1851806640625" valign="top">Setting</th><th width="366.5184326171875" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Repo Visibility (dropdown)</td><td valign="top">Determines if this policy applies to public repos, private repos or both.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Business Priority Less Than</td><td valign="top">Ignore repos with Business Priority less than the number entered.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Branch protection code review can be ignored by developer</mark></summary>

**Purpose:** Detects repositories where branch protection settings allow developers to bypass required code reviews.

**Supported Source Control Managers:**

* GitHub

**Business impact:** Allowing developers to ignore code review requirements weakens a key security and quality control. Compromised accounts can push unreviewed or malicious changes to protected branches. This increases security risk and may lead to non-compliance with standards such as SOC 2, PCI DSS, and ISO 27001.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-b5be5f0e38334aca61168c279e28bd0527253d0c%2FGit%20posture%20%20Branch%20Protection%20code%20review%20can%20be%20ignored%20by%20developer.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="268" valign="top">Setting</th><th width="290.4815673828125" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Repo Visibility<br>(dropdown)</td><td valign="top">Choose if the policy applies to private, public or all repo types.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Business Priority Less Than</td><td valign="top">Ignore repos with Business Priority less than the number entered.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Choose an Available Fix for a Violation</td><td valign="top">Pick between the options of available fixes for violation.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Branch protection code review can be ignored by outside collaborator</mark></summary>

**Purpose:** Detects repositories where branch protection settings allow outside collaborators to bypass required code reviews.

**Supported Source Control Managers:**

* GitHub

**Business impact**: Allowing outside collaborators to bypass code reviews weakens a key safeguard against bugs and malicious changes. A compromised external account can push unreviewed code to protected branches. This increases security risk and may result in non-compliance with standards such as SOC 2, PCI DSS, and ISO 27001.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-d5b7b5e62c8588b8f82982836b8629c932925493%2FGit%20posture%20-%20%20Branch%20Protection%20code%20review%20can%20be%20ignored%20by%20Outside%20Collaborator.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="213.926025390625" valign="top">Setting</th><th width="338.370361328125" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Repo Visibility (dropdown)</td><td valign="top">Choose if the policy applies to private, public or all repo types.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Business Priority Less Than</td><td valign="top">Ignore repos with Business Priority less than the number entered.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Choose an Available Fix for a Violation</td><td valign="top">Pick between the options of available fixes for violation.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Branch protection not enforced</mark></summary>

**Purpose:** Detects repositories where branch protection is not configured to require code reviews and restrict direct push events.

**Supported Source Control Managers:**

* GitHub
* GitLab
* BitBucket Cloud

**Business impact:** Without enforced branch protection, code changes can bypass review and approval. Compromised accounts may push malicious or insecure code directly to protected branches. This increases security risk and may result in non-compliance with standards such as SOC 2, PCI DSS, and ISO 27001.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-d460ab185b40faad05e7f4a975bc846b44b95663%2FGit%20posture%20Branch%20Protection%20not%20enforced.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="208.592529296875" valign="top">Setting</th><th width="373.9259033203125" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Repo Visibility<br>(dropdown)</td><td valign="top">Choose if the policy applies to private, public or all repo types.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Business Priority Less Than</td><td valign="top">Ignore repos with Business Priority less than the number entered.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr><tr><td valign="top">Choose developers that can bypass branch code</td><td valign="top">Type in usernames of restricted developers that can bypass branch code reviews.<br><br>Click to add.</td><td valign="top">Current setting</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Branch protection push restriction can be ignored by developer</mark></summary>

**Purpose:** Detects repositories where branch protection settings allow developers to bypass push restrictions on protected branches.

**Supported Source Control Managers:**

* GitHub
* GitLab

**Business impact:** Allowing developers to bypass push restrictions weakens enforcement of code review and approval controls. A compromised developer account can push unreviewed or malicious changes directly to protected branches. This increases security risk and may lead to non-compliance.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-d5b7b5e62c8588b8f82982836b8629c932925493%2FGit%20posture%20-%20%20Branch%20Protection%20code%20review%20can%20be%20ignored%20by%20Outside%20Collaborator%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="214.2222900390625" valign="top">Setting</th><th width="347.25927734375" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Repo Visibility</td><td valign="top">Determines if this policy applies to public repos, private repos or both.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Business Priority Less Than</td><td valign="top">Ignore repos with Business Priority less than the number entered.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Branch protection push restriction can be ignored by outside collaborator</mark></summary>

**Purpose:** Detects repositories where branch protection settings allow outside collaborators to bypass push restrictions on protected branches.

**Supported Source Control Managers:**

* GitHub
* GitLab

**Business impact:** Allowing outside collaborators to bypass push restrictions weakens enforcement of review and approval controls. A compromised external account can push unreviewed or malicious changes to protected branches. This increases security risk and may result in non-compliance with standards such as SOC 2, PCI DSS, and ISO 27001.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-d5b7b5e62c8588b8f82982836b8629c932925493%2FGit%20posture%20-%20%20Branch%20Protection%20code%20review%20can%20be%20ignored%20by%20Outside%20Collaborator%20(2).png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="224.296142578125" valign="top">Setting</th><th width="355.9259033203125" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Repo Visibility</td><td valign="top">Determines if this policy applies to public repos, private repos or both.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Business Priority Less Than</td><td valign="top">Ignore repos with Business Priority less than the number entered.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Branch protection allows unsigned commits</mark></summary>

**Purpose**: Detects repositories with no recent activity that remain unarchived.

**Supported Source Control Managers:**

* GitHub
* GitLab
* Bitbucket Cloud

**Business impact:** Inactive repositories that remain writable increase the risk of unnoticed changes or misuse. Stale code may be reintroduced into builds or deployments without proper context. Archiving unused repositories reduces the attack surface and clarifies that the code is no longer maintained.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-9c1328949ab9f9c5c55f8e41847015db5b3a21e6%2FGit%20posture%20Branch%20Protection%20allows%20unsigned%20commits%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th valign="top">Setting</th><th valign="top">Description</th><th width="149.7747802734375" valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Months Since Change</td><td valign="top">Choose a minimum number of months before a violation could occur</td><td valign="top">Current setting</td></tr><tr><td valign="top">Repo Type<br>(dropdown)</td><td valign="top">Choose if the policy applies to private, public or all repo types.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">CODEOWNERS file missing in repo</mark></summary>

**Purpose**: Detects repositories that do not contain a CODEOWNERS file to define required reviewers.

**Supported Source Control Managers:**

* GitHub
* GitLab
* Azure
* Bitbucket Cloud

**Business impact:** Without a CODEOWNERS file, pull requests may not receive review from appropriate maintainers. Code changes can be approved by users without relevant expertise. This reduces review quality and weakens branch protection effectiveness.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-4313d6d65789dabfccd2399129b1409192482a86%2FGit%20posture%20%20CODEOWNERS%20file%20missing%20in%20repo.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="210.888916015625" valign="top">Setting</th><th width="402.0740966796875" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Repo types applied by the policy (dropdown)</td><td valign="top">Choose if the policy applies to private, public, or all repo types</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr><tr><td valign="top">Branch Protection (Required Reviews)<br>(checkbox)</td><td valign="top">Determine if the policy applies only to repos with branch protection turned on</td><td valign="top">ON</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Developer did not write code in repo</mark></summary>

**Purpose:** Detects users with write access to a repository who have not contributed code to it.

**Supported Source Control Managers:**

* GitHub
* GitLab
* Azure
* Bitbucket Cloud

**Business impact:** Unused write access increases the attack surface for account compromise. A compromised account with write permissions can tamper with code or configurations. Reducing unnecessary access lowers the risk of unauthorized changes.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-c24a0e9c60b40d16eebda192e794cde0763b1b92%2FGit%20posture%20Developer%20did%20not%20write%20code%20in%20repo.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="239.22216796875" valign="top">Setting</th><th width="363.5555419921875" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">External user has access to repo</mark></summary>

**Purpose:** Detects repositories where users outside the organization have ongoing access.

**Supported Source Control Managers:**

* Source Control Managers
* GitHub
* GitLab
* Azure
* Bitbucket Cloud

**Business impact:** External access increases the attack surface for account compromise. A compromised external account can introduce malicious code as part of a supply chain attack. This raises the risk of unauthorized changes and downstream impact on applications that consume the code.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-34848252757fa9ddf904e0021eb3288504b5e763%2FGit%20posture%20external%20user%20has%20access%20to%20repo.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="256.1480712890625" valign="top">Setting</th><th width="318.7037353515625" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">OFF</td></tr><tr><td valign="top">Email Domains (Suffix)</td><td valign="top">Choose the email domains that should have access to the build systems.<br><br>Click to add.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Repo Type (dropdown)</td><td valign="top">Choose if the policy applies to private, public or all repo types.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Git Posture repo wiki publicly editable</mark></summary>

**Purpose:** Detects repositories where the wiki is publicly editable by users outside the repository collaborators.

**Supported Source Control Managers:**

* GitHub

**Business impact:** Publicly editable wikis can be abused to insert malicious links or misleading content. Attackers may direct users to download compromised binaries or artifacts. This increases the risk of malware distribution and supply chain attacks.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-ff3790601c89693fc0cc4a1027cbd2539152d5ec%2FGit%20posture%20Repo%20wiki%20publicly%20editable.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th valign="top">Setting</th><th valign="top">Description</th><th width="115.7008056640625" valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">License file missing in repo</mark></summary>

**Purpose:** Detects repositories where users outside the organization have ongoing access.

**Supported Source Control Managers:**

* GitHub
* GitLab
* Azure
* Bitbucket Cloud

**Business impact:** External access increases the attack surface for account compromise. A compromised external account can introduce malicious code as part of a supply chain attack. This raises the risk of unauthorized changes and downstream impact on applications that consume the code.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-35b63607f59911ee754de8e03a653c1461827d9f%2FGit%20posture%20%20License%20file%20missing%20in%20repo%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="237.6295166015625" valign="top">Setting</th><th width="300.1112060546875" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Repo Visibility (dropdown)</td><td valign="top">Determines if this policy applies to public repos, private repos or both.</td><td valign="top">Current setting</td></tr><tr><td valign="top">License File Name</td><td valign="top"><p>License File names to search for.</p><p><br>Click to add.</p></td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Missing 2FA in organization</mark></summary>

**Purpose:** Detects organizations where two-factor authentication (2FA) is not enforced for user access.

**Supported Source Control Managers:**

* GitHub
* GitLab
* Azure
* Bitbucket Cloud

**Business impact:** Lack of 2FA increases the likelihood of account compromise through credential theft. Compromised accounts may grant attackers access to repositories and administrative functions. This raises the risk of unauthorized changes and large-scale security incidents.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-8193614dba37fecf6bafe764b7df1029a22d22a3%2FGit%20posture%20%20Missing%202FA%20in%20organization.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="217.888916015625" valign="top">Setting</th><th width="353.92578125" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Enforce for (dropdown)</td><td valign="top">Choose what type of users the policy will apply to: Admin, Member, Admin or Member.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Org owner with no admin activity</mark></summary>

Purpose: Detects organization or first-level group owners who retain administrative privileges without recent administrative activity.

Supported Source Control Managers:

* GitHub
* GitLab
* Azure
* BitBucket Cloud

Business impact: Inactive owners retain full control over repositories and user management. Accounts belonging to former employees or unused identities increase the risk of unnoticed compromise. Reducing inactive administrative access lowers the attack surface and limits the potential impact of unauthorized actions.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-0d7a73d3f524bf0d3e47db8b3fd8aab639085e85%2FGit%20posture%20Org%20owner%20with%20no%20admin%20activity.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="230.3704833984375" valign="top">Setting</th><th width="316.888916015625" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Months Since Activity</td><td valign="top">Choose how many months since the last activity will trigger a violation.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr><tr><td valign="top">Audit log access</td><td valign="top">Grant Ox access to your source control platform's audit logs. This enables the detection of admin activity across all repositories. The access is required for Ox to accurately evaluate policies related to administrative functions.</td><td valign="top">Required</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Outside collaborator not using 2FA</mark></summary>

**Purpose**: Detects outside collaborators who have access to repositories without two-factor authentication (2FA) enabled.

**Supported Source Control Managers:**

* GitHub

**Business impact:** Accounts without 2FA are more likely to be compromised through credential theft. A compromised outside collaborator can provide attackers with access to source code and repository functions. This increases the risk of unauthorized changes and supply chain attacks.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-6be76b7b54d1be5b103c8d58e3d8dead70f35d74%2FGit%20posture%20%20Outside%20Collaborator%20not%20using%202FA.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th valign="top">Setting</th><th valign="top">Description</th><th width="99.9918212890625" valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>ON</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Outside collaborator is a repo admin</mark></summary>

**Purpose:** Detects repositories where an outside collaborator is assigned administrator-level permissions.

**Supported Source Control Managers:**

* GitHub
* GitLab

**Business impact:** Outside collaborators are not managed as internal users and their status may change without visibility. Administrative access allows full control over repository settings and code. A compromised external account can enable unauthorized changes and persistent access, increasing supply chain risk.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-9350a9ac49a270ef9a619a229d72a8e6f72ec58f%2FGit%20posture%20Outside%20Collaborator%20is%20a%20repo%20admin.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="230.3704833984375" valign="top">Setting</th><th width="368.74072265625" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Outside collaborator is a repo maintainer</mark></summary>

**Purpose**: Detects repositories where an outside collaborator is assigned maintainer-level permissions.

**Supported Source Control Managers:**

* GitHub
* GitLab

**Business impact:** Outside collaborators are not governed by internal user controls and their status may change without notice. Maintainer access allows elevated control over repository settings and workflows. A compromised external account can introduce unauthorized changes and increase supply chain risk.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-dc0f4dc820b7a7785cc3142f2a529e09624788af%2FGit%20posture%20%20Outside%20Collaborator%20is%20a%20repo%20maintainer.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th valign="top">Setting</th><th valign="top">Description</th><th width="104.589599609375" valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Outside collaborator with no activity</mark></summary>

**Purpose:** Detects outside collaborators who retain access to repositories without recent contribution activity.

**Supported Source Control Managers:**

* GitHub
* GitLab

**Business impact:** Inactive external access increases the risk of unnoticed account compromise. A compromised outside collaborator account can be used to introduce unauthorized changes. Removing unused access reduces the attack surface and limits potential impact.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-2f281f4b603edd4590c5d10b2d50da4e46428566%2FGit%20posture%20Outside%20Collaborator%20with%20no%20activity.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th valign="top">Setting</th><th valign="top">Description</th><th width="143.8489990234375" valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Months Since Activity</td><td valign="top">Choose how many months since the last activity will trigger a violation.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Personal public repo detected</mark></summary>

**Purpose:** Detects public personal repositories owned by organization members.

**Supported Source Control Managers:**

* GitHub
* GitLab
* Azure
* Bitbucket Cloud

**Business impact:** Public personal repositories may expose code copied from private organizational repositories. Sensitive logic or proprietary information can become publicly accessible. This increases the risk of data leakage and intellectual property loss.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-5e4fd91a06e2acf23d1b0c2b423762ee4e88aadc%2FGit%20posture%20Personal%20public%20repo%20detected.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th valign="top">Setting</th><th valign="top">Description</th><th width="144.5897216796875" valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Ignore User Repos Older Than (Months)</td><td valign="top">Ignores mentioning repos older than X Months.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Users to report on</td><td valign="top"><p>Determines the organization users to report on.</p><p>Click to add.</p></td><td valign="top">Current setting</td></tr><tr><td valign="top">Monitor Time for Former Members (Months)</td><td valign="top">Stops evaluating former members who left the company after the selected months ago.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Include Forked Public Repos (checkbox)</td><td valign="top">If the repo is forked (from another public repo by definition), then it is unlikely to contain proprietary data.</td><td valign="top">ON</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Private repo fork detected</mark></summary>

**Purpose:** Detects private personal repositories owned by organization members that may contain code copied or forked from organizational repositories.

**Supported Source Control Managers:**

* GitHub

**Business impact:** Organizational code stored in personal repositories reduces visibility and governance. Sensitive or proprietary code may persist outside approved controls and processes. This increases the risk of data leakage, compliance gaps, and unmanaged code reuse, even without malicious intent.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-aa03c092952d7d0572feef9ffb1eebaf1677ad36%2FGit%20posture%20Private%20repo%20fork%20detected.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="228" valign="top">Setting</th><th valign="top">Description</th><th width="142.1082763671875" valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Ignore User Repos Older Than (Months)</td><td valign="top">Ignores mentioning repos older than X Months.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Users to report on</td><td valign="top"><p>Determines the organization users to report on.</p><p>Click to add.</p></td><td valign="top">Current setting</td></tr><tr><td valign="top">Monitor Time for Former Members (Months)</td><td valign="top">Stops evaluating former members who left the company after the selected months ago</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Private repo forking is enabled</mark></summary>

**Purpose:** Detects organizations or repositories where forking of private repositories is allowed.

**Supported Source Control Managers:**

* GitHub

**Business impact:** Forking private repositories can duplicate proprietary or confidential code outside organizational control. Forks may persist even after access is revoked, reducing visibility and governance. This increases the risk of data leakage and uncontrolled distribution of sensitive code.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-a48ee32a5784705f9aa0f9827effc491f2c08f75%2FGit%20posture%20Private%20repo%20forking%20is%20enabled.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th valign="top">Setting</th><th valign="top">Description</th><th width="137.923095703125" valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr><tr><td valign="top">Ignore Business Priority Less Than</td><td valign="top">Ignore repos with Business Priority less than the number entered.</td><td valign="top">Current setting</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Protected branch can be deleted by a non-admin</mark></summary>

**Purpose:** Detects repositories where protected branches can be deleted by users without administrator privileges.

**Supported Source Control Managers:**

* GitHub
* GitLab
* Bitbucket Cloud

**Business impact:** Allowing non-admin users to delete protected branches increases the risk of accidental or malicious deletion. Loss of critical branches can disrupt development, block deployments, and prevent artifact generation. Recovery may be difficult or impossible, leading to operational impact.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-c39e8973e6a5bb6e27de5b2aca1677a65fb736f2%2FGit%20posture%20%20Protected%20branch%20can%20be%20deleted%20by%20a%20non-admin.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="194.6666259765625" valign="top">Setting</th><th width="388.70361328125" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Repo Visibility (dropdown)</td><td valign="top">Determines if this policy applies to public repos, private repos or both.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Business Priority Less Than</td><td valign="top">Ignore repos with Business Priority less than the number entered.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Public repo detected</mark></summary>

**Purpose:** Detects public personal repositories owned by organization members.

**Supported Source Control Managers:**

* GitHub
* GitLab
* Azure
* Bitbucket Cloud

**Business impact:** Public personal repositories may expose code copied from private organizational repositories. Proprietary logic or sensitive information can become publicly accessible. This increases the risk of data leakage and intellectual property loss.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-5e4fd91a06e2acf23d1b0c2b423762ee4e88aadc%2FGit%20posture%20Personal%20public%20repo%20detected%20(2).png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th valign="top">Setting</th><th valign="top">Description</th><th width="143.1082763671875" valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Ignore User Repos Older Than (Months)</td><td valign="top">Ignores mentioning repos older than X Months.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Users to report on</td><td valign="top"><p>Determines the organization users to report on.</p><p>Click to add.</p></td><td valign="top">Current setting</td></tr><tr><td valign="top">Monitor Time for Former Members (Months)</td><td valign="top">Stops evaluating former members who left the company after the selected months ago</td><td valign="top">Current setting</td></tr><tr><td valign="top">Include Forked Public Repos</td><td valign="top">If the repo is forked (from another public repo by definition), then it is unlikely to contain proprietary data.</td><td valign="top">ON</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Repo admin with no admin activity</mark></summary>

**Purpose:** Detects repository administrators, excluding organization or group owners, who retain admin access without recent administrative or development activity.

**Supported Source Control Managers:**

* GitHub
* GitLab
* Azure
* Bitbucket Cloud

**Business impact:** Inactive administrators retain the ability to delete repositories and manage user access. Accounts belonging to former employees or unused identities increase the risk of unnoticed compromise. Reducing inactive admin access lowers the attack surface and limits the potential impact of unauthorized actions.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-23ee46b7655a347fe65e6544da56502e0dda2739%2FGit%20posture%20%20Repo%20admin%20with%20no%20admin%20activity.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th valign="top">Setting</th><th valign="top">Description</th><th width="148.2933349609375" valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Months Since Activity</td><td valign="top">Choose how many months since the last activity will trigger a violation.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Security policy file missing in repo</mark></summary>

**Purpose:** Detects repositories that do not contain a security policy file.

**Supported Source Control Managers:**

* GitHub
* GitLab
* Azure
* Bitbucket Cloud

**Business impact:** Without a security policy, users may not know how to responsibly report vulnerabilities. This can delay disclosure or lead to public exposure of security issues. For public repositories, missing guidance increases the risk of unmanaged vulnerability handling and reputational damage.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-40c07965b67df1bc880a57c0db9e2bed807c2e84%2FGit%20posture%20Security%20Policy%20file%20missing%20in%20repo.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="210.29638671875" valign="top">Setting</th><th width="367.25927734375" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Repo Visibility (dropdown)</td><td valign="top">Determines if this policy applies to public repos, private repos or both.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Single owner in org</mark></summary>

**Purpose:** Detects organizations or groups that have only one owner account.

**Supported Source Control Managers:**

* GitHub
* GitLab
* Azure
* Bitbucket Cloud

**Business impact:** A single owner creates a single point of failure for administrative access. If the owner account becomes unavailable or compromised, critical management actions may be blocked. This increases operational risk and weakens the resilience of access controls.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-56f89ac51c57f18f52108796e277e783b782aa5c%2FGit%20posture%20Single%20owner%20in%20org.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th valign="top">Setting</th><th valign="top">Description</th><th width="140.145263671875" valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Min Users</td><td valign="top">No issue will be created if the number of users in the org or group is less than or equal to the entered value.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Too many org owners</mark></summary>

**Purpose:** Detects organizations or first-level groups where the number of owners or admins is disproportionately high.

**Supported Source Control Managers:**

* GitHub
* GitLab
* Azure
* Bitbucket Cloud

**Business impact:** Each owner or admin has broad authority over repositories and access controls. A larger set of privileged accounts increases the attack surface and impact of compromise. Reducing the number of owners improves security and limits potential damage from unauthorized actions.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-882e09717184aa71506505621e33c702964e70c9%2FGit%20posture%20Too%20many%20org%20owners.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th valign="top">Setting</th><th valign="top">Description</th><th width="147.5526123046875" valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Max Admins</td><td valign="top">Issue will be created if the number of admins is bigger than the entered value.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Max Admin Percent</td><td valign="top">Issue will be created if the percentage of admins is bigger than the entered value.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Too many repo admins</mark></summary>

**Purpose:** Detects repositories with an excessive number of users assigned administrator privileges.

**Supported Source Control Managers:**

* GitHub
* GitLab
* Azure
* Bitbucket Cloud
* Requires Audit Log Access

**Business impact:** Each repository admin has full control over settings and access management. A higher number of admin accounts increases the likelihood and impact of account compromise. Reducing admin roles limits the attack surface and potential damage from unauthorized actions.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-34ae45bd0395dc7f82a76aea0561d9f407c65896%2FGit%20posture%20Too%20many%20repo%20admins.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th valign="top">Setting</th><th valign="top">Description</th><th width="157.182373046875" valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Max Admins</td><td valign="top">Issue will be created if the number of admins is bigger than the entered value.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Max Admin Percent</td><td valign="top">Issue will be created if the percentage of admins is bigger than the entered value.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Owners</td><td valign="top">Choose if Org/Group owners who by default are repo admins will be ignored.</td><td valign="top">ON</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr><tr><td valign="top">Audit log access</td><td valign="top">Grant Ox access to your source control platform's audit logs. This enables the detection of admin activity across all repositories. The access is required for Ox to accurately evaluate policies related to administrative functions.</td><td valign="top">Required</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Unarchived stale repo</mark></summary>

**Purpose**: Detects repositories with no recent activity that remain unarchived.

**Supported Source Control Managers:**

* GitHub
* GitLab
* Bitbucket Cloud

**Business impact:** Inactive repositories that remain writable increase the risk of unnoticed changes or misuse. Stale code may be reintroduced into builds or deployments without proper context. Archiving unused repositories reduces the attack surface and clarifies that the code is no longer maintained.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-fc3151098df4b9f912a70bc1c2a3fdda0bd9ff2c%2FGit%20posture%20Unarchived%20stale%20repo.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th valign="top">Setting</th><th valign="top">Description</th><th width="149.7747802734375" valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Months Since Change</td><td valign="top">Choose a minimum number of months before a violation could occur</td><td valign="top">Current setting</td></tr><tr><td valign="top">Repo Type<br>(dropdown)</td><td valign="top">Choose if the policy applies to private, public or all repo types.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Unreviewed code change</mark></summary>

**Purpose:** Detects code changes that were merged or pushed without meeting the minimum required number of reviews.

**Supported Source Control Managers:**

* GitHub
* GitLab
* Azure
* Bitbucket Cloud

**Business impact:** Unreviewed changes increase the likelihood of bugs or malicious code reaching production. Lack of review weakens a key control used to detect insecure or unintended changes. This elevates the risk of security incidents and downstream impact.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-46680b84339ee28480e7cc78681942aaca00a039%2FGit%20posture%20%20Unreviewed%20code%20change.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th valign="top">Setting</th><th width="342.0740966796875" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Reviews Required</td><td valign="top">Please specify the minimum number of reviewers per code push for the policy.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Files Changed</td><td valign="top">Specify the minimum number of files changed for the policy.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Older Code Changes (Months)</td><td valign="top">Specify the max number of months to find changes to evaluate</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore File Types</td><td valign="top">Choose the file types that will not trigger a violation.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Business Priority Less Than</td><td valign="top">Ignore repos with Business Priority less than the number entered.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Admins &#x26; Owners</td><td valign="top">An admin will not trigger a violation.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Dominant Language Percentage Min</td><td valign="top">A violation will not occur if dominant language percentage is lower than the value entered.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Veteran developer review required</mark></summary>

**Purpose:** Detects code changes made by infrequent contributors that are not reviewed by a designated veteran developer.

**Supported Source Control Managers:**

* GitHub
* GitLab
* Azure
* Bitbucket Cloud

**Business impact**: Infrequent contributors are more likely to introduce bugs or security vulnerabilities. Without review by an experienced maintainer, risky changes may reach production unnoticed. This increases the likelihood of security issues and unstable code entering critical branches.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-db19095c614cb5ebb22a06974f806e6128d2ea26%2FGit%20posture%20%20Veteran%20developer%20review%20required.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="209.851806640625" valign="top">Setting</th><th width="333.926025390625" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Infrequent Developer (Max Code Changes)</td><td valign="top">Please specify the number of pushes or pull requests that define an infrequent developer (less than).</td><td valign="top">Current setting</td></tr><tr><td valign="top">Veteran Reviewer (Min Reviews)</td><td valign="top">Specify the number of reviews that define a veteran reviewer (greater than or equal to).</td><td valign="top">Current setting</td></tr><tr><td valign="top">Veteran Reviewer (Min Code Pushes)</td><td valign="top">Specify the number of pushes that define a veteran reviewer (greater than or equal to).</td><td valign="top">Current setting</td></tr><tr><td valign="top">Always a Veteran Reviewr</td><td valign="top">Users by name who will always be considered as veteran reviewers in the system.<br><br>Click to add.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Older Code Changes (Months)</td><td valign="top">Specify the max number of months to find changes to evaluate</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Business Priority Less Than</td><td valign="top">Ignore repos with Business Priority less than the number entered.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore File Types</td><td valign="top">Click to add.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Admins &#x26; Owners</td><td valign="top">An admin will not trigger a violation.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

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
