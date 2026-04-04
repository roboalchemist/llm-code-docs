# Source: https://docs.debricked.com/opentext-core-sca-blogs/blogs/oss-licenses-part-3-permissive-licenses.md

# OSS licenses part 3: permissive licenses

> This blog was published on 7th May, 2024.

A distinguishing feature of permissive licenses is that you are allowed to do basically anything you want with the code. Most importantly, for organizations, you are allowed to reuse and distribute the code together with proprietary code.

Specifically, derivative works do not have to maintain the same license when distributed. Modifications can be licensed under another license, though *not* under *any* other license. Still, the original license text typically has to accompany the distributed work. Here we look at, and compare, the most common permissive licenses that are found in open-source software.

### BSD licenses

The BSD license is actually a set of several licenses, sometimes also including related licenses as being BSD-like (or BSD-style) in their wordings and intention. The original BSD license is the so-called BSD 4-clause license, which has later been followed by the much more popular BSD 3-clause license and the BSD 2-clause license. Other than these there are several other variants of the license.

#### BSD 4-clause license

The original BSD license consists of four clauses and is thus referred to as the[ BSD 4-clause license](https://spdx.org/licenses/BSD-4-Clause.html). It applies to redistribution and use of code and corresponding binaries. As a starting point, the license permits redistribution and use in source and binary forms, with or without modification. Then the four clauses give the conditions for this to be permitted. We can summarize the four clauses as follows.

1\. The copyright notice and the license must be included in redistribution of the code.

2\. The copyright notice and the license must be written somewhere if a binary is redistributed.

3\. All advertising material that mentions features or use of the software must acknowledge the copyright holder.

4\. The names of the copyright holders or contributors cannot be used to promote products that use the software.

The clauses are followed by a disclaimer saying that the copyright holder is not responsible for how it is used or the implications of its use.

Though the conditions are very permissive and seem straight-forward to comply with, the third clause causes problems. With many contributors, there will be many names needed in advertising material for products that somehow use the code. The clause, also called the advertising clause, further results in the license not being compatible with GPL since it adds additional restrictions that are not included in GPL. Additional restrictions are not allowed by the GPL license.

#### BSD 3-clause license

The problems with the advertisement clause in the BSD 4-clause license motivated a new license, removing this clause. This resulted in the[ BSD 3-clause license](https://spdx.org/licenses/BSD-3-Clause.html), keeping only the clauses 1, 2 and 4 from the original license, together with the disclaimer.

The removal of the advertisement clause not only made the license easier to comply with, it also made it compatible with GPL. Such compatibility makes it possible to use both GPL and BSD 3-clause licensed code in programs, assuming that the program is licensed under GPL.

Due to its history, the license is sometimes called BSD-new or modified BSD license.

#### BSD 2-clause license

An even more simplified variant of the BSD license is the[ BSD 2-clause license](https://spdx.org/licenses/BSD-2-Clause.html). Compared to the three clause license, it removes the endorsement clause. This is the fourth clause as referred to above in the 4-clause license, and the third clause in the 3-clause license. Thus, it only keeps the two clauses that requires that redistributed source code and binaries (modified or not) must keep the license text. The disclaimer is also kept. Similar to the BSD 3-clause license, the 2-clause version is compatible with GPL.

This license is used by the FreeBSD operating system and is also sometimes referred to as the FreeBSD License. It is sometimes also referred to as the Simplified BSD License, as it is a simplification of the 3-clause license.

#### Other considerations

Only referring to the BSD license should be avoided as it leaves much ambiguity. Just stating “the BSD license” often refers to the BSD 3-clause license, which can be somewhat confusing. Still, it is approved by the Open Source Initiative (BSD 4-clause is not), it is the most commonly used of the BSD licenses, and it is compatible with GPL (BSD 4-clause is not).

There is also a[ BSD 1-clause](https://spdx.org/licenses/BSD-1-Clause.html) license and a[ BSD 0-clause license](https://spdx.org/licenses/0BSD.html). The 1-clause license only keeps the first clause about retaining the copyright notice and the license for redistributed source code. The BSD 0-clause license is created to mimic the public domain. It has no clauses with conditions, but just simply states that “Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted.” The license text does not have to accompany distribution of neither source code nor binaries.

### MIT

Of the commonly used permissive licenses, the MIT license is the shortest and simplest one. The name comes from the origins at the Massachusetts Institute of Technology. It is the most common license found among those used by software on GitHub.

The license permits the licensee to do basically anything with the code. The only condition stated by the license is that the license text should be included in all copies of the software, or if a substantial part of the software is used. This is very similar to the first two clauses of the BSD licenses.

The license is also known as the expat license. The Free Software Foundation suggests that the license should be referred to as the X11 license, while the Open Source Initiative calls it the MIT license. As a middle ground, some people refer to it as the MIT X , MIT/X or MIT/X11 license. Still, MIT is the name that is most frequently encountered, and the SPDX identifier is just MIT. The license used by the X Window System only differs in that the X consortium is explicitly pointed out in the disclaimer, and that the consortium cannot be used in advertising to promote sales. This last part is very similar to the corresponding clause in the 3-Clause and 4-Clause BSD licenses.

#### Other considerations

Due to its simplicity, the MIT license does not have that many variants. One notable variant is the[ MIT-0](https://spdx.org/licenses/MIT-0.html), or MIT No Attribution license. This variant removes the (only) condition that the license text should be included in copies of the software. Thus, it only keeps the permissions granted and the disclaimer.

Compared to the BSD licenses, the MIT license makes it explicit that you can copy, modify, merge, publish, sublicence or sell copies of the software. While this is considered implicit in the BSD licenses, those licenses only explicitly permits use and redistribution of the software with or without modifications.

### Apache license

The Apache license, created by the Apache Software Foundation (ASF),  is another common permissive license.

The license has a few versions, but the Apache License 2.0 is the preferred version for most use cases. The original Apache License 1.0 from 1995 was very similar to the 4-clause BSD license, i.e., with the (problematic) advertising clause. When this clause was dropped, forming the 3-clause BSD license, the Apache license was also updated to Apache License 1.1 in 2000. This license similarly removed the advertisement clause, but kept a requirement for attributing contributors in the documentation material.

When the Apache License 2.0 was introduced in 2004 it introduced several significant changes that can not be found in the BSD licenses. Let us look at some of the most important aspects of the Apache License 2.0.

#### Patent clauses

Out of the three major permissive licenses (BSD, MIT and Apache), the Apache license is the only one to include an explicit patent clause. The clause has both a patent grant and a patent retaliation part.

The grant states that the contributors to the software grants any user a patent license. This means that if a developer adds code that is covered by any of their patents, the developer will give all licensees of the code a license for that patent. Thus, users can rest assured that their use of the software will not be subject to anyone claiming patent royalties for code they contributed. This is the narrow version of the patent grant, meaning that the grant only applies to code added by the patent holder. They do not automatically grant a patent license to other parts of the code.

The retaliation part states that anyone that initiates a patent litigation based on the software will lose their patent grants to the software.

The patent clauses in the Apache License 2.0 creates compatibility issues with GPL version 2 since they impose further restrictions on the rights than given in GPL version 2. License compatibility will be further discussed in a later post in this series.

#### Disclose changes

The Apache License 2.0 requires developers to disclose if changes have been made from the original code when it is redistributed. The modified source code itself does not have to be disclosed, but if a file has been changed, this must be stated in the file. It can be noted that the BSD licenses and the MIT license do not require this.

#### Explicit contributor license agreement clause

Anyone who contributes to an open-source project is assumed to accept that their contribution is under the same license as the project itself. The Apache License 2.0 explicitly states that all contributions fall under the license unless something else is explicitly stated. This clause aims to remove the need for a separate contributor license agreement (CLA), though there could be cases when such an agreement is still preferable.

#### Attribution notices

If the project includes a text file named NOTICE, then contributors must be attributed when the software is redistributed. Attributions can be in the file itself, the documentation or in the source files.

#### Derivative works

The Apache License 2.0 is a permissive license so work that is based on Apache licensed code can have another license. However, the situation here is a bit more involved than in e.g., the MIT or BSD licenses. Any work that is considered a derivative work must still comply with the conditions of the Apache license when distributed. This adds some restrictions to the license term you can put on derivative work. On the other hand, the definition of derivative work is quite narrow and not at all like the broad ones you see in e.g., GPL licenses. Just linking a library would not be considered derivative here, but it would be considered derivative in GPL.

#### Other considerations

Apache license 1.0 and 1.1 include non-endorsement clauses, in which you were prohibited to use “Apache” and “Apache Software Foundation” to endorse or promote products derived from the software. Similar to 2-clause BSD, this clause was removed in the Apache license 2.0.

### Conclusion

This was a brief overview of permissive licenses. For more details it is always a good idea to read the actual license texts. For the licenses discussed here, those texts are quite easy to read and they have been developed with simplicity in mind. In the next part we are going to look closer on copyleft, and in particular strong copyleft licenses, including the different versions of GPL and AGPL.
