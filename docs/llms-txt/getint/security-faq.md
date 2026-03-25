# Source: https://docs.getint.io/support-legal-and-others/faq/security-faq.md

# Security FAQ

Welcome to the Security FAQ section for Getint, particularly focusing on our SaaS deployment type, which is the default for Jira Cloud customers. Here, we aim to address common security concerns and standards expectations from our customers regarding data handling, encryption, access, and more.

{% hint style="info" %}
**Alternative Deployment Options**: If our SaaS deployment does not fully meet your security requirements, consider our On-Premise (Self-Hosted) version. This option allows you to run the Getint platform entirely behind your firewall, integrated within your company's infrastructure for enhanced security control.
{% endhint %}

#### **What type of data is transmitted, processed, generated, and/or stored by Getint?**&#x20;

Getint handles only essential data required for integration and synchronization as configured by the customer. This includes item data (issues, tasks, bugs, incidents), comments, user identifiers, encrypted connection details, and URLs to app instances under integration.

#### **Does Getint handle sensitive (personal, health, financial, etc.) data?**&#x20;

Typically, no. Sensitive data is only processed if it is stored in the items being synchronized and explicitly selected for sync by the customer.

#### **How is data encrypted at rest, and how are keys/secrets managed?**&#x20;

Keys and secrets are encrypted and stored securely on Getint-owned hosts. Detailed information on key management is restricted for security reasons.

#### **Who has access to Personally Identifiable Information (PII) or Protected Health Information (PHI) within Getint?**&#x20;

Access to PII or PHI is strictly limited and not applicable under general circumstances, with only Getint company owners having potential access.

#### **Is the code stored in source control, and are clear-text passwords present?**&#x20;

Our source code is managed in GIT via Azure DevOps, with no clear-text passwords stored in the code. Passwords required for application operation are provided at runtime.

#### **What is Getint's data backup strategy?**&#x20;

Getint implements daily backups, which are retained for 30 days, ensuring data resilience and recovery capabilities.

#### **How does Getint ensure the sanitization of backup tapes, failed hard drives, and other storage media?**&#x20;

Our infrastructure relies on AWS, which manages all aspects of backups, hard drives, and VM utilization according to their SLA terms, ensuring proper data sanitization.

#### **How is patching of the software/application implemented in Getint?**&#x20;

Patching follows rigorous testing phases including unit, automatic, UAT testing, and deployment to production, ensuring backward compatibility with a blue/green deployment technique.

#### **How does data get to the application/service, and can external users load it?**&#x20;

Data is provided by the customer through a secured account within the application. Each customer's data is stored in a separate database schema, with no external access for loading/reading data, except for backups.

#### **How does Getint ensure the integrity of data, including input validation and related techniques?**&#x20;

Getint employs standard security techniques provided by the Spring framework for data integrity and input validation.

**Is Getint participating in a Bug Bounty program?**&#x20;

Yes.

#### **Are strong password rules applied, and is multifactor authentication used?**&#x20;

Yes, strong password rules are enforced, with frequent rotation. Multifactor authentication is implemented for internal systems used by Getint company members.

#### **How is the authorization of users managed, and is role-based access used?**&#x20;

We establish direct connections to applications using authentication tokens. For example, when connecting to Jira as an admin, you typically provide the URL, email address, and token. The required credentials vary across platforms. Some use OAuth, others rely on username and password combinations. The specific method depends on what each application supports and what our customers prefer.

#### **Are secure code development practices used to develop the product?**&#x20;

Yes, Getint follows best practices including code reviews, segmented environments, UAT, and smoke testing, among others.

#### **Who is responsible for the maintenance and update of the software?**&#x20;

Getint company members are responsible for the ongoing maintenance and updates of the software.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FOv7nYqlVwMy9NbBCIo4i%2FGetint%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=2f082b7d-3abd-44b8-b4b6-9b092105a04c" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
