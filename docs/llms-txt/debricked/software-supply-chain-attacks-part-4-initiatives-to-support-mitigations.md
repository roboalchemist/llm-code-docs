# Source: https://docs.debricked.com/opentext-core-sca-blogs/blogs/software-supply-chain-attacks-part-4-initiatives-to-support-mitigations.md

# Software supply chain attacks, part 4: initiatives to support mitigations

> This blog was published on 23rd December, 2021.

There are several practices, tools and techniques that can help secure the software supply chain. We have seen a few already, and here we take a brief look at some emerging initiatives that can help support mitigations. This blog post highlights two SBOM formats, two new approaches to security by design, and three tools for better understanding the health of open-source components.

***

**See our previous posts in our Software Supply Chain attack series:**

* Software supply chain attacks, part 1: defining and understanding the attack
* Software supply chain attacks, part 2: open-source software
* Software supply chain attacks, part 3: role of software composition analysis

### A brief look-back

The focus on supply chain attacks in general, and perhaps software supply chain attacks in particular, has exploded. As discussed in our previous posts, this has good reasons. The attack provides means to amplify the number of targeted machines, users, and organizations. An online search will offer several suggestions for protection mechanisms to consider to avoid being exposed to the attacks. Some mechanisms apply only to the supplier, some target the customer, while others are general mechanisms that apply to all entities in the supply chain.

In part 1 of this series, we summarized some protection mechanisms listed by CSA and NIST. Some are very general, like “use a Secure Software Development Framework,” while others are a bit more specific, like “deliver a Software Bill of Materials (SBOM).” For open-source software, in particular, there are a large number of entry points for an adversary. It is thus clear that there is no silver bullet. Even if a development organization builds a fortress of defense mechanisms, a sloppy or insecure supplier can still render it vulnerable. Still, improving the cybersecurity posture will surely raise the bar for the attackers.&#x20;

In the open-source software environment, we could see that many attack vectors were identified as credential compromise. This is by no means unique to the software supply chain attacks. Again and again, we see stolen passwords as the initial step in an attack. There are enough blog posts discussing password management, both from the user and the service perspective, so we will not go further into those topics. Still, our discussion would be imbalanced without stressing the importance of protecting your accounts. Use good passwords. Use a password manager. Use two-factor authentication whenever possible — so, done.

### Emerging technologies

Now, let us dwell a little deeper into other protection mechanisms, or actually technologies, standards, frameworks, etc., that can help mitigate the software supply chain attacks on different levels. We will diverge from the common “10 things to do”-lists.&#x20;

Not that we have anything against such lists, but adding another one is redundant. They can often be summarized as “know your vendors,” “perform a risk assessment,” “increase developer security awareness,” “patch your systems,” and, of course, as noted above, “protect your account credentials.” Instead, we describe a few specific examples from a wide range of mechanisms, both general and specific. The common denominator is that they are reasonably new and emerging (in one way or the other) and should be seen as things to keep an eye on in the future.&#x20;

### Software Bill of Materials

Greater transparency in the software supply chain is one step towards preventing and responding to attacks in the supply chain. Having a well-defined format for an SBOM will allow software metadata to be efficiently communicated and processed. This will lead to a more accurate inventory of open-source components and help identify risks and assess the security of these components.&#x20;

Transparency of the included components is essential for securing the supply chain. Today, there are two main formats for SBOM, both being continuously developed and improved.

#### SPDX

