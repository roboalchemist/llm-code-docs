# Source: https://docs.axonius.com/docs/application-risk-score.md

# Application Risk Level

An application's risk level is an assessment of the application's potential security risks. This helps organizations make informed decisions regarding the application.

A risk level has three values: Low, Medium, and High. On the Asset Graph, the risk level of an application is [indicated by an icon](/docs/viewing-risk-level-for-saas-applications) on the node icon for each application.

The risk is calculated based from a number of parameters which are gathered from public information shared by the application’s vendor and updated on a monthly basis. Parameters include:

* **Product security** - Takes into account whether the application supports SSO, 2FA/MFA enforcement, bug bounty program or the customer’s ability to report security issues. For example, the lack of SSO support increases the risk score.
* **Data security** - Measures the application does or does not take to secure their data, for example, data encryption in transit/at rest. The lack of data encryption increases the risk score.
* **Compliance with relevant industry standards** - Such as SOC2, ISO 27001, PCI DSS, HIPAA or GDPR. Meeting a compliance standard reduces the risk score.
* **Publicly available reports and policies** - Such as privacy policy, user terms, or DPA. Inability to meet various policies increases the risk score of the application.
* **Additional aspects** - The vendor’s geographic location, the number of employees, and other relevant information.

### Example

The following table is for illustration purposes only. In reality, Axonius implements a wider range of parameters to determine the application’s risk level.

| Criteria                   | Application A | Application B |
| -------------------------- | ------------- | ------------- |
| SSO supported              | V             |               |
| MFA supported              | V             |               |
| Data encryption at rest    | V             |               |
| Data encryption in transit | V             | V             |
| SOC2                       | V             |               |
| ISO 27001                  | V             |               |
| Privacy policy             | V             | V             |
| User terms                 |               | V             |
| HQ location                | USA           | USA           |
| Number of employees        | 1000          | 50            |
| **Risk Level**             | **Low**       | **High**      |

You can view the risk levels for various applications on the [SaaS Applications](/docs/saas-applications) page.