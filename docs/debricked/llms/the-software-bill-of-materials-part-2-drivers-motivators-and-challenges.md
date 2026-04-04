# Source: https://docs.debricked.com/opentext-core-sca-blogs/blogs/the-software-bill-of-materials-part-2-drivers-motivators-and-challenges.md

# The Software Bill of Materials, part 2: drivers, motivators, and challenges

> This blog was published on 13th February, 2023.

SBOMs are not new but have received an increased interest recently. For many organizations, it has gone from being a nice-to-have thing to a must-have. This shift is driven partly by new compliance requirements and, in part, by the cybersecurity threat landscape.

The many actual benefits discussed in part 1, both for suppliers and customers, have been significant drivers for the popularity of SBOMs. Still, working with an SBOM presents a set of challenges to be aware of and to overcome. In this part, we take a more detailed look at the drivers, motivators, and challenges for the usage.

***

Catch up on other posts in our SBOM series:

* The Software Bill of Materials, part 1: benefitting from the SBOM
* The Software Bill of Materials, part 3: The SBOM file
* The Software Bill of Materials, part 4: SBOM with OpenText Core SCA

### Compliance and regulatory requirements&#x20;

New regulations and requirements have appeared from a range of different organizations, governments, and similar. These requirements are in response to the many supply chain attacks that we have witnessed over the last few years. &#x20;

#### Cybersecurity executive order &#x20;

