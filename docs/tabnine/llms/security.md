# Source: https://docs.tabnine.com/main/welcome/readme/security.md

# Security

Tabnine provides a secure, reliable, and resilient platform that's been designed from the ground up based on industry best practices.

This article reviews the network and hardware infrastructure, software, and information security that Tabnine includes as part of this platform.

{% hint style="info" %}
View our [Trust Center](https://trust.tabnine.com/) for more information.
{% endhint %}

## **Compliance**

* [SOC2 compliant](https://trust.tabnine.com/)
* [GDPR compliant](https://trust.tabnine.com/)

## Tabnine SaaS datacenters <a href="#data-centers" id="data-centers"></a>

The Tabnine SaaS platform utilizes Amazon Web Services (AWS) and Google Cloud Platform (GCP) to host our cloud-based capabilities. AWS’s main datacenter is located in North Virginia on the East Coast, GCP’s main datacenter is located in Council Bluffs, Iowa, North America, and Heroku’s main datacenter is located in Virginia, United States.

**Datacenters security and compliance**

AWS and GCP design and manage their infrastructure in alignment with the following regulations, standards, and best practices:

* [AWS Cloud Security](https://aws.amazon.com/security/)
* [Google Cloud Security](https://cloud.google.com/security)
* [AWS compliance](https://aws.amazon.com/compliance/programs/), [GCP compliance](https://cloud.google.com/security/compliance/offerings): ISO 27001, 27017, 27018, SOC1/SOC2/SOC3, PCI DSS Level 1, HIPAA, FedRAMP (and more)

**Datacenters architectural physical security**

**Access control:** Physical access is limited only to approved employees and contractors with a legitimate business purpose. Visitors are required to present identification cards and are signed in and escorted by authorized staff. Privileges for employees are revoked immediately when there is no longer a business need for them. Cardholder access to datacenters is reviewed on a quarterly basis.

**Surveillance:** Physical access is controlled both at the perimeter and at building entrance points by professional security staff utilizing video surveillance, intrusion detection systems, and other electronic means.

**Two-factor authentication:** Authorized staff must pass two-factor authentication twice to access dataenter floors.

#### **Environmental protection**

**Redundancy:** The dataenters are designed to anticipate and tolerate failure while maintaining service levels with core applications deployed to an N+1 standard.

**Fire detection and suppression:** Automatic fire detection and suppression equipment have been installed to reduce risk.

**Redundant power:** The datacenter electrical power systems are designed to be fully redundant and maintainable without impact on operations, 24 hours a day, and uninterruptible power supply (UPS) units provide backup power in the event of an electrical failure. Datacenters use generators to provide backup power for the entire facility.

**Climate and temperature controls:** Maintain a constant operating temperature and humidity level for all hardware.

## Tabnine SaaS setup

Tabnine's SaaS deployment includes an end-to-end encryption system to ensure that the communication between our client’s users and our servers remains completely secure.

* **End-to-end encryption:** As the user codes and Tabnine provides suggestions, the data sent from the user's machine to our servers is encrypted using industry-standard encryption algorithms. This ensures that the data can’t be read or tampered with during transit. Likewise, when our servers send back code suggestions to the user's machine, this data is also encrypted. This encryption process ensures that only the user's machine and our servers can decrypt and understand the data, making it secure from eavesdropping or person-in-the-middle attacks.
* **Transport Layer Security (TLS):** We use TLS — a widely adopted security protocol — for securing the communication channel between the client's machine and our servers. TLS ensures that the data is not only encrypted but also that the integrity and authenticity of the data are maintained.
* **No code storage policy (ephemeral processing):** At Tabnine, we recognize the sensitive nature of the codebase. This means that we adhere to a strict policy wherein no code is stored on our servers. The code is only ephemerally processed to provide coding suggestions and is then immediately discarded. This minimizes the risk of any unauthorized access or data breaches concerning your code.
* **Data handling compliance:** In addition to end-to-end encryption, Tabnine complies with various international standards and regulations regarding data handling and privacy. This ensures that our practices are aligned with the best industry standards.
* **Continuous monitoring and audits:** Our security team continuously monitors for vulnerabilities and conducts regular audits to ensure that our security infrastructure is up to the latest standards. This ensures that our customers' data is handled with the utmost care and security.

## Application security <a href="#application-security" id="application-security"></a>

**Software development life cycle:** Software development and change management at Tabnine are performed in a manner that helps ensure applications are properly designed, tested, approved, and aligned to Tabnine’s customers’ business objectives.

Changes are discussed, evaluated, and approved by relevant managers from Product, Development, and DevOps. Changes are documented and approved within an SDLC application. Personnel responsibilities for the design, acquisition, implementation, configuration, modification, and management of systems are assigned. In addition, changes performed to the application are communicated to Tabnine’s customers through release notes.

**Data encryption:** All traffic between the customer client and Tabnine’s Server is encrypted using HTTPS TLS 1.2. Stored data is encrypted on a disk using a 256-bit AES cipher.

**Threat and mitigation analysis:** Tabnine will typically perform a threat and mitigation analysis with security consultants for new products and major changes.

**User identity:** For cloud solutions, Tabnine uses [Google Cloud Identity](https://cloud.google.com/identity) to manage user identity, supporting customers using either strong user/password authentication **or** using provider identity including GitHub, Google, or Microsoft accounts using OAuth2 (user can only choose one of the methods, not both). In the self-hosted solution, built-in user/password authentication is available, as well as support for SAML2 SSO integration.

**Authentication:** All requests from client to server are protected by JWT with an expiration period of 1 hour.

**User permissions:** Tabnine provides two levels of user permissions. A user can be assigned to either "member" or "admin" on the Members page in Tabnine’s web admin application. Admin permission allows control over team membership, payments, and code repository integrations.

**Self-service user management:** Tabnine provides a self-service user management system. The customer’s admins have access to a user management console. There, the team admin can manage users for the account.

**Default password policy:** A user password must be at least six characters long and contain at least one letter and one digit character. Upon password loss, the user can unlock the account by going through the "forgot password" procedure, which allows them to choose a new password after being authenticated through email.

### Enterprise security

Tabnine Enterprise customers Tabnine in a private installation to comply with the strictest enterprise security and privacy policies.
