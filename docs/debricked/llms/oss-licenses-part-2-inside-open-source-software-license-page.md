# Source: https://docs.debricked.com/opentext-core-sca-blogs/blogs/oss-licenses-part-2-inside-open-source-software-license-page.md

# OSS licenses part 2: inside open- source software license page

> This blog was published on 28th March, 2024.

In the previous part, we gave an overview of copyright, gradually narrowing down the concept to open-source software (OSS) licenses. In this part, we will look at OSS licenses to understand what aspects are often being governed by the license. We will also discuss a universally adopted categorization of OSS licenses. The category then provides a general understanding of how the terms are dictated without going into the exact license text.

### The software license

Before diving into the OSS licenses, let us start by looking at software licenses in general. The software license is a legal agreement that dictates how software can be used and distributed. It specifies what users can do and what they cannot do with the software and it is at the licensor or copyright owner’s discretion to determine this within legal bounds, apart from what would be considered fair use.

To give a few typical examples, a software license often includes the following terms:

* **Warranty:** Normally, a warranty is a guarantee that something should work, e.g., over a given period of time. If not, you get your money back, or you get a replacement, or they will fix it for you. In software licenses, warranty clauses are usually quite the opposite. They explicitly say that the software is provided “as is” and that there is no warranty in the commonly used sense of the word. Some warranty can be provided by saying that the software should perform “substantially as described”.
* **Indemnity:** Indemnity is an agreement to compensate one party for loss or damage. It sometimes also comes with a maximum amount for that compensation. For software, indemnity is often connected to patent infringement or compliance with laws. In this case, the licensor is responsible for defending against claims and has to pay the associated costs. The license also lists all exceptions and limitations to the damages that can be paid.
* **Solving disputes:** In case there is a dispute, the license includes information on how this dispute should be settled.
* **Termination of license:** The license can detail under which circumstances it can be terminated. It can then also state the consequences of such a termination, e.g., that the software must be deleted from the system or device.

### Inside the open source software license

The typical content of an open source software license differs somewhat from the proprietary software license. The license has to handle the distinguishing features of source code availability, the right to use it for any purpose, the right to modify it, and the right to redistribute it with your own changes. The collaborative nature of open source, where anyone can contribute to the code, also distinguishes it from proprietary software, something that has to be taken into consideration in the license.

Let us look at some of the general properties that need to be handled in an OSS license. In later blog posts, we will discuss how different open source licenses handle some of these in more detail.

#### Obtaining a license to use open source software

A key difference between open source software and proprietary or otherwise licensed software is how a license is obtained. In non-OSS, an agreement is made between the licensee and the licensor, e.g. if you want to use the software, you contact the copyright holder and request a license. A license is then given to you as a result of some financial transaction or agreement. In open source, a license is automatically given to anyone following the license obligations. The license will remain valid for as long as the license obligations are met. No contact or explicit agreement between the licensee and the copyright holder is ever needed.

#### Preserving license information

A core principle of OSS licenses is that all recipients are made aware of their rights and obligations. In practice this means that the license text must accompany any redistribution of the software. This in turn ensures to preserve the right to freely use, modify, and share the software. Even very short and slimmed down licenses, like the 1-clause BSD and MIT licenses, include this as the minimum (only) requirement. Only those that try to mimic putting the code into the public domain lack this requirement, like 0-clause BSD, MIT-0 and CC0.

#### Warranty

OSS is provided “as is”, meaning that there is no warranty. The software comes with no guarantee regarding its performance or suitability for a particular purpose. This means that all potential issues fall under the user’s responsibility. This includes software bugs, vulnerabilities, compatibility issues, and any consequences of those. Because of the lack of warranties, users should thoroughly test and evaluate the software to ensure that it meets their specific requirements before deploying it in any production environment. Thus, if you use OSS you should be prepared to take full responsibility for anything you use the software for.

The limited warranty is a natural consequence of OSS being collaboratively developed, often by volunteers. Providing warranty would expose individual authors to liability. Such legal and financial risks could make developers more hesitant to contribute to open-source projects.

#### Copyleft provisions

Since you are allowed to modify and redistribute the code, there are sometimes requirements on modified or derived works. These requirements are also what distinguishes the main categories of OSS licenses. Copyleft requires that a modified version of the software, or software that includes copylefted code, is also distributed under the same or similar terms as the original. This is generally referred to as the license being reciprocal. Thus, it must also allow free access to the source code and permit further modifications and redistribution under the same license.

The goal of copyleft is to maintain the open and free nature of the software, ensuring that it remains available to all to use and build upon. In short, the idea is for any improvements made to the software to be available to anyone. The GNU General Public License (GPL) is one of the most well-known examples of a copyleft license.

#### Non-endorsement clauses

If you add OSS authored by someone else to your own code, the authors of that OSS will automatically become co-authors of the resulting software package. In particular, if you use OSS authored by someone else in a commercial product, such contributions may not be taken advantage of by implying that the authors endorse, approve or support the product.

The purpose of the non-endorsement clause is to provide a clear boundary between the authors of the included OSS and the authors of the product itself. This protects the reputation and integrity of the OSS contributors. The non-endorsement clause is the difference between the BSD 2-clause and the BSD 3-clause licenses. It is also present in Apache License 1.0 and 1.1, but was rephrased in Apache License 2.0 to instead include the use of the licensor’s trademarks. Using names of developers for endorsement is likely prohibited even without the clause.

#### Patent clauses