A software bill of materials (SBOM) is a prerequisite for understanding the third-party software in any product. [SPDX](https://spdx.dev/), short for Software Package Data Exchange, is an open standard for communicating information about the software in a product. It is hosted by the Linux Foundation.&#x20;

The SPDX document includes the component and its version, the component’s license, and security references. Open-source license compliance is the main focus. It has recently been published as an international standard [ISO/IEC 5962:2021](https://www.iso.org/standard/81870.html) by the ISO/IEC JTC 1 standards body.

The SPDX data can be expressed in different file formats, such as XLSX, JSON, XML, and Yaml. In addition to specifying a format, SPDX also provides a [license list](https://spdx.org/licenses/), covering many licenses together with unique identifiers. For example, these identifiers have been adopted by GitHub in their licenses API.&#x20;

#### CycloneDX

Another format for software bill of materials is [CycloneDX](https://cyclonedx.org/). It is an OWASP project with a similar goal as SPDX but designed explicitly for cybersecurity use cases. It builds on SPDX in the sense that it uses the license identifier defined by that standard. It also incorporates support for [CPE identifiers](https://nvd.nist.gov/products/cpe), package URL, and [SWID](https://csrc.nist.gov/projects/Software-Identification-SWID). Both XML and JSON can be used with their digital signature formats. While primarily being an SBOM format, it can also include, e.g., information on hardware components, communication endpoints, and authentication requirements.

Targeting cybersecurity use cases, CycloneDX has support for including vulnerability information in the SBOM. It can also include external references to documentation and security advisories. This will allow the SBOM to be static while updating the external referenced information. The suggested format for security advisories is the [Common Security Advisory Framework (CSAF)](https://oasis-open.github.io/csaf-documentation/) by OASIS.

### Secure by design

Raising the cybersecurity bar through better practices and processes is a general defense. It will increase the resiliency against software supply chain attacks as well as other attacks. This increased resiliency will be evident through fewer vulnerabilities, hardened systems, and better awareness. There are a large number of technologies, guidelines, and frameworks to this end, and here we look at two of the most recent initiatives.

#### Google SLSA

Google has proposed a framework which they denote [SLSA](https://slsa.dev/), short for Supply chain Levels for Software Artifacts. The framework defines a set of practices for ensuring the integrity of software artifacts throughout the supply chain. It particularly targets open-source software, taking into consideration the attack possibilities in each part of the chain. This includes the version control system (VCS) or source code management (SCM), the build system, and the package distribution platform. The attack possibilities for these were previously discussed in detail in our previous blog post.

The integrity refers to both the source integrity, comprising the VCS/SCM, and the build integrity, comprising the build system and the package distribution platform. The requirements defined by SLSA are grouped into Source, Build, Provenance, and Common.&#x20;

The SLSA requirements are incrementally adoptable, divided into four levels. Each level provides increased confidence in the software integrity, i.e., assurance that it has not been tampered with and can be traced back to the source. To give a brief sense of the framework, the levels are roughly defined as follows:

**Level 1, Basic protection**&#x20;

The build process is fully scripted. It also generates (possibly unauthenticated) metadata about how it was built and which dependencies were used. This latter part is the provenance.

**Level 2, Medium protection**&#x20;

Version control is used together with a hosted build service that provides authenticated provenance. The authentication prevents tampering with the provenance, assuming that the build service itself is trusted.

**Level 3, Advanced protection**&#x20;

The source and build platforms meet specific standards. This will guarantee that the source is auditable and the provenance is integrity protected. A third-party auditor is one way to certify that the standards are met.

**Level 4, Maximum protection**&#x20;

This level adds a two-person review of changes and a reproducible build process. It also requires a hermetic build to guarantee that the list of dependencies is complete.

It should be noted that the SLSA level describes integrity protection of the build process and top-level source. It does not take the actual dependencies and how these are built into consideration. There could be a large number of dependencies that themselves have a very low SLSA level, while the software using them has a higher level. In this sense, the levels are not transitive but independent of each other. Still, with SLSA level transparency, the security of a software artifact can be better understood.

#### MITRE D3FEND

In 2021, Mitre introduced its newest framework in the cybersecurity domain, [D3FEND](https://d3fend.mitre.org/). Mitre has been very active and influential in establishing standard languages and formats in the cybersecurity domain. Contributions include, e.g., CVE, CWE, CPE, which together form the foundation for identifying and categorizing vulnerabilities in software and hardware. D3FEND provides a model of cybersecurity countermeasures and their relationships. It is the defensive counterpart of their already established [ATT\&CK](https://attack.mitre.org/) framework which takes a similar approach but focuses on offensive techniques by modeling adversarial behavior.

The most important and central parts of the model are the defense techniques. Each such technique has been carefully phrased in order to capture maximum information. The knowledge graph is divided into three logical levels. At the lowest, most specific level, there are defensive techniques. These are then grouped into base techniques, e.g., application hardening or message analysis. On the highest level, the base techniques are grouped into one of five defense tactics, namely harden, detect, isolate, deceive, and evict.

The D3FEND knowledge base is still at an early stage, and we can expect future addition and modifications. Still, it is an attempt to get a common language for defense techniques similarly as ATT\&CK does for offensive techniques. Better understanding defenses will allow us to create more resilient applications and systems. Though there is much more to be done, D3FENSE is one step in this direction that will likely become widely used soon.

### Package health and overall quality

We see that companies are increasingly open-sourcing some of their in-house developed packages, and the open-source business model has grown significantly over the past few years. Moreover, developers can engage with others in the community and benefit from showing others what they have accomplished.&#x20;

With the increased use of open source across all industries, the number of open-source packages is also increasing. This makes it more challenging to choose the right piece of software to use in your own projects. Imagine choosing between two packets with very similar functionality, not knowing that one of them is far worse when handling security vulnerabilities or is declining in core developer commitment. A risk-based decision needs information about the risks in order to make informed decisions. Well-maintained dependencies are a core requirement for mitigating software supply chain attacks.&#x20;

Let us look at some new and emerging initiatives that aim to help developers and organizations assess, choose and compare open-source software.

#### OpenSSF scorecard

The [Open Source Security Foundation (OpenSSF)](https://openssf.org/) is a member organization under the Linux Foundation. Its members lead several initiatives and projects related to open-source security. One such project is Scorecard. It is a tool that automatically collects information for assessing if a dependency is safe. Some example metrics that are collected are:

* Contributors – whether the project has contributors from at least two different organizations
* SAST – whether the project uses static analysis tools
* Security policy – whether the project contains a security policy, i.e., instruction on how to report security vulnerabilities
* Code-review – whether the project requires code review before merging code
* CI tests – whether the project runs tests in CI

A full list of the metrics can be found on the [project’s GitHub page](https://github.com/ossf/scorecard). Scorecard can be run as a command-line tool, pointing out the Github repo to assess, or by pointing to a package in a package repository, like npm, PyPI, or RubyGems. Results are also collected in a public BigQuery dataset and can be retrieved in JSON format.&#x20;

OpenSSF collects several metrics related to security for dependencies. However, it does not include many non-security-related metrics.

#### CHAOSS

The [Community Health Analytics Open Source Software (CHAOSS)](https://chaoss.community/) project is a Linux Foundation project. It was initiated in 2017 and aims to create analytics and metrics for community health. CHAOSS consists of [a set of working groups, each with a set of focus areas](https://chaoss.community/metrics/). Each focus area defines a set of metrics that can be used to measure specific aspects of an open-source project.&#x20;

Technical metrics include e.g. programming languages used, the number of forks and clones, the time to close issues, and data related to contributors. All these metrics are in the common metrics working group. Metrics in the diversity, equity, and inclusion working group include, e.g., board diversity, documentation accessibility, and chat platform inclusivity. The three other working groups are Evolution, Risk, and Value.

Together, all metrics provide a comprehensive overview and understanding of the open-source software. Some metrics are based on information that can be automatically retrieved, while others must be assessed from interviews with maintainers. CHAOSS defines the actual metrics and also helps point out tools or methodologies that can be used to retrieve data for the metrics. The project also develops software for retrieving the data. However, there is no open source software database with corresponding metrics that can be used to evaluate and compare different OSS components.

#### The OpenText Core SCA Open-source select

We end this post with our own contribution to open source health, namely our [Open Source Select database](https://debricked.com/select/). It is a database with 28 million open-source projects and health metrics for all these OSS projects. It is being actively developed with new metrics being added. Currently, we provide metrics for contributors and popularity. Each metric consists of a set of practices consisting of a group of features.&#x20;

\
For contributors, the practices are experience, efficiency, diversity, activity, and longevity. The final contributor practice is the core team commitment, where the core team is defined as the contributors that can merge pull requests. The features and practices that make up the contributor metric are visualized below. [See our documentation for more details about health.](https://portal.debricked.com/project-health-45)

<figure><img src="https://debricked.com/blog/wp-content/uploads/2021/12/supply-chain-attacks-four-blog-debricked-1024x398.jpg" alt="" height="299" width="768"><figcaption><p>The Contributors metric consists of six practices, each of which consists of a group of features.</p></figcaption></figure>

For project popularity, we measure how much it is used, how highly it is rated, how active the community is, and its ecosystem buzz. Soon we will also add a security metric. The documentation provides further details on the features, practices, and metrics.

The database is open and freely available for anyone to use. It is possible to view metrics for one chosen OSS project and compare different projects in terms of the provided metrics. The database can be used to better understand an OSS component, the community around it and to assess its suitability for being included in a software project as a dependency.&#x20;

The database is also searchable through the software functionality. A search for “web framework” filtered on the pip package manager will provide information and metrics for flask, django, galaxy, tornado, etc. It is also possible to filter on licenses, e.g., only showing projects with MIT, BSD, or Apache licenses.

### Conclusion

This post provides just a few examples of emerging technologies and initiatives that can help secure the software supply chain. However, the limiting factor is not the lack of tools and knowledge but to get these things right in the organization or development process.&#x20;

We protection against all vulnerabilities in all parts of the software supply chain. At the same time, the adversary only needs to find one weakness to exploit in any part of the supply chain. This asymmetry has been plaguing security for a long time, and there is no quick fix. However, a structured and consistent approach to securing our software, taking advantage of existing knowledge is a good step in the right direction.

Another step in the right direction is having tooling in place that will help you stay ahead of attackers. OpenText Core SCA is a [software composition analysis tool](https://debricked.com/tools/security) that helps you not only know what’s in your code, but also prevent vulnerabilities from entering. [Read more and create a free account today here](https://debricked.com/tools/security).
