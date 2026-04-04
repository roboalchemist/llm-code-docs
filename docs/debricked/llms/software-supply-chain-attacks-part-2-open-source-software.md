# Source: https://docs.debricked.com/opentext-core-sca-blogs/blogs/software-supply-chain-attacks-part-2-open-source-software.md

# Software supply chain attacks, part 2: open-source software

> This blog was published on 10th December, 2021.

The use of open-source software is an ideal example of a software supply chain. Basically, all software depends on some open-source software, and often lots of it. This makes this software particularly interesting from a software supply chain attack perspective.&#x20;

In our previous post, we discussed supply chain attacks in general. Here, we will continue this discussion, but turn our attention to the open-source ecosystem and its role in the attacks.

***

**Go to other posts in our Software Supply Chain attack series:**

* Software supply chain attacks, part 1: defining and understanding the attack
* Software supply chain attacks, part 3: role of software composition analysis
* Software supply chain attacks, part 4: initiatives to support mitigations

### Supply chain attacks in open-source software

All companies that develop software are part of a supply chain. They assemble software using many third-party components, or dependencies, which often are open source. In this case, the creators of these components are suppliers, while the software product manufacturers are customers. This means that each dependency is a potential first attack target where the software using such dependency is the real target.

The Solarwinds, Keseya, and Codecov software supply chain attacks have received much attention in the media. Despite being unique in the attack details, they have one thing in common: the attackers targeted software code by adding malware to the code. This modified code was then downloaded and used by customers. The three are all private companies with proprietary software. The software is developed in-house and distributed through their own software distribution platform.