Some licenses explicitly include patent clauses. These are used to regulate how patents related to the software are handled by contributors and users. There are two main patent considerations that can be found in the licenses, patent grant and patent retaliation. Though the wordings and details can differ between different licenses, the main ideas are the same.

The patent grant clause says that if a contributor adds code that is covered by any of his or her patents, all receivers of the software will automatically get a license for those patents. A contributor can not sue or claim royalties from someone using the software. A grant can be broad or narrow. If the grant is broad, if you contribute, the grant will hold for all code in the licensed software. For narrow grants, the grant will only hold for the code they contributed. A middle ground between broad and narrow grants is to include code that is tied to the same functionality in the grant. GPLv3 has a broad grant as it applies to the whole program. Apache License 2.0 has a narrow grant since it only applies to the code contributed by the entity distributing the software.

A practical example of how a patent grant might work is two companies collaborating on a software project. When the project is ready and the companies individually start building business around the software, an explicit patent grant protects either company from the other company suddenly claiming that the code that they contributed included patented ideas and that anybody using it now has to obtain patent licenses.

Patent retaliation intends to make it less attractive to initiate a patent litigation towards distributors of the software. If someone starts a litigation for patent infringement, that entity will also lose all rights to use the software, as well as all patent grants related to the software. By the initiator losing the patent rights, the distributor has a possibility to use their own patents to defend against such infringement claims. As the entity that starts the litigation will no longer have a valid license to distribute the open source they will also open themselves up to legal action from any copyright holder.

Even if there are no explicit clauses regarding patents, some licenses are said to have implicit grants. This is particularly true for the permissive licenses that say that you can basically do anything you want with the code. Such statements could be interpreted as also granting use of any patented ideas expressed through the source code. But of course, in the end it is not a layman’s interpretation that counts, but the court’s in which the litigation is handled.

#### Contributed code

When a developer contributes to an open source project, by copyright laws the contributed code is owned by the contributor. That means that he or she basically can decide permissions and restrictions for that code. This situation can be handled in different ways. It is generally understood that if you open a pull request to a project with code under a certain license, the contributed code has the same license. However, this is not necessarily clear from a legal point of view.

A common solution to this is using a contributor license agreement, or CLA. This is a legal document that a contributor needs to sign before any contribution of theirs can be accepted to a project, stating the license of the code that they contribute. Another solution is a statement on the project web page saying that contributors agree to have their code licensed with the same license as the project itself. Finally, these wordings are also sometimes found directly in the license. As an example, the Apache License 2.0 states that contributions are under the terms and conditions of the license.

### Open-source software license categories

Open source software licenses can be divided into permissive and copyleft licenses. Basically, permissive licenses have very few restrictions and obligations on what you can do with the software, while the copyleft licenses have more restrictions and obligations. This categorization is perhaps a bit too coarse grained since there are very many different licenses, but by further dividing copyleft into weak and strong copyleft licenses we can catch most of the major differences using the resulting three categories.

**Permissive**. A permissive license typically has few restrictions and obligations, and those are generally easy to comply with. Basically, you can use the code however you want as long as you provide the original license text and attribute copyright holders on distribution. This includes modifying the code and releasing the modifications under another license, even a proprietary one. There is no need to share your modifications or release the source code of the resulting work. The most common permissive licenses are MIT, Apache and BSD.

**Strong copyleft**. For strong copyleft licenses, any work that is based on or uses the work in some way, must maintain the same strong copyleft license (or a license with the same restrictions or obligations). Due to the reciprocal nature of copyleft licenses, any distributed modifications must be made available under the same license as the original code. The license ensures that anyone down the chain of code that uses the strong copyleft code, will also release the code under the strong copyleft license. This is why strong copyleft licenses are sometimes referred to as viral, as they will automatically apply to all distributed code that comes into contact with them. The GPL license is by far the most commonly used license that falls into the strong copyleft category. The AGPL license takes this one step further, stating that also non-distributed code that can be accessed over a network (e.g., SaaS), need to follow these copyleft requirements.

**Weak copyleft.** A weak copyleft license is somewhat more permissive than the strong copyleft variants. It will allow you to link to and use the code without your own code being subject to the same license. So, proprietary code can use weak copyleft code by linking to it, and still maintain its proprietary license. The LGPL, MPL, and the EPL licenses are common weak copyleft licenses. A specific requirement in LGPL is that, if you use the weak copyleft licensed library, you need to make sure it is possible to easily replace it by another library.

Another category is the **public domain**. This is not really open source, but deserves to be mentioned due to its connection to some open source licenses. If the software is in the public domain it means that there are no intellectual property rights connected to the software anymore. So no license is needed to use or distribute it.

Works created by the U.S. Government are in the public domain since they are excluded from copyright law in the U.S. It is possible to explicitly dedicate a work to the public domain, thereby abandoning the copyrights. This could however be a bit problematic since, in some countries, you are not allowed to abandon your moral rights. To solve this, there are licenses that try to mimic the public domain as far as possible. The idea is to put it into the public domain, but if that is not possible a very permissive license without an attribution clause is used as a fallback option. Examples include the CC0 and the unlicensed licenses.

### Conclusion

This was an overview of open source licenses and what they typically contain. We also categorized the licenses into their main categories. Just referring to the category often gives enough information to know if a particular OSS can be used in a given use case. Still, each license has its own properties and sometimes even small differences can have important legal consequences. In the next part of this series we will look at the permissive licenses in more detail. Both their different versions and the differences between them.
