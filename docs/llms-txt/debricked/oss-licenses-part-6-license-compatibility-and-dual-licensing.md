# Source: https://docs.debricked.com/opentext-core-sca-blogs/blogs/oss-licenses-part-6-license-compatibility-and-dual-licensing.md

# OSS licenses part 6: license compatibility and dual licensing

> This blog was published on 28th August, 2024.

When developing software that uses open-source components it is important to understand to which extent those components can be used together. When used together, what license applies for the combined work? This problem is referred to as license compatibility. In this part we will discuss license compatibility and also what dual licensing is and how it can help in certain situations when combining software components.

In the previous posts in this series, we have sometimes referred to a license as being compatible or not compatible with another license. We noted that the BSD 4-clause license is not compatible with the GPL, while the BSD 3-clause license is. We also noted that the MPL 2.0 is compatible with the GPL (using the secondary license option), while the MPL 1.0 is not. Let us look more closely on compatibility.

When you distribute a software package that includes a set of open source components, each component is governed by its own license terms. Thus, you need to make sure that all license terms are respected for each component. In some cases this is easy, while in others it is not even possible given the terms in the different licenses.

### License compatibility

When we talk about license compatibility, we talk about the possibility of combining software licensed under two different licenses into a larger work. Two licenses can have conflicting requirements such that it is impossible to satisfy all requirements in both licenses. Such licenses are incompatible.

As an example of compatible licenses, the MIT license is compatible with the GPLv3. This means that we can use MIT licensed code and GPLv3 licensed code in the same distributed software project. This notion of compatibility does not consider exactly which license the distributed software is licensed with. It just says that it is possible to do it. Continuing the same example, the distributed software must be licensed under GPLv3 as a requirement of the GPLv3 is that any derivative is also licensed under the GPLv3. There is no similar requirement in MIT. The software can, however, not be distributed under MIT since that would violate the terms in the GPLv3. Still, they are compatible since by meeting the requirements in the GPLv3 we also meet all MIT requirements.

An example of licenses that are not compatible is the combination of the Apache 2.0 license and the GPLv2 in the same distributed software. Apache 2.0 sets restrictions on patents, which are not included in the GPLv2. At the same time, the GPLv2 explicitly states that you can not add further restrictions in modified and distributed code. Thus, you can not license the distributed software under the GPLv2 since it will now include software with patent restrictions. It is also not possible to distribute it under the Apache 2.0 license since the GPLv2 is reciprocal, stating that the combination must be licensed under GPLv2. Thus, there are contradicting requirements, i.e., the two licenses are incompatible.

The GPLv3 introduced patent clauses very similar to the ones in the Apache 2.0 license. This makes the GPLv3 compatible with the Apache 2.0 license. Distributing software consisting of both GPLv3 and Apache 2.0 licensed code is possible as long as the combination is GPLv3 licensed.

In some cases, GPLv2 licensed software is licensed under “GPLv2 or later”, as given by the copyright notice. If this is the case, it is possible to achieve compatibility with Apache 2.0. The licensee then chooses to apply the terms of GPLv3 to the software and distribute the resulting software package under the GPLv3.

