# Source: https://docs.ox.security/ox-policies/license-policies.md

# License Policies

License policies identify legal and compliance risks in the open-source and third-party components used by your applications. These policies check the license information in your dependencies and highlight packages that do not meet your organization’s security or compliance standards.

The article describes the policies in this category, configuration options, and the impact of policy violations. For an overview of policies and policy management, see the [Policies](https://docs.ox.security/ox-policies)article.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-9dd81619e8926c81ceb36fabd341d39394fa9fb1%2FLicense%20SBOM%20section.png?alt=media" alt=""><figcaption></figcaption></figure>

## What is an approved license

There are two license types:

* **Approved:** These are licenses that you allow in your organization. The licenses are either part of the OX default, or you added them to the organization's approved list of licenses.
* **Not Approved**: The licenses are either not approved as part of the OX default, or you added them to the organization's list of unapproved licenses. When a license is not approved, OX generates a license issue in Active Issues.

> <mark style="color:purple;">IMPORTANT:</mark> OX only classifies licenses that are in the Approved list as approved. Licenses that are **not** in the Approved list are **not approved**.

## View and manage license policies

1. Open the Policies page and select the SBOM category.
2. Select a license policy to view the license details.

<details>

<summary><mark style="color:purple;">Unapproved license used by direct dependency in code</mark></summary>

**Purpose:** Detect direct code dependencies that use licenses not approved by the organization.

**Business impact:** Unapproved licenses can create legal and compliance risk. Certain licenses impose obligations such as source code disclosure or usage restrictions. Non-compliance can result in copyright claims or enforced license terms, as U.S. courts recognize open-source licenses as legally binding.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-f63f0420fc891fd496be4e4aeb6cad9b9002ccfc%2Flicense%20details%20direct%20dependency.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="208.5555419921875" valign="top">Item / Setting</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top">Severity (dropdown)<br>ON/OFF (toggle)</td><td valign="top"><p>Change the severity as needed.</p><p>Enable/disable the policy.</p></td></tr><tr><td valign="top">Policy text</td><td valign="top">A description of the implications for using unauthorized licenses for the policy. The description is also available in the tooltip.</td></tr><tr><td valign="top">Optional features</td><td valign="top"><p>Activate the checkboxes to enable the feature/s.<br></p><p><strong>Generate issue for library with N/A licenses</strong></p><p>When enabled, an issue will be created for libraries that have no licenses.</p><p><strong>Ignore Application Business Priority for severity calculation</strong> When enabled, the severity of an issue is not affected by the Application Business Priority.</p></td></tr><tr><td valign="top">Approved licenses</td><td valign="top"><p>Click to open and view all approved licenses. Scroll as needed.</p><p>The licenses use the standard format SPDX. The list includes the OX default list. Users can add or remove licenses.</p><p><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-d52483ae9afcd4ecffe17816f50ffdb500639a22%2Flicense%20approved%20box.png?alt=media" alt="" data-size="original"></p><p>OX classifies licenses that are <strong>not included</strong> in the Approved list a as <strong>not approved</strong>.</p><p><strong>To add a license:</strong></p><ol><li>Click <strong>Add</strong> and type the exact license name in SPDX format.</li><li>From the page header, click <strong>SAVE</strong>.</li></ol><p><strong>To remove a license:</strong></p><ul><li>Click <strong>X</strong>, then click <strong>SAVE</strong>.</li></ul></td></tr><tr><td valign="top">Unapproved licenses</td><td valign="top"><p>This section gives visibility of licenses that are not approved.</p><p><strong>To add a license:</strong></p><ol><li>Click <strong>Add</strong> and type the exact license name. The name must be in SPDX format.</li><li>From the page header, click <strong>SAVE</strong>.</li></ol><p><strong>To move a license to the Approved list:</strong></p><ol><li>Delete from the Unapproved list and add to the Approved list.</li><li>From the page header, click <strong>SAVE</strong>.</li></ol><p><strong>To remove a license:</strong></p><ul><li>Click <strong>X</strong>, then click <strong>SAVE</strong>.</li></ul></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Unapproved license used by indirect dependency in code</mark></summary>

**Purpose:** Detect transitive (indirect) dependencies that use licenses not approved by the organization.

**Business impact:** Indirect dependencies with unapproved licenses can introduce hidden legal exposure. These licenses may require source disclosure or impose redistribution limits without direct developer awareness. Failure to address them can lead to copyright infringement or enforced compliance actions.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-8c3f138bf5a73f61dc52fc524cbfddf6f3ffb290%2Flicense%20details%20indirect%20dependency.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="204.5555419921875" valign="top">Item / Setting</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top">Severity (dropdown)<br>ON/OFF (toggle)</td><td valign="top"><p>Change the severity as needed.</p><p>Enable/disable the policy.</p></td></tr><tr><td valign="top">Policy text</td><td valign="top">A description of the implications for using unauthorized licenses for the policy. The description is also available in the tooltip.</td></tr><tr><td valign="top">Optional features</td><td valign="top"><p>Activate the checkboxes to enable the feature/s</p><p><strong>Generate issue for library with N/A licenses</strong></p><p>When enabled, an issue will be created for libraries that have no licenses.</p><p><strong>Ignore Application Business Priority for severity calculation</strong> When enabled, the severity of an issue is not affected by the Application Business Priority.</p></td></tr><tr><td valign="top">Approved licenses</td><td valign="top"><p>Click to open and view all approved licenses. Scroll as needed.</p><p>The licenses use the standard format SPDX. The list includes the OX default list. Users can add or remove licenses.</p><p><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-d52483ae9afcd4ecffe17816f50ffdb500639a22%2Flicense%20approved%20box.png?alt=media" alt="" data-size="original"></p><p>OX classifies licenses that are <strong>not included</strong> in the Approved list a as <strong>not approved</strong>.</p><p><strong>To add a license:</strong></p><ol><li>Click <strong>Add</strong> and type the exact license name in SPDX format.</li><li>From the page header, click <strong>SAVE</strong>.</li></ol><p><strong>To remove a license:</strong></p><ul><li>Click <strong>X</strong>, then click <strong>SAVE</strong>.</li></ul></td></tr><tr><td valign="top">Unapproved licenses</td><td valign="top"><p><strong>To add a license:</strong></p><ol><li>Click <strong>Add</strong> and type the exact license name. The name must be in SPDX format.</li><li>From the page header, click <strong>SAVE</strong>.</li></ol><p><strong>To move a license to the Approved list:</strong></p><ol><li>Delete from the Unapproved list and add to the Approved list.</li><li>From the page header, click <strong>SAVE</strong>.</li></ol><p><strong>To remove a license:</strong></p><ul><li>Click <strong>X</strong>, then click <strong>SAVE</strong>.</li></ul></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Unapproved license detected by 3rd party security app</mark></summary>

**Purpose:** Detect third-party components flagged by an integrated security tool as using unapproved licenses.

**Business Impact:** Unapproved licenses can violate internal licensing policies and external legal requirements. They may force code changes, restrict distribution, or trigger contractual disputes. Unresolved violations can result in financial penalties or operational disruption.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-0d68940b2203e6f42c316dcc7548a8d29c118709%2Flicense%20details%203rd%20party%20app.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="197.5555419921875" valign="top">Item / Setting</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top">Severity (dropdown)<br>ON/OFF (toggle)</td><td valign="top"><p>Change the severity as needed.</p><p>Enable/disable the policy.</p></td></tr><tr><td valign="top">Policy text</td><td valign="top">A description of the implications for using unauthorized licenses for the policy. The description is also available in the tooltip.</td></tr><tr><td valign="top">Optional features</td><td valign="top"><p><strong>Ignore Application Business Priority for severity calculation.</strong></p><p>When enabled the severity of an issue will not be affected by the Application Business Priority.</p></td></tr></tbody></table>

</details>

<details>

<summary><mark style="color:purple;">Unapproved license used in forked open source</mark></summary>

> **Note:** This capability is currently in Early Access (EA) and is not generally available. To request access, please contact OX technical support.

**Purpose:** Detect forked open-source components that use licenses not approved by the organization.

**Business impact:** Forked projects with unapproved licenses can introduce compliance gaps if license terms change or differ from the original source. These issues can lead to legal disputes, mandatory remediation, or restrictions on software use and distribution.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-e0fc6343a5198114047b32d43729dd4f6b3c92aa%2FUnapproved%20license%20used%20in%20forked%20open%20source%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="197.5555419921875" valign="top">Item / Setting</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top">Severity (dropdown)<br>ON/OFF (toggle)</td><td valign="top"><p>Change the severity as needed.</p><p>Enable/disable the policy.</p></td></tr><tr><td valign="top">Policy text</td><td valign="top">A description of the implications for using unauthorized licenses for the policy. The description is also available in the tooltip.</td></tr><tr><td valign="top">Optional features</td><td valign="top"><p><strong>Ignore Application Business Priority for severity calculation.</strong></p><p>When enabled, the severity of an issue will not be affected by the Application Business Priority.<br><br><strong>Approved licenses (SPDX format)</strong></p><p>Click <strong>Add</strong> to add additional licenses (case sensitive). Click <strong>X</strong> to remove. Save changes.<br><br><strong>Approved licenses by deployment type</strong></p><p>Use the Enabled checkboxes to apply the setting.<br>Click <strong>Add</strong> to add additional licenses (case sensitive). Click <strong>X</strong> to remove. Save changes.</p></td></tr></tbody></table>

</details>

## View license policy issues

When a license policy detects a nonconformity, OX creates an issue. You can view license-related issues on the Active Issues and SBOM pages.

**To view license issues on the Issues page:**

* Open the Active Issues page and select the relevant Unapproved license option from the Policy filter.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-4d176203439f06015cf713c59c86dee1f1826e97%2Flicense%20filter%20issues%20page.png?alt=media" alt=""><figcaption></figcaption></figure>

**To view license issues in SBOM:**

* Open the SBOM page and select Unapproved Licenses in the Issues filter to view libraries with violations.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-d4fadb8181db77b6b9f35106c06d8e6da1f2006f%2Flicense%20filter%20sbom%20page.png?alt=media" alt=""><figcaption></figcaption></figure>

## Create or save policy profiles

When you change a policy’s severity, ON/OFF toggle or any other setting, you must save the current profile or create a new one.

* To save the current profile, click **SAVE** in the page header.
* To create a new profile, click **SAVE AS** in the page header. For instructions, see the section [Create or edit policy profiles](https://open-2c.gitbook.com/url/preview/site_RHimt/~/revisions/esBak1HVuTgsCEeNbzHE/policies?theme=light#create-or-edit-policy-profiles)in the [Policies](https://docs.ox.security/ox-policies/policies)article.
