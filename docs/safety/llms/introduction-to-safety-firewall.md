# Source: https://docs.safetycli.com/safety-docs/firewall/introduction-to-safety-firewall.md

# Introduction to Safety Firewall

## What is Safety Firewall?

Safety Firewall is a new approach to software supply chain security that *prevents* vulnerable and malicious packages from entering your systems before they can cause harm. Safety Firewall intercepts package installation requests, analyzes them against Safety's comprehensive vulnerability and malicious package database, and either approves, warns about, or blocks installations based on your organization's security policies.

### Key Benefits

* **Prevention-First Security**: Stop threats before they enter your system instead of detecting them after installation
* **Developer-Friendly Protection**: Seamlessly integrates with existing workflows and package managers (pip, poetry, and more)
* **Comprehensive Coverage**: Protects against known vulnerabilities, malicious packages, typosquatting, and other supply chain risks
* **Real-Time Protection**: Analyzes every package installation request as it happens
* **Organizational Visibility**: Provides insights into what packages are being installed, where, and by whom across your organization'

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2FVOdAnu6Z3BwbgfDHqaHa%2FFirewall%20Dashboard.png?alt=media&#x26;token=af5c10e7-d421-4422-aeea-b6a2862e0883" alt=""><figcaption></figcaption></figure>

### How Safety Firewall Works

1. Safety Firewall creates secure aliases for your package managers (pip, poetry, etc.)
2. When a package installation is requested, Safety Firewall intercepts the request.
3. The package is analyzed in real-time against Safety's comprehensive vulnerability and malicious package database.
4. Based on your policies, the package is either approved, flagged with a warning, or blocked.
5. All installation activity is logged to Safety Platform for visibility and audit purposes.

{% hint style="success" %}
Safety Firewall protects not only code projects but also development environments and systems that fall outside of version-controlled codebases. This means even ad-hoc package installations by developers or data scientists are protected.
{% endhint %}

### Who Benefits from Safety Firewall?

* **Security Teams**: Gain confidence that supply chain threats are being prevented, not just detected
* **DevOps Teams**: Ensure consistent security policies across all environments without disrupting workflows
* **Developers**: Stay protected without changing how you work or adding security overhead
* **Compliance Teams**: Generate comprehensive audit logs of all package installations across the organization