Since the GPL is both very restrictive and very common, license compatibility is often discussed in the context of licenses being compatible with the GPL. This often refers to both GPL version 2 and version 3, though as we saw above, the Apache 2.0 license is only compatible with one of them.[ GNU maintains a list of licenses](https://www.gnu.org/licenses/license-list.html) together with their compatibility with GPL.

When it comes to permissive licenses, these never put restrictions on the software that the permissively licensed software is combined with, so there are no restrictions that block the compatibility. You can combine MIT and BSD 3-clause licensed code with your own and license the resulting program under either MIT or BSD 3-clause, or virtually any other license you wish.

#### Copyleft compatibility

As noted in part 5 of this blog series, the MPL 2.0 and the EPL 2.0 are both compatible with GPL through the use of a secondary license. This means that contributions can also be licensed under the GPL, making it possible to combine and distribute software with GPL-licensed code. The secondary license option is explicitly stated in the MPL 2.0 and the EPL 2.0.

The other common copyleft licenses are the AGPL license and the different versions of the LGPL and the GPL licenses.[ GNU provides a matrix](https://www.gnu.org/licenses/gpl-faq.html#AllCompatibility) that summarizes the compatibility between these licenses. In short, if you want to combine LGPL and GPL licensed code, that combination is compatible, but the resulting combined program must be licensed under GPL. The main incompatibility issue is between GPLv2 and GPLv3. The problem is similar to the problem when combining code licensed under the Apache 2.0 license and the GPLv2. The GPLv2 explicitly disallows more restrictions to the distributed program and the GPLv3 has additional restrictions. These include the patent grant/termination, but also the tivoization restrictions introduced in GPLv3.

Again, the incompatibility between the GPLv2 and the GPLv3 can be fixed if the GPLv2 copyright notice adds the possibility to re-license the software under a later version. This is true for some GPLv2 licensed software, but not for all.

LGPLv2.1 licensed code may be relicensed to GPLv2 or GPLv3, which can help solve compatibility issues with those licenses.

The GPLv3 is compatible with AGPL. This compatibility is explicitly handled in both licenses. They state that you can combine code under both licenses, but the resulting program must be licensed under the AGPL.&#x20;

### Dual licensing

Dual licensing refers to distributing software under two (or sometimes more) different licenses. Since “dual” semantically refers to “two”, sometimes the term multi licensing is used to also include situations where more than two licenses are used. Still, we will keep referring to it as dual licensing here.

Dual licensing allows licensors to meet different user needs, where the licensee can meet the license requirements for the software by meeting the obligations of either license. Various dual licensing models can help maximize the adoption, while maintaining community engagement and allow profitability. Dual licensing can include different commercial licenses, a mix of commercial and open source licenses, or different open source licenses.

To distribute software under different commercial licenses is very common. It can be used to capture different market segments, meet specific needs, and to maximize revenue. In the freemium or open core models, a limited version of the software is freely available, but to get access to advanced features another license can be purchased. Different licenses can also be defined depending on the number of users and usage metrics. This is particularly common in SaaS offerings.

#### Commercial and open source dual licensing

Since we are focusing on open-source licensing here, let us take a look at the case of combining a commercial license with an open source license. One purpose of such a dual licensing model is to strike a balance between monetizing the software while at the same time benefit from the advantages of having a community that can improve the software.

From the licensee’s point of view, the ability to choose between an open source and a commercial license adds flexibility. The open source licenses offer the benefits of community collaboration, transparency and cost, while commercial licenses can provide the assurance of professional support, additional features and not having to release the source code of derivative works. The specific advantages of each choice will of course depend on the details of the licenses. In the end, which license to choose will depend on the use case and if the terms and obligations in the open-source license can be complied with or if a commercial license is necessary.

Some examples of software with this dual licensing model include[ MySQL](https://www.mysql.com/about/legal/licensing/oem/) with dual GPLv2 and commercial license, the[ Qt framework](https://scythe-studio.com/en/qt-license) with dual AGPL and commercial license, and[ Ghostscript](https://www.ghostscript.com/licensing/index.html) with dual LGPLv3 and commercial license.

#### Dual open source licenses

As has been discussed in the previous part of this blog post series, there are significant differences between open source software licenses. They all have their advantages and different use cases.

Software can also be dual licensed in order to gain wider adoption. Some communities or organizations might prefer a certain license (or explicitly forbid others) and offering to choose between licenses can increase adoption of the software.

Wider adoption can be gained by increasing the license compatibility. Offering the software under several licenses ensures broader compatibility with other software. In the previous blog post we saw an example where EPL 1.0 licensed code was sometimes dual licensed with BSD to make it compatible with the GPL.

Another example is Mozilla Firefox, which was previously released under a triple license, with the MPL 1.1, the GPL and the LGPL. Since the MPL 1.1 was not compatible with the GPL, licensees could opt for the terms in the GPL and distribute derivative works under the GPL. Similarly, some licensees might want to use the code in a LGPL licensed library and distribute the derived work under LGPL. By also distributing Mozilla Firefox under LGPL, this was possible. Current versions of Mozilla Firefox are however released under MPL 2.0, which is compatible with GPL.

#### Applying more than one license

Dual licensing is often understood as the possibility for the licensee to choose between two or more licenses. It is also possible, but less common, to have two licenses being applicable at the same time. Thus, the licensee must comply with both licenses. The most well-known example is OpenSSL, which previously had two different licenses where both applied at the same time. To make this clear, the licenses are separated by an “AND”, while in the more common case they are separated by an “OR”.

### Conclusion

Tracking license compatibility becomes increasingly important due to the integration of diverse and complex software components in modern products. Incompatible licenses can lead to legal and compliance risks. Detecting license incompatibility early also allows faster remediation since it can be difficult to migrate to other software components when they become an integral part of a product.

Dual licensing can make it easier for users to avoid license compatibility issues and also allow organizations to choose a license that is most suitable for their given use case.

We have so far covered the most common open-source licenses in this blog series. In the next part we will look at some other licenses, some that are common but not considered open-source, and some a bit less common but still considered open-source.