Perhaps the one that is most cited is the [Biden cybersecurity executive order](https://www.whitehouse.gov/briefing-room/presidential-actions/2021/05/12/executive-order-on-improving-the-nations-cybersecurity/) from May 2021. It is noted that the private sector needs to step up the game if they are to provide systems to the U.S. Federal Government. To enhance software supply chain security, the order lists a set of requirements that need to be fulfilled for these suppliers.

One part of the order discusses SBOMs and specifically requires that the purchaser is provided an SBOM together with the purchased software. At the same time, the National Telecommunications and Information Administration (NTIA) was tasked to create a list of the [minimum required elements](https://www.ntia.gov/files/ntia/publications/sbom_minimum_elements_report.pdf) of such an SBOM.&#x20;

#### Proposed DHS law&#x20;

Related is the H.R.4611 – DHS Software Supply Chain Risk Management Act of 2021, which is a proposed law that will require contractors to the Department of Homeland Security (DHS) to submit an SBOM together with a certification that there are no security vulnerabilities in the software. Alternatively, if there are known vulnerabilities, they must provide a list of these. &#x20;

#### The EU Cyber Resilience Act&#x20;

In the EU, there is a proposal for a regulation for cybersecurity requirements, the [Cyber Resilience Act](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:52022PC0454). Regulations are mandatory to follow for all member states. Among other things, the Cyber Resilience Act requires manufacturers to draw up an SBOM. Different from the U.S. regulations, this EU regulation will apply to all manufacturers of products with digital elements that connect to a device or a network. On the other hand, only top-level dependencies need to be included in the SBOM.&#x20;

#### FDA requirement&#x20;

For specific markets, the [FDA is currently pushing](https://www.medtechdive.com/news/fda-seeks-more-power-for-medical-device-cybersecurity-mandates/605107/) for an SBOM to be a mandatory requirement for healthcare products. This is in response to an increased number of cybersecurity incidents in healthcare, as, e.g. [reported by Forbes](https://www.forbes.com/sites/forbestechcouncil/2022/12/20/health-care-cybersecurity-past-present-and-future/?sh=47a7a2b91b64). Moreover, patient data protected by healthcare products are typically very sensitive, and service disruption by these products can jeopardize the life of people.&#x20;

#### Other guidelines&#x20;

In addition, [guidelines from the National Highway Traffic Safety Administration](https://www.nhtsa.gov/sites/nhtsa.gov/files/2022-09/cybersecurity-best-practices-safety-modern-vehicles-2022-tag.pdf) mention SBOM as a means to track vulnerabilities in the vehicle development process. These guidelines are non-binding and voluntary but underline the importance perceived throughout several verticals.&#x20;

### The cybersecurity threat landscape&#x20;

Requirements and legislation will drive the adoption, but these requirements emerge from the actual need in industry and society. The cybersecurity threat landscape is present with or without regulations, and many businesses adopt SBOM practices regardless of external requirements. Let us take a brief look at the cybersecurity threat landscape and how it is developing.&#x20;

#### New vulnerabilities&#x20;

First, the number of vulnerabilities registered as CVEs in the National Vulnerability Database is increasing. In 2017, the number of new vulnerabilities jumped to more than 14 000 after previously never exceeding 8 000 in a year. Since then, the number has steadily increased, and in 2022 it surpassed 25 000.

There are more vulnerabilities if we include the [GitHub Advisory Database](https://github.com/advisories) and those that are language specific, e.g., [FriendsOfPHP](https://github.com/FriendsOfPHP) and the [Python Packaging Advisory Database](https://github.com/pypa/advisory-database), but there are significant overlaps.&#x20;

#### Exploiting vulnerabilities is a common attack vector&#x20;

A known vulnerability can be used as an attack vector in a breach. With many vulnerabilities across a range of applications, there are more opportunities to mount attacks. Surely enough, looking at the top attack vectors as observed by [IBM Security X-Force in the 2022 report](https://www.ibm.com/reports/threat-intelligence/), 34% was due to exploiting vulnerabilities, second only to phishing. Thus, fixing security vulnerabilities must be top-of-mind for organizations relying on software applications in their business.&#x20;

#### Cost of breaches&#x20;

So, clearly, there are not only breaches due to security vulnerabilities, but they are prevalent. Add to this; a breach is very costly. The global average cost of a data breach caused by a vulnerability in third-party components [is estimated to be $4.55 million](https://www.ibm.com/reports/data-breach). If you do not take application security seriously, it is just a matter of time before it happens.&#x20;

In all, it is clear that the cybersecurity threat landscape calls for investing in application security. The alternative is just too costly. With assessing and remediating security vulnerabilities being a top SBOM use case, it is natural to adopt it. &#x20;

### Reliance on software&#x20;

Software is shaping our society, and every day we have become increasingly reliant on software. In the smart city, we try to optimize for sustainability and efficiency through sensors, actuators, databases, communications, and processing.

The data that is collected, processed, and stored will often be sensitive, so we need confidentiality. Also integrity protection is needed to ensure that the data is not modified in transit or at rest. All parts and their functionality are controlled by software.&#x20;

Since software influences how we live and work, the need to have better insights into its inner workings becomes more important. The SBOM can be used to provide at least parts of this insight. &#x20;

### Challenges&#x20;

From the previous discussion, it should be clear that SBOMs are here to stay. But, when generating and working with SBOMs, there are several challenges to consider. It’s not just to generate an SBOM and call it a day. Having an SBOM is not worth much if you cannot, or do not, use it for its intended purposes.

### Completeness&#x20;

Completeness refers to the SBOM including all data that is expected. Looking at the various SBOM formats, there is support for many different entries. A complete SBOM does not have to include all this data. Instead, it does have to cover all software components that it sets out to include. Moreover, if there is information for a component that can be expected to be included, this must be included. &#x20;

#### Missing components&#x20;

If information is missing, e.g., there is an open-source software component that is used but not included in the SBOM, then this poses a risk to the receiving organization. It could mean critical vulnerabilities that can not be listed and assessed. It can also mean that the application uses a component with a non-permissive license in a way that violates the license. In addition to the security and license compliance risks, incomplete SBOMs will reduce the trust in the provider and can delay the time-to-market for an application. &#x20;

#### Missing information&#x20;

The same is true for open-source components that are included, but information about the component is incomplete. In many cases, vulnerability information is written directly in the SBOM. Then, if vulnerability information is only taken from NVD, there will likely be vulnerabilities that are present but not included. &#x20;

#### Known unknowns&#x20;

It can be argued that an incomplete SBOM can be worse than no SBOM at all. If we think the SBOM is complete, we will have a false sense of security, perhaps letting the guard down and not being fully prepared to handle an exploited security vulnerability. With knowledge of a vulnerability, even if it is not patched, other measures can be taken to avoid exploitation and breaches.

To help with “known unknowns,” the common SBOM formats have support for indicating if a dependency relationship is (possibly) incomplete or if all relations have been accounted for.&#x20;

### Up-to-date&#x20;

An SBOM is not a one-off thing. It is a moving target that needs to be kept up-to-date. Having an outdated SBOM comes with the same risks as having an incomplete one, erroneous data. &#x20;

The SBOM can become outdated for different reasons. An application continuously developed and updated will soon have an outdated SBOM. New dependencies will be used, some will be updated to newer versions, while others might be removed.

Any assessments based on outdated SBOMs risk having errors. Vulnerabilities can be missed, while some might already be fixed. The first is a security problem, and the latter gives overhead for developers and security analysts since there will be false positives in the assessment.&#x20;

#### Outdated external data&#x20;

The SBOM can also be outdated in terms of the external data it can provide. In particular, security vulnerabilities are constantly discovered. If the SBOM includes a list of known vulnerabilities, e.g., CVE identifiers, such a list will be outdated as soon as there is a new vulnerability affecting any of the included components.

This should come as no surprise, and looking at the guidelines for how to use the SPDX specification, it is even explicitly stated that “SPDX consumers should always assume vulnerabilities enumerated by an SPDX creator to be out-of-date.” The need for having up-to-date SBOMs makes it important also to include a timestamp. &#x20;

#### Automation and SCA&#x20;

To help generate the SBOM, automation is almost always necessary. There are just too many dependencies in software today, and there is too much information that needs to be collected and to keep up-to-date to do it manually. An automated tool is less error-prone and can generate a full SBOM in a fraction of the time compared to manual processes.&#x20;

Instead of having to constantly update the SBOM due to external changes, an SCA tool can be used to keep track of vulnerabilities, alert you when they arise, and even help you to fix them. This will always provide an up-to-date view of the risks. For developers, by integrating the code repositories with the SCA tool, the view will also update when there are new or updated components.&#x20;

### Actionable&#x20;

The SBOM is useless if the information in it is not used. It cannot do anything on its own, which is why it is crucial that it is actionable. This means that both the content of the SBOM needs to be in a format that can be easily consumed and that its content can be used for the use case it is generated for. It also means that there need to be organizational processes in place to use the SBOM when it is received.&#x20;

#### Targeting the use case&#x20;

An SBOM with only license information could be sufficient if only license compliance is considered, but not if you need to certify that there are no vulnerabilities. If you want to use the SBOM to create an attribution report for your use of open-source software, the license text also needs to be included. It is not enough with the license name.&#x20;

### Conclusion

The current threat landscape with an increasing number of vulnerabilities and attacks should be enough drivers for adopting SBOMs on a wider scale. If that is not enough, the push from regulations and authorities will surely help organizations in the right direction.

However, as we have seen, it is not just to turn a switch and have everything working in two shakes of a lamb’s tail. Some challenges need to be considered for a purposeful deployment.

To help push forward, to have automation, and to have interoperability between organizations, there are a few well-defined formats for encoding the SBOM information. The leading formats, SPDX and CycloneDX, will be described in the next part.
