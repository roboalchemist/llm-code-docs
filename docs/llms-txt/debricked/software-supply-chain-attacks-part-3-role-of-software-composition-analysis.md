# Source: https://docs.debricked.com/opentext-core-sca-blogs/blogs/software-supply-chain-attacks-part-3-role-of-software-composition-analysis.md

# Software supply chain attacks, part 3: role of software composition analysis

> This blog was published on 17th December, 2021.

As discussed in the previous post, open-source software and its surrounding ecosystem open up several possibilities for software supply chain attacks. Many previous attacks and proof-of-concepts have underlined the importance of protecting the supply chain of open-source dependencies.

There is, unfortunately, no one-stop-shop for eliminating the supply chain attack threat, but there are several measures that together can add up to higher security. In this post, we look at Software Composition Analysis and its role in protecting software from these kinds of attacks.

***

**Go to other posts in our Software Supply Chain attack series:**

* Software supply chain attacks, part 1: defining and understanding the attack
* Software supply chain attacks, part 2: open-source software
* Software supply chain attacks, part 4: initiatives to support mitigations

### OSS provides a colossal attack surface

In software development, products often rely on many open-source components. Each project can have thousands of direct and transitive dependencies in total, each of them being a potential attack target. Having a malicious component as a software dependency puts all users of that software at risk. It is nearly impossible to manually keep track of all these dependencies and understand the risks each carries.&#x20;

We often do not know anything about the suppliers, and still, we are heavily dependent on the software that they bring to our products. Even if these suppliers are not malicious, they still open up for possible attacks through vulnerabilities in their development processes or how they operate their environments. Small mistakes can have devastating consequences, not only for their own software but for all customers that rely on their software. Our previous blog post described a plethora of ways how to compromise OSS components in a supply chain attack scenario.

### SCA and supply chain attacks

Software Composition Analysis (SCA) is all about open-source, and third-party components. At Debricked, we love open-source, and we embrace all its possibilities. It brings so many positive aspects, both in terms of collaboration and community building. It is also great from an efficiency and security point of view, with code reuse and transparency. SCA provides a way to better understand and optimize the use of open-source components. This aligns very well with the goal to minimize the risk and consequences of supply chain attacks. Indeed, in the context of the open-source software supply chain, these attacks take advantage of the trust we put into our third-party components.&#x20;

Recalling the Solarwinds Orion supply chain attack, an SCA tool would not prevent such attacks. Also, several attacks targeting open-source components would also not have been directly prevented. However, knowing your OSS components can lower the risk of attacks and often reduce their consequences. Let us discuss this in more detail from three different points of view. Since not all SCA tools are created equal, our discussion will focus on how [Debricked’s SCA tool](https://debricked.com/tools/security/) can help.

#### SBOM generation

By including an OSS component in your software, you implicitly declare a certain level of trust in that component. It will be run with the access rights of the software and can read and manipulate its environment. Knowing and analyzing who you trust is a fundamental practice in security. The first step towards this is to enumerate (know) all software components that you use. The Software Bill of Materials is a list of all software components used and the versions in use. Depending on the format, the SBOM sometimes includes additional information, such as license information for each component.

Vendors can use the SBOM to understand the components better, but it can also be shipped with the software. The [Biden executive order](https://www.whitehouse.gov/briefing-room/presidential-actions/2021/05/12/executive-order-on-improving-the-nations-cybersecurity/) explicitly demands that a purchaser should be provided with an SBOM for each product. This could be achieved either by shipping it with the product or publishing it on a website. Another example is the Food and Drug Administration (FDA), who has [set out to require](https://www.medtechdive.com/news/fda-seeks-more-power-for-medical-device-cybersecurity-mandates/605107/) medtech companies to supply an SBOM together with their devices.&#x20;

The main reason for requiring an accompanying SBOM is to allow the customer and any other third party to have a better view of the software composition. This will enable more people to promptly know if they are susceptible to potential vulnerabilities in the devices. It also puts pressure on the vendor to include better and more secure components as they now can be judged by the components and versions they choose.

The primary purpose of an SCA tool is to provide insight into the software components, i.e., the components that would be the first target in a software supply chain attack. Though the SBOM itself will not protect against a specific attack, it sheds light on the components, helping us analyze and assess the trust we put into them.&#x20;

#### Open-source health data

As a consumer of open-source software, i.e., someone that uses it in their own projects, probably the most crucial aspect for security is how “good” the OSS component is. It is, of course, better to have well-maintained OSS upstream in your software than to have something that no one has maintained for years. The “good” OSS is likely to have better development processes with higher security overall. This applies both to the people in the community and the code that is produced.

There are lots of aspects that can be seen as positive vs. negative for how good a project is. Well-maintained is certainly not a well-defined term. This is a rather complex issue, and it would take forever to manually assess all imaginable aspects for all OSS in your software. Even if you do it for all direct dependencies, you are most likely left with hundreds or thousands of transitive dependencies. Of course, you can leave it to the maintainers of the direct dependencies to assess the ones they include upstream, but that is probably not a safe bet.&#x20;

To assess a component, you may want to ask yourself, “How experienced are the contributors?”, “How active are the contributors”, “How widely used is it?”, or “How are vulnerabilities managed”?. If we can quantify these and many other important metrics, we can also comprehend the component’s strengths and limitations. Using such metrics then allows us to get a better idea about the security risks they carry and we can actively choose to replace them with components with better metrics.&#x20;

The [Open Source Select database](https://debricked.com/en/select/) provides these metrics and many more. Additionally, you can see how the metric has changed over time to early on identify components that have decreasing metrics. But best of all, the database is open and free to use for everyone.

#### Automatic patching

The software supply-chain attacks aim to insert malicious code in a dependency or software and then distribute this as a new version. As soon as the malicious version has been detected, a new patched version is released as soon as possible in order to minimize the consequences and the number of malicious code downloads. Subsequently, as a software customer, it is essential to update to the patched version immediately.&#x20;

Even though you have already previously downloaded the malicious code, this code might not yet have been triggered or even made it into a production environment. Automatically patching the code and downloading the new version is often part of an SCA offering. Through the SBOM and an updated vulnerability database with the malicious version(s), Debricked’s SCA tool will alert you on the vulnerable version and automatically create a pull request with the secure version. Thus, you will have updated your dependency with just the click of a button and are no longer susceptible to the attack.

### Try it out!

Do you want to see what an SCA tool can do for you? [Feel free to try out](https://debricked.com/app/en/register) or [browse our pricing plans](https://debricked.com/pricing/) to learn more. We have a freemium alternative for small companies. For larger needs, we can assure you that it is well worth your investment. It does not only help you protect against supply chain attacks but also direct attacks targeting your software. [IBM’s X-force threat intelligence index (2021)](https://www.ibm.com/security/data-breach/threat-intelligence) concluded that the most common attack vector in 2020 was “scan and exploit”. Thus, the most common way for attackers to gain access to a target is to exploit security vulnerabilities in software.&#x20;

As noted, the SCA tool is not a magic wand to fully mitigate the risk of software supply chain attacks. It is part of the bigger picture. In our next post, we will look at current initiatives in the security community that can help reduce software supply chain attacks.
