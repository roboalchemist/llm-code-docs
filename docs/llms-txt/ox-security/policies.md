# Source: https://docs.ox.security/ox-policies/policies.md

# About Policies

Policies help organizations control risk across the supply chain and enforce security standards. When a policy detects a violation, OX creates an issue and links it to the relevant application, repository, or artifact.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-842214fc9405b504091c9668492c97ac1f469fc4%2Fimage%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

## **Policy categories**

Each policy category focuses on a different area of the organization’s supply chain, such as code, dependencies, pipelines, cloud posture, or artifacts. You can view the categories on the Policies page in the UI.

<table><thead><tr><th width="164" valign="top">Policy Category</th><th width="373.0908203125" valign="top">Description</th><th valign="top">Typical Critical issues</th></tr></thead><tbody><tr><td valign="top"><strong>Git Posture</strong></td><td valign="top">Checks repository configuration, access controls, branch protection rules, exposure settings, and overall repository security posture.</td><td valign="top"><p>Public repo</p><p>Weak branch protection</p></td></tr><tr><td valign="top"><strong>Code Security</strong></td><td valign="top"><p>Evaluates source code using static analysis and pattern detection (SAST).</p><p>Identifies insecure coding patterns and vulnerabilities in source code before the application is built or deployed.</p></td><td valign="top"><p>SAST issues<br>Use of unapproved SaaS in code<br>Code smell detections<br>SQL Injection</p><p>XML External Entity</p></td></tr><tr><td valign="top"><strong>Secret / PII Sca</strong>n</td><td valign="top">Detects exposed secrets, credentials, and personal identifiable information in code, configuration files, and commit history.</td><td valign="top">API key leak<br>Token in history<br><br>Hard-coded secrets</td></tr><tr><td valign="top"><strong>Open Source Security</strong></td><td valign="top">Uses Software Composition Analysis (SCA).<br>Reviews open-source packages for common vulnerabilities and Exposures (CVEs) in open-source dependencies or base images</td><td valign="top">Critical CVEs</td></tr><tr><td valign="top"><strong>SBOM</strong></td><td valign="top">Uses third party libraries with unapproved licensing, low health (i.e., outdated or unpopular libraries) and malicious behavior.<br><br>Validates dependency and artifact metadata, including completeness, accuracy, and licensing compliance across the supply chain.</td><td valign="top">Disallowed license Missing metadata<br>Malicious dependencies</td></tr><tr><td valign="top"><strong>Infrastructure as Code Scan</strong></td><td valign="top">Checks IaC templates (Terraform, CloudFormation, Kubernetes YAML, Helm, etc.) for insecure defaults and misconfigurations.</td><td valign="top">Open security group<br>Weak IAM role</td></tr><tr><td valign="top"><strong>CI/CD Posture</strong></td><td valign="top">Evaluates CI/CD pipeline permissions, runner security, secret handling, and build isolation controls.</td><td valign="top">Insecure runner<br>Poor secret handling</td></tr><tr><td valign="top"><strong>Security Tool Coverage</strong></td><td valign="top">Confirms that required scanning tools and security controls are installed, configured, and active in the environment.</td><td valign="top"><p>Missing scan</p><p>Disabled tool</p></td></tr><tr><td valign="top"><strong>Container Security</strong></td><td valign="top">Analyzes container images for vulnerabilities, embedded secrets, insecure configurations, and unsafe base images.</td><td valign="top">Vulnerable base image Embedded secrets</td></tr><tr><td valign="top"><strong>Dynamic App Security</strong></td><td valign="top">Detects security issues found during runtime testing, including logic flaws, authentication failures, and exposed endpoints.</td><td valign="top"><p>Auth bypass</p><p>Logic flaw</p></td></tr><tr><td valign="top"><strong>API Security</strong></td><td valign="top">Checks API configuration, authentication, authorization, and exposure settings to ensure safe API behavior.</td><td valign="top"><p>Weak authorization</p><p>Exposed endpoints</p></td></tr><tr><td valign="top"><strong>Artifact Integrity</strong></td><td valign="top">Validates that build artifacts are authenticated, untampered, complete, and consistent with expected metadata.</td><td valign="top"><p>Tampered artifact</p><p>Missing signature</p></td></tr><tr><td valign="top"><strong>Cloud Security</strong></td><td valign="top">Evaluates Cloud Asset Posture and Cloud Security Posture (CSPM).</td><td valign="top">Public bucket, exposed access key</td></tr><tr><td valign="top"><strong>Manual Upload</strong></td><td valign="top">Analyzes manually uploaded issue files (CSV/SARIF).</td><td valign="top"><p>Malware indicator</p><p>Invalid metadata</p></td></tr></tbody></table>

