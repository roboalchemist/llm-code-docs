# Source: https://docs.debricked.com/overview/help/frequently-asked-questions-faq.md

# Frequently asked questions (FAQ)

### Is OpenText Core SCA’s service *on prem* or *SaaS*? <a href="#isdebrickeds-serviceonpremorsaas" id="isdebrickeds-serviceonpremorsaas"></a>

OpenText Core SCA is a Software as a Service (SaaS) solution currently.

### What type of scanning does OpenText Core SCA do?

OpenText Core SCA utilizes manifest-based scanning, which effectively identifies security issues across a wide range of file formats. While binary scanning is often considered superior due to its ability to produce fewer false positives, it can overlook critical security vulnerabilities, supply chain attacks, and [licensing problems](https://docs.debricked.com/product/license-risk-management). Additionally, binary scanning does not account for test and build dependencies, which can still present risks, unlike manifest-based scanning.&#x20;

Manifest-based scanning identifies components listed in your dependency files, while binary scanning analyzes and fingerprints binary files. Binary scanning can be useful when source code or package managers for installing dependencies are unavailable. However, it does not include development and test dependencies, which can pose significant risks. Manifest-based scanning is more effective at identifying vulnerabilities and compliance issues, making it better suited for the developer workflow. For vendor code and C++/C scanning, OpenText Core SCA can [scan an SBOM](https://docs.debricked.com/overview/language-support/cyclonedx-sbom) if the vendor provides one.&#x20;

Ultimately, the decision between manifest scanning and binary scanning depends on your workflow and objectives. At OpenText Core SCA, we emphasize [automation](https://docs.debricked.com/product/automation) and tools that enable developers to identify and resolve issues swiftly and accurately. This is why we concentrate on manifest scanning.&#x20;

### How accurate is the service in finding a vulnerability?

OpenText Core SCA service detects any open-source vulnerabilities in your repository, drawing information from various sources, including but not limited to the NVD Database, NPM, C# Announcements, FriendsOfPHP’s security advisories, the Go Vulnerability Database, the PyPA Python Advisory Database, GitHub Issues, GitHub Security Advisories, mailing lists, and more. These sources are updated every 15 minutes to ensure that we identify as many vulnerabilities as possible.

### OpenText Core SCA has found a wrong dependency. What should I do?

If you think OpenText Core SCA has identified an incorrect dependency, you can [manage and override your dependency matches using our CLI](https://docs.debricked.com/tools-and-integrations/cli/debricked-cli/file-fingerprinting#manage-or-override-results).

### What is meant by “increased computation” for enterprise customers?

Increased computation is when the number of available workers is increased to allow scanning more number of files simultaneously. This greatly enhances the scan speed for enterprise customers.

### To what extent can root fixes break the code?

When root fixes cause issues in the code, you should manually update the dependencies. There is always a risk of breaking changes when updating these dependencies, and the extent of that risk varies with each update. While the risk is not inherently greater with root fixes than with indirect fixes, OpenText Core SCA ensures that dependency tree is not compromised by introducing a version of a dependency incompatible with its upstream dependencies.

### How long do I need to wait to before requesting a second password reset?

You must wait one hour before you can request a second password reset.

### Is there a way to restrict what repositories certain users can see?

[Role Based Access Control](https://docs.debricked.com/product/administration/users/role-based-access-control-enterprise), which is an Enterprise feature, enables granting and enforcing access to functionalities and integrated repositories by assigning predefined roles to users.

### Is it possible to extract a pie chart or other visualization of the identified licenses and dependencies?

You can export licenses, including both licenses and dependencies, in an Excel format, which allows you to create a pie chart. Alternatively, use the API for assistance.

### What do we classify as a “scan”?

When a developer commits code, the code is scanned irrespective of the size of the committed changes

### Does OpenText Core SCA run on a PC, or does it upload data to your servers?

There are several ways to run OpenText Core SCA service.

* Manually upload your dependency files.
* Integrate OpenText Core SCA service into your test pipelines through Platforms such as GitHub or GitLab.

### How do you distinguish between frequent and sporadic contributors?

OpenText Core SCA examines averages and reviews the list of committers on a monthly basis. As many businesses have a certain number of "non-developer" committers for a limited time, the customers are expected to determine the actual number of contributing developers and incorporate the information into the contract.

### What measures does OpenText Core SCA implement to prevent and detect vulnerabilities?

OpenText Core SCA implements the following measures to prevent and detect vulnerabilities:

* Use own service to find known vulnerabilities in dependencies
* Conduct third-party penetration tests
* Continuously run own penetration tests internally

### Where is OpenText Core SCA’s data stored?

Customer data is stored using Google Cloud Platform (GCP) as the service provider, located in Netherlands.
