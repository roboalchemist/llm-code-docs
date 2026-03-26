# Source: https://docs.socket.dev/docs/license-policy.md

# License Policy

# License Enforcement and Policy Documentation for Socket

At Socket, we believe in the transformative power of open-source software to unlock limitless possibilities for both large enterprises and small businesses. While open-source software drives innovation, it also presents challenges, particularly around security vulnerabilities and license compliance. Managing these risks is especially daunting in large projects with numerous dependencies.

To address these challenges, Socket introduces **License Enforcement**—a major advancement in our mission to provide comprehensive software supply chain security.

<Image border={false} src="https://files.readme.io/40fe7d6bb1b76d562069814cc0ac4ce9ac3115bb002dcb5ce5102b76e6ddb7d1-image.png" />

<br />

***

## Key Features of License Enforcement

### 1. **Comprehensive License Detection**

Socket’s advanced system identifies over 800 license types, providing unmatched coverage. Whether you’re dealing with widely-used licenses or more obscure ones, Socket ensures you're protected with reliable license detection.

### 2. **Detailed Provenance Information**

Understanding the origin of a license violation is critical. Socket provides detailed provenance data, tracing the origin of potential license issues directly to their source. This granular information helps teams make informed decisions about which software components to integrate into their projects.

### 3. **Accuracy You Can Trust**

Socket offers one of the most accurate license detection tools in the industry. By employing a meticulous scanning process, we ensure that no critical compliance issues are overlooked. [Read more about our state-of-the-art license scanner](https://socket.dev/blog/introducing-license-enforcement) to explore its accuracy and capabilities.

### 4. **Pre-Merge Compliance Checks**

Socket’s License Enforcement feature helps prevent non-compliant code from entering your codebase. By detecting potential license violations in Pull Requests (PRs), it ensures that problematic code never gets merged, streamlining the development process while safeguarding your software’s compliance.

***

## License Categories and Actions

Socket categorizes licenses based on their permissiveness, restrictions, and risk, offering flexibility in policy enforcement. These categories include:

### **Permissive Licenses** ✅

* Broadly allow usage, modification, and redistribution with minimal restrictions.
* **Default Action**: Generally allowed by most organizations.
* **Examples**: MIT, Apache 2.0, BSD

### **Weak Copyleft Licenses** ⚠️

* Require changes and additions to the software to be shared under the same license terms but with fewer restrictions than strong copyleft.
* **Default Action**: Organizations may choose to allow or deny based on their compliance requirements.
* **Examples**: LGPL, MPL

### **Strong Copyleft Licenses** ⚠️

* Imposes more restrictions, requiring derived work to be licensed under the same terms.
* **Default Action**: Typically denied by companies working on proprietary software due to its strict sharing requirements.
* **Examples**: GPL, AGPL

### **Lead Category Licenses** ⚠️

* These licenses lack essential elements of permissive licenses or impose unusually burdensome requirements.
* **Default Action**: Often denied to minimize legal and compliance risks.
* **Examples**: Adobe Glyph License, Aladdin Free Public License

***

## License Enforcement Actions

With Socket’s License Enforcement, you can tailor how your organization handles license violations based on its risk tolerance. Actions include:

### **Block 🚫**

* Prevents the merge of any PR introducing a license violation.
* Ideal for high-risk licenses such as **Strong Copyleft** or known non-compliant licenses.
* **Example**: GPL License being blocked in a proprietary software project.

### **Warn ❗**

* Flags potential license violations but allows PRs to proceed.
* Suitable for licenses that might pose moderate risks but don’t require an immediate block.
* **Example**: LGPL flagged as a warning but not blocked for internal tools.

### **Monitor 👁️**

* Tracks license violations without alerting developers or blocking PRs.
* Useful for licenses that require ongoing observation but don’t present immediate risk.
* **Example**: Monitoring permissive licenses that may require further review.

***

## Policy defaults and implicit deny behavior

Socket’s license policy follows a **default-deny model**.

Only licenses that are explicitly configured as **Block**, **Warn**, or **Monitor** are persisted in your policy. Any license not explicitly configured is treated as **Denied** when policy data is evaluated or exported.

### What this means in practice

* If a license is not present in your Allow / Warn / Monitor configuration, it will appear as denied.
* This includes **newly introduced license types** that were not previously detected or configurable.
* These licenses are not explicitly blocked by you—they are implicitly denied because they are unknown to your policy configuration.

### Recommended approach

If you do not intend to deny a license but still want visibility:

* Move it to **Monitor**
* This prevents it from being treated as denied while continuing to track usage

We recommend periodically reviewing your monitored licenses, especially after enabling License Enforcement or when new license types are introduced.

***

## Setting Up License Enforcement

Follow these simple steps to configure and enable **License Enforcement** in your Socket dashboard:

1. **Access License Policy**:
   * Navigate to the **License Policy** page from your Socket dashboard to view and configure your license rules.

2. **Quick Setup**:
   * Use the quick setup to apply default rules based on **Blue Oak Tiers** and common license categories. This is a great starting point for organizations new to managing open-source licenses.

3. **Define Custom Rules**:
   * After the quick setup, you can fine-tune individual licenses by specifying whether to allow or deny specific ones. This is especially useful for organizations with custom compliance needs.

4. **Configure Enforcement Levels**:
   * Customize how strictly you want to enforce the policy:
     * **Block** PRs that violate your organization’s license policy.
     * **Warn** developers through PR comments.
     * **Monitor** license issues without alerting developers or blocking PRs.

<Image border={false} src="https://files.readme.io/dd32b9607624c49b732dd5ef871419fb42134b42623990f9e0179ae3ebf84dc4-image.png" />

<br />

***

## Integration into Existing Workflows

Socket’s **License Enforcement** integrates seamlessly into your development workflows, providing real-time alerts in your GitHub PRs:

* **Alert Generation**: License violation alerts are treated like any other Socket alert. Depending on your organization’s configuration, these alerts can **Block**, **Warn**, or **Monitor** potential issues.
* **GitHub PR Integration**: License violation alerts will appear in GitHub PR comments with detailed provenance data, allowing developers to review and resolve issues in real-time.
* **Allow/Deny List Approach**: Tailor your license policy to your organization’s needs by maintaining a simple allow/deny list.

***

### Example of License Setup in Socket:

<Image align="center" border={false} src="https://files.readme.io/5079ba09dc8a29249b118c96ce2e4ae5b30e999f4c33512144c6416ff94cd8ac-Screenshot_2024-09-30_at_1.32.19_PM.png" />

In this example:

* Permissive Licenses like **MIT** and **Apache 2.0** are allowed.
* Strong Copyleft Licenses like **GPL** are denied due to stricter redistribution rules.
* Licenses like **Lead Category** are set to deny due to burdensome requirements.

***

### Conclusion

The License Policy feature in Socket ensures that you maintain control over the open-source licenses permitted in your codebase, reducing the risk of using non-compliant or restrictive licenses. By setting appropriate actions for each license type, you can enforce your organization's policies and compliance frameworks effectively.

For further details, visit the [Socket Blog on License Policy](https://socket.dev/blog/introducing-license-enforcement).