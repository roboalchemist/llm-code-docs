# Source: https://docs.debricked.com/opentext-core-sca-blogs/blogs/oss-licenses-part-4-strong-copyleft-licenses.md

# OSS licenses part 4: strong copyleft licenses

> This blog was published on 29th May, 2024.

The copyleft licenses are in several ways similar to the permissive licenses. Anyone is allowed to use, modify, and distribute the software, including making any changes to the software. The main aspects in which they differ are the restrictions and rights put on the software that is used together with, or derived from, a copyleft licensed software. Here, we take a closer look at the strong copyleft licenses, focusing on the dominant GPL and AGPL licenses.

As a copyleft licensee, the rights that are given to you for using and modifying the software, you also have to give to anyone who uses and modifies the software that you distribute. The core idea behind this is to ensure that any user of the software also has the rights and means to improve on it, and that any improvements are made available to the community. Due to this they are often also called reciprocal licenses. A permissive license would instead allow the licensee to put further restrictions on the software that they distribute. This includes making the software proprietary.

To separate the circumstances under which restrictions apply to software that use copyleft software, copyleft is often divided into strong and weak copyleft. Simply put, strong copyleft will apply to all works that are based on a strong copyleft work, while weak copyleft only applies to the specific weak copyleft licensed work. Basically, you can link to and use weak copyleft work without having to use a copyleft license for your own work. If you use strong copyleft work in any way you will have to make your own work strong copyleft as well. Weak copyleft licenses will be discussed in the next part of this blog post series.

