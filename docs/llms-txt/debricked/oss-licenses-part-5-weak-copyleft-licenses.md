# Source: https://docs.debricked.com/opentext-core-sca-blogs/blogs/oss-licenses-part-5-weak-copyleft-licenses.md

# OSS licenses part 5: Weak copyleft licenses

> This blog was published on 9th July, 2024.

For the strong copyleft licenses, a distinguishing property is that their requirements and restrictions also apply to works that use the licensed software in some way. This is true even if the software is just used as a library. If you distribute the software, the complete program has to be licensed using a strong copyleft license. In this part of this blog post series, we look at the weak copyleft licenses. They are not as restrictive in this sense, but still keep the copyleft property when the software package is modified.

The strong copyleft idea is in many ways attractive. If you create or contribute to the software, you allow everyone else to use and improve on it in any way they wish if you distribute it with a strong copyleft license. You are also certain that others’ improvements will continue to be shared, usable, and modifiable by everyone.

One could however claim that this will limit adoption of the software since it can not be used together with proprietary code (if distributed). Permissive licenses allow this without putting requirements on other code.

The middle ground is to have a weak copyleft license. Such a license will allow you to use the software under certain circumstances without having to distribute your own derivative work under a copyleft license. The exact circumstances differ between the licenses, but the general idea is that you have to share the source code of any improvements you make to the software but not necessarily to software that uses it as a library. Here, we will look at some of the most common weak copyleft licenses.

### LGPL license