For OSS, there is added complexity including multiple diverse maintainers, software code repositories, and package distribution platforms. Though all these factors contribute to the success of OSS, they do open up a wide range of possibilities to initiate a supply chain attack. There is a sometimes extreme many-to-many relationship between suppliers and customers. [According to GitHub](https://octoverse.github.com/), the median number of transitive dependencies for a JavaScript project is 683. This means that not only will an OSS component be used by many customers, but each customer also uses a lot of OSS components.

We define a supply chain attack in the context of open-source software as an attack where a dependency is modified to include malicious code. This dependency is then included by other software, allowing the malicious code to run as part of that software. Referring to the definition in our previous blog post, the supplier asset is the code for the dependency. The attack techniques used to compromise the supplier can vary, which will be further detailed below.\
Parts of this post are inspired by [Ohm et al. – Backstabber’s Knife Collection: A Review of Open Source Software Supply Chain Attacks](https://link.springer.com/chapter/10.1007/978-3-030-52683-2_2), which was published at DIMVA 2020.

### Open-source development environment

To better understand and contextualize supply chain attacks in open source software, let us briefly sketch a typical open source development environment. We divide the supporting tools and services into three main categories: the version control system, the build system, and the distribution platform.

<figure><img src="https://debricked.com/blog/wp-content/uploads/2021/12/oss-dev-environment-graphic-supply-chain-attacks-two-post-debricked-1024x397.jpg" alt="" height="397" width="1024"><figcaption><p>An overview of the open source development environment</p></figcaption></figure>

#### Version Control System

The software is developed, controlled, and maintained using the Version Control System (VCS). This is also called Source Code Management (SCM). The older CVS and Subversion tools have today to a large extent been replaced by the distributed revision control tool Git. While Git can be used locally, most software is today hosted on a remote system that supports version control with Git. [GitHub](https://github.com/) is the main such provider, also offering access control, bug tracking, task management, and continuous integration. [Bitbucket](https://bitbucket.org/) is another well-known hosting service provider. [GitLab](https://about.gitlab.com/) is an example of a management tool for Git repositories. It provides version control, software management, and several DevOps-related functionalities.&#x20;

A number of maintainers regularly work on the code, committing their updates to the Git repository. Moreover, the community can contribute their own suggested changes and improvements. This is achieved by creating pull requests that the maintainers can review and incorporate into the repository.

#### Build system

In modern development, the build system consists of a build automation tool. This automates the process of compiling, linking, testing, and packaging the software. They integrate with the version control system. Some tools also include support for plugins. Importantly, they also include support for dependency management, being able to pull dependencies from a distribution platform, using a package manager. Some well-known build automation tools are Maven and Gradle (for Java), NAnt (for .NET), Webpack and Grunt (for JavaScript), Phing (for PHP), and Bazel that supports multiple languages.

#### Distribution platform

The distribution platform is used as a registry and storage of published open-source packages. It provides a centralized repository to find all dependencies that are used in a software project. The build system can pull the required dependencies at build time, updating to newer versions if required.&#x20;

For developers, the distribution platform also provides a place to publish dependencies such that they are easy to find for other developers and build systems. The distribution platform is often combined with a package manager. This is the entity that manages the dependency packages. It installs the packages into the correct locations, replaces old versions with newer ones, deletes unwanted packages, and installs transitive dependencies when needed.&#x20;

A well-known distribution platform for JavaScript packages is the npm registry, with npm being the corresponding package manager. For .NET, NuGet is a package manager, with NuGet Gallery a central package repository. Packagist is a packet repository for PHP, with the composer being a package manager. For Python, PyPI is a package repository and pip is a package manager.

### Supply chain attacks in the open-source environment

Referring to the open-source development environment described above, a supply chain attack can be initiated in several places. An attacker can compromise the version control system or its surrounding environment. Also, the build system or the distribution platform for hosting the dependency can be compromised in various ways. Let us look at some concrete examples where these different entities have been compromised in order to initiate a supply chain attack.

#### Attacking the VCS hosting environment

By compromising the hosting environment (GitHub, GitLab, Bitbucket), an attacker could inject malicious code into the software repository. This code, if undetected, would then be shipped with the next regular update of the software. The malicious code can be injected by a contributor, by creating a pull request with the new code. It could also be committed into the repository by a malicious maintainer.&#x20;

A significant example of the first case is when a researcher at the University of Minnesota [submitted vulnerabilities as bug fixes to the Linux Kernel](https://www.theverge.com/2021/4/30/22410164/linux-kernel-university-of-minnesota-banned-open-source). The goal was to demonstrate that it was possible to get these kinds of malicious bug fixes approved. The Linux community deemed this experiment awfully unethical, wasting the time of maintainers when they were reviewing the patches. Indeed, many maintainers do this work in their free time for the benefit of the Linux community.

In the second case, the project maintainer would be the one inserting the malicious code. A notable example is [the attack on the event-stream package in 2018](https://blog.npmjs.org/post/180565383195/details-about-the-event-stream-incident). In the attack, a person offering to help on the event-stream project was added as a project maintainer. This is an example of social engineering, where asking to become a maintainer allowed one to maliciously tamper with the code. Through this, the attacker added a dependency containing malicious code, flatmap-stream. Everyone who used event-stream with the malicious dependency was then a potential target. However, this attack specifically targeted the Copay software, which used the event-stream package. This was a Bitcoin wallet platform, and the malicious code attempted to steal Bitcoin from the end-users.

While the event-stream attack used social engineering to become a maintainer, another option would be to get hold of the credentials of other maintainers. This was e.g., demonstrated when a [security researcher noticed](https://medium.com/@vesirin/how-i-gained-commit-access-to-homebrew-in-30-minutes-2ae314df03ab) that the API token for committing code to a GitHub repository was accidentally published in Jenkins. Luckily, this issue was responsibly disclosed and no packages were affected according to the subsequent analysis.

In addition to accidental disclosure of credentials, an attacker can rely on guessing passwords for a maintainer’s account. A password guessing [attack was reported on the Gentoo GitHub account](https://wiki.gentoo.org/wiki/Project:Infrastructure/Incident_Reports/2018-06-28_Github). Gentoo is a popular Linux distribution. Attackers got administrative privileges, allowing them to modify the repository. Fortunately, the attack was early detected since the attackers decided to lock out other Gentoo developers from GitHub. Moreover, the changes did not make their way to a published distribution of Gentoo, but the attack underlines the importance of using two-factor authentication, at least for important accounts.

#### Attacking the build system

The next component, the build system, is another entry point for an attack. One possibility here is to take advantage of the limitations of multi-tenant systems, where one tenant can e.g., use security flaws to affect the build process of other tenants. With access to a common build server, one attack would be to let the [build step include a change to the host’s file](https://dl.acm.org/doi/pdf/10.1145/2491055.2491070). (For the historically interested readers, this might remind you of the [original description of the confused deputy attack](https://dl.acm.org/doi/10.1145/54289.871709), with the CSRF attack being a modern web-based variant.) This can change the VCS endpoint from which the code is downloaded. In the case of shared servers, a clear separation between the tenants is needed to avoid such attacks.

Another option would be to hijack the communication channel used to download packets from the distribution platform. This can be achieved by mounting a man-in-the-middle attack and replacing the genuine packet with a malicious packer instead. If there is no authentication of the remote server, and the genuine packet can not be otherwise authenticated, the client would not be able to detect such an attack. An example of this [was noted in 2014](https://max.computer/blog/how-to-take-over-the-computer-of-any-java-or-clojure-or-scala-developer/) when a user demonstrated the risks of downloading a packet over a non-TLS protected channel. TLS was only offered for paid accounts, leaving free accounts exposed to the attack. Subsequently, the provider turned on TLS for all accounts. This removed the possibility of mounting such man-in-the-middle attacks.&#x20;

The configuration of how to fetch packages can also be vulnerable to a so-called [dependency confusion attack](https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610). This attack technique started to emerge in early 2021. It uses the fact that the software uses private packages which are downloaded from within the organization. By creating public packages, and publishing them on a distribution platform, the package manager can be tricked to download those instead. If, for instance, the public repository has a version that is higher than the version number on the internal repository, the public repository can take precedence. [This can be mitigated](https://azure.microsoft.com/en-us/resources/3-ways-to-mitigate-risk-using-private-package-feeds/) through e.g., careful configuration of the package manager to specify the sources to be used for packages.&#x20;

#### Attacking the distribution platform

The distribution platform component of the open-source environment is the third possibility for initializing supply chain attacks on OSS. This can be accomplished in several ways. Similar to the VCS case, obtaining the credentials of a user with publish permission is a common attack vector.&#x20;

A [security researcher describes](https://github.com/ChALkeR/notes/blob/master/Gathering-weak-npm-credentials.md) how he was able to gather npm credentials for 14% of the npm package systems. This gave him publishing rights for these packages, allowing him to (potentially) inject malicious code in all the packages. The credentials were recovered by brute-forcing passwords, testing passwords that had been leaked on other services for the same email usernames, and searching for leaked credentials on GitHub repos. Many of the compromised accounts had packages that were used as transitive dependencies in other packages. Taking this into account, 54% of the npm ecosystem was affected. Luckily, the security researcher did not take advantage of this possibility.

A real attack was, however, [mounted on the eslint-scope and eslint-config-eslint packages](https://eslint.org/blog/2018/07/postmortem-for-malicious-package-publishes). This was accomplished by recovering the login credentials of a maintainer. The password had been reused on several other sites. With one of those sites compromised, and the password leaked, it was possible to log in on other accounts (npm in this case) with the reused credentials.

Malware has also been found in the [UAParser.js package on npm](https://therecord.media/malware-found-in-npm-package-with-millions-of-weekly-downloads/). The attack stands out as targeting a widely used package that several large businesses use. It has several millions of weekly downloads and is used by companies such as Facebook, Apple, Amazon, and Microsoft. It is believed that the npm account was compromised and benign versions were replaced by malicious ones. The included malware was able to download and execute programs on the affected systems. Due to the high severity of this incident, [CISA published a security alert](https://us-cert.cisa.gov/ncas/current-activity/2021/10/22/malware-discovered-popular-npm-package-ua-parser-js).

Npm is of course not the only package repository that has been subject to malicious changes to packages. The bootstrap-sass gem, distributed on RubyGems, was updated [to include a backdoor](https://lwn.net/Articles/785386/). This was most likely due to the credentials for one of the maintainers being compromised. Fortunately, the version with the malicious code was discovered quickly and removed from RubyGems.&#x20;

A related attack is to use social engineering to impersonate a user and have packages uploaded, or to get an account with publishing rights.

#### Injecting new packages

The examples above introduced malicious code through the use or download of the intended packages. A variant is to create new packages that are malicious and have them included as a dependency of other packages.&#x20;

A very common approach is to use typosquatting, i.e., to create new packages with names resembling names of other packages. If the names are not properly examined, a small typo could result in the malicious package being used. In 2017, the Slovak National Security Office (NBU) identified ten malicious Python libraries [uploaded on PyPI](https://www.bleepingcomputer.com/news/security/ten-malicious-libraries-found-on-pypi-python-package-index/). As an example, both urllib and urlib3 were created to typosquat the well-known urllib3 package. In another example, npm removed 38 JavaScript packages that were caught stealing environment variables from infected projects. A few examples, in this case, include sqlite.js and sqliter, typosquatting the sqlite package.

Typosquatting does not require any specific attack on the first target. No credentials need to be compromised or found, and no connection is hijacked. It only requires a packet with a name similar to the targeted packet. In that sense, it is borderline to be classified as a supply chain attack according to ENISAs definition. However, the malicious code does place itself as part of the supply chain, making it reasonable and common to view it as a type of supply chain attack.

### Protecting your software

Previously, we provided some general protection mechanisms for both suppliers and customers. These apply to a great extent also for the attacks targeting open-source software. Still, the examples above make it very clear that protecting the accounts can thwart many attacks. This includes both the VCS accounts and the distribution platform accounts.&#x20;

For suppliers, turning on two-factor authentication is one giant, and easy, leap towards fewer attacks like this. For the customers, i.e., those that rely on the open-source dependencies, a Software Composition Analysis (SCA) tool is a great asset. Such a tool will help understand and control the open-source dependencies. Our next blog post will discuss the role of the SCA tool in more depth.

[Debricked SCA](https://debricked.com/tools/security) helps you get an overview of all your open source dependencies, direct and indirect, as well as all vulnerabilities. Also, Debricked helps you automate the task of solving vulnerabilities and preventing new ones from being imported. [Create a free account](https://debricked.com/app/en/register) today (no credit card needed!) or browse our [pricing plans](https://debricked.com/pricing/).