The first copyleft license is the GNU General Public License (GPL). The GPL is actually a set of licenses. There are three different GPL versions, with [version 2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html) from 1991 and [version 3](https://www.gnu.org/licenses/gpl-3.0.en.html), released in 2007, still being very commonly used. Also, depending on how you count, the AGPL and the LGPL licenses can also be seen as GPL licenses. Their latest versions share several properties with GPL, just making slight modifications for their own intended purpose. Since LGPL is a weak copyleft license, that license will not be discussed here.&#x20;

### GPL license

The GPL license versions will here be referred to as GPLv1, GPLv2, and GPLv3 respectively.

The main difference between GPLv1 and GPLv2 is that the latter adds the explicit requirement that the work can be distributed only if all obligations are fulfilled. In other words, no other legal obligations can take precedence over the obligations in the license. Based on this, we will only look at GPLv2 and GPLv3 here.

Version 2 of GPL is the first of the two commonly used GPL licenses. GPLv2 and GPLv3 differ in some ways that make them relevant for different purposes and preferences, so there is still plenty of software licensed under GPLv2. The Linux kernel is the most prominent example of this.

#### Release of source code

The GPL license requires that the source code is also made available when the software is distributed. Under GPLv2 the source code needs to be offered to be distributed on a physical media upon request, or be accompanied with the executable. GPLv3 gives more flexibility and allows it to alternatively be made available over a network. It is of course most common to also distribute GPLv2 source code over a network, which is perfectly fine as long as you also offer to provide it physically.

#### Entire work falls under GPL

The main distinguishing property of a strong copyleft license is that a modified version must be licensed under the same license. There are two things to note here. First, the term “modified versions” include works that in any way use the GPL licensed software. It could be an actual modification of the source code, or it could be that you are linking your own program with a GPL licensed library, statically or dynamically.

Secondly, all combined code must be licensed under the GPL. This is sometimes referred to as a viral property. Any change to or derivative work of software licensed under the GPL can only be distributed under the GPL. A notable exception, explicitly written in the GPLv3, is software that is combined with AGPL licensed software. In that case, GPLv3 code will continue to be GPLv3 licensed, but the combined program will have the restrictions defined by the AGPL. The reciprocal property makes license compatibility important. Licenses that are compatible with the GPL can be combined into the same program, and the combined software can be licensed under the GPL.

The GPL still allows software with other licenses to be bundled together with GPL licensed software. In that case the GPL and non-GPL software must be clearly separated or not dependent on each other such that they together form a larger program.

#### Only distributed software

The GPL only applies if you distribute the software. Usage of the program, and modifications that are never distributed, are not restricted. This means that you can use the GPL licensed software yourself, or within the same company without being subject to the license. The exact definition of distribution is not clear from the GPLv2 license, and the word is used differently in different jurisdictions. GPLv3 clarifies this by talking about conveying instead, which means to make it available to the public so that others can make copies. Specifically, the license defines it as

> *To “convey” a work means any kind of propagation that enables other parties to make or receive copies. Mere interaction with a user through a computer network, with no transfer of a copy, is not conveying.*

The definition here is more clear than what was used in the GPLv2.

### Additions in GPLv3

The GPLv3 adds some clarifications and new requirements compared to the GPLv2. The GPLv3 license is considerably longer than the GPLv2 and there are many changes, both in the phrasing, but also in the actual obligations. Some updates and clarifications were made to the definitions to avoid ambiguity. Some of these were discussed in the previous section. As the GPLv3 adds additional obligations, it is not compatible with GPLv2. GPLv2 does not allow adding additional obligations and GLPv3 does not allow removing obligations. Thus, they can not be combined. Here, let us look at some of the other notable differences.

#### Anti-Tivoization

One property that was discovered in the GPLv2 was that it was possible to use GPL licensed software in end-user equipment, but to lock down the possibility to install new and modified software. Thus, you could still follow the license and release the source code, allowing everyone to redistribute it. In some sense, modification is also possible since you have the software, but the hardware can limit modified software to run on the devices. This was still compliant with the license, and used by e.g., Tivo. Thus, this practice is called tivoization.

The GPLv3 adds the requirement to also distribute information necessary to modify the software and to run modified versions on the products.

#### Patent grant and retaliation

GPLv2 does not include any explicit clauses regarding patent grants and patent retaliation. This is also the main reason why the permissive Apache License 2.0 is not compliant with GPLv2. The patent clauses in the Apache license put further restrictions on software than what is in GPLv2, which is not allowed by the GPLv2 license.

GPLv3 adds explicit information regarding both patent grant and patent retaliation. For the grant part, each contributor gives you a patent license for the claims in the patent. For the retaliation part, you may not initiate a litigation for patent infringement against someone using the software in accordance with the license. If you do so, your own license to the software will be terminated.

Though the patent grant is not explicit in GPLv2, it still has an implicit patent grant. The interpretation here is that if you are licensed the right to use, modify and sell the software, that also covers the right to do that for the parts of the software that are subject to a patent. In other words, you also give a patent license.

#### Application to DRM technology

GPL licensed software can be used for any purpose. This is one of the four software freedoms stipulated by the Free Software Foundation. This includes developing DRM technology. Some countries have legislation against developing software for circumventing technological prevention measures for DRM. If you distribute GPLv3 licensed software, the license states that you will not enforce any laws against your software. In effect, if you use any GPLv3 licensed software to develop DRM technology, this software should not be considered a technological prevention measure. You will not enforce such circumvention and you also allow such circumvention software to be further distributed.

### Allowing later versions of GPL

Most often, the copyright of GPL version X licensed programs says that it can be redistributed or modified under the terms of GPL version X or any later version. The following snippet is part of the copyright statement suggested by GNU when licensing code with GPLv2.&#x20;

> *This program is free software; you can redistribute it and/or* *modify it under the terms of the GNU General Public License* *as published by the Free Software Foundation; either version 2* *of the License, or (at your option) any later version.*

A corresponding phrasing is used with the GPLv3 license. Thus, if there are future versions of GPL that are more permissive, those permissions can then be applied to the terms. At the same time, if there are more restrictions in future license versions you can either choose to use the previous version without those restrictions, but it could also be that future versions of the program will be released with the new restrictions.

In some cases, licensors/copyright holders have decided to explicitly not allow later versions. Then the copyright text just specifies the GPL version that has terms that are applicable to the program. The Linux kernel is an example of software that is distributed under only the GPLv2 license.

These two options are distinguished by having different [SPDX identifiers](https://spdx.org/licenses/). For GPL version 3, the former case uses the GPL-3.0-or-later identifier, while the latter uses GPL-3.0-only identifier. This distinction can be particularly important for GPLv2, since the Apache License 2.0 is not compatible with GPL v2.0. Thus, GPL-2.0-only cannot be combined with Apache-2.0 while GPL-2.0-or-later can.

### The AGPL license

Another common strong copyleft license is the [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html). In the GPLv3 license, to convey a program explicitly means that you enable other parties to make or receive copies. If they cannot do that, then you are not conveying. If you are not conveying, then the obligations in the GPLv3 license do not apply.

Today, many services are offered over a network connection, e.g., web applications and SaaS services. The backend code of these services are not conveyed since the end users are not able to make copies. Thus, you can use and modify GPLv3 licensed code without being subject to the restrictions in GPLv3. GNU themselves also acknowledges this in the preamble of the AGPL license.

*The GNU General Public License permits making a modified version and letting the public access it on a server without ever releasing its source code to the public.*

AGPL closes this so-called Application Service Provider (ASP) loophole. AGPL aims to ensure that code that is accessed over a network has to be made available. The first version was published by Affero inc, hence the name. It was picked up by GNU and the current version is aligned with GPLv3 and is sometimes referred to as GNU AGPLv3.

The license text is a verbatim copy of the GPLv3 license text, but with the addition of one clause. The clause specifically requires source code of software that users can interact with over a network to be released to those users.

Combining works licensed under GPLv3 and AGPL is also specifically handled in both licenses. Code under the respective licenses will continue to have their own license, which is otherwise not allowed in copyleft licenses. However, the combined work will be subject to the AGPL requirements for network interaction.

### Conclusion

The GPL and AGPL licenses are by far the most important and dominant strong copyleft licenses. In particular GPL, both version 2 and 3, are the most commonly used. In the next part we will take a closer look at weak copyleft licenses. These serve as a middle ground when the permissive licenses are too permissive and GPL is too restrictive in terms of what the licensees can do with the code when combining it with their own.