Originally, LGPL was short for Library General Public License. This was the name of its first release, which was [LGPL 2.0](https://www.gnu.org/licenses/old-licenses/lgpl-2.0.en.html), when it was released in 1991. It started off with version 2.0 since it aimed to align with the GPL version 2, so there are no earlier versions. The name “Library” reflected the fact that it was created to allow the use of libraries without this resulting in a derivative work.

In the [LGPL 2.1](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.en.html), released in 1999 and [LGPL 3.0](https://www.gnu.org/licenses/lgpl-3.0.en.html), released in 2007, LGPL is instead short for Lesser General Public License. The term “Lesser” was used to clarify that it does less to protect the freedom to share and change software. LGPL 2.1 is an update to the LGPL 2.0, while LGPL 3.0 is a complete rewrite and provided as an addition to the GPLv3. Thus, the main differences between the LGPL 2.1 and the LGPL 3.0 are the same as the differences between the GPLv2 and GPLv3. This includes the differences related to patent retaliation, tivoization and compatibility with other licenses.

#### Modifying the library code

If you make modifications to the LGPL licensed library, and distribute the modified library, then the copyleft obligations apply. In the case of the LGPL, the license for the modified library must be either LGPL or GPL. This means that you must also provide the source code of the modifications. If the library is part of a combined work, where the library is just one part, then the requirement only applies to the library, not to the rest of the code.

#### Dynamic and static linking

A main distinguishing feature of the LGPL compared to many other weak copyleft licenses is how the copyleft obligations apply to the linking of code. The main idea here is that it should be easy for users to replace the LGPL licensed code with other code.

The LGPL allows for dynamically linking the LGPL licensed code to code with other licenses. This means that you can have a program with a proprietary license that uses functionality in LGPL code by dynamically linking to the code. Since it is dynamically linked (shared library), it is easy to replace the LGPL code with other, or modified, code and still run the program.

Static linking is a bit trickier. If the LGPL code is statically linked, this will make it much more difficult to replace the LGPL code within that software. This does not mean that the whole codebase needs to have a copyleft license, but the requirement of being able to relink the LGPL code still applies. This means that you need to provide necessary code and installation information that allow users to modify and relink the software to a modified library.

### Mozilla Public License (MPL)

The Mozilla Public License is a weak copyleft license, but it differs in significant ways from the LGPL when it comes to the copyleft requirement. MPL is file-based, meaning that if you make changes to a file that is MPL licensed, then those changes need to be distributed under an MPL license as well. Additional files that extend or interact with the library do not have this obligation. This is somewhat less restrictive, but a lot simpler to understand (and agree on), than the LGPL.

#### MPL 1.0 and MPL 1.1

The first version of the [Mozilla Public License (MPL 1.0)](https://www-archive.mozilla.org/mpl/mpl-1.0) was released in 1998. Only a year after, based on public comments and contributions, an updated version was released, the [MPL 1.1](https://www.mozilla.org/en-US/MPL/1.1/). The main changes were the introduction of a patent retaliation clause, to allow multiple licenses if the author wishes, to give alternatives for distributing the code, and some clarifications of other parts.

#### MPL 2.0

The [MPL 2.0](https://www.mozilla.org/en-US/MPL/2.0/), which was released in 2012 modernized the license. Several changes were introduced, but the main idea with file-based weak copyleft was unchanged. It clarified the file-based property, which was a bit more implicit in the previous versions.&#x20;

To allow for compatibility with the GPL licenses, a secondary license was added. The secondary license is one of the GPL licenses (including LGPL and AGPL) and it allows for the work to be combined with work under the secondary license and to be distributed under that license. It differs from traditional dual licensing in that the original work remains licensed exclusively under MPL 2.0. The secondary license only applies when the work is combined and redistributed with other code that is licensed with the secondary license. If the licensor wishes to exclude the secondary license, this must be explicitly stated in the copyright notice.

MPL 2.0 also added an explicit patent grant clause to make it clear that contributors granted a patent to any code added by the contributor. The grant is a so-called narrow grant, meaning that it only applies to the contributed code. This is, e.g., different from the broader patent grant in the GPLv3.

Another important change was the introduction of a grace period if you are non-compliant, before your license rights are permanently terminated. If you become compliant within 30 days you will regain your license rights.

A final change worth mentioning is that MPL 2.0 removed the requirement to state all modifications made to the original code.

#### Common Development and Distribution License (CDDL)

The CDDL license is based on MPL. It was released by Sun Microsystems in 2004, i.e. after MPL 1.1 but before MPL 2.0, as a simpler and clearer version of MPL 1.1.

CDDL comes in two versions, [CDDL 1.0](https://spdx.org/licenses/CDDL-1.0.html) and [CDDL 1.1](https://spdx.org/licenses/CDDL-1.1.html), with very minor differences. Moreover, the actual differences between CDDL 1.0/1.1 and MPL 1.1 are very few. One notable difference is that CDDL did not have the requirement of stating all modifications, the part that was also dropped in MPL 2.0.

### Eclipse Public License (EPL)

The Eclipse Public License (EPL) is another weak copyleft license. It is a successor to the Common Public License (CPL) and is very similar to the MPL license. Both the EPL and the MPL differ from the LGPL in the same way. First, EPL applies only on file-level and, second, there is no requirement to have the library easily replaced. Thus, static linking is not problematic for EPL licensed software.

The patent grant in EPL is considered narrow as it only applies to the code made by the contributor. This is the same patent coverage as was added in MPL 2.0.

[CPL 1.0](https://opensource.org/license/cpl1-0-txt) was released by IBM in 2001. Through a collaboration between IBM and the Eclipse Foundation, it was replaced by [EPL 1.0](https://www.eclipse.org/legal/epl-v10.html) in 2004. Apart from shifting the responsibility for the license from IBM to the Eclipse Foundation, the only difference was a small change in the patent retaliation part. See[ here](https://www.eclipse.org/legal/eplfaq.php) for details.

#### EPL 2.0

[EPL 2.0](https://www.eclipse.org/legal/epl-2.0/) was released in 2017. It remains very similar to the previous version but includes some minor changes. To clarify that it is a file-based weak copyleft license, the word “file” was explicitly used instead of the previous word “module”. In EPL 1.0, it was explicitly stated that it was governed by U.S. laws and the laws of the state of New York. EPL 2.0 is less US-centric and removes this clause. EPL 2.0 also removed the phrasing “object code” in order to make it more suitable also for scripting languages, where source code and object code often is the same.

Perhaps the most important addition in EPL 2.0 was, similarly to MPL 2.0, the possibility to assign a secondary license. It had the same purpose as for MPL 2.0, allowing compatibility with the GPL licenses, but it only allows GPLv2 and later versions to be named as secondary license. Different from MPL 2.0, here the copyright notice must explicitly include that the software can be distributed under the secondary license.

With EPL 1.0, projects were sometimes dual-licensed with BSD in order to make the projects compatible with GPL. But with BSD the copyleft parts were removed. Using a secondary license, the copyleft was instead maintained.

### Conclusion

The weak copyleft licenses provide a middle ground between copyleft and permissive licenses. Only changes to the weak copyleft licensed code needs to be redistributed under the same license, but it is allowed to call the code with code that has another, even proprietary, license.

Within this category, there are clear distinctions between the LGPL and the other weak copyleft licenses. LGPL takes a holistic approach and considers the complete library as one entity that the copyleft applies to. You need to provide means to modify or replace the LGPL parts, which is difficult to adhere to if the library is statically linked. For the other licenses discussed here, the copyleft requirements apply on file level. There are no requirements that the library must be easy to modify or replace, making static linking not a problem.

We have already touched upon the concept of license compatibility and dual licensing. In the next part of this series we will take a close look at these concepts to better understand them and the implications they have.
