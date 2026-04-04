# Source: https://docs.debricked.com/opentext-core-sca-blogs/blogs/comply-with-sbom-requirements-of-the-new-cybersecurity-executive-order.md

# Comply with SBOM requirements of the new Cybersecurity Executive Order

> This blog was published on 29th November, 2022.

With the new cybersecurity executive order, Biden is raising the bar for security in products purchased by the U.S. Government. This includes mandating the need to provide a Software Bill of Materials (SBOM) for all software.

With OpenText Core SCA tool, we help you create an SBOM and keep track of license and security risks in all included open-source components. From both our UI and API’s, you can obtain an SBOM in the CycloneDX format.

### Change is underway

Our society is facing an increased number of cyber attacks. In the light of these attacks, [Biden’s executive order](https://www.federalregister.gov/documents/2021/05/17/2021-10460/improving-the-nations-cybersecurity) on cybersecurity is a welcomed step towards an increased focus on security.

To secure Federal Government computer systems, significant security measures are to be put in place. This includes both cloud-based systems and those that operate on-premise. It also includes both IT and OT systems.&#x20;

The [SolarWinds attack](https://www.businessinsider.com/solarwinds-hack-explained-government-agencies-cyber-security-2020-12) compromised data confidentiality at a number of organizations, including the Department of Homeland Security and Treasury Department. As such, it highlighted the need for higher security in the supply chain. Maybe most importantly, it emphasized this need to the U.S. Government, a government with the capacity to mandate real change.

The executive order from president Biden identifies a wide range of measures, and anyone selling products to the U.S. Government must implement these measures. In effect, any private sector company that has (or wants to have) the government as a customer, must follow the requirements.

One category of requirements is focused on improving software supply chain security. While sophisticated attacks such as the SolarWinds compromise are difficult to protect against, a wide range of security measures will at least raise the bar for the attackers.&#x20;

### The Software Bill of Materials (SBOM)

Commercial software often lacks transparency, and the manufacturers often have insufficient focus on the software’s ability to resist attacks. One defined measure mandates providing a Software Bill of Materials (SBOM) for each product.

The SBOM is a record of the supply chain relationships between components used when building software. The record lists all components in a product, including all open-source software, similar to the list of ingredients given on food packaging.

This is valuable both to those that develop and those that purchase the product. It allows the developers to proactively manage and remediate license risks and security vulnerabilities, and it allows the buyers to verify such risks throughout the product’s life cycle.

### Handling security and license risks

The complexity of managing license and security risks should not be underestimated. Software dependencies very often include their own dependencies, so-called transitive (or indirect) dependencies. These can in turn include further dependencies. For this reason, the SBOM can have hundreds, or thousands, of listed components. Each of these components have its own license and its own security risk from vulnerabilities.

It is clear that the SBOM and the related risks cannot be managed manually for any reasonably sized software. It requires automation, which is also explicitly mentioned in the executive order.&#x20;

The [OpenText Core SCA tool](https://debricked.com/tools/security) automatically creates the SBOM for you. We also identify all licenses and assess your risk level, which is automatically calculated based on how your software is used. What this solution means in the context of SBOM, we recommend you to dive deeper into software composition analysis and ecosystem.

In addition to this, the SBOM information is matched with our vulnerability database in order to identify security vulnerabilities in the software components. With the click of a button, these vulnerabilities can be remediated through an automatically created pull request.

### SBOM export is live

As an [Enterprise](https://debricked.com/pricing) user, you now have the possibility of [exporting the SBOM](https://portal.debricked.com/language-support-49/cyclonedx-sbom-157#what-is-cyclonedx) to the widely used [CycloneDX format](https://cyclonedx.org/). CycloneDX is an open standard for communicating SBOM information. This format has e.g., recently been adopted by OWASP as a flagship project. [Get in touch](mailto:sales@debricked.com) to get started with Debricked today.
