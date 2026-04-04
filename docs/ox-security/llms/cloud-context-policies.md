# Source: https://docs.ox.security/ox-policies/cloud-context-policies.md

# CI/CD Posture Policies

CI/CD Posture policies detect insecure configurations, integrations, and behaviors within continuous integration and delivery environments. These policies focus on workflows, permissions, webhooks, secrets handling, and tool usage that affect pipeline integrity. Proper CI/CD posture reduces the risk of unauthorized access, supply chain compromise, and insecure code reaching production.

The article describes the policies in this category, configuration options, and the impact of policy violations. For an overview of policies and policy management, see the [Policies](https://docs.ox.security/ox-policies)article.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-c19ce1b842fe0dc739b291dd90f483904c5ba026%2Fcloud%20context%20summary.png?alt=media" alt=""><figcaption></figcaption></figure>

## View and manage CI/CD Posture policies

Open each policy to view the business impact and optional settings.

<details>

<summary><mark style="color:purple;">Anomaly in webhook usage</mark></summary>

**Purpose:** Detects uncommon or anomalous webhook configurations that may indicate unauthorized or persistent access to code repositories.

**Business impact:** Anomalous webhooks can allow long-term unauthorized access after account compromise. They may also expose source code or secrets through unintended data transfer. This increases the risk of data leakage and supply chain compromise.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-4e1f101a7521b9bd9ac75e6a92c931736ebe6c4a%2FCICD%20Posture%20Anomaly%20in%20webhook%20usage.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="228.333251953125" valign="top">Setting</th><th width="300.6666259765625" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Max Repos Process</td><td valign="top">An issue will only be generated if the webhook URL is present in less than the selected percentage of repositories.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Max Repos Count</td><td valign="top">An issue will only be generated if the webhook URL is present in less than the selected count of repositories.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr><tr><td valign="top">Domain Exclusions (dropdown)</td><td valign="top">Webhooks utilizing domains with the specific regex will not generate issues. Select from the list.</td><td valign="top">Current setting</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">CI/CD bot can approve code review</mark></summary>

**Purpose**: Detects repository configurations that allow CI/CD bots to approve code reviews.

**Business impact:** Allowing bots to approve reviews enables self-review bypass of branch protection rules. A single compromised developer account can push unreviewed code to protected branches. This increases the risk of introducing malicious or insecure changes into production.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-a6fcf40eb6e209e117e05072fe9a131bf8b848b2%2FCICD%20Posture%20bot%20can%20approve%20code%20review.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="232.666748046875">Setting</th><th width="344.6666259765625">Description</th><th>Default</th></tr></thead><tbody><tr><td>ON/OFF (toggle)</td><td>Enable/disable the policy.</td><td>ON</td></tr><tr><td>Repos Type (dropdown)</td><td>Choose if the policy applies to private, public, or all repo types.</td><td>Current setting</td></tr><tr><td>Only Enforce with Branch Protection (checkbox)</td><td>If enabled the policy will only be checked for repos with branch protection requiring code reviews</td><td>Current setting</td></tr><tr><td>Ignore Application Business Priority for severity calculation (checkbox)</td><td>When enabled, severity is not adjusted based on application priority.</td><td><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">CI/CD context values in workflow</mark></summary>

**Purpose:** Detects CI/CD workflows that use context values in execution paths without validation.

**Business impact:** Untrusted context values can enable injection of malicious content into workflows. This may lead to unintended command execution or abuse of CI/CD actions and APIs. Such exposure increases the risk of pipeline compromise.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-0cd20e2cb10537e77ffec13b999226399306c1f3%2FCICD%20Posture%20context%20values%20in%20workflow.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
This policy currently applies to GitHub only.
{% endhint %}

<table><thead><tr><th width="230.6666259765625" valign="top">Setting</th><th width="297.3333740234375" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">SCA (dropdown)</td><td valign="top">Select one or more approved SCA applications.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">CI/CD workflow security issue</mark></summary>

**Purpose:** Detects invalid configuration settings and security vulnerabilities within CI/CD workflow files.

**Business impact:** Insecure workflow files can allow unauthorized changes, unintended execution, or abuse of CI/CD capabilities. These weaknesses increase the risk of pipeline compromise and introduction of malicious code. Failure to address them can undermine the integrity of the build and deployment process.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-d47b32d5a6cfc84b608c94105d24f3576cc9ff08%2FCICD%20Posture%20workflow%20security%20issue.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="263.9998779296875" valign="top">Setting</th><th width="282.666748046875" valign="top">Description</th><th valign="top">Defau</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">All (including Info)</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Deprecated command in workflow</mark></summary>

**Purpose:** Detects CI/CD workflows that use deprecated GitHub Actions commands with known security weaknesses.

**Business impact:** Deprecated commands can expose workflows to injection vulnerabilities during execution. Attackers may exploit these weaknesses to manipulate paths or environment variables. Continued use increases the risk of workflow compromise and unintended code execution.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-ea9db8533247b03f7dca306f6687b3631217b984%2FCICD%20Posture%20deprecated%20command%20in%20workflow.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
This policy currently applies to GitHub only.
{% endhint %}

<table><thead><tr><th width="252.6666259765625" valign="top">Setting</th><th width="296.0001220703125" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Repo Visibility</td><td valign="top">Determines if this policy applies to public repos, private repos or both.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Excessive permissions in workflow file</mark></summary>

**Purpose**: Detects CI/CD workflow files that request permissions exceeding what is required for job execution.

**Business impact:** Excessive permissions increase the impact of token exposure during workflow execution. A compromised token can grant attackers broader access to the repository or allow bypass of controls such as required reviews. Limiting permissions reduces the blast radius of credential misuse and pipeline compromise.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-83b975e85f79177684a4b0645bce4cf0790a7ed5%2FCICD%20Posture%20Excessive%20permissions%20in%20workflow%20file.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
This policy currently applies to GitHub only.
{% endhint %}

<table><thead><tr><th width="230.6666259765625" valign="top">Setting</th><th width="297.3333740234375" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Repo Visibility</td><td valign="top">Determines if this policy applies to public repos, private repos or both.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Excessive permissions in workflow setting</mark></summary>

**Purpose:** Detects CI/CD workflows where permission settings grant broader access than required, based on GitHub API configuration data.

**Business impact:** Overly permissive workflow settings increase the impact of token theft or misuse. Compromised tokens may allow attackers to access repositories, secrets, or bypass review requirements. Applying least-privilege permissions limits the potential damage from compromised CI/CD credentials.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-5430208f35ab6eb7222de34433f58280ef2bb100%2FCICD%20Posture%20excessive%20permissions%20in%20workflow%20setting.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
This policy currently applies to GitHub only.
{% endhint %}

<table><thead><tr><th width="230.6666259765625" valign="top">Setting</th><th width="297.3333740234375" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Repo Visibility</td><td valign="top">Determines if this policy applies to public repos, private repos or both.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Incorrect storage of secret in GitHub Action</mark></summary>

**Purpose:** Detects GitHub Actions configurations where sensitive values are stored as variables instead of encrypted secrets.

**Business impact:** Storing secrets in plaintext variables increases the risk of exposure if a runner is compromised. Exposed credentials can be used to access repositories, services, or infrastructure. Proper secret storage reduces the likelihood of credential leakage and unauthorized access.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-42244f211b7faea9f1d14efe13ba88d73790d4af%2FCICD%20Posture%20Incorrect%20storage%20of%20secret%20in%20GitHub%20Action.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
This policy currently applies to GitHub only.
{% endhint %}

<table><thead><tr><th width="230.6666259765625" valign="top">Setting</th><th width="297.3333740234375" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Repo Visibility</td><td valign="top">Determines if this policy applies to public repos, private repos or both.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Malicious webhook</mark></summary>

**Purpose:** Detects webhook URLs with a malicious reputation based on threat intelligence sources.

**Business impact:** Malicious webhooks can provide attackers with continuous visibility into code and environment changes. They may enable data exfiltration or support persistence after a breach. Leaving such webhooks in place increases the risk of ongoing compromise.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-b3a4682178b8cf2aab0ce23dfb7f871171e6b77f%2FCICD%20Posture%20Malicious%20webhook.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="230.6666259765625" valign="top">Setting</th><th width="297.3333740234375" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Secret echoed in workflow console</mark></summary>

**Purpose:** Detects CI/CD workflows that output secret values to logs or console output.

**Business impact:** Exposed secrets in workflow logs can be accessed by users with log visibility or, in public logs, by anyone. Compromised credentials may enable unauthorized access to systems or services. This increases the risk of data breaches and lateral movement.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-69f071c747ae71d8b9dac89b5148665b1abc293f%2FCICD%20Posture%20Secret%20echoed%20in%20workflow%20console.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
This policy currently applies to GitHub only.
{% endhint %}

<table><thead><tr><th width="230.6666259765625" valign="top">Setting</th><th width="297.3333740234375" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">OFF</td></tr><tr><td valign="top">Repo Visibility</td><td valign="top">Determines if this policy applies to public repos, private repos or both.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Show issues of severity (dropdown)</td><td valign="top">Limits which severities appear as issues.</td><td valign="top">All (including Info)</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Suspicious webhook</mark></summary>

**Purpose:** Detects webhook URLs with a suspicious reputation based on threat intelligence sources.

**Business impact:** Suspicious webhooks may indicate early-stage compromise or unauthorized monitoring of repository activity. They can expose information about code changes and environments. Failure to investigate increases the risk of escalation to persistent or malicious access.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-ec3205cc584c9b105cbdf55b4361d479fb2116ab%2FCICD%20Posture%20Suspicious%20webhook.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="230.6666259765625" valign="top">Setting</th><th width="297.3333740234375" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Unauthorized CI/CD used</mark></summary>

**Purpose:** Detects code repositories that are built or deployed using CI/CD systems not approved by the organization.

**Business impact:** Use of unauthorized CI/CD bypasses required guardrails, tests, and security checks. Code changes may reach production without validation. This increases the risk of introducing vulnerabilities or malicious code.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-6520e6086c41c0ceaab3372642f75af32d2e60e2%2FCICD%20Posture%20Unauthorized%20CICD%20used.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="242.6666259765625" valign="top">Setting</th><th width="297.3333740234375" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr><tr><td valign="top">CI/CD</td><td valign="top">Select one or more approved to be used CI/CD tools for this policy.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Business Priority Less Than</td><td valign="top">Ignore repos with a Business Priority that is less than the value entered.</td><td valign="top">Current setting</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Unauthorized serverless function deployment</mark></summary>

> **Note:** This capability is currently in Early Access (EA) and is not generally available. To request access, please contact OX technical support.

**Purpose:** Detects serverless functions that are deployed without using an authorized CI/CD application.

**Business impact:** Unauthorized deployment bypasses required build, test, and security controls. Functions may run with insecure code or misconfigurations. This increases the risk of runtime vulnerabilities and unauthorized behavior in production.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-2c1bf29219215e34405b38c490675e21792b9fdb%2FCICD%20Posture%20Unauthorized%20serverless%20function%20deployment.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="230.6666259765625" valign="top">Setting</th><th width="308" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr><tr><td valign="top">Ignore Business Priority Less Than</td><td valign="top">Ignore repos with a business priority that is less than the value entered.</td><td valign="top">Current setting</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Unpinned (SHA) third-party actions in GitHub</mark></summary>

**Purpose:** Detects GitHub Actions workflows that reference third-party actions without pinning them to a specific commit Service Hash Algorithm (SHA).

**Business impact:** Unpinned actions can change without notice and introduce malicious or insecure behavior. A compromised action may access repository secrets or use the GITHUB\_TOKEN to modify code. This increases the risk of supply chain attacks through CI/CD workflows.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-47c5d7c49cf5299e85c6d8b4a8a4594e85d9ba66%2FCICD%20Posture%20Unpinned%20(SHA)%20Third-Party%20Actions%20in%20GitHub.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
This policy currently applies to GitHub only.
{% endhint %}

<table><thead><tr><th width="237.333251953125" valign="top">Setting</th><th width="307.3333740234375" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Repo Visibility</td><td valign="top">Determine if this policy applies to public repos, private repos or both.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Skip Verified Creators</td><td valign="top">If the repo creator is verified, no violation will occur.</td><td valign="top">ON</td></tr><tr><td valign="top">Exclude Actions Creators</td><td valign="top">When the action creator is excluded, no violation occurs.<br><br>Click to add values.</td><td valign="top">Current setting</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top"><p>OFF</p><p><br></p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Webhook with unknown reputation</mark></summary>

**Purpose:** Detects webhook URLs with an unknown reputation based on threat intelligence sources.

**Business impact:** Webhooks with unknown reputations may indicate unauthorized or unverified integrations. They can expose information about code changes and environments. Failure to validate these webhooks increases the risk of data exposure and persistent access.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-871bcd1658a6090be7a7255f25927a3530bcd992%2FCICD%20Posture%20Webhook%20with%20unknown%20reputation.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="228.333251953125" valign="top">Setting</th><th width="300.6666259765625" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Webhook without secret key</mark></summary>

**Purpose:** Detects webhooks that are configured without a secret key for request validation.

**Business impact:** Webhooks without a secret key cannot verify the authenticity of incoming requests. Attackers may spoof webhook calls to trigger unauthorized actions or extract data. This weakens trust in CI/CD integrations and increases the risk of abuse.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-7dcaf827a021a4c3d324990f91e4676b278ac204%2FCICD%20Posture%20Webhook%20without%20secret%20key.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="264.333251953125" valign="top">Setting</th><th width="322.6666259765625" valign="top">Description</th><th valign="top">Default</th></tr></thead><tbody><tr><td valign="top">ON/OFF (toggle)</td><td valign="top">Enable/disable the policy.</td><td valign="top">ON</td></tr><tr><td valign="top">Ignore Application Business Priority for severity calculation (checkbox)</td><td valign="top">When enabled, severity is not adjusted based on application priority.</td><td valign="top">OFF</td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Webhook without SSL/TLS</mark></summary>

**Purpose:** Detects webhooks that communicate over connections not secured with SSL/TLS.

**Business impact:** Unencrypted webhook traffic can be intercepted or modified in transit. Exposed data may include code or sensitive metadata. This increases the risk of data leakage and man-in-the-middle attacks.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-26729a2c26a0a7c1a8e36b40c509a7da2392a505%2FCICD%20Posture%20Webhook%20without%20SSL%20TLS.png?alt=media" alt=""><figcaption></figcaption></figure>

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
