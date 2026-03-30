# Source: https://docs.debricked.com/opentext-core-sca-blogs/blogs/the-software-bill-of-materials-part-1-benefitting-from-the-sbom.md

# The Software Bill of Materials, part 1: benefitting from the SBOM

> This blog was published on 13th February, 2023.

Whether you produce, purchase, or operate software, insights into the supply chain will provide you with a range of benefits.

The SBOM will help provide these insights. In a series of blog posts, we will discuss several aspects of the SBOM, including benefits and drivers for adoption, and also dig a bit deeper into the actual SBOM files and formats. But let us start with defining what an SBOM is.

***

Catch up on other posts in our SBOM series:

* The Software Bill of Materials, Part 2: Drivers, motivators, and challenges
* The Software Bill of Materials, Part 3: The SBOM file
* The Software Bill of Materials, Part 4: SBOM with OpenText Core SCA

### What it is&#x20;

Simply put, the Software Bill of Materials (SBOM) is a listing of all software dependencies that are included in a software application. It includes not only the direct dependencies used but also the dependencies used by those dependencies, also known as indirect or transitive dependencies. As such, it describes the supply chain relationships used when building the software. &#x20;

#### A list of ingredients&#x20;

Just like food in the grocery store has a list of ingredients written on the package, we can think of the SBOM as a list of ingredients for a software application. For people with allergies, the list of ingredients can be used to verify that it does not contain anything unwanted.

Often, people may want to stay away from unethical or unhealthy content or things with too many unnatural chemicals used only for preservation, color, or profit. The list is mandatory since we want to allow people to make informed decisions about the food they buy. The transparency also puts pressure on the manufacturer to not include unnecessary bad ingredients since the food and the manufacturer can now be judged by the ingredients.

The SBOM serves a very similar purpose. By listing all packages included in a software application, users will be able to make informed decisions about which applications to use based on the included packages, and the developers will be incentivized to use up-to-date, secure, and well-maintained software.&#x20;

#### Not just ingredients&#x20;

The analogy to ingredients is often used. Yes, it will show you the components that the software product consists of. But it does not stop there. Looking at the most common SBOM formats used today, there is also support for adding valuable metadata about the components.

This metadata can consist of details on known vulnerabilities for the component. It can also be detailed license information, i.e., the requirements and the restrictions for including the component in another piece of software. The metadata can also include how the different components fit together, i.e., which component depends on other components. If these relationships are complete, the SBOM can provide the full dependency graph for all components in the software.&#x20;

Thus, while the ingredients analogy is easy to grasp, there can be quite much more to it if the SBOM capabilities are fully used.&#x20;

In the following blog posts, we will look at SBOMs from several points of views. In this part, we will first discuss their benefits and how they can affect the different stakeholders in a value chain. Then, in part 2, we will take a look at the current drivers behind adopting SBOMs at a wide scale. We will also discuss several challenges related to creating and consuming an SBOM.

In part 3, we will look more closely at the leading formats for SBOMs. These are currently SPDX and CycloneDX, but we will also compare them to the SWID tags that can also be used as an SBOM format. Finally, in part 4, we will show how SBOMs can be used with Debricked. It is very easy to generate an SBOM from an integration, but it is also easy to manually just upload an SBOM file to be scanned for vulnerabilities and license compliance.&#x20;

### Benefits and use cases&#x20;

The SBOM can be used to provide insights into your software. It is an invaluable enabler for several business critical operations related to software development, software management and software consumption across the value chain. &#x20;

#### Not a silver bullet&#x20;

Before discussing the benefits, we note that the SBOM does not really solve any problems on its own. It needs to be accompanied by organizational processes to take advantage of the data it holds. With technical tools and automations, you will be able to collect, present, and add business value to the data in the SBOM.

This will make the data actionable and improve software and product security. It will also allow organizations to be compliant with both licenses and security requirements. Assuming such tools and processes are in place, let us look at some of the benefits the SBOM will give you.&#x20;

#### Security&#x20;

