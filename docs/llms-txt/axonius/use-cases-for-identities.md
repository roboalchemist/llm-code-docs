# Source: https://docs.axonius.com/docs/use-cases-for-identities.md

# Use Cases for Identities

The following sections describe just some of the many use cases that can be addressed by Axonius Identities.

### Manage the Identity Lifecycle

Rules can be used to automate the provisioning and de-provisioning of user accounts and access rights based on changes in their identity attributes or roles. For example, a rule could be created to automatically grant a new employee (joiner) access to specific systems and resources based on their job title or department.

When an employee changes roles (mover), rules can be used to update their access rights accordingly, ensuring that they have the necessary permissions for their new position.

Similarly, when an employee leaves the organization (leaver), rules can be used to automatically revoke their access to all systems and resources, preventing security risks and compliance violations.

By automating these tasks, rules can help identity managers save time and reduce the risk of human error. They can also help ensure that employees have the correct access rights at all times, which can improve security and compliance.

See [Rules](/docs/rules-page) and [Workflows](/docs/workflows-overview).

### Streamlining User Onboarding

Optimize the new hire onboarding process by automating key tasks, providing access to essential resources, and facilitating a smooth transition into the organization. This includes automating account provisioning, granting access to systems and applications, assigning mentors, and gathering feedback to ensure a positive and efficient onboarding experience.

See [Workflows](/docs/workflows-overview)

### Simplifying User Offboarding

Streamlines user offboarding processes by automating account deprovisioning and access revocation. This ensures that departing employees' access is promptly removed, minimizing security risks and ensuring compliance. By simplifying offboarding, organizations can enhance operational efficiency, maintain a strong security posture, and protect sensitive data.

See [Workflows](/docs/workflows-overview)

### Enforcing Least Privilege

Leverages peer group analysis to automatically identify and address access outliers, ensuring adherence to the principle of least privilege. By comparing user entitlements against those of their peers, the system detects inconsistencies and recommends adjustments to optimize access rights, minimizing security risks and promoting a robust security posture.

See [Peer Group Simulator](/docs/peer-group-simulator)

### Managing Privileged Access

Securely manage and monitor privileged accounts, preventing abuse and protecting against insider threats.

### Meeting Compliance Requirements

Ensures adherence to regulatory requirements (e.g., SOX, HIPAA, GDPR) by implementing appropriate access controls and audit trails.

### Detecting and Responding to Threats

Identify and respond to suspicious user activity, such as anomalous logins or data access attempts, to prevent security breaches.

### Optimizing Access Certification

Streamline the access certification process, ensuring that access rights are regularly reviewed and validated.

### Improving Operational Efficiency

Free up IT resources by automating identity management tasks, such as user provisioning, de-provisioning, and access reviews.

### Assessing and Mitigating Security Risks

Identify and remediate security vulnerabilities and misconfigurations across your IT environment.

### Machine Identity and Service Account Management

Identify and categorize locally created service accounts using the platform's machine learning engine, which analyzes their attributes and behavior. Manage their lifecycle by assigning owners, approving entitlement changes, and more.

### Assign Owners to Non-Human Identities

Assigning human owners to non-human identities (NHI) is crucial for establishing accountability, ensuring proper security oversight, maintaining compliance, and optimizing operational efficiency. This practice promotes responsible management of automated agents and mitigates potential risks associated with their activities.

Managing non-human identity owners can be done by leveraging [Workflows](/docs/workflows-overview) and create a process to identify newly detected NHIs without an ownership and notify the administrators to assign one. Another use case can be to establish a Workflow that identifies when an owner of a NHI account is leaving the organization (terminated) and assign a new owner instead.

### Stale Groups and Roles

Simplify your identity setup and expedite identity hygiene by finding and removing unused groups and roles. This includes empty groups and roles and those assigned to outdated users.

See the “Identity Hygiene Overview” dashboard.

### MFA Enrollment Tracking

Monitor the type of authentication users are enrolled in (none, weak, or strong), track the progress of the enrollment program, and receive alerts if users manage to circumvent or bypass the organization's policy.

See the “Identity Risk Overview” and the “Identity Hygiene Overview” dashboards. This can also be queried in Managed Identities by using the “MFA Authentication” attributes.

### Managing External Users

Tracking external users is crucial for maintaining security and compliance, as these users often have access to sensitive systems and data. This situation is increasingly prevalent in today's applications due to the widespread use of third-party vendors, contractors, and partners.
Each Managed Identity has an attribute named “Is External” for each of the applications to which Axonius is integrated.

### Password Rotation

Ensuring that passwords are updated regularly helps to mitigate security risks for human and non-human identities.