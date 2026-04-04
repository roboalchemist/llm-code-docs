# Source: https://docs.getint.io/support-legal-and-others/privacy-and-security.md

# Privacy & Security

### Our Approach to Security and Compliance

At [Getint.io](http://getint.io), we take security and compliance seriously, ensuring that user data is protected and that we meet industry standards. Our certifications reflect this commitment:

* **ISO/IEC 27001:2022**: This is the latest evolution of the gold standard for Information Security Management Systems (ISMS). By migrating to the 2022 standard, we have implemented updated controls addressing modern security challenges, including cloud security, threat intelligence, and information deletion.
* **ISO/IEC 27018:2025**: As one of the early adopters of the 2025 revision, we demonstrate our industry-leading commitment to protecting Personally Identifiable Information (PII) in public clouds.
* **SOC 2 Type II**: Examined between January 13, 2025, and April 12, 2025, confirmed by Prescient Assurance LLC.

#### **Managing Log Retention**

We provide flexible options for storing logs:

* Logs are **kept for 14 days by default**.
* Users can adjust storage from **1 to 14 days** in SaaS environments.
* On-premise and data center deployments allow extended retention upon request.
* Logs can be **fully disabled**, while ticket metadata remains stored.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FtV7nC0FVGRRmnVxNjcVz%2FLogs%20retention%20with%20Getint.png?alt=media&#x26;token=97439ef1-133b-4ba7-b5a5-d0e8e3da9703" alt=""><figcaption></figcaption></figure>

#### **Protecting Data with Encryption**

Security is a priority, so we apply encryption to stored and transmitted data:

* **AES-256 encryption** secures data at rest.
* **SSL/TLS1.2 encryption** ensures safe data transfers.
* Users can enable or disable encryption for logs and sensitive configuration data.

#### **Data Collection and Storage**

To execute synchronizations, Getint processes and stores specific data points. We adhere to the principle of data minimization, only retaining what is necessary for the app to function.

* **Processed Data**: To facilitate synchronizations, the app processes connection details (URL, user email, encrypted personal access tokens) and synchronization configuration profiles.
* **Stored Data**: Because ticket metadata is always retained, all of the following information is kept in the database.
  * **Connection Details**: Site URL, user email, and **encrypted** personal access tokens.
  * **Configuration Profiles**: Field mapping configurations, which may contain user email mappings and specific field values (e.g., priority, severity, issue names, status names, and custom field options).
* **Jira Cloud vs. Data Center**: We only store data for **Jira Cloud** environments. For **Jira Data Center** users, Getint does not store this data within our cloud infrastructure.
* **Retention rules for backups and configurations** after offboarding require CTO approval.

#### **Security in Development and Infrastructure** <a href="#security-in-development-and-infrastructure" id="security-in-development-and-infrastructure"></a>

We follow structured security practices to protect our systems:

* Security scans run **quarterly** to detect vulnerabilities.
* Infrastructure monitoring tools help identify and resolve issues quickly.

#### Security Measures and Ongoing Vigilance <a href="#security-measures-and-ongoing-vigilance" id="security-measures-and-ongoing-vigilance"></a>

We utilize JSON Web Tokens (JWT) for user authentication, in conjunction with Role-Based Access Control (RBAC), ensuring that each user accesses only the resources permitted by their role. This approach helps maintain clarity and security in how access is managed across the platform.

Security is not a one-time setup. It’s something we monitor constantly. That’s why we’ve put a few additional measures in place.

* **Bug Bounty Program**: We invite independent researchers to test our system. If a potential issue is found, we address it quickly. This proactive stance helps us strengthen security in the real world, not just on paper.
* **Cloud Fortified Status**: This designation recognizes our commitment to stability, security, and best practices in cloud operations. It reflects the steps we take every day to protect the platform and the people who rely on it.

These efforts, combined with certifications and established security protocols, are all part of how we keep trust at the core of everything we build.

#### **Controlling Access and Permissions** <a href="#controlling-access-and-permissions" id="controlling-access-and-permissions"></a>

We limit access based on roles and responsibilities:

* **Role-Based Access Control (RBAC)** ensures permissions align with user needs.
* **Quarterly access reviews** keep security policies up to date.
* **Privileged access** is monitored and audited.

#### **Incident Response Plan** <a href="#incident-response-plan" id="incident-response-plan"></a>

We have a clear process for handling security issues:

* The **Incident Response Plan** is tested **annually**.
* Any security or privacy concerns are addressed and communicated promptly.
* No incidents were reported during the **SOC 2 review period**.

#### **Third-Party Security (AWS)** <a href="#third-party-security-aws" id="third-party-security-aws"></a>

AWS provides additional security measures for our data centers:

* Physical access is **strictly controlled** with **CCTV monitoring**.
* Security protocols are reviewed **regularly** to maintain high standards.

#### **Ongoing Security Improvements** <a href="#ongoing-security-improvements" id="ongoing-security-improvements"></a>

We conduct **annual assessments** to evaluate and strengthen security controls. Any issues are quickly addressed, with management actively involved.

Security and compliance are central to our operations, and we remain committed to protecting user data while maintaining transparency in our practices.

#### **Contact Us** <a href="#contact-us" id="contact-us"></a>

If you have questions or need further information about our security and compliance policies, feel free to contact us at our [Support Center](https://getint.io/help-center).

We’re here to assist you and ensure that you have the information you need.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FX3GqOIkUxYW5FQS8LNKU%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=7bb7a965-7fe6-40de-846a-2748399bff4c" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>