Its main claim for success is risk management and risk reduction, with security being the most well-known use case. It is easy to argue for the security case. We all want to avoid a costly data breach. In 2022 the average cost of a data breach was [estimated](https://www.ibm.com/reports/data-breach) to be $4.24 million. At the same time, together with phishing, using known vulnerabilities are the [two main attack vectors](https://www.ibm.com/reports/threat-intelligence/) seen today. Now, add to this that the number of discovered vulnerabilities is constantly increasing.

With the SBOM listing all software dependencies, it is possible and feasible to assess if any of these dependencies have known security vulnerabilities. And if they do, we know to patch them. Without the SBOM, or at least without the detailed insights into the supply chain that the SBOM provides, there would be no way of really knowing if the software is vulnerable or not.

This is a game changer for those purchasing and using the software. If there is a new vulnerability, they can immediately assess if they are exposed.&#x20;

#### License compliance&#x20;

Another benefit is license compliance. Every time we include code written by someone else, e.g., Open-Source Software (OSS), we are using copyrighted code. We can not use that code without a license. The license will tell us what we are allowed to do with the code and under what circumstances.

In some cases, the restrictions and our obligations are rather heavy if we want to include the code in distributed software. With the SBOM, we get insights into third-party dependencies. Then we can also know what licenses apply to the different dependencies. These licenses can also be written directly in the SBOM. &#x20;

#### Dependency health&#x20;

Security and license compliance are the two benefits that are most often discussed in the SBOM context. At the same time, we see that the use of OSS is increasing, and today’s codebases have around 80-90% OSS. This increased dependency on OSS presents new challenges, some of which the SBOM can help meet. &#x20;

One thing that many organizations are struggling with is how to choose the best OSS component for a specific task. There can be many OSS projects supporting similar functionality, so which one should we choose? This question is more important than it may seem at first. You want a project that has ongoing community support, not one that was or will be abandoned in the near future. You also want a project that will patch vulnerabilities, otherwise, there is no safe version to upgrade to, and you must patch the source yourself.

You may also want to choose a project that engages experienced developers, a project with reasonable documentation, and perhaps a project with an active core team. Though there are no current security vulnerabilities or license compliance risks, all these properties will contribute to a forward risk.

Having a software inventory through the SBOM will help in analyzing the software dependencies for such forward risks. An automated tool, such as Debricked, will automatically scan the SBOM and present you with a range of metrics that will help you understand the health of your software dependencies.&#x20;

#### Increased transparency&#x20;

The benefits do not stop here. Using the data to assess security, license compliance, and health can be seen as very direct benefits. But we also need to consider the effect of having to supply an SBOM when software is distributed or sold to customers. With the SBOM, the software is no longer a black box. There is transparency in what you deliver.

The software provider can no longer hide bad practices when it comes to patching and vetting the included software, and license compliance need to be top-of-mind in order to avoid facing legal problems. &#x20;

When customers have insight into the components of an application, they can also check for security vulnerabilities, license compliance, and scrutinize the software for out-of-date and unsupported components. And by doing this, they can judge their suppliers by their practices in choosing and maintaining dependencies.

This clearly incentivizes better practices on the supplier’s side. In particular, security vulnerabilities will affect the customer if they are exploited, so the customer can put pressure on the supplier to have patched software in the applications. This will lead to better, more secure, and compliant software. &#x20;

#### Stronger supplier-customer relationships&#x20;

The supplier can also use the SBOM as a chance to get stronger relationships with their customers. Consider an organization that chooses between two suppliers, one of them is able to provide a detailed and up-to-date SBOM, while the other is not willing or able to do so. As a customer, which one would you choose? &#x20;

In one case, you will be in control of vetting the software yourself if you wish, and the supplier is also incentivized to have good software practices for their third-party components. &#x20;

In the other case, you are buying a black box without any possibility of scrutinizing the application’s components. And why are they not providing an SBOM? Is it because they just don’t have the tools or knowledge to produce one, or is it because the software actually has known vulnerabilities? Or do they not know if there are vulnerabilities or not? Are they using tons of outdated software? Do they even know if they do? None of the reasons are very flattering, and all other things equal, the supplier would surely go for the supplier that provides an SBOM.&#x20;

The SBOM will also facilitate an ongoing discussion between the supplier and the customer. Why did you choose this software? Are we actually vulnerable to this new CVE related to an included component? Yes, there will likely be more questions from customers, some good and some less relevant, but it is a chance for the supplier to show good practices throughout the software lifecycle. This will increase confidence in the supplier and improve the relationship between the customer and the supplier.&#x20;

#### Reduce remediation costs and time-to-market&#x20;

Fixing security problems is more costly the later they are done. Updating to a secure version of a dependency can be easily done at development time. If you do it later, there will be added complexity. Updating software that is in production or that has already been distributed can be very costly.&#x20;

Using SBOMs and an accompanying process for keeping track of vulnerabilities, licenses, and health information will allow developers to find problems quickly. This will also reduce the remediation cost. In fact, having, e.g., an SCA tool for keeping track of all these things related to dependencies will probably quickly pay off when vulnerabilities, licenses, and health are continuously monitored.&#x20;

With carefully considered choices for third-party dependencies, there will hopefully be fewer problems with this software in the future. This includes fewer vulnerabilities, faster patch processes, no license issues, and better-maintained software. Less added complexity will allow developers to focus more on performance, stability, user experience, and added features. In the end, this will reduce the time-to-market and allow the supplier to be more competitive.&#x20;

### **Conclusion**

The SBOM presents several benefits to all stakeholders. Though the pure benefits should be enough to immediately adopt SBOMs, this is often not enough to push organizations over the edge. Adoption sometimes requires a push from governments and authorities. In the next part, we will discuss these drivers as well as the emerging threat landscape and the challenges presented when faced with SBOM adoption.
