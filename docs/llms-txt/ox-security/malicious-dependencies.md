# Source: https://docs.ox.security/ox-policies/malicious-dependencies.md

# Malicious Dependencies

> **Note:** This capability is currently in Early Access (EA) and is not generally available. To request access, please contact OX technical support.

The Malicious Dependency policy helps you maintain supply-chain security by ensuring that every component in your SBOM is trustworthy.

It prevents known malicious code from being deployed and protects your environment from hidden threats that live inside third-party libraries.

The policy flags any library or package that is known or suspected to contain malware, backdoors or other malicious code.

When a vulnerable or compromised dependency is referenced in the code, OX Security flags it and creates an issue recommending its removal or replacement before deploying to production.

## Viewing Malicious Dependencies in OX Security

When you select a Malicious Dependencies issue in the SBOM page or the Active Issues page, you can view the information you need to triage and remediate.

**To view Malicious Dependency issues in SBOM:**

* Go to **SBOM** and then from the **Filter** panel, select **Issues > Malicious**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-99f60775456607cc8d4597a51b235ef2e98b2c3a%2FSBOM_Mal_Dep1.png?alt=media" alt=""><figcaption><p>Malicious Dependencies in SBOM</p></figcaption></figure>

* The SBOM Safe column shows that malware was detected in this item.
* The SBOM CVE column displays the number of CVEs identified for this item. Clicking on this number opens the relevant issue in the Active Issues page.

**To open a Malicious Dependency issue:**

* Go to **Active Issues** and then from the Filter panel, select **Policy > Malicious dependency in code**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-e40cc1c5afbc6f98b8b9b4a9f26b2f8730e9df37%2Fissues_mal_dependency_details1.png?alt=media" alt=""><figcaption></figcaption></figure>

Use the following details to understand what was detected, why it received its severity rating, and how to prioritize your response:

* Issue title and policy name showing that Malicious Dependencies triggered this alert.
* Short description identifying the matched malware signature along with the package name, version and source registry.
* Detailed description under More info.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-e5057f25caa2291d28d128e7be45cb3ddfd32dc5%2Fissues_mal_dependency_details_more_info.png?alt=media" alt=""><figcaption></figcaption></figure>

* An ℹ️ icon next to the severity badge.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-576795e87b0dbe7f055b74084ebc772724ac3c14%2Fissues_mal_dependency_details_severity.png?alt=media" alt="" width="294"><figcaption></figcaption></figure>

* Category label indicating the threat category, for example malware or supply-chain risk)

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-20160b9e382b1b5603447364587b3264476f1008%2Fissues_mal_dependency_category.png?alt=media" alt="" width="148"><figcaption></figcaption></figure>

| **Attack Category**                     | **Example and Description**                                        |
| --------------------------------------- | ------------------------------------------------------------------ |
| Typosquatting (Lookalike Packages)      | `crossenv` (malicious) vs. `cross-env` (legit); stole AWS keys     |
| Protestware / Sabotage                  | `node-ipc`, deleted files on systems with Russian/Belarussian IPs  |
| Credential Theft / Exfiltration         | `pymafka`, sent AWS keys to the attacker                           |
| Backdoors / Remote Code Execution (RCE) | `coa`, included malicious payloads to execute remote commands      |
| Postinstall Scripts Abuse               | `loadyaml`, exfiltrated environment variables during `npm install` |
| Dependency Chain Hijacks                | `event-stream`, maintainer handed control to attacker              |

## Disabling the Malicious Dependencies policy

By default, the Malicious Dependencies policy is enabled. You can disable it at any moment.

**To disable Malicious Dependencies:**

1. Go to **Policies > SBOM** and select **Malicious Dependencies** from the list.
2. Click its toggle switch so the status changes to **Off**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-bb529f1ed080f868fce8d1d9fe5223a1a8de993e%2FMal_Dependency_policy_enable.png?alt=media" alt=""><figcaption></figcaption></figure>

1. Confirm the change in the dialog that appears.

After disabling the policy, no new malicious-dependency alerts appear.

### Severity calculation for Malicious Dependencies

When OX Security detects a malicious dependency, it automatically assigns a severity rating that helps you prioritize remediation.

Every flagged malicious dependency starts with a Critical rating by default. This ensures you treat all potential supply-chain threats with high urgency.

OX Security evaluates additional factors and may lower severity when certain conditions apply:

* **Internal repository:** If the package resides in an approved internal registry, the severity may be downgraded.
* **Defanged package:** When a known malicious component has been neutralized, for example, code execution paths removed, the rating can be reduced.
* **No code reference:** If the dependency is present but not actually referenced by your application code, the system may lower its impact rating.

Other factors, such as known mitigations in your environment or custom severity rules may also influence the final rating. These adjustments help you focus on the most urgent issues.

When you enable the Ignore application business priority option, OX Security calculates severity using only those three adjustment factors and the original base severity. That final, adjusted rating appears in the Active Issues page.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-d7b1ce9e90206a5fac0f986fed916612a78e7550%2FMal_Dependency_policy_enable_ignore.png?alt=media" alt=""><figcaption></figcaption></figure>
