# Source: https://docs.debricked.com/opentext-core-sca-blogs/blogs/oss-licenses-part-7-other-licenses.md

# OSS licenses part 7: other licenses

> This blog was published on 13th February, 2025.

We have previously discussed the most common permissive, weak copyleft and copyleft open- source licenses. We have also discussed license compatibility and dual licensing. Now we turn our attention to licenses that are not really considered open source, but still have a role to play in the open source ecosystem. But before we do that, we briefly discuss some permissive licenses that are somewhat less common but that are still quite often encountered in code bases.

### Other permissive licenses

There is a vast number of open source licenses and it is not possible to discuss them all in a blog post series. And it does not make sense to do so, since many of them are not used much. The majority are categorized as permissive licenses, and in addition to the ones we have already seen, there are a few that could be considered semi-important. At least from the point of view that they are sometimes encountered and it is good to have a grasp of how they aim to distinguish themselves from the common ones. Here, we briefly summarize six open source licenses other than the common BSD, MIT and Apache 2.0 that were previously discussed. For details, refer to the respective license.

The[ ISC license](https://www.isc.org/licenses/) was published by the Internet Software Consortium. It is used for code in OpenBSD and it is in effect the same as the MIT and the 2-clause BSD license, i.e., all distributed copies shall include the copyright notice. The license text is just a bit simpler and more concise.

The[ Unlicense](https://unlicense.org/) license is an attempt to put the software into the public domain. There are no requirements specified, only the right to do anything for any purpose and by any means. This also means that the license does not have any warranty disclaimer, which is otherwise seen in most open source licenses.

The[ WTFPL](http://www.wtfpl.net/about/) (Do What the F\* You Want to Public License) is another license that waives all rights with the intention of putting the software in the public domain. It is very informal and explicit, making it lack clear legal implication. For this reason some organizations may wish to avoid using software with this license. Licensors may want to dual license it with something more formal, e.g., the MIT license.

The[ zlib license](https://www.zlib.net/zlib_license.html) is e.g., used for the zlib compression library itself and for the libpng library for handling PNG images. It is a simple license, and compared to MIT it adds a suggestion to include an acknowledgement to the software in the documentation if it is used in a product. It also adds the requirement to mark altered versions so that it is clear that it is not the original software.

The[ Academic Free License 3.0](https://opensource.org/license/afl-3-0-php) is a permissive license that aims to be more explicit and unambiguous in its language than the more common and short MIT and BSD licenses. It targets academic or research projects and, from a legal point of view, its language makes it more enforceable than MIT and BSD. In addition, it has both patent grant and patent retaliation clauses.

The[ Artistic License 2.0](https://opensource.org/license/artistic-2-0) is a permissive license designed to balance flexibility for derivative works while preserving the original project’s identity. It allows modifications to be distributed under the same name if they remain open source, or under a different name with fewer restrictions. This ensures the original project remains distinct, while giving developers the freedom to adapt and innovate. The Artistic License 2.0 is most notably associated with the Perl programming language and its related modules and libraries.

### Notable non-open source licenses

The previous parts of this series have focused on open source licenses. A source available license is similar in that the source code is available, but it has not been approved by the [Open Source Initiative](https://opensource.org/licenses) as an open source license due to additional restrictions. These restrictions are typically designed to prevent unrestricted commercial exploitation of the code. This ensures that the creators retain control over how their software is used commercially, which open source licenses generally do not enforce.

Since open source software also makes the source code available, those licenses can be seen as a subset of the source available licenses. Let us take a closer look at two licenses that are source available, but not considered open source, namely the Server Side Public License and the Business Source License.

#### Server Side Public License

The[ Server Side Public License](https://www.mongodb.com/legal/licensing/server-side-public-license) (SSPL) is a copyleft license that shares some similarities with the AGPL. It is based on the GPLv3 but extends the coverage to software that is made available over a network. However, in contrast to the AGPL, the SSPL requires anyone that offers the software as a service (SaaS) to make not just the source code of the SSPL-covered software available, but also the entire source code of the service. This includes the infrastructure, the tools, deployment scripts, user interfaces, APIs, etc, even if they are not directly part of the SSPL-licensed software.

The SSPL was introduced in 2018 by MongoDB with the intention to limit the possibility for cloud vendors to profit from offering the database as a service. With AGPL, it is unclear exactly what parts of such an offering would have to be open sourced. With SSPL, MongoDB aimed to clarify this by making it explicit that all parts of the service must be open sourced, and also released under the SSPL. The specific changes can be found in Section 13 of the[ SSPL license](https://www.mongodb.com/legal/licensing/server-side-public-license).

The SSPL has[ not been approved by the Open Source Initiative](https://opensource.org/blog/the-sspl-is-not-an-open-source-license) as an open source license. The motivation is that the introduced requirements are overly restrictive and renders the software not usable for any purpose. This violates the first of the four freedoms, as[ defined by GNU](https://www.gnu.org/philosophy/free-sw.en.html#four-freedoms), namely “The freedom to run the program as you wish, for any purpose”.

SSPL has subsequently also been adopted by e.g., Elastic and Redis. Both release their software dual licensed with SSPL and another license that restricts the use of the software as a managed service unless a commercial license is obtained.

#### Business Source License

The[ Business Source License](https://mariadb.com/bsl11/) (BUSL) is another source available license that is not considered an open source license. It originates from the MariaDB corporation which uses it for the MaxScale product. It intends to strike a balance between allowing access to source code and protecting the commercial interests of the creators.

The license has a few distinguishing features. First, the software will be relicensed to another license within four years. The exact license and time frame can be specified by the license text as long as the new license is compatible with the “GPL 2.0 or later”. This time restriction allows creators to monetize the software, while still eventually contributing it back to the open source ecosystem.

Second, by default production use of the software is prohibited. This severely limits commercial use of the product. However, it is possible to define an “additional use grant” to make the allowed use a bit less limited. This could e.g. be that it is allowed to use the software in a production environment, but not in a way that competes with the vendor’s business. An example of this is[ Terraform that uses BUSL with an additional use grant](https://github.com/hashicorp/terraform/blob/main/LICENSE) like this. While this might seem like a reasonable limitation, it can be difficult to exactly know what would be considered competing and not. Such ambiguity creates a legal risk and in order to err on the side of caution, the software might still be avoided in some organizations despite the additional use grant.

Similar to SSPL, the restrictions in the use of the software do not comply with the requirements for open source software and it is thus not considered an open source license. It is also similar to SSPL in the sense that it prevents competitors from offering the software as a service, but it differs in that it will eventually revert the code to an open source license while SSPL licensed software will remain source available indefinitely.

#### Microsoft .NET Library License

The[ Microsoft .NET Library License](https://www.microsoft.com/web/webpi/eula/aspnetcomponent_rtw_enu.htm) is a license used by Microsoft to distribute .NET libraries via NuGet. This is not an open source license and the packages are distributed as compiled object code. At the same time, the source code for the libraries is typically open source and available on GitHub under a permissive license, usually MIT.

This is a special case of a dual license where the source code is provided with a permissive license, but the compiled object code is provided with a much more restrictive license.

Distributing the code with an MIT license encourages contributions from the community, as well as providing transparency. At the same time, Microsoft maintains control over the official distributions and can protect the integrity of these. It prevents unofficial modified versions from being distributed as if they were Microsoft products. From the developers’ point of view, the precompiled, production-ready object code is very easy to use through the NuGet package manager. If the more permissive MIT licensing is required, the developers can go through the extra steps of building their own versions.

Microsoft .NET Library License has restrictions that clearly separates it from open source licenses. You can only use the software as expressively permitted by the license. It is e.g., not allowed to work around any technical limitations and you can not reverse engineer and decompile it in an attempt to derive the source code. You can also not provide the software as a standalone offering.

Still, by using the MIT licensed source code (on GitHub) instead of the Microsoft provided object code (via NuGet), the software will have the properties of open source software. This source code can be modified and distributed according to the MIT license.

### Licenses for Open Content and Creative Works

There are also licenses that complement the open-source ecosystem by providing licensing solutions for creative non-software assets like documentation, media, and design. They often share the values of openness and sharing with open source software, but they are not suitable for software due to their lack of provisions for e.g., source code, patents, linking, and warranty disclaimers. Some examples include the[ GNU Free Documentation License (GFDL)](https://www.gnu.org/licenses/fdl-1.3.en.html), the[ Open Data Commons (ODC)](https://opendatacommons.org/licenses/)**,** and the[ Creative Commons](https://creativecommons.org/share-your-work/cclicenses/) license. The latter is by far the most common one, so let us look at the Creative Commons license in more detail.

#### The Creative Commons License

Creative commons is actually a set of licenses that can be built in a somewhat modular way, creating a suite of licenses. Depending on which requirements to include, the license can be made similar in spirit to both permissive and copyleft licenses, but more restrictions are possible that are not in the spirit of open source. A creative commons license will start with CC, and then be followed by abbreviations for the chosen additional requirements.

CC0 is a bit special since it is not really a license, but instead it dedicates the work to the public domain. The work can be used, copied, modified and distributed without any restrictions or attribution requirement. Different from the other Creative Common licenses, CC0 can be used also for dedicating software to the public domain.

Other than CC0, there are six Creative Commons licenses. The most permissive variant is CC-BY, which adds the requirement of attribution. Attribution here means that you need to give credit to the original creator, provide a link to the license, and indicate if changes were made. This is very similar to permissive open source licenses.

Another variant is CC BY-SA (Attribution-ShareAlike). In addition to attribution, works based on the original work must be distributed under the same license as the original. This is in turn similar to the copyleft licenses.

Different from open source licenses, Creative Commons provides the possibility to restrict the work from being used for commercial purposes. This can be achieved with CC BY-NC (Attribution-NonCommercial).

The above restrictions can also be combined into CC BY-NC-SA (Attribution-NonCommercial-ShareAlike).

It is also possible to disallow distribution of modified works, e.g., by using CC BY-ND (Attribution-NoDerivatives). In this case the work can be used for commercial purposes, but it can not be modified. Commercial use can be additionally restricted by using CC BY-NC-ND (Attribution-NonCommercial-NoDerivatives).

Note that SA and ND are mutually exclusive and can not be used together.

### Conclusion

The open source ecosystem is always in motion. We have recently seen several projects that were previously distributed under an open source license now being licensed under BSL or SSPL. New licenses are likely to emerge, covering specific use cases and restrictions that match new technology and software use. At the time of writing, the[ SPDX license list](https://spdx.org/licenses/) includes about 650 different licenses that are deemed “commonly found”. This blog post series has included only a small fraction of all these, but it still covers the vast majority of the actual licenses seen in commonly used software.
