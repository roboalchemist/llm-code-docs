# Source: https://docs.debricked.com/opentext-core-sca-blogs/blogs/software-supply-chain-attacks-part-1-defining-and-understanding-the-attack.md

# Software supply chain attacks, part 1: defining and understanding the attack

> This blog was published on 26th November, 2021.

Software supply chain attacks have become increasingly important. They entered the main spotlight after the Solarwinds attack, and security people and businesses cannot seem to stop talking about them.

Looking at that attack and several other recent similar attacks, it is clear that the recent superstar status is quite well-earned.&#x20;

We have written a four-post series covering software supply chain attacks to delve further into the subject. The first part will touch upon the general definition to help you better understand such attacks. In later posts, we will look at it in the light of open-source software, see the role of software composition analysis tools, and also give an overview of current community initiatives for thwarting the attacks.

***

**See other posts in our Software Supply Chain attack series:**

* Software supply chain attacks, part 2: open-source software
* Software supply chain attacks, part 3: role of software composition analysis
* Software supply chain attacks, part 4: initiatives to support mitigations

### The supply chain attack

Starting from the beginning, the supply chain is the set of entities involved in supplying a product or a service to a customer. This can start with producing raw materials in the form of silicon chips to hardware assembly, software development, and delivery to the end customer. In a *supply chain attack*, an early step in the chain is maliciously modified. This modification then propagates to later entities and spreads throughout the product supply chain as more and more companies use the outputs of the previous steps. The [National Institute for Standards and Technology (NIST)](https://www.nist.gov/) defines supply chain attacks as,

*“Attacks that allow the adversary to utilize implants or other vulnerabilities inserted prior to installation in order to infiltrate data, or manipulate information technology hardware, software, operating systems, peripherals (information technology products) or services at any point during the life cycle.”*

The most well-known supply chain attack is probably the [manipulation of Supermicro’s hardware](https://www.bloomberg.com/news/features/2018-10-04/the-big-hack-how-china-used-a-tiny-chip-to-infiltrate-america-s-top-companies). In that attack, a tiny chip was added to motherboards that made it into servers at Amazon, Apple, and about 30 other U.S. companies. In a *software supply chain attack*, we restrict the supply chain to only software development. The idea is to make malicious changes to a piece of software. This software is then used (and trusted) by others, either end-users or other software that includes the malicious component as a dependency.

### A recent focus on software supply chain attacks

The attack methodology is not new, but several factors add up to its recent popularity. First, we have witnessed several impactful attacks that fall under the umbrella of software supply chain attacks. These attacks include the Solarwinds Orion software compromise and the Kaseya software platform. Second, as digital innovation has accelerated during the global pandemic, our reliance on software, digital platforms, and digital infrastructure has increased. This has boosted cyberattacks in general, and supply chain attacks are no exception.&#x20;

A third factor is the increased use of third-party open-source software (OSS), providing more entry points where malicious code can be inserted. It also opens up for including OSS that is not well-maintained and where the development processes and policies are still in their infancy.&#x20;

### The importance of the attack

The importance of the supply chain attack can primarily be attributed to the fact that the attack will affect a large number of customers while only initially targeting one supplier. Instead of targeting thousands of organizations, an attacker can target one organization, still attacking lots of organizations.&#x20;

In that sense, it can be seen as a variant of an amplification attack. The attacker will get much more “bang for the buck” when malicious code is automatically distributed between the supplier and its many customers or users.

<figure><img src="https://debricked.com/blog/wp-content/uploads/2021/11/supply-chain-attack-one-post-1024x683.jpg" alt="" height="392" width="589"><figcaption><p><em>The attacker targets a software supplier, but the attack affects its customer.</em></p></figcaption></figure>

For software, this distribution is typically in the form of publishing updates to a piece of software, but we will present a few other examples later in this blog post series. The common “always keep your software updated” paradigm helps this distribution as well.

Many software products have elevated privileges on the device or computer they are running on. A successful attack that targets such software will subsequently also have the same access rights. In addition, if the customer software runs within a protected network, the attacker could also gain access to other devices on the same network.

Evidence of its importance can be found in the recent cybersecurity executive order by U.S. president Biden, which was discussed in the context of SBOMs in a previous post. The executive order explicitly discusses the need to secure the software supply chain. This should be addressed in several ways, including multi-factor authentication, automatic tools for discovering vulnerabilities, and participating in a vulnerability disclosure program.

### Elements of a supply chain attack?

We temporarily take a step back to the more general definition of a supply chain attack. The [European Union Agency for Cybersecurity (ENISA)](https://www.enisa.europa.eu/) characterizes a supply chain attack as having two targets. The first target is the supplier, and the second is the customer using the supplier’s software or hardware. Further, ENISA, in a [recent report](https://www.enisa.europa.eu/publications/threat-landscape-for-supply-chain-attacks), formally defined four key characteristics present in a supply chain attack.

#### 1. Attack techniques used to compromise the supplier&#x20;

The first one refers to how the attack was carried out in order to compromise the supplier. Examples include exploiting software or a configuration vulnerability, brute-forcing credentials, or social engineering.

#### 2. Supplier assets targeted in the attack&#x20;

The second key characteristic refers to the target of the attack. The target often forms the connection to the attack on the customer. If the target is software code, the idea is to get the customer to download and execute this code. If the target is data, then this data can be used in phishing attacks. If the data is a private key, it could be used to create digital certificates in a man-in-the-middle attack.

#### 3. Attack techniques used to compromise the customer&#x20;

This refers to how the customer was attacked. When downloading malicious code through an automatic software update, the attack is exploiting a previously established trust relationship. Other examples could be a drive-by download on a website or a phishing attack.

#### 4. Customer assets targeted in the attack&#x20;

This is the main target of the attack. It includes e.g., stealing and modifying data, performing money transfers, or sending spam.

According to ENISA, any supply chain attack should have these characteristics. For the software supply chain attacks, the targeted supplier asset is the code. Exactly how the code is accessed and compromised varies between attacks. The customer is the most often compromised through the trust relationship that exists when downloading new code. Additionally, the customer asset can vary widely, from opening backdoors to stealing passwords or accessing cryptocurrency wallets.

### The Solarwinds attack

Many large-scale supply chain attacks often rely on compromising enterprise networks or systems for creating software. Indeed, this was reported to be the case in the [Solarwinds](https://www.businessinsider.com/solarwinds-hack-explained-government-agencies-cyber-security-2020-12?r=US\&IR=T), [Keseya](https://www.csoonline.com/article/3626703/the-kaseya-ransomware-attack-a-timeline.html), and [Codecov ](https://about.codecov.io/security-update/?utm_medium=article\&utm_source=blog\&utm_campaign=security-incident\&utm_content=security-event\&utm_term=clicked-inline-cta)attacks. By targeting the suppliers’ software distribution platform, a modified version of the software was sent to a large number of customers. As an example, in the Solarwinds attack, out of the 33,000 customers using the Orion product, around 18,000 of them reportedly installed the vulnerable updates. Victims included U.S. agencies such as the Pentagon and the Department of Homeland Security. But also large private companies, such as Microsoft, Cisco, and Intel were subject to the attack. In total, 425 of the fortune 500 companies were affected.

We can map this attack to the characteristics defined above. It is not fully known how the attackers took control over the software build system. Nonetheless, there are indications that a zero-day vulnerability was used, possibly in combination with brute-forcing credentials and social engineering. The assets targeted were primarily the software code of Solarwinds. This was used to mount the second attack targeting the customers.&#x20;

The second attack took advantage of the trust relationship between Solarwinds and their customers. The malicious code was downloaded and signed using a valid certificate signed by Symantec. In Internet communication, digital certificates form the backbone of all secure connections and establish trust on websites. The primary customer assets targeted in the attack was their data. The malware, denoted Sunburst, could upload data on the infected system to third-party servers. It was also able to execute files, profile the system, and control system services. It is clear that though the attack targeted Solarwinds, the actual targets were their customers.

The Solarwinds attack shows that an organization can be vulnerable to an attack even though its own security processes and policies are good. This is what makes the attack very difficult to protect against from the customers’ perspective. They are attacked by someone within their trust boundary, which is comparable to an insider attack.&#x20;

### General protection mechanisms

Since the supply chain attack targets both a supplier and the customer, both these can and should take part in the protection against the attacks. [The Cybersecurity and Infrastructure Security Agency](https://www.cisa.gov/) (CISA) and NIST have jointly released guidelines for Defending Against Software Supply Chain Attacks. The recommendations target both the customer and the supplier. We refer to the [published guidelines](https://www.cisa.gov/sites/default/files/publications/defending_against_software_supply_chain_attacks_508.pdf) for an in-depth discussion, but let us summarize some of the recommendations.

#### Customer recommendations

The customer recommendations given by CISA and NIST can be briefly summarized as follows:

* Use a risk management program to understand the software used and its risks in their context. One such process is the [Cyber Supply Chain Risk Management (C-SCRM)](https://csrc.nist.gov/Projects/cyber-supply-chain-risk-management/publications) program.&#x20;
* Ensure (through, e.g., certifications) that the supplier follows best practices for security throughout the software development lifecycle. This includes penetration testing, code analysis, and identification of known vulnerabilities.&#x20;
* Require a software bill of materials (SBOM) that explicitly lists components developed by the vendor or a third party.
* Understand what data is critical and how it is communicated between system components. This will make it easier to monitor the right parts of the system and to identify anomalous behavior.
* Limit external connections that could be used to exfiltrate data from the system.
* Use network segmentation to confine an attack to a small part of the organization. A more advanced approach could be to use different vendor software for different parts of the system or network. This decreases the overall risk from vulnerabilities in a single product.
* Have a contingency plan with failover processes to efficiently mitigate a successful attack.

#### Supplier recommendations

Similarly, CISA and NIST present a set of recommendations for the suppliers. The attack on the supplier is similar to any other targeted attack. Therefore recommendations follow common software development best practices. We summarize them as follows:

* Follow a software development lifecycle process and make sure to implement security in all steps of the process. NIST has its own [Secure Software Development Framework (SSDF)](https://csrc.nist.gov/Projects/ssdf) with key security practices. Other well-known and widely used frameworks are the [BSIMM ](https://www.bsimm.com/)and [SAMM](https://owaspsamm.org/) maturity models for secure software development. These can help structuring the work to satisfy security requirements, follow secure coding practices, and to verify the security of third-party components.
* Identify system components that are high-value assets in order to better prioritize component importance. This could help to more efficiently allocate resources.
* Set up a process for discovering vulnerabilities post-release since such vulnerabilities could be the result of an attack. Discovery can be made by the vendor, the customer, or a third-party, and vulnerabilities should be remediated quickly.
* Deliver a software bill-of-materials to give customers and third-parties an inventory of the product.
* Have a defined disclosure practice that enables fast remediation of vulnerabilities and submissions to the CVE community.

#### A Zero Trust Architecture (ZTA)

Another general protection against supply chain attacks is to implement a [Zero Trust Architecture (ZTA)](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf). Somewhat simplified, this means to trust no one. Or, in other words, assume that everything is an attack attempt until proven otherwise. As noted above, trust is a significant component in the attack, and by assuming that an entity is not trusted, the attack would be more difficult. This is not to say that the attack(s) will be prevented, but on average, it should raise the bar for the attackers.&#x20;

ZTA is a modern and still emerging philosophy and security paradigm. It can be seen as a response to another emerging trend, namely the reliance on remote users, systems, and resources. In fact, Bring Your Own Device (BYOD), and cloud-based assets are the new normal in enterprise networking. Today, the network is not the central component to protect, but instead, the focus is being put on protecting resources, services, accounts, workflows, etc.

The adoption of a ZTA is explicitly required by Joe Biden’s Cybersecurity Executive Order, which is a witness of its perceived importance to improve cybersecurity in organizations and the supply chain.

### Software supply chain attacks and open-source software

The open-source ecosystem allows a wide range of possibilities to compromise the software supply chain. The use of, and reliance on, third-party code repositories and the online packet distribution channels open up additional attack possibilities. In our next blog post, we will dive deeper into the attacks targeting open-source software.