## **Policy permissions**

<table><thead><tr><th width="306">Role</th><th width="214" align="center">View</th><th align="center">Edit</th></tr></thead><tbody><tr><td>Admin</td><td align="center"><i class="fa-check">:check:</i></td><td align="center"><i class="fa-check">:check:</i></td></tr><tr><td>Policy Manager</td><td align="center"><i class="fa-check">:check:</i></td><td align="center"><i class="fa-check">:check:</i></td></tr><tr><td>Dev Manager / Security Champion</td><td align="center"><i class="fa-check">:check:</i></td><td align="center"><i class="fa-check">:check:</i></td></tr><tr><td>Developer</td><td align="center"><i class="fa-check">:check:</i></td><td align="center"><i class="fa-check">:check:</i></td></tr><tr><td>Read only</td><td align="center"><i class="fa-check">:check:</i></td><td align="center"><i class="fa-x">:x:</i></td></tr></tbody></table>

## **Edit policy settings**

OX determines the policy severity by default, but you can change the severity or enable / disable the policy if your organization requires it.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-45461f662f0fdc2e685a66860d85afcef5fafbc3%2Fpolicy%20overview%20change%20severity%20or%20toggle%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

**To change policy severity:**

1. Select the severity from the dropdown.
2. To save the change in the current profile, click **SAVE** in the page header.

**To enable or disable a policy:**

1. Use the ON / OFF toggle.
2. To save the change in the current profile, click **SAVE** in the page header.

{% hint style="info" %}
If you want to save the changes **and** create a separate profile, see the section [Create or edit policy profiles](#create-or-edit-policy-profiles).
{% endhint %}

## **Filter policy issues**

1. Open the Active Issues page.
2. Use the **Policy** filter to refine the list by category or specific policy.

## **Create or edit policy profiles**

The Policies page has a default profile. You can create multiple profiles anḍ decide which profile you want to be the active profile. OX backs up the active profile only.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-45461f662f0fdc2e685a66860d85afcef5fafbc3%2Fpolicy%20overview%20change%20severity%20or%20toggle.png?alt=media" alt=""><figcaption></figcaption></figure>

**To save changes to the current profile:**

1. Change either the severity and/or ON/OFF status on one or multiple policies.
2. From the page header, click **SAVE**.

**To create a new profile:**

* From the page header, click **SAVE AS**, name the profile, and choose whether to set it as the active profile.\ <img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-56a91518681038e3b53559b47f72bcd9b2145a5e%2Funknown%20(12)%20(1).png?alt=media" alt="" data-size="original">

**To change the active profile:**

1. From the page header, open the **Select Profile** dropdown and select the profile you want to make active.
2. Activate the checkbox **Set as active profile**. When you return to the Policies page, the new active profile displays.\
   ![](https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-d9e1afadd68c0073e32df07d444fc6cf6330be7d%2Funknown%20\(13\)%20\(1\).png?alt=media)

**To view a non-active profile:**

* Select the profile from the Select Profile dropdown.

## Policy best practices

We recommend you:

* Review issues regularly to identify non-compliant artifacts.
* Enable only the policies your organization needs.
* Adjust the OX policy severity only if you believe that the default severity does not reflect your organization’s risk policy.
