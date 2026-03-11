# Source: https://fivetran.com/docs/security

Title: Fivetran Security Policy

URL Source: https://fivetran.com/docs/security

Markdown Content:
Fivetran is committed to providing a robust security program that protects each customer's information that is used and processed by Fivetran for providing our products and services. The following security documentation describes the administrative, physical, and technical safeguards Fivetran maintains for protecting the security, confidentiality, and integration of Customer Data while connecting, replicating, and loading data from all your data sources. To learn about Fivetran security in detail, see our [security white paper](https://resources.fivetran.com/datasheets/fivetran-security-whitepaper). Any terms that are used but not defined herein shall have the meanings assigned to them in the [Fivetran Master Subscription Agreement](https://www.fivetran.com/legal).

* * *

Deployment options[](https://fivetran.com/docs/security#deploymentoptions)
--------------------------------------------------------------------------

Fivetran offers multiple deployment options so you can choose where your data moves in between the source and destination:

*   [SaaS](https://fivetran.com/docs/deployment-models/saas-deployment): The SaaS model is fully managed in Fivetran's cloud. Depending on your pricing plan, you can choose the [region and data center](https://fivetran.com/docs/privacy#fivetrandataresidency) where you want to host Fivetran in the cloud.
*   [Hybrid](https://fivetran.com/docs/deployment-models/hybrid-deployment): The Hybrid Deployment model allows you to process your data within your own network while leveraging Fivetran's cloud to orchestrate the data movement. It provides a balance for organizations that need to keep their data local for security reasons but still want to benefit from Fivetran's managed service.
*   [Self-Hosted (HVR)](https://fivetran.com/docs/deployment-models/self-hosted-deployment): The Self-Hosted model offers the ability to run Fivetran technology on your own servers. It is designed for organizations that require full control over their data movement and infrastructure.

* * *

Company policies[](https://fivetran.com/docs/security#companypolicies)
----------------------------------------------------------------------

*   Fivetran requires that all employees comply with security policies designed to keep any and all customer information safe, and address multiple security compliance standards, rules and regulations.
*   Two-factor authentication and strong password controls are required for administrative access to systems.
*   Security policies and procedures are documented and reviewed on a regular basis.
*   Current and future development follows industry-standard secure coding guidelines, such as those recommended by OWASP.
*   Networks are strictly segregated according to security level. Modern, restrictive firewalls protect all connections between networks.

* * *

Responsible disclosure policy[](https://fivetran.com/docs/security#responsibledisclosurepolicy)
-----------------------------------------------------------------------------------------------

At Fivetran, we are committed to keeping our systems, data, and product(s) secure. Despite the measures we take, security vulnerabilities will always be possible.

If you believe you’ve found a security vulnerability, please email us at [security@fivetran.com](mailto:security@fivetran.com). Include the following details with your report:

*   Description of the location and potential impact of the vulnerability
*   A detailed description of the steps required to reproduce the vulnerability (POC scripts, screenshots, and compressed screen captures are all helpful to us)

Make a good faith effort to avoid privacy violations as well as destruction, interruption, or segregation of services and/or data.

* * *

Your organization permissions[](https://fivetran.com/docs/security#yourorganizationpermissions)
-----------------------------------------------------------------------------------------------

*   Users can use Single Sign-On with SAML 2.0. See [the list of identity providers](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings/sso#supportedidentityproviders) officially supported by Fivetran.
*   Only users of your organization registered within Fivetran and Fivetran operations staff have access to your organization's Fivetran dashboard.
*   Your organization's Fivetran Dashboard provides visibility into the status of each integration, the aforementioned metadata for each integration, and the ability to pause or delete the integration connection - not organization data.
*   Organization administrators can request that Fivetran revoke an organization member's access at any point; these requests will be honored within 24 hours or less.

* * *

Connections[](https://fivetran.com/docs/security#connections)
-------------------------------------------------------------

*   Connections to customers' database sources and destinations are SSL encrypted by default.
*   Fivetran can support multiple connectivity channels
*   Connections to customers' software-as-a-service (SaaS) tool sources are encrypted through HTTPS.

* * *

Permissions[](https://fivetran.com/docs/security#permissions)
-------------------------------------------------------------

*   **Databases and API cloud applications** - Fivetran only requires READ permissions. For data sources that by default grant permissions beyond read-only, Fivetran will never make use of those permissions.
*   **Destinations** - Fivetran requires the CREATE permission. This permission allows Fivetran to CREATE a schema within your destination, CREATE tables within that schema, and WRITE to those tables. Fivetran is then able to READ only the data it has written.

* * *

Web portal connectivity[](https://fivetran.com/docs/security#webportalconnectivity)
-----------------------------------------------------------------------------------

*   All connections to Fivetran's web portal are encrypted by default using industry-standard cryptographic protocols (TLS 1.2+).
*   Any attempt to connect over an unencrypted channel (HTTP) is redirected to an encrypted channel (HTTPS).
*   To leverage HTTPS, your browser must support encryption protection (all versions of Google Chrome, Firefox, and Safari).

* * *

Solution infrastructure[](https://fivetran.com/docs/security#solutioninfrastructure)
------------------------------------------------------------------------------------

Access to Fivetran production infrastructure is only allowed using hardened bastion hosts, which require an active account protected by MFA (multi-factor authentication) to authenticate. Further access to the environment and enforcement of least privilege is controlled by IAM (identity and access management) policies. Privileged actions taken from bastion host are captured in audit logs for review and anomalous behavior detection.

* * *

Physical and environmental safeguards[](https://fivetran.com/docs/security#physicalandenvironmentalsafeguards)
--------------------------------------------------------------------------------------------------------------

Physical and environmental security is handled entirely by our cloud service providers. Each of our cloud service providers provides an extensive list of compliance and regulatory assurances, including SOC 1/2-3, PCI-DSS, and ISO27001.

### Google[](https://fivetran.com/docs/security#google)

See the [Google Cloud Platform compliance](https://cloud.google.com/security/compliance/), [security](https://cloud.google.com/security/overview/), and [data center security](https://cloud.google.com/security/overview/whitepaper#state-of-the-art_data_centers) documentation for more detailed information.

### Amazon[](https://fivetran.com/docs/security#amazon)

See the [Amazon Web Services compliance](https://aws.amazon.com/compliance/), [security](https://aws.amazon.com/security/), and [data center security](https://aws.amazon.com/compliance/data-center/controls/) documentation for more detailed information.

### Azure[](https://fivetran.com/docs/security#azure)

See the [Azure compliance](https://docs.microsoft.com/en-us/azure/compliance/), [security](https://docs.microsoft.com/en-us/azure/security/), and [data center security](https://docs.microsoft.com/en-us/azure/security/fundamentals/physical-security) documentation for more detailed information.

* * *

Diagnostic data access[](https://fivetran.com/docs/security#diagnosticdataaccess)
---------------------------------------------------------------------------------

Fivetran cannot access your data without your approval.

Depending on your deployment model, we may request access to your data in order to troubleshoot data integrity issues or fix broken connections or destinations. Learn how we troubleshoot for each deployment model type:

*   [SaaS](https://fivetran.com/docs/security#saasdeployment)
*   [Hybrid](https://fivetran.com/docs/security#hybriddeployment)
*   [Self-hosted](https://fivetran.com/docs/security#selfhosteddeployment)
*   [Fivetran Activations](https://fivetran.com/docs/security#fivetranactivations)

### SaaS deployment[](https://fivetran.com/docs/security#saasdeployment)

When working on a support ticket, we may ask you to grant Fivetran access to your data for the next 21 days while we troubleshoot. You can allow or deny data access. If you grant us data access, you can revoke it at any time before the 21-day diagnostic period has expired.

You can monitor your account's diagnostic data access in your Fivetran logs. View your account's access information using two log events, [`diagnostic_access_approved`](https://fivetran.com/docs/logs#diagnosticaccessapproved) and [`diagnostic_access_granted`](https://fivetran.com/docs/logs#diagnosticaccessgranted).

See our [getting support](https://fivetran.com/docs/getting-started/faq#howdoicontactfivetransupport) documentation for more details.

#### Data access options[](https://fivetran.com/docs/security#dataaccessoptions)

You can choose which level of data access to grant Fivetran. The levels of access are as follows:

*   **Source Access** allows a Support Engineer or Connector Engineer to make API requests using the same token that Fivetran uses. We can then see the responses Fivetran receives from the source API during a sync and debug specific issues. With source access, we can also perform mock syncs, which use the same code as true syncs. While we can see each step of the sync to troubleshoot errors, it's not a real sync and so no data is written to the destination.
*   **Destination Access** allows a Support Engineer or Connector Engineer to run SELECT queries using the same read-only permissions granted to the connection database user. We can then validate discrepancies and debug specific issues.
*   **Group Access** grants source access for all connections within the given group, as well as destination access.
*   **Account Access** grants source access for all connections within the account, as well as destination access for all groups.

#### Debugging environments[](https://fivetran.com/docs/security#debuggingenvironments)

We create a unique debugging environment for each troubleshooting case. The debugging environment is created in the region of your data syncs, so it has the same data residency as your normal syncs. We automatically delete the debugging environment and all associated data after seven days.

#### Data access security protocols[](https://fivetran.com/docs/security#dataaccesssecurityprotocols)

We follow multiple security protocols to protect your data while it's in the debugging environment. To connect to the debugging environment, our Support Engineer must authenticate with our company single-sign-on (SSO). The SSO requires multi-factor authentication (MFA), which enforces the use of a one-time passcode and a Fivetran-issued laptop. The laptop is managed by our IT department through mobile device management (MDM) software. Our MDM controls include the following:

*   Full-disk encryption (FDE)
*   MFA authorization through Fivetran's SSO
*   Device firewalls
*   Device's screen locks after 15 minutes of inactivity
*   Anti-malware software

### Hybrid Deployment[](https://fivetran.com/docs/security#hybriddeployment)

Since your connections run in your own environment, Fivetran doesn't have or request access to your data. We collaborate with you to troubleshoot, since only you have access to your data.

### Self-hosted deployment[](https://fivetran.com/docs/security#selfhosteddeployment)

Since your connections run in your own environment, Fivetran doesn't have or request access to your data. We collaborate with you to troubleshoot, since only you have access to your data.

### Fivetran Activations[](https://fivetran.com/docs/security#fivetranactivations)

By using Fivetran Activations, you provide approval for the following limited access: We may view your data within the product user interface solely in the course of troubleshooting to resolve Fivetran Activations errors that you raise to us. This includes observability features in the user interface that show samples of customer data. For example, records that are sent in syncs, and previews of query results from datasets set up by a customer. The visibility of data in Fivetran Activations and what we can access is determined by what permissions you grant in the set up of connected integrations (such as sources and destinations). You can employ additional controls, like designating a column as PII, which will prevent a column with a PII designation from being displayed within the user interface. In most cases, Fivetran Activations data is only stored for the duration of an activation sync, see the [Activations Security & Privacy documentation](https://fivetran.com/docs/activations/misc/security-and-privacy) for more details and exceptions to this policy.

* * *

Certificate Verification[](https://fivetran.com/docs/security#certificateverification)
--------------------------------------------------------------------------------------

Transport Layer Security (TLS, also referred to as Secure Socket Layer, HTTPS, or SSL) is one of the encryption methods that Fivetran uses to secure data in motion. TLS allows for both encryption and authentication of the connections that Fivetran makes to your data sources and to your destinations.

Fivetran connections made over TLS are always encrypted, and support automatic verification for connections that use hostname verification (such as web-based applications), and for proprietary systems with built-in certificate authority management such as Snowflake, BigQuery, and Redshift.

For other connections, such as customer operated databases, we support verifying a certificate using root certificate authority verification.

### Verifying a certificate[](https://fivetran.com/docs/security#verifyingacertificate)

Connections require a user to explicitly select the certificate to use as the trust anchor. Customers who use self-signed certificates for their databases can do the verification based on the fingerprint of the certificate, and customers who use a certificate authority model can select the authority which Fivetran should validate against.

### Auditing trusted certificates[](https://fivetran.com/docs/security#auditingtrustedcertificates)

The account page in your Fivetran dashboard includes a section where your security team can audit all the trust selections that have been made within your Fivetran configuration. You have the option to revoke the trust of a certificate at any time. Once a certificate’s trust has been revoked, you will need to re-run the setup tests for any affected connections to select the new certificate and resume data replication.

Thanks for your feedback!

Was this page helpful?
