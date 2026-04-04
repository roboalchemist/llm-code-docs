# Source: https://docs.debricked.com/opentext-core-sca-blogs/blogs/the-software-bill-of-materials-part-3-sbom-file.md

# The Software Bill of Materials, part 3: SBOM file

> This blog was published on 21st February, 2023.

There are a few different formats for storing and encoding SBOM information. The most well-known targeting supply chain transparency is the SPDX and the CycloneDX formats.

In this post, we take a deeper dive into these formats and provide a comparison between them. We also briefly discuss the SWID tags, which can also be used for SBOM information, but has a somewhat different target use case.

***

Catch up on other posts in our SBOM series:

* The Software Bill of Materials, part 1: benefitting from the SBOM
* The Software Bill of Materials, part 2: drivers, motivators, and challenges
* The Software Bill of Materials, part 4: SBOM with OpenText Core SCA

### NTIA minimum elements&#x20;

The Cybersecurity Executive Order instructed (among others) the National Telecommunications and Information Administration (NTIA) to publish a set of [minimum elements for an SBOM](https://www.ntia.gov/files/ntia/publications/sbom_minimum_elements_report.pdf). These elements are divided into three categories.&#x20;

* Data fields&#x20;
* Automation support&#x20;
* Practices and processes&#x20;

Let us discuss these categories in a little more detail.&#x20;

#### Data fields&#x20;

The data fields define what data an SBOM should include. This is the minimum amount of information required for each component, as well as metadata for the SBOM file itself. Seven data fields are defined. These are the *supplier* of a component, the *component name*, its *version*, *other unique identifiers*, the *relationship between the dependencies*, i.e., which upstream components are used by a component, the *author of the SBOM*, and a *timestamp*.&#x20;

In particular, having other unique identifiers will allow the component information to be mapped to known vulnerabilities and licenses. Such mappings assume that the component is not confused with other components of a similar name. The main unique identifiers are CPE, PURL, and SWID.&#x20;

#### Automation support&#x20;

The vast number of components, and their relations, require tools support for both reading and generating the SBOM. Automation and tools support will also ensure interoperability between organizations. Since SBOMs will often be provided from a supplier to a purchaser/consumer, such interoperability is crucial for its usage.&#x20;

While automation requires a machine-readable format, the SBOM should also be human-readable. This will help with manual troubleshooting and a quick overview of certain specific data in the SBOM. To support these requirements, NTIA mandates using one of the SPDX, CycloneDX, or SWID data formats for an SBOM. This list might be expanded in the future, but proprietary formats should be explicitly avoided.&#x20;

#### Practices and processes&#x20;

NTIA defines several minimum requirements for the processes surrounding the creation and management of SBOMs. &#x20;

Related to the frequency of generating an SBOM, it must be generated every time there is a new software release.  &#x20;

The dependencies used in software can be seen as a tree hierarchy, with the direct dependencies at the top and the upstream transitive dependencies below. At a bare minimum, the SBOM must include all top-level direct dependencies. These should be provided with enough detail so that it is possible to find the transitive dependencies. Additionally, it must be clear if there are no further transitive dependencies or if the presence of such dependencies is unknown.&#x20;

NTIA also highlights the importance of starting with generating and providing SBOMs as soon as possible. This includes accepting that an SBOM can have some initial errors and omissions, but instead of waiting for perfection, SBOM practices should start today.&#x20;

### Two main formats: SPDX and CycloneDX &#x20;

There are two main formats for SBOMs that are widely used and accepted. SPDX is maintained and supported by the Linux Foundation, while CycloneDX is maintained and supported by OWASP.&#x20;

Let us briefly look at the SPDX and CycloneDX files to get a feeling for the information they can contain. Both formats have support for much more data than given here, and we refer to the respective specifications for details. The information provided here is based on SPDX v2.3 and CycloneDX v1.4.&#x20;

### Inside the SPDX SBOM file&#x20;

An [SPDX SBOM](https://spdx.dev/specifications/) consists of a set of sections. The first part, which is mandatory, is the meta-information about the SPDX file. This is called the Document Creation Information. This includes, e.g., when the SBOM was created, which tool was used to create it, which SPDX version it is based on, and other SPDX documents that are referred to in this document.&#x20;

#### Package information

Then there are sections for each of the packages. Each package includes basic information on its name, version, and download location. There is also a unique identifier to be used within the SPDX document to reference other information.

The package section also includes license information, and if different files within the package have different licenses, then the complete list of all found licenses within the package can be listed. The package section in SPDX also has support for free text comments on licenses, copyright text, and other types of free text comments on the package in general.

#### Security information in external references&#x20;

An important field is the one for *external references*. This field can be used to refer to an external source for more information about the package.

One defined category for external information is security, which can be used to link to advisories, fixes, or URLs with security-related information. The advisory can include links to CVEs, the vendor’s vulnerability disclosure document, or even security information formatted in a CycloneDX SBOM file.

#### Files and snippets&#x20;

Following information about a package, it is also possible to add information about specific files inside a package. Such information is given in a separate section after the corresponding package section. Further details can be given in yet another section referring to specific snippets inside a file. These snippets can be referenced by byte ranges or line numbers and can have licenses that are different from the rest of the file or from the package.&#x20;

#### Describing the dependency graph&#x20;

In the package, file, and snippet sections, the data given in each element is independent of the others. The relationship between a package and its files is implicit in that the files section follows the corresponding package section. But there can also be relationships between files and, maybe more importantly, relationships between packages. One package typically depends on another package, and there are transitive dependencies such that one package will depend on a package that, in turn, depends on a third package, etc.&#x20;

These relations between components are described in their own section. The relationship can be one of many but “depends on” and “dependency of” are useful for describing the dependency graph for the software.&#x20;

The relation can also be marked to indicate that a part of the graph might be incomplete or that the creator assures that it is complete.

### Inside the CycloneDX SBOM file&#x20;

Similar to SPDX, [CycloneDX](https://cyclonedx.org/docs/1.4/json/) starts with identification information and metadata. This specifies that it is a CycloneDX SBOM, which specification version it conforms to, and the SBOM version for that particular software. Then there is, e.g., a timestamp and an identifier for the tool used to generate the SBOM (or the author if it was manually generated).

#### Components&#x20;

Following the metadata, the components are described. The component type is defined as, e.g., file, container, library, or application. Some notable component information includes the component’s type, name, and version.

To make it uniquely identifiable, it can also include one or several of the CPE, PURL or SWID identifiers. This will allow the SBOM file to be used to identify and monitor new vulnerabilities in the software. The component information will also include license information. It will hold the license ID but can also include the license text itself or a URL pointing to the license file. Each component can also include a bom-ref identifier which can be used to reference the component in other parts of the SBOM.

#### Services&#x20;

Separate from components, it is also possible to list services, e.g., microservices. The SBOM can then be used to define if using a service crosses a trust boundary if it requires authentication and specific API endpoints for a service. &#x20;

#### External components&#x20;

CycloneDX has also support for adding external references. These can be either declared as part of a specific component or be defined outside the components part of the SBOM. External references are added in the form of URLs to the information.

#### Describing the dependency graph&#x20;

The relationship between dependencies is documented in a separate part. It is here possible to refer to a component using the bom-ref attribute and to declare which other components it directly depends on. Doing this for all components will provide a dependency graph of the software that represents both direct and transitive relationships between dependencies.

#### Compositions and assemblies&#x20;

CycloneDX has also support for describing compositions, which is a collection of components, services, and dependency relationships. A composition can describe an assembly which can be seen as a well-defined part of the software or application that, in turn, can include other parts in a nested fashion. The composition can also be described with dependencies, which are parts of the software that requires other independent parts.

#### Vulnerabilities&#x20;

Vulnerabilities are described explicitly in a separate part of the CycloneDX SBOM. A vulnerability description refers to the bom-ref of the affected component and can include several pieces of information. This includes the vulnerability ID, the publisher, references, the CWE identifier, CVSS information, a description of the vulnerability, advisory information, timestamps, etc.

It is also possible to include analysis details for the vulnerability, e.g., describing it as resolved, exploitable, in triage, or not affecting the component or service, including a justification for this assessment.

#### Signing data&#x20;

Finally, the complete SBOM can also be signed using a JSON-formatted digital signature, including the public verification key and a certificate path. In addition to signing the SBOM, individual parts, such as components, services, and compositions, can also be individually signed.

### Comparing SPDX and CycloneDX&#x20;

SPDX and CycloneDX share the support for the main use cases in that both licensing information and vulnerability information is supported. However, they differ in the extent of the support. Looking at the specifications, it is clear that SPDX leans more heavily towards the licensing use case, while CycloneDX has more support for vulnerability information. &#x20;

#### License information support&#x20;

As an example for license information, SPDX adds a specific field for “concluded license,” which can be used if the license can not be determined or if there has been no attempt to find it. It also has a field for collecting all licenses in the files of a package and adding comments to the licenses.

The snippet information section also has its own fields for license information. Such a level of granularity, down to specifying snippets of files, is not supported by the CycloneDX specification. As part of the SPDX specification, there is also the SPDX license list. This list provides a standardized short identifier for all commonly found licenses. This identifier is becoming an industry standard for identifying licenses and is also used by CycloneDX SBOMs.

#### Security and vulnerability information support&#x20;

Looking at security, CycloneDX defines a large number of fields related to vulnerabilities, their metadata, assessment, and the actions taken for them. This data is not explicitly supported by SPDX, though it is possible to use external references to include some security data.&#x20;

Another security-related difference is the support for digital signatures in the CycloneDX SBOM. Both the SBOM and parts of the data inside it can be digitally signed in order to provide data authentication and non-repudiation for the data. It is, of course, also possible to digitally sign an SPDX document. Still, it has no support for enveloped signatures, as is the case for CycloneDX, i.e., the signature is part of the signed document.

#### Encoding of data&#x20;

Both SPDX and CycloneDX support JSON formatted data, while SPDX additionally supports YAML, RDF, a tag: value text file, and XLS spreadsheets. CycloneDX has XML support, while SPDX is looking to add this support in the next release.

### Software Identification (SWID) Tags&#x20;

As noted above, NTIA also includes the possibility of using Software Identification (SWID) Tags as an SBOM format. [A SWID tag](https://csrc.nist.gov/projects/software-identification-swid/guidelines) can include the information needed for transparency in the open source software supply chain, but its main use case is somewhat different. A SWID tag is designed for tracking installed software throughout the lifecycle. Here, throughout the lifecycle is supported by defining different types of tags for pre-installed and installed software, as well as patch tags, to define patches to software and supplemental tags for additional information.

The XML-formatted SWID tag will include information about the software, its license, and the files needed to install the software. It can also include information on what other packages are needed as a prerequisite for installation. This will allow for the automated installation of software and for monitoring what software is installed in a system, which version it has, and which patches have been installed.

#### Four variants of SWID tags&#x20;

The *corpus tag* is used pre-installation and is used by the software installer. They can authenticate the issuer and be used to verify the integrity of the software. License information can be used to make sure that no license is violated before the software is installed.&#x20;

The *primary tag* is used to describe software that has been installed. It has a globally unique tag ID to make it possible to track that particular installation. It can also link to other SWID tags. Such a link can be defined as a component if other software is a component of the software. It can also be defined with a required attribute if it depends on another software component. A simple example is a productivity suite that has a word processor and a spreadsheet processor as components. Both these will, in turn, have some common libraries and functionalities as required.

The *patch tag* describes a patch rather than the software product itself. It includes information about which product the patch is for, if other patches need to be applied before this patch, or if it replaces another patch.&#x20;

The *supplemental tag* can be used by the local system to provide additional information. This could be, e.g., the time of installation.&#x20;

#### Tags are tied to installed software&#x20;

SWID tags are designed to be removed once the installed software is uninstalled and removed from the system. This shows the close relationship that the SWID tags have with the installed software. Comparing this to SPDX and CycloneDX, these two SBOM formats are more descriptive of the software and its composition and not tied to the particular installation of the software.&#x20;

For more details, NIST provides an [excellent guideline for SWID tags](https://csrc.nist.gov/pubs/ir/8060/final).&#x20;

### Conclusion&#x20;

Having well-defined formats for storing, communicating, and encoding SBOM information is vital for its adoption. Both CycloneDX and SPDX have been widely adopted, and it seems that the current trend is that CycloneDX is getting the most attention. This can be attributed to the fact that the recent drivers, e.g., the Biden executive order and the EU cyber resilience act, are heavily focused on the security benefits for SBOMs.

In the next and final part of this series, we will show how OpenText Core SCA supports both exporting and importing of SBOMs to help you stay on top of security and license compliance.
