# Adempiere Documentation

Source: https://adempiere.gitbook.io/docs/llms-full.txt

---

# ADempiere Documentation

[![Join the chat at https://gitter.im/adempiere/adempiere-documentation](https://badges.gitter.im/adempiere/adempiere-documentation.svg)](https://gitter.im/adempiere/adempiere-documentation?utm_source=badge\&utm_medium=badge\&utm_campaign=pr-badge\&utm_content=badge)

Learn, use, configure and extend a world leading open-source ERP project.

This is a collection of key documentation gathered from the ADempiere wiki and the collective experience of the ADempiere Development Community. The aim of this collection is to provide a searchable and usable source of project documentation that will improve on the data contained in the wiki while enhancing the readers experience.

The collection includes a number of books covering the main topics of:

* User Guides
* Knowledge Bases
* How To Guides
* System Administration and Configuration
* Development and Customization


# About this Documentation

Learn, use, configure and extend a world leading open-source ERP project.

This is a collection of key documentation gathered from the ADempiere wiki and the collective experience of the ADempiere Development Community. The aim of this collection is to provide a searchable and usable source of project documentation that will improve on the data contained in the wiki while enhancing the readers experience.

The collection includes a number of books covering the main topics of:

* User Guides
* Knowledge Bases
* How To Guides
* System Administration and Configuration
* Development and Customization


# Copyright

Copyright (c) 2017 ADempiere Foundation E.V and the respective authors and contributors.

Permission is granted to copy, distribute and/or modify this document under the terms of the [GNU Free Documentation License, Version 1.3](https://www.gnu.org/licenses/fdl-1.3-standalone.html) or any later version published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts. A copy of the license is included in the section entitled "[GNU Free Documentation License](https://adempiere.gitbook.io/docs/readme-1/gnu-free-documentation-license)".

Every effort is made in the preparation of these books to ensure the accuracy of the information presented. However, the information in these books is provided/sold/posted without waranty, either expressed or implied. Neither the author(s) nor ADempiere Foundation E.V. nor the ADempiere Community, its members and implementors will be held liable for any damanges caused or alledged to be caused directly or indirectly by these books.

In gathering the information, every effort has been made to retain the original author's information. Where there has been massive collaborative editing, a reference to the ADempiere wiki page has been provided. The accuracy of these attributions cannot be guaranteed. Where there are no attributions or links, the information has been rewritten extensively or is a new contribution.


# Conventions Used

Menu paths will start with the top level entry, be in bold and have the right angle separating levels: **System Admin > General Rules > System Rules**

Window and tab names will be in bold and will be followed by the word window or tab as appropriate: **Product** window

Field names in a window will be in bold italics: ***Field Name***.

Values in fields or references to items other than fields, windows, tabs and menu items will be in Italics.

Links will be in the style used by GitBook:[ About this Documentation](https://adempiere.gitbook.io/docs/readme-1).


# Contributors

* Karsten Thiemann, Schaeffer AG
* Michael McKay, McKayERP


# Version Control

The documentation collection is maintained in GitHub at [https://github.com/adempiere/adempiere-documentation](https://github.com/adempiere/admpiere-documentation). Corrections and updates can be made through pull-requests to that repository.

The goal is to maintain the set of documentation in parallel with the software so individual software releases will have corresponding documentation releases. Branches in the documentation repository will mirror the main branches in the software repository with the "master" branch being the most current release. Editing work should be done in the "develop" branch. Branches with names like "v3.9.1" will identify version releases.

To contribute, you will need an account on [GitHub](http://github.com). Fork the [ADempiere-Documentation](https://github.com/adempiere/adempiere-documentation) repository to your GitHub account.

Create or login to your account on [GitBook](https://www.gitbook.com/) and create a space linked to your GitHub fork of the ADempiere documentation. When you specify the branches to sync with your GitHub account, use the following branch names:

`master develop v* contrib*`

After GitBook has synced content with your GitHub fork, you can use GitBook to make edits in your fork. At the top left of the GitBook window, you will see the name of the branch/version you are currently reading. If you expand that drop down, a list of available versions will be shown. The version "1.0.0" is the "master" version. (You can click on a version and change its name if you wish.) Select the one version edit. When it appears, at the bottom right, click the button to edit the selected version. The list of versions should show a link with the name "Create a new release +".

![Menu to create a new release](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LKY7yW0a5Tl_ZgKLmKL%2F-LKXrH7-JuSAEvQOYTZE%2Fimage-1.png?generation=1534966629611452\&alt=media)

Select "Create a new release" and give it a name that follows the wildcard patterns, for example "contrib\_grammar". A copy of the currently selected version will be created. Make your edits and save them. Add a comment to describe the draft's changes in the space above the "draft" icon and then publish them. GitBook will sync with your GitHub repository automatically.

When you have completed all the edits and want to submit them to the main adempiere-documentation repository, go to your account on GitHub and submit a pull request from your edited version to the target version/branch in the ADempiere repository - typically "develop". When a set of edits is complete, the develop branch will be merged into the master branch and the edits will be available in the official documentation.

GitHub provides excellent documentation on making pull requests. Be sure to target the correct branch in the main repository when making the pull request.

If you run into trouble, you can delete your local GitBook version and recreate it from the data in GitHub. Just ensure all your edits are committed first.


# Getting Involved in the ADempiere Project

ADempiere is a open-source project using commons-based peer-production methods. Organized as a bazaar of Citizens, the project is governed by Technical, Functional and Community Council Teams. The intellectual property of the community is protected by the ADempiere Foundation, a non-profit group which provides legal and financial support to the community.

If you are reading this, you are already part of our community. To join our efforts all you have to do is get involved.

* Learn
  * Adopt our [Etiquette](http://wiki.adempiere.net/Etiquette) and learn about our [Community Governance Structure](http://wiki.adempiere.net/Community_Governance) and, specifically, our [Behaviour Guidelines](http://wiki.adempiere.net/Community_Governance#Behavior).
  * Read these documents
  * Read the wiki
* Connect with us, meet developers from all over the world and find answers to your questions
  * Join our chat at <http://www.adempiere.net/web/guest/chat-on-line>
  * Add topics to the forums at <http://www.adempiere.net/en/web/guest/forums>
  * Follow us on [Twitter](http://www.twitter.com/adempiere) and LinkedIn
* Contribute
  * Create a wiki account and let the tech-writer in you come alive.
  * Help test the software.
  * Fix a bug.  Check out the project issues on Github.  Choose a bug and solve it, as a good initiation to ADempiere source code and development process.
  * Get involved in [Bug Triage](http://wiki.adempiere.net/Bug_Triage)  or [ADempiere Bug Day](http://wiki.adempiere.net/ADempiere_Bug_Day)
* Donations
  * If you wish to donate money, please do so through donation to the [ADempiere Foundation](http://www.adempiere.net/en/web/guest/thefoundation), our non-profit organization based in Berlin and Canada.


# GNU Free Documentation License

Version 1.3, 3 November 2008

Copyright © 2000, 2001, 2002, 2007, 2008 Free Software Foundation, Inc. <<https://fsf.org/>>

Everyone is permitted to copy and distribute verbatim copies of this license document, but changing it is not allowed.

## 0. PREAMBLE

The purpose of this License is to make a manual, textbook, or other functional and useful document "free" in the sense of freedom: to assure everyone the effective freedom to copy and redistribute it, with or without modifying it, either commercially or noncommercially. Secondarily, this License preserves for the author and publisher a way to get credit for their work, while not being considered responsible for modifications made by others.

This License is a kind of "copyleft", which means that derivative works of the document must themselves be free in the same sense. It complements the GNU General Public License, which is a copyleft license designed for free software.

We have designed this License in order to use it for manuals for free software, because free software needs free documentation: a free program should come with manuals providing the same freedoms that the software does. But this License is not limited to software manuals; it can be used for any textual work, regardless of subject matter or whether it is published as a printed book. We recommend this License principally for works whose purpose is instruction or reference.

## 1. APPLICABILITY AND DEFINITIONS

This License applies to any manual or other work, in any medium, that contains a notice placed by the copyright holder saying it can be distributed under the terms of this License. Such a notice grants a world-wide, royalty-free license, unlimited in duration, to use that work under the conditions stated herein. The "Document", below, refers to any such manual or work. Any member of the public is a licensee, and is addressed as "you". You accept the license if you copy, modify or distribute the work in a way requiring permission under copyright law.

A "Modified Version" of the Document means any work containing the Document or a portion of it, either copied verbatim, or with modifications and/or translated into another language.

A "Secondary Section" is a named appendix or a front-matter section of the Document that deals exclusively with the relationship of the publishers or authors of the Document to the Document's overall subject (or to related matters) and contains nothing that could fall directly within that overall subject. (Thus, if the Document is in part a textbook of mathematics, a Secondary Section may not explain any mathematics.) The relationship could be a matter of historical connection with the subject or with related matters, or of legal, commercial, philosophical, ethical or political position regarding them.

The "Invariant Sections" are certain Secondary Sections whose titles are designated, as being those of Invariant Sections, in the notice that says that the Document is released under this License. If a section does not fit the above definition of Secondary then it is not allowed to be designated as Invariant. The Document may contain zero Invariant Sections. If the Document does not identify any Invariant Sections then there are none.

The "Cover Texts" are certain short passages of text that are listed, as Front-Cover Texts or Back-Cover Texts, in the notice that says that the Document is released under this License. A Front-Cover Text may be at most 5 words, and a Back-Cover Text may be at most 25 words.

A "Transparent" copy of the Document means a machine-readable copy, represented in a format whose specification is available to the general public, that is suitable for revising the document straightforwardly with generic text editors or (for images composed of pixels) generic paint programs or (for drawings) some widely available drawing editor, and that is suitable for input to text formatters or for automatic translation to a variety of formats suitable for input to text formatters. A copy made in an otherwise Transparent file format whose markup, or absence of markup, has been arranged to thwart or discourage subsequent modification by readers is not Transparent. An image format is not Transparent if used for any substantial amount of text. A copy that is not "Transparent" is called "Opaque".

Examples of suitable formats for Transparent copies include plain ASCII without markup, Texinfo input format, LaTeX input format, SGML or XML using a publicly available DTD, and standard-conforming simple HTML, PostScript or PDF designed for human modification. Examples of transparent image formats include PNG, XCF and JPG. Opaque formats include proprietary formats that can be read and edited only by proprietary word processors, SGML or XML for which the DTD and/or processing tools are not generally available, and the machine-generated HTML, PostScript or PDF produced by some word processors for output purposes only.

The "Title Page" means, for a printed book, the title page itself, plus such following pages as are needed to hold, legibly, the material this License requires to appear in the title page. For works in formats which do not have any title page as such, "Title Page" means the text near the most prominent appearance of the work's title, preceding the beginning of the body of the text.

The "publisher" means any person or entity that distributes copies of the Document to the public.

A section "Entitled XYZ" means a named subunit of the Document whose title either is precisely XYZ or contains XYZ in parentheses following text that translates XYZ in another language. (Here XYZ stands for a specific section name mentioned below, such as "Acknowledgements", "Dedications", "Endorsements", or "History".) To "Preserve the Title" of such a section when you modify the Document means that it remains a section "Entitled XYZ" according to this definition.

The Document may include Warranty Disclaimers next to the notice which states that this License applies to the Document. These Warranty Disclaimers are considered to be included by reference in this License, but only as regards disclaiming warranties: any other implication that these Warranty Disclaimers may have is void and has no effect on the meaning of this License.

## 2. VERBATIM COPYING

You may copy and distribute the Document in any medium, either commercially or noncommercially, provided that this License, the copyright notices, and the license notice saying this License applies to the Document are reproduced in all copies, and that you add no other conditions whatsoever to those of this License. You may not use technical measures to obstruct or control the reading or further copying of the copies you make or distribute. However, you may accept compensation in exchange for copies. If you distribute a large enough number of copies you must also follow the conditions in section 3.

You may also lend copies, under the same conditions stated above, and you may publicly display copies.

## 3. COPYING IN QUANTITY

If you publish printed copies (or copies in media that commonly have printed covers) of the Document, numbering more than 100, and the Document's license notice requires Cover Texts, you must enclose the copies in covers that carry, clearly and legibly, all these Cover Texts: Front-Cover Texts on the front cover, and Back-Cover Texts on the back cover. Both covers must also clearly and legibly identify you as the publisher of these copies. The front cover must present the full title with all words of the title equally prominent and visible. You may add other material on the covers in addition. Copying with changes limited to the covers, as long as they preserve the title of the Document and satisfy these conditions, can be treated as verbatim copying in other respects.

If the required texts for either cover are too voluminous to fit legibly, you should put the first ones listed (as many as fit reasonably) on the actual cover, and continue the rest onto adjacent pages.

If you publish or distribute Opaque copies of the Document numbering more than 100, you must either include a machine-readable Transparent copy along with each Opaque copy, or state in or with each Opaque copy a computer-network location from which the general network-using public has access to download using public-standard network protocols a complete Transparent copy of the Document, free of added material. If you use the latter option, you must take reasonably prudent steps, when you begin distribution of Opaque copies in quantity, to ensure that this Transparent copy will remain thus accessible at the stated location until at least one year after the last time you distribute an Opaque copy (directly or through your agents or retailers) of that edition to the public.

It is requested, but not required, that you contact the authors of the Document well before redistributing any large number of copies, to give them a chance to provide you with an updated version of the Document.

## 4. MODIFICATIONS

You may copy and distribute a Modified Version of the Document under the conditions of sections 2 and 3 above, provided that you release the Modified Version under precisely this License, with the Modified Version filling the role of the Document, thus licensing distribution and modification of the Modified Version to whoever possesses a copy of it. In addition, you must do these things in the Modified Version:

* A. Use in the Title Page (and on the covers, if any) a title distinct from that of the Document, and from those of previous versions (which should, if there were any, be listed in the History section of the Document). You may use the same title as a previous version if the original publisher of that version gives permission.
* B. List on the Title Page, as authors, one or more persons or entities responsible for authorship of the modifications in the Modified Version, together with at least five of the principal authors of the Document (all of its principal authors, if it has fewer than five), unless they release you from this requirement.
* C. State on the Title page the name of the publisher of the Modified Version, as the publisher.
* D. Preserve all the copyright notices of the Document.
* E. Add an appropriate copyright notice for your modifications adjacent to the other copyright notices.
* F. Include, immediately after the copyright notices, a license notice giving the public permission to use the Modified Version under the terms of this License, in the form shown in the Addendum below.
* G. Preserve in that license notice the full lists of Invariant Sections and required Cover Texts given in the Document's license notice.
* H. Include an unaltered copy of this License.
* I. Preserve the section Entitled "History", Preserve its Title, and add to it an item stating at least the title, year, new authors, and publisher of the Modified Version as given on the Title Page. If there is no section Entitled "History" in the Document, create one stating the title, year, authors, and publisher of the Document as given on its Title Page, then add an item describing the Modified Version as stated in the previous sentence.
* J. Preserve the network location, if any, given in the Document for public access to a Transparent copy of the Document, and likewise the network locations given in the Document for previous versions it was based on. These may be placed in the "History" section. You may omit a network location for a work that was published at least four years before the Document itself, or if the original publisher of the version it refers to gives permission.
* K. For any section Entitled "Acknowledgements" or "Dedications", Preserve the Title of the section, and preserve in the section all the substance and tone of each of the contributor acknowledgements and/or dedications given therein.
* L. Preserve all the Invariant Sections of the Document, unaltered in their text and in their titles. Section numbers or the equivalent are not considered part of the section titles.
* M. Delete any section Entitled "Endorsements". Such a section may not be included in the Modified Version.
* N. Do not retitle any existing section to be Entitled "Endorsements" or to conflict in title with any Invariant Section.
* O. Preserve any Warranty Disclaimers.

If the Modified Version includes new front-matter sections or appendices that qualify as Secondary Sections and contain no material copied from the Document, you may at your option designate some or all of these sections as invariant. To do this, add their titles to the list of Invariant Sections in the Modified Version's license notice. These titles must be distinct from any other section titles.

You may add a section Entitled "Endorsements", provided it contains nothing but endorsements of your Modified Version by various parties—for example, statements of peer review or that the text has been approved by an organization as the authoritative definition of a standard.

You may add a passage of up to five words as a Front-Cover Text, and a passage of up to 25 words as a Back-Cover Text, to the end of the list of Cover Texts in the Modified Version. Only one passage of Front-Cover Text and one of Back-Cover Text may be added by (or through arrangements made by) any one entity. If the Document already includes a cover text for the same cover, previously added by you or by arrangement made by the same entity you are acting on behalf of, you may not add another; but you may replace the old one, on explicit permission from the previous publisher that added the old one.

The author(s) and publisher(s) of the Document do not by this License give permission to use their names for publicity for or to assert or imply endorsement of any Modified Version.

## 5. COMBINING DOCUMENTS

You may combine the Document with other documents released under this License, under the terms defined in section 4 above for modified versions, provided that you include in the combination all of the Invariant Sections of all of the original documents, unmodified, and list them all as Invariant Sections of your combined work in its license notice, and that you preserve all their Warranty Disclaimers.

The combined work need only contain one copy of this License, and multiple identical Invariant Sections may be replaced with a single copy. If there are multiple Invariant Sections with the same name but different contents, make the title of each such section unique by adding at the end of it, in parentheses, the name of the original author or publisher of that section if known, or else a unique number. Make the same adjustment to the section titles in the list of Invariant Sections in the license notice of the combined work.

In the combination, you must combine any sections Entitled "History" in the various original documents, forming one section Entitled "History"; likewise combine any sections Entitled "Acknowledgements", and any sections Entitled "Dedications". You must delete all sections Entitled "Endorsements".

## 6. COLLECTIONS OF DOCUMENTS

You may make a collection consisting of the Document and other documents released under this License, and replace the individual copies of this License in the various documents with a single copy that is included in the collection, provided that you follow the rules of this License for verbatim copying of each of the documents in all other respects.

You may extract a single document from such a collection, and distribute it individually under this License, provided you insert a copy of this License into the extracted document, and follow this License in all other respects regarding verbatim copying of that document.

## 7. AGGREGATION WITH INDEPENDENT WORKS

A compilation of the Document or its derivatives with other separate and independent documents or works, in or on a volume of a storage or distribution medium, is called an "aggregate" if the copyright resulting from the compilation is not used to limit the legal rights of the compilation's users beyond what the individual works permit. When the Document is included in an aggregate, this License does not apply to the other works in the aggregate which are not themselves derivative works of the Document.

If the Cover Text requirement of section 3 is applicable to these copies of the Document, then if the Document is less than one half of the entire aggregate, the Document's Cover Texts may be placed on covers that bracket the Document within the aggregate, or the electronic equivalent of covers if the Document is in electronic form. Otherwise they must appear on printed covers that bracket the whole aggregate.

## 8. TRANSLATION

Translation is considered a kind of modification, so you may distribute translations of the Document under the terms of section 4. Replacing Invariant Sections with translations requires special permission from their copyright holders, but you may include translations of some or all Invariant Sections in addition to the original versions of these Invariant Sections. You may include a translation of this License, and all the license notices in the Document, and any Warranty Disclaimers, provided that you also include the original English version of this License and the original versions of those notices and disclaimers. In case of a disagreement between the translation and the original version of this License or a notice or disclaimer, the original version will prevail.

If a section in the Document is Entitled "Acknowledgements", "Dedications", or "History", the requirement (section 4) to Preserve its Title (section 1) will typically require changing the actual title.

## 9. TERMINATION

You may not copy, modify, sublicense, or distribute the Document except as expressly provided under this License. Any attempt otherwise to copy, modify, sublicense, or distribute it is void, and will automatically terminate your rights under this License.

However, if you cease all violation of this License, then your license from a particular copyright holder is reinstated (a) provisionally, unless and until the copyright holder explicitly and finally terminates your license, and (b) permanently, if the copyright holder fails to notify you of the violation by some reasonable means prior to 60 days after the cessation.

Moreover, your license from a particular copyright holder is reinstated permanently if the copyright holder notifies you of the violation by some reasonable means, this is the first time you have received notice of violation of this License (for any work) from that copyright holder, and you cure the violation prior to 30 days after your receipt of the notice.

Termination of your rights under this section does not terminate the licenses of parties who have received copies or rights from you under this License. If your rights have been terminated and not permanently reinstated, receipt of a copy of some or all of the same material does not give you any rights to use it.

## 10. FUTURE REVISIONS OF THIS LICENSE

The Free Software Foundation may publish new, revised versions of the GNU Free Documentation License from time to time. Such new versions will be similar in spirit to the present version, but may differ in detail to address new problems or concerns. See <https://www.gnu.org/licenses/>.

Each version of the License is given a distinguishing version number. If the Document specifies that a particular numbered version of this License "or any later version" applies to it, you have the option of following the terms and conditions either of that specified version or of any later version that has been published (not as a draft) by the Free Software Foundation. If the Document does not specify a version number of this License, you may choose any version ever published (not as a draft) by the Free Software Foundation. If the Document specifies that a proxy can decide which future versions of this License can be used, that proxy's public statement of acceptance of a version permanently authorizes you to choose that version for the Document.

## 11. RELICENSING

"Massive Multiauthor Collaboration Site" (or "MMC Site") means any World Wide Web server that publishes copyrightable works and also provides prominent facilities for anybody to edit those works. A public wiki that anybody can edit is an example of such a server. A "Massive Multiauthor Collaboration" (or "MMC") contained in the site means any set of copyrightable works thus published on the MMC site.

"CC-BY-SA" means the Creative Commons Attribution-Share Alike 3.0 license published by Creative Commons Corporation, a not-for-profit corporation with a principal place of business in San Francisco, California, as well as future copyleft versions of that license published by that same organization.

"Incorporate" means to publish or republish a Document, in whole or in part, as part of another Document.

An MMC is "eligible for relicensing" if it is licensed under this License, and if all works that were first published under this License somewhere other than this MMC, and subsequently incorporated in whole or in part into the MMC, (1) had no cover texts or invariant sections, and (2) were thus incorporated prior to November 1, 2008.

The operator of an MMC Site may republish an MMC contained in the site under CC-BY-SA on the same site at any time before August 1, 2009, provided the MMC is eligible for relicensing.


# Glossary

## Accounting Dimension

An Accounting Dimension is a value that is included in the Accounting Facts. The value is drawn from a field on a document when the document is posted. Typical Accounting Dimensions in ADempiere include the Client, Organization, Business Partner, Product, Project, Campaign, and Activity. The Accounting Dimensions are defined in the [**Accounting Dimension**](https://adempiere.github.io/functional-guide/window/window-accounting-dimensions.html) window.

## Accounting Facts

An Accounting Fact or just Fact is the results of a document posting. It includes all the information about the accounts and Dimensions used and the debit/credit information. The Facts are the basis of financial reports and can be traced back to the documents that created them. Facts are also referred to as Accounting Consequences.

## AD

Short form for the [**A**pplication **D**ictionary](https://adempiere.gitbook.io/docs/system-administration/the-application-dictionary)**.**

## Application Dictionary

A collection of meta-data that defines the look and behavior of the application.  Nearly every aspect of the ADempiere interface and functionality is defined by the Application Dictionary.  The application can also be easily extended with new functionality by adding to the Application Dictionary.  Also referred to as simply the "AD".

## Application Server

A software program running on a server that provides a web interface or access to a Java Client. The Application Server also performs system and client processes as required - for example, the off-line posting of documents.

## Client

A Client is the highest level business entity in the ADempiere Application. It represents the entire business and may include one or more Organizations as separate legal entities or departments. Client data can not be shared with other Clients.

ADempiere is a multi-tenant system. Client data and the application that uses it are hosted on a server as a tenant and there can be multiple tenants on a server.

A Client is not to be confused with the [Java Client](#java-client), a Java software application that runs on a local computer and communicates with the Application Server to access data.

## Client Administrator

A Client Administrator is a User logged into a Role that provides administrative control of the Client. The Client Administrator's main function is to define the Roles and rule used by the Client. Client Administrators can only affect their Client.

## Combination

The set of Accounting Dimensions used in generating an Accounting Fact. For accounting systems that don't use dimensions, the Combination is equivalent to the account number. For ADempiere, the Combination uses the account number plus a number of additional Accounting Dimensions. The Combinations keep the actual account number simpler - for example, you don't have to have a revenue account for each particular product. They also make reporting by Accounting Dimension simpler.

## Commitment Accounting

A type of accounting that creates Accounting Facts for Sales or Purchase Orders and similar documents to record the legal/financial commitment that the Order represents. Commitment Accounting is controlled in the **System Configurator** window and the default is not to use it.

## Dunning

The process of making repeated and insistent demands upon a customer, especially for the payment of a debt.

## Dunning Run

A collection of information and also the process of collecting information for the purposes of Dunning.

## Entity Type

An entity type defines the "entity" or owner of a particular entry in the Application Dictionary.  The owner has responsiblity for the entry.  Entity Types "Dictionary" and "Adempiere" are reserved for the application developers and all Application Dictionary entries using these Entity Types will be overwritten every time the application is migrated to a new version.

## Identifier

See [Record Identifiers](#record-identifiers).

## Integrator

A person or company who is involved in the customization, installation and configuration of the ADempiere software. Integrators are typically consultants who are not involved in the day-to-day operation of the system but who played a role in the adoption of the software at a particular company.

## Java Client

A Java Client is a stand-alone software application that runs on the local computer. Unlike a web-based application, a Java Client does not require a browser but it may communicate with a server over a network.

## Record Identifiers

When a field displays information linked to another window or tab, for example a ***Product*** field in a Sales **Order Line**, the ***Product*** field is displayed using an Identifier that can include one or more fields from the **Product** window. These fields are selected and given a sequence by the System Administrator. The default is often \<Search Key>\_\<Name> but it can be configured to include other useful fields.

For System Administrators, the identifier is the collection of fields used in a Table Direct reference of an ID field. The fields used and their sequence are selected from the Table and Column window, Column tab. Typical usage would be \<Search Key>\_\<Name>.

## Role

A security measure that limits the possible actions and access of a User to their intended function. When a User logs in to the application, they log in to a particular Role. Roles are defined and managed by Client Administrators.

## System Administrator

A particular User and Role in ADempiere that can define how the application behaves, what data is shown and how it is used. The System Administrator creates Clients and supports all Clients on a server but is not able to access the Client's data. Each Client can also have Roles with Administrative privileges but these are restricted to the Client and can not affect other Clients on the server.

## User

A person who is logged in to the application. Users are defined by the Client Administrator. Users may be associated with a Business Partner Contact and are typically assigned specific Roles and Organizational access.


# User Guide

Instruction and hints on the use of the ADempiere software

### About this Guide

The ADempiere Users Guide provides instructions and hints on the use of the software in day-to-day operation. It is intended as a reference on how to use the software to perform general functions. It includes configuration information where this is in the realm of the end-user. More complex configuration information can be found in the System Administration Guide or the Development Guide.

### About the ADempiere Application

ADempiere is a world-class ERP software application designed to support:

* **Multiple Organizations within the Enterprise**

  ADempiere can have multiple branch offices and companies in one single installation, making it especially attractive in large franchises where consolidation of financial and operational data is critical.
* **Multiple Languages across the Enterprise and its Customers**

  All user and customer-facing information can be presented in multiple languages. This, along with Multiple Organizations, makes Adempiere especially attractive for companies with branches in areas of different languages.
* **Multiple Accounting Formats**

  The accounting data can be managed and presented with multiple accounting schemas making the ADempiere application especially suited to the multi-national environment.
* **Multiple Operating Systems**

  Having been developed in Java, the applicaiton is able to run on most operating systems.
* **Complex Workflows**

  ADempiere provides workflows from simple documents, to multi-level approval and automated processing that can be fully customized to any business process.

The application supports all the main features and functions expected of an ERP system and allows for the customization of the software so company specific features can be easily added. As an end-user, you will likely be presented with a customized version of the software, specific to your business. Information on those customizations will be provided to you by your system provider or administrator. This guide covers the ADempiere application in its released configuration and uses the Garden World demo client for examples.

## Launching the Application

There are two ways of accessing the ADempiere Application: through a java software client that runs on the user's computer or through a web user interface (webui) which can be accessed through a browser. Both these applications communicate with the ADempiere Application Server. Which you use will be determined by your system implementation. In general, the two methods are similar and provide the same functionality. The Users Guide will focus on the Client software and will discuss the web version where it differs.

#### Launching the ADempiere Client using Web Start

To launch using Web Start, you will need the ADempiere Application Server URL. It may be provided as a link on your company's intranet or you can ask the System Administrator. It may look like <http://mycompany.com:8088/admin>.

Open the Application Server URL. It will look something like the following image.

![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LKY7yW0a5Tl_ZgKLmKL%2F-LKY7zFyLpezTSfuTFKD%2Fimage_appserver_admin%20\(1\).png?generation=1534966630340158\&alt=media)

The WebStart option automatically makes sure that the your computer will use the latest version of the ADempiere Client.

From the Application Server web page, click on the blue WebStart button and you will see the WebStart Dialog:

![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LJxc0hBdvotIr8-V10n%2F-LJxc1XrF1LNZtbIBpDd%2FWebstart_download_progress.jpg?generation=1534337236613053\&alt=media)

Note: If the application client does not start immediately after this, you may need to ask your System Administrator to ensure the java JNLP file is associated with the Java Web Starter application (javaws).

If a security window appears, click on "Always trust content from this publisher".

The very first time the application starts, you will see a license dialog. Accept the license terms.

The application client should start at this point and present a log in dialog.


# Getting Started

Helpful advice and an introduction to first time users of the ADempiere application.

Welcome to the ADempiere application! You are about to experience a full featured Enterprise Resource Planning (ERP) System. As an enterprise system, it provides companies with a means to manage their processes, record data, report on that data and make better decisions. Its a complex business so be forewarned - this is a beast of an application and there is lots to learn.

While the software developers endeavor to make things as simple as possible, businesses are necessarily complex and the software has to match that complexity. Every business is also different and the processes that work in one company, may not be appropriate for another. In ADempiere, almost all parts of the application can be customized. If you are working with an installed version of the software, its likely that the System Administrators and Integrators responsible for it have developed numerous customized workflows, processes, reports and what not. You will likely receive specialized training on these things.

This guide is based on the core software as it exists out of the box. There are a few key concepts to learn that will apply to most processes. Once you understand these, you should be able to find your way around without too much difficulty.

If you get lost or don't understand something, don't hesitate to reach out on the community chat (<http://adempiere.net/web/guest/chat-on-line>).

Lets get started!


# About the Application

ADempiere is a world-class ERP software application designed to support:

* **Multiple Organizations within the Enterprise**

  ADempiere can have multiple branch offices and companies in one single installation, making it especially attractive in large franchises where consolidation of financial and operational data is critical.
* **Multiple Languages across the Enterprise and its Customers**

  All user and customer-facing information can be presented in multiple languages. This, along with Multiple Organizations, makes Adempiere especially attractive for companies with branches in areas of different languages.
* **Multiple Accounting Formats**

  The accounting data can be managed and presented with multiple accounting schema making the ADempiere application especially suited to the multi-national environment.
* **Multiple Operating Systems**

  Having been developed in Java, the application is able to run on most operating systems.
* **Complex Workflows**

  ADempiere provides workflows from simple documents, to multi-level approval and automated processing that can be fully customized to any business process.

The application supports all the main features and functions expected of an ERP system and allows for the customization of the software so company specific features can be easily added.


# Launching the Application

There are two ways of accessing the ADempiere application: through a java software client that runs on the user's computer or through a web user interface (webui) which can be accessed through a browser. Both these applications communicate with the ADempiere Application Server. Which you use will be determined by your system implementation. In general, the two methods are similar and provide the same functionality. The User Guide will focus on the java client and will discuss the web version where it differs.

## Launching the ADempiere JAVA Client using Web Start

To launch the application, you will need the ADempiere Application Server URL. It may be provided as a link on your company's intranet or you can ask the System Administrator. It may look like

```
http://mycompany.com:8088/admin
```

Open the Application Server URL. It will look something like the following image.

![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LKYc5kZmAN3DUIAq3t5%2F-LKYc6_5l1Uf7JaZlH7P%2Fimage_appserver_admin%20\(1\).png?generation=1534974787327720\&alt=media)

The WebStart option automatically makes sure that the your computer will use the latest version of the ADempiere JAVA Client.

From the Application Server web page, click on the blue WebStart button and you will see the WebStart Dialog:

![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LJxc0hBdvotIr8-V10n%2F-LJxc1XrF1LNZtbIBpDd%2FWebstart_download_progress.jpg?generation=1534337236613053\&alt=media)

{% hint style="info" %}
If the application Java Client does not start immediately after this, you may need to ask your System Administrator to ensure the Java JNLP file is associated with the Java Web Starter application (javaws).
{% endhint %}

If a security window appears, click on "Always trust content from this publisher".

The very first time the application starts, you will see a license dialog. Accept the license terms.

The application client should start at this point and present a log in dialog. See [Logging In](https://adempiere.gitbook.io/docs/introduction/getting-started/logging-in) for more information.

## Accessing the Web Application

To log in to the Web Application, click the link for the **ADempiere ZK Webui** in the administration page above. You may also have been given the address directly. It will look something line this:

```
http://mycompany.com:8088/webui
```

The web page shown will be the login page to the Web Application running on the server. See [Logging In](https://adempiere.gitbook.io/docs/introduction/getting-started/logging-in) for more information.


# Logging In

The Log In process is similar to both the Java Client and the Web Application. Each is discussed below. The default users and passwords are the same.

### **Default Users and Passwords**

The following Users and passwords are part of the initial seed database:

| For ...                              | **Log in as User ID...** | **With Password...** |
| ------------------------------------ | ------------------------ | -------------------- |
| System Management                    | System                   | System               |
| System Management or any role/Client | SuperUser                | System               |
| Sample Client Administration         | GardenAdmin              | GardenAdmin          |
| Sample Client User                   | GardenUser               | GardenUser           |

The System and SuperUser User accounts are used to manage the system. For first time use, try the GardenAdmin User account which will access the Garden World demonstration client.

For more information about using the Garden World Client when you first log on, see the page on [Garden World](http://wiki.adempiere.net/Garden_World) and its initial setup.

## Java Client

### The Login Dialog

After [Launching the ADempiere Application](https://adempiere.gitbook.io/docs/introduction/getting-started/launching-the-application) the login dialog will appear. This dialog has two tabs, a [Connection Tab](#connection-tab) and a [Default Tab](#defaults-tab). Before you can set the defaults, you must complete the connection by logging in. Enter you user name and password and click the green check mark ( ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ91Z9iE_zlndNxTU%2Fok24.gif?generation=1550287155741996\&alt=media) ) called "Confirm". If you don't have a user name, you can use one of the default names as shown below. For the first time, just confirm the defaults that appear and move on to [Finding Your Way Around](https://adempiere.gitbook.io/docs/introduction/getting-started/finding-your-way-around).

{% hint style="info" %}
The icons ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ91a8kKlMklOa3NB%2Fok16.gif?generation=1550287155453533\&alt=media) and ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ91c9usXDA31xOdX%2Fcancel16.gif?generation=1550287154974361\&alt=media) at the bottom of each page will confirm/process or cancel the dialog respectively.
{% endhint %}

### Connection Tab

![ADempiere Login Connection Tab](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZ5G1bjZ0BFZHjQciW2%2F-LZ5G44Nz-zWpr_TadqR%2Fimage%20\(2\).png?generation=1550588336575832\&alt=media)

| **Field** | **Description**                                                                                                                                                           |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Server    | This field is for reference. You can change the definition of the server if you click in the field. This will bring the [**Connection Test Dialog**](#connection-test) up |
| User ID   | Fill in with the user ID provided for you. There are a few defaults mentioned above.                                                                                      |
| Password  | Fill in with the password provided for you. Again, the defaults are above.                                                                                                |
| Language  | Select the language you wish to use. The change is immediate.                                                                                                             |

{% hint style="info" %}
Note that it is not possible to request a new password when using the Java Client application. If you forgot your password, please contact an Administrator for your Client to have it reset.
{% endhint %}

The first field called Server shows which server and database you are connected to. The Server field highlights the status of the application server and database that will be used. It indicates this status with a red background if either:

* the database service is not available or the connection information is incorrect or the connection hasn't been initiated; and
* the application server is not running of the connection information is incorrect.

If only one of the the application server or database service is the cause of the problem, the icons on the right and left of the field will appear red. For example, in the image above, the database icon is red indicating, in this case, that the database connection hasn't been attempted yet. If both the application server and database connection have issues, the entire field will be red.

When launching the client, the initiation process tests the application server status but not the database connection. The Server field will show the database with a red background as in the diagram above. This is normal. Once you enter the user name and password, the connection is established. The delay in the database connection allows you to change the database during the log-in process.

Click in the Server field to go to the Connection Test Dialog to diagnose the problem causing red backgrounds in the field or to change the database parameters.

{% hint style="info" %}
The Client will still operate if the database is available but the application server is not running.
{% endhint %}

### Defaults Tab

![ADempiere Login Window - Defaults Tab](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LKCEAIzH4FqGSKfo3Je%2F-LKCHlhnnhUppmxE48Pm%2FLogin_Defaults.jpg?alt=media\&token=f42187a9-489f-4f74-853c-ce7e16819f91)

After selecting the desired values in this tab, you can click on the green check mark to start the application. See [Finding Your Way Around the Client](https://adempiere.gitbook.io/docs/introduction/getting-started/finding-your-way-around).

| **Field**    | **Description**                                                                                                               |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| Role         | Select the role to work on ADempiere. The list is filled with the roles allowed for the user                                  |
| Client       | Select the client/company to work on ADempiere. The list is filled with the companies allowed for the role                    |
| Organization | Select the default organization to work on ADempiere. The list is filled with the organizations allowed for the role and user |
| Warehouse    | Select the default warehouse to use for this session                                                                          |
| Date         | Fill in the default date to keep while working on ADempiere                                                                   |
| Printer      | Select the default printer to work on ADempiere                                                                               |

### Connection Test Dialog

When you click in the Server field in the Connection tab of the login dialog, the Connection Test dialog appears. Note that this window is intended for system administrators. As a user, you should not need to look at it.

![Connection Test Dialog](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LKCEAIzH4FqGSKfo3Je%2F-LKCIJO6JzZqzl9MD0NT%2FLogin_Connection_test.jpg?alt=media\&token=3c025f37-223f-4e3c-896d-ef2b282194c9)

{% hint style="info" %}
Please talk with your system administrator if you don't know how to manage this window. In order to use the Connection Test Dialog, the ADempiere Application Server must be running and the database service must be available.
{% endhint %}

| **Field**               | **Description**                                                                                                          |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Name                    | The name of the connection is generated automatically by Adempiere                                                       |
| Application Host        | Fill in with the hostname or IP address of the JBoss Adempiere server                                                    |
| Application Port        | Fill in with the port for the JBoss Adempiere server, normally 1099                                                      |
| Connection              | Select the connection type from the list, provided are LAN, Terminal Server, VPN and WAN. Normally LAN can work for you. |
| Overwrite               | Check here if you need to overwrite the database definition provided by the JBoss Adempiere server                       |
| Test Application Server | Click this button to test the JBoss Adempiere server and get the database information from there                         |
| Database Type           | Select the database type, provided are Oracle, DB2, PostgreSQL, Fyracle                                                  |
| Database Host           | Fill in with the hostname or IP address of the database server                                                           |
| Database Port           | Fill in with the port provided to connect to database                                                                    |
| Database Name           | Fill in with the database name (instance for Oracle)                                                                     |
| User                    | Fill in with the database user owner of Adempiere schema                                                                 |
| Password                | Fill in with the database password                                                                                       |
| via Firewall            | Check here if you need to connect via Firewall (only for Oracle connection)                                              |
| Firewall Host           | Fill in with the hostname or IP address provided for the firewall                                                        |
| Firewall Port           | Fill in with the port provided for the firewall                                                                          |
| Test Database           | Click this button to check the database connection                                                                       |

Once all the tests are complete, click the green check mark to return to the Defaults Tab.

## WEB Application

The Web Application launch is simpler than the JAVA Client as there is no need to verify the connection with the server. After Launching the Web Application you will be presented with a login dialog as shown below.

![ADempiere Web Application Login](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ91gm4AKB6f_50W8%2Fwebui_login.PNG?generation=1550287155300018\&alt=media)

The login fields are pretty self-explanatory:

| **Field**        | **Description**                                                                                                                                                                                                                                                                                             |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| User ID          | Fill in with the user ID provided for you. There are a few defaults mentioned above.                                                                                                                                                                                                                        |
| Password         | Fill in with the password provided for you. Again, the defaults are above.                                                                                                                                                                                                                                  |
| Language         | Select the language you wish to use. The change is immediate.                                                                                                                                                                                                                                               |
| Remember Me      | Check if you wish the Login Dialog to remember your entries the next time you access the Web Application.  This option will only appear if allowed in your implementation.                                                                                                                                  |
| Forgot Password? | Click this link if you have forgotten your password.  A dialog will be presented where you can enter your User ID and submit the request to have the password reset.  You will receive an email with a link to a page where you can reset your password.  The email link will be active for only 5 minutes. |

After you click the Confirm button, the dialog will change to allow the selection of the Role, Client, Organization and Warehouse.

![Role Login Dialog](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ91iNEy4j961fvfZ%2Fwebui_login_roles.PNG?generation=1550287156164081\&alt=media)

The Roles available to the User will determine the Client and possibly the Organization and Warehouse. The first time the user logs in, the ***Default*** Role (as defined in the **User Assignment** tab of the **Role** window or **User Roles** tab of the **User** window) will be selected. From then on, the Role selected on the last login will be the default.

{% hint style="info" %}
If there is only one Role available to the User and the System is configured to only show multiple roles, the Role combo box may not be displayed in the dialog.
{% endhint %}

After selecting the Role, Client, Organization and Warehouse, click the Confirm button to complete the login. See [Finding Your Way Around the Web App](https://adempiere.gitbook.io/docs/introduction/getting-started/finding-your-way-around-the-web-app).


# Finding Your Way Around the Java Client

This page describes the structure of the Java Client and how to find information.

Once you log in, you will be presented with a window that may have three or four tabs as shown below. If performance measures are defined, the Performance tab will be visible and shown. Otherwise, the first tab displayed will be the Menu.

![The initial window showing the performance measures.](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZ5G1bjZ0BFZHjQciW2%2F-LZ5G3vOTXFDMd8x792u%2Fimage%20\(7\).png?generation=1550588337028442\&alt=media)

Some things to note as you look at the window for the first time:

* The title bar at the top show who is logged in and what they are logged in to.  This is important where there are several possible databases. For example a sandbox database you can "play" in and the production database where things are serious.  A quick look at the title bar will prevent you from spending hours working on data in the wrong database. The format of the information is
  * User name ( Role) @ the client . the organization  | The app server {The database server,  the database name, the database user}
* Below the title bar is the [Application Menu](https://adempiere.gitbook.io/docs/introduction/getting-started/finding-your-way-around/adempiere-application-menu).
* The status bar at the bottom of the window provides hints on what to do and the results of what you did.
* Above the status bar are two buttons: Notice; and Requests.  Notices are internal messages from the system advising the user that something needs their attention.  Requests are typically from a customer and are a request for some sort of action or service.  The number beside each shows the number of active items.
* To the right of the buttons is a status indicator showing the amount of memory currently in use and the percentage of what is available.
* Above the graphs is a white space which can be used to post company notices and other information relevant to the users of the application.

The other three tabs besides the Performance tab are:

* Menu - the main menu of the system
* Workflow Activities - where administrators can mange the workflows and track their completion.  The number shows the number of workflows that are active; and
* Workflow - where a particular workflow can be visualized.

These tabs will be discussed in detail in the following pages.


# The Application Menu

The main application menu

## The Application Menu   <a href="#firstheading" id="firstheading"></a>

![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5e2MuJPHVmFRxnu%2Fapplicationmenu.PNG?generation=1550287164421642\&alt=media)

The Application Menu appears at the top of most windows in the ADempiere Java Client. The number of menu items varies depending on the type of window currently open. Its structure is similar to most applications.

For reference, the following list contains all the options that will appear in the Application Menu:

| Icon                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Menu                                                                                             | Description                                                                                                                                                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **File**                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                  |                                                                                                                                                                                                                                                                                                                                     |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5FJUSK34xrSCJoz%2Fprintscreen24.gif?generation=1550287160138645\&alt=media)                                                                                                                                                                                                                                                          | Print Screen                                                                                     | Prints the current computer screen to the default printer.                                                                                                                                                                                                                                                                          |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5e68-sT24JYK-8a%2Fscreenshot24.gif?generation=1550287166643683\&alt=media)                                                                                                                                                                                                                                                           | Screen Shot                                                                                      | Copy the current window to the clipboard.                                                                                                                                                                                                                                                                                           |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5e8-pyBgh7_a0BK%2Freport24.png?generation=1550287164025459\&alt=media)                                                                                                                                                                                                                                                               | Report                                                                                           | Previews a report based on the current record. See [Report](http://wiki.adempiere.net/Report) for more information.                                                                                                                                                                                                                 |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5FHgOpXUco2tIrA%2Fprint24.gif?generation=1550287147988429\&alt=media)                                                                                                                                                                                                                                                                | Print                                                                                            | Prints a predefined report based on the current record. See [Printing and Print Preview](http://wiki.adempiere.net/Printing_and_Print_Preview) for more information.                                                                                                                                                                |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5eCjsASII9CiQIL%2Fprintpreview24.gif?generation=1550287162047761\&alt=media)                                                                                                                                                                                                                                                         | Print Preview                                                                                    | Displays a preview of a predefined report based on the current record. See [Printing and Print Preview](http://wiki.adempiere.net/Printing_and_Print_Preview) for more information.                                                                                                                                                 |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5eENIG9qxf1DC7R%2Fexport24.gif?generation=1550287162464856\&alt=media)                                                                                                                                                                                                                                                               | Export                                                                                           | Export all displayed records to an external spreadsheet (\*.xls) file. Not just the current record, but all records in the current window. The number of records can be adjusted by the [Lookup](http://wiki.adempiere.net/Lookup) function.                                                                                        |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5eGQUsVhGkUf1Pi%2Fend24.gif?generation=1550287163588736\&alt=media)                                                                                                                                                                                                                                                                  | eXit Window                                                                                      | Close the current window. In the main application window, this will close the application.                                                                                                                                                                                                                                          |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5eIi0O7xQqtsQeo%2Flogout24.png?generation=1550287165038105\&alt=media)                                                                                                                                                                                                                                                               | Log Out                                                                                          | Log out of the application and open the log-in screen                                                                                                                                                                                                                                                                               |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5eK6nVkZYIVmeAo%2Fexit24.gif?generation=1550287167007014\&alt=media)                                                                                                                                                                                                                                                                 | Exit Application                                                                                 | Exit the application entirely.                                                                                                                                                                                                                                                                                                      |
| **Edit**                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                  |                                                                                                                                                                                                                                                                                                                                     |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5eMWPMBA1FXSXLx%2Fnew24.gif?generation=1550287167308660\&alt=media)                                                                                                                                                                                                                                                                  | New Record                                                                                       | Creates a new record. Required fields will have red backgrounds which turn to blue once they are filled.                                                                                                                                                                                                                            |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5eOv7giyEZZ7sK6%2Fsave24.gif?generation=1550287167091193\&alt=media)                                                                                                                                                                                                                                                                 | Save changes                                                                                     | Saves any changes to the current record.                                                                                                                                                                                                                                                                                            |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5eQvKdSfG7hfqwj%2Fcopy24.gif?generation=1550287166227839\&alt=media)                                                                                                                                                                                                                                                                 | Copy Record                                                                                      | Creates a copy of the current record. Only the record is copied, not the lower level tabs.                                                                                                                                                                                                                                          |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5F-xfae5uDfUEbu%2Fdelete24.gif?generation=1550287148364679\&alt=media)                                                                                                                                                                                                                                                               | Delete Record                                                                                    | Deletes the current record.                                                                                                                                                                                                                                                                                                         |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5eUIu5jkeiS6XBs%2Fdeleteselection24.gif?generation=1550287166421656\&alt=media)                                                                                                                                                                                                                                                      | Delete Selected Records                                                                          | Opens a dialog where a subset of the records can be selected for deletion.                                                                                                                                                                                                                                                          |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5eWVJR4Lfqb-p_L%2Fundo24.gif?generation=1550287164816750\&alt=media)                                                                                                                                                                                                                                                                 | Undo Changes                                                                                     | Reverts the changes made and returns the record to the state after the last save.                                                                                                                                                                                                                                                   |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5F3DVja5UAlgxyR%2Frefresh24.gif?generation=1550287161408177\&alt=media)                                                                                                                                                                                                                                                              | Requery                                                                                          | Requeries the data according to the current search criteria. Useful if changes have been made in other windows.                                                                                                                                                                                                                     |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5F5MC-MROfNCaRX%2Ffind24.gif?generation=1550287147381762\&alt=media)                                                                                                                                                                                                                                                                 | [Lookup Record](http://wiki.adempiere.net/Lookup)                                                | Opens the [Lookup](http://wiki.adempiere.net/Lookup) dialog where search criteria can be defined.                                                                                                                                                                                                                                   |
| <p><img src="https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5ebW7El8YtJsA_k%2Flock24.gif?generation=1550287162525308&#x26;alt=media" alt=""></p><p><img src="https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5edLTG4-sEF1hZe%2Flockx24.gif?generation=1550287161480506&#x26;alt=media" alt=""></p>   | [Private Record Lock](http://wiki.adempiere.net/Private_Record_Lock)                             | Marks the record as private, preventing other users from viewing or making any changes to the data. See [Private Record Lock](http://wiki.adempiere.net/Private_Record_Lock) for more information.                                                                                                                                  |
| **View**                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                  |                                                                                                                                                                                                                                                                                                                                     |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5FZQXS3DV2PMivj%2Fproduct24.gif?generation=1550287161405614\&alt=media)                                                                                                                                                                                                                                                              | [Product Info](http://wiki.adempiere.net/Product_Info)                                           | Opens the [Product Info](http://wiki.adempiere.net/Product_Info) window which displays availability and pricing for products. The menu item will appear if the Role permits access to this information.                                                                                                                             |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5ehlLomS1TyrS2r%2Finfobpartner24.gif?generation=1550287162847882\&alt=media)                                                                                                                                                                                                                                                         | [Business Partner Info](http://wiki.adempiere.net/Business_Partner_Info)                         | Opens the [Business Partner Info](http://wiki.adempiere.net/Business_Partner_Info) dialog which displays key information about business partners. The menu item will appear if the Role permits access to this information.                                                                                                         |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5ejj-myYdU-G910%2Finfoaccount24.gif?generation=1550287163134027\&alt=media)                                                                                                                                                                                                                                                          | [Account Info](http://wiki.adempiere.net/Account_Info)                                           | Opens the [Account Info](http://wiki.adempiere.net/Account_Info) dialog which displays detailed information about account transactions. The menu item will appear if the Role permits access to this information.                                                                                                                   |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5eljpiJsnHfL0gG%2Finfoschedule24.gif?generation=1550287166217391\&alt=media)                                                                                                                                                                                                                                                         | [Schedule Info](http://wiki.adempiere.net/Schedule_Info)                                         | Opens the [Schedule Info](http://wiki.adempiere.net/Schedule_Info) dialog which displays detailed information about resource assignments and schedules. The menu item will appear if the Role permits access to this information.                                                                                                   |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5ezzRr6vpIRLZHF%2Finfo24.gif?generation=1550287160373595\&alt=media)                                                                                                                                                                                                                                                                 | [MRP Info](http://wiki.adempiere.net/MRP_Info)                                                   | Opens the [MRP Info](http://wiki.adempiere.net/MRP_Info) dialog which displays detailed information about Material Resource Planning. The menu item will appear if the Role permits access to this information.                                                                                                                     |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5ezzRr6vpIRLZHF%2Finfo24.gif?generation=1550287160373595\&alt=media)                                                                                                                                                                                                                                                                 | [CRP Info](http://wiki.adempiere.net/CRP_Info)                                                   | Opens the [CRP Info](http://wiki.adempiere.net/CRP_Info) dialog which displays detailed information about Capacity Resource Planning. The menu item will appear if the Role permits access to this information.                                                                                                                     |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5ezzRr6vpIRLZHF%2Finfo24.gif?generation=1550287160373595\&alt=media)                                                                                                                                                                                                                                                                 | [Order Info](http://wiki.adempiere.net/Order_Info)                                               | Opens the [Order Info](http://wiki.adempiere.net/Order_Info) dialog which displays detailed information about Orders. The menu item will appear if the Role permits access to this information.                                                                                                                                     |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5ezzRr6vpIRLZHF%2Finfo24.gif?generation=1550287160373595\&alt=media)                                                                                                                                                                                                                                                                 | [Invoice Info](http://wiki.adempiere.net/Invoice_Info)                                           | Opens the [Invoice Info](http://wiki.adempiere.net/Invoice_Info) dialog which displays detailed information about Invoices. The menu item will appear if the Role permits access to this information.                                                                                                                               |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5ezzRr6vpIRLZHF%2Finfo24.gif?generation=1550287160373595\&alt=media)                                                                                                                                                                                                                                                                 | [Shipment Info](http://wiki.adempiere.net/Shipment_Info)                                         | Opens the [Shipment Info](http://wiki.adempiere.net/Shipment_Info) dialog which displays detailed information about Shipments. The menu item will appear if the Role permits access to this information.                                                                                                                            |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5ezzRr6vpIRLZHF%2Finfo24.gif?generation=1550287160373595\&alt=media)                                                                                                                                                                                                                                                                 | [Payment Info](http://wiki.adempiere.net/Payment_Info)                                           | Opens the [Payment Info](http://wiki.adempiere.net/Payment_Info) dialog which displays detailed information about Payments. The menu item will appear if the Role permits access to this information.                                                                                                                               |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5ezzRr6vpIRLZHF%2Finfo24.gif?generation=1550287160373595\&alt=media)                                                                                                                                                                                                                                                                 | [Cash Journal Info](http://wiki.adempiere.net/Cash_Journal_Info)                                 | Opens the [Cash Journal Info](http://wiki.adempiere.net/Cash_Journal_Info) dialog which displays detailed information about the Cash Journal. The menu item will appear if the Role permits access to this information.                                                                                                             |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5ezzRr6vpIRLZHF%2Finfo24.gif?generation=1550287160373595\&alt=media)                                                                                                                                                                                                                                                                 | [Resource Info](http://wiki.adempiere.net/Resource_Info)                                         | Opens the [Resource Info](http://wiki.adempiere.net/Resource_Info) dialog which displays detailed information about Resource Assignments. The menu item will appear if the Role permits access to this information.                                                                                                                 |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5ezzRr6vpIRLZHF%2Finfo24.gif?generation=1550287160373595\&alt=media)                                                                                                                                                                                                                                                                 | [Resource Info](http://wiki.adempiere.net/Resource_Info)                                         | Opens the [Resource Info](http://wiki.adempiere.net/Resource_Info) dialog which displays detailed information about Resource Assignments. The menu item will appear if the Role permits access to this information.                                                                                                                 |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5ezzRr6vpIRLZHF%2Finfo24.gif?generation=1550287160373595\&alt=media)                                                                                                                                                                                                                                                                 | [Asset Info](http://wiki.adempiere.net/Asset_Info)                                               | Opens the [Asset Info](http://wiki.adempiere.net/Asset_Info) dialog which displays detailed information about Asset Utilization. The menu item will appear if the Role permits access to this information.                                                                                                                          |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5F71k9-eNoKO0DP%2Fattachment24d.gif?generation=1550287148844560\&alt=media)                                                                                                                                                                                                                                                          | [Attachment](http://wiki.adempiere.net/Attachment)                                               | Opens the [Attachment](http://wiki.adempiere.net/Attachment) dialog where notes and files can be "attached" to a record. When attachments are present, the icon changes to [![Image:Icon\_AttachmentX24.png](http://wiki.adempiere.net/images/4/4d/Icon_AttachmentX24.png)](http://wiki.adempiere.net/File:Icon_AttachmentX24.png). |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5f8mO2VTbz2OAfE%2Fchat24.gif?generation=1550287159951731\&alt=media)                                                                                                                                                                                                                                                                 | [Chat](http://wiki.adempiere.net/Chat)                                                           | Opens the [Chat](http://wiki.adempiere.net/Chat) dialog where time-stamped comments about the record can be maintained.                                                                                                                                                                                                             |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5fA4RYLECCvtuBp%2Fhistory24.gif?generation=1550287161659299\&alt=media)                                                                                                                                                                                                                                                              | [History Records](http://wiki.adempiere.net/History)                                             | Opens the [History](http://wiki.adempiere.net/History) dialog where the change record is displayed. Only applies to records where history tracking is enabled.                                                                                                                                                                      |
| <p><img src="https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5fCc1GHYl5IJIy9%2Fmulti24.gif?generation=1550287163575280&#x26;alt=media" alt=""></p><p><img src="https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5FBBgtEV8MqlmPY%2Fmultix24.gif?generation=1550287161548598&#x26;alt=media" alt=""></p> | Grid Toggle                                                                                      | Toggles the display from a single record form to a spreadsheet view and back.                                                                                                                                                                                                                                                       |
| **Go**                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                  |                                                                                                                                                                                                                                                                                                                                     |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5fGF8vYNqia4ksM%2Ffirst24.gif?generation=1550287159419112\&alt=media)                                                                                                                                                                                                                                                                | First record                                                                                     | Move to the first record.                                                                                                                                                                                                                                                                                                           |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5FgJAi8MmowYp9Z%2Fprevious24.gif?generation=1550287160562356\&alt=media)                                                                                                                                                                                                                                                             | Previous record                                                                                  | Move to the previous record.                                                                                                                                                                                                                                                                                                        |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5fKzDXr1MKQClMa%2Fnext24.gif?generation=1550287161856251\&alt=media)                                                                                                                                                                                                                                                                 | Next record                                                                                      | Move to the next record.                                                                                                                                                                                                                                                                                                            |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5fM74fYD-0PwXms%2Flast24.gif?generation=1550287165195440\&alt=media)                                                                                                                                                                                                                                                                 | Last record                                                                                      | Move to the Last record.                                                                                                                                                                                                                                                                                                            |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5Fmgj6CN5U4XsjD%2Fparent24.gif?generation=1550287158561572\&alt=media)                                                                                                                                                                                                                                                               | Parent tab                                                                                       | Move to the previous tab.                                                                                                                                                                                                                                                                                                           |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5Foga1VmznhBXQz%2Fdetail24.gif?generation=1550287157583456\&alt=media)                                                                                                                                                                                                                                                               | Detail tab                                                                                       | Move to the next tab.                                                                                                                                                                                                                                                                                                               |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ7y1N64RxoaiqEPk%2Fzoomacross24.gif?generation=1550287153082827\&alt=media)                                                                                                                                                                                                                                                           | [Zoom Across](http://wiki.adempiere.net/Zoom_Across) (where used)                                | Zoom to a related record. See [Zoom Across](http://wiki.adempiere.net/Zoom_Across) for more information.                                                                                                                                                                                                                            |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5fUXIeiPssayllv%2Frequest24.gif?generation=1550287165585989\&alt=media)                                                                                                                                                                                                                                                              | Check [Requests](http://wiki.adempiere.net/Request)                                              | Pops up a selection list where a new request can be created or one of the active requests can be opened. See [Requests](http://wiki.adempiere.net/Request) for more information.                                                                                                                                                    |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5fWrV_aqXesOBr-%2Farchive24.gif?generation=1550287163206581\&alt=media)                                                                                                                                                                                                                                                              | [Archived Documents](http://wiki.adempiere.net/Archived_Documents)/Reports                       | Pops up a selection list of archived documents and reports related to the current record. See [Archived Documents](http://wiki.adempiere.net/Archived_Documents) for more information.                                                                                                                                              |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5fY9zfKW1QrV1dW%2Fhome24.gif?generation=1550287161644733\&alt=media)                                                                                                                                                                                                                                                                 | Menu                                                                                             | Brings the Main Panel with the menu tree to the front.                                                                                                                                                                                                                                                                              |
| **Tools**                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                  |                                                                                                                                                                                                                                                                                                                                     |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5f__Ts1r2gj0lHJ%2Fcalculator24.gif?generation=1550287161251745\&alt=media)                                                                                                                                                                                                                                                           | [Calculator](http://wiki.adempiere.net/Calculator_Tool)                                          | Opens a [Calculator Tool](http://wiki.adempiere.net/Calculator_Tool) that can be used for simple math (+ - \* / %) and currency conversion.                                                                                                                                                                                         |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5fbvQ4zPvu-LU5m%2Fcalendar24.gif?generation=1550287161003296\&alt=media)                                                                                                                                                                                                                                                             | [Calendar](http://wiki.adempiere.net/Calendar_Tool)                                              | Opens a simple [Calendar Tool](http://wiki.adempiere.net/Calendar_Tool) which can be used to find dates and days of the week.                                                                                                                                                                                                       |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5fdYbOvOtnyCcpx%2Feditor24.gif?generation=1550287162869515\&alt=media)                                                                                                                                                                                                                                                               | [Editor](http://wiki.adempiere.net/Text_Editor_Tool)                                             | Opens a [Text Editor Tool](http://wiki.adempiere.net/Text_Editor_Tool) which can be used to edit text and see the output as HTML.                                                                                                                                                                                                   |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5ffiOQQ0leXqj2u%2Fscript24.gif?generation=1550287160761010\&alt=media)                                                                                                                                                                                                                                                               | [Script](http://wiki.adempiere.net/Script_Editor_Tool)                                           | Opens a [Script Editor Tool](http://wiki.adempiere.net/Script_Editor_Tool) which can be used to edit scripts and see the output as HTML. Available to system administrators only.                                                                                                                                                   |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5fhYvNX8fqTUW0N%2Fwinsize24.gif?generation=1550287159851994\&alt=media)                                                                                                                                                                                                                                                              | [Set Window Size](http://wiki.adempiere.net/Window_Size)                                         | Opens a [Window Size](http://wiki.adempiere.net/Window_Size) dialog which can be used to set the default window size for all users. Available to system administrators only.                                                                                                                                                        |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5fjzMoYcMVl84Ro%2Fworkflow_24.gif?generation=1550287165407725\&alt=media)                                                                                                                                                                                                                                                            | [Active Workflows](http://wiki.adempiere.net/Workflow)                                           | Opens the [Active Worflows](http://wiki.adempiere.net/Workflow) window where the active workflows can be managed.                                                                                                                                                                                                                   |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5flOoz8_fJYOxgM%2Fpreference24.gif?generation=1550287162388227\&alt=media)                                                                                                                                                                                                                                                           | [Preference](http://wiki.adempiere.net/index.php?title=User_Preferences\&action=edit\&redlink=1) | Opens the [Preference](http://wiki.adempiere.net/index.php?title=User_Preferences\&action=edit\&redlink=1) window where user preferences can be set and context and error messages can be viewed.                                                                                                                                   |
| **Window**                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                  |                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Show all Windows                                                                                 | Displays all widows as miniature panels. Click on the desired window to bring it to the top of the desktop.                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Close Other Windows                                                                              | Keeps the Main Panel window and the current window open. Closes all other windows.                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Close All Windows                                                                                | Closes all windows except the Main Panel window.                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                  | Opens the Main Panel window. The text is in the form <user@client.org> \[app\_server{db\_server-db\_name-db\_user}]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                  | A list of open windows. Click on one to bring it to the top of the desktop.                                                                                                                                                                                                                                                         |
| **Help**                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                  |                                                                                                                                                                                                                                                                                                                                     |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5EuVmmBWxrbnHxj%2Fhelp24.gif?generation=1550287148561278\&alt=media)                                                                                                                                                                                                                                                                 | Help                                                                                             | Opens a help dialog that displays contextual help for the current window.                                                                                                                                                                                                                                                           |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5fpKBW54ELPcUDx%2Fonline24.gif?generation=1550287159068423\&alt=media)                                                                                                                                                                                                                                                               | Online                                                                                           | Opens the [Manual](http://wiki.adempiere.net/Manual) page of this wiki.                                                                                                                                                                                                                                                             |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5fr04fLPqPGnclb%2Femailsupport24.gif?generation=1550287161258499\&alt=media)                                                                                                                                                                                                                                                         | EMail to Support                                                                                 | Opens the internal [EMail](http://wiki.adempiere.net/EMail) dialog with an email already filled with the system and context information. Requires that the internal email is properly configured.                                                                                                                                   |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5ftT9S4E_iNDuEF%2Fabout24.gif?generation=1550287158904861\&alt=media)                                                                                                                                                                                                                                                                | About                                                                                            | Opens an about splash screen that contains the version info and the main context.                                                                                                                                                                                                                                                   |


# The Performance Dashboard

![The initial window showing the performance measures.](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZ5G1bjZ0BFZHjQciW2%2F-LZ5G3vOTXFDMd8x792u%2Fimage%20\(7\).png?generation=1550588337028442\&alt=media)

The Performance Dashboard is the typical landing spot when you first log in to the application. It only appears if you have a set of Performance Measures and Goals defined for your role. The tab displays these as indicators, gauges or graphs and you can click on these to see the details of the performance measure. For the performance gauges, clicking on these will display a chart. For the charts, clicking on a data point will open the relevant documents for that point. For example, clicking a bar in the Open Invoices Amount graph will open the Invoice (Customer) window with the set of open invoices loaded.

Setup properly for your role, the Performance Tab should provide you with accurate information about the things that are important for your job and provide guidance on the tasks you need to perform.


# The Menu (Home) Tab

Describes the main menu/home tab of the Java Client

![The Java Client home menu tab](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj0nK8N30FU1B0sW0%2Fswing_menu.PNG?generation=1550780738880213\&alt=media)

The Menu tab or Home tab contains the main menu tree used to access the windows, forms, reports and processes which make up the application. The default menu tree has over 800 entries and is challenging to deal with. The tree structure of the menu can be configured to suit your role so it may not appear as shown and may contain only a few entries relevant to you.

The tree may have summary items which have a folder icon. You can expand these by clicking on them. Alternatively, you can select the Expand Tree tool at the bottom left of the menu to open all the summary items.

![Example of an expanded menu](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj0nM97aFwHdLjvSu%2Fswing_menu_expanded.PNG?generation=1550780738372447\&alt=media)

There are four types of items in the menu differentiated by their icon:

| Icon                                                                                                                                                                                                            | Description                                                                                      |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj0nOxQg8Gw4a5ow3%2Fmwindow.gif?generation=1550780739307258\&alt=media)    | Window or form - used to enter or view data                                                      |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj0nQAdVf8kD5Kwe-%2Fmreport.gif?generation=1550780740411054\&alt=media)    | Report - a collection of data that can be printed                                                |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj0nSHkz5Kr-P7e08%2Fmprocess.gif?generation=1550780736875574\&alt=media)   | Process - a software tool that performs an action                                                |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj0nUkcNFZKLqSrsg%2Fmdocaction.gif?generation=1550780737422606\&alt=media) | Browser - a combination form and process used to select records and perform a process with them. |

Clicking on a menu item will open the window or dialog related to that item.

## Lookup - Finding Menu Items

To find a Menu Item based on its name, use the Lookup tool in the bottom right.

![The Lookup tool for the main menu.](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj0nWZ5TvN5lkyMmR%2Fswing_menu_lookupdetail.PNG?generation=1550780739778977\&alt=media)

Enter the name or part of the name in the Lookup tool and hit \<Enter>. The Menu will expand to the first matching item. Keep typing \<Enter> until the Menu item your looking for is highlighted. You can open this entry by typing \<Ctrl>\<Enter>.

## The Menu Bar

![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj0nYcLYQXSASEozL%2Fswing_menu_bar.PNG?generation=1550780740926591\&alt=media)

To the left of the Menu is a blue area called the "Bar". You can add your favorite menu items to the Bar by right-clicking on the menu item and selecting "Add to Bar" from the pop-up. You can remove items from the Bar by right-clicking on them and selecting "Remove from Bar" from the pop-up.

The Bar items will be organized into lists according to the top level menu summary where they were originally found. At the top of the Bar, a list labeled "Recent Item" will be shown. This is a list of recently opened menu items. For example, if you opened Sales Order 80007 and updated it, you would see an entry for "Sales Order: \_80007..." in the recent items. Clicking this link will take you back to that record.

The size of the list is limited to 50 entries by default but this can be configured for the Client or User to any number. (Have a look at the bottom of the **User Contact** tab in the **My Profile** window.) If a recent record is deleted, it will be automatically removed from the list.

To refresh the Bar, right-click in any of the list areas and select "Refresh the Bar" from the popup menu.


# Finding Your Way Around the Web App

After you login, you will be presented with a dashboard which can be configured to show a variety of information.

![ADempiere web application dashboard](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ7glHs464RBE1-Sl%2Fwebui_dashboard.PNG?generation=1550287152139814\&alt=media)

## The User Panel

![Web app User Panel](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ7gnglQxelCPzTmG%2Fwebui_userpanel.PNG?generation=1550287151700193\&alt=media)

At the top right is the User Panel. This small panel shows the User ID of the current user and the Client and Organization they are logged-in to, in this case GardenAdmin, GardenWorld and all Organizations (\*). Below that are five links that provide some useful information and actions:

| Clicking the link ... | Opens ...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Context               | A Context dialog showing the full context of the application. The context is useful for developers and system administrators. If you are having issues with a particular window, the context may provide the Support Team valuable help.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Preference            | <p>A small dialog where a few preferences can be set. These are:</p><ol><li>Automatic Commit - If not selected, a dialog will ask if you want to save changes before moving to another record. If selected, the changes will be performed automatically.</li><li>Automatic New Record - If selected, if a window is opened or a search performed and no record is found, a new record will be opened automatically if possible.</li><li>Window Tab Collapsible - To save screen space, the tabs on the side of a Window can be collapsed.</li><li>Window Tab Placement - The tabs can be on the right or left.</li></ol><p>Click the Save icon at the bottom right to save the Preferences. You will have to log out and in for the changes to have effect.</p> |
| Change Role           | Closes all windows and effectively logs out, returning the user to the Login Role dialog. This provides a quick way to change the current Role, Client, Organization or Warehouse. For the Super User, its a great tool. For a user with access to only one of each, not so much.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Log Out               | Closes all windows and logs out, returning the user to the Login dialog.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

![Web Application Menu](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ7gpyvWYcobaahE0%2Fwebui_menu.PNG?generation=1550287152062368\&alt=media)

On the left is the Menu which is a tree of all the available Windows, Reports and Processes the User has access to. The tree can be quite large and contain hundreds of items but it can be customized to each role and only show the entries required.

At the top of the menu is a Lookup combo box that can be used to find a particular menu item. At the bottom is a checkbox that will expand the entire tree if it is selected.

The Menu is always visible but it can be collapsed to the left by clicking on the small button (![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ7grX2LeFRUqCmDh%2Fborderlayout-btn-left.png?generation=1550287152698572\&alt=media)) in the top right of the Menu.

## Window Tabs

![Web Application Window Tabs](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ7gt6I1kRjqADU4Y%2Fwebui_windowtabs.PNG?generation=1550287152546016\&alt=media)

To the right of the Menu are the Window Tabs, or just Windows. The Menu Tab, shown in the image as "Menu (1)", is the Dashboard for the User. Other Menu Items opened, such as the Sales Order Window, will appear as additional Tabs. Any Window can be closed by closing its Tab (clicking on the X in the Tab). It is not possible to Close the Menu Tab. Clicking the Window Tab will bring it to the fore.


# The Dashboard

Describes the User Dashboard on the Menu tab.

![The GardenAdmin Dashboard](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ9vnH-nPexaaagXi%2Fwebui_dashboardonly.PNG?generation=1550287157400362\&alt=media)

The Dashboard can contain a variety of Panels that provide information such as:

* [Activities](#activities);
* [Calendar](#calendar);
* [Document tasks](#document-tasks);
* [Favorites (User)](#favorites-user);
* [Favorites (System)](#favorites-system);
* [Performance measures](#performance-measures);
* [Recent Items](#recent-items); and&#x20;
* [Views](#views)

{% hint style="info" %}
Access to Dashboard Items has to be specifically granted for each Role by a Client Administrator. If no access has been granted for the Role chosen at login, the Dashboard will be blank.
{% endhint %}

Each panel has a header bar and can be collapsed to make room on the screen.

## Activities

![Dashboard Activities Panel](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ9vpkkDrUV8SqaV0%2Fwebui_dashboardactivities.PNG?generation=1550287157113677\&alt=media)

The Activities panel has three buttons that provide some of the key information about the tasks that must be accomplished. Beside the text in each button is a number representing the number of items that need attention. The three buttons function as described below.

| Button ...          | Opens ...                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Notice              | The **Notice** window which displays Client and Organization information the user may need.  Notices are raised by the system and may indicate problems that need to be addressed or information that needs to be managed.  The User can choose to receive these "Notes" via email, the **Notice** window or both.  Notices may have Attachments such as spreadsheets or reports relevant to the note. |
| Request             | The **Request** window showing items that may require attention.  Requests are typically customer driven and can be for products, services or warranty action and may trigger the creation of other documents such as sales orders.                                                                                                                                                                    |
| Workflow Activities | The **Workflow** window which shows any active workflows the user is involved with.  Workflows may require approvals or additional actions on the part of the user to complete the work.                                                                                                                                                                                                               |

{% hint style="info" %}
The Menu Tab text "Menu (1)" shows the total of the activities that need attention. The number will be updated as new items appear. Keep an eye out for it as you work and return to the Menu Tab to address these activities.
{% endhint %}

## Calendar

![Dashboard Calendar](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ9vrH_KHPpuRQa7z%2Fwebui_dashboard_calendar.PNG?generation=1550287157701831\&alt=media)

A Calendar can be displayed in the Dashboard. This is an embedded Google calendar which can be used to find dates and to add events to your personal calendar, although they will not appear in this panel.

{% hint style="info" %}
The Calendar is not configurable. If you need the Calendar to show events, ask your System Administrator. A modification to the application code will be required.
{% endhint %}

## Document Tasks

![Dashboard Document Tasks](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ9vtCKO6mt2Z4eXD%2Fwebui_dashboard_doctasks.PNG?generation=1550287157761043\&alt=media)

The *Document tasks* panel displays a count of documents with a particular status. Clicking on the link beside the number will open the corresponding window with the relevant documents loaded. The entries in this panel are set in the [**Document Status Indicator**](https://adempiere.gitbook.io/docs/introduction/system-administration/managing-organizations/document-status-indicators) window. Its likely that the system administrator will set these up for you as it is an advanced task.

## Favorites (User)

The User Favorites panel is a list of frequently used menu items that you can select and organize as you wish. Clicking on items in the panel will open the associated menu item. Having these items easily available saves time when looking for a frequently needed menu item.

The pane, when empty, appears as shown in the image below.

![Favorites (User) panel when empty](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ9vviNJOxPEe7ePa%2Fwebui_dpuserfavoritesempty.PNG?generation=1550287158560466\&alt=media)

You can add items to the Favorites by simply dragging them from the main menu and dropping them into the panel. You can create folders to organize the items by right-clicking in the panel or on an existing item and selecting "Add Folder" from the pop-up menu. The order and structure can be arranged by dragging and dropping items. An item dropped on another item will be placed after it. An item or folder dropped on a folder will cause a menu to appear with options to "Insert After" or "Move Into".

![Favorites (User) panel with items](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ9vxRIjXjOz7483X%2Fwebui_dpuserfavoritesfull.PNG?generation=1550287157779715\&alt=media)

A Folder can be renamed by double-clicking on it. A simple text dialog will open. Edit the text and hit \<Enter> to save the new name or close the dialog. Hit \<Esc> to cancel.

Folders can also be set to Start Collapsed or Expanded by right-clicking the folder and selecting the corresponding menu entry from the pop-up menu.

{% hint style="info" %}
The Folders will be created in the language you are using at the time. If you switch to a different language, the folder names will not be translated.
{% endhint %}

The trash can icon at the bottom of the panel can be used to delete items from the list. Simply drag items from the list and drop them on the trash can. You can also delete items using the right-click pop-up menu.

The Expand Tree check box can be used to expand or collapse the entire tree.

## Favorites (System)

Like the Favorites (User), the Favorites (System) is a list of menu items but these ones are common to all users of the Role. Items from the menu can be added by dragging and dropping onto the list or deleted from the list by dragging to the trash can icon.

You can only delete the items that you have added. Items added by other users cannot be deleted.

The items are displayed in the order they appear in the Menu and all at the same level.

{% hint style="info" %}
The Favorites (System) uses the same list as the Java Client Menu Bar. However, the Favorites (System) panel includes items added from ALL users of the Role. The Java Client Menu Bar will only show items added by the User.
{% endhint %}

{% hint style="warning" %}
If multiple users add the same menu item to the Favorites (System) or to the Java Client Menu Bar, the menu item will appear multiple times in the list. See issue [#2355](https://github.com/adempiere/adempiere/issues/2355).
{% endhint %}

## Performance Measures

![Example Performance Measure indicator](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj0qc8tIt58aoKVUy%2Fwebui_dashboard_perfmeasure.PNG?generation=1550780742421386\&alt=media)

Performance Measures provide a quick visual reference to key performance data. The information presented is specific to your role. What is measured and the assessment of good, mediocre and bad can be configured using any data in the database. To be most effective, the measures should be very relevant and agreed upon between you and your supervisor. Like instruments in an aircraft, the indicators should give the you clues as to what you need to focus on and how well you are doing your job.

Performance Measures are configured in the **Performance Analysis > Performance Measurement** menu. See [Performance Measurement Setup](https://adempiere.gitbook.io/docs/introduction/accounting-and-performance-analysis/performance-measurement-setup) for more information.

If you click on a Performance Measure Indicator, a window will open that will show the performance measure data in a graph along with a table containing information about the measure.

![Performance Measure Data](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj0qe3qMIiGYC__eT%2Fwebui_dashboard_perfmeasure_data.PNG?generation=1550780741395850\&alt=media)

You can click on the graph or on the measurement data in the table to open relevant documents or see more detail about the measurement data. At the top left is a combo-box that can be used to change the style of chart displayed

## Recent Items

![Dashboard Recent Items panel](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-Lds_dPUW-NWkXppkN3o%2F-LZGj0qg0d1eRyUmwTHy%2Fwebui_dashboard_recentitems.PNG?generation=1556801304992909\&alt=media)

The Recent Items panel is a list of windows/records that have been opened recently. The entries are ordered with the most recent at the top. Clicking on a Recent Item will open that record, a handy way to return to work in progress.

The size of the list is limited to 50 entries by default but this can be configured for the Client or User to any number. (Have a look at the bottom of the **User Contact** tab in the **My Profile** window.) If a recent record is deleted, it will be automatically removed from the list. You can also drag and drop items onto the Trash Can icon to delete them.

Click on the Refresh icon at the bottom left to refresh the display manually.

## Views

![Dashboard Views](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj0qihb1Xuh6fjHqy%2Fwebui_dashboard_views.PNG?generation=1550780738503630\&alt=media)

Views are special forms that present information in useful ways. The Product Info view, for example, provides a way to search for products and see quantities in inventory and the expected changes. The form can be used to provide promise dates to customers or suggest alternative (substitute) or complementary products. The Business Partner info window can be used like a phone or contact list for Business Partners.

The views can be used standalone to find information but they are also connected to search/lookup fields as helper functions. For example, any search field connected to the Product table will have a helper button that will open the Product Info window.

![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj0qklS7XcfU8squu%2Fwebui_productinfoview.PNG?generation=1550780738043047\&alt=media)

The Views are similar in layout except for the Account Info and Schedule Info view. There is a set of constraints at the top to limit the search. At the top left is a refresh button that will reset the constrains. In the middle will be one or more tables of information. At the bottom are buttons that control how the form behaves and that provide some functions such as zoom to the selected entry.

For more information, refer to the section on Views.


# Opening and Using Windows

In the ADempiere Menu Tree, clicking on or activating any item that has the Window icon ( ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj0nOxQg8Gw4a5ow3%2Fmwindow.gif?generation=1550780739307258\&alt=media) ) will open a window that will display data in a table.

Most windows are organized the same way in ADempiere, and, apart from the style differences, function the same way in the Java Client and the Web App. Images used in this manual to highlight certain windows may come from either. While the look may differ, the location and function of most icons and fields will be the same.

At the top of the window is a Tool Bar of icons that are common across all Windows as shown below. See [The Tool Bar](https://adempiere.gitbook.io/docs/introduction/getting-started/opening-and-using-windows/the-tool-bar) for more information about the icons and functions the represent.

![The Java Client Toolbar that appears in most windows.](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ7xPwndgSf6AjrGE%2Ftoolbarswing.PNG?generation=1550287154040857\&alt=media)

![The equivalent Toolbar in the Web Application.](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj1SkTSNI1ouNgdXK%2Fwebui_toolbar.PNG?generation=1550780739004853\&alt=media)

In the Java Client, a window will show a form with tabs on the left. The Web App can display the tabs on either side. The tabs represent sets of hierarchical data: parent and child records if you will. Each subordinate tab will show records related to the record currently selected/viewed in the parent tab.

![Java Client window tabs, for the GL Journal Batch window.](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj1SmQ1pKqBsMD5xV%2Fswing_window_tabs.PNG?generation=1550780742975039\&alt=media)

In the image above, the GL Journal Batch window has three levels of tabs. Each Batch record could have several Journal records and each Journal record could have several lines. To look at a Line record, you would first have to select the Batch and then a Journal.

Moving between records and switching between tabs allows you to go through huge amounts of data without having to backtrack as much. When you move between records or tabs, whatever data you have entered is automatically saved.

In each tab, the data can be displayed as a table view (like a spreadsheet) where you can see many records at once or as a form view showing one record at a time. Buttons that control processes will generally be accessed from the form view.

![The Business Partner window displayed in form view, one record at a time.](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj1SouKleL63pgrSw%2Fswing_businesspartnerwindow.PNG?generation=1550780739389827\&alt=media)

![The Business Partner window displayed in table view. Several records are visible.](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj1SqZETFpcJHf9OQ%2Fswing_businesspartnerwindowtable.PNG?generation=1550780739690316\&alt=media)

At the bottom of the window is a status bar providing information about the available actions or results of a process. At the very bottom right is a record count showing the current record number and the total number of records displayed. If you click on this record count a [Record Info dialog](https://adempiere.gitbook.io/docs/introduction/getting-started/dialogs-and-forms/change-log-or-record-info) (also called a Change Log) will be displayed.


# The Tool Bar

Details on the main Tool Bar used in most windows.

![The Application Menu and the Tool Bar that appears in most windows.](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ7xPwndgSf6AjrGE%2Ftoolbarswing.PNG?generation=1550287154040857\&alt=media)

![The equivalent toolbar in the Web Application.](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj1LugTdWoehFNvTP%2Fwebui_toolbar.PNG?generation=1550780746901195\&alt=media)

Most windows are organized the same way in ADempiere. At the top of the window is a tool bar of icons, shown above, that is common across all Windows.

{% hint style="info" %}
While the Web Application and the Java Client are mostly similar, there are a few differences. Specifically, the web application:

* does not have both print and print-preview. In the Web Application there are the same thing so there is only one icon.
* does not have a Home icon.&#x20;
* does not have an Exit icon.
* does have a button to allow "quicksheet" entry
  {% endhint %}

The details of the various toolbar icons follow:

| Client Icon                                                                                                                                                                                                            | Web Icon                                                                                                                                                                                                                       | Function                                                | Description                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5eWVJR4Lfqb-p_L%2Fundo24.gif?generation=1550287164816750\&alt=media)            | ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj1M2p75ViLQV8VAu%2Fignore24.webicon.png?generation=1550780747317235\&alt=media)          | Undo                                                    | Reverts any changes made to the record since the last save. Enabled if there are changes to be saved.                                                                                                                                                                                                                                                                                                                   |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5EuVmmBWxrbnHxj%2Fhelp24.gif?generation=1550287148561278\&alt=media)            | ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj1M4UfRJiXSxGfi2%2Fhelp24.webicon.png?generation=1550780747910581\&alt=media)            | Help                                                    | Opens a help dialog where the field descriptions and help text are displayed.                                                                                                                                                                                                                                                                                                                                           |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5eMWPMBA1FXSXLx%2Fnew24.gif?generation=1550287167308660\&alt=media)             | ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj1M6CBcQ3UU5QGub%2Fnew24.webicon.png?generation=1550780747279766\&alt=media)             | New                                                     | Creates a new record. Fields colored red are mandatory. They turn blue once data has been entered. Enabled if creating a new record is possible.                                                                                                                                                                                                                                                                        |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5F-xfae5uDfUEbu%2Fdelete24.gif?generation=1550287148364679\&alt=media)          | ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj1M8Vi1XT3DWM7xm%2Fdelete24.webicon.png?generation=1550780747772950\&alt=media)          | Delete                                                  | Deletes the current record. Enabled if it is possible to delete the record.                                                                                                                                                                                                                                                                                                                                             |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5eUIu5jkeiS6XBs%2Fdeleteselection24.gif?generation=1550287166421656\&alt=media) | ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj1MAoGUPjkvbgRj9%2Fdeleteselection24.webicon.png?generation=1550780747368350\&alt=media) | Delete Selection                                        | Opens a dialog Listing all the records in the current tab. You can select all or a subset of these for deletion. It is helpful to use the Search function to limit the number of records. Enabled if it is possible to delete records.                                                                                                                                                                                  |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5eOv7giyEZZ7sK6%2Fsave24.gif?generation=1550287167091193\&alt=media)            | ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj1MCn_FzUkiEjxoN%2Fsave24.webicon.png?generation=1550780746134611\&alt=media)            | Save                                                    | Saves any changes to the current record. Saves are made automatically any time you move from record to record, tab to tab or close the window. Enabled if there are any changes to save.                                                                                                                                                                                                                                |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5F3DVja5UAlgxyR%2Frefresh24.gif?generation=1550287161408177\&alt=media)         | ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj1MEJN7QNYvr0Ibi%2Frefresh24.webicon.png?generation=1550780746756278\&alt=media)         | Requery                                                 | Requery the records using the last search criteria. Requery is useful if another process or user has added or changed the information in the table since the last search was performed or the tab was opened.                                                                                                                                                                                                           |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5F5MC-MROfNCaRX%2Ffind24.gif?generation=1550287147381762\&alt=media)            | ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj1MGxnJ1_Cl4oNZF%2Ffind24.webicon.png?generation=1550780746422030\&alt=media)            | [Lookup](http://wiki.adempiere.net/Lookup)              | Lookup or search for records in the current tab. There is a basic search based on common fields and an advanced search where complex queries can be developed. See [Lookup](http://wiki.adempiere.net/Lookup) functionality for more information.                                                                                                                                                                       |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5F71k9-eNoKO0DP%2Fattachment24d.gif?generation=1550287148844560\&alt=media)     | ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj1MITmaVN891LIIE%2Fattachment24.webicon.png?generation=1550780747409149\&alt=media)      | [Attachment](http://wiki.adempiere.net/Attachment)      | Every record can have a file and/or notes added to it. See [Attachment](http://wiki.adempiere.net/Attachment) for more info.  If attachment already exist for the record, the icon will look yellow. ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ7xeXPelFKeHTg7x%2Fattachmentx24.gif?generation=1550287153459045\&alt=media) |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5f8mO2VTbz2OAfE%2Fchat24.gif?generation=1550287159951731\&alt=media)            | ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj1MKrkqlNW4QSKMM%2Fchat24.webicon.png?generation=1550780746780717\&alt=media)            | [Chat](http://wiki.adempiere.net/Chat)                  | Chat allows users to share a series of timestamped notes on the current record.                                                                                                                                                                                                                                                                                                                                         |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5fCc1GHYl5IJIy9%2Fmulti24.gif?generation=1550287163575280\&alt=media)           | ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj1MM5YkepaICnH4d%2Fmulti24.webicon.png?generation=1550780747412920\&alt=media)           | Multi View                                              | A toggle to switch from the form view to a multi-record spreadsheet style view.                                                                                                                                                                                                                                                                                                                                         |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5FBBgtEV8MqlmPY%2Fmultix24.gif?generation=1550287161548598\&alt=media)          | ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj1MOsY_FGams16Gx%2Fmulti24.webicon.png?generation=1550780747806791\&alt=media)           | Form View                                               | A toggle to switch from the multi-record view to a single-record view form view.                                                                                                                                                                                                                                                                                                                                        |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5fA4RYLECCvtuBp%2Fhistory24.gif?generation=1550287161659299\&alt=media)         | ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj1MQKCscAcImifHC%2Fhistoryx24.webicon.png?generation=1550780746510474\&alt=media)        | [History](http://wiki.adempiere.net/History)            | Shows the history for the selected record.                                                                                                                                                                                                                                                                                                                                                                              |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5fY9zfKW1QrV1dW%2Fhome24.gif?generation=1550287161644733\&alt=media)            | N/A                                                                                                                                                                                                                            | Home                                                    | Brings the main window to the front of the desktop. Useful for people with messy desks.                                                                                                                                                                                                                                                                                                                                 |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5Fmgj6CN5U4XsjD%2Fparent24.gif?generation=1550287158561572\&alt=media)          | ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj1MSv5UJSguSwtEo%2Fparent24.webicon.png?generation=1550780746375648\&alt=media)          | Parent Record                                           | Move up to or towards the parent tab of the current tab. Doesn't jump tabs.                                                                                                                                                                                                                                                                                                                                             |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5Foga1VmznhBXQz%2Fdetail24.gif?generation=1550287157583456\&alt=media)          | ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj1MUsO5cmjy1xk1c%2Fdetail24.webicon.png?generation=1550780746348751\&alt=media)          | Detail Record                                           | Move down to the next tab.                                                                                                                                                                                                                                                                                                                                                                                              |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5fGF8vYNqia4ksM%2Ffirst24.gif?generation=1550287159419112\&alt=media)           | ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj1MWONfmGZIS37M-%2Ffirst24.webicon.png?generation=1550780746245827\&alt=media)           | First Record                                            | Move to the first record in the current tab.                                                                                                                                                                                                                                                                                                                                                                            |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5FgJAi8MmowYp9Z%2Fprevious24.gif?generation=1550287160562356\&alt=media)        | ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj1MYRubm8qZQtMZZ%2Fprevious24.webicon.png?generation=1550780745758929\&alt=media)        | Previous Record                                         | Move to the previous record in the current tab.                                                                                                                                                                                                                                                                                                                                                                         |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5fKzDXr1MKQClMa%2Fnext24.gif?generation=1550287161856251\&alt=media)            | ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj1M__5h2Dr3v563s%2Fnext24.webicon.png?generation=1550780745806742\&alt=media)            | Next Record                                             | Move to the next record in the current tab.                                                                                                                                                                                                                                                                                                                                                                             |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5fM74fYD-0PwXms%2Flast24.gif?generation=1550287165195440\&alt=media)            | ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj1Mb7c3N0UVmEyFd%2Flast24.webicon.png?generation=1550780745889495\&alt=media)            | Last Record                                             | Move to the Last record in the current tab.                                                                                                                                                                                                                                                                                                                                                                             |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5e8-pyBgh7_a0BK%2Freport24.png?generation=1550287164025459\&alt=media)          | ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj1MdCSLowGm6-uJs%2Freport24.webicon.png?generation=1550780745936608\&alt=media)          | [Report](http://wiki.adempiere.net/Report)              | Create a report based on the current record.                                                                                                                                                                                                                                                                                                                                                                            |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5fWrV_aqXesOBr-%2Farchive24.gif?generation=1550287163206581\&alt=media)         | ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj1MfJq7LLXXHn5aV%2Farchive24.webicon.png?generation=1550780746823875\&alt=media)         | [Archive](http://wiki.adempiere.net/Archived_Documents) | View archived reports or documents for the current record. See [Archived Documents](http://wiki.adempiere.net/Archived_Documents) for more information.                                                                                                                                                                                                                                                                 |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5eCjsASII9CiQIL%2Fprintpreview24.gif?generation=1550287162047761\&alt=media)    | N/A                                                                                                                                                                                                                            | Print Preview                                           | Preview the defined print layout. See [Printing and Print Preview](http://wiki.adempiere.net/Printing_and_Print_Preview) for more information.                                                                                                                                                                                                                                                                          |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5FHgOpXUco2tIrA%2Fprint24.gif?generation=1550287147988429\&alt=media)           | ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj1MhfDVddbc4kp5m%2Fprint24.webicon.png?generation=1550780745785572\&alt=media)           | Print                                                   | Print the defined print layout. See [Printing and Print Preview](http://wiki.adempiere.net/Printing_and_Print_Preview) for more information.                                                                                                                                                                                                                                                                            |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ7y1N64RxoaiqEPk%2Fzoomacross24.gif?generation=1550287153082827\&alt=media)      | ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj1MjskXdA3FBVtZT%2Fzoomacross24.webicon.png?generation=1550780746901158\&alt=media)      | [Zoom Across](http://wiki.adempiere.net/Zoom_Across)    | Zoom to related records in other tables. For example, zoom to payments from invoices. See [Zoom Across](http://wiki.adempiere.net/Zoom_Across) for more information.                                                                                                                                                                                                                                                    |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ7y3CBvSbrIczTJC%2Fworkflow24.gif?generation=1550287154567735\&alt=media)        | ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj1Ml8rlDMO5bwlDK%2Fworkflow24.webicon.png?generation=1550780749653892\&alt=media)        | Workflow                                                | Opens the [**Workflow Process Window**](http://wiki.adempiere.net/ManPageW_WorkflowProcess). See [Workflow](http://wiki.adempiere.net/Workflow) for more information.                                                                                                                                                                                                                                                   |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5fUXIeiPssayllv%2Frequest24.gif?generation=1550287165585989\&alt=media)         | ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj1MnvuVq6UHF47uS%2Frequest24.webicon.png?generation=1550780747901156\&alt=media)         | Check [Requests](http://wiki.adempiere.net/Request)     | Check or create Requests for service. See [Request](http://wiki.adempiere.net/Request) for more information.                                                                                                                                                                                                                                                                                                            |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ7y8_-0ujkhz8UkO%2Fprocess24.gif?generation=1550287153865339\&alt=media)         | ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj1Mp1yTPlN7lxWcq%2Fprocess24.webicon.png?generation=1550780748407753\&alt=media)         | Process                                                 | Execute a predefined process associated with the displayed record.                                                                                                                                                                                                                                                                                                                                                      |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5FZQXS3DV2PMivj%2Fproduct24.gif?generation=1550287161405614\&alt=media)         | ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj1Mr4kRC2b224unf%2Fproduct24.webicon.png?generation=1550780748037862\&alt=media)         | [Product Info](http://wiki.adempiere.net/Product_Info)  | Open the Product Info page where information concerning a product's pricing and availability can be displayed. See [Product Info](http://wiki.adempiere.net/Product_Info) for more information.                                                                                                                                                                                                                         |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5eGQUsVhGkUf1Pi%2Fend24.gif?generation=1550287163588736\&alt=media)             | N/A                                                                                                                                                                                                                            | Exit                                                    | Close the current window. The window's state is saved and if the window is reopened in the same session, the record and tab last viewed will be displayed.                                                                                                                                                                                                                                                              |
| N/A                                                                                                                                                                                                                    | ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj1MtvARurfE3X1Pe%2Fquickentry24.webicon.png?generation=1550780748405473\&alt=media)      | Quick Entry                                             | Opens a dialog where data can be entered much like a spreadsheet.                                                                                                                                                                                                                                                                                                                                                       |


# Shortcut Keys

A list of keyboard shortcuts used in the application.

The following shortcut keys can be used to speed your work with the software. Print this page and keep it handy beside the terminal until you have the shortcuts memorized.

| Action                  | <p>Shortcut key<br>Java Client</p> | <p>Shortcut Key</p><p>Web App</p> |
| ----------------------- | ---------------------------------- | --------------------------------- |
| Help                    | `<F1>`                             | `<F1>`                            |
| New Record              | `<F2>`                             | `<F2>` or `<Ctrl>N`               |
| Copy Record             | `<Shift><F2>`                      | `<Shift><F2>`                     |
| Delete Record           | `<F3>`                             | `<F3>` or `<Ctrl>D`               |
| Save changes            | `<F4>`                             | `<F4>` or `<Ctrl>S`               |
| Requery                 | `<F5>`                             | `<F5>`                            |
| Lookup Record           | `<F6>`                             | `<F6>` or `<Ctrl>F`               |
| Attachment              | `<F7>`                             | `<F7>`                            |
| Grid Toggle             | `<F8>`                             | `<F8>`                            |
| History Records         | `<F9>`                             | `<F9>`                            |
| Quick Entry             |                                    | `<F10>`                           |
| Report                  | `<F11>`                            | `<F11>` or `<Alt>P`               |
| Print                   | `<F12>`                            | `<F12>` or `<Ctrl>P`              |
| Print Preview           | `<Alt><Shift>P`                    |                                   |
| eXit Window             | `<Alt>X`                           | `<Alt>X`                          |
| Log Out                 | `<Alt><Shift>L`                    |                                   |
| Exit Application        | `<Alt><Shift>X`                    |                                   |
| Delete Selected Records | `<Ctrl>D`                          |                                   |
| Undo Changes            | `<Esc>`                            | `<Alt>Z`                          |
| Product Info            | `<Alt>I`                           |                                   |
| Business Partner Info   | `<Alt><Shift>I`                    |                                   |
| Account Info            | `<Ctrl><Alt>I`                     |                                   |
| First record            | `<Alt><Page Up>`                   | `<Alt><Page Up>`                  |
| Previous record         | `<Alt><Up Arrow>`                  | `<Alt><Up Arrow>`                 |
| Next record             | `<Alt><Down Arrow>`                | `<Alt><Down Arrow>`               |
| Last record             | `<Alt><Page Down>`                 | `<Alt><Page Down>`                |
| Parent tab              | `<Alt><Left Arrow>`                | `<Alt><Left Arrow>`               |
| Detail tab              | `<Alt><Right Arrow>`               | `<Alt><Right Arrow>`              |
| Show all Windows        | `<Ctrl>W`                          |                                   |


# Entering Data - Fields and Buttons

Each window, form and process uses fields and buttons to display and gather data.  This page describes how to use the various types.

Each window that you open in ADempiere will likely provide you with the opportunity to enter data. This article describes the types of fields, buttons and controls that you will come across, the type of data that they will accept and how each of them functions. All the controls are listed below. The most common ones are [String](#string), [Number](#number), [Date](#date) and [Search](#search).

Several of the fields have helper functions, indicated by an icon/button at the right side of the field. The helper functions can be opened by clicking this icon. They may also open if the entered data is not clear or complete. The helper functions include the Calendar Tool, Calculator Tool, Search and Info windows (See the Functionality list), and others.

Unless noted in the field notes, most fields will accept and lose the focus as the \<Tab> key is typed on the keyboard. When buttons have the focus, the buttons can be activated by typing the \<Space> key. Each field also controls the pop-up menu that appears when the mouse is right-clicked over the field.

Data entered into a field is not processed until the field loses focus or, unless noted in the field notes, the \<Enter> key is typed.

The fields and buttons are similar between the Web Application and the Java Client.

##

## FileName [![Image:Icon\_Open24.png](http://wiki.adempiere.net/images/2/2e/Icon_Open24.png)](http://wiki.adempiere.net/File:Icon_Open24.png)

The FileName control is intended to hold a file name that can be found in the local default directories. Clicking the button will open the File Chooser dialog where you can select the file of interest. You can also enter the file name in the text field directly.

## FilePath [![Image:Icon\_Open24.png](http://wiki.adempiere.net/images/2/2e/Icon_Open24.png)](http://wiki.adempiere.net/File:Icon_Open24.png)

Local File Path control is similar to the FileName control but is restricted to a directory path only - no file names. Clicking the button will open the File Chooser dialog where you can select the directory of interest. You can also enter the file path in the text field directly.

## ID [![Image:Icon\_Reset24.png](http://wiki.adempiere.net/images/a/a5/Icon_Reset24.png)](http://wiki.adempiere.net/File:Icon_Reset24.png)

The ID control identifies a specific record in a table using the \*\_ID field. The control uses a [lookup/search](http://wiki.adempiere.net/Entering_Data_-_Fields_and_Buttons#Search) to identify the record. What appears in the ID control is determined by the Identifier field selection in the [**Column Tab**](http://wiki.adempiere.net/ManPageW_TableandColumn#Tab:_Column) of the [**Table And Column Window**](http://wiki.adempiere.net/ManPageW_TableandColumn) where the \*\_ID field is the key. For example, the Value can be Identifier 1 and Name Identifier 2, appearing as Value\_Name. References (see the [**Reference Window**](http://wiki.adempiere.net/ManPageW_Reference)) can also be used to control what is displayed in particular windows/fields.

For most ID columns, the ID control will present a combo box with a list of available values. As you type text in the control, the combo box will drop down and the most likely choice will be selected. Typing \<Enter> of selecting the entry with a mouse click will save the data in the field.

If there is an Info window associated with the target table, the icon in the button will change to ([![Image:Icon\_Reset24.png](http://wiki.adempiere.net/images/a/a5/Icon_Reset24.png)](http://wiki.adempiere.net/File:Icon_Reset24.png)). Text entered in the field will be compared with common columns in the table to find a match. If no match is found, more than one match is found or the button is clicked, the associated Info window will appear. Selecting and confirming a record in the info window will cause the ID field to be filled with the associated ID. Canceling the Info window will clear the ID field. Closing the Info window will have no effect. See [Functionality](http://wiki.adempiere.net/Functionality) for a list that includes the info windows.

The following ID fields behave slightly differently:

* Product ID ([![Image:Icon\_InfoProduct24.png](http://wiki.adempiere.net/images/e/eb/Icon_InfoProduct24.png)](http://wiki.adempiere.net/File:Icon_InfoProduct24.png)): text typed into the field will be matched with the Name, Value or Search Key and SKU. If a single match is found, the ID field will be filled with that Product ID. If more than one match is found, no matches are found or the text is a wild card "%", then the [Product Info](http://wiki.adempiere.net/Product_Info) dialog will be opened. The ID field will be filled by the selected and confirmed value in the Product Info dialog. Canceling the Product Info dialog will clear the ID field. See [Product Info](http://wiki.adempiere.net/Product_Info) for more information.

The pop-up menu in a Product ID field will display the following entries:

* [![Image:Icon\_Zoom24.png](http://wiki.adempiere.net/images/7/7c/Icon_Zoom24.png)](http://wiki.adempiere.net/File:Icon_Zoom24.png) [Zoom](http://wiki.adempiere.net/Zoom)
* [![Image:Icon\_Refresh24.png](http://wiki.adempiere.net/images/2/2a/Icon_Refresh24.png)](http://wiki.adempiere.net/File:Icon_Refresh24.png) Requery
* [![Image:Icon\_ChangeLog24.png](http://wiki.adempiere.net/images/e/e1/Icon_ChangeLog24.png)](http://wiki.adempiere.net/File:Icon_ChangeLog24.png) [Change Log](http://wiki.adempiere.net/Change_Log)
* [![Image:Icon\_VPreference24.png](http://wiki.adempiere.net/images/b/b0/Icon_VPreference24.png)](http://wiki.adempiere.net/File:Icon_VPreference24.png) [Value Preference](http://wiki.adempiere.net/Value_Preference_Dialog)
* Business Partner ID ([![Image:Icon\_BPartner24.png](http://wiki.adempiere.net/images/a/a1/Icon_BPartner24.png)](http://wiki.adempiere.net/File:Icon_BPartner24.png)): text typed into the field will be matched with the Name, Value or Search Key. The search will be limited to customers or vendors depending on the nature of the transaction (IsSOTrx?) of window on which the ID is found. If a single match is found, the ID field will be filled with that Business Partner ID. If more than one match is found, no matches are found or the text is a wild card "%", then the [Business Partner Info](http://wiki.adempiere.net/Business_Partner_Info) dialog will be opened. The ID field will be filled by the selected and confirmed value in the Business Partner Info dialog. Canceling the Business Partner Info dialog will clear the ID field. See [Business Partner Info](http://wiki.adempiere.net/Business_Partner_Info) for more information.

The pop-up menu in a Business Partner ID field will display the following entries:

* [![Image:Icon\_Zoom24.png](http://wiki.adempiere.net/images/7/7c/Icon_Zoom24.png)](http://wiki.adempiere.net/File:Icon_Zoom24.png) [Zoom](http://wiki.adempiere.net/Zoom)
* [![Image:Icon\_Refresh24.png](http://wiki.adempiere.net/images/2/2a/Icon_Refresh24.png)](http://wiki.adempiere.net/File:Icon_Refresh24.png) Requery
* [![Image:Icon\_InfoBPartner24.png](http://wiki.adempiere.net/images/7/76/Icon_InfoBPartner24.png)](http://wiki.adempiere.net/File:Icon_InfoBPartner24.png) [New Record](http://wiki.adempiere.net/Business_Partner_Dialog)
* [![Image:Icon\_InfoBPartner24.png](http://wiki.adempiere.net/images/7/76/Icon_InfoBPartner24.png)](http://wiki.adempiere.net/File:Icon_InfoBPartner24.png) [Update Record](http://wiki.adempiere.net/Business_Partner_Dialog)
* [![Image:Icon\_ChangeLog24.png](http://wiki.adempiere.net/images/e/e1/Icon_ChangeLog24.png)](http://wiki.adempiere.net/File:Icon_ChangeLog24.png) [Change Log](http://wiki.adempiere.net/Change_Log)
* [![Image:Icon\_VPreference24.png](http://wiki.adempiere.net/images/b/b0/Icon_VPreference24.png)](http://wiki.adempiere.net/File:Icon_VPreference24.png) [Value Preference](http://wiki.adempiere.net/Value_Preference_Dialog)

See [Search](http://wiki.adempiere.net/Entering_Data_-_Fields_and_Buttons#Search) for more information.

## Image

Image fields can be used to display images that are stored in the database as binary data or linked to a URL. When the Image field is initially displayed, it will appear as a button with the text "-" displayed. Clicking on this button will open an Image dialog which appears as a small window as shown below.

[![](http://wiki.adempiere.net/images/2/2c/ImageDialog.png)](http://wiki.adempiere.net/File:ImageDialog.png)

The dialog has three buttons: the standard Cancel and Confirm, and a small button "-" labeled Select File. Clicking this last button will open a file chooser where you can select an image from the file system. When the image is selected and opened, it will appear in the Image dialog and the button will hold the file name. Clicking Confirm will save the image to the database. Clicking Cancel will delete any image saved in the database and close the window. Closing the window will have no effect.

Once an image is saved in the database, it will appear in the window/tab in place of the button. The image will be sized to fit within a box defined by the column width set for that column in that tab.

Clicking the image again will re-open the Image dialog with the image loaded. To delete the image, click the Cancel button. Clicking the button with the file path/name will open the file chooser where you can select another image. Click Confirm to save that image to the database.

## Integer

The Integer field is a numeric field with no fractional part and a maximum of 10 digits. See [Number](http://wiki.adempiere.net/Entering_Data_-_Fields_and_Buttons#Number) for more information.

## List

A List appears as a combo box pre-filled with values that you can select. As you type in the box, the combo box will expand to show the best choice based on what you have typed. Type \<Enter> to select it, or use the mouse to select the list entry. To set the List field to null, select the blank entry in the list.

See also

* [Search](http://wiki.adempiere.net/Entering_Data_-_Fields_and_Buttons#Search)

## Location (Address) [![Image:Icon\_Location24.png](http://wiki.adempiere.net/images/8/85/Icon_Location24.png)](http://wiki.adempiere.net/File:Icon_Location24.png)

The Location control provides a way to attach an address to a record. The Location control does not accept text directly but the button can receive the focus and can be activated from the keyboard by typing \<Space>. You can also click on the button ([![Image:Icon\_Location24.png](http://wiki.adempiere.net/images/8/85/Icon_Location24.png)](http://wiki.adempiere.net/File:Icon_Location24.png)). This will open the Location Dialog where you can specify the full address.

[![](http://wiki.adempiere.net/images/2/29/LocationAddress.gif)](http://wiki.adempiere.net/File:LocationAddress.gif)

When the Location Dialog is closed, the Location control will display a summary of the address information entered.

There is no way to fully clear the Location control once data has been entered. The pop-up menu item Delete will delete the record by clearing the entry and will open the Location Dialog. Canceling the dialog will only clear some of the information, leaving defaults in place.

The pop-up menu (right-click) provides options to:

* [![Image:Icon\_Delete24.png](http://wiki.adempiere.net/images/a/af/Icon_Delete24.png)](http://wiki.adempiere.net/File:Icon_Delete24.png) Delete
* [![Image:Icon\_ChangeLog24.png](http://wiki.adempiere.net/images/e/e1/Icon_ChangeLog24.png)](http://wiki.adempiere.net/File:Icon_ChangeLog24.png) [Change Log](http://wiki.adempiere.net/Change_Log)

## Locator (WH) [![Image:Icon\_Locator24.png](http://wiki.adempiere.net/images/a/a1/Icon_Locator24.png)](http://wiki.adempiere.net/File:Icon_Locator24.png)

The Warehouse Locator field displays the key field of a warehouse location. Both the field and the button will accept the focus.

Text typed into the Locator field will be compared to valid locations already defined. If the window already references a warehouse or a product, the locator entries will be limited to valid values for these references. If a single match is found, it will be used. If the text consists of a single percent symbol (wildcard %), no results are returned or more than one result is found, then the Locator Dialog is opened as shown below.

[![](http://wiki.adempiere.net/images/c/c1/LocatorDialog.png)](http://wiki.adempiere.net/File:LocatorDialog.png)

The Locator Dialog can be used to select an existing Locator reference or define a new one. If a new entry is defined, the Key value will be used to identify it in the Locator field.

The pop-up menu (right-click) provides options to:

* [![Image:Icon\_Zoom24.png](http://wiki.adempiere.net/images/7/7c/Icon_Zoom24.png)](http://wiki.adempiere.net/File:Icon_Zoom24.png) [Zoom](http://wiki.adempiere.net/Zoom) to the [**Warehouse & Locators Window**](http://wiki.adempiere.net/ManPageW_WarehouseLocators)
* [![Image:Icon\_Refresh24.png](http://wiki.adempiere.net/images/2/2a/Icon_Refresh24.png)](http://wiki.adempiere.net/File:Icon_Refresh24.png) Requery the field
* [![Image:Icon\_ChangeLog24.png](http://wiki.adempiere.net/images/e/e1/Icon_ChangeLog24.png)](http://wiki.adempiere.net/File:Icon_ChangeLog24.png) View the [Change Log](http://wiki.adempiere.net/Change_Log)

## Memo

The Memo field will accept character strings up to 2000 characters. It is similar to the [Text](http://wiki.adempiere.net/Entering_Data_-_Fields_and_Buttons#Text) and [String](http://wiki.adempiere.net/Entering_Data_-_Fields_and_Buttons#String) fields with the exception that it uses a text area with 80 columns width and a height of 50 rows and can't be encrypted. If the text in the field exceeds the size of the text area on the screen, scroll bars will appear.

The memo field will accept the focus but \<Tab> characters will be entered as text. Use \<Ctrl>\<Tab> or \<Ctrl>\<Shift>\<Tab> to change the focus.

Typing \<Escape> will reset the text to its previous value.

The pop-up menu includes a single entry. If the Column name is "Script", the pop-up will point to the [Script](http://wiki.adempiere.net/Script_Editor_Tool) editor. Otherwise, it will point to the text [Editor](http://wiki.adempiere.net/Text_Editor_Tool).

## Printer Name

The Printer Name field is a [String](http://wiki.adempiere.net/Entering_Data_-_Fields_and_Buttons#String) field. See [String](http://wiki.adempiere.net/Entering_Data_-_Fields_and_Buttons#String) for more information.

## Product Attribute [![Image:Icon\_PAttribute24.png](http://wiki.adempiere.net/images/c/ca/Icon_PAttribute24.png)](http://wiki.adempiere.net/File:Icon_PAttribute24.png)

The Product Attribute field or Product Attribute Instance is a field dedicated to selecting or displaying a specific instance of [Product Attributes](http://wiki.adempiere.net/Product_Attributes). It appears as a text field with an icon/button ([![Image:Icon\_PAttribute24.png](http://wiki.adempiere.net/images/c/ca/Icon_PAttribute24.png)](http://wiki.adempiere.net/File:Icon_PAttribute24.png)). The text field will not accept the focus but the button will. You can double click the field or click the button to activate the helper function and open the [Product Attribute Dialog](http://wiki.adempiere.net/Product_Attribute_Dialog).

[![](http://wiki.adempiere.net/images/a/a5/PAttributeDialog.png)](http://wiki.adempiere.net/File:PAttributeDialog.png)

The dialog displays the details of the product attribute instance. There are two controls:

* New Record (or Edit Record) - New is used when adding items to inventory. Edit is used to modify attributes on an order.
* Select an Existing Record - Used to select an existing attribute instance from inventory.

The other fields that appear depend entirely on how the [Product Attributes](http://wiki.adempiere.net/Product_Attributes) are defined.

The pop-up menu for the field will have entries to

* [![Image:Icon\_Zoom24.png](http://wiki.adempiere.net/images/7/7c/Icon_Zoom24.png)](http://wiki.adempiere.net/File:Icon_Zoom24.png) [Zoom](http://wiki.adempiere.net/Zoom)
* [![Image:Icon\_ChangeLog24.png](http://wiki.adempiere.net/images/e/e1/Icon_ChangeLog24.png)](http://wiki.adempiere.net/File:Icon_ChangeLog24.png) [Change Log](http://wiki.adempiere.net/Change_Log)

See [Product Attributes](http://wiki.adempiere.net/Product_Attributes) for more information.

## Quantity [![Image:Icon\_Calculator24.png](http://wiki.adempiere.net/images/d/db/Icon_Calculator24.png)](http://wiki.adempiere.net/File:Icon_Calculator24.png)

The Quantity field is a numeric field with a maximum of 12 digits in the fractional part and 28 digits in the integer part. See [Number](http://wiki.adempiere.net/Entering_Data_-_Fields_and_Buttons#Number) for more information.

## RowID

The Row ID Data Type is currently not active in the database.

## Search [![Image:Icon\_Reset24.png](http://wiki.adempiere.net/images/a/a5/Icon_Reset24.png)](http://wiki.adempiere.net/File:Icon_Reset24.png)

A Search Field is used to look up data. The Search field appears as a combo box with a list of available values. The text field will accept the focus but the button can only be operated by the mouse.

As you type text in the control, the combo box will drop down and the most likely choice will be selected. Typing \<Enter> of selecting the entry with a mouse click will save the data in the field.

Text entered in the field will be compared with common columns in the table to find a match. If no match is found, more than one match is found or the button is clicked, the associated Info window will appear. Selecting and confirming a record in the info window will cause the ID field to be filled with the associated ID. Canceling the Info window will clear the ID field. Closing the Info window will have no effect.

There are a few special cases:

* If the column name ends in "\_ID", it is treated as an [ID Field](http://wiki.adempiere.net/Entering_Data_-_Fields_and_Buttons#ID). There are special cases for these as well. See the [ID](http://wiki.adempiere.net/Entering_Data_-_Fields_and_Buttons#ID) field for more info.
* If there is an Info window associated with the column name, that info window will be used to perform the search. See [Functionality](http://wiki.adempiere.net/Functionality) for a list that includes the info windows.
* If none of the above, a generic [Lookup](http://wiki.adempiere.net/Lookup) form will be used.

The pop-up menu (mouse right-click) will have the following options:

* [![Image:Icon\_Zoom24.png](http://wiki.adempiere.net/images/7/7c/Icon_Zoom24.png)](http://wiki.adempiere.net/File:Icon_Zoom24.png)[Zoom](http://wiki.adempiere.net/Zoom)
* [![Image:Icon\_Refresh24.png](http://wiki.adempiere.net/images/2/2a/Icon_Refresh24.png)](http://wiki.adempiere.net/File:Icon_Refresh24.png) Requery
* [![Image:Icon\_VPreference24.png](http://wiki.adempiere.net/images/b/b0/Icon_VPreference24.png)](http://wiki.adempiere.net/File:Icon_VPreference24.png) [Value Preference](http://wiki.adempiere.net/Value_Preference_Dialog)
* [![Image:Icon\_ChangeLog24.png](http://wiki.adempiere.net/images/e/e1/Icon_ChangeLog24.png)](http://wiki.adempiere.net/File:Icon_ChangeLog24.png) [Change Log](http://wiki.adempiere.net/Change_Log)

See also

* [List](http://wiki.adempiere.net/Entering_Data_-_Fields_and_Buttons#List)
* [ID](http://wiki.adempiere.net/Entering_Data_-_Fields_and_Buttons#ID)
* [Table](http://wiki.adempiere.net/Entering_Data_-_Fields_and_Buttons#Table)
* [Table Direct](http://wiki.adempiere.net/Entering_Data_-_Fields_and_Buttons#Table_Direct)
* [Lookup](http://wiki.adempiere.net/Lookup)

## String

String fields are one of the most common types of fields in the database. A String is simply a sequence of up to 2000 characters but it is intended for shorter amounts of information.

The String field appears as a simple text field. It can accept and lose the focus with the \<Tab> key. The \<Escape> key will reset the value. It can be encrypted, like a password, if necessary and can have an "auto complete" feature enabled. It can also have special formatting applied.

The pop-up menu (right-click) provides options to:

* [![Image:Icon\_Edit24.png](http://wiki.adempiere.net/images/8/87/Icon_Edit24.png)](http://wiki.adempiere.net/File:Icon_Edit24.png) [Editor](http://wiki.adempiere.net/Text_Editor_Tool) (Launches a text editor. Appears if the string length is greater than the displayed length.)
* [![Image:Icon\_VPreference24.png](http://wiki.adempiere.net/images/b/b0/Icon_VPreference24.png)](http://wiki.adempiere.net/File:Icon_VPreference24.png) [Value Preference](http://wiki.adempiere.net/Value_Preference_Dialog)
* [![Image:Icon\_ChangeLog24.png](http://wiki.adempiere.net/images/e/e1/Icon_ChangeLog24.png)](http://wiki.adempiere.net/File:Icon_ChangeLog24.png) [Change Log](http://wiki.adempiere.net/Change_Log)

## Table

The Table data field uses a reference to look up data in a table. It behaves like the [ID](http://wiki.adempiere.net/Entering_Data_-_Fields_and_Buttons#ID) and [Search](http://wiki.adempiere.net/Entering_Data_-_Fields_and_Buttons#Search) fields. See [Search](http://wiki.adempiere.net/Entering_Data_-_Fields_and_Buttons#Search) for more information.

## Table Direct

The Table Direct data field uses a default reference to look up data in a table. It works best for tables that have defined Info windows. It behaves like the [ID](http://wiki.adempiere.net/Entering_Data_-_Fields_and_Buttons#ID) and [Search](http://wiki.adempiere.net/Entering_Data_-_Fields_and_Buttons#Search) fields. See [Search](http://wiki.adempiere.net/Entering_Data_-_Fields_and_Buttons#Search) for more information.

## Text

The Text data field is used for character strings up to 2000 characters long. It appears as a text area. It will be 2 rows high if the field length is less than 300 and three rows high otherwise. It is very similar to the [Memo](http://wiki.adempiere.net/Entering_Data_-_Fields_and_Buttons#Memo) field.

The pop-up menu includes the following options:

* [![Image:Icon\_Edit24.png](http://wiki.adempiere.net/images/8/87/Icon_Edit24.png)](http://wiki.adempiere.net/File:Icon_Edit24.png) Script Editor - if the column name is "Script" or ends with "\_Script". This will open the [Script Editor Tool](http://wiki.adempiere.net/Script_Editor_Tool)
* [![Image:Icon\_Edit24.png](http://wiki.adempiere.net/images/8/87/Icon_Edit24.png)](http://wiki.adempiere.net/File:Icon_Edit24.png) Editor - if not a Script. This will open the [Text Editor Tool](http://wiki.adempiere.net/Text_Editor_Tool)

See also

* [Memo](http://wiki.adempiere.net/Entering_Data_-_Fields_and_Buttons#Memo)
* [String](http://wiki.adempiere.net/Entering_Data_-_Fields_and_Buttons#String)
* [Script Editor Tool](http://wiki.adempiere.net/Script_Editor_Tool)
* [Text Editor Tool](http://wiki.adempiere.net/Text_Editor_Tool)

## Text Long

The Text (Long) field is intended for Text > 2000 characters in length. It is interpreted and presented as HTML text.

The pop-up control includes the following items:

* [![Image:Icon\_Edit24.png](http://wiki.adempiere.net/images/8/87/Icon_Edit24.png)](http://wiki.adempiere.net/File:Icon_Edit24.png) Editor - which brings up a rudimentary [HTML Editor Tool](http://wiki.adempiere.net/HTML_Editor_Tool)
* [![Image:Icon\_ChangeLog24.png](http://wiki.adempiere.net/images/e/e1/Icon_ChangeLog24.png)](http://wiki.adempiere.net/File:Icon_ChangeLog24.png) [Change Log](http://wiki.adempiere.net/Change_Log)

See also:

* [Memo](http://wiki.adempiere.net/Entering_Data_-_Fields_and_Buttons#Memo)
* [String](http://wiki.adempiere.net/Entering_Data_-_Fields_and_Buttons#String)
* [Text](http://wiki.adempiere.net/Entering_Data_-_Fields_and_Buttons#Text)

## Time [![Image:Icon\_Calendar24.png](http://wiki.adempiere.net/images/5/52/Icon_Calendar24.png)](http://wiki.adempiere.net/File:Icon_Calendar24.png)

The Time control is similar to the [Date](http://wiki.adempiere.net/Entering_Data_-_Fields_and_Buttons#Date) control but only shows the time component in the local format similar to h:mm:ss z or HH:mm:ss z. The text field can't be edited directly so you have to click the button to open the [Calendar Tool](http://wiki.adempiere.net/Calendar_Tool) to enter the values.

See [Date](http://wiki.adempiere.net/Entering_Data_-_Fields_and_Buttons#Date) above for more information.

## URL [![Image:Icon\_Online24.png](http://wiki.adempiere.net/images/0/0a/Icon_Online24.png)](http://wiki.adempiere.net/File:Icon_Online24.png)

The URL behaves like a [Text](http://wiki.adempiere.net/Entering_Data_-_Fields_and_Buttons#Text) field with an added helper function ([![Image:Icon\_Online24.png](http://wiki.adempiere.net/images/0/0a/Icon_Online24.png)](http://wiki.adempiere.net/File:Icon_Online24.png)). When you click the button, the software will attempt to open the text as a URL using the default browser on the system.

The pop-up menu (right-click) provides options to access:

* [![Image:Icon\_Edit24.png](http://wiki.adempiere.net/images/8/87/Icon_Edit24.png)](http://wiki.adempiere.net/File:Icon_Edit24.png) [Editor](http://wiki.adempiere.net/Text_Editor_Tool)
* [![Image:Icon\_VPreference24.png](http://wiki.adempiere.net/images/b/b0/Icon_VPreference24.png)](http://wiki.adempiere.net/File:Icon_VPreference24.png) [Value Preference](http://wiki.adempiere.net/Value_Preference_Dialog)
* [![Image:Icon\_ChangeLog24.png](http://wiki.adempiere.net/images/e/e1/Icon_ChangeLog24.png)](http://wiki.adempiere.net/File:Icon_ChangeLog24.png) [Change Log](http://wiki.adempiere.net/Change_Log)

## Yes-No

The Yes-No control appears as a Check Box.[![](http://wiki.adempiere.net/images/e/ef/Yes-no.png)](http://wiki.adempiere.net/File:Yes-no.png)

Checking the box is equivalent to Yes. Deselecting the box is equivalent to No. The data is saved in the database as the corresponding letter "Y" or "N".

The pop-up menu (right-click) provides options to access:

* [![Image:Icon\_ChangeLog24.png](http://wiki.adempiere.net/images/e/e1/Icon_ChangeLog24.png)](http://wiki.adempiere.net/File:Icon_ChangeLog24.png) [Change Log](http://wiki.adempiere.net/Change_Log)


# Account Field

The Account Field

![An Account field in the Accounting tab of the Product window.](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1rGpPpwYvov7eQJR%2Fswing_field_account_example.PNG?generation=1551809346450039\&alt=media)

Icons: ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1rGrkRP99h2vu5U9%2Faccount24.gif?generation=1551809346252294\&alt=media) ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1rGt2NOXql3eaXEU%2Finfoaccount24.webicon.png?generation=1551809346286182\&alt=media)

The Account field displays the details of a selected set of [Accounting Dimensions](https://adempiere.gitbook.io/docs/glossary#accounting-dimension) referred to as a [Combination](https://adempiere.gitbook.io/docs/glossary#combination). It is usually found on Accounting tabs which provide accounting information related to the parent tab.

The field shows a text value with the Accounting Dimensions separated by a hyphen. Dimensions that have not yet been set have an underscore as a place holder. When the Combination is used to post Accounting Facts, the values of the Dimensions will be drawn from the posted document, overwriting the placeholders and other values in the Combination and the final Combination will be used to create the Accounting Fact. The account number dimension is not overwritten.

To set a Combination, you can type in a text value or you can click on the helper button. The text that is entered will be assessed as follows:

* If the text is null, zero length or equals "%" - the wild card - , the [Account Dialog](https://adempiere.gitbook.io/docs/introduction/getting-started/dialogs-and-forms/account-dialog) will be opened.
* If the text does not end with a percent sign "%", one is added as the last character.
* The software then looks for a valid combination where the alias or the combination string match the text
* If there is a single match, the field is filled with the valid combination.
* If there is no match or more than one match, the [Account Dialog](https://adempiere.gitbook.io/docs/introduction/getting-started/dialogs-and-forms/account-dialog) is opened.

The Account Icon ([![Image:Icon\_Account24.png](http://wiki.adempiere.net/images/3/31/Icon_Account24.png)](http://wiki.adempiere.net/File:Icon_Account24.png)) can also be pressed to activate the [Account Dialog](https://adempiere.gitbook.io/docs/introduction/getting-started/dialogs-and-forms/account-dialog). A combination selected in the Account Dialog will be displayed once the dialog is confirmed and closed. If the Account Dialog is canceled, the Account field will be cleared.

The pop-up menu (mouse right-click) will display the following entry:

* [![Image:Icon\_ChangeLog24.png](http://wiki.adempiere.net/images/e/e1/Icon_ChangeLog24.png)](http://wiki.adempiere.net/File:Icon_ChangeLog24.png) [Change Log](http://wiki.adempiere.net/Change_Log)


# Assignment Field

Assignment field description

![Assignment Field example](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r-CZMvdfyTgatli%2Fswing_field_assignmentexample.PNG?generation=1551809344729523\&alt=media)

Icon: ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r-EgqIh61MMUCci%2Fassignment24.gif?generation=1551809344740125\&alt=media)

The Resource Assignment field provides a way to assign resources to schedule slots. If a resource assignment exists, the field will show the resource name, the date of the assignment and the number of slots used or it will display the resource assignment ID.

The Assignment field is typically found on the **Sales Order** window on the **Order Line** tab.

There is no way to enter data directly in the field. You have to use the helper functions. Clicking the Assignment helper function ( ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r-GBsaybgXcb9lJ%2Fassignment24.gif?generation=1551809344720715\&alt=media) ) will do the following:

* If the Assignment field is blank, it will open the [Schedule Info](http://wiki.adempiere.net/Schedule_Info) window where you can double-click on a the starting schedule slot. The double-click will open the [Resource Assignment Dialog](http://wiki.adempiere.net/Resource_Assignment_Dialog) which displays information about the assignment.
* If the assignment already exists, the [Resource Assignment Dialog](http://wiki.adempiere.net/Resource_Assignment_Dialog) will open directly.

Confirming and closing the [Resource Assignment Dialog](http://wiki.adempiere.net/Resource_Assignment_Dialog) will save the assignment to the Assignment field. Canceling the Resource Assignment Dialog will clear the Assignment field.

The pop-up menu (mouse right-click) will display the following entries:

* [![Image:Icon\_Zoom24.png](http://wiki.adempiere.net/images/7/7c/Icon_Zoom24.png)](http://wiki.adempiere.net/File:Icon_Zoom24.png) Resource Info
* [![Image:Icon\_ChangeLog24.png](http://wiki.adempiere.net/images/e/e1/Icon_ChangeLog24.png)](http://wiki.adempiere.net/File:Icon_ChangeLog24.png) Change Log

For more information see:

* Schedule Info
* Resource Info
* Resource Assignment Dialog


# Binary Data Field

Information on the function and use of the Binary Data Field

Binary Data fields can be used to store pretty much anything that can be found in a computer's file system. The binary data is stored as a BLOB or Binary Large OBject. The Binary field appears in ADempiere as a [Button](https://adempiere.gitbook.io/docs/introduction/getting-started/entering-data-fields-and-buttons/button-field). Clicking the button will open the File Chooser and allow you select a BLOB (any file) and save it to the database. The button text will show the following:

* "-" if there is no data stored
* "#xyz" where xyz is the size of the data in bytes
* The name of the class object stored
* "?" if the data is not byte data and not a class.

If a blob is already saved, clicking the button will allow you to reverse the process and save the BLOB to the file system.

ADempiere does not make direct use of Binary fields in windows and tabs but they are used by the software for [Attachments](http://wiki.adempiere.net/Attachment), Images, Migration scripts and class instances. However, nothing prevents you from using Binary fields in any custom windows and tabs you develop.


# Button Field

Use of Button fields

Buttons perform a command of some sort - starting a process, running a script or performing some other task.

The Button is defined as a field in the database, but data may not be stored there. Instead, the record in the Column definition includes information that determines how the Button is to function. There are a few special cases.

If the column name is:

* **Record\_ID** ([![Image:Icon\_Zoom24.png](http://wiki.adempiere.net/images/7/7c/Icon_Zoom24.png)](http://wiki.adempiere.net/File:Icon_Zoom24.png)), then the button performs the [Zoom](http://wiki.adempiere.net/Zoom) function, going directly to the default window and tab for that record. This is useful in situations where the current window is reporting on the status of another record, such as in the [Workflow](http://wiki.adempiere.net/Workflow) windows. The Record\_ID value is pulled from the context. There are a few special cases of this as well:
  * If the current tab does not have a Record\_ID and the key column name is "AD\_Language", the Record\_ID is set to the AD\_Language\_ID value.
  * If the current tab does not have a Record\_ID and the process associated with the Button is "Un-Do Changes" or "Re-Do Changes", then the Record\_ID is set to the AD\_Changelog\_ID.
* **PaymentRule** ([![Image:Icon\_Payment24.png](http://wiki.adempiere.net/images/1/13/Icon_Payment24.png)](http://wiki.adempiere.net/File:Icon_Payment24.png)), clicking the Button will pop-up the [Payment Dialog](https://adempiere.gitbook.io/docs/introduction/getting-started/dialogs-and-forms/payment-dialog). If the invoice is not completed, the [Payment Dialog](https://adempiere.gitbook.io/docs/introduction/getting-started/dialogs-and-forms/payment-dialog) will be limited to payments types. If the invoice is completed, the [Payment Dialog](https://adempiere.gitbook.io/docs/introduction/getting-started/dialogs-and-forms/payment-dialog) will allow you to complete a full payment. This is very useful in POS applications when using POS Orders or Credit Orders with Invoice Indirect and immediate payment. The button text will reflect the payment method chosen.
* **DocAction** ([![Image:Icon\_Process24.png](http://wiki.adempiere.net/images/e/eb/Icon_Process24.png)](http://wiki.adempiere.net/File:Icon_Process24.png)), clicking the Button will open the [Document Action Dialog](http://wiki.adempiere.net/Document_Action_Dialog). This dialog allows you to set the status (Drafted, In Progress, Completed, Closed, etc...) of the document. Changing the status will trigger the associated workflow process, if any, the document processing engine and the accounting engine. The button text will reflect the next document action in the normal workflow.
* **CreateFrom** ([![Image:Copy24.png](http://wiki.adempiere.net/images/c/c6/Copy24.png)](http://wiki.adempiere.net/File:Copy24.png)) and there is no process associated with the Button, clicking the Button will open a [Create From Dialog](http://wiki.adempiere.net/Create_From_Dialog) where lines from an associated document can be selected and used to create lines in the current document. See the [Create From Dialog](http://wiki.adempiere.net/Create_From_Dialog) page for more information.
* **Posted** ([![Image:Icon\_InfoAccount24.png](http://wiki.adempiere.net/images/b/be/Icon_InfoAccount24.png)](http://wiki.adempiere.net/File:Icon_InfoAccount24.png)) and the User's role has **Show Accounting** in the [**Role Window**](http://wiki.adempiere.net/ManPageW_Role), then if the document is processed and posted, clicking the button will open the [Account Info](http://wiki.adempiere.net/Account_Info) dialog with the Select Document set to the current document. The accounting consequences or financial accounting details of the posting will be shown. Note that the **Re-post** button will be enabled. If the document has not been posted yet, clicking the button will open a dialog that asks "Post Immediate?". Confirming this dialog will cause the record to be posted. Typically, the Posted button is hidden and will only appear once the document has been completed, closed, reversed or voided. The label of the button will reflect the status of the posting.

If none of the above apply, the software checks to see if a process is defined for the Button and attempts to run that process or invoke a custom form.


# Color Field

Using the Color field

## Color

A Color element provides a way to set a color in the database. The Color control appears as a button. Clicking the button will open a color dialog where the color properties can be set. Colors can be selected using the java swing JColorChooser tool.


# Date Field

Using the Date field

## Date ![Image:Icon\_Calendar24.png](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5fbvQ4zPvu-LU5m%2Fcalendar24.gif?generation=1550287161003296\&alt=media)

The Date control maintains data as a time stamp in a format consistent with the locale and language of the user's system. The format definitions follow the Java class [SimpleDateFormat](https://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html). If no default format is found, the JDBC standard will be used "yyyy-MM-dd". Local formats will be converted to contain at least "dd" and "MM" numbers in the format code. Year codes will be increased to at least four digits.

The Date control operates like a text field where data can be input by keyboard entry. The digit being entered is enclosed in blue square brackets and format characters are ignored - just type the numbers.

Alternatively, the [Calendar Tool ](https://adempiere.gitbook.io/docs/introduction/getting-started/dialogs-and-forms/calendar-tool)can be opened and used to enter a date.

The pop-up menu displays the following options:

* [![Image:Icon\_VPreference24.png](http://wiki.adempiere.net/images/b/b0/Icon_VPreference24.png)](http://wiki.adempiere.net/File:Icon_VPreference24.png) [Value Preference](http://wiki.adempiere.net/Value_Preference_Dialog)
* [![Image:Icon\_ChangeLog24.png](http://wiki.adempiere.net/images/e/e1/Icon_ChangeLog24.png)](http://wiki.adempiere.net/File:Icon_ChangeLog24.png) [Change Log](http://wiki.adempiere.net/Change_Log)


# Date + Time Field

Describe the use of the Date + Time field

## Date + Time ![Image:Icon\_Calendar24.png](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5fbvQ4zPvu-LU5m%2Fcalendar24.gif?generation=1550287161003296\&alt=media)

Date with time control is similar to the [Date](https://adempiere.gitbook.io/docs/introduction/getting-started/entering-data-fields-and-buttons/date-field) control but includes the time component with the full timestamp format of yyyy-MM-dd HH:mm:ss. The text field can't be edited directly so you have to click the button to open the [Calendar Tool](https://adempiere.gitbook.io/docs/introduction/getting-started/dialogs-and-forms/calendar-tool) to enter the values.

See [Date Field](https://adempiere.gitbook.io/docs/introduction/getting-started/entering-data-fields-and-buttons/date-field) for more information.


# Untitled


# Number Field

The Number field

![Number field example](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r0Ypg_4F6MXvgtg%2Fswing_field_numberexample.PNG?generation=1551809344811649\&alt=media)

Icon: ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5f__Ts1r2gj0lHJ%2Fcalculator24.gif?generation=1550287161251745\&alt=media)

Number fields provide a way to enter and display numeric values. There are several types:

* Amounts
* Costs + Prices
* Integers and
* Quantities

The default number field has a maximum of 28 digits in the integer part and 12 digits in the fractional part. The default presentation is as a float number with one digit after the decimal. The number of digits in the presentation varies with the type of field.

All the numeric fields use the [Calculator Tool](https://adempiere.gitbook.io/docs/introduction/getting-started/dialogs-and-forms/calculator-tool) as the helper function. To access the Calculator, click on the Calculator icon ( ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5f__Ts1r2gj0lHJ%2Fcalculator24.gif?generation=1550287161251745\&alt=media) ).

The pop-up menu displays the following options:

* [![Image:Icon\_VPreference24.png](http://wiki.adempiere.net/images/b/b0/Icon_VPreference24.png)](http://wiki.adempiere.net/File:Icon_VPreference24.png) [Value Preference](http://wiki.adempiere.net/Value_Preference_Dialog)
* [![Image:Icon\_ChangeLog24.png](http://wiki.adempiere.net/images/e/e1/Icon_ChangeLog24.png)](http://wiki.adempiere.net/File:Icon_ChangeLog24.png) [Change Log](http://wiki.adempiere.net/Change_Log)


# Dialogs and Forms

A list of dialogs and forms that provide specific functionality to the application.

The following pages provide detailed descriptions of the various forms and dialogs which provide functionality to the application. Here is a list with links to the pages:

* [Account Dialog](https://adempiere.gitbook.io/docs/introduction/getting-started/dialogs-and-forms/account-dialog)


# Account Dialog

The **Account Dialog** provides a method to select an account from the Chart of Accounts and add [Accounting Dimensions](https://adempiere.gitbook.io/docs/glossary#accounting-dimension), effectively creating a "Combination" of dimensions that can be used to filter and sort accounting data in useful ways. The Combination is added to the list in the [**Account Combination**](https://adempiere.github.io/functional-guide/window/window-account-combination.html) *\*\**&#x77;indow.

## Access

| Icon   | ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r-2huXh8tBbtj8P%2Faccount24.gif?generation=1551809344924053\&alt=media) ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r-4lSSgK6_EDIRa%2Finfoaccount24.webicon.png?generation=1551809344853904\&alt=media) |
| ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Field: | [Account Field](https://adempiere.gitbook.io/docs/introduction/entering-data-fields-and-buttons#account)                                                                                                                                                                                                                                                                                                                                  |

## Restrictions

To see the fields where the this dialog can be accessed, your role must have ***Show Accounting*** checked in the [**Role** ](https://adempiere.github.io/functional-guide/window/window-role.html)window.

In the Java Client, to see the Accounting Tabs where many of these fields are located, the [User Preferences](http://wiki.adempiere.net/index.php?title=User_Preferences\&action=edit\&redlink=1) must have **Show Accounting Tabs** checked.

## Description

The Account Dialog window will appear similar to the following. There are two parts to the dialog: the upper section where a "combination" is defined/created/edited and the lower section where the combination is selected and saved for use by the application.

![Account Dialog](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r-6Xyuzh8M4jpd0%2Fswing_accountdialog.PNG?generation=1551809344868627\&alt=media)

In the upper panel, the number of fields depends on the number of [Accounting Dimensions](https://adempiere.gitbook.io/docs/glossary#accounting-dimension) in use. (See also the **Account Combination**.) If a combination was already defined in the originating field, the fields in the upper panel will contain the dimension information. To the right of these fields are three buttons:

| Icon                                                                                                                                                                                                           | Function     | Description                                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5F3DVja5UAlgxyR%2Frefresh24.gif?generation=1550287161408177\&alt=media) | Requery      | Clicking this button will find all combinations that use the dimension information. The combinations found will be listed in the lower panel.                                                                                        |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5eWVJR4Lfqb-p_L%2Fundo24.gif?generation=1550287164816750\&alt=media)    | Undo Changes | Clears the definition fields in the upper panel.                                                                                                                                                                                     |
| ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5eOv7giyEZZ7sK6%2Fsave24.gif?generation=1550287167091193\&alt=media)    | Save         | Uses the definition fields to either create a combination and save it to the database or update an existing combination if a single one matches the definition fields. The saved/updated combination will appear in the lower panel. |

In the lower panel is a list of saved combinations that match the criteria in the upper panel.

At the very bottom are the two standard buttons Cancel and Confirm. Selecting a combination in the lower panel and clicking Confirm will save this combination in the originating [Account Field](http://wiki.adempiere.net/Entering_Data_-_Fields_and_Buttons#Account).

Clicking Cancel will delete the [Account Field](http://wiki.adempiere.net/Entering_Data_-_Fields_and_Buttons#Account) information.

In the window title bar, the name of the dialog and the icon shown will reflect the name and icon associated with the originating window and field.

At the bottom status bar is a reference to the Account Schema being used. On the bottom right is a indicator of the number of records found.

This dialog is opened from the Account Field when the information entered in the field does not match any or matches more than one combination OR if the button in the field was activated. To save an account combination back in the field, one must be selected from the lower panel list and the Confirm button clicked. If no suitable combination exists in the lower field, one can be created or a search performed using the upper panel.

## See Also

* [Accounting Dimensions](https://adempiere.gitbook.io/docs/glossary#accounting-dimension)
* [Account Field](https://adempiere.gitbook.io/docs/introduction/entering-data-fields-and-buttons#account)
* [Combination](https://adempiere.gitbook.io/docs/glossary#combination)
* [Account Combination Window](https://adempiere.github.io/functional-guide/window/window-account-combination.html)


# Change Log or Record Info

Describes the Change Log and Record Info dialog

![The Java Client Change Log](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r0tiuEd6h56Kaxk%2Fswing_changelog.PNG?generation=1551809344829275\&alt=media)

The Change Log or Record Info dialog displays information about the records and changes to a particular field or all fields. The top part of the dialog contains information about the field or tab of interest. The bottom part is a table listing the changes.

The Change Log is accessed:

| For a ...  | By ...                                                                                                                                                                                                                                                                  |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Field      | Clicking "![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r0vyxvSLY1YVPOI%2Fchangelog16.png?generation=1551809344888919\&alt=media) Change Log" in the pop-up menu for the field |
| Window Tab | Clicking the record count in the very bottom right of the window.                                                                                                                                                                                                       |

## Restrictions

The Change Log entry will appear in the pop-up menu for most fields but the change log will only be kept for certain windows and fields.

Changes will only be recorded if made by a user with a Role having ***Maintain Change Log*** selected.

Further, only users with a Role that has the ***Preference Level*** set to *Client Preference* will be able to see the changes in Change Log.

## See Also

* Entering Data - Fields and Buttons
* **Change Audit** window
* **Table and Column** window


# Calculator Tool

Description of the Calculator tool which is the helper function for Number fields.

The Calculator Tool is a small and simple calculator that provides simple math support to data entry for number fields. It is most commonly accessed in Number fields as the helper function.

![A Number field with the Calculator Tool as the helper function.](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1rHBNfvDfHE3OeUT%2Fswing_field_amountexample.PNG?generation=1551809346134604\&alt=media)

| Accessed through ... | In ...                      |
| -------------------- | --------------------------- |
| Helper Function      | Number Fields               |
| Java Client Menu:    | **Tools > Calculator** menu |
| Short Cut Key:       | (none)                      |
| Menu Tree            | (none)                      |

## Restrictions

None.

## Description

![Java Client version of the Calculator Tool](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1rHEaQr7HYC-7K9U%2Fswing_calculatorttool.PNG?generation=1551809346030786\&alt=media)

![Web Application version of the Calculator Tool](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1rHGfjts3eFmu2ab%2Fwebui_calculatortoo.PNG?generation=1551809346136985\&alt=media)

The calculator tool is a simple calculator that provides support for the following operators: + - \* / %. Is also can be used to perform currency conversions by clicking the '$' button. (Bottom, left. It is hard to see in yellow.)

{% hint style="info" %}
The Web Application version of the calculator is simpler and only performs basic calculations. There is no currency conversion.
{% endhint %}

In the Java Client, the calculator can be activated from the **Tools > Calculator** menu entry or by clicking on the calculator icon[![Image:Icon\_Calculator24.png](http://wiki.adempiere.net/images/d/db/Icon_Calculator24.png)](http://wiki.adempiere.net/File:Icon_Calculator24.png) in any number field.

The calculator can be operated by the mouse but it is most effective with a number pad and keyboard. The behavior between the Java Client and the Web Application is slightly different.

For the Java Client, the following keys are accepted:

* 0-9 - standard digits are added to the end of the display
* In the Java Client, '.' and ',' are both treated as decimals and replaced by '.' in the display.&#x20;
* / \* - + operands are added to the end of the display. If there is already an operand in the last position, it is replaced by the one just typed. If there is an operand between two numbers, the calculation is completed before the new operand is added.
* % operand will divide the displayed number by 100.
* \= or \<Enter> will complete the calculation. If the calculator was opened from a number field, the equal sign will close the calculator tool and the result will appear in the number field.
* 'A' or \<Delete> will clear the display.
* 'C' or \<Backspace> will remove the last character typed.
* \<Esc> or clicking the red Cancel button will abort the calculation and close the Calculator Tool.
* '$' or clicking the $ button will display the currency conversion buttons. Selecting and double clicking either currency will convert the currently displayed number.

![Java Client calculator showing the currency conversion.](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1rHI_vjDd8qAZpBD%2Fswing_calculatortoolcurrency.PNG?generation=1551809346442409\&alt=media)

For the Web Application, the calculator is simpler.

* The 0-9 - standard digits are added to the end of the display
* / \* - + operands are added to the end of the display.&#x20;
* % operand, if clicked, will divide the displayed number by 100.   If typed into the box, nothing will happen.
* \= will complete the calculation. If the calculator was opened from a number field, the equal sign will close the calculator tool and the result will appear in the number field.
* 'A' will clear the display.
* 'C' will remove the last character typed.
* Clicking outside the calculator will abort the calculation and close the Calculator Tool.
* The $ button is disabled.

## See Also

* [Number Field](https://adempiere.gitbook.io/docs/introduction/getting-started/entering-data-fields-and-buttons/number-field)


# Calendar Tool

Describes the use of the Calendar tool

## Calendar

The Calendar Tool provides a calendar to set dates and times.

### &#x20;Access

| Access via ... | By using ...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Icon:          | ![Image:Icon\_Calendar24.png](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5fbvQ4zPvu-LU5m%2Fcalendar24.gif?generation=1550287161003296\&alt=media)<img src="https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj1MQKCscAcImifHC%2Fhistoryx24.webicon.png?generation=1550780746510474&#x26;alt=media" alt="" data-size="line"> |
| Menu:          | **Tools -> Calendar**                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Short Cut:     | (none)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Menu Tree:     | (none)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

{% hint style="info" %}
The calendar can also be enabled anytime you are entering date data by clicking on the calendar icon ![Image:Icon\_Calendar24.png](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ5fbvQ4zPvu-LU5m%2Fcalendar24.gif?generation=1550287161003296\&alt=media)<img src="https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZGj1MQKCscAcImifHC%2Fhistoryx24.webicon.png?generation=1550780746510474&#x26;alt=media" alt="" data-size="line"> in the date field.
{% endhint %}

### &#x20;Restrictions

* Dates from 1 January 1900 to 31 December 2100 are allowed.
* The timezone can't be set.
* Double click speed is hard-coded to 1 second.

### &#x20;Description

The Calendar tool provides a method to find dates using a standard month calendar. There are two forms of the Calendar tool, date only or date and time, as shown below. &#x20;

| Format      | Java Client                                                                                                                                                                                                                                                                            | Web                                                                                                                                                                                                                                                                             |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Date        | <img src="https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-M-Pcq6_gW5u_6Uc2rfx%2F-M-PdAV9AuchveoVY-SD%2Fswing_calendarTool_date.png?alt=media&#x26;token=fb08704e-8b67-4b15-a26a-023dd47f83c9" alt="" data-size="original">     | <img src="https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-M-Pcq6_gW5u_6Uc2rfx%2F-M-PgxQq-nKzs-uejdE4%2Fzk_calendarTool_date.png?alt=media&#x26;token=87f658e1-75cc-4ebd-b5b3-6728cf32076a" alt="" data-size="original"> |
| Date + Time | <img src="https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-M-Pcq6_gW5u_6Uc2rfx%2F-M-PdZDKDXJLdz-m1X3Q%2Fswing_calendarTool_dateTime.png?alt=media&#x26;token=6aebf9c8-019e-4207-a3ee-3057511878bc" alt="" data-size="original"> | The Web interface uses a separate field for the time element.                                                                                                                                                                                                                   |

Which form appears depends on the data type of the field being entered. The menu link and most date fields are [date only](https://adempiere.gitbook.io/docs/introduction/getting-started/entering-data-fields-and-buttons/date-field). The time portion will appear if the data type is set to [date & time (time stamp)](http://wiki.adempiere.net/Entering_Data_-_Fields_and_Buttons#Date.2BTime).

The Web version of the control is much simpler and only allows selection of a date.

Using the Java Client Calendar tool is easy. Use the controls to select the month and year and then **double click** the date. For the date/time version, there is also a handy check mark icon which you can click.

There are three icons to assist you:

* &#x20;C - Clear - will clear the date in the date field
* &#x20;x - Cancel - close the Calendar tool, making no changes
* &#x20;\* - Today - set today's date

The following keyboard controls can be used:

* &#x20;\<Pg Dn> will increment the month
* &#x20;\<Pg Up> will decrement the month
* &#x20;\<Up Arrow> will decrement by a week
* &#x20;\<Down Arrow> will increment by a week
* &#x20;\<Left Arrow> will decrement by a day
* &#x20;\<Right Arrow> will increment by a day
* &#x20;\<Enter> will close the Calendar tool, saving the date/time if the tool was opened from a field.
* &#x20;\<Esc> will cancel the and close the tool.

### &#x20;See Also

* [Entering Data - Fields and Buttons](https://adempiere.gitbook.io/docs/introduction/getting-started/entering-data-fields-and-buttons)
* [Date Field](https://adempiere.gitbook.io/docs/introduction/getting-started/entering-data-fields-and-buttons/date-field)
* [Date + Time Field](https://adempiere.gitbook.io/docs/introduction/getting-started/entering-data-fields-and-buttons/date-+-time-field)


# Payment Dialog

The **Payment Dialog** provides a convenient way to complete a payment from a **Sales Order** or **Invoice**. It is accessed by clicking on the button for the Payment Rule which can have a number of labels but will have a payment icon such as ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r10Bp5uQ99v3g7o%2Fpayment24.gif?generation=1551809345580665\&alt=media) or ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r136t4_uiYMG3pO%2Fwebui_paymenticon.PNG?generation=1551809345516922\&alt=media).

{% hint style="info" %}
A Payment Rule is simply a description of how the order or invoice will be paid, for example, by cash, check or credit card.
{% endhint %}

![Example of the Payment Rule button in the Web App, showing the rule as Cash.](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r15d6umlxgLa93e%2Fwebui_paymentrulebutton.PNG?generation=1551809345565009\&alt=media)

This convenience is useful for sales that don't use a Point of Sale terminal and where payments are collected immediately when the order or invoice is created. It can also be used to pay Vendor Invoices. It saves the steps involved in opening the **Payment** window and filling out the fields.

The button will also appear on Purchase Orders but will be limited to changing the Payment Rule on the Purchase Order.

{% hint style="warning" %}
This is a simple dialog intended for simple cases. It is not recommended it be used to collect payments to settle a customer account, pay multiple invoices or for complex payment terms with payment schedules.
{% endhint %}

### Restrictions

There are some restrictions:

* The Payment Rule button is only accessible on Order or Invoice documents.
* The Business Partner on the Payment will be the same as on the Order or Invoice so you can't use the button to take a payment for any customer.
* The Payment Rule dialog will not open if the document status is Voided or Reversed.
* If the document status is Completed or Waiting Payment and the ***Grand Total*** field has a non-zero value, a Payment can be generated. Otherwise, only the Payment Rule can be changed.
* Only the Payment Rule can be changed on Purchase Order documents.
* The payment amount shown may not be accurate.  The payment amount shown in the dialog only looks at the base document  and does not consider the state of the Business Partners credit status or balance owing.  Payments made that do not reference this order or invoice may not be considered.

## Description

### Setting the Payment Rule

The Payment Dialog appears as a button, as shown above, displaying the payment icon (![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r1AedGXCvq_sdzP%2Fpayment24.gif?generation=1551809345568533\&alt=media)or ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r1CKeCEfaPVE-Ux%2Fwebui_paymenticon.PNG?generation=1551809345847450\&alt=media) )and labeled with the currently selected method of payment.

Clicking the button will open the Payment Dialog. If the source document is not Completed or Waiting Payment and not yet able or ready to accept payment, the Payment Dialog will appear as a combo box listing various payment rules or methods.

![Payment Dialog showing just the Payment Rule](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r1EBLNSJRnTLSvQ%2Fwebui_paymentformpaytermonly.PNG?generation=1551809345618150\&alt=media)

The Payment Methods in the combo box may vary depending on your setup but generally contain the following values:

* Cash
* Credit Card
* Direct Deposit (appears on purchase orders/vendor invoices)
* Check
* On Credit
* Direct Debit (appears on sales orders/customer invoices)

Selecting one of these Payment Methods will set the Payment Rule in the document to that value meaning the text on the Payment Rule button will change.

Below the combo box, there are two buttons:

* ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r1GqlVKfB_oYtkX%2Fwebui_iconcancel.PNG?generation=1551809345572862\&alt=media)  Cancel - this will close the dialog.
* ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r1IdwqG9VUqLYFy%2Fwebui_iconconfirm.PNG?generation=1551809345499527\&alt=media) Confirm - this will save the Payment Rule value.

## Taking a Payment

If the source document status is Completed or Waiting Payment, the Payment Rule button can be used to create and complete a payment. If a single invoice is involved, either as the source document or if related to the source Order, the payment will be allocated against the invoice.

{% hint style="info" %}
The Payment Rule button can be clicked multiple times and will create a new payment each time. This is useful for mixed payments where, say, the customer wants to pay a portion by cash and the balance by credit card.
{% endhint %}

The ***Amount*** field that appears will display the "unpaid" amount. This is calculated as follows:

* For an Order, If no Invoices are associated with the Order, the Amount will be the ***Grand Total*** of the Order less any payments made towards that Order.
* Otherwise, the Amount will be the Invoice Open Amount less any unallocated payments made towards the Order where the Order is the source document for the dialog or referenced directly from the Invoice if the Invoice is the source document.

Some payment methods can be processed online if a suitable payment processor has been configured to manage the online transactions. If a payment processor has not been configured, the online button will not function and a error will be displayed if it is clicked. Without an online process, some manual care is required to ensure that the payment record will match the actual payment.

If the payment process was successful, a dialog will appear with the message "Created Payment: \<Payment Document No>". If there was an error, an error message will be displayed.

{% hint style="warning" %}
In most cases, if there is an error, no payment is created. However, in the case where the online process succeeds but the system payment cannot be completed, the payment will be left as draft so that the user can troubleshoot the problem.
{% endhint %}

### **Cash**

Selecting the Payment Rule *Cash* will display the window shown below.

![Example of a Cash Payment](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r1KX8c8zxn7U5rw%2Fwebui_paymentformcash.PNG?generation=1551809345502988\&alt=media)

The Cash Payment requires

| Field              | Description                                                                                                                                                                                         |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ***Cash Journal*** | The Cash Journal where the resulting payment will be recorded.                                                                                                                                      |
| ***Account Date*** | The date of the accounting consequences.  This will also be used as the date of the transaction.  The date may be different than the date of the source document.  The default is the current date. |
| ***Amount***       | The remaining unpaid amount for this document.  Note the restrictions and warnings above.                                                                                                           |

On clicking Confirm (![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r1McOGDMMZXHLTE%2Fwebui_iconconfirm.PNG?generation=1551809345549453\&alt=media)), a cash payment will be created, completed and added to the selected Cash Journal. If possible, the payment will be allocated towards an invoice.

### **Check**

If *Check* is selected in the Payment Rule combo, the Payment Dialog will appear as shown below.

![Payment Dialog for a Check payment](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r1Oth2NwK2AI7PY%2Fwebui_payformcheck.PNG?generation=1551809345684880\&alt=media)

The Check Payment fields require the following

| Field              | Description                                                                                                                           |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| ***Bank Account*** | The bank account where the check will be deposited.                                                                                   |
| ***Amount***       | The amount of the payment.                                                                                                            |
| ***Routing No***   | The routing number of the source bank from the check. This is generally just used for reference but may be used in online processing. |
| ***Account No***   | The account number from the check.  Again, used for reference.                                                                        |
| ***Check No***     | The check number.  Used for reference.                                                                                                |

{% hint style="info" %}
The system can be configured to overwrite the payment document number with the check information. For a receipt, the resulting document number will look like : "\<Routing No>: \<Account No> \<Check No>. For payments, the outgoing check number will be used.
{% endhint %}

On clicking ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r1QW5g-_wdu9Whh%2Fwebui_iconconfirm.PNG?generation=1551809346257545\&alt=media) Confirm, the payment information will be saved and allocated to the invoice if possible.

### **Credit Card**

If *Credit Card* is selected in the Payment Rule combo, the Payment Dialog will appear as shown below.

![Example of a Credit Card Payment](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r1UgIU5smc633mC%2Fwebui_payformcreditcard.png?generation=1551809345599898\&alt=media)

Select the appropriate credit card type from the combo box and fill in the other text fields.

The Credit Card fields require the following

| Field                          | Description                                                                                                                                      |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| ***Credit Card***              | Select the credit card type.  These are configured and associated with Bank Accounts.  The list will only include Credit Cards that are accepted |
| ***Name***                     | The card holder name as it appears on the card                                                                                                   |
| ***Number***                   | The card number                                                                                                                                  |
| ***Expires (MMYY)***           | The credit card expiry month and year using the four character MMYY format                                                                       |
| ***Amount***                   | The amount of the payment                                                                                                                        |
| ***Voice Authorization Code*** | When the credit card payment is taken manually and a phone authorization code is received, the code can be entered here for reference.           |

Clicking the "Online" button will attempt to process the credit card information online through the associated payment processor.

### **Direct Debit / Deposit**

If *Direct Debit* or *Direct Deposit* is selected in the Payment Rule combo, the Payment Dialog will appear as shown below. The term debit / deposit will be used with sales orders / purchase orders respectively.

![Example Direct Debit payment.](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r1YHRW_aeWrAEcD%2Fwebui_payformdirectdebit.png?generation=1551809345545619\&alt=media)

The required fields are:

| Fields                     | Description                                                                                                                                   |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| ***Partner Bank Account*** | For Direct debits and deposits, a target bank account is required.  This is defined in the **Business Partner** window, **Bank Account** tab. |
| ***Amount***               | The amount of the payment.                                                                                                                    |

Clicking the Online button will attempt to process the payment online if a suitable payment processor is configured.

Clicking the confirm button will simply create a payment record but will not process the payment online.

### **On Credit**

The On Credit payment will only update the payment terms of the order or invoice. No payment is created.

![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r1aODUQw0JxIhsc%2Fwebui_payformoncredit.png?generation=1551809345782130\&alt=media)


# Key Concepts

A number of key concepts that are important to understand when working with ADempiere

## Clients, Organizations & Users

ADempiere is built on an organizational model where the **Client** is the highest level of an independent business entity. Each Client will have one or more **Organizations** reporting to it. The Client defines the accounting parameters (Accounting Schema, Tree definition, Non Monetary UOM's) that are used by all the Organizations under that client. An **Organization** is a legal entity (business) with its own banking, and business processes. Each Organization can have a number of **Users**. The **Users** can be restricted to an organization, multiple organizations or the client through **Roles**.

When you login to ADempiere, you are logging in as a User with a specific Role into a specific Client and Organization.

Any implementation of ADempiere for a business starts with creating the Client. See [Creating the Client](http://wiki.adempiere.net/index.php?title=Creating_the_Client\&action=edit\&redlink=1).

## Security: Users and Roles

Users are defined as business partner contacts where the business partner is an employee and the user has a password defined. There needs to be a single business partner for each user.

ADempiere implements security through roles which define what elements of the data, menu, processes etc each user has access to. While the administration role may see all aspects of the system and a menu of over 700 entries, a particular functional role may see a menu with a small handful of windows and reports. Roles also help define the workflow and approval levels of the users.

There are a few special users and roles:

* The System user controls the application dictionary and a few other configuration items for the application. The system user can not access client data.
* SuperUser is a system level user that has access to all clients and can access any role.
* For each client, there is an administration user and role created when the client is created and a more restricted user and role.

## Accounting Schema, Combinations, Defaults and keeping track of the money

ADempiere is designed to work with multiple sets of books or "Accounting Schema". Every process that creates accounting consequences does so in all the schema. Schema can be based in different currencies or apply different rules and accounting for a given circumstance.

One of the key benefits of ADempiere is the manner in which accounting consequences are defined. Rather than a single number signifying an account, ADempiere uses a number of fields to generate references to the accounting data. These fields include the traditional account number but add business partners, products, organizations, projects, and other "dimensions". This makes it easy to generate reports or lists of accounting consequences by filtering the various dimensions.

A particular set of dimensions is called a combination and the combinations usually include placeholders for dimensions that will be filled in when a particular transaction takes place. For example the combination defined for product revenue will specify the revenue account but have place holders for the product. The product information will be added when an invoice is completed.

It is important when establishing a new client to completely define the default combinations required by the system in the initial Chart of Accounts. This is a key part of creating a new client. See [Chart of Accounts](http://wiki.adempiere.net/Chart_of_Accounts) for more information.

## Documents and Document Processing

ADempiere is a process and document based system. The processes in the software mimic a document workflow of generation, checks and approvals, action and follow-up. The documents also go through stages of preparation from draft, to prepared, to complete. They can also be voided, reversed and so on.

Most documents, when they are completed, create some accounting consequences in the system. The consequences are created when the document is "posted" and the process that happens is particular to the document. It is important to understand that no accounting consequences can be created without a document and that any consequence or accounting entry can be traced back to the document that generated it.

The document processing is defined by workflows and every document has one. Workflows can be fully automated with documents created and processed behind the scenes with no user intervention. It is also possible to create complex multi-level approval workflows to manage and provide oversight and control with the documents passed from user to supervisor and back.

Another powerful feature of ADempiere is the inter-organizational transactions that can take place. Where there are multiple organizations for the client, it is possible for the organizations to "do business" with each other. Behind the scenes, when a document is created in one organization, say a Purchase Order, a counter document, in this case a Sales Order, is automatically created in the other organization. A Shipment in one organization generates a Material Receipt in the other and so on. These counter documents ensure that the accounting across the client is consistent and it also saves a lot of time.

## Database Tables and Common Fields

In ADempiere, most database tables contain a set of common fields that are used by most windows or by the underlying rules and software. These are:

| Field                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ***Client***                       | A Client is a company or a legal entity.  The Client is created by the System Administrator. Where a server hosts several Clients, any data created for or by one Client cannot be shared with any other client.  The Client is determined when you log into the system.                                                                                                                                                                                                                                                                                                                                                                                                 |
| ***Organization***                 | Within a Client there can be one or more Organizations.  An Organization is a unit of the Client.  Examples are stores, departments.  Data can be shared between Organizations.  Depending on your Role, you may have access to all, some or only one Organization.                                                                                                                                                                                                                                                                                                                                                                                                      |
| ***Created*** and ***Created By*** | These fields are included with nearly every record in the system and record the timestamp of when a record was created and which user was responsible for creating it.  These fields are not usually shown in windows or forms but are available for audits.                                                                                                                                                                                                                                                                                                                                                                                                             |
| ***Active***                       | A check box which indicates the that record is active in the system.  There are two methods of making records unavailable in the system: One is to delete the record, the other is to de-activate the record. A de-activated record is not available for selection, but available for reports. There are two reasons for de-activating and not deleting records: (1) The system requires the record for audit purposes. (2) The record is referenced by other records. E.g., you cannot delete a Business Partner, if there are invoices for this partner record existing. You de-activate the Business Partner and prevent that this record is used for future entries. |
| ***Search Key***                   | A key value for the record in the format required. It provides a fast way of finding a particular record.  The value must be unique but can often be chosen by the user.  If you leave the ***Search Key*** field empty, the system automatically creates a numeric number for it when the record is saved. The sequence used for this fallback number is defined in the **Document Sequence** window with the name "DocumentNo\_\<TableName>", where TableName is the actual name of the table (e.g. C\_Order).                                                                                                                                                         |
| ***Name***                         | An alphanumeric identifier of the record.  The ***Name*** field is used as a default search option in addition to the ***Search Key***. The name can be up to 60 characters long.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ***Description***                  | An optional short description of the record, limited to 255 characters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ***Comment/Help***                 | An optional comment, hint or help about the use of the record.  The text can be up to 2,000 characters long.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ***Updated, Updated By***          | Like ***Created/Created By***, these fields record the timestamp of the last change made to the record and the user responsible for the change.  These fields are not included on most windows and forms but are available for audits.                                                                                                                                                                                                                                                                                                                                                                                                                                   |

## Record Identifiers

When a field displays information linked to another window or tab, for example a ***Product*** field in a Sales **Order Line**, the ***Product*** field is displayed using an Identifier that can include one or more fields from the **Product** window. These fields are selected and given a sequence by the System Administrator. The default is often \<Search Key>\_\<Name> but it can be configured to include other useful fields.


# Workflow Activities


# Workflow


# Windows and Tabs


# Reports and Processes


# Garden World Demonstration Client

This page describes the Garden World Demonstration Client which is included with the ADempiere installation.

## Garden World   <a href="#firstheading" id="firstheading"></a>

Garden World is a demonstration business that exists as a Client in the ADempiere database. It can be used a demonstration, a sandbox to try business processes or a learning tool. Garden World comes prepared with products, vendors and customers.

### Setup

Before Garden World can be used as a demo, a few steps should be followed to generate data that is normally generated by the ADempiere server but which has been eliminated from the seed database to reduce space:

* (Before version 3.8.0) **Turn on Immediate posting:** Log in as System (System/System/System Administrator) and open the [**System Configurator Window**](http://wiki.adempiere.net/ManPageW_SystemConfigurator) in the **System Admin > General Rules > System Rules** menu. Find the "CLIENT\_ACCOUNTING" record and change its ***Value*** field to "I". Save the record and log out.

{% hint style="info" %}
By default, documents are posted by the server in an process that occurs at a regular schedule so that the processing doesn't impact operations. For demonstrations, its handy to have the posting data available immediately.
{% endhint %}

* (Before version 3.8.0) **Set the Garden World client to "Immediate Costing":** Log in as GardenAdmin (GardenAdmin/GardenAdmin/Garden Administrator) and open the [**Client Window**](http://wiki.adempiere.net/ManPageW_Client) window in the **System Admin→Client Rules**. Select the checkbox for "Cost Immediately".
* **Generate Cost Transactions:** Select the **Generate Cost Transactions** process in the **Performance Analysis→Costing** menu. Set all the fields to blank and the date to '01/01/1999' then run the process.
* **Run the Client Accounting Processor:** Select the **Client Accounting Processor** process in the **Performance Analysis→Accounting Rules** menu. Set all the fields to blank and then run the process.

### Description

Garden World is a national retail and manufacturing enterprise with a headquarters, a plant that makes fertilizer, and five stores spread across the country. It has a central warehouse at the headquarters which distributes goods to the plant and store warehouses. The company sells plants, fertilizer, lawn furniture and tools.

### A Simple Process to Start

Log into the Garden World Client with User ID GardenAdmin and password GardenAdmin. Select the Organization field "Store Central" and Warehouse field "Store Central".

When the log-in completes, you will be presented with a performance screen and a menu of options. For a quick sample of how the software works, try the following:

* Find and open the Sales Order in the menu under **Quote-to-Invoice>Sales Orders > Sales Order**.
* Create a new Sales order (click on the New Record ( ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ9rq_giAzifgNjK0%2Fnew16.gif?generation=1550287156485373\&alt=media) ) icon).
* Set the following fields:
  * Business Partner to Joe Block
* Save the record (click on the Save Record ( ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ9rsM_HeVexXbnux%2Fsave16.gif?generation=1550287156868846\&alt=media) ) icon). This completes the order header.
* Click on the Order Line tab.
* In the product field, enter "Oak" and \<tab> or \<enter>. It should find an Oak Tree product and set the prices accordingly.
* Save the record.
* Return to the Order header tab and scroll to the bottom. Note the totals are set.
* Click on the "Complete" button and select "Complete" in the dialog and click on OK ( ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ91a8kKlMklOa3NB%2Fok16.gif?generation=1550287155453533\&alt=media) ).

Congratulations, you've made your first sale with ADempiere!

Now, lets look at what has happened behind the scenes.

On the Order header, you'll note that the document type you just completed is a "POS Order" or Point of Sale order. This is the sort of document that would be completed at a cash register where a customer would buy and carry their item out of the store. (There are even faster ways of doing this with special POS software but behind the scenes, the same document would get completed.) There is no need for shipping or invoices and other complications. But these documents are needed by the system. For the POS Order, they are completed automatically. To see them, click the Zoom Across ( ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ9ruhKsvUL9lSfwl%2Fzoomacross16.gif?generation=1550287156612809\&alt=media) ) icon. You'll note a shipment and an invoice. So you have actually completed three documents with this single transaction:

* A Sales Order which has no accounting consequences (or Facts) on its own, unless you set your system to do Commitment Accounting;
* A Shipment which debits the sold item from inventory and
* A Customer Invoice which recognizes the revenue and charges the customer account payable.

To see the Accounting Facts of each document, you can click on the "Posted" button. (If the button says "Not Posted", you need to perform the setup steps above or you can click the button and manually post the document.) The Info Account window opens showing the accounting entries. For the Sales Order, these will be blank, but for the Shipment and Invoice, you'll note the accounting entries that took place.

The rest of the User Guide will use examples from the Garden World Client to illustrate concepts and processes. You can also use the Garden World Client as a sandbox to experiment and try out things without impacting any real production data.


# Untitled


# System Administration


# General Rules


# System Rules

## Trees and Tree Maintenance

Trees are collections and organizations of data using a summary and child structure. They are primarily used in financial reporting to summarize information in useful ways.

Each Accounting Dimension, such as Product, can have multiple trees and which tree gets used in a report is defined in a Reporting Hierarchy. Financial Reports are defined in lines and columns that can use the summary level elements of the tree. For example, in the Garden World Balance Sheet, there is a Reporting Line for Cash and the Account Element Value is set to 11 - Cash. This is a summary level account and the line value on the report would include all activity in all the subordinate accounts shown in the tree below.

![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZ5G1bjZ0BFZHjQciW2%2F-LZ5G4DmkN1YdNe9ZO0O%2Fimage%20\(10\).png?generation=1550588336739443\&alt=media)

Each Accounting Dimension requires at least one tree and the default trees are used if no Reporting Hierarchy is selected.

Where it is important to have multiple trees, a Reporting Hierarchy can be created to define the collection of trees to use in a given report. You can use the trees and reporting hierarchy to change the meaning of the summary product or to use different summary products.

For example, in Garden World, suppose it is important to report only on the sale of plants. A summary level product "Plants" could be created and the Product tree modified to group the various "plant" Products under the Summary Level Product. Then a financial Report Line Set or Report Column Set could be created that referenced this summary product and the "Plant Results" financial report would only shows results for the "plant" products. If it was important to show only "tree" plants, you could create a new product tree and hierarchy where the Plants summary level product only had "tree" type products as children. More realistically, you may need to use different categorizations altogether rather than subsets, such as New versus Legacy products in one tree and Plants, Tools, Furniture, Misc in another.


# Security


# Defining Users and Contacts

Describes how to setup Users and Contacts

Users are an important aspect of the ADempiere Application. The Application tracks every action taken by users and ensures the security of the data and process by ensuring that users only see what they are allowed to see and can only change what they are allowed to change.

There are two types of Users of the ADempiere Application: Users who represent customers or vendors and who may have access to the web store; and Users who access the Client and Application data. The first type is also considered a Contact of a Business Partner.

{% hint style="info" %}
Contacts can also be added and managed through the **Contacts** tab of the **Business Partner** window found in the **Partner Relations > Business Partner Rules** menu.
{% endhint %}

For security, every User who is to have access to the Application must be assigned at least one Role in the Client.


# Roles and Managing Data Access

## User Level

The user level determines the extent of information the User has access to. The possible settings and limitations are shown in the table below. Organization access is controlled via the fields ***Access All Orgs***, ***Use User Org Access*** and through the **Org Access** tab in the **Role** window. Table access levels are set by the System Administrator but can be further restricted by Role in the **Role Data Access** window.

{% hint style="info" %}
Organizations are specified by name except for a special organization identified by the asterisk symbol (\*) which means All Organizations.
{% endhint %}

| Users with this Level... | Can update records from the ...                          | and can view tables with Access Level ...                                                   |
| ------------------------ | -------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Client                   | Login Client and all Organizations (\*)                  | <p>All,<br>Client Only,<br>Client + Organization,<br>System + Client</p>                    |
| Client + Organization    | Login Client and all allowed Organizations, including \* | <p>All,<br>Client Only,<br>Organization,<br>Client + Organization</p><p>System + Client</p> |
| Organization             | Login Client and all allowed Organizations except \*     | <p>All,</p><p>Organization,<br>Client + Organization</p>                                    |
| System                   | System Client and Organization \*                        | <p>All,<br>System Only,<br>System + Client</p>                                              |


# Dashboard Access

Describes how to enable the display of Dashboard items to the User.

When a User logs in to the Web Application, the Menu tab contains a [Dashboard](https://adempiere.gitbook.io/docs/introduction/getting-started/finding-your-way-around-the-web-app/untitled) which displays information relevant to the User and their Role. The information that is displayed is unique to each Role and is set in the in the **Role** window, **Dashboard Access** tab found in the **System Administration > General Rules > Security** menu. This is a simple tab that involves adding records and selecting the desired ***Dashboard Content***  to display.


# Role Access Update

Describes the Role Access Update process

When changes are made to the Application Dictionary such as creating new menu items or windows, the user roles that need to use these new entries have to be updated to have access to them.  The easiest way of doing so is to update the roles using the Role Access Update process.

The Process is found in the **System Administration -> General Rules -> Security** menu as the **Role Access Update** process.

This process takes two parameters:

* **Client**; and
* **Role**

To update a single role, select that role in the **Role** parameter.  To update all roles for a Client, leave the **Role** parameter blank.&#x20;

To update all roles in all clients, set the **Client** parameter to "*System*". &#x20;


# Server


# EMail Configuration

The ADempiere Application can communicate through email if the email is configured properly. The System Administrator sets the System level email for support and server-level communications. Each Client can setup individual email configurations for use by the Client processes.

Email configurations are created on the **EMail Configuration** window found in the **System > General Rules > Server** menu. The fields should be self-explanatory for anyone familiar with adding an e-mail account to an application. ADempiere supports SMTP, IMAP or POP3 Protocols. Check with your email provider for the correct email configuration settings to use.

Once the email configuration is saved, select the configuration in the **Client** window/tab in the ***EMail Configuration*** field. Complete the configuration by adding the ***Request EMail*** , the ***Request User*** and the ***Request User Password***. These three fields are used when Client sends emails as the "From" addressee.

You can test the configuration by clicking the "Test Email" button in the Form View. A test email is sent from the Request Email to the Request Email.

{% hint style="info" %}
The Test Email process will also check that the ***Request Folder*** exists and will send test emails from any Web Store record that has a Web Store EMail defined.
{% endhint %}


# Managing the Client


# Configuring the Client Password Reset

Describes the steps necessary to configure the Password Reset functionality.

Password Reset is a common feature in applications. In ADempiere, users can request a new password if they have forgotten their current one. There is a bit of configuration required to make this work though. In particular:

* The Client must have a valid email configuration setup. (See [Email Configuration](https://adempiere.gitbook.io/docs/introduction/system-administration/general-rules/server/email-configuration));
* The User must already have an account and have a valid email address;
* A **Mail Template** for a "restore password" email that will be sent to the user has to exist and must include a link to the password reset web page (the system account provides an example of this email); and
* The **Client Info** tab in the **Client** window has to identify the email template in the ***Restore Password Mail Text***  field.
* The Web application must be accessible to the user via a browser in order to complete the password reset process.

{% hint style="info" %}
Password reset is not available in the Java Client application.
{% endhint %}

The User requests a password reset through the login dialog. (See [Logging In](https://adempiere.gitbook.io/docs/introduction/getting-started/logging-in).) If they submit a valid User ID, the system will send them a email with a link to a web page where they can reset their password.

The password reset is made using a Token which grants the User access to change their password. The tokens granted can be viewed in the **Token for Access** window in the **System Admin > General Rules > Security** menu.

{% hint style="warning" %}
The Token expires in 5 minutes.
{% endhint %}


# Managing Organizations


# Document Status Indicators

Describes how to configure the document status indicators in the Dashboard Document Tasks panel

The Web Application dashboard includes a panel showing Document Tasks as shown below.

![Dashboard Document tasks panel](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJ9vtCKO6mt2Z4eXD%2Fwebui_dashboard_doctasks.PNG?generation=1550287157761043\&alt=media)

The information displayed to the User is configured in the **Document Status Indicator** window in the **System Administration > Organizational Rules** menu. Access to the Document Tasks panel in the Dashboard also has to be enabled for the User in the **Role** window, **Dashboard Access** tab found in the **System Administration > General Rules > Security** menu.

{% hint style="warning" %}
Configuring Document Status Indicators requires an understanding of the underlying database tables and columns which represent "documents" in ADempiere and SQL queries.
{% endhint %}

![Document Status Indicator window](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJAeL2c3Pq7y3HBJV%2Fwebui_win_documentstatusindicator.PNG?generation=1550287167492757\&alt=media)

There can be many Document Status Indicator records for an Organization or Client. The selection of which indicators are displayed to a particular User is based on the following:

* Only ***Active*** indicators are shown
* From the same ***Client***
* Where the ***User/Contact*** field is blank or matches the User
* AND where the **Role** field is blank or matches the User's Role.

The sequence that the indicators are shown in is determined by the ***Sequence*** field, with lower numbers being shown first.

The ***Table*** **\*\*field identifies the document of interest and the \_**&#x53;QL Where ***field selects the relevant document records from the*** Table\*\*\_.

The display in the Document Tasks panel is a count of the documents of interest. The link beside the number is based on the ***Name*** field.

{% hint style="warning" %}
The name field is not translated.
{% endhint %}

The count of the documents and the link to those documents is made using an SQL Where clause that is constructed from the ***SQL Where*** field plus a few other constraints:

* Only documents within the same ***Client***
* If the ***Organization*** field is not All (**\***), then only documents that match the ***Organization***
* If the **Projec**t field is not blank, then only documents that match that **Project**

If the User clicks on a status indicator and a ***Window*** is specified, the window will be opened and loaded with the selected documents. If the ***Window*** field is blank and the ***Special Form*** field identifies a form, the form will be opened and loaded with the documents.

{% hint style="warning" %}
If both the ***Window*** and ***Special Form*** fields are blank, nothing will happen when the User clicks on the link in the Document Status panel.
{% endhint %}

{% hint style="info" %}
The ***Name Font***, ***Name Color***, ***Number Font*** and ***Number Color*** fields are not used.
{% endhint %}

## Example - Unpaid AR Invoices

As an example using the Garden World client, assume that Garden User needs to see unpaid invoices to ensure payment allocations are made and to personally dun (collect) the amount owed. The GardenAdmin user is not interested in this. The Document task panel for the GardenUser should look like the following:

![GardenUser Dashboard entry for Document tasks showing the Unpaid Invoices entry](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LYoJAeP7PkscydhmAf6%2Fwebui_dashboard_doctaskexample.PNG?generation=1550287167442464\&alt=media)

1. Login as GardenAdmin and the GardenAdmin role.
2. Open the **Document Status Indicator** window and create a new record.  Set the fields as follows and save the record.:
   1. ***Client*** - will default to Garden World
   2. ***Organization*** - \*
   3. ***Name*** - Unpaid Invoices
   4. ***User*** - GardenUser
   5. ***Sequence*** - 10
   6. ***Table*** - C\_Invoice
   7. ***SQL Where*** - C\_Invoice.IsSOTrx='Y' AND C\_Invoice.DocStatus='CO' AND C\_Invoice.IsPaid='N' AND PaymentTermDueDays(C\_Invoice.C\_PaymentTerm\_ID, C\_Invoice.DateInvoiced, getdate()) > 0
   8. ***Window*** - Invoice (Customer)
3. Verify that a **Dashboard Content Edit** entry exists for the *Document tasks*. The System Client entry will do.
4. Open the **Role** window and find the record for the *GardenWorld User* role.
   1. In the **Dashboard Access** tab, add an entry and set the ***Dashboard Content*** to *Document tasks*, if it doesn't already exist. Save the record.
5. Verify that there are paid and unpaid/due customer invoices in the system. Create some if necessary.
6. Log in as GardenUser and verify that the *Document tasks* panel shows the correct number of unpaid invoices.  Click on the link and ensure that only unpaid invoices appear in the **Invoice (Customer)** window when it opens.
7. Make a full payment to one of the invoices.  Return to the dashboard and verify that the *Document tasks* entry has been updated. (Note that it may take a minute to update.  The dashboard refresh happens every 60 seconds.)
8. Log in as GardenAdmin, verify that the "Unpaid Invoices" item does not appear in the *Document tasks* panel.

   .


# Data

About data import and utilities


# Data Import

How to import data into the ADempiere Application.

## Introduction

The Data Import features of ADempiere allow you to import data into the database as part of the process of establishing opening balances, entering historical data or for routine entry of orders, invoices and general journal entries. Importing of bank statements is covered in the [Banking](http://wiki.adempiere.net/Banking) page.

The data import process has two main steps. Data is read into the system and placed in a temporary table. From there it is processed and entered into the main database. The two step process helps prevent errors in the data from affecting the main database. The first step of importing the data requires a definition of the data file that will be imported and information about where to put it in the temporary tables. This is performed by an Import File Loader and an Import Loader Format.

## Import Loader Format

The **Import Loader Format** Window is simply a window that defines the target intermediate table and a list of the fields that are to imported. In the **Import Format** Tab, you define both the import table and the format of the data to be imported.

The following import tables are available as a default:

* Business Partner
* Product ASI
* Product BOM
* Product
* Product Planning
* Price List
* Workflow
* Account
* Budget
* Report Line Set
* Inventory
* Employee Data
* Inventory Move
* Order
* Invoice
* Confirmations
* Currency Rate
* GL Journal
* Sales History
* Financial Agreement
* Payment
* Payroll Movement
* Fixed Asset
* Bank Statement
* Attendance Record
* Employee Attribute

This is simply a list of all tables in the database with the prefix I\_. (See the validation rule AD\_Table Import Tables.) If, for example, the target table was C\_BPartner, the import table would be I\_BPartner. The relation with the target table is not one-to-one. The import tables are used to create subordinate information as well. The I\_Invoice table is used to create invoice headers and lines. The I\_GLJournal table is used to create journal batches, journal entries and the journal line items. While you can add tables simply, the processing required to import the data from the import table to the target table(s) is involved and the subject of other articles. See the section For Developers

The import formats supported for the data file you wish to import include:

* Comma Separated (CSV)
* Custom Separator Char
* Fixed Position and
* Tab Separated

### Creating an Import Loader Format

To create a new Import Loader Format based on your data, login to your client and browse to **System Admin » Data » Import Loader Format**. This will open the **Import Loader Format** Window. Create a new record, give it a name and description of your choice then pick the import Table and the format of your data file. Move to the **Format Field** Tab.

{% hint style="info" %}
It is helpful to give the Import Loader Format a name similar to the import data file. A leading number in the name can help keep the order of imports straight. For example, the csv file is called "0 - Opening Trial Balance.csv" and the Import Loader Format name is set to "0 - Opening Trial Balance". This makes it easy to deal with lots of import files and their associated formats.
{% endhint %}

The Import Format Tab is where you connect the data you want to import to the columns in the import table. An example will help here.

Suppose you have a list of invoices to import. Your list is in a spreadsheet which contains all the necessary columns. The Search Key/Values used in the spreadsheet match those already in the ADempiere database for the Business Partners and Products. (If they don't, you will have to use an intermediate table to translate the key values. More on that later.) In this case, you can simply define a row in the Import Format tab for each column of data in the spreadsheet. Pay attention to the following:

| Field Name     | Description                                                                                                                                                                                                                                                                                                                                                                                                    |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ***Start No*** | The ***Start No*** field is important since it determines where to look for the record data. For a CSV file, it is the column number, with the first (left most) column being 1.                                                                                                                                                                                                                               |
| ***Sequence*** | The ***Sequence*** field simply provides another way to order the records. It has no other purpose. It is helpful to use it to keep the rows in the Import Format tab in the same order as the columns in the spreadsheet. Use the Start No or multiply by ten. For example, if you have data in columns 1, 2, 4, 7, 8 and 9 that should be imported, set the sequence to 10, 20, 40, 70, 80, 90 respectively. |

{% hint style="warning" %}
If the ***Data Type*** is "Date", be sure to indicate the format and watch for differences between systems, such as dd/mm/yy vs. mm/dd/yy.
{% endhint %}

As you create the Import Loader Format, it is helpful to create header rows in your spreadsheet that match the ***Start No*** and ***Name*** columns. Then, in the Import File Loader, when the csv file and the loader format are selected, the first two rows you see in the import loader form will be the spreadsheet headings and you can quickly compare those values with the form column headings. When columns contain an ID it is hard to know what ID it is so the column description can highlight errors.&#x20;

To get rid of this test data, you can then either:

* delete the two rows and resave the data file;
* add another sheet to the workbook that displays all the data from the first except for the header rows and then only save that sheet as a CSV file; or
* import the data as is and delete the first two rows in the Import table before you process it.

## Preparing the data for Import

In an ideal world, you want to perform the data import to the intermediate table without errors and then process the intermediate table, also without errors. Errors within ADempiere take more effort to fix than applying the same corrections to a spreadsheet. So, if at all possible, prepare the data in a spreadsheet before attempting the import.

{% hint style="info" %}
If you have too much data to deal with or no control over the format, you may have to consider developing a customer import loader - a software process.&#x20;
{% endhint %}

To properly prepare the data, it is important to understand the import process and what the Import File Loader and the Import processes are looking for.

{% hint style="info" %}
First, review the concepts of [Database Tables and Common Fields](https://adempiere.gitbook.io/docs/getting-started/key-concepts#database-tables-and-common-fields).
{% endhint %}

### Understanding the Import Process

Assuming your data has been read properly by the Import File Loader and is now sitting in the Import Table, when you press the button to perform the import, the import processes generally follow this sequence:

* For each record in the import data table that has not previously been imported, the software assigns default values to the mandatory fields (***Client***, ***Organization***, ***Created***, ***CreatedBy***, ***IsActive***, ***Updated***, ***UpdatedBy***) and sets two other fields: ***Import Error Message*** to blank ("") and ***Is Imported***  to "N".
* The software then tests the import field values, looking for matches with the information required in the database.
* If supporting records don't exist, they may be created: for example, the business partner identified on an invoice may be created if it doesn't already exist.
* As the software progresses and at the end, it tests for errors. If one is found, a suitable error message is saved in the field ***Import Error Message***.
* Where there are no errors, the necessary data records are created in the database and the Import record field ***Is Imported*** is set to 'Y'.

### **IDs and Value Fields**

It is important to understand the differences between the ***Value/Search Key***, ***Name*** and ***ID*** fields. The ID fields are usually hidden numerical keys that distinguish one record from another. Their value is controlled by the software and they are generally not available for searches. The Value fields, on the other hand, are visible, often updateable and frequently used as the unique key for searches.

For example, a Business Partner in the database may have a ***Name*** "C\&W Construction", a ***Value*** "C\&W" and a ***C\_BPartner\_ID*** field = 117.

When you import a table directly, the ID field is assigned by the software and you can set the key value to what ever you want. It is pretty straight forward. However, if you want to link your import data to data that is already existing in the database, for example connecting an invoice to a business partner such as "C\&W Construction", you have to import the Value field "C\&W" or Name so the software can link that to the C\_BPartner\_ID field 117.

If you know them, it is possible to import the ID values for the \*\_ID columns in the import table, but only for records that already exist in the database. The loader software that determines if data needs to be added only tests the existence of records where the ID value is null. In other words, if you set the ID value, the Import Loader will assume a record with that ID exists and flag errors when it can't find it.

The same approach applies to many of the look-up or reference fields. The database may use hidden keys for these fields that need to be matched by name. To import matching data, you have to know the name, not the key.

In some cases, if related records are not already in the database, the import process will try to create them. For example, if unknown business partners are referenced in imported invoice data, the business partners will be added to the database using the available information from the invoice import.

### **Cross Linking Data**

Where the import data uses different data formats than the database, you may need to perform a data translation using intermediate tables that relate the keys in the external data to the keys in the database. An example is where the source system for the data uses entirely different keys, values and names to describe records than ADempiere. A translation table provides a mechanism to find the ADempiere Search Key based on the source name or key value.&#x20;

In another actual example, an ADempiere installation replaced a POS/AR system that was run in parallel with Quickbooks. Here the issues was that the POS system and Quickbooks used different customer formats entirely. Linking was performed based on the corporate memory of the book keeper. ADempiere was loaded with Business Partners from Quickbooks but the AR invoices and payments had to use translation tables to ensure the debits and credits were charged to the correct accounts. In addition the Quickbooks chart of accounts was different than the ADempiere chart of accounts so translation was also required when importing trial balances and journal entries.

{% hint style="info" %}
In practical terms, the intermediate table could be another spreadsheet in your import data workbook where the final import data spreadsheet uses the VLookup() function to find the ADempiere key based on the key values in the spreadsheet with the raw data.
{% endhint %}

### **Mandatory and Optional Fields**

For advice on which fields are mandatory or optional, see the help for the individual Import windows.  Mandatory fields have to be included in the imported data. &#x20;

{% hint style="info" %}
If the mandatory fields have the same value in all the data rows, its a good idea to add these to your spreadsheet and not use a Constant Value in the Import Loader Format.  Then all the data for your import is coming from one place, your data file.
{% endhint %}

## Defining the Import Loader Format

As mentioned above, the Import Loader will accept comma separated (CSV), a custom separator character, fixed position or tab separated data.

### **Fixed Position**

Fixed position data is treated differently than the other three and the meaning of the ***Start No*** changes from the column of data to the character count in the data. Also, when Fixed position data is used, each field requires an ***End No***. To test the fixed position data import, create a text file (txt) with the following lines:

```
0000000001111111111222222222233333333334444444444555555555566666666667
1234567890123456789012345678901234567890123456789012345678901234567890
007BOND, James         My name is Bond, James Bond.  MI5  Molly Penny 
   Jolly Green Giant   Look up. Way up!              CBC  Rusty        
```

and save the file in \<ADEMPIERE\_HOME>\data\import. (This is for convenience. You can save it anywhere.) The first two lines are there only to help with the column numbering.

Next, create an Import File Format with the following fields:

* Import Format Tab
  * ***Name***: Test
  * ***Table***: I\_BPartner
  * ***Format***: Fixed Position
* Format Field Tab
  * ***Seq***: 10, ***Name***: Name, ***Column***: Name\_Name, ***Data Type***: String, ***Start No***: 4, ***End No***: 23
  * ***Seq***: 20, ***Name***: Assistant, *Column*: Name2\_Name2, ***Data Type***: String, ***Start No***: 59, ***End No***: 70

Then open the **System Admin -> Data -> Data Import** menu **Import File Loader** form. Click on the button ***Select file to load*** and find the text file you created above.

Next, click on the button labeled ***Import Format*** and select the Import File Format "Test" you created above.

Using the **<** and **>** buttons, move to the third line. You should see the ***name*** and ***name2*** fields filled as shown below:

![Import File Loader example for a "fixed" import format](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-M0rKwyLw_Zu5IdaGELU%2F-M0rT-YEmumf69xS_htd%2Fswing_ImportFileLoader_FixedExample.jpg?alt=media\&token=7c9e86ea-2b85-4df2-9214-9d3d63251d31)

### **Delimited Data**

Delimited data using CSV, tab or other customer separator character is interpreted in columns of data.&#x20;

{% hint style="info" %}
The ***Start No*** is the column number with the left most column being 1.  Any column with ***Start No*** = 0 will be ignored.
{% endhint %}

Each data line is read sequentially to find the delimiters. &#x20;

If fields include the delimiter character, ensure they are surrounded by double quotes (").   Double quotes can be included in the data by using them twice (""). For example: a CSV line of "Artikel,bez","Artikel,""nr""",DEM,EUR results in four data fields:

* Artikel,bez
* Artikel,"nr"
* DEM
* EUR

#### **Comments**

Any field data enclosed in square brackets '\[' or ']' will be interpreted as a comment and ignored. The data for that field will be set to a null string. Only the first and last characters are tested.

#### **Dates**

Date data is read as a string and converted to a timestamp without milliseconds (YYYY-MM-DD HH24:MI:SS). The Data Format field is used to set the format of the date data using the Java class SimpleDateFormat. See the link for the wide variety of format patterns available.

{% hint style="info" %}
One confusing bit with the date formats has to do with months and minutes, one is 'M' and the other 'm'. A data format like 'dd/mm/yy' will give incorrect results.
{% endhint %}

If the Data Format field is null, the date/time format will be set to the system default format pattern.

If the date data is null or blank string, the current system time will be used.

#### **Numbers**

Numbers are read as strings and converted to numbers as follows:

* The decimal point is kept, but any thousand separators are removed. The system assumes that if the decimal character is a '.', the separator will be a ',' as in 1,234,568.99 and vice versa. If the decimal character is a ',', it is changed to '.'.
* All characters except '.' and '-' are removed from the string and the string converted to a Big Decimal. If the remaining string has no characters left, the number is set to zero (0).
* If Divide by 100 is selected in the **Import Format Tab**, the number is divided by 100.

This means that it is possible to correctly interpret numbers in string format 'zz-a1,b2,c3,@@@45,,,asog6.7\@8@9\@0@@@' as -123456.789.&#x20;

Incorrect placement of or multiple minus signs '-' and decimal characters will cause errors.

#### **Strings**

Strings are read directly with the exception of the following character sequences which are changed to work with SQL.

* \\' is changed to ''
* \\\ is changed to \\\\\\\\

#### **Constants**

In the **Import Format Tab**, fields can be defined as constants and a ***Constant Value*** supplied. These constants are used for all records in the import. The constant does not have to be included in the data file: it is added to the Import table in each record created.

The Constant Value is parsed in the same way as strings (above) except if the Constant Value is all digits and decimal points '.' in which case it is treated as a number.

{% hint style="info" %}
If you have a constant, which has a number value, but the corresponding field is a string (i.E. BPartner\_Value), you may get an exception, because the generated sql does not have the valid syntax. For example

&#x20;`WHERE ... BPartner_Value=123`&#x20;

instead of&#x20;

`WHERE ... BPartner_Value='123'`.&#x20;

The work-around is to define the constant value as 123\<Space>. This is treated as a string and the trailing space is trimmed.
{% endhint %}

{% hint style="info" %}
To keep all your import data in one place, its better to add the "constant" fields to your spreadsheet data and import it directly.  With constants, some of the data is in your file, and some in the Import File Loader format.
{% endhint %}

#### **Scripts, Callouts and Advanced Processing**

In some cases, the import data can be processed by scripts and rules to prepare it for processing. This is an advanced topic.

## Import File Loader

Once the data has been prepared and an Import File Format defined, the import of the data is performed by the **Import File Loader** Form.

Open the **System Admin -> Data -> Data Import** menu **Import File Loader** form and click on the button ***\<Select file to load>***. Find and select the data file you have prepared. If necessary, select the character encoding used in the file.

Next, click on the button labeled ***Import Format*** and select the Import File Format you created above.

{% hint style="info" %}
With many data files to import and just as many Import File Formats, it is helpful to use a naming convention for both so that you can easily find the correct Import File Format to use with a given data file.
{% endhint %}

Once the Import File Format is loaded, the columns should appear in the lower part of the form. If you click on the '<' and '>' buttons, you can cycle through the records and verify that the data is being read properly.

If the data appears to be read properly, then you can click the green check mark and import the data into the temporary table. This can take a while with large imports, so please be patient.

A dialog will appear showing the number of records read and imported. These should be the same. If not, there were problems that you will have to investigate. Check the console log for messages and verify that the data type of the columns matches the data type of the target fields.  Another cause is duplicated data or data that violates multiple key constraints.  When importing products, for example, the UPC codes need to be unique.  If any are duplicated, the row is discarded.&#x20;

With the import completed, you can now open the target Import table and review the data.

## Import\<Table> process

If you are happy with what you see, click the **Import \<Table>** button at the bottom of the window or select it from the **Process** icon in the toolbar. This starts the Import\<Table> process.

A dialog will appear where you can set some default parameters and, depending on the Import Table, whether the import will be just processed or processed and imported. Import Tables that import documents also allow the document status to be set. Set the parameters accordingly and click the green check mark.

{% hint style="info" %}
When importing thousands of invoices, be sure to set the status to completed if that is what you want. Manually completing thousands of documents is an unnecessary chore.
{% endhint %}

The import process will display a dialog with the status of the import showing number of records imported and the number with errors.

If errors occurred, check the Import Error Message in the Import table.

If the import was a partial success, you can correct the errors and try again.

If you correct the errors in the data file and try to import the same data file again, you may get duplicate entries or errors due to key constraint conflicts.

If there were no errors, sigh with relief and celebrate by telling co-workers of your victory.

## Deleting Imported Data

You can easily empty an Import table with the process in the menu tree **System Admin -> Data -> Data Import -> Delete Import**. This process will wipe the contents of the Import table so you can re-import the same data or try another batch of data.

{% hint style="danger" %}
Once you have processed the import and data has been moved to the main tables, if you have to delete it, you will be in a world of hurt. In a production system, you may need to recover from a backup or make the corrections at the database level - best be careful.
{% endhint %}

## Data Import Tips

* Test your import formats with a small data set before importing your 300,000 records. To understand what data is required to complete the import without errors, it helps to work with a small representative data set, perhaps ten rows or so, that you can test with.
* If you are going to import data into a production system, it is good idea to work with a sandbox to ensure you get the format and data requirements correct. It is a very annoying and tedious task correcting import errors in a production system.
* Remember to delete imported records from your table before re-importing them
* Be wise in the choice of document types. Documents with indirect types will create additional documents in the system. For example, importing customer orders will create indirect invoices and shipment documents. Non-indirect invoices will require you to create shipment documents. Avoid the extra work if you can.
* You can manipulate data in your Import Table after importing it - so you can load information into the 'wrong' fields and then move it into the correct place (using SQL) before finalizing the import. (In some cases, this may be easier than writing a custom import loader in software.)
* If using a spreadsheet to analyze your data before importing it:
  * use a function like clean() to clean your text of any unprintable characters
  * double check any functions that have references to ensure the references line up properly. Be wary of deleting a line in raw data as the processed data may be out of sync.
  * be careful with fields that can have leading zeros like Postal Codes, SSNs. Being very helpful, the spreadsheet software may convert these to numbers, dropping the leading zero.

### Adaxa tips

Other tips from Adaxa (based on Steven Sacket's 8+ years of experience) ...

1. Always use the format with user-selected delimiter and then you nominate the delimit char ... this protects from a bug which keeps reappearing
2. When you create the import loader format make sure that the name you give to the column shows what you expect eg name the column OrgCode or OrgID (not Org!) and "DateAcct-yyyyMMdd" "CurrencyCode-AUD" "Rate 1.0" etc. If the name does not show you the data to expect you are lost. Always use the java yyyyMMdd format so excel does not screw the dates up. Become familiar with excel command =Text(\[field with date],"yyyymmdd") Note that excel needs small "m" and java needs caps "M".
3. Always nominate your own Code/Search Key/Value and import it, do not let the system create. Then, when you need to add an extra Contact or Location (etc) the spreadsheet will already know which BP or Product its supposed to be updating.
4. Avoid using the "constant" capability in the print format. Its easy to just populate the column in your data with a constant and then all the data being considered by the importer is coming from one place - your file!
5. Create a report of the print format lines with "Start No" as column 1 and "name" as column 2 ... and order by start no. Open the report in Excel/Libreoffice. Select the column info and say >copy >paste special/ transpose and repaste the cells. This gives you column headers/names in \_exactly\_ the right order and no stuff-ups possible.
6. Ensure the import table is empty.  Run the **Delete Import** process at the end of the import menu to delete any rows in the table you are trying to import into!!!
7. Leave the headers there and add your data underneath looking at the names to make sure the data format is consistent. When you are done (optionally) delete the rows containing the inherited header info.
8. Save another copy of the file with only 1 to 5 rows of data as a csv (or whatever). Open the import loader and load the file and select the import loader that suits. Scroll through the rows using the right and left buttons at the top right of the screen. Note particularly the first row that still contains the labels inherited from the print format you exported. check that they align properly. Delete the header labels row you imported from the import staging table.
9. Now click the green tick to load the rows into the import staging table (I\_Product etc) Check that the import table is loading properly with your few test rows. fix the errors in your data and run the process again. Remember to delete the header labels row you imported from the import staging table.
10. When you get data into the import staging table, click the import button. hit refresh so that you can see any error messages that have been generated. fix the errors in the data displayed in the window by hand modifying the data or adding extra data until the record will import correctly. Reflect any required changes in your import data set.
11. When it all works, import the rest of the records.

## Trouble Shooting

### **ERROR: operator does not exist: character varying = integer**

If you get an exception like the following:

```
org.postgresql.util.PSQLException: ERROR: operator does not exist: character varying = integer
 Hinweis: No operator matches the given name and argument type(s). You might need to add explicit type casts.
...
```

It is likely that you used a numerical Constant. These need to be treated specially.  See [Constants](#constants)

### **Import File Loader discards input records**

Import File Loader ends successfully with but the number of records in the data and the number imported are different.

Check the uniqueness rules.  There is uniqueness defined in the Import File Loader process for the Product table. The columns UPC and Value must be unique in the data file. Also the concatenated BPartner\_Value+VendorProductNo must be unique. These are not a database constraints - just software rules. No message is displayed if the rules are violated, but the records are discarded.


# Partner Relations


# Revenue Recognition

How to setup the process of automated revenue recognition.

At the time of writing, automated revenue recognition process had not been implemented.

Revenue recognition could be achieved manually by setting the product's Product Revenue account to a deferred revenue account and recognizing the revenue via a general journal entry.

The Revenue Recognition window could be used to define the rules related to the recognition and link these to a product for information purposes.


# Open Items

Describes the management of payments, allocation of payments to invoices and payment reconciliation with bank statements.


# Dunning

Dunning is the process of informing customers about the state of their account and collecting money from customers that they owe to the organization.

Dunning is the process of informing customers about the state of their account and collecting money that they owe to the organization. As a process, it generally starts with polite requests, perhaps verbally or a sent statement of account, followed by e-mails and letters that might escalate to legal threats before the account is written off and passed to a collections agent.

An example of a company policy on Dunning might be as follows:

1. For invoices over their due date by less than 15 days, a polite phone call to inquire and request payment. No action taken on the Customers's Account.
2. For returned checks - enter a negative payment and a new invoice charging a returned check fee. Find the original payment and reset the payment allocation. Allocate/cancel the original payment and the returned check. This will leave the invoice unpaid. Call the customer and politely request payment. No action taken on the Customers's Account.
3. For invoices over 30 days, a letter requesting immediate payment. No action taken on the Customers's Account.
4. For invoices over 60 days, a letter threatening that the amounts will be passed to a collections agent.  The Customers credit is stopped and the payment term applied to new invoices is changed to Immediate.
5. For invoices over 90 days, write off the amount owing and pass the invoice to a collections agent. This is a manual process.

ADempiere includes tools to help with the Dunning process making it easy to manage collections for a large number of customers by keeping track of where each customer and invoices sits in the process. The intent is that the Dunning process be "run" on a periodic basis and at each run, invoices move through the process until they are paid or written off. There are two key periodic tasks:

1. Generating lists of invoices and payments relevant to the Dunning policy, referred to as a "Dunning Run"; and
2. Printing or emailing Dunning letters to the delinquent customers, a process called "Print Dunning Letters."

The Dunning process can be customized for a particular Business Partner or Business Partner Group and each process can have multiple levels or steps that collectively define the Dunning policy of the company. Each level can take a number of actions such as printing letters, sending emails, stopping credit or resetting the payment terms for the Customer. Customer Invoices are flagged as being in the Dunning process and associated with a particular Dunning Level.

The relationship with individual customers can be further managed by setting a ***Dunning Grace*** ***Date*** in the **Business Partner** window, **Customer** tab, which affects all invoices, or in the **Invoice (Customer)** window, **Invoice** tab, for a particular invoice. The Customer or Invoice affected will not be included in Dunning processes until after the Dunning Grace Date.

## Dunning Setup

To start using Dunning, the dunning policies must be defined and setup according to your needs. Once the setup is complete, Dunning becomes a periodic and repeatable activity of creating **Dunning Runs** and **Printing Dunning Letters**.

### The Dunning Policy

A Dunning policy definition starts with a Dunning record and one or more Levels. Open the **Dunning** window in the **Partner Relations** **> Business Partner Rules** menu. The **Dunning** window is relatively simple. You will need to create a new record for each distinct dunning policy or collection of levels you require. The key fields are as follows:

| Field                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ***Name***                       | Any useful name.  The ***Name*** is used to identify the Dunning process to apply to Business Partners and Business Partner Groups.                                                                                                                                                                                                                                                                                                                                        |
| ***Default***                    | Indicates the Dunning record is the default Dunning process.  It is not currently used.                                                                                                                                                                                                                                                                                                                                                                                    |
| ***Create levels sequentially*** | Select if the actions defined by the Dunning Levels need to be performed in order.  For example, if you have several reminders based on the number of days an invoice is due, it might not be a good idea to send all of them at the same time to the same customer.  On the other hand, if the Levels can be performed in parallel, then you can deselect this field. Examples of parallel actions might be sending a statement and stopping credit for overdue accounts. |

### Dunning Levels

The Dunning Level defines the actions that should be taken based on some triggers. To understand how to setup the levels it helps to know how they are used.

The gathering of information on which Business Partner needs to be Dunned is called a "run". When the Dunning process is run, it is run for a particular level or all levels and for a particular date. The date when the Dunning process is run determines the age of the invoices and the number of days after the payment due date for each unpaid invoice. For each level, all the invoices that meet the constraints of the Level are identified. If payments are to be included, these are also identified. Fees, if any are added. All this information is gathered in a Dunning Entry for each Business Partner but nothing is done with the information at this point. You can review the Dunning Entries and the Entry Details (the identified invoices etc..) and verify that all is in order or you can re-run the Dunning process and recreate the Dunning Entry information. If a new run is performed before the previous was processed, the Entries and Entry Details will be duplicated.

Actions are taken when the Dunning Entry is processed. This could include the sending of e-mails or printing of letters and other actions as mentioned below. Once processed, no further changes are allowed and the invoices identified will be in the dunning process. Once processed, if a new run is performed, the Entries and Entry Details will be different depending on the constraints set in the Level.

The Level defines the constraints using the following fields:

| Field                      | Description                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ***Show All Due***         | If true, the dunning letter with this level includes all due invoices, including invoices that are not due yet. If false, it will only show invoices where the ***Days after due date*** is less than the days due of the invoice or within the range of ***Days From*** and ***Days To*** if ***Range*** is selected.                                                                     |
| ***Show Not Due***         | If true, invoices that are not due yet (based on the Dunning Run date) will be included.  If false, only invoices with a positive number of days due will be included (>=0).  The field is ignored if ***Range*** is selected.                                                                                                                                                             |
| ***Range***                | If selected, only invoices with days due that fall between ***Days From*** and ***Days To*** are considered.  ***Range*** is only displayed if ***Show All Due***  is deselected.  \_\_                                                                                                                                                                                                    |
| ***Days after due date***  | Indicates the number of days after the payment due date to initiate dunning. If the number is negative, it will include invoices due in the future (not due). ***Days after due date***  is only displayed if ***Range*** and ***Show All Due*** are deselected.                                                                                                                           |
| ***Days between dunning*** | The Days Between Dunning indicates the minimum number of days between sending dunning notices.  Invoices that were dunned more recently than this will be ignored.  ***Days between dunning*** is only tested if ***Range*** and ***Show Not Due*** are deselected. See the note below. ***Days between dunning*** is only displayed if ***Range*** and ***Show All Due*** are deselected. |
| ***Days From***            | The inclusive lower limit of the invoice days due to consider.  Invoices with days due less than ***Days From*** will be ignored.  Only relevant if ***Range*** is selected.                                                                                                                                                                                                               |
| ***Days To***              | The inclusive upper limit of the invoice days due to consider.  Invoices with days due more that ***Days To*** will be ignored.  Only relevant if ***Range*** is selected.                                                                                                                                                                                                                 |
| ***Include Payments***     | If selected, unallocated payments for the Business Partner will be included.  If ***Is Statement*** is selected, all payments will be included.  Otherwise, payments will only be included if there is at least one invoice - this prevents dunning for money you owe to the customer.                                                                                                     |
| ***Charge fee***           | Indicates if the dunning letter will include fees for overdue invoices.  Note that the fee amount is not automatically added to the customer's account.                                                                                                                                                                                                                                    |
| ***Fee Amount***           | The ***Fee Amount*** indicates the charge amount on a dunning letter for overdue invoices. This field will only be display if the ***Charge Fee*** checkbox has been selected. Note that the fee amount is not automatically added to the customer's account.                                                                                                                              |
| ***Print Text***           | A label to be printed on documents or correspondence.                                                                                                                                                                                                                                                                                                                                      |
| ***Note***                 | Optional additional information about this record.                                                                                                                                                                                                                                                                                                                                         |
| ***Dunning Print Format*** | The **Dunning Print** process will generate a PDF of the list of entries associated with this Level and either print it or send it as an attachment to an e-mail.  If you do not specify a ***Dunning Print Format***, the PDF will not be generated and the Dunning Run will not be processed.                                                                                            |
| ***Credit Stop***          | Select if the Customer's ***Credit Status*** should be set to *Credit Stop* for any invoices found at this level.  This may help prevent further losses.                                                                                                                                                                                                                                   |
| ***Set Payment Term***     | Select if the Customer's ***Payment Term*** should be changed, for example from *Net 30* to *Immediate,* if any invoices are found at this level.                                                                                                                                                                                                                                          |
| ***Payment Term***         | The Payment Term to set if ***Set Payment Term*** is selected.  ***Payment Term*** only appears if ***Set Payment Term*** is selected.                                                                                                                                                                                                                                                     |
| ***Collection Status***    | The Collection Status to set on the affected invoices.  If left blank and ***Is Statement*** is not selected, the invoice ***Collection Status*** will be set to *Dunning*.                                                                                                                                                                                                                |
| ***Is Statement***         | Select if the dunning level is intended as a statement of accounts for the Customer.  If selected and ***Collection Status*** is blank, then the ***Collection Status*** of any affected invoices will not be changed.                                                                                                                                                                     |

{% hint style="info" %}
For the first Dunning Level, its important to set the ***Days between dunning*** to zero since invoices that have not yet been dunned have zero days since the last dunning. If you set ***Days between dunning*** > 0 on all Levels, no new invoices will ever be found.

This only applies if you deselect the ***Show all due*** and ***Show not due*** flags.
{% endhint %}

### Assigning a Dunning Policy to Business Partners

Each Business Partner needs to be associated with a Dunning policy or they will not be included in the Dunning process. The Dunning policy can be set for a Business Partner Group or individual Business Partners. The individual setting takes precedence.

To set the Dunning policy for a whole group, open the **Business Partner Group** window in the **Partner Relations** **>** **Business Partner Rules** menu. Select the desired Dunning entry in the ***Dunning*** field.

To override the Group Dunning policy, set the ***Dunning*** field in the **Customer** tab of the **Business Partner** window for a particular Business Partner.

## Dunning Runs

A **Dunning Run** is a record of the dunning process. The **Dunning Run** record identifies the ***Dunning Date*** and ***Dunning*** policy and ***Dunning Level*** that was used. Each affected Business Partner becomes an **Entry** in the **Dunning Run** and each invoice, payment and fee becomes a **Line** of the **Entry.**

The **Dunning Run** window can be found in the **Open Items** menu.

There are two ways to create Dunning Runs:

1. Manually, by creating a record in the **Dunning Run** window with a ***Dunning Date***, ***Dunning*** policy, and optionally a ***Dunning Level***; or
2. Via a process, **Create Dunning Run**, which will also create the **Entry** and **Line** information.&#x20;

The **Create Dunning Run** process is found in the **Open Items** menu as is the **Dunning Run** window. The **Dunning Run** window/tab also includes a button that executes the **Create Dunning Run** process.

### Creating Dunning Runs Manually

Open the **Dunning Run** window and create a new record. Set the fields accordingly. The key fields are as follows:

| Field               | Description                                                                                                                                                                                                         |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ***Dunning Date***  | Mandatory. Specifies the date of the Dunning Run.  The ***Dunning Date*** determines the number of days payments are past their due date for invoices.  The ***Dunning Date*** defaults to the current system date. |
| ***Dunning***       | Mandatory. The Dunning policy used to create the **Entry** and **Line** records.                                                                                                                                    |
| ***Dunning Level*** | The Dunning Level used to create the Entry and Line records.  If blank, all Levels of the Dunning policy will be used.                                                                                              |

In addition to these three key fields, there is a Button ***Create Dunning Run*** *\*\*\_and a flag* **Processed***. The button process and parameters are described below. When run from the **Dunning Run** window, the* **Create Dunning Run**\_ process will generate the Entry and Line records for the Dunning Run.

The ***Processed*** flag is read-only and will be set once the **Dunning Run** is sent/printed.

{% hint style="warning" %}
There is a button ***Send*** in the **Dunning Run** window that appears when the ***Processed*** flag is set. It is not used. See issue [#2363](https://github.com/adempiere/adempiere/issues/2363).
{% endhint %}

### Creating Dunning Runs via the Process

Dunning Runs can also be created using the **Create Dunning Run** process found in the **Open Items** menu. The benefit to using the **Create Dunning Run** process from the menu is that it will create a number of **Dunning Run** records at once along with their associated **Entry** and **Line** information.

{% hint style="warning" %}
If you run the **Create Dunning Run** process from the menu, it may duplicate an existing **\*\*unprocessed** Dunning Run\*\* rather than recreate the Entry and Line records.
{% endhint %}

Whether run from the menu or from a **Dunning Run** record, the process is similar. The **Create Dunning Run** process has a number of parameters that control how the **Dunning Run**, **Entry** and **Line** records are created:

| Parameter                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ***Organization***           | Sets the Organization to use in the Dunning Run.  If not *All (\*),* the invoices and payments added to the Entry Lines will be limited to those belonging to the specified Organization.                                                                                                                                                                                                                                                      |
| ***Include Disputed***       | If selected, the Lines will include invoices that are marked as ***In Dispute***.                                                                                                                                                                                                                                                                                                                                                              |
| ***Only Sales Invoices***    | If selected, only Sales (Customer) Invoices will be included.  Otherwise, both Sales and Purchase (Vendor) invoices will be included.  This is useful where a Business Partner is both a Customer and Vendor and contra allocations are possible.                                                                                                                                                                                              |
| ***Default Sales Rep***      | The Sales Rep added to the Entry when it is created.  The ***Default Sales Rep*** is not used to filter the invoices or payments.                                                                                                                                                                                                                                                                                                              |
| ***Dunning Currency***       | If ***Include All Currencies*** is not selected, only invoices in the selected  currency are included in the Lines.                                                                                                                                                                                                                                                                                                                            |
| ***Include All Currencies*** | Select to include items in all currencies in the Dunning Run.                                                                                                                                                                                                                                                                                                                                                                                  |
| ***Business Partner***       | If not blank, only generate Entries and Lines for the specified Business Partner.                                                                                                                                                                                                                                                                                                                                                              |
| ***Business Partner Group*** | If not blank, only generate Entries and Lines for Business Partners in the specified Business Partner Group. Ignored if ***Business Partner***  is not blank.                                                                                                                                                                                                                                                                                  |
| ***Dunning Date***           | Specifies the date of the Dunning Run.  The ***Dunning Date*** determines the number of days payments are past their due date for invoices.  The ***Dunning Date*** defaults to the current system date.                                                                                                                                                                                                                                       |
| ***Dunning***                | If selected, only that Dunning policy will be used to create a Dunning Run.  If blank, Dunning Runs will be created for all active Dunning policies for the Client.  This is only relevant if the **Create Dunning Run** process is performed from the Menu and not from the **Dunning Run** window.  In the **Dunning Run** window, if the parameter is not blank it will replace the ***Dunning*** policy set in the **Dunning Run** record. |
| ***Dunning Level***          | If a ***Dunning*** policy is specified, the Dunning Run Entry and Line information can be limited to a single Dunning Level. If not specified, Entries will be created for each Dunning Level in the Dunning policy. In the **Dunning Run** window, if the parameter is not blank it will replace the ***Dunning Level*** set in the **Dunning Run** record.                                                                                   |

### Dunning Run Entries and Lines

Once the Dunning Run Entries and Lines have been created by the **Create Dunning Run** process, they can be reviewed and adjusted if required. No changes to the status of the invoices or customers has occurred and won't until the Dunning Run is printed. Until then, Run Entries and Lines can be deleted or made inactive (by deselecting the ***Active*** field). The entire Run can also be deleted. It may be apparent, for example, that payments can be allocated to unpaid invoices and that this should be done before the Customer is sent a dunning note. If necessary, the Create Dunning Run process can be repeated and the Dunning Run entries will be recreated.

To review the Dunning Run, open the **Dunning Run** window in the **Open Items** menu. The **Dunning Run** tab is pretty straight forward. Processed runs will be read only. Click the ***Create Dunning Run*** button to recreate the entries if required.

{% hint style="info" %}
The **Create Dunning Run** process will overwrite the ***Dunning Date***, ***Dunning*** policy and ***Dunning Level*** fields.
{% endhint %}

#### Dunning Run Entry

The **Entry** tab shows records for each Business Partner and Dunning Level. If a Level was not specified on the **Dunning Run** tab, there may be multiple **Entry** records for each Business Partner, one for each Level that applies. The following describes the key fields:

| Field                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ***Dunning Level***        | Read only.  Shows the Dunning Level that applies to this Entry.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ***Business Partner***     | Mandatory.  The Business Partner that is responsible for the Line items. Note that this should be a read-only field. Be careful not to change it.                                                                                                                                                                                                                                                                                                                                                                |
| ***Partner Location***     | Mandatory. This will default to the Business Partner Location that is flagged as "Remit To" or "Pay From".  If these aren't found, the first "Bill To" location will be used and if this also isn't found, the first active location will be used.  If there are no active locations, the Create Dunning Run process will throw an exception.                                                                                                                                                                    |
| ***User/Contact***         | Select the User or Contact who will receive the Dunning letter or email.  The **User/Contact** will default to the first User associated with the ***Partner Location*** selected or the only User if there is just one User/Contact for the ***Business Partner***. If there are multiple Users but none associated with the Partner Location, the field will be left blank. The ***User/Contact*** is required and the User record requires a valid email address if the Dunning letter will be sent by email. |
| ***Currency***             | Mandatory. The currency to use on the dunning letter.  Defaults to the Currency used in the Create Dunning Run process. Invoice amounts will be converted to this currency using the default exchange rate in effect when the record is first saved.                                                                                                                                                                                                                                                             |
| ***Sales Representative*** | Mandatory. Defaults to the Sales Representative set in the Create Dunning Run process. The Sales Representative info can be used as contact info in letters and will be the "From" addressee on emails.                                                                                                                                                                                                                                                                                                          |
| ***Note***                 | The ***Note*** text can be used on the dunning letter to the Customer.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ***Amount***               | Read only. The converted total amount of all the invoices, payments, fees and interest in the **Lines**.  A negative amount may indicate that the company owes the customer money.                                                                                                                                                                                                                                                                                                                               |
| ***Quantity***             | Read only.  A count of all the invoices and payments in the Lines.  The count does not include lines for fees or interest.                                                                                                                                                                                                                                                                                                                                                                                       |

#### Dunning Run Line

The Line *\*\**&#x74;ab list the invoices, payments, fees and interest being dunned. The fields are self explanatory.

{% hint style="warning" %}
The ***Times Dunned*** field is a count of the number of times the item appears on Dunning Run Lines, including unprocessed ones. See issue [#2365](https://github.com/adempiere/adempiere/issues/2365).
{% endhint %}

#### Previewing the Dunning Letter

It is possible to preview or print a Dunning Letter from the **Entry** tab of the **Dunning Run** window. Simply select an Entry record and click the Print or Print Preview icon in the toolbar. A Dunning Letter for that entry, using the assigned print format will be shown/printed. An example is linked below.

{% hint style="info" %}
Printing or previewing the Dunning Letter this way does not "process" the Entry. It only allows you to see the document that was or will be sent to the customer. To "process" the Entry, you have to run the **Print Dunning Letters** process discussed below.
{% endhint %}

{% file src="<https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZGj-BMl5jA-adpuRYY%2F-LZ5G4Myc_jDQGHqI5OO%2Fdunningentryexample.pdf?generation=1550780743646552&alt=media>" %}
Example Dunning Letter
{% endfile %}

## Print Dunning Letters

The process **Print Dunning Letters** in the **Open Items** menu will print the Dunning Run information and/or send the information as a PDF attachment to the customers. Running the process will mark the Dunning Run as "Processed", making it read-only. The process will also update the ***Collection Status*** and ***Dunning Level*** of the Invoice, and, if so configured in the Dunning policy, set the Customer's Business Partner ***Credit Status*** to *Credit Stop* and replace the Customer's default ***Payment Term**.*

There are a few parameters you can set to control how the process runs. The process can be run multiple times to reprint the information or change the parameters.

| Parameter                            | Description                                                                                                                         |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| ***EMail PDF***                      | If selected, the a PDF report listing the Dunning Run Entry Lines will be emailed to the Customer.                                  |
| ***Mail Template***                  | The email template to use.  Mandatory if ***EMail PDF*** is selected.                                                               |
| ***Dunning Run***                    | The Dunning Run to print.  Only unprocessed Runs can be chosen.  If left blank, ALL Dunning Runs will be (re)printed.               |
| ***Only if BP has Balance***         | If selected, emails or printed reports will only be generated if the Entry ***Amount*** shows a positive balance greater than zero. |
| ***Print Unprocessed Entries Only*** | If selected, only unprocessed Entry records will be printed.  If not selected, processed Entry records will be reprinted as well.   |

{% hint style="warning" %}
If the ***Dunning Run*** parameter is left blank and ***Print Unprocessed Entries Only*** is deselected, ALL Dunning Runs will be (re)printed. If ***EMail PDF*** is also selected, all the Dunning Run Entries will be (re)sent to the Customers. \_*\*\**\_See issue [#2369](https://github.com/adempiere/adempiere/issues/2369).
{% endhint %}


# Products & Material Management

Creating and using products.

Products are one of the key elements of the ADempiere ERP system. A product is an idea: a definition of some thing or service that is bought, sold, produced or consumed in the course of running the enterprise. Tracking the costs and use of products is usually of great importance and the ADempiere system provides many methods of gathering and reporting on this information.

Product information is gathered on most documents that deal with purchasing and ordering, shipping and receiving, invoices and manufacturing production. Product information also appears in the Accounting Facts as one of the Accounting Dimensions allowing financial information to be queried based on the products that appear in the original documents.

Product prices are another important component of the product information and ADempiere provides a complete solution to managing the price lists that apply to various business partners.

Before the products can be setup in ADempiere, you should have a good understanding of how the product information is used to generate performance data so that you can generate the reports required to manage your operations. The first question is whether you require a product at all. Consider a bill for electricity. It would be unusual to verify that the quantity of electricity provides was actually received before the bill was paid. In such a simple case, the accounting for the electricity could be made using a **Charge** with no product definition involved and no process beyond the invoice and payment. However, if it was important to track the amount of electricity consumed and the cost of the electricity over time, creating a product for it would be helpful.

Beyond the choice of Charge or Product, there are a number of ways a product can be configured to track expenses and material costs. The rest of this section of the book describes how to configure the products.


# Product Setup

The workflow to follow to define products

## Product Setup

Product setup involves several steps:

1. Defining the [Warehouses and Locators](https://adempiere.gitbook.io/docs/introduction/products-and-material-management/product-setup/warehouse-and-locators) that will be used to store products;
2. Defining the [Units of Measure](https://adempiere.gitbook.io/docs/introduction/products-and-material-management/product-setup/units-of-measure) that the products will use;
3. Create [Asset Groups](https://adempiere.gitbook.io/docs/introduction/products-and-material-management/product-setup/asset-groups) to define the accounting for the asset products
4. Creating [Product Categories](https://adempiere.gitbook.io/docs/introduction/products-and-material-management/product-setup/product-categories) which will define the accounts to use to record the costs and revenue from the product. You can also create [Product Classifications, Classes and Groups](https://adempiere.gitbook.io/docs/introduction/products-and-material-management/product-setup/product-classifications-classes-and-groups) to assist in summarizing reports;
5. Create [Product Attributes, Sets and Instances](https://adempiere.gitbook.io/docs/introduction/products-and-material-management/product-setup/product-attributes-sets-and-instances)
6. Follow the [Tax Setup](https://adempiere.gitbook.io/docs/introduction/accounting-and-performance-analysis/tax-setup) process to define the [Tax Categories](https://adempiere.gitbook.io/docs/accounting-and-performance-analysis/tax-setup#tax-category) that will be applied when the product is purchase or sold;
7. Setting the [Revenue Recognition](https://adempiere.gitbook.io/docs/introduction/revenue-recognition) rules for the product; and finally
8. Defining the product itself.


# Warehouse & Locators

How to define the physical locations used to store inventory and the logistic processes used to replenish that inventory.

The model of logistics in ADempiere is based on a large company with a hierarchy of storage and replenishment warehouses where goods are received from suppliers at some of the warehouses and moved between warehouses to replenish those that do not receive goods directly.

Each warehouse has a physical location with an address.

Where the warehouses are located far from each other, there can be a significant period of time where the inventory is in transit from one location to another. In-transit warehouse locations can be defined that keep track of this inventory that has been shipped but not received. The products are recorded in the in-transit warehouse until the receipts have been confirmed.

Inside the warehouse, products are stored in locations called **Locators** defined by Aisle, Bin and Level, a sort of XYZ coordinate system. A single Locator can hold many different products.

Every warehouse needs at least one Locator and one of the Locators should be flagged as the "Default". This is the locator that will be the default used on documents where a locator is required. Typically, it would be the location of shipping/receiving in the warehouse.

For a very simple organization with small or no inventory, the minimum requirement is a single warehouse and single locator. Nothing else needs be configured.

For very complex companies, there is a full Warehouse Management System included with ADempiere that will support complex logistical processes. The Warehouse Management System provides ways to create areas and sections in the warehouse data to organize the locators more effectively and processes to manage the flow of material between warehouses.

## Setup and Definition

To setup the basic warehouses, go to **Material Management » Material Management Rules** and open the [**Warehouse & Locators Window**](http://wiki.adempiere.net/ManPageW_WarehouseLocators).

For more complex implementations, see **Warehouse Management** and **Distribution Management**.

## Replenishment Rules

Replenishment Rules help keep the necessary but minimum level of inventory in the warehouse to keep the costs low while also ensuring adequate availability of the products. The rules can be used with a regular process of replenishment planning to reduce the workload of procurement - the answer of the question "What do I need to buy today?".

Within each warehouse, replenishment rules can be established for each product. There are a number of replenishment types included:

* Maintain Maximum Level - Replenishment quantities will be ordered if the inventory level is below the maximum level.
* Reorder Below Minimum Level - Replenishment quantities will be ordered if the inventory level is below the minimum level.
* Replenish Plan Calculated - A Replenishment Plan is used to calculate when and how much material to order.
* Custom - It is possible to define a custom rule in software to calculate the replenishment quantities. The software class is defined in the **Warehouse** window.

## Replenishment Process

The replenishment rules are tested when the [**Replenish Report**](http://wiki.adempiere.net/ManPageR_ReplenishReport) \_\*\*\_is generated. The software that generates the report can also automatically generate the associated documents based on the replenishment rules assigned to the products in the warehouse including Distribution Orders, Inventory Moves, Purchase Orders, or Requisitions.

Where replenishment occurs from a source warehouse rather than procurement, the default source warehouse for the replenishment can be identified in the **Warehouse** window. This can be overridden for each product on the **Replenishment** tab.

## Warehouse Accounting

Each warehouse requires a set of accounts for

* Inventory Adjustment - This account is used to post Inventory value adjustments.&#x20;
* Warehouse Differences - The Warehouse Differences Account indicates the account used to record differences identified during inventory counts.
* Inventory Revaluation - The Inventory Revaluation Account identifies the account used to record changes in inventory value due to currency revaluation.

The value of inventory is recorded in the Product Asset account associated with each product.


# Units of Measure

How Units of Measure are defined

Unit of Measure (UOM) are how the quantities of products are defined. For Products, these are non monetary in nature and represent something that can be measured such as time, distance, volume, quantity, weight, etc.... Conversion from one UOM to another is possible, allowing the UOM to be specified on documents and have the quantities dealt with properly.

UOM types can include product specific types such as packaging (box, 6-pack, pallet). The conversion to other UOM such as "each" can be defined so the packaging can be broken down.

Each UOM is also used to set the precision of quantities and costs. The precision value is the number of decimal places the system will maintain when calculating the quantity or cost of the product.

One UOM should be marked as the default. Typically, this is the unit Each.

## Unit of Measure Conversion

The ADempiere system provides some automatic conversions between common units of measures (e.g. minute, hour, day, working day, etc.) but these are only used in resource scheduling operations. All other conversions have to be defined explicitly for each product.

Each product has a base or system UOM. All conversions are from this base UOM. Conversions need to be direct (i.e. if you have only a conversion between UOMs A-B and B-C, the system cannot convert A-C).

The conversion is defined by a multiply rate and divide rate used to convert the quantity from one of the units to the other. The Product UOM has to be the smallest UOM in the set of possible conversions. The divide rate must be > =1. For example, to convert Each to Pair, the multiply rate would be 0.5.

As an example, suppose there are two types of rope in inventory. The rope is stocked and sold in meters (m) but its is purchased by spool. For rope A, the spool contains 1000m of the rope. For rope B, the spool contains 400m. Each rope product would use Meter as its base unit and each would have a UOM conversion from Meter to Spool with different values.

![The Meter Unit of Measure](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZ5G1bjZ0BFZHjQciW2%2F-LZ5G3L68JQlTRhJmOqV%2Fimage%20\(8\).png?generation=1550588336942678\&alt=media)

![The Spool Unit of Measure](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LYoJ3xKkP5g22YWe_M3%2F-LKSuKcmYEEujXOHKw1P%2Fimage.png?generation=1550287136708456\&alt=media)

![Conversions from Meter to Spool for the two Rope products](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZ5G1bjZ0BFZHjQciW2%2F-LZ5G3L8rOsUngTXcPwT%2Fimage%20\(14\).png?generation=1550588338276928\&alt=media)

![Purchase Order Line for 3 Spools of Rope A](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZ5G1bjZ0BFZHjQciW2%2F-LZ5G3LAUMchhTNKxvBD%2Fimage%20\(11\).png?generation=1550588335900034\&alt=media)

![Purchase Order Line for 3 Spools of Rope B](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-LZ5G3LILf-EXjz9mW06%2Fimage%20\(19\).png?generation=1551809343479838\&alt=media)

![Product Info for the Rope products showing Ordered Quantities in meters](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZ5G1bjZ0BFZHjQciW2%2F-LZ5G3LE65eEIrPJUYRi%2Fimage%20\(12\).png?generation=1550588335569655\&alt=media)

![Material Receipt Lines showing receipt of spools. Not matched to order yet.](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZ5G1bjZ0BFZHjQciW2%2F-LZ5G3LGqzMqpJzsGZly%2Fimage%20\(4\).png?generation=1550588335944193\&alt=media)

![After the Material Receipt, On Hand quantity is shown in meters](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1qz6MMH7cxPsSRVD%2Fimage%20\(20\).png?generation=1551809344438190\&alt=media)

![After the Matching of PO with the Receipt, the On Order quantity is now zero. ](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LZ5G1bjZ0BFZHjQciW2%2F-LZ5G3LKac2LEcKhanSN%2Fimage%20\(3\).png?generation=1550588335410014\&alt=media)


# Asset Groups

How to define Asset Groups and link them to the Product Categories

ADempiere provides an Asset Management capability that allows users to manage capital assets using standard documents rather than GL Accounting. If you are not going to use the Asset Management module, you can skip this section. For more information, see the section on the [Assets & Asset Management](https://adempiere.gitbook.io/docs/introduction/assets-and-asset-management).

If you are going to use the Asset Management module, you will need to link Product Categories to the Asset Groups. The Product Category and Asset Group are linked on the Product Category page, so its easier if the Asset Groups exist before the Product Categories are created. The Product Category Accounts referred to here are described in more detail in the [Product Categories](https://adempiere.gitbook.io/docs/introduction/products-and-material-management/product-setup/product-categories) section.

The **Assets** [**Asset Groups Window**](http://wiki.adempiere.net/index.php?title=ManPageW_Asset_Groups\&action=edit\&redlink=1) is the first window to use when defining assets. Each Asset Group defines specific accounting elements to use so the groups should be set up according to the asset reporting structure in the corporate financial statements. For example, in the GardenWorld demo, the financial statements report on the assets using the following categories:

* 16 Land and Building
  * 16100 Land
  * 16200 Building
  * 16300 Land Improvements
  * 16400 Building Improvements
  * 16500 Leasehold Improvements
* 17 Furniture, Fixtures & Equipment
  * 17100 Furniture
  * 17200 Fixtures
  * 17300 Equipment
  * 17400 Vehicles
  * 17500 Data Processing Equipment
  * 17600 Software

The Asset Groups are set up in a similar way:

* Buildings
* Furniture
* Fixtures
* Equipment
* Vehicles
* Data Processing Equipment
* Software

Each group relates to a specific set of accounts that are used for the asset accounting for any asset that is part of that group. Again, in the Garden World demo, the accounts for the Buildings Asset Group are:

* Asset Acct HQ-16200-\_-\_-\_-\_
* Accumulated Depreciation Account HQ-18120-\_-\_-\_-\_
* Depreciation Account HQ-67120-\_-\_-\_-\_
* Disposal Revenue Acct HQ-79200-\_-\_-\_-\_
* Disposal Gain Acct HQ-80800-\_-\_-\_-\_
* Disposal Loss Acct HQ-82800-\_-\_-\_-\_

These accounts should be straight forward for most people familiar with a balance sheet with the exception of the Disposal Revenue Account. This account is debited with the proceeds of the disposal of the asset which would normally be a cash account. However, as the sale of the asset will likely involve invoicing and accounts receivable, the Disposal Revenue account should point at a clearing account that will be balanced by the invoice Product Revenue account. For this reason, the Asset Group Disposal Revenue account and Product Category Product Revenue account should be the same clearing account.

The Asset Group also defines the type of depreciation processing to use and the life of assets that are part of the Group. The Building Asset Group defines the depreciation function as [Straight Line](http://wiki.adempiere.net/Accounting_of_Assets#Straight_Line_Method) and the Usable Life as 10 years or 120 periods/months. This means that 10% of the depreciable value of the asset will be expensed as depreciation in each year.

There are a number of possible depreciation functions to choose from that match the most common depreciation schemes in use around the world.

The other key element that can be set in the Asset Group is the Accounting Schema. This allows the accounts and depreciation methods to change from one Schema to another where multiple schema are in use. For example, an accelerated depreciation scheme could be used in one Schema for tax purposes and a basic straight line scheme in another for regulatory reporting.

## Product Categories for Asset Products

After defining Asset Groups, the Asset Groups need to be matched to Product Categories. The next page provides details on setting up Product Categories for non-asset products. Here, the connection between Asset Groups and Product Category accounts are examined in detail.

When an asset is defined, it is defined using a Product and Asset Group. The Product Category used in the definition of the Product has to be linked to the Asset Group or it won't be possible to save the Asset record.

{% hint style="info" %}
Create a summary Product Category for all assets and use this as the Parent Product Category for the asset related Product Categories. Then in the Product Info window, you will be able to search for all asset related products using the summary category or for specific product assets using the detail categories.
{% endhint %}

The **Material Management>Material Management Rules** [**Product Category Window**](http://wiki.adempiere.net/ManPageW_ProductCategory) performs the same function as the Asset Group in that it defines the accounting for product transactions. The key items here are:

* The Parent Product Category - point to the summary category if following that approach.
* The Asset Group - select the matching asset group.

When setting the accounts on the Product Category Accounting tab, there are a few hints.

**It is recommended that the Product Revenue, Product Expense, Product Inventory Clearing, Cost of Goods Sold and Product Asset accounts be pointed at the same account which will function as a clearing account.**

The Product Asset account is used when the asset is first added to the books using the [Asset Addition](https://adempiere.gitbook.io/docs/assets-and-asset-management#adding-assets) process via a Vendor Invoice. This account will be credited the equivalent of the net book value of the asset. When the asset is received, the Product Asset account will be debited by the Material Receipt with the same value.

If moving from asset accounting using a GL, the product expense account could be pointed at a clearing account and a final GL entry could be made to remove the original assets and accumulated depreciation values to balance the clearing account after the asset has been added using the Asset Addition process.

Ignoring tax and other adjustments, the relevant postings that occur for the addition of an asset related product appear as follows. If the Asset Product is stocked, the Inventory Clearing account will be used. Otherwise, the Product Expense account. The Product Category accounts are in bold italics. The Asset Addition document is created and completed automatically by the Match Invoice document via the asset model validator.

| Document         | Debit Account                                     | Credit Account                                    |
| ---------------- | ------------------------------------------------- | ------------------------------------------------- |
| Vendor Invoice   | ***Product Expense*** or ***Inventory Clearing*** | Accounts Payable                                  |
| Material Receipt | ***Product Asset***                               | Not Invoiced Receipts                             |
| Match Invoice    | Not Invoiced Receipts                             | ***Product Expense*** or ***Inventory Clearing*** |
| Asset Addition   | Asset                                             | ***Product Asset***                               |

The end result of these four documents is a capital asset and an equivalent accounts payable.

The Product Revenue account will be credited on the sale of the asset, assuming an AR invoice is used to make the sale. The invoice line net amount will be considered as the proceeds of the sale. The documents and the relevant accounts affected are shown below.

| Document | Debit Account | Credit Account |
| -------- | ------------- | -------------- |

| Customer Invoice | Accounts Receivable | ***Product Revenue*** |
| ---------------- | ------------------- | --------------------- |

| Shipment | ***Cost of Goods Sold*** | ***Product Asset*** |
| -------- | ------------------------ | ------------------- |

| Asset Disposal | <p><em><strong>Product Revenue</strong></em>,<br>Accumulated Depreciation,</p><p>Disposal Loss or Disposal Revenue</p> | Asset |
| -------------- | ---------------------------------------------------------------------------------------------------------------------- | ----- |


# Product Categories

How to use the Product Categories

A Product Category provides a way to set values and behavior across all the products that belong to the Category. This is a great time saver when first setting up products and also provides a way to make changes to hundreds of products at a time.

The most important values are the accounting elements that the associated products should use. The Product Category header provides a few others:

* **Parent Product Category** - this can be useful when reporting by Product Category. The parent Category provides a way to summarize a number of other Categories.
* The **Material Policy** to use when selecting items from inventory.  The choices are First In, First Out (FiFo) or Last In, First Out (LiFo).  This choice can not be overwritten by the products assigned to this category.  If left empty, the Material Policy set in the Client window will be used.
* The **Asset Group** used to connect assets to products when buying and selling assets frequently. This connection makes it easier to manage the accounting of capital asset values. See [Assets and Asset Management](https://adempiere.gitbook.io/docs/assets-and-asset-management#asset-groups) for more information.

  **Planned Margin %** - this value is used in calculating the planned margin for products created by Projects. Specifically, where the project line hasn't identified a specific product but the product category is known.
* **Self-Service** - A flag to indicate if the product category should appear in the web store.
* The **Print Color** - Currently not implemented.  May be used to highlight the products assigned to the category by color in menu trees or reports.

## Product Category Accounting

This is an important tab as it provides the main mechanism to assign the same accounting setup to many products. When a new product is created, the accounts defined in the Product Category Accounting tab are copied to the product. In the Product Window, its possible to override these accounts. These accounts are part of the default accounting setup and will be set to defaults when the a new Accounting record is created. They accounts must be defined for the ADempiere software to function - even if they will not be used.

Changes made to the Product Category Accounting can be copied to all the assigned products using the "Copy Accounts" button at the bottom of the Accounting Tab.

{% hint style="info" %}
A set of accounts is needed for each Accounting Schema defined for the system. These will be set to the defaults for the system when the Product Category if first created.
{% endhint %}

{% hint style="info" %}
Note that For Product Categories connected to Asset Groups, refer to the [Asset Groups](https://adempiere.gitbook.io/docs/introduction/products-and-material-management/product-setup/asset-groups) page for hints on how to link the accounts.
{% endhint %}

The required accounts are:

| Account                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Product Asset           | The account used to record the cost of the product. For stocked products, this would typically be the balance sheet inventory account. For non-stocked products, this could be set to an appropriate expense account. The costs recorded are determined by the cost methods used.                                                                                                                                                 |
| Product COGS            | The Cost of Goods Sold (COGS) account to use to record the costs of the product shipped as an expense.                                                                                                                                                                                                                                                                                                                            |
| Product Revenue         | The account used to record the revenue from sales of the product.                                                                                                                                                                                                                                                                                                                                                                 |
| Product Expense         | The account used to record expenses associated with the product.                                                                                                                                                                                                                                                                                                                                                                  |
| Inventory Clearing      | The Account used for posting matched product (item) expenses (e.g. AP Invoice, Invoice Match). You would use a different account then Product Expense, if you want to differentiate service related costs from item related costs. The balance on the clearing account should be zero and accounts for the timing difference between invoice receipt and matching.                                                                |
| Cost Adjustment         | The account to record cost adjustments when, for example, landed costs are added                                                                                                                                                                                                                                                                                                                                                  |
| Invoice Price Variance  | An account used to record the difference between the invoice price and the product asset cost when matching AP invoices to material receipts. The material receipt document creates accounting facts in the Product Asset account and the Not Invoice Receipt account. The matching processes cancels the Not Invoice Receipt account amount with the Invoice amount and any difference is charged to the Invoice Price Variance. |
| Purchase Price Variance | The account used to record the difference between the Standard Cost and the Purchase Order Price. The Purchase Price Variance is only used in Standard Costing.                                                                                                                                                                                                                                                                   |
| Average Cost Variance   | Not currently used.                                                                                                                                                                                                                                                                                                                                                                                                               |
| Trade Discount Received | The account used to post the amount of trade discounts received on AP invoices/credit memos if the "Post Trade Discount" flag is selected in the Account Schema. If the invoice is based on an item with a list price, the discount received is the difference between the invoice line list price amount and the actual price amount.                                                                                            |
| Trade Discount Granted  | The account used to post the amount of trade discounts granted on sales invoices/credit memos if the "Post Trade Discount" flag is selected in the Account Schema. If the invoice is based on an item with a list price, the discount granted is the difference between the invoice line list price amount and the actual price amount.                                                                                           |
| Work in Process         | The account used to record work in progress costs during manufacturing. It is equivalent to the Product Asset account but records the costs issued to a manufacturing order or services purchased as part of the manufacturing process. When the manufacturing order is complete and the results issued, the value of the Work in Progress is transferred to the Product Asset account.                                           |
| Floor Stock             | <p>The account to use when issuing stock to a work order where the issue method of the Component of the Manufacturing Order is set to "Floor Stock". The issue is handled as<br>Debit Floor Stock Account</p><p>Credit Work in Process Account</p>                                                                                                                                                                                |
| Method Change Variance  | The account to use during a manufacturing process when there is a difference between the Standard BOM, Standard Manufacturing Workflow and the Manufacturing BOM Manufacturing Workflow. It is used in Standard Costing to record the difference in costs in the manufacturing process for this product.                                                                                                                          |
| Usage Variance          | The Usage Variance is used in Standard Costing. It reflects the difference between the Quantities on the Standard BOM or Time on the Standard Manufacturing Workflow and Quantities on the Manufacturing BOM or Time on the Manufacturing Workflow of the Manufacturing Order.                                                                                                                                                    |
| Rate Variance           | The Rate Variance is used in Standard Costing. It reflects the difference between the Standard Cost Rates and The Cost Rates of the Manufacturing Order.                                                                                                                                                                                                                                                                          |
| Mix Variance            | The Mix Variance is used when a co-product received in Inventory is different the the quantity expected                                                                                                                                                                                                                                                                                                                           |
| Labor                   | The account to use to record the labor costs of manufacturing this product.                                                                                                                                                                                                                                                                                                                                                       |
| Burden                  | The account to use to record the burden costs of manufacturing this product.                                                                                                                                                                                                                                                                                                                                                      |
| Cost of Production      | The account to use to record the costs of manufacturing other than labor.                                                                                                                                                                                                                                                                                                                                                         |
| Outside Processing      | The account to use to record the outside costs of manufacturing this product for outside/outsourced processing.                                                                                                                                                                                                                                                                                                                   |
| Overhead                | The account to use to record the overhead costs of manufacturing this product.                                                                                                                                                                                                                                                                                                                                                    |
| Scrap                   | The account used to record the scrap costs of manufacturing this product.                                                                                                                                                                                                                                                                                                                                                         |


# Product Classifications, Classes and Groups

Additional ways to classify products to ease reporting.

There are several windows that provide means to classify the products in trees of hierarchy to ease reporting:

* Product Classification
* Product Class
* Product Group

Each of these is similar, providing a name and a link to a parent. Like the Product Category, these could be used to report on product results. Their use is optional.

By creating entries in these windows, you can select the Group, Class and Classification in the Product window from a drop down list.

{% hint style="info" %}
The system administrator will have to create custom reports using parent Product Group, Class or Classifications. The default reports do not provide summaries by parent.
{% endhint %}

In addition, there are three text fields in the Product window that allow further identification for reporting:

* Group 1
* Group 2
* Classification

These fields are uncontrolled and could hold any text value.


# Product Attributes, Sets and Instances

How to setup and use Product Attributes to extend the product definition.

## The Product Attribute Model

**Attributes** enrich the information about products and provide additional ways in which the products can be defined and managed. The attributes can be thought of as specifications of the product. A collection of attributes is called an **attribute set** and the attribute set is applied to specific products as required. The attribute set can include information on the lot, serial number, and guarantee date of the product.

Product attributes allow the product name and value, fields to be kept short, since the information about the nature of the product can be defined in the attributes.

The attributes can also be used in product searches based on the attribute values. For example, find all resistors in stock that have a rating of 100 kOhms and a rectangular two-terminal surface mount package (0201). An electronic manufacturer could easily have tens of different products in inventory that match this search.

Attributes can be defined for a variety of products, be specific to a group of products or specific to a single item. An example of a specific attribute is a serial number. Only one item in the entire inventory of that product will have that serial number attribute. The value of the attribute is called and **Attribute Instance** and the collection of Attribute Instances is an **Attribute Set Instance**.

Attributes and their instances can be defined at the product level as in a specification or at the inventory level. At the product level, these are **Product Attributes** and at the inventory level **Instance Attributes**.

Product attributes are defined by the attribute set applied to the [**Product Window**](http://wiki.adempiere.net/ManPageW_Product). The Attribute Set Instance in the product window sets product level attributes that will be common across all attribute set instances created for that product.

Instance attributes are typically defined at the time that product or item enters or leaves the control of the company, such as at production, material move, inventory counts, material receipts, or material shipments. Instance attributes are associated with items in storage and are tracked on documents that affect these items.

There are three elements of instance attributes that can be assigned to any attribute set:

* a lot number or code
* a serial number
* a guarantee date

Beyond these three, any attribute can be defined as an instance attribute.

Once an Attribute Set Instance is created, it can be searched and tracked through documents via the [**Attribute Set Instance Window**](http://wiki.adempiere.net/ManPageW_AttributeSetInstance).

The Attributes Set Instances can also appear on shipments or material receipts as well.

## Setup

{% hint style="info" %}
For an example of the attributes in use, see [Example - Using Product Attributes.](https://adempiere.gitbook.io/docs/introduction/products-and-material-management/product-setup/product-attributes-sets-and-instances/example-using-product-attributes)
{% endhint %}

Before you establish your attributes and attribute sets, you need to define the information that you will need to track for each product and why it is needed. Some examples of how attributes can be required:

* Vendor serial numbers which need to be tracked and used if items are returned
* Vendor shipping code which needs to be tracked
* A lot or product number which needs to be tracked in case of recall
* Manufactured sub-assemblies have serial numbers which are tracked during manufacture
* Final products are assigned serial numbers and these are listed on shipping documents when sent to customers.
* Product attributes are assigned to define product specifications. Products need to be searchable based on the individual attribute values and/or attribute sets. (For an example of how complex this can get, see [Arrow Electronics Parametric Search](http://components.arrow.com/part/search/^6/11/863))
* Guarantee dates that need to be tracked. Items close to expiry need to be located in inventory and put on sale or disposed of.
* Warranty dates based on the date sold

Next, split the information into the product level and instance level information. The product level information will be similar for every instance associated with that product.

For each element of the information, define an attribute using the [**Attribute Window**](http://wiki.adempiere.net/ManPageW_Attribute). In this window you can define the attribute using a name, description and the type of value the attribute will hold. The available choices are:

* List
* String with a max length of 40 characters
* Numeric

If using the List type, you have to define the allowed attribute values on the [**Attribute Value Tab**](http://wiki.adempiere.net/ManPageW_Attribute#Tab:_AttributeValue).

The Attribute Window also has two check box fields:

* Mandatory - indicating the attribute must be set when an inventory transaction takes place. Failure to do so will cause an error/warning when trying to complete the document.
* Instance Attribute - if checked the attribute is an instance attribute which relates to specific instance information. If unchecked, that attribute is a product attribute that relates to product information common to all instances. The product attribute can be changed in the product window.

Once all the attributes are entered, combine them in Attribute Sets in the [**Attribute Set Window**](http://wiki.adempiere.net/ManPageW_AttributeSet). Here you can set the name, description of the attribute set and select the attributes associated with the set. You can also determine if the set contains a lot code, serial number of guarantee date and the parameters that control these. Finally, you can set the controls associated with the set so that its use is mandatory or not. The available options are:

* Always mandatory
* Not Mandatory
* When Shipping

A mandatory attribute set needs to be filled on every document where the product is referred to. If the mandatory type is set to When Shipping, the attribute set needs to be filled on any material shipment document but not on other transactions.

The [**Attribute Use Tab**](http://wiki.adempiere.net/ManPageW_AttributeSet#Tab:_AttributeUse) is used to determine the attributes that are part of the attribute set and the sequence of their appearance on the forms.

The [**Exclude Tab**](http://wiki.adempiere.net/ManPageW_AttributeSet#Tab:_Exclude) can be used to control the mandatory nature of the attribute set by excluding certain tables. This is helpful when attributes are required only on outbound shipping but not on the original purchase, for example.

### Lot Codes

Lot codes are essentially strings and can be manually entered or created and tracked in ADempiere in a way similar to document and sequence numbering.

To create Lot codes as a sequence of numbers, open the [**Lot Control Window**](http://wiki.adempiere.net/ManPageW_LotControl) in **Material Management→Product Attributes**. There you can establish:

* the control name;
* description;
* the starting number of the lot code;
* the increment to use when creating a new code; and
* the prefix and suffix for the codes created.

On the Lot Control window there is also an [**Exclude Tab**](http://wiki.adempiere.net/ManPageW_LotControl#Tab:_Exclude) tab. Identifying a table in this tab will prevent the lot control "New Record" button from appearing on the [Product Attribute Dialog](http://wiki.adempiere.net/Product_Attribute_Dialog) when creating a new attribute set instance.

In the [**Lot Window**](http://wiki.adempiere.net/ManPageW_Lot), you can manage the actual lot codes created using the Product Attribute Dialog and the Lot Control or you can create your own Lot codes and assign them to a product. Here you can add additional information to the lot code such as a description, comment and date-from and date-to limits for the lot. The string Name field is the actual Lot Code. Date From and Date To limits can be used to show only valid lot codes in the Product Attribute Dialog.

When an Attribute Set Instance is created or edited in the Product Attribute Dialog, there are two fields that reference the Lot: **Lot No** and **Lot**. The contents of the **Lot No** field are used in the description of the Attribute Set.

[![Image:ASI\_NewFromTemplate.png](http://wiki.adempiere.net/images/5/52/ASI_NewFromTemplate.png)](http://wiki.adempiere.net/File:ASI_NewFromTemplate.png)

The underlying model has a Lot ID (M\_Lot\_ID) which is associated with the lots in the [**Lot Window**](http://wiki.adempiere.net/ManPageW_Lot). This Lot ID is set by the **Lot** combo box. If the Lot Id is not set, the **Lot No** text field will be editable and you can enter the lot number manually. Otherwise, the Lot No field will be read-only and will contain the number/name of the lot selected in the Lot combo box.

{% hint style="info" %}
Text entered directly in the Lot No text field in the Product Attribute Dialog is just a text value in the Attribute Set Instance - it will not appear in the Lot Window.
{% endhint %}

The **Lot No** text field can be used if the Lot Control and Lot window are not required. This may be the case, for example, if tracking the lot numbers on incoming material. In such a case, you could setup the Lot Control to exclude the tables where the Attribute Instances may be set, which would prevent selection of a Lot and encourage or force entry of text in the Lot No field.

**Prefixes and Suffixes for Lot Codes**

The prefixes and suffixes in the Lot Control window can be used to distinguish the lots in the displays of the Attribute Set Instance. The strings in the Prefix and Suffix fields will be used in the lot codes. For example, if the Prefix is "Lot" and the Suffix "E", when creating a new Lot record, say 124, it will be recorded and will appear in the Lot combo box and the Lot No field as "Lot124E".

Further, in the [**Attribute Set Window**](http://wiki.adempiere.net/ManPageW_AttributeSet), there are two prefix and suffix delimiters for Lot identification:

* Lot Char Start Overwrite and
* Lot Char End Overwrite.

By default, these will be the "«" and "»" characters. These characters can be over-written in the description by a **single** character in the Lot Char Overwrite fields. Multiple characters or a single space (" ") will be ignored.

For example, if the Lot Char Start/End Overwrite fields are filled with "@" characters, and using the above example of the lot prefix and suffix codes, the display will appear as shown below.

[![Image:ASI\_ShowingPrefixSuffix.png](http://wiki.adempiere.net/images/2/2d/ASI_ShowingPrefixSuffix.png)](http://wiki.adempiere.net/File:ASI_ShowingPrefixSuffix.png)

### Serial Numbers

Serial numbers are the ultimate instance attribute as they should be unique in the life of a product.

Serial Number attributes are essentially similar to Lot numbers with the exception that the serial number only has a text entry option on the Product Attribute Dialog and no combo box to select existing serial numbers from.

To create serial numbers as a sequence of numbers, open the [**Serial No Control Window**](http://wiki.adempiere.net/ManPageW_SerialNoControl) in **Material Management→Product Attributes**. There you can establish:

* the control name;
* description;
* the starting number of the serial number;
* the increment to use when creating a new number; and
* the prefix and suffix for the codes created.

This window behaves identically to the Lot Control window. Note that there is also an [**Exclude Tab**](http://wiki.adempiere.net/ManPageW_SerialNoControl#Tab:_Exclude) tab. Identifying a table in this tab will prevent the serial number control "New Record" button from appearing on the [Product Attribute Dialog](http://wiki.adempiere.net/Product_Attribute_Dialog) when creating a new attribute set instance.

**Prefixes and Suffixes for Serial Numbers**

The prefixes and suffixes in the Serial No Control window can be used to distinguish the serial numbers in the displays of the Attribute Set Instance. The strings in the Prefix and Suffix fields will be used in the display of serial numbers. For example, if the Prefix is "ICX" and the Suffix "-01", when creating a new serial number record, say 104789, it will be recorded and will appear in the serial number field as "ICX104789-01".

Further, in the [**Attribute Set Window**](http://wiki.adempiere.net/ManPageW_AttributeSet), there are two prefix and suffix delimiters for serial number identification:

* Serial Char Start Overwrite and
* Serial Char End Overwrite.

By default, these will be the "#" and "" characters respectively. These characters can be over-written in the description by a **single** character in the Serial Char Overwrite fields. Multiple characters or a single space (" ") will be ignored.

**Assigning Serial Numbers to Product Instances**

In planning the use of serial numbers, consider how the serial numbers are determined for and found on your products.

* Are they defined by the vendors of those product?
* Are they defined in the production process?
* Are they determined by the number on a sticker applied to the product at the time of final assembly?
* Are they chosen at the time from a list of available numbers on a spreadsheet perhaps?
* Is there a bar code associated with the serial number?

Answers to these questions will help in defining when and how the attribute set instances should be defined for the products.

For example, suppose the serial numbers are defined by stickers applied to the products as one of the final steps in the manufacturing process. The serial number control is maintained by the printer of the stickers so it is not required in ADempiere. The stickers come in large sheets. Each assembly station has several sheets and the stickers are applied as part of the product BOM and assembly process. Keeping track of the stickers is not important. Finished goods are placed on a shelf for testing. When moving the products from the assembly area to the testing area, the attribute set instance information is captured on an Inventory Move document generated by the [**Inventory Move Window**](http://wiki.adempiere.net/ManPageW_InventoryMove). An Inventory Move line is created for each (Qty 1) product and the Attribute Set Instance To field is filled using the serial number on the sticker. This is accomplished with a bar code scanner which is programmed to read the serial number and add the short-cut codes (tab, space bar, enter key, F2 and F4) as required to save the attribute set instance, save the inventory move line record, copy the line and then open the Attribute Set Instance To field again.

### Guarantee Date

The **Guarantee Date**, like the Lot Number, is another instance attribute that applies to a set of instances of a product. Guarantee Dates provide a date that can be calculated when the attribute set instance is created and which can be interpreted in a variety of ways depending on the product. For example, it could be the Best Before date on food products or it could be used to indicate the beginning of a performance guarantee or the end of a trial period.

Guarantee Dates are defined on the [**Attribute Set Window**](http://wiki.adempiere.net/ManPageW_AttributeSet) by selecting the **Guarantee Date** check box. The Guarantee Date can be made mandatory by selecting the **Is Mandatory** check box. If a new attribute set instance is created and a new guarantee date record created, the date will be defined by the **Guarantee Days** field. When the new record is created the resulting date will be Guarantee Days from the current system time.

Guarantee Dates are set in the [**Attribute Set Instance Window**](http://wiki.adempiere.net/ManPageW_AttributeSetInstance) by clicking on the **New Record** button or entering a date in the **Guarantee Date** field.

When the record is saved, the date will appear in the attribute set instance description as a date formatted according to the local language settings. For example: #101\_«125»\_07/12/2013.

## Assigning Attribute Sets to Products

Attribute Sets are assigned to Products in the [**Product Window**](http://wiki.adempiere.net/ManPageW_Product). By defining an attribute set in the **Attribute Set** field, and attribute set instance can be created in documents that deal with product transactions.

### Setting Product Attribute values

If you need to define product attribute values - attribute instance information common to all items of that product - such as specifications, use the **Attribute Set Instance** field in the Product window and click on the button in the field. This will open the [Product Attribute Dialog](http://wiki.adempiere.net/Product_Attribute_Dialog) where you can set the product attributes that will be used in all instances of that product. This special instance becomes a template that is copied to other instances when the those instances are created. Note that the Product Attribute Dialog will only show the Product Attributes and not the Instance Attributes defined in the attribute set.

The Product Attributes can only be edited in the Product window. When the template is used to create a new instance in a document, the Product Attribute Dialog will show the Product Attributes as read only.

## Setting Instance Attribute Information

Attribute Set Instances are created on documents that deal with product transactions. When a product that has an attribute set defined is entered on a line these documents, the **Attribute Set Instance** field is activated and can be used to create, edit or delete the Attribute Set Instance information.

Clicking the button in the Attribute Set Instance field will open the Product Attribute Dialog which will show the Attribute Instance Values. Here the values can be created as a new record if the **New Record** is selected at the top right.

If the Instance has been created from a Product Attribute Set template, the top right check box will show **Edit Record** instead.

An alternative is to select the Attribute Set Instance from the list of previously created Attribute Set Instances by clicking on the **Select existing record** button. This can be useful if, for example, a number of production runs produce products that all have the same lot and guarantee dates.

If an Attribute Set Instance has been defined, it can be deleted from that field by opening the Product Attribute Dialog and clicking the Cancel button.

### Automatic Selection of Attribute Set Instances

ADempiere uses Attribute Set Instance information to track products in inventory and tries to do so intelligently. For example, if no attribute set instance information is specified on a customer shipment lines, in completing the document, the system will select from the available Attribute Set Instances in inventory and attach this information to the shipping record in the [**Attributes Tab**](http://wiki.adempiere.net/ManPageW_Shipment\(Customer\)#Tab:_Attributes).

If you are going to allow the system to select the attributes in this fashion, be sure to test that the selection matches the process used in handling the inventory.

{% hint style="warning" %}
Certain documents, like the POS Order, will create new instances of attributes regardless of what is in inventory. This may create problems with inventory tracking where products with attribute set instances are sold using a POS. This may be a bug.
{% endhint %}

## Displaying Attribute Set Instance Info on Documents

## Searching Attribute Information

### Attribute Search

### Attribute Instances

### Product Info Window


# Example - Using Product Attributes

## Example - Using Product Attributes   <a href="#firstheading" id="firstheading"></a>

| [![Image:Note.gif](http://wiki.adempiere.net/images/6/62/Note.gif)](http://wiki.adempiere.net/File:Note.gif) | <p><strong>Note:</strong></p><p>This page describes features not yet incorporated. Some of the features described here are part of the changes in ADEMPIERE-72 - fixes to the info windows and lookup/search fields. In version 3.8 and earlier, product attributes and instance attributes can not co-exist.</p> |
| ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### Fertilizer in Garden World

#### Attribute setup

Garden World sells lawn fertilizer in 50 and 70kg bags. They want to expand this to a variety of formats (50 or 70 Kg bags, cubic yards), chemical specifications, and base compost (chemical, manure, mushroom, peat). Each product has a lot number and a guarantee date. Each of these things represents an attribute of the fertilizer product. Collectively, they represent an attribute set and, with a specific lot and guarantee date defined, they represent an instance of the attribute set.

The demo database has an attribute set defined for Fertilizer Lot and that needs to be expanded to include the format, chemical specs and base compost. This is done by defining attributes for each of these items as follows:

* Open the [**Attribute Window**](http://wiki.adempiere.net/ManPageW_Attribute) window and create new attributes as follows:
  * New Attribute - Package
    * Name: Pkg
    * Description: Fertilizer Package
    * Attribute Value Type: List
    * Instance Attribute: checked
    * Attribute values
      * New Value - 50Kg
        * Key: 50Kg
        * Name: 50Kg
        * Description: 50 Kilogram bag
      * New Value - 70Kg
        * Key: 70Kg
        * Name: 70Kg
        * Description: 70 Kilogram bag
      * New Value - Cubic Yard
        * Key: CY
        * Name: CY
        * Description: Cubic Yard
  * New Attribute - Chemical - Nitrogen
    * Name: N
    * Description: Nitrogen
    * Attribute Value Type: Number
    * Instance Attribute: unchecked
  * New Attribute - Chemical - Phosphorous
    * Name: P
    * Description: Phosphorous
    * Attribute Value Type: Number
    * Instance Attribute: unchecked
  * New Attribute - Chemical - Potassium
    * Name: K
    * Description: Potassium
    * Attribute Value Type: Number
    * Instance Attribute: unchecked
  * New Attribute - Base
    * Name: Base
    * Description: Base Component
    * Attribute Value Type: List
    * Instance Attribute: unchecked
    * Attribute values
      * New Value - Chemical
        * Key: Chem
        * Name: Chem
        * Description: Chemical
      * New Value - Manure
        * Key: Man
        * Name: Manure
        * Description: Manure
      * New Value - Mushroom
        * Key: Mus
        * Name: Mushroom
        * Description: Mushroom
      * New Value - Peat
        * Key: Peat
        * Name: Peat
        * Description: Peat

Next, open the [**Attribute Set Window**](http://wiki.adempiere.net/ManPageW_AttributeSet) and find the attribute set "Fertilizer Lot". Note that the attribute set contains a lot number and a guarantee date. Add the new attributes to this attribute set.

Clear the cache or log out and in before continuing.

#### Assigning Attributes to Products

Now, open the [**Product Window**](http://wiki.adempiere.net/ManPageW_Product) and find the Fertilizer #50 product. Note that the attribute set is already defined as Fertilizer Lot. Click on the button in the Attribute Set Instance field to open the [Product Attribute Dialog](http://wiki.adempiere.net/Product_Attribute_Dialog) and set the product attributes for the Fertilizer #50 product. Specifically, set these as shown:

[![Image:Product\_asi\_example.png‎](http://wiki.adempiere.net/images/a/ab/Product_asi_example.png)](http://wiki.adempiere.net/File:Product_asi_example.png)

Note that the lot and guarantee dates do not appear on this window. They will be set later.

Repeat this process for the Fertilizer #70 product: find the product, assign the attribute set then assign the product attributes. For Fertilizer #70, use the 70Kg package.

Now we have to make some fertilizer that meets these specs. We will do this with the [**Production Window**](http://wiki.adempiere.net/ManPageW_Production) window. Create a new production header and save it. Then move to the [**Production Plan Tab**](http://wiki.adempiere.net/ManPageW_Production#Tab:_ProductionPlan) and select Fertilizer #50 as the product and a quantity of 40. Set the Locator to Fertilizer and save the record. Create a second record and repeat this step with the Fertilizer #70 product. Move back to the [**Production Header Tab**](http://wiki.adempiere.net/ManPageW_Production#Tab:_ProductionHeader) and click the "Create/Post Production" button. This will pull the BOM from the product window and fill the [**Production Line Tab**](http://wiki.adempiere.net/ManPageW_Production#Tab:_ProductionLine).

Move to the [**Production Line Tab**](http://wiki.adempiere.net/ManPageW_Production#Tab:_ProductionLine) and find the Fertilizer #50 product. Note that the Attribute Set Instance field is blank. Click the Attribute Set Instance button and the [Product Attribute Dialog](http://wiki.adempiere.net/Product_Attribute_Dialog) will appear again.

[![Image:Production\_asi.png‎](http://wiki.adempiere.net/images/3/35/Production_asi.png)](http://wiki.adempiere.net/File:Production_asi.png)

The form is a copy of the attribute set instance template created in the product window and now the instance attributes are visible. In this dialog, the lot number and guarantee date can be set manually or you can click on the New Record button to calculate the next lot number or the guarantee date based on the attribute set information. The logical place to do this is in the production process.

Close the Product Attribute Dialog and note that the Attribute Set Instance field is filled in. Save the record. If you click on the Attribute Set Instance button again, you can see the values of the attributes. Repeat this with the Fertilizer #70 Production Plan.

Back on the [**Production Header Tab**](http://wiki.adempiere.net/ManPageW_Production#Tab:_ProductionHeader) and click the "Create/Post Production" button again to complete the process. The new product will appear in the Fertilizer locator.

Open the Product Info window to see the attributes available.

[![](http://wiki.adempiere.net/images/thumb/e/e4/Productinfo_fert50.png/800px-Productinfo_fert50.png)](http://wiki.adempiere.net/File:Productinfo_fert50.png)

Select or search for the Fertilizer #50 product. The Warehouse tab shows 40 in stock. If you click on that line in the Warehouse tab and then click on the Available to Promise tab, and the Show Detail check box, you will see the instance attribute information. In this case, (<<120>> 2013-06-30).

To see the Product attribute info for the Fertilizer #50 product, click on the Product Attribute tab. It will list the product attributes as

```
***  Product Attribute  ***
 Pkg: 50Kg
 N: 10
 P: 20
 K: 15
 Base: Chem
```


# Defining the Product

With the setup work complete, the products can be created easily using the Product Window. There are several mandatory elements to the product definition:

* **Product** **Name**
* **Product Category**
* **Tax Category**
* **Unit of Measure**
* **Product Type**

These are the minimum required to define the product. Apart form the mandatory fields, there is a large number of other fields helpful in defining the products. The next sections will go into more detail on how to configure these fields. But first, its important to look at the various [Product Types](https://adempiere.gitbook.io/docs/introduction/products-and-material-management/product-setup/defining-the-product/product-types) possible so some of the terms will make sense.


# Product Types

Describe the Product Types available when defining products

A product may be physical, like an apple, or intangible, like a fee for a service. They can be very simple in concept or a complex assembly of sub-components. ADempiere uses the product type to determine how the product information should be treated. Product Types are entered in the Product Window. There are four Product Types availabl&#x65;**:**

| **Product Type** | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Expense Type** | A product that may or may not be physical. It may require material handling but it is not tracked in inventory. The purchase of the product creates an expense rather than an increase in inventory value. The Expense Type is used where inventory tracking is not required, for example, in products with low volume, low cost and rapid turnover such as office stationary but where more granularity is required in the financial information than, say, the total cost of Office Supplies.  Expense Type products are usually purchased, rather than sold.  Expense Type products are created in the Expense Type window. |
| **Item**         | A physical good, an Item is something that is manufactured, bought, or sold and may be held in inventory (stocked).  Items can typically be measured by some physical unit of measure and may have a size and weight. Material handling processes are important and the location of the item in inventory can be tracked.  Costs associated with the item can also be tracked using specific cost methods.  Unlike the other Product Types, which affect the income statement accounts, the Item product type cost affects the balance sheet Inventory (or Product Asset account).                                             |
| **Resource**     | A Resource is a type of product that is typically limited in availability and controlled with a calendar and schedule.  Resource products are not tracked in inventory.  A consultant, hotel room or a piece of manufacturing equipment would be examples. Resource products are usually sold, not purchased.  Resource products are created in the Resource window.                                                                                                                                                                                                                                                           |
| **Service**      | A service product is not tracked in inventory. It can be considered as a fee such as consulting fees or utility costs.  Services are most often expensed but may be included in costs related to work in progress. They can be sold or purchased.                                                                                                                                                                                                                                                                                                                                                                              |


# Basic Product Setup

How to configure a basic product.

For details on the various fields, see the Manual for the Product Window. This page won't go into all of them, just the ones that are not standard.

## Product Fields

### The Key Identifiers: Value, Name, UPC and SKU

A Product appears in windows and forms using a lookup editor that displays the identifier for the Product, usually its value and name together. When you need to enter a product in the editor, the editor tries to match the data entered with one of the four key identifiers: the Value, Name, Universal Product Code (UPC) or Stock Keeping Unit (SKU). For users who are familiar with the products and can memorize one of these, its a simple matter to enter the data.

A laser scanner can also be used to populate the editor from a label on the product using one of these fields. If you are using a laser scanner, setup one of these fields to match the output of the scanner.

The goal should be to enable users and scanners to uniquely identify the product with a simple entry. If the entry is ambiguous and relates to more than one product, the Product Info window will appear. While helpful, this takes time and can quickly become annoying if entering large amounts of data.

### Version Number

A reference field, the version number of the Product is used when assets are delivered. The Version Number is copied to the Asset.

### Groups, Classes, Classifications and Categories

These fields are helpful for summarizing reports. See [Product Categories](https://adempiere.gitbook.io/docs/introduction/products-and-material-management/product-setup/product-categories) and [Product Classifications, Classes and Groups](https://adempiere.gitbook.io/docs/introduction/products-and-material-management/product-setup/product-classifications-classes-and-groups) for more info. The Product Category is mandatory.

### Summary Level

The Summary Level field is intended to allow a tree of products to be defined and used in reporting. Where the summary level product is identified in a report, the results will be based on the child products. The Summary Level field can be set in the Product window but the selection of child products is done in the Tree Maintenance window. See [Trees and Tree Maintenance](https://adempiere.gitbook.io/docs/system-administration/general-rules/system-settings#trees-and-tree-maintenance) for more info.

### Tax Category

Select the appropriate Tax Category. See the description of [Taxes Setup](https://adempiere.gitbook.io/docs/introduction/accounting-and-performance-analysis/tax-setup) for more information about the Tax Category.

### Tax Type

Part of the Global Tax Management menu, the Tax Type field is not used in the core system but is available if you need to develop a Global Tax Management system to treat complex tax cases. Some Localizations may use this field.

### Revenue Recognition

Select the appropriate Revenue Recognition type. This field only appears if the Product is sold. The field is currently for reference only. See [Revenue Recognition](https://adempiere.gitbook.io/docs/introduction/revenue-recognition) for more info.

### UOM

Enter the UOM in which the product will be stored. This needs to be the smallest UOM that will be used for the Product. See [Units of Measure](https://adempiere.gitbook.io/docs/introduction/products-and-material-management/product-setup/units-of-measure) for more information about using UOMs and the conversion from one to the this "Product" UOM.

### Company Agent

The sales rep or User responsible for this product. Used for reference only.

### Product Type

Select the appropriate product type. See [Product Types](https://adempiere.gitbook.io/docs/introduction/products-and-material-management/product-setup/defining-the-product/product-types) for more information about the possible choices.

### Mail Template

The mail template is used when this Product relates to an Asset or Item that can be delivered by e-mail as a URL to a download location. The mail template can be used to provide information about the product or to asset. The Mail Template is used in the Asset Delivery process to deliver customer assets electronically.

### Weight

Enter the weight of the product. This field only appears if the Product Type is "Item". The weight is used in calculating the total weight of an order or shipment, in estimating the cost of shipping or applying landed costs. There are no units for the Weight so you will need to have a system wide definition for which unit to use.

### Volume

Enter the volume of the product. This field only appears if the Product Type is "Item". The volume is used in calculating the total volume of an order or shipment, in estimating the cost of shipping or applying landed costs. There are no units for the Volume so you will need to have a system wide definition for which unit to use.

### Freight Category

Select the appropriate Freight Category. The Product Freight Category is used in the order and shipping documents to determine which Shipper to use and the estimated costs of the shipment based on the product weight. Freight Categories are defined in the Freight Category window and Shippers in the Shipper window. Each Shipper can be associated with a number of Freight Categories. The actual Shipper used and the final Freight Category are set on the Shipping document.

### Drop Shipment

Select this field if the product can be drop shipped (sent direct from the vendor to the customer.) For reference only.

### Stocked

Select if the product is to be held and tracked in inventory. This field will only appear if the Product Type is "Item".

{% hint style="info" %}
On an Invoice or Order, non-stocked products that have a BOM will have the BOM tree "exploded" - meaning expanded - when the document is prepared. In this case the BOM line products will be added to the document as if they were additional products. The BOM ***Valid From*** and ***Valid To*** dates must agree with the document date, ***Date Promised*** for orders and ***Date Invoiced*** for invoices, and the BOM ***Search Key*** field needs to match the Product ***Search Key*** field. See [Product Bill of Materials](https://adempiere.gitbook.io/docs/introduction/products-and-material-management/product-setup/defining-the-product/product-bill-of-materials) for more information.
{% endhint %}

### Locator

The default location for the product in storage. This field will only appear if the item is Stocked. This is the Locator that will be used when the product is first added to a Material Receipt Line IF the Locator Warehouse and the Warehouse identified on the Material Receipt are the same. If they Warehouses are different, the default Locator for the Warehouse will be used.

For Production Light, if the Production header is created from an Order Line, the Product Locator will be used. When the Production BOM is created, the BOM line products will also use the Product Locator.

Other than setting default values in a few documents, this field does not control the location in storage at all.

{% hint style="info" %}
Note that the Locator used for reservations and orders will always be the default locator for the warehouse.
{% endhint %}

### Shelf Width, Shelf Height, Shelf Depth, Units Per Pallet

These fields provide information about how the Product fits into inventory locations. The fields are not used other than for information and reference.

### Bill of Materials, Verify BOM, Verified

If a Bill of Materials (BOM) is defined on the BOM tab of the Product Window, the Bill of Materials checkbox will be selected and the Verify BOM button and Verified checkbox will be visible. After the BOM is entered, you can click the Verify BOM button and the system will check the BOM products and processes making sure there are no recursive products in the BOM tree. Once the BOM has been verified, the Verified checkbox will be selected.

{% hint style="warning" %}
Any BOM defined for the product will not be available to use unless the Verify BOM process is completed and the Verified checkbox is selected.
{% endhint %}

### **Print detail records on invoice**

This field appears if the Product has a BOM. If selected, the contents of the BOM will be added to the Invoice print out, not as new line items but as details of the master product. This does not affect the invoice document - no lines are added. It only affects the invoice Print or Print Preview output.

{% hint style="warning" %}
If the product has multiple BOMs, all of the BOM lines will be printed on the Invoice, even the inactive ones. See issue [2305](https://github.com/adempiere/adempiere/issues/2305).
{% endhint %}

### **Print detail records on pick list**

This field appears if the Product has a BOM. If selected, the BOM details will be added to the Pick List for the Product. This does not affect the shipment document - no lines are added. It only affects the Pick List Print and Print Preview output.

The same caution as for ***Print detail records on invoice*** applies.

### Purchased, Sold

These fields indicate if the Product is purchased or sold or both. As a rule of thumb, if the product is not purchased but is sold, it must be manufactured and will usually have a BOM associated with it. On the other hand, if the product is purchased but not sold, it will usually be consumed somehow, typically as a component in another product.

The Purchased flag is used when calculating replenishment plans. Requisitions are created for purchased products.

{% hint style="warning" %}
If the Product is purchased and also has a BOM, the behavior is not consistent across all replenishment processes. In some cases a requisition will be generated instead of a manufacturing order. In others, the manufacturing order will come first. See [issue 2286](https://github.com/adempiere/adempiere/issues/2286).
{% endhint %}

The Sold field is not used much. It is used to limit the display of products in the Point of Sale (POS) and web store. Otherwise, it is for reference only.

{% hint style="info" %}
The real control on whether a product is purchased or sold is the Price List. If the Price List has "Sales Price List" selected, then products on the list can be sold. If not, the products on the price list can be purchased. Sales orders only use sales price lists and purchase orders don't. Any product, regardless of the settings of "Purchased" or "Sold" can be added to any price list.
{% endhint %}

{% hint style="info" %}
The rules of Purchased/Sold do not apply to Counter Docs - documents that are automatically created to balance processes. For example, inter-organizational invoices where one organization purchases a product from another organization within the same client.
{% endhint %}

### Discontinued

The Discontinued field shows if the product will no longer be produced or purchased. When a product is discontinued, it will not appear in the POS. When the field is selected, the User who made the change is recorded.

### Expense Type

If the Product Type is set to "Expense type", the Expense Type field will appear and will contain the related Expense Type. Expense Type products are not created in the Product Window but can be viewed. They are created in the Expense Type window.

### Resource

If the Product Type is set to "Resource", the Resource field will appear and will contain the related Resource. Resource products are not created in the Product Window but can be viewed. They are created in the Resource window.

### Subscription Type

Enter the Subscription Type. Subscription Types are created and managed in the Subscription Type window. The value is for reference only. Subscription management has not been implemented. See [issue 411](https://github.com/adempiere/adempiere/issues/411).

### Exclude Auto Delivery

Select to exclude this product from Auto Delivery via a process. Auto delivery can occur if the Customer (Business Partner) has a Delivery Rule other than "Manual". Selecting Exclude Auto Delivery on the Product window will prevent automatic delivery of this product. This is useful where the product is sensitive, potentially dangerous or stock levels are likely to be insufficient. A product that should be excluded from air freight would be a good example.

The Exclude Auto Delivery flag is ignored if the Business Partner Delivery Rule is "Force" or if the Order is one of the following document types, all of which over-write the Delivery Rule with "Force":

* On Credit Order,
* Warehouse Order,
* POS Order, or
* Prepay Order.

### Image URL and Description URL

The Image URL and Description URL are used in the Web Store. The Image URL is used to display the image of the product and the Description URL is used as a link for the Product Name.

### Guarantee Days and Min Guarantee Days

These numbers are used to calculate the Good For Days, Shelf Life Days and Shelf Life Remaining values shown in the Attribute Instance dialog.

The Good For Days (GFD) is calculates as

$$
GFD = DaysBetween(ASI.GuaranteeDate, SysDate) - MGD
$$

where ASI.GuaranteeDate is the Guarantee Date of a particular Attribute Set Instance of this Product, SysDate is the current system date and MGD is the Product Min Guarantee Days.

The Shelf Life Days (SLD) is simply

$$
SLD = DaysBetween(ASI.GaranteeDate, SysDate)
$$

and Shelf Life Remaining Percent (SLRP) is

$$
SLRP = 100\*DaysBetween(ASI.GuaranteeDate, SysDate)/GD
$$

where GD is the Product Guarantee Days and GD > 0. If GD <= 0 the SLRP is shown as 0.

### Attribute Set and Attribute Set Instance

Enter the Attribute set used by the product and the template Attribute Set Instance. The Attribute Set Instance field will not be enabled until the Attribute Set field has a suitable value.

For more information about these fields, see [Product Attributes, Sets and Instances.](https://adempiere.gitbook.io/docs/introduction/products-and-material-management/product-setup/product-attributes-sets-and-instances)

### Featured in Web Store

This field should be selected if the product will be shown in the Web Store by default. The product must also have the Is Self-Service field selected and meet the requirements of that field. Products that are not selected as part of the Web Store but that are on the same price list and that have the Is Self-Service field selected can be shown in the Web Store Shopping Basket.

### Self-Service

Selecting the field is required to display the product in the Web Store, by default if the field Featured in Web Store is also selected. The product must also be Active, Sold and be on a suitable price list with a Standard Price greater than zero.

## Copying a Product

After the basic product fields are generated here, if the product is similar to another product, the Copy From Product button at the bottom of the form can be used to copy a number of the subordinate tab data from that product to this one.

The current Product record needs to be saved. When you click the Copy From Button, a dialog will appear where you can select the source product. Click the Confirm button and the following data will be copied from the selected product:

* Product Prices
* Substitutes
* Related Products
* Warehouse Replenishment Rules
* Product Business Partner Info
* Product Download Info

{% hint style="info" %}
Note that the Copy From Product process does not fill in any of the Product Tab fields and doesn't change the Accounting
{% endhint %}


# Product Bill of Materials

Describes the creation and maintenance of a Product Bill of Materials (BOM)

A Bill of Materials or BOM is a list of raw materials, processes, sub-components and assemblies that describe the product. A BOM is required to manufacture a product. The Product BOM is comprised of a header record with information about the BOM and a number of subordinate lines representing the components used or required. A BOM can range from a simple list to a complex tree of components and processes that turn raw material into the final product.

The BOM has a number of possible uses:

* It can be used to breakdown a product on Orders (referred to as "exploding" the BOM).  The Order would be created using one line for the master product but the printed Order and Shipping documents would show the BOM components. In this case, the product would function as a summary product for its components, making it easy to add a number of lines to an order with a single entry.  (See the note in the [Stocked field in Basic Product Setup ](https://adempiere.gitbook.io/docs/introduction/products-and-material-management/product-setup/basic-product-setup#stocked)for more info.)
* The BOM can be "Dropped" onto an Order, Invoice or Project which has the effect of entering the BOM components as lines on the document.  During this process, options and product configuration are possible.
* In manufacturing, the BOM provides the processes and materials necessary to create the master product.  Manufacturing planning relies on this data to create effective and efficient plans of what needs to be built when to fulfill customer orders.
* For procurement, the BOM converts demand for the master product into demand for its components allowing procurement planning to purchase required material in a timely manner.
* For Engineering, the BOM provides a way to manage the configuration of the product during development prior to manufacturing.
* The BOM also provides cost information and allows costs to be "rolled up" to the parent product.

## Defining a BOM

The BOM is defined in the **Product** window, **BOM** tab. It can also be defined in the **Bill of Materials & Formula** window, which is essentially a copy of the **BOM** tab.

Start by creating a new record. If in the **Product** window, creating the new record will fill in the ***Product*** field with the parent Product. In the **Bill of Materials & Formula** window, you will need to start by selecting the parent or final Product.

{% hint style="info" %}
If the manufacturing process using this BOM creates other final products, these can be identified in the **BOM Components** by selected *Co-Product as the **Component Type*** and setting the ***Quantity Required*** to a negative amount.
{% endhint %}

The system will then fill the following fields with default values taken from the parent Product or set as described:

* ***Attribute Set Instance*** - the template value from the Product will be used.
* ***Search Key***&#x20;
* ***Name***
* ***Description***
* ***Comment/Help***
* ***Unit of Measure***
* ***Valid from***  - the date will default to the current system date.
* ***BOM Type*** - will default to *Currently Active*
* ***BOM Use*** - will default to *Manufacturing*

Additional information about the non-standard fields or special conditions follows.

## Search Key

If you have more than one BOM for this Product, the Search Key will have to be unique for each BOM.

### Default BOM

{% hint style="warning" %}
The BOM where the ***Search Key*** matches the **Product** ***Search Key*** will be considered the default BOM for the Product regardless of its ***BOM Type*** or ***BOM Use*** settings.
{% endhint %}

This default BOM is used:

* When the Product appears as a BOM Component on another BOM with ***Component Type*** set to *Phantom*,  then this BOM is used as the Phantom BOM and is exploded on Manufacturing Orders.
* When doing Product Planning, the Default BOM is used if a specific BOM was not specified for the Product.
* When calculating the costs a Bill of Materials, the default is used if there is no Product Planning record for the product or no BOM specified on that record.
* When automatically creating a Manufacturing Order as part of the resupply process for a Warehouse or from a Project
* When adding a product to a Manufacturing Order where there is no Product Planning record for the matching Organization, Product, Warehouse, Resource on the Order.
* When preparing Distribution Orders.
* When performing a [BOM Drop](https://adempiere.gitbook.io/docs/introduction/products-and-material-management/bom-drop).

## Attribute Set Instance

The template of the Product Attribute Set Instance, if one exists, can be changed from this field. It is not possible to set Instance values in the Product BOM. The template applied here will be applied to the resulting products of the BOM. See [Product Attributes, Sets and Instances](https://adempiere.gitbook.io/docs/introduction/products-and-material-management/product-setup/product-attributes-sets-and-instances) for more information.

## UOM

The BOM can use any UOM (Unit of Measure) valid for the Product - meaning where a Product UOM conversion exists. This is helpful where the units of measure for manufacturing or procurement are different than the units of measure used in sales. See [Units of Measure](https://adempiere.gitbook.io/docs/introduction/products-and-material-management/product-setup/units-of-measure) for more info.

## Change Notice

The ***Change Notice*** field is used to record the Change Notice that is/was being applied to the BOM. A Change Notice is a way to inform people that need to know about the change as to the reasons and nature of the change.

The Change Notice information is passed to the Manufacturing Order when it is created.

Management of change can be complex. See [Engineering Change Management](https://adempiere.gitbook.io/docs/introduction/manufacturing/engineering-change-management) (ECM) for more information. In summary, the need to make a change is identified on Change Request and this change may affect one or more BOMs for the product and its components. The actual change is specified in a Change Notice. The affected BOM is copied to a new record, the new record is modified according to the change, and the Change Notice provides a reference on the new BOM as to what changed, why and who approved it.

## Revision

The ***Revision*** field provides a reference for revision information. The revision information is passed to the Manufacturing Order when it is created.

## Valid From, Valid To

The ***Valid From*** and ***Valid To*** fields are used to ensure the BOM is or will be valid at the time of use. For example, in Manufacturing Orders the dates are tested against the scheduled start date of the manufacturing process.

{% hint style="warning" %}
Valid From/To dates are not used when selecting the "default" BOM. The BOM with the ***Search Key*** field matching the **Product** ***Search Key*** is considered the default. If the default BOM is not valid, you may receive errors in some operations, even if a valid BOM exists. See issue [2303 ](https://github.com/adempiere/adempiere/issues/2303)and [2304](https://github.com/adempiere/adempiere/issues/2304).
{% endhint %}

## BOM Type

The ***BOM Type*** **can be used to describe the purpose of the BOM. There can be typically no more than one** ***BOM Type*** for each ***BOM Use*** value and should be only one *Make-To-Order or* *Make-To-Kit* type per Product. Allowable values and the uses follow:

| BOM Type          | Impacts                                                                                                                                                                                            |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Current Active    | Indicates that this BOM is the currently active BOM for the ***BOM Use*** selected.                                                                                                                |
| Maintenance       | A Maintenance Order will be created for this BOM Type instead of a Manufacturing Order                                                                                                             |
| Make To Kit       | If it exists with a ***BOM Use*** of *Manufacturing*, a **Manufacturing Order** will be created, processed and closed when the parent product is added to a **Sales Order**.  See the notes below. |
| Make To Order     | Similar to Make To Kit but the created Manufacturing Order will be left at the prepared state and will need to be completed, and processed. See the notes below.                                   |
| Product Configure | The BOM used to configure a product where there are options. For more information, see Product Configuration                                                                                       |
| Repair            | Not currently used by the system.                                                                                                                                                                  |
| \<Blank>          | Use if the BOM Type is not known.                                                                                                                                                                  |

## BOM Use

There are five possible settings for the ***BOM Use*** field.

| BOM Use       | Description                                                                                                                                                                   |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Master        | The BOM that is the basis for the other copies.  For ***BOM Type*** *Product Configure,* it is the BOM displayed in the **Product Configuration BOM** or **BOM Drop** window. |
| Engineering   | Can be used to track engineering version and copies of the BOM during development.                                                                                            |
| Manufacturing | Used when the product is manufactured. When associated with ***BOM Type*** *Make To Kit* or *Make To Order*, this BOM will be used to create a **Manufacturing Order**.       |
| Planning      | Not currently used.                                                                                                                                                           |
| Quality       | Not currently used.                                                                                                                                                           |

{% hint style="info" %}

## *Make To Order and Make To Kit*

When an Order is completed, if any product on the order has a BOM with ***BOM Type*** set to *Make To Kit* or *Make To Order*, and the ***BOM Use*** set to *Manufacturing*, then a **Manufacturing Order** will be created automatically to build the products. This applies for all Sales Orders with document types *Standard, Warehouse, On Credit or POS.* The Product must not be [***Purchased***](https://adempiere.gitbook.io/docs/introduction/products-and-material-management/product-setup/basic-product-setup#purchased-sold).

For **BOM Type** *Make To Kit*, the Manufacturing order will automatically have material issued to it and the final product will be received into inventory. This is useful where the manufacturing process is simple and there is no need for pick lists and other material handling processes.

For **BOM Type** *Make To Order*, the Manufacturing Order created will be prepared (materials reserved) but not completed and will need to be processed according to the manufacturing workflow.
{% endhint %}

## \_\_


# BOM Components

Adding component products to a BOM

After the BOM header is entered and saved, the next step is to add the product components to the BOM. The components are a single layer, meaning if there are sub-components, these will have to be entered as lines on a BOM for their parent products.

{% hint style="info" %}
If a BOM already exists that has the set of products identified or nearly, you can copy it easily by clicking the button ***Copy BOM Lines From*** at the bottom of the form view.
{% endhint %}

When you create a new record, the following fields are mandatory:

* ***Line No*** - should default to the next line number, counted by 10
* ***Product***
* ***Issue Method*** - see notes below.
* ***Valid From*** - defaults to the current system date

The other fields will have the following default values:

* ***Component Type*** - the ***Component Type*** will default to *Component*
* **Critical Component** *-* will default to *No*

The following describes the possible settings of the important BOM Component fields and the impacts.

## Product

Select the product component. There are no restrictions on the type of product - it can be any [Product Type](https://adempiere.gitbook.io/docs/introduction/products-and-material-management/product-setup/defining-the-product/product-types).

## Component Type

The Component Type defines what the component does in the BOM and how it should be treated. The following table outlines the choices and their meaning:

| Component Type | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Component      | The default. A component is consumed or incorporated into the final product by the manufacturing process. The quantity entered is in UOM selected.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| By-Product     | A product produced as a result of the manufacturing process.  By-Products are treated differently when calculating the rolled-up cost of the BOM and are not included in the final Product costs nor do they absorb a portion of the cost of the production. By-Products are used in Material Resource Planning (MRP) to calculate supply.                                                                                                                                                                                                                                                                                                                                                |
| Co-Product     | A product that is produced along with the final Product and that will need to be received into inventory when a M**anufacturing Order** is completed.  The ***Quantity*** consumed must be negative. The Costs of a Co-Product are calculated from a  percentage of the BOM cost using either the ***Cost Allocation Percent***, mentioned below, or the ratio of the quantity of Co-Product produced versus the qty of final product.  Co-Products are used in Material Resource Planning (MRP) to calculate supply.                                                                                                                                                                     |
| Phantom        | A Component of this type, when added to a **Manufacturing Order**, will have its ***Quantity Required*** amount set to zero and, if the Product has a [default BOM](https://adempiere.gitbook.io/docs/introduction/products-and-material-management/product-setup/defining-the-product/product-bill-of-materials/..#search-key), all the default BOM Components will be added to the Order at the same level with the original ***Quantity Required***.  This is useful for adding common material and process components to a large number of BOMs while keeping the BOMs rather simple. It also allows the Phantom BOM to be changed independently of all the BOMs that make use of it. |
| Packing        | A Packing component quantity is assumed to be per batch when the component is entered on a Manufacturing Order.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Tools          | A Tools component quantity is assumed to be quantity one per BOM quantity when the component is entered on a Manufacturing Order.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Option         | A component that will be optionally added to an Order Line when the BOM is "dropped" onto an Order, Invoice or Project.  Option components are not allowed on Manufacturing Orders.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Variant        | Similar to the *Option* type but used as a choice of one from several variant Components within a group where the variants share a ***Feature***. Variant components are not allowed on Manufacturing Orders.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## UOM

Select the UOM for the component. This can be any valid UOM for the Component Product.

## Attribute Set Instance

This should default to the Product Attribute Set Instance value if one is defined. This represents a template that will be passed to a Manufacturing Order. It is not possible to add Instance values for Product BOM Components. See [Product Attributes, Attribute Sets and Instances](https://adempiere.gitbook.io/docs/introduction/products-and-material-management/product-setup/product-attributes-sets-and-instances) for more info.

## Change Notice

Select the Change Notice that relates to this Component. This is a link to a change process describing what was changed and why.

## Valid From/To

The ***Valid From*** and ***Valid To*** fields are used to ensure the Component is or will be valid at the time of use. For example, in Manufacturing Orders the dates are tested against the scheduled start date of the manufacturing process before the Component is added to a Manufacturing Order.

## Is Critical Component

A flag that indicates that this component Is Critical. It is not currently used by the Application.

## Is Quantity Percentage

If selected, this indicates that the quantity of the Component will need to be calculated as a percentage of the Quantity Ordered on a Manufacturing Order. When this field is selected, the quantity is entered as a batch quantity percentage. If deselected, the quantity is a quantity per BOM UOM.

## Quantity

The quantity of the component required to create one BOM UOM. This field is shown if the ***Is Quantity Percentage*** field is not selected.

## Quantity in %

The quantity as a percentage of the Batch Quantity on a Manufacturing Order. This field is shown if the ***Is Quantity Percentage*** field is selected.

## Cost Allocation Percent

If the ***Component Type*** is set to *Co-Product***,** this field will appear. It is used to allocate a percentage of the cost of the BOM to the Co-Product. If the field is left blank, the Cost Allocation Percent is calculated based on the quantity of Co-Product produced.

## Scrap %

Indicates the percentage of the quantity that will become scrap as a result of the manufacturing process. The quantity of the Component to order to fulfill the BOM will be calculated as

$$
QtyToOrder = QtyRequired / (1 - Scrap/100)
$$

where *Scrap* is the Scrap % value.

## Quantity Assay

A quantity of the component that will be consumed in tests or assay during the manufacturing process. The value is not currently used.

## Issue Method

There are three methods for issuing products to a Manufacturing Order:

| Issue Method | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Issue        | Indicates that manual material handling processes will be followed to draw material form inventory and provide the component to the manufacturing process.  The component can be issued individually from other components and in partial quantities if necessary.                                                                                                                                                                                                                                                                                                                                                                                     |
| Backflush    | The required quantity of the component will be automatically issued to the manufacturing process with no material handling involved.  Components using the Backflush Issue Method can be grouped using the ***Backflush Group*** field.  This Issue Method is useful where the quantities of the component in stock are high and readily available to the manufacturing process.                                                                                                                                                                                                                                                                       |
| Floor Stock  | The Component will be drawn from Floor Stock with no material handling involved. Floor Stock is an expense account similar to the Product Asset or Inventory account but that represents material that will be consumed in production.  It is used for issue methods such as Kanban where the Kanban locations are filled from inventory and treated as an internal use expense when filled. This "fill" process would remove products from inventory, credit Inventory and debit Floor Stock as an expense.   The *Floor Stock* Issue Method will allocate this expense to the cost of the BOM Product as debit Work-In-Progress, credit Floor Stock. |

## Backflush Group

This field appears if the ***Issue Method*** is set to *Backflush.* It is not currently used.

## Lead Time Offset

An optional field, it is used to identify a Lead Time Offset before starting production. It is not currently used.

## Feature

A string field that appears when the ***Component Type*** is set to *Option* or *Variant* and the ***BOM Type*** is *Product Configure*. The field is used to group similar optional or variant components when performing a BOM Drop or Product Configuration.

## Forecast

A percent number representing the % contribution of this component or variant to planning for the BOM Product. The Forecast field is displayed if the ***BOM Use*** is set to *Planning.*

{% hint style="info" %}
The planning feature using this Forecast field has not been implemented yet.
{% endhint %}

For the purposes of the planning based on a forecast, the BOM Product represents a family of products and the BOM Components are members of that family. The Forecast % is the contribution of each member of the family to the overall demand. For example, if the product family is an automobile with four types based on color, the overall forecast of the demand for the automobile could be broken down as shown in the table below.

| Product           | Forecast (%) |
| ----------------- | ------------ |
| Automobile Green  | 30           |
| Automobile Red    | 15           |
| Automobile Blue   | 10           |
| Automobile Silver | 45           |

The forecast for the Automobile family could be say, 10,000 vehicles. The Material Resource Planning process would generate demand, procurement and Manufacturing Orders for the four Automobile types and their components according to the Forecast percentage of each.


# BOM Drop

How to add the components of a BOM to an Order, Invoice or Project.

Adding the components of a BOM to a document is referred to as "Dropping" the BOM onto the document. This can be performed in two ways:

1. Ensure the parent product is not Stocked. When the parent product is added to an Order, it will be replaced by its components. See the note in the description of the Stocked field in [Basic Product Setup](https://adempiere.gitbook.io/docs/introduction/product-setup/defining-the-product/basic-product-setup#stocked);
2. Use the **BOM Drop** form which can be used to drop any default BOM onto an Order, Invoice or Project.

## BOM Drop Form

The **BOM Drop** form provides more control over which components of the BOM are added to the document and the quantities of each. Used with Optional or Variant components, the form acts as a checklist or menu of components, allowing the user to quickly select which options or variants are added to the document. This is especially helpful where product configuration is common. For example, when buying components to build a computer.

The form is accessed from the **Material Management** menu or from a button/process on an Order, Invoice or Project.

![The BOM Drop form opened from the menu.](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-Lds_dPUW-NWkXppkN3o%2F-Lds_fuOo6Lpb0kc9f7i%2Fwebui_form_bomdropmenu.PNG?generation=1556801307404613\&alt=media)

### Selecting the BOM to Drop

At the top of the form is a selection panel where the parent product can be selected. The panel will show the following fields:

| Field             | Description                                                                                                                                                 |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ***Product***     | The parent product.  The Product must have a default BOM and be Verified.                                                                                   |
| ***Quantity***    | Select an integer quantity of the product to add to the document. The quantities of the BOM components will be adjusted accordingly.                        |
| ***Explode BOM*** | Explode or expand the BOM to include all sub-components, if any.                                                                                            |
| ***Order***       | Select the target Order document.  The documents must be in a draft or "In Progress" state.  This field only appears if the form is opened from the menu.   |
| ***Invoice***     | Select the target Invoice document.  The documents must be in a draft or "In Progress" state.  This field only appears if the form is opened from the menu. |
| ***Project***     | Select the target Project.  This field only appears if the form is opened from the menu.                                                                    |

{% hint style="info" %}
Only one target document can be selected at a time.
{% endhint %}

### Selecting BOM Components

When a Product is selected, the lower panel will show the components of the default BOM for that product. Only [Component Types](https://adempiere.gitbook.io/docs/introduction/product-setup/defining-the-product/product-bill-of-materials/bom-components#component-type) **Component**, **Option,** or **Variant** will be shown. However, if the ***Explode BOM*** checkbox is selected, any component type that represents a BOM will be exploded to the lowest level. For example, a [Phantom](https://adempiere.gitbook.io/docs/introduction/product-setup/defining-the-product/product-bill-of-materials/bom-components#component-type) component type will not appear in the lower panel but its sub-components will if the top level BOM is exploded.

The lower selection panel is a list of the BOM sub-components. **Option** and **Variant** component types will be grouped by the [Feature](https://adempiere.gitbook.io/docs/introduction/product-setup/defining-the-product/product-bill-of-materials/bom-components#feature) to which they belong. There will be one group for each feature name, Component Type and parent product - even if the feature names are the same.

The fields are as follows:

| Field        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Product**  | A check box or radio button selection of the BOM line product. **Component** component types will be selected by default and can't be deselected. They are considered mandatory. Within a feature, only one **Variant** component type can be selected at a time and one must be selected.  The first Variant is selected by default.  **Option** component types are deselected by default and one or more of these components can be selected at a time. |
| **Quantity** | The BOM Line quantity that will be used on the document.  Initially, it is the BOM Line quantity multiplied by the BOM quantity in the upper panel.  It can be adjusted.                                                                                                                                                                                                                                                                                   |
| **UOM**      | The Unit of Measure to use on the document line.  Where conversions exist for the selected component product, the UOM can be changed as required.                                                                                                                                                                                                                                                                                                          |

{% hint style="warning" %}
As the Price List is in the Product's UOM, the quantity and UOM used in the form will be converted to the Product UOM on an Order or Invoice.
{% endhint %}

At the bottom of the form are standard Cancel and Confirm buttons. The Confirm button will be enabled when a Product BOM is selected and, if opened from the Menu, a target document is selected. Clicking Confirm will save the selected components to the document as new lines. Clicking Cancel or closing the form will cancel the BOM Drop.

## Restrictions

### Products must have a Default BOM and be Verified

To appear in the BOM selection panel, the product must have a [Default BOM](https://adempiere.gitbook.io/docs/introduction/product-setup/defining-the-product/product-bill-of-materials#default-bom) and be [Verified](https://adempiere.gitbook.io/docs/introduction/product-setup/defining-the-product/basic-product-setup#bill-of-materials-verify-bom-verified).

### Components Must Exist on the Price List

To drop components into an Order or Invoice, the component products must exist on the price list being used on the document. If not, an error will be displayed. This does not apply to Projects.

### Target Documents must be Draft or In-Progress

Only Draft or In-Progress Orders and Invoices can be target documents. This does not apply to Projects.


# Accounting & Performance Analysis


# An Overview of Accounting in ADempiere

Provides an overview of how the accounting works in ADempiere

Accounting is one of the expected functions of any ERP system.  In ADempiere, the accounting capabilities are at the core of the system, keeping track of the transactions and entries that make up the financial records known as the company books. Like most capabilities in ADempiere, with proper configuration and setup, the user doesn't need to deal with the accounting directly - it all happens automatically.  At the same time the accountants have full control.

ADempiere can manage multiple books in multiple currencies as required to meet the financial reporting requirements in different regions of the world.  Each book is represented by an "Accounting Schema" which defines the currency, behavior and accounts used by the book.  &#x20;

The there can be multiple Charts of Accounts defined in ADempiere as Account Elements.  Each Schema can select which Account Element to use.  In addition, each Schema can add additional "dimensions" of data to the accounts, enabling detailed reporting across these dimensions as required. The dimensions provide a way to categorize the accounting data so that the the number of accounts can be small.  In other words, there is no need to create a large number of accounts, each specific to some combination of these dimensions.

When assigning accounts to use for a particular purpose, a "combination" of these dimensions is used.  The Account Combination defines the account and default dimension values that will be used when posting an accounting fact.  A set of default Account Combinations is defined within the Schema and then the behavior can be customized in each area of accounting as required.  For example, the account combination to use for the accounts receivable of a particular customer can be set uniquely for that customer, for all customers of a group or as the default for all customers.

The generation of accounting facts, the detailed entries in the books, is performed by documents such as invoices, material receipts, bank statements etc.  There is a direct analogy with the equivalent paper document process.  The document has some accounting consequence and provides the source for the accounting facts that are posted in the books.  For this reason, the documents are strictly controlled to prevent changes once they are approved and completed but the accounting facts aren't.  While it is not possible to manipulate the accounting data directly, the accounting data can be "reset" as required and regenerated using the information in the documents.  This makes is possible to correct the accounting if changes in the account combinations are required.  For example, if a particular customer requires a different account for accounts receivable and you need to use this account for all their transactions since the beginning of the fiscal year, then you can change their default account combination and reset the accounting to post the information to the correct account.

With multiple Accounting Schema setup, a single document will post its accounting facts into every Schema defined, using the accounts, currencies and dimensions defined for that Schema.

Manual generation of accounting facts can be done using a General Ledger Journal (GL Journal) entry to provide management estimates and corrections as required.  With proper setup and use of the ADempiere system, the need for manual GL Journal entries is minimized compared to other accounting systems.  Each accounting facts is associated with a document and that document is controlled, providing an audit trail for the accounting results.  This provides a direct relation between the accounting balances and the documents, making the audit process simpler.  To prevent GL Journal entries from affecting this direct relationship, the Accounts can be set as "Document Controlled" to limit the accounting facts to those generated by documents rather than GL Journal entries.  Corrections to these accounts should be done by correcting the documents, not by adjusting the accounting with a GL Journal entry.

Postings to the accounting data can also be controlled by opening and closing calendar periods.  If a period is closed, it won't be possible to post new accounting data or reset the data in that period.  Closing periods is useful to prevent inadvertent changes to the accounting data after an audit or the end-of-period processes is completed.  The period control is actually done at the document level so a period can be closed for, say, invoice posting, but not for the GL Journal.

Finally, detail reporting is possible to summarize the accounting data or delve into it in great detail.  The reporting structure provides ways to report by account or any specific dimension within the schema.


# Accounting Setup

How to setup the accounting system in ADempiere

The process for setting up the accounting system in ADempiere is partially done when the Client is created.  A set of default accounts is required in the Client creation process and these ensure the system will work as soon as the Client is first used.  The setup process modifies these initial defaults so the accounting is tailored to your enterprise.

There are six main steps in the setup:

1. Define the Calendars and periods in each;
2. Create the Account Elements (also called the Chart of Accounts) required;
3. Define the Accounting Schema or books that will be used by the Client;
4. Define the General Ledger categories that will be used in the accounting facts posted to the books;
5. Define the document sequences that will be used to number the various documents; and&#x20;
6. Define the document types specific to the Client.

Each step is covered in the following chapters.


# Calendar, Year and Periods

Setup and control of the Calendar, Year and Periods used by the accounting system

The Calendar, Year and Periods define the date-based grouping of financial data used in the reporting system.  The accounting consequences of a particular document are posted into one Period determined by the Accounting Date used by the document.   The Calendar Year and Periods are common across all Accounting Schema defined.&#x20;

While it is possible to define multiple Calendars, only one is used at a time.  The ***Client*** window, ***Client Info*** tab selects which Calendar will be used.  If the selected Calendar is changed, it will affect any subsequent accounting postings, not the currently posted data.  To change the currently posted data, the accounting data should be reset.

## Calendar

The Calendar setup is straight forward.  An initial Calendar will have been created for the Client and this can be modified or a new one defined.


# Tax Setup

How to design the taxes in ADempiere

Before entering documents that have tax consequences, the taxes must be created.

Taxes can be complex, with different accounting requirements, calculations and reporting requirements. The tax can vary by product and by the geographical location of the seller, or buyer. In the ADempiere tax model, the tax to use on a document is selected based on a tax category. The tax category is assigned to products and charges and must contain at least one summary or parent tax definition. Subordinate taxes determine the details and actual accounting consequences based on the situation and geography. For really difficult and unruly tax situations, a software or script rule can be created to determine what tax to apply.

{% hint style="info" %}
There is a Tax Setup workflow defined in ADempiere but since you have not setup the products yet, you can skip most of it. Follow the window sequence below instead.
{% endhint %}

## Examples

Before getting into the details, consider a few examples.

### Canada

In Canada, the sales tax varies by province. There is typically a Provincial Sales Tax (PST) which is different in each province, and a common national Goods and Services Tax (GST). Certain provinces combine these into a Harmonized Sales Tax (HST) but there are still products where only the GST or PST portion of the HST applies. GST/HST is a pass through tax meaning that it is tracked as a liability or receivable based on the sales or purchase transactions. The PST is an end-user tax meaning its a liability on a sale but an expense on a purchase.

### EU and VAT

The rules in the EU are complex. A primer can be found on the [VAT](http://wiki.adempiere.net/VAT) page. The page also contains lots of examples. Many of the countries use a graded tax scheme based on the type of product. For example, in Sweden there are four different VAT categories on sold goods and services. These are:

* **Full Rate** - 25%
* **Half Rate** - 12%
* **Low Rate** - 6%
* **No VAT** - 0%

Different products and services belong to these different categories.

## Setup Taxes

Tax setup uses windows found in the menu under **Performance Analysis » Accounting Rules**

### **Tax Category**

The [**Tax Category Window**](http://wiki.adempiere.net/ManPageW_TaxCategory) is used to enter and maintain Tax Categories. Each and every product or charge is associated with a tax category which determines how taxes will be applied to the product. This is where the major differences in taxes applied to various products are defined. Set up the categories to identify the high level differences. Regional differences will be handled in other windows. A good selection of Tax Categories in Canada would be:

* **No Tax** - no tax applied to the document. Tax is not applicable to the transaction.
* **Exempt** - the product or service is exempt from tax. This has special consequences for input tax credits and the accountants will want to track it. The Government determines which products and services are exempt.
* **Zero-Rated** - the product of service is considered tax free without the special consequences. Again, the Government determines where this applies.
* **PST Only** - the product only has Provincial Salse Tax (PST) applied.
* **GST only** - the product only has GST applied.
* **PST/GST** - the product can have both PST and GST applied.
* **HST** - the product has HST applied.

### Tax Rate

The [**Tax Rate Window**](http://wiki.adempiere.net/ManPageW_TaxRate) defines the different taxes used for each tax category. For example Sales Tax must be defined for each State in which it applies. If you have multiple taxes falling in a single category, create a summary level tax with the approximate total tax rate. Then create the subordinate tax rates and assign the the summary level tax as their parent.

| [![Image:Note.gif](http://wiki.adempiere.net/images/6/62/Note.gif)](http://wiki.adempiere.net/File:Note.gif) | <p><strong>Note:</strong></p><p>Every tax rate requires a parent or summary tax. When entering the order or invoice lines the tax is first estimated using the summary tax rate. The correct tax is calculated when the document is prepared or completed. With many possible rates for a tax category, be aware that estimation can be wrong and that the order/invoice grand total shouldn't be trusted until the document is prepared.</p> |
| ------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

The tax is always calculated from the line net amount. For taxes that include multiple taxes in the base amount, you will have to calculate the net effect and adjust the individual tax rates accordingly. For example, ADempiere calculates the line total tax for two subordinate taxes as

$$
TT = LNA\*(Tax1 + Tax2)
$$

where TT is the Total Tax. Tax1 and Tax2 are the subordinate rates and LNA is the line net amount. If you need the calculation where Tax2 is based on the Tax1 amount as in

$$
TT = LNA*Tax1 + (LNA*Tax1)\*Tax2
$$

you will have to adjust the Tax2 rate to equal Tax1\*Tax2. Similarly, if the equation was

$$
TT = LNA*Tax1 + LNA*(1+Tax1)\*Tax2
$$

the adjusted Tax2 rate would be (1+Tax1)\*Tax2. For more complex cases, you may need to define custom rules to calculate the tax.

#### Dealing with Regional Differences

The tax rates are defined regionally as there can be major differences. The "Billing From" and "Shipping To" location information determines the match with the Country and Regions on the Tax Rate and which tax to apply. In other words, if HST only applies to sales billed in Canada and shipped to customers located in Canada, the HST Tax Rate has the From and To countries set to Canada. HST will not be applied to sales billed in Canada and shipped to customers in the USA. The granularity of the regional definitions can be extended from countries and regions to ZIP codes. Leaving the country or regions fields blank means the tax rate will apply in all countries or regions.

{% hint style="info" %}
A corollary rule is that every business partner needs to have a bill from and ship to location defined, as does every warehouse that receives goods. If not, there will be errors.
{% endhint %}

#### Exempt Tax Rates

You can define tax rates as "SO Exempt". If a business partner is flagged as Tax Exempt, the software will find the the first tax rate marked as SO Exempt with the lowest actual rate - not necessarily zero, just the lowest rate. In the simplest case, define a single tax rate as SO Exempt with the rate set to 0%.

#### How Tax Rates are Selected

There is no restriction on the number of tax rates assigned to a category so it is possible to have many to choose from. The software decides which tax rate to apply by simply picking the first summary tax rate it finds that can be applied. It is not possible to force the order of the search except that summary tax rates with no country or region defined will be tested first.

The Valid From date field will only limit new taxes which will come into effect. The date is compared to the billing date. There is no way to define a date to stop applying a tax. For that, you have to manually mark the rate as inactive. For special cases, a software or script rule can be defined to determine what amount of tax to apply.

#### Tax Rate Accounting

On the Accounting Tab, you can define the accounting for each tax rate. There are five accounts:

| Account         | Description                                               |
| --------------- | --------------------------------------------------------- |
| Tax Due         | The account for taxes owed and payable                    |
| Tax Credit      | The account for taxes expected to be refunded or received |
| Tax Expense     | The account for paid taxes that can't be reclaimed        |
| Tax Liability   | The account for tax declaration liability                 |
| Tax Receivables | The account for tax credit after tax declaration          |

### Global Tax Management

There are a few other windows that you can use to define tax related information. The information in these windows is not used by ADempiere but is available for use by any rules or scripts you may need to develop. Find them in the menu under **Performance Analysis » Accounting Rules » Global Tax Management**:

* [**Tax Rate Parent Window**](http://wiki.adempiere.net/index.php?title=ManPageW_TaxRateParent\&action=edit\&redlink=1) - The Tax Rate Parent Window defines the different subordinate taxes used for each tax category. It is essentially similar to the Tax Rate windows but shows the child taxes in an included tab.
* [**Tax Group Window**](http://wiki.adempiere.net/index.php?title=ManPageW_TaxGroup\&action=edit\&redlink=1) - allows you to group the business partner with a reference tax.
* [**Tax Type Window**](http://wiki.adempiere.net/index.php?title=ManPageW_TaxType\&action=edit\&redlink=1) - another method to group taxes together.
* [**Tax Base Window**](http://wiki.adempiere.net/index.php?title=ManPageW_TaxBase\&action=edit\&redlink=1) - defines the tax base as the product price, quantity, cost or weight.
* [**TaxDefinition Window**](http://wiki.adempiere.net/index.php?title=ManPageW_TaxDefinition\&action=edit\&redlink=1) - You can use the tax definition information to create the logic necessary to get the tax rate to your document.


# Performance Measurement Setup


# Assets and Asset Management

This section is an overview of the Asset Management within ADempiere. For background on the terms used, please see Accounting of Assets.

## Overview

This section is an overview of the Asset Management within ADempiere. For background on the terms used, please see [Accounting of Assets](http://wiki.adempiere.net/Accounting_of_Assets).

The basic approach to assets in ADempiere is that they are specialized products which are amortized over time using a monthly or period process which performs all the necessary calculations. This ensures that all assets are depreciated properly and consistently and takes much of the effort out of depreciation calculations.

### Defining Assets

Essentially, assets are products and are treated like products in every sense.

Asset related products are bought and sold just like the services or other items but the accounting is managed differently so that the cost of the asset product is capitalized rather then expensed. The accounting of the assets is controlled by the Asset Group for the capital portion and by the Product Category for the product expenses and revenue. These two windows are the starting point for managing assets in ADempiere.

#### Asset Groups

The Product Category and Asset Group are linked on the Product Category page, so the **Assets** [**Asset Groups Window**](http://wiki.adempiere.net/index.php?title=ManPageW_Asset_Groups\&action=edit\&redlink=1) is the first window to use when defining assets. Each Asset Group defines specific accounting elements to use so the groups should be set up according to the asset reporting structure in the corporate financial statements. For example, in the GardenWorld demo, the financial statements report on the assets using the following categories:

* 16 Land and Building
  * 16100 Land
  * 16200 Building
  * 16300 Land Improvements
  * 16400 Building Improvements
  * 16500 Leasehold Improvements
* 17 Furniture, Fixtures & Equipment
  * 17100 Furniture
  * 17200 Fixtures
  * 17300 Equipment
  * 17400 Vehicles
  * 17500 Data Processing Equipment
  * 17600 Software

The Asset Groups are set up in a similar way:

* Buildings
* Furniture
* Fixtures
* Equipment
* Vehicles
* Data Processing Equipment
* Software

Each group relates to a specific set of accounts that are used for the asset accounting for any asset that is part of that group. Again, in the Garden World demo, the accounts for the Buildings Asset Group are:

* Asset Acct HQ-16200-\_-\_-\_-\_
* Accumulated Depreciation Account HQ-18120-\_-\_-\_-\_
* Depreciation Account HQ-67120-\_-\_-\_-\_
* Disposal Revenue Acct HQ-79200-\_-\_-\_-\_
* Disposal Gain Acct HQ-80800-\_-\_-\_-\_
* Disposal Loss Acct HQ-82800-\_-\_-\_-\_

These accounts should be straight forward for most people familiar with a balance sheet with the exception of the Disposal Revenue Account. This account is debited with the proceeds of the disposal of the asset which would normally be a cash account. However, as the sale of the asset will likely involve invoicing and accounts receivable, the Disposal Revenue account should point at a clearing account that will be balanced by the invoice Product Revenue account. For this reason, the Asset Group Disposal Revenue account and Product Category Product Revenue account should be the same clearing account.

The Asset Group also defines the type for depreciation processing to use and the life of assets that are part of the Group. The Building Asset Group defines the depreciation function as [Straight Line](http://wiki.adempiere.net/Accounting_of_Assets#Straight_Line_Method) and the Usable Life as 10 years or 120 periods/months. This means that 10% of the depreciable value of the asset will be expensed as depreciation in each year.

There are a number of possible depreciation functions to choose from that match the most common depreciation schemes in use around the world.

The other key element that can be set in the Asset Group is the Accounting Schema. This allows the accounts and depreciation methods to change from one Schema to another where multiple schema are in use. For example, an accelerated depreciation scheme could be used in one Schema for tax purposes and a basic straight line scheme in another for regulatory reporting.

#### Product Categories

After defining Asset Groups, the Asset Groups need to be matched to Product Categories. When an asset is defined, it is defined using a product and Asset Group. The Product Category used in the definition of the product has to be linked to the Asset Group or it won't be possible to save the Asset record.

| [![Image:Note.gif](http://wiki.adempiere.net/images/6/62/Note.gif)](http://wiki.adempiere.net/File:Note.gif) | <p><strong>Note:</strong></p><p>Create a summary product category for all assets and use this as the parent product category for the asset related product categories. Then in the Product Info window, you will be able to search for all asset related products using the summary category or for specific product assets using the detail categories.</p> |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

The **Material Management>Material Management Rules** [**Product Category Window**](http://wiki.adempiere.net/ManPageW_ProductCategory) performs the same function as the Asset Group in that it defines the accounting for product transactions. The key items here are:

* The Parent Product Category - point to the summary category if following that approach.
* The Asset Group - select the matching asset group.

On the Accounting tab, set the accounts as follows:

* The Product Expense account which is used when the asset is first added to the books using the [#Asset Addition](http://wiki.adempiere.net/Assets_and_Asset_Management#Asset_Addition) process. This account will be charged the equivalent of the net book value of the asset. If moving from asset accounting using a GL, the product expense account could be pointed at a clearing account and a final GL entry could be made to remove the original assets and accumulated depreciation values to balance the clearing account after the asset has been added using the process. If the asset is first managed through the inventory as a purchase of a product, the Product Asset account will be used by the Material Receipt (unless the product is identified as a "Service" product type - in which case the value will be assigned to the Work In Progress account, if there is a cost collector defined, or the Product Expense account otherwise). It is recommended that the Product Expense and Product Asset accounts be pointed at the same account.
* The Product Revenue account will be credited on the sale of the asset, assuming an AR invoice is used to make the sale. The invoice line net amount will be considered as the proceeds of the sale. The sale invoice will trigger an [#Asset Disposal](http://wiki.adempiere.net/Assets_and_Asset_Management#Asset_Disposal) transaction which will debit the Disposal Revenue Account from the Asset Group with the same amount. In most cases the Product Revenue account and Asset Group Disposal Revenue Account should be set to the same account as the net balance should be zero.
* The Product Asset account should point to the same account as the Product Expense Account for the reasons described above.

In the Garden World demo, the Product Category Accounts for the Building Product Category are set up to point at the suspense balancing account:

* Product Asset HQ-79200-\_-\_-\_-\_
* Product Revenue HQ-79200-\_-\_-\_-\_
* Product Expense HQ-79200-\_-\_-\_-\_

#### Defining the Asset Product

Asset products are defined as if they were regular products in the **Material Management>Material Management Rules** [**Product Window**](http://wiki.adempiere.net/ManPageW_Product). The Product Category should be one that was linked with an associated Asset Group. The product should be stocked if it is at all tangible as the value of the asset will be easier to manage through the acquisition and disposal processes. For assets that are tracked by serial numbers, an appropriate Attribute Set should be defined. Also, if the asset product is unique, a specific Attribute Set Instance can be created with a serial number and set on the Product tab.

Next (optionally) create the Asset product using the **Assets** [**Asset Window**](http://wiki.adempiere.net/ManPageW_Asset). Give the asset a suitable name and select the matching Asset Group and Product Category. If these are not properly linked on the Product Category, an error will be displayed when you try to save the record. This step is optional because it can be performed automatically by the invoice. Creating the record manually does give more control over the dates.

Set the Create Date to the day the asset was created in the system and set the In Service Date to the day where depreciation will start to apply.

Select "Owned" if the asset is owned by the client organization and considered a capital asset. If the asset is owned, it can also be selected as subject to depreciation.

When the Asset record is saved, the definitions are ready to be used but no accounting has taken place yet. The value of the asset has not been defined and there are no entries in the Accounting Facts.

### Adding Assets

There are two ways to add assets to the balance sheet:

* Manually, using the **Assets>Asset Transactions** [**Asset Addition Window**](http://wiki.adempiere.net/index.php?title=ManPageW_AssetAddition\&action=edit\&redlink=1)
* Via a Vendor Invoice.

#### Adding Assets with an Invoice

Assets are added when the invoice line has the "Create Asset" button selected and the asset type is identified as a "Capital" asset. If the product is one of many under a single Asset, select the check box "Is Collective Asset" and select the associated Asset.

If an asset is not identified on the line, one will be created from the connection between the Product Category and the Asset Group. The addition of the asset to the books is performed when the Match Invoice record is created following the receipt of the Asset Product. The addition is performed by an Asset Addition document which creates the necessary postings to add the asset to the books.

As an example of the invoice, consider the following scenario:

In the Garden World example, the Fertilizer organization has an Equipment Shed, a large fabric covered structure roughly 450 square meters in size. The shed was purchased about a year ago for $175,000 in a turnkey fashion so all expenses required to make the asset ready for sale were included in that price. The Equipment Shed is owned and will be depreciated according to the "Building" Asset Group settings of a 10 year life using the Straight Line method. For this asset, there is a Product "Equipment Shed" and a Asset "Fertilizer Equipment Storage Shed". The invoice date and asset creation date are about 2 months ahead of the activation date.

For this example, the asset record was created before the invoice. A standard invoice header record was created. The date of the invoice will become the document date of the Asset Addition document. A single invoice line was added as follows:

* The product set to "Equipment Shed"
* "Create Asset" selected
* Asset Type (Capital/Expense) set to Capital
* Asset set to the asset product completed above "Fertilizer Equipment Storage Shed"
* Is Collective Asset deselected
* Qty set to One
* Price set to $175,000

When the invoice was completed, the posting is as follows:

| Account            | Debit    | Credit   |
| ------------------ | -------- | -------- |
| Tax                | $22,750  |          |
| Inventory Clearing | $175,000 |          |
| Accounts Payable   |          | $197,750 |

The material receipt of the asset was accomplished with a standard Material Receipt, adding the "building" to the inventory of the Fertilizer organization. The posting on the MR was as follows:

| Account               | Debit    | Credit   |
| --------------------- | -------- | -------- |
| Suspense Balancing    | $175,000 |          |
| Not invoiced receipts |          | $175,000 |

The Matching Invoice record had the following facts:

| Account               | Debit    | Credit   |
| --------------------- | -------- | -------- |
| Not invoiced receipts | $175,000 |          |
| Inventory Clearing    |          | $175,000 |

If the Asset record was not identified on the Invoice Line, the Asset record would have been created based on the Product Category and Asset Group information.

When the Match Inv was created, an Asset Addition record was also created. In addition to the Asset Addition document, a worksheet is created containing all the expected depreciation expenses over the life of the asset and the current asset balances are established.

The accounting fact posting of the Asset Addition are as follows:

| Account            | Debit    | Credit   |
| ------------------ | -------- | -------- |
| Building           | $175,000 |          |
| Suspense Balancing |          | $175,000 |

The net effect of all the postings, removing the cancelling entries, is:

| Account          | Debit    | Credit   |
| ---------------- | -------- | -------- |
| Tax              | $22,750  |          |
| Building         | $175,000 |          |
| Accounts Payable |          | $197,750 |

#### Adding Assets Manually

To add an asset to the books manually, without any invoice, simple create the Asset record and then the Asset Addition document and Complete it.

When adding assets in this manner, there are a few additional options to consider.

* The starting values of the capital asset and accumulated depreciation can be set on the Asset Addition record. When using an invoice, the capital asset value is the purchase price and accumulated depreciation is considered zero. To make this adjustment select the checkbox "Adjust Accumulate Depreciation", then fill in the starting values for the accumulated depreciation and set the starting period. The asset depreciation workbook will start at that period and calculate the depreciation to the end of life.
* The quantity of assets can be set to a number other than one. This is useful if a number of items are grouped as a single "asset" but added and disposed of individually or in smaller sets. This is known as a "Collective Asset".

After completing and posting the Asset Addition Document, the undepreciated value of the asset will be posted to the Product Expense account. A General Journal entry may be required to deal with this expense - for example, to reduce an existing asset and accumulated depreciation amounts.

### Depreciating Assets

The automatic depreciation calculations possible in ADempiere make the periodic depreciation calculations and reporting quite simple - almost a button push effort. This is a great time and accuracy savings for those who traditionally handled depreciation calculations on a spreadsheet. The basic process is as follows:

* Open the **Assets> Depreciation Processing** menu, [**Post Depreciation Entry Window**](http://wiki.adempiere.net/index.php?title=ManPageW_PostDepreciationEntry\&action=edit\&redlink=1).
* Enter the values for the following fields:
  * Organization
  * Document Type - there is only one choice "Asset Depreciation"
  * Posting Type
  * Accounting Schema
  * Document Date/Accounting Date
  * Period
* Save the record.

At this point, you can check the "Records" tab that will show the depreciation expense entries that will be applied that were drawn from all the available asset depreciation workbooks created when the assets were added to the system. If you change any of the values on the header Entry tab, the list of expense records will change.

When satisfied, complete the Depreciation Entry document. When posted, this will debit the depreciation expense account and credit the accumulated depreciation account according to each line in the "Records" tab.

### Disposing of Assets

#### Asset Disposal


# Manufacturing


# Engineering Change Management


# Product Configuration


# Forecasting

Establishing and maintaining production forecasts which can be used for decision making.

## Overview

Forecasting is a way to estimate the future quantity and revenue from sales of products or services over a period of time.  Forecasts use quantitative and statistical methods based on historical data and market statistics to predict future sales.

The projected quantities and sales amounts can be used for decision making, pricing, cash flow, estimated future demand, calculating master production schedule, supply plan and future capacity requirements.

A forecast is basically a set of products, quantities and time that shows how much of a particular product will be required or sold at that time.  The forecast data is used by the Material Resource Planning to drive the material planning processes which will trigger purchase demands for raw material and production activity to generate the required products in time to meet the forecast.

Forecasts have several basic components that are discussed in detail below:

1. An **Operational Calendar** which defines the number and duration of the periods that will be used for the forecast.  The periods are forecast buckets or measurement cycles which can be, for example, weekly or monthly periods.
2. The **sales history** on which the forecast is based.
3. A set of **Forecast Rules** which are the various mathematical and statistical processes that can be applied.  Additional rules can be added in software if required.
4. A **Forecast Definition** which defines the parameters required by the Forecast Rules and filters on the historical data.
5. **Simulations** of the forecast which use all the above to calculate forecast amounts.
6. The **accepted forecast** which is generated from the simulations and which can be used in Material Resource Planning to generate demands on the production system.

## Operational Calendar

The operation calendars defined the set of periods that will be used in the forecast calculations and reports.  These periods are like buckets or measurement cycles with a specific duration.   &#x20;

For planning purposes, the choice of period size depends on your manufacturing and sales turnover time.  Typically, the periods will be weekly or monthly.  Too small periods can result in excessive data that is difficult to deal with.  Periods that are too large can generate manufacturing plans that are not efficient resulting in excessive inventory.  You can create multiple calendars to test which approach works best for your situation.

To define the Operational Calendar open the **Operational Calendar** window in the **Manufacturing Management -> Planning Management -> Forecast Management** menu.&#x20;

![Operational Calendar window](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-M-Q1fcK_PqpA8V23JwS%2F-M-QAK1jGioLLRerSKss%2Fwebui_forecast_operationalCalendar.png?alt=media\&token=60a1f11f-1681-4104-853a-1a3122f4f0db)

Create a new record and give it a name and description. Save the record and move to the **Period Definition** tab.

### Period Definition

The **Period Definition** tab, provides a way to create periods to use in the Forecast. &#x20;

![Operational Calendar window, Period Definition tab](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-M-tWDFXS7yTgn4eagf0%2F-M-tjxjwsm7sj0Mqxl3e%2Fwebui_forecast_operationalCalendar_PeriodDefinition.png?alt=media\&token=c30794cf-bf99-4565-b244-64beeccdf8a9)

The main fields here are:

| Field             | Description                                                                                                                                                                                                                                                        |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ***Name***        | A name for the period definition record.  As you may have several period definitions for a single calendar, the name is used to identify them.                                                                                                                     |
| ***Description*** | A description of the period definition if required and helpful.                                                                                                                                                                                                    |
| ***Year***        | The Calendar Year that the periods will start in.  This only applies if a ***Start Date*** is not set in the **Create Periods** process discussed below.  If a ***Start Date*** is specified, the "year" used will be the year of that date instead of this field. |

{% hint style="warning" %}
At the time of writing, the ***Start Date*** parameter is mandatory, making the ***Year**&#x20;*&#x20;field irrelevant. See issue [#3013](https://github.com/adempiere/adempiere/issues/3013).
{% endhint %}

#### Creating the Periods

With the Period Definition record completed, the periods are created by clicking the button ***Create Periods*** below the ***Year***  field in the **Period Definition** tab. &#x20;

![Create Periods process dialog](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-M-vHR6bwnV8gjxavhNw%2F-M-vJlSa4TVkYq4DYfbw%2Fwebui_forecast_operationalCalendar_PeriodDefinition_CreatePeriods.png?alt=media\&token=676aa8e7-6d1c-4535-8673-1f83d2aa88b7)

The parameters for the process are as follows:

| Parameter               | Description                                                                                                                                                                          |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ***Start Date***        | The start date for the periods.                                                                                                                                                      |
| ***Number of Periods*** | 12 or 52 are allowed, providing monthly or weekly periods.                                                                                                                           |
| ***Date Format***       | The period name will follow the date format entered here.  This uses the Java [SimpleDateFormat](https://docs.oracle.com/javase/9/docs/api/java/text/SimpleDateFormat.html) pattern. |

The Periods begin on the start date specified.  The format pattern should be enough to differentiate the period.  For example, a common format for months would be "yyyy-MM" which would create periods that can be sorted in chronological order by year and month.  For weeks, you might use "yyyy-MM-DD' ('w')'" which would give the start date of each week period and the week number in brackets.

{% hint style="warning" %}
If you run the Create Periods process multiple times, it will create multiple versions of the periods.  While you can use this to generate periods over multiple years, you can also duplicate periods within the year if you are not careful.  If you do need to redo the Create Periods process, please delete the existing periods first. See issue [#3014](https://github.com/adempiere/adempiere/issues/3014).
{% endhint %}

### Periods

The periods created by the process are listed in the **Periods** tab which is embedded in the **Period Definition** tab.  Each period has a name, period number, start date and end date, which set the date range for the specified period.  You can manually manipulate the periods if required.

## Sales History

The forecasts are created by extrapolating a historical trend.  This trend is defined either by the sales contained in historical invoices or directly from an import of data.  The sales history provides the statistical data required to generate a forecast.

### Generating Sales History from Invoices

Not every invoice is relevant when it comes to forecasting so the process of creating the history is selective and only copies relevant information from the invoices into the sales history.

The filters used to select the relevant invoices include:&#x20;

* business partner;&#x20;
* business partner group;
* business partner location;
* product category;
* product classification;
* product class;
* product group;
* Product
* warehouse;
* sales region;
* project; and more

To generate the sales history, run the **Generate Sales History** process found  in the **Manufacturing Management -> Planning Management -> Forecast Management** menu.

![Generate Sales History process parameters](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-M0hTtrlePX5JTAdtL3i%2F-M0j-DPOdztoXVuXcgWS%2Fwebui_forecast_generateSalesHistory.png?alt=media\&token=91877c8f-c406-4b38-87e8-6d6df26aa011)

As you can see in the image, there are a large number of parameters. Only the ***Date Invoiced*** range is mandatory.&#x20;

### Importing Sales History

When ADempiere does not hold enough data to provide its own sales history, there is the possibility of importing data from other sources, such as a legacy system.  The import is performed using the standard [Data Import](https://adempiere.gitbook.io/docs/introduction/system-administration/data/data-import) processes.  The import can be used to provide the sales statistics necessary to perform the forecast.

There is an **Import Sales History** import format that can be used or modified to suit your needs.  At a minimum, the sales history needs to know the qty invoiced, the invoiced date, the warehouse that the products were shipped from and the business partner who was invoiced.  The sales history can provide much richer data than that though including business partner data, prices, costs and reference values.

The historical sales information is used to realize the forecast calculus and to get sales statistics reports.

## Forecasting Rules

The Forecasting Rules define the mathematical and statistical methods that are available to calculate the forecast given a set of Sales History data.  These rules are used in the Forecast Definition to define how the forecast will be calculated. There are nine rules provided in the core application but it is possible to extend these with others by providing the appropriate software classes.  The rules are described in detail in [Engineering Statistics Handbook, 6.4 Introduction to Time Series Analysis](https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc4.htm) by Author Steven R. Gould.  The summaries below are taken from this reference.

In the **Forecast Definition** window, the Simulation parameters can be entered.  How these parameters apply to the Rules depends on the rule. &#x20;

### Moving Average

| Uses Parameter ... | To ...                                                                                                                                                                                                                                                               |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ***User Factor***  | Define the number of periods to average.  For example, if the sales history data is using weeks and a 10-week moving average is required, set the ***User Factor*** to 10.  This also determines the maximum number of periods that can be forecast into the future. |

A moving average forecast model is based on an artificially constructed time series in which the value for a given time period is replaced by the mean of that value and the values for some number of preceding and succeeding time periods. As you may have guessed from the description, this model is best suited to time-series data; i.e. data that changes over time.  For example, many charts of individual stocks on the stock market show 20, 50, 100 or 200 day moving averages as a way to show trends.

&#x20;Since the forecast value for any given period is an average of the previous periods, then the forecast will always appear to "lag" behind either increases or decreases in the observed (dependent) values.  For example, if a data series has a noticeable upward trend then a moving average forecast will generally provide an underestimate of the values of the dependent variable.

&#x20;The moving average method has an advantage over other forecasting models in that it does smooth out peaks and troughs (or valleys) in a set of observations. However, it also has several disadvantages.  In particular this model does not produce an actual equation. Therefore, it is not all that useful as a medium-long range forecasting tool. It can only reliably be used to forecast one or two periods into the future.

&#x20;The moving average model is a special case of the more general weighted moving average. In the simple moving average, all weights are equal.&#x20;

### Simple Exponential Smoothing

| Uses Parameter ... | To ...                                                                                                                                          |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| ***Factor Alpha*** | Define the smoothing constant. This is a value from 0.0 to 1.0. The higher the number, the faster the dampening or weight given to recent data. |

Simple (or single) exponential smoothing is a very popular model used to produce a smoothed time series. Whereas in simple Moving Average models the past observations are weighted equally, Exponential Smoothing assigns exponentially decreasing weights as the observations get older.

In other words, recent observations are given relatively more weight in forecasting than the older observations.

In the case of moving averages, the weights assigned to the observations are the same and are equal to 1/N. In simple exponential smoothing, however, a "smoothing parameter" - or "smoothing constant" - is used to determine the weights assigned to the observations.

This simple exponential smoothing model begins by setting the forecast for the second period equal to the observation of the first period. Note that there are ways of initializing the model. As of the time of writing, these alternatives are not available in this implementation. Future implementations of this model may offer these options.

#### Choosing a Smoothing Constant

The Single Exponential Smoothing rule uses the ***Factor Alpha*** as the Smoothing Constant.

The smoothing constant must be a value in the range 0.0-1.0. But, what is the "best" value to use for the smoothing constant? This depends on the data series being modeled. The speed at which the older responses are dampened (smoothed) is a function of the value of the smoothing constant. When this smoothing constant is close to 1.0, dampening is quick - more weight is given to recent observations - and when it is close to 0.0, dampening is slow - and relatively less weight is given to recent observations.

The best value for the smoothing constant is the one that results in the smallest mean of the squared errors (or other similar accuracy indicator).  There are numerical methods for determining this value but these would have to be applied outside of ADempiere.

### Double Exponential Smoothing

| Uses Parameter ... | To ...                                                                                                                                         |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| ***Factor Alpha*** | Define the smoothing constant. This is a value from 0.0 to 1.0. The higher the number, the faster the dampening or weight given to data.       |
| ***Factor Gamma*** | Define the trend smoothing constant. This is a value from 0.0 to 1.0. The higher the number, the faster the dampening or weight given to data. |

Double exponential smoothing - also known as Holt exponential smoothing - is a refinement of the popular single exponential smoothing model but adds another component which takes into account any trend in the data. Simple exponential smoothing models work best with data where there are no trend or seasonality components to the data. When the data exhibits either an increasing or decreasing trend over time, simple exponential smoothing forecasts tend to lag behind observations. Double exponential smoothing is designed to address this type of data series by taking into account any trend in the data.

Note that double exponential smoothing still does not address seasonality. For better exponentially smoothed forecasts using data where there is expected or known to be seasonal variation in the data, use triple exponential smoothing.

As with simple exponential smoothing, in double exponential smoothing models past observations are given exponentially smaller weights as the observations get older. In other words, recent observations are given relatively more weight in forecasting than the older observations.&#x20;

Double Exponential Smoothing uses ***Factor Alpha*** and ***Factor Gamma*** as the smoothing factors.  Factor Alpha smooths the base data and Factor Gamma smooths the trend.

### Triple Exponential Smoothing

| Uses Parameter ... | To ...                                                                                                                                                                                                                                                           |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ***Factor Alpha*** | Specify the tolerance of the alpha (base data) smoothing factor.  The smoothing factor is a number from 0.0 to 1.0 so the tolerance would need to be a much smaller number.  The smaller the number, the more calculations may be required to find the best fit. |
| ***Factor Beta***  | Specify the tolerance of the beta (trend data) smoothing factor.  The smoothing factor is a number from 0.0 to 1.0 so the tolerance would need to be a much smaller number.  The smaller the number, the more calculations may be required to find the best fit. |

Triple exponential smoothing - also known as the Winters method - is a refinement of the popular double exponential smoothing model but adds another component which takes into account any seasonality - or periodicity in the data.

Simple exponential smoothing models work best with data where there are no trend or seasonality components to the data. When the data exhibits either an increasing or decreasing trend over time, simple exponential smoothing forecasts tend to lag behind observations. Double exponential smoothing is designed to address this type of data series by taking into account any trend in the data. However, neither of these exponential smoothing models address any seasonality in the data.

For better exponentially smoothed forecasts of data where there is expected or known to be seasonal variation in the data, use triple exponential smoothing.

As with simple exponential smoothing, in triple exponential smoothing models past observations are given exponentially smaller weights as the observations get older. In other words, recent observations are given relatively more weight in forecasting than the older observations. &#x20;

At least two complete cycles (years) of data are required to initialize the model. For best results, more data is recommended - ideally a minimum of 4 or 5 complete cycles. This gives the model a chance to better adapt to the data, instead of relying on getting - guessing - good estimates for the initial conditions.

The parameters for the triple exponential smoothing algorithm are determined using a best-fit Mean Square Error (MSE) approach.  As a result, only the tolerances for the alpha and beta smoothing parameters are required.

### Polynomial Regression

{% hint style="info" %}
The implementation of the Polynomial Regression algorithm does not take any parameters.
{% endhint %}

This rule implements a single variable polynomial regression model using the variable named in the constructor as the independent variable. The coefficients of the regression as well as the accuracy indicators are determined from the data set used in the initialization. &#x20;

A single variable polynomial regression model essentially attempts to put a polynomial line - a curve if you prefer - through the data points. Mathematically, assuming the independent variable is x and the dependent variable is y, then this line can be represented as:

$$
y = a0 + a1*x + a2*x^2 + a3*x^3 + ... + am*x^m
$$

The default for the order $$m$$ is 10  but the order is reduced to the square root of the number of data points if there are less than 100 data points.

### Regression

{% hint style="info" %}
The implementation of the Regression algorithm does not take any parameters.
{% endhint %}

This model implements a single variable linear regression. The coefficients of the regression - the intercept and the slope - as well as the accuracy indicators are determined from the sales history and are applied to the forecast.

A single variable linear regression model essentially attempts to put a straight line through the data points. For the more mathematically inclined, this line is defined by its gradient or slope, and the point at which it intercepts the x-axis (i.e. where the independent variable has, perhaps only theoretically, a value of zero). Mathematically, assuming the independent variable is x and the dependent variable is y, then this line can be represented as: &#x20;

$$
y = intercept + slope \* x
$$

### Multiple Linear Regression

{% hint style="info" %}
The implementation of the Multiple Linear Regression algorithm does not take any parameters.
{% endhint %}

This model implements multiple variable linear regression but with only one independent variable, time.  So in effect, it is no different than the Linear Regression model.

It might be interesting to use this model to forecast demand given time and say price but the current implementation will not allow that.

### Naive Forecasting

{% hint style="info" %}
The implementation of the Naive Forecasting does not take any parameters.
{% endhint %}

A naive forecasting model is a special case of the moving average forecasting model where the number of periods used for smoothing is 1. Therefore, the forecast for a period, t, is simply the observed value for the previous period, t-1.

Due to the simplistic nature of the naive forecasting model, it can only be used to forecast up to one period in the future. It is not at all useful as a medium-long range forecasting tool.

This really is a simplistic model, and is included partly for completeness and partly because of its simplicity. It is unlikely that you'll want to use this model directly. Instead, consider using either the moving average model, or the more general weighted moving average model with a higher (i.e. greater than 1) number of periods, and possibly a different set of weights.

## Forecast Definition

The **Forecast Definition** window provides a way to manipulate the creation of the forecast by focusing on sets of specific information.  Essentially, the complete forecast can be treated as a number of very focused forecasts, each looking at different data and using different parameters to forecast that data. &#x20;

The Forecast Definition includes a header, which has the standard identifying fields and an embedded tab for the **Forecast Definition Lines**.

This window allows to define the valid combinations, used to select the historic sales records. The combinations order is determined by the sequence, where the lower sequence has priority over the higher sequence.

The information to define combinations are defined by business partner data (business partner, business partner group, sales region and campaign), Product data (product, category, classification, class and group), factor data for calculus (Alpha Factor, Gamma, Multiplier, Scale).

The suitable use of the forecast definition, allows to generate calculus with different factors for each main group of data defined for a business partner or product.

In this way is possible to get a forecast for each product category, different from another.

To set the sequence of the combinations is possible to use the tab of sequences, with which is possible to define the order of each combination.

### Forecast simulation:

The forecast simulation window, allows to define the required parameters to process a forecast calculation, these parameters are used for the forecast engine to extract the data from the sales historical, to execute the calculation algorithm based on the forecast rule and to save the forecast results.

Forecast Definition: Establishes the forecast definition for this simulation.

Forecast Rule: Establishes the forecast rule to calculate this simulation.

Operational Calendar: Establishes the calendar to use, for the base periods definition and the target period definition.

Source Warehouse: Determines the warehouse for which the sales statistics information will be filtered, in this way it is possible to calculate a forecast for an specific warehouse.

Base Period Definition: Defines the basic periods to filter the sales history information.

Target Periods Definition: Defines the target periods, once the simulation process is executed the calculated values are organized in the order of the target periods definition.

Periods Historical: Determines the number of history periods, which must be used for the forecast calculation, the periods number are equivalent to the defined inputs at the operational calendar.

Target Warehouse: Determines the destiny warehouse with which the results are generated. In some enterprises the sales historical is generated for each point of sales, by this field is possible to change the source warehouse to a target warehouse with the goal of consolidate the demand in a target warehouse.

Calculate Forecast: This process allows to execute, by the forecast engine, the calculus algorithm established by the forecast rule, the forecast engine uses the established factors in the forecast definition. The calculated values for each period are saved as result of the simulation.

#### Master of Forecast Simulation:

The records of this tab are generated as result of applying the combinations set in the forecast definition, each master record is a unique combination of product, warehouse, and the forecast factors used for this calculus.

Alpha Factor: This factor is used for the forecast engine and determines the smoothing constant used for some forecast models of exponential smoothing. It hast to be a value in the range of 0.0-1.0

Gamma Factor: This factor is used for the forecast engine and determines the smoothing constant used in second place for some forecast models of exponential smoothing forecast, the Gamma Factor is used to smooth the tendency, it must be a value in the range of 0.0-1.0

Multiplied Factor: This factor is used by the forecast engine and determines the percentage in which the calculated quantity of the forecast is increased or decreased. A negative percentage indicates the quantity is reduced.

Scalar Factor: This factor is used for the forecast engine and determines the percentage to be multiplied or scale a calculated quantity of the forecast, this value must be absolute.

#### Forecast Simulation Detail:

The records of this tab are generated as result of applying the established combinations in the forecast definitions and the number of established periods in the definition of basic periods for each master of forecast simulation, a detail record is created for each period accumulating the invoiced quantities between the range of the start and the period end date.

#### Forecast simulation line:

Shows the source of the sales historical for each detail.

#### Results of the Forecast Simulation:

The records on this tab are generated by the execution of the Forecast Engine, using the implemented algorithm in the Forecast Rule, a record is created for each established period in the target periods definition.

The Forecast Engine uses the Forecast Simulation Detail, the Forecast Rule and the factors, to calculate a resultant forecast for each target period, this allows to use the sales historical of the previous year and to calculate the current year sales forecast.

### Forecast Simulation Result:

The forecast simulation browser allows to compare base period data with the simulation result of the target period, after executing a forecast simulation. The goal of this query is to validate that the results are considered in the company plans.

### Forecast Simulation Report:

This process generates a report containing the result of the forecast calculation, parameters can be used to filter the result of the report. The main goal of this report is to evaluate and analyze the result of multiple simulations to determine the most adequate, to be able to generate the forecast.

### Generate Forecast Process:

This process allows to generate a forecast based on the forecast simulation calculation.

The process uses the resulting simulation values ​ to generate a new forecast.

Action Type of the forecast:  It Indicates how the forecast will be generated

If the action type is "Replace" all lines of this forecast are going to be  eliminated and will be generated again, based on the simulation products and the selection criteria.

If the action type  is "Merge" all lines of this forecast will be combined, based on the unique combination of product, warehouse and period. Therefore, if the combination exists, the forecast quantities are accumulated.

The Load Type of forecast: Indicates which date of the period will be used to determine the forecast line promised date.

Options:

To Use the Period Start Date: The due date is set  based on the period start date

To Use the Period End Date:  The due date is set based on the period end date.

Days after the due date:  Indicates the number of days to be added or subtracted to the due date. If the value is negative, the days are subtracted.

#### Selection Criteria:

It is possible to use the category, classification, class and group of the product to get the products to be included in the new forecast.

### Forecast:

The Forecast window allows to maintain the sales forecast information for an organization.

Inside the forecast window the field  Price List has to be defined to determine the sales goal amounts and to obtain an estimated value for the sales plan by sales representative.

The Forecast report show the Sales Plan , the goal amounts which has to be accomplished, the information to be grouped by sales representative, product, warehouse and period.

The field Operational Calendar and Periods Definition, must be defined to determine the delivery promised date for the forecast products.

The forecast lines can be captured manually entering the sales representative, product, warehouse, quantity, period or it can be generated from a simulation using the Generate forecast process.

The products and its quantities are considered by MRP when  the forecast is already  processed, ADempiere allows to have several forecast simultaneously.

If you don’t want that MRP considers a Forecast processed,  it should be deactivated.

### Forecast Report:

This process generates a sales forecast detailed report, classified by sales representative, product warehouse, period and promised date, these parameters can be used to create filters at the report result.

The main goal of this report is to analyze the sales plan, considering quantities and amounts.

### Forecast Report by Period:

This process generates a report summarized by forecast period , some parameters can be used to filtrate the report results.

The main goal of this report is to analyze the sales plan, considering quantities and amounts by an specific period.


# Warehouse Management System

Usually the sales department creates Sales Orders *SO* using alternative Delivery Rules:

| **Delivery Rule**   |
| ------------------- |
| Full Line Delivery  |
| Full Order Delivery |

## Distribution Plan

This report comes out of executing a standard process, basically shows current status of items to be delivered, it allows to consolidate commitments from previous orders in order to generate a delivery plan, this in turn allows to create Outbound Orders based on the items to be delivered.

![Input Parameters for Delivery Plan Report](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-MSaiA3SNKjv_RdQn6Iu%2F-MSajZPlqO3kOrZSsQ_D%2Fimage.png?alt=media\&token=eacccdd3-0a1f-491e-8d1b-335bce5a2472)

![Delivery Plan Report](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-MSak6tmlZvAQ7_kSgDn%2F-MSakN_ySqZbRr2FhyVr%2Fimage.png?alt=media\&token=57fd72e9-40ba-4ae4-8d9b-6e71d3ff9f9a)

Important data is obtained from this report, such as delivery date, source warehouse, customer, quantity, among others.

## Generate Outbound Order

The user generates a picking list through an Outbound Order *OO* using several criteria based on demand or open sales orders. It is important to mention the key parameters chosen here refer to common criteria that makes delivery possible, for example: Promised Date range, Document Type, Sales Region.

![Generate Outbound Order Selection Criteria](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-MSc9b8DcJuSaAVQE6hW%2F-MScE4Mk_DcsWHENbeKZ%2Fimage.png?alt=media\&token=ba473864-96ce-4e05-a6b6-aaa26195faa5)

![Record Selection Preview from Order Lines](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-MSc9b8DcJuSaAVQE6hW%2F-MScGVZjbdPOPqzrQNFn%2Fimage.png?alt=media\&token=99d43aee-e9b5-44d0-8e5f-dc4a700198b5)

![Generated Outbound Order Example](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-MScHlj47ygiX_QVbc-6%2F-MScJ3xHqMuTAW0zzzoE%2Fimage.png?alt=media\&token=6f65a106-283c-487f-b408-40799fa8f53d)

![Outbound Order Line Detail](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-MTy4cV_R2R_GyDumy1H%2F-MTySmE55uFkenVme6fz%2Fimage.png?alt=media\&token=81368ec3-a9c9-473d-b66e-e65e2f1b792a)

You may notice there are different sales order lines reference in an outbound order, This is because their focus is to ease deliveries across several criteria, for example a distribution route and/or fulfilling truck capacity.

![Release Outbound Order to Pick](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-MTy4cV_R2R_GyDumy1H%2F-MTy_KzEXJh4xQ6gi6qb%2Fimage.png?alt=media\&token=5b909548-d2f2-4853-8418-fd9c569d9fcd)

As we reach one of the critical steps in this process, this is the Release Outbound Order to Pick that generates the pick tickets and indicates the picking list and the location of the items.

## Distribution Order

The pick tickets that were created on the previous steps will now show up as distribution orders

![Distribution Order from Pick Ticket](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-MTy4cV_R2R_GyDumy1H%2F-MTyayLeqQAnKh2WlgUz%2Fimage.png?alt=media\&token=15b8ccd7-a493-49d4-9062-64c5055c29d4)

There are a number of different business scenarios that leverage the distribution order document so from here we can manage picking tickets and inventory movement transactions which also include an In-Transit Warehouse.

The final step involves Generate Shipments from Outbound Order

![Generate Shipments from Outbound Order](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-MUCY7_SkHWF1iUv1QVd%2F-MUCdBPCfRpYSNf4ly8D%2Fimage.png?alt=media\&token=ca4d83cd-065c-4d8d-a1fd-c351ce069e97)

![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-MUCY7_SkHWF1iUv1QVd%2F-MUCe3jbDGyYrZDmtgn-%2Fimage.png?alt=media\&token=360bad26-51a2-45f8-bce2-b8dc63cc4415)


# System Administration

This guide provides instructions for the effective administration of the ADempiere system.


# Installation

The following sections provide information on the installation and configuration of the ADempiere ERP application.


# System Requirements

ADempiere system requirements vary considerably with the complexity of the enterprise being supported. This page provides a minimum set of system requirements.

It is possible to install ADempiere on a single computer with the database, server and client all running on the same machine. This is quite adequate for evaluation or very small applications. In a production environment such a simple installation may not be sufficient, especially when there are more than a handful of concurrent users. Performance demands will require more attention to the architecture of the installation. In a production environment, it is highly recommended to separate the servers, with the [Application Server](http://en.wikipedia.org/wiki/Application_server) and [Database Server](http://en.wikipedia.org/wiki/Database_server) on different machines.

> \| [![Image:Note.gif](http://wiki.adempiere.net/images/6/62/Note.gif)](http://wiki.adempiere.net/File:Note.gif) | **Note:** Proper database server architecture and database tuning is essential to efficient operation. For installations with more than 10 users, ensure you do your homework. See specifics about your database or consult with a database specialist for correct hardware architecture, database tuning and query tuning.For PostgreSQL, see [Postgres Performance](http://wiki.postgresql.org/wiki/Category:Performance) [Hardware Design](http://www.postgresql.org/files/documentation/books/aw_pgsql/hw_performance/) [Tuning Your PostgreSQL Server](http://wiki.postgresql.org/wiki/Tuning_Your_PostgreSQL_Server) [Using EXPLAIN (Query Tuning)](http://wiki.postgresql.org/wiki/Using_EXPLAIN) | | :--- | :--- |

The following sections describe the main requirements and options.

## ADempiere Application Server Requirements

### Software

* Operating Systems - any one of the following
  * Microsoft Vista, Windows 7 or later (Support for will be limited by the supporting stack of Java and database.)
  * Linux
    * Suse \*
    * Red Hat \*
    * CentOS
    * Debian / Ubuntu
    * FreeBSD
  * Unix
    * OpenSolaris
  * MAC OSX

### Hardware

* Architecture of hardware
  * [Intel](http://en.wikipedia.org/wiki/XEON)
  * [AMD Opteron](http://en.wikipedia.org/wiki/Opteron)
  * [Sparc](http://en.wikipedia.org/wiki/SPARC)]
  * [Power](http://en.wikipedia.org/wiki/Power_Architecture)
  * [Itanium](http://en.wikipedia.org/wiki/Itanium)

### Databases

* Oracle 10g release 2 (Express, Standard and Enterprise editions)

> \| [![Image:Note.gif](http://wiki.adempiere.net/images/6/62/Note.gif)](http://wiki.adempiere.net/File:Note.gif) | **Note:** The export utility (used by RUN\_DBExport) on 11g doesn't export empty tables by default. Some configuration of the database is needed or you need to use a different tool. For that reason, 11g is not "officially" supported. | | :--- | :--- |

* PostgreSQL 8.2 or better
* MySQL

### Stack Required

* (Versions 3.7.0 and below) Java 2 Platform Standard Edition 5.0 or higher
* (Version 3.8.0 and above) Java 2 Platform Standard Edition 7.0 or higher
* JBoss
* Apache-ant 1.6 or higher.

### Technologies Used

* Java
* JavaServer pages (JSP)
* Servlets
* EJB
* SQL/SQLJ
* XML
* HTML/CSS
* PDF

### Client Side

For web start or web application:

* Browsers
  * Firefox 2.0 or better
  * Google Chrome
  * Safari 2 or better
  * Internet Explorer 7.0 or better
  * Java 2 Platform Standard Edition 5.0 or higher

For client application

* Java 2 Platform Standard Edition 5.0 or higher
* Operating Systems - any one of the following
  * Microsoft Windows 2000, XP\*, Vista or newer
  * Linux
    * Suse \*
    * Red Hat \*
    * CentOS
    * Debian / Ubuntu
    * FreeBSD
  * Unix
    * OpenSolaris
  * MAC OSX


# Install ADempiere easily with Docker

Describes the steps to install ADempiere with Docker.

## Install Docker for your operating system

To install Docker on MacOS see <https://docs.docker.com/docker-for-mac/install/>

To Install Docker on Window see <https://docs.docker.com/docker-for-windows/install/>

To Install Docker on Debian Linux see <https://docs.docker.com/engine/install/debian/>

Verify that docker is installed :

```bash
docker --version
Docker version 20.10.2, build 2291f61
```

## Install Docker Compose for your operating system

To install Docker <https://docs.docker.com/compose/install/>

```bash
docker-compose --version
docker-compose version 1.27.4, build 40524192
```

## Install git for your operating system

to Install git see <https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>

```
git --version
git version 2.24.3 (Apple Git-128)
```

## Clone the ADempiere Docker Repository

```bash
git clone https://github.com/adempiere/adempiere-docker.git
```

## Setup ADempiere Docker Install

Open a shell command terminal and run the following statements:

Edit and modify the default settings for the PostgreSQL database&#x20;

```bash
cd adempiere-docker
cat .env
#  Copyright (C) 2010-2017, OpenUp S.A. , http://www.openup.com.uy
#  Copyright (C) 2003-2017, e-Evolution Consultants S.A. , http://www.e-evolution.com
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#  Email: raul.capecce@openupsolutions.com, http://openupsolutions.com , http://github.com/rcapecce
#  Email: victor.perez@e-evolution.com, http://www.e-evolution.com , http://github.com/e-Evolution
ADEMPIERE_DB_PORT=55432
ADEMPIERE_DB_PASSWORD=adempiere
ADEMPIERE_DB_ADMIN_PASSWORD=postgres
PG_VERSION=12.2
vi .env
```

Edit and modify the default setting for the ADempiere

```bash
cd adempiere
cat .env
#  Copyright (C) 2003-2017, e-Evolution Consultants S.A. , http://www.e-evolution.com
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.ce
#  Email: victor.perez@e-evolution.com, http://www.e-evolution.com , http://github.com/e-Evolution
ADEMPIERE_WEB_PORT=8274
ADEMPIERE_SSL_PORT=4444
ADEMPIERE_VERSION=3.9.3
# ATENTION If is "Y" it will be replace de actual defined database with a empty ADempiere seed
ADEMPIERE_DB_INIT=Y
vi .env
```

Deployment ADempiere using the application shell script

```bash
cd ..
pwd 
# From the adempiere-docker directory execute
./application.sh adempiere up -d --build
# Wait a few minutes while the ADempiere Server installation is done 
docker ps |grep postgres
# The output should show something like 
e70086fe9f89   dd4fa36a9c2f             "docker-entrypoint.s…"   11 months ago       Up 4 minutes       0.0.0.0:55432->5432/tcp                          postgres122_db_1
docker ps |grep adempiere
# The output should show something like 
fe8cc0a49e77   adempiere                "/bin/sh -c '/root/s…"   11 months ago       Up 8 minutes       0.0.0.0:4444->4444/tcp, 0.0.0.0:8274->8888/tcp   adempiere
docker logs adempiere
```

Based on the configuration of ./adempiere/.env, docker will show the available ports where the ADempiere services were deployed 0.0.0.0:4444->4444/tcp, 0.0.0.0:8274->8888/tcp

If everything goes well up to here, open the following url <http://0.0.0.0:8274/webui/> in the browser of your choice

![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-MSdW1uWbSW0MAlM0YCL%2F-MSddzYa7tn_S04R8MXb%2Fimage.png?alt=media\&token=4e28fab1-a1ab-4e76-887a-bbea9497fa27)

To access use the username and password GardenAdmin

![ADempiere Role](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-MSdW1uWbSW0MAlM0YCL%2F-MSde6O7b-3YoftgH9Xj%2Fimage.png?alt=media\&token=94cd9bd8-33cb-416f-a1b1-db50629f2e83)

Congratulations now you can evaluate and try adempiere locally

![ADempiere Main Screen](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-MSdW1uWbSW0MAlM0YCL%2F-MSdeFUqxc225QbXWUpu%2Fimage.png?alt=media\&token=bfb56f31-c28e-49e1-b51f-70379ecdf838)

{% hint style="danger" %}
The deployment in Docker is done for didactic purposes, for a production installation requires specific adjustments in the database and memory parameters
{% endhint %}

## See Also

[Github ADempiere Docker Repository](https://github.com/adempiere/adempiere-docker/blob/master/README.md)


# Installing ADempiere Manually

## General Installation Instructions

The database and application server can be installed on a single computer or multiple computers. Demonstrations and small installations can easily be handled by a single server but larger companies will benefit from dedicated database and application servers in a more complex and secure environment.

These installation instructions are intended for initial installations and cover the basic installation requirements. For installation in larger complex environments, additional security concerns may need to be addressed. See Securing Your ADempiere Installation.

The installation process is similar across operating systems with a few minor exceptions and involves the following steps:

1. [Database Server Installation and Setup](https://adempiere.gitbook.io/docs/system-administration/installation/installing-adempiere-manually/database-server-installation-and-setup)
2. [Application Server Installation and Setup](https://adempiere.gitbook.io/docs/system-administration/installation/installing-adempiere-manually/application-server-installation-and-setup)
3. [Initialize the Database](https://adempiere.gitbook.io/docs/system-administration/installation/installing-adempiere-manually/initialize-the-database)
4. [Launch the Application Server](https://adempiere.gitbook.io/docs/system-administration/installation/installing-adempiere-manually/launch-the-application-server)

The details of each step are covered in the following sections.


# Database Server Installation & Setup

## Things to Think About

The ADempiere scripts will need to find the database command line utilities, so set your path to point to the "bin" directory of the database install. You can do this in the same way JAVA\_HOME was used above. Create an environment variable such as DATABASE\_HOME set to the database install directory, and add DATABASE\_HOME/bin to your path according to the methods for your system

{% hint style="info" %}
The ADempiere application utility scripts need access to the database binary commands from the application server machine. You may need to install an empty version of database on the ADempiere application server or, at least, a copy of the necessary binary executable files.
{% endhint %}

{% hint style="warning" %}
If for some twisted reason you also have Oracle running on the same machine as PostgreSQL, be aware that the two databases include some executables with the same name. If you have both POSTGRES\_HOME and the equivalent ORACLE\_HOME on the path, you might have errors when running some of the ADempiere scripts. Try to keep the path pointing to one or the other database at a time and switch between the two as required.
{% endhint %}

## PostgreSQL Installation & Setup

It is recommended that you read the [PostgreSQL Manuals](http://www.postgresql.org/docs/manuals) carefully. There are many useful tips and tricks in the documentation and user comments.

If you use the Postgres Windows Installer, many of the following steps will be done for you by the installer but you will have to pay attention to the security settings.

The following is from the PostgreSQL installation guide after the software has been built and installed from source.

Create a unpriviledged user on the database server computer that is unique to the PostgreSQL installation and has sole access to/ownership of the data the database creates but little else. Don't use this user to install the software but ensure the PostgreSQL server daemon runs under this account. The user "postgres" is a common choice.

Log in as the "postgres" user and [create the database cluster](http://www.postgresql.org/docs/8.4/interactive/creating-cluster.html) - a group of databases. This is done by defining the location where the databases will be stored. This can be anywhere on the file system. The cluster is created with the command initdb which comes with PostgreSQL. The format is

```
$ initdb -D /usr/local/pgsql/data
```

where /usr/local/pgsql/data is the location of the database cluster. As an alternative to the -D option, the environment variable PGDATA can be defined.

{% hint style="info" %}
If the postgres user is unpriviledged, the initdb command may not be able to create the data directory if it doesn't already exists. In that case, log in as root/administrator and create the data directory before you run the command as the postgres user. The initdb command will remove all access permissions to the data directory for everyone but the postgres user. See the PostgreSQL manuals for additional security settings.
{% endhint %}

It is important to properly set up the [pg\_hba.conf](http://www.postgresql.org/docs/8.4/interactive/auth-pg-hba-conf.html) file to ensure the ADempiere application server can talk with the database. Remote TCP/IP connections will not be possible until this file is modified since the default behavior is to listen for TCP/IP connections only on the local loopback address "localhost". When the application server and the database server are separate machines, the pg\_hba.conf file must be set to allow connections from the application server. For security, use as restrictive a connection as possible.

Follow the instructions to start the database server.

Move on to [Application Server Installation & Setup](https://adempiere.gitbook.io/docs/system-administration/installation/installing-adempiere-manually/application-server-installation-and-setup).

## Oracle Installation & Setup

{% hint style="info" %}
The Oracle XE version (Express Edition) is available for free but there are limitations on its use in terms of maximum database size, number of running instances allowed, amount of RAM used, number of CPUs used to process queries (only 1 used) and a lack of https support. While these limitations are acceptable for demonstrations and development, use in production and multi-user environments is not recommended. Please review the Oracle Database Express Edition documentation on Licensing Restrictions prior to making your choice. If you require Oracle, consider purchasing licenses for the Standard Editions.
{% endhint %}

Oracle installation is straight forward. Follow the instructions in the Oracle documentation.

Move on to [Application Server Installation & Setup](https://adempiere.gitbook.io/docs/system-administration/installation/installing-adempiere-manually/application-server-installation-and-setup).

## MySQL Installation & Setup

{% hint style="info" %}
ADempiere integration with MySQL requires developer support. Please verify in the repository and forums if MySQL is supported by the version of ADempiere you wish to use.
{% endhint %}

This section from [Naquib13](http://wiki.adempiere.net/User:Naquib13). He is documenting from Trifon's [SF thread](http://sourceforge.net/projects/adempiere/forums/forum/610546/topic/3854274).

* SUN JDK
* [MySQL 5.x](http://www.mysql.com/downloads/mysql/) I recommend using [Workbench](http://www.mysql.com/downloads/workbench/)
* Do the following after installing the above:
* Change my.cnf file.
* Set tables names to be lower case.
* Enable recursive stored procedures.
* Enable MySQL ANSI mode. $ sudo vim /etc/mysql/my.cnf lower\_case\_table\_names=1 max\_sp\_recursion\_depth=128 sql\_mode='ANSI'
* Restart MySQL server $ sudo /etc/init.d/mysql restart
* Create "adempiere" database $ mysql -u root -p mysql>create database adempiere DEFAULT CHARACTER SET = utf8 DEFAULT COLLATE = utf8\_bin;
* Create "adempiere" MySQL DB user $ mysql -u root -p mysql> GRANT ALL ON adempiere.\* TO 'adempiere'@'localhost' IDENTIFIED BY 'adempiere';
* Import Initial MySQL DB Seed(ADempiere version 3.6.0LTS) $ mysql -u adempiere -p -h localhost adempiere < \<ADEMPIERE\_HOME>/data/Adempiere\_mysql.dmp
* Follow standard ADempiere installation process $ \<ADEMPIERE\_HOME>/RUN\_setup.sh
* Start ADempiere Server $ \<ADEMPIERE\_HOME>/utils/RUN\_Server2.sh
* Start ADempeire Swing client $ \<ADEMPIERE\_HOME>/RUN\_Adempiere.sh

Move on to [Application Server Installation & Setup](https://adempiere.gitbook.io/docs/system-administration/installation/installing-adempiere-manually/application-server-installation-and-setup).

### Links

* [ADempiere on MySQL](http://sourceforge.net/projects/adempiere/forums/forum/610546/topic/3854274)- SF.net thread by Trifon on 2010 & 2011.
* [Running ADempiere on MySQL](http://blogs.sun.com/praneet/entry/mysqling_adempiere) by Praneet on Jul 03, 2009.
* [MySQL Download](http://www.mysql.com/downloads/mysql/)


# Application Server Installation and Setup

This page provides advice on installation of the ADempiere application server.

This page is directed at System Administrators who need to install the **ADempiere Application Server** in a network environment where the database server could be running on a separate network server and the clients run on remote computers.

## Prerequisites

Before continuing, ensure you have installed a suitable database (i.e. Oracle 10g, Oracle 10gXE, PostgreSQL, MySQL) and that the database server is running. See [Database Server Installation & Setup](https://adempiere.gitbook.io/docs/system-administration/installation/installing-adempiere-manually/database-server-installation-and-setup).

## Required Downloads

Download each of the following packages:

* **Java SE Development Kit** - Get the latest from [http://www.oracle.com/](http://www.oracle.com/technetwork/java/javase/downloads/index.html). You only need the JDK without JavaFX, EE or NetBeans bundles.
* **ADempiere Latest Release** - Download the latest ADempiere from [here](https://github.com/adempiere/adempiere/releases).
* **ADempiere Patches** - Any patches or customization jars to apply.

## Install Java

Install the JAVA JDK with the default installation settings. Say OK to install the follow-on JRE as well. Carefully note the full path for the JDK directory (e.g: C:\Program Files\java\jdk1.5.0\_19) and the JRE directory that you have just installed.

{% hint style="info" %}
There may well be a number of JDK and JRE directories, so choose the right one! The JDK should include the JRE.
{% endhint %}

The ADempiere scripts rely on the existence of a system environment variable JAVA\_HOME. When the scripts call java, they use the full path as JAVA\_HOME/bin/java so it is important that this variable exist.

Following the instructions for your system, add a new System Variable JAVA\_HOME for your new JDK directory. Set JAVA\_HOME to C:\Program Files\Java\jdk1.7.0\_25 (or whatever your JDK directory is called).

According to your OS, append the following JDK path to the system path:

`%JAVA_HOME%\bin` or

`$JAVA_HOME/bin`

## Install the ADempiere Software

There is no install script. Just extract the ADempiere archive to a suitable location: (e.g. c: or /u01/). For reference, call this directory ADEMPIERE\_ROOT. You should end up with the files in a folder like ADEMPIERE\_ROOT\Adempiere. For reference, call this folder ADEMPIERE\_HOME.

{% hint style="info" %}
**Avoid spaces in the directory path**. The batch scripts do not like directory names with spaces. If using a ADEMPIERE\_ROOT with multiple directories, avoid directory names with spaces.
{% endhint %}

### Apply the Patches

Patches are a combination of \*.jar files, which replace \*.jar files in the ADEMPIERE\_HOME\lib directory, and migration scripts which update the database. In the Patches directory on Source Forge, there may be more than one type of \*.jar that needs patching. If you downloaded one or more patch files, replace the existing file with the downloaded one, changing its name to match. For example, copy the \*\_patches\_\*.jar file to ADEMPIERE\_HOME\lib\patches.jar, overwriting the existing file. See the detailed instructions in [Patches Installation](http://wiki.adempiere.net/Patches_Installation).

{% hint style="info" %}
It is a good idea to rename the existing \*.jar file to something like patches.jar.old before you replace it with the the new file.
{% endhint %}

### Apply Customizations, Packages and other Files

If you have a customization.jar with customized code or a packages.jar file with supporting \*.jar files, add them to the ADEMPIERE\_HOME\lib directory, overwriting the existing files.

For migration scripts which end in .xml, store these in the ADEMPIERE\_HOME/migration directory.

## Setting Up The ADempiere Server

The Application Server is configured by a utility RUN\_Setup.(sh/bat) found in the ADEMPIERE\_HOME directory. This utility launches a tool where the configuration settings can be set and tested. Once everything passes the tests, the configuration is saved and the software repackages itself with the new settings. You can then launch the Application Server.

You can rerun this utility as many times as you like until everything is correct.

{% hint style="info" %}
In case you are changing settings on an existing Application Server, make sure that the Application Server is shut down before you start. Otherwise you will get port errors during the testing. You can shut down the Application server by running the script RUN\_Server2Stop.(sh/bat) from ADEMPIERE\_HOME/utils or by stopping the "service".
{% endhint %}

In a command shell with administrative privileges, run the script **RUN\_Setup**, located in the ADEMPIERE\_HOME directory. The ADempiere Server Setup window should appear as shown below:

![ADempiere Server Setup window](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LKXrGTYoHPeh7rnZ4hI%2F-LKXrH6wWklu234b7jOu%2Fimage%20\(2\).png?generation=1534962004019410\&alt=media)

The Setup window opens and loads its values from the file AdempiereEnv.properties. It looks for this file in the ADEMPIERE\_HOME directory. If the environment variable ADEMPIERE\_HOME is not set or is null, it will look in the directory defined in the system property "user.dir".

{% hint style="info" %}
The setup process creates a file named Adempiere.properties. This is the main configuration file for your Client. You can copy this file and pass it as a variable when you start ADempiere using the command line interface parameter-DPropertyFile=AdempiereProduction.properties. If you create several files you can use them to easily switch between development, test and production environments, for example.
{% endhint %}

### Setup Fields

Fill in the setup window fields as follows:

* Java
  * **Java Home**: select the SDK Java Home location (e.g. C:\jdk1.5.0\_05). This should be the same as the JAVA\_HOME environment variable.
  * **Java VM**: the Java Virtual Engine Vendor (Default= Sun).
* Adempiere
  * **ADempiere Home**: is the base directory where the distribution files are located (e.g. C:\Adempiere). This should be the same a the ADEMPIERE\_HOME environment variable.
  * **KeyStore Password**: ADempiere requires a SSL certificate. It automatically creates a certificate in the key store $ADEMPIERE\_HOME/keystore/myKeystore with the keystore password entered. The self certified certificate created has the alias adempiere and uses the same password as the keystore. You can replace the certificate used with the Java "keytool" (see Java tool documentation).
* Application Server
  * **Application Server**: is the name, URL or IP of your server PC (Don't use localhost). The Application Server defaults to the server currently running the program. Avoid using IP addresses - use the DNS name of the server.
  * **Web Port**: The web port that the Application Server will listen on. Access to the application server will be through a URL similar to [http://myApplicationServer:webport](http://myapplicationserver/:webport) ([http://appserver:8088\\](http://appserver/:8088\)/). Please keep in mind that, under Linux/Unix, ports under 1000 need root privileges. If you use Apache as a front end, you may need to use ports like 8080 or 8088 - basically, find a free port. The default ports is 80
  * **SSL**: The secure socket layer port. The default is 443. If that is not available try another value such as 4443 or 8443.
  * **JNP Port**: The Java Name Provider and Remote Method Invocation(RMI) port. The Default ports are 1099 (1098).
* Database Server
  * **Database Server**: The Database Server defaults to the server currently running the program. Avoid using IP addresses - use the DNS name of the server. Localhost can be used only if the database server is running on the same machine as the Application Server and client software. For Oracle, the Service names are discovered. You can overwrite the entries if they are not correct.
  * **Database Name**:
    * PosgreSQL: PostgreSQL database name
    * Oracle: SID/Service name. Oracle 10g/11g default: orcl, OracleXE default: xe
  * **Database Type**: select the database you have installed (i.e. Oracle 10g, Oracle 10gXE, PostgreSQL).
  * **Database Port**: select the port for connect to database.(i.e. Oracle use 1521 as standard port, PostgreSQL 5432, etc.)
  * **System Password:**
    * Oracle: Password for the system user.
    * PostgreSQL: Password for the postgres user.
  * **Database User**: The application database user name, default is adempiere.
  * **Database Password**: The application database password, default is adempiere.
* Mail Server (See notes below)
  * **Server**: \_\*\*\_the mail server  (e.g. smtp.gmail.com)
  * **Port**: the mail server port for sending mail
  * **Protocol**: the protocol to use, SMTP or IMAP
  * **Admin E-Mail**: The email to use as the From address
  * **Encryption Type**: The type of encryption to use
  * **Auth. Mechanism**: how the account is authorized.  Login is the default.
  * **Mail User**: the mail user login name
  * **Mail Password**: the mail user password

Mail setup is optional but a server does have to be identified. The Setup Tool will finish successfully whether the mail tests work or not. You can maintain the mail server connection in the Application on a Client basis from the [**Client Window**](http://wiki.adempiere.net/ManPageW_Client). If you don't want to setup mail or don't have an SMTP server, just enter a valid server - the field defaults to the local computer name. As long as the server exists, the setup will finish successfully.

{% hint style="info" %}
The software only needs a method to send email. There is no ability to read email in the application.&#x20;
{% endhint %}

### Testing the Setup

After you fill the Setup fields, press the Test button to verify them. As the test progresses, you will see the boxes checked (√). Only if all the parameters are verified will you will not be able to save them. If an entry cannot be verified, a pop-up window stating the error will be displayed Fix it and test again.

If, for example, the Application Server name is wrong, then you will see a message such as:

![Server setup error dialog](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-MVWAQ9PuO2w1oJDGdJs%2F-MVWEetz8MJhOmUJCTia%2FIS_ServerSetupError.PNG?alt=media\&token=950a7416-45c5-4888-8cba-29a3df353f13)

When all the tests pass (you can see the boxes checked: √ ):

![ADempiere Server Setup with the test results shown](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LKZhyRHZJ7BidS9rrYg%2F-LKZhzcOpuEBHYyvYRXf%2Fimage-1-1%20\(1\).png?generation=1534993107786077\&alt=media)

* press the Save button. This will save the settings to the AdempiereEnv.properties file in the ADEMPIERE\_HOME directory.
* After you accept the license, you will see the dialog:

![The setup was saved and the process is ready to start deployment](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-MVWAQ9PuO2w1oJDGdJs%2F-MVWF8fywjouF4Xs8TW0%2FIS_EnvironmentSaved.PNG?alt=media\&token=2ed63599-efdc-4b9e-ba25-08cbcbbab3f9)

* Press the OK button to continue and take a look into the log. Make sure that you see the **BUILD SUCCESSFUL** and **Done**, such as:

```
     [echo] AppsDeployment= C:\Adempiere\jboss\server\adempiere\deploy
     [copy] Copying 1 file to C:\Adempiere\jboss\server\adempiere\deploy
     [copy] Copying 1 file to C:\Adempiere\jboss\server\adempiere\deploy
     [copy] Copying 1 file to C:\Adempiere\jboss\server\adempiere\deploy
     [copy] Copying 1 file to C:\Adempiere\jboss\server\adempiere\deploy

 setupTomcat:

 setupDeploy:
     [echo] AppsDeployment= C:\Adempiere\jboss\server\adempiere\deploy

 setup:

BUILD SUCCESSFUL
Total time: 2 minutes 22 seconds

*** 2006-12-28 14:15:35.53 Adempiere Log (CLogConsole) ***
ErrorLevel = 0
===================================
Setup Client Environment
===================================
SET ADEMPIERE_HOME=C:\Adempiere
SET JAVA_HOME=c:\Archivos de programa\Java\jdk1.5.0_05
Path is OK = c:\Archivos de programa\Java\jdk1.5.0_05\bin;C:\Archivos de programa\Java\jdk1.5.0_05\
bin;C:\oraclexe\app\oracle\product\10.2.0\server\bin;%SystemRoot%\system32;%SystemRoot%;
%SystemRoot%\System32\Wbem
Created Shortcut Adempiere.lnk
Created Shortcut Adempiere Web Site.url
Done
.
For problems, check log file in base directory
```

If something is wrong, you can fix it and rerun the script until everything is correct.

Once the setup is complete, you can move on to [Initialize the ADempiere Database](http://wiki.adempiere.net/Initialize_the_ADempiere_Database).

## Common Issues

* **Application Server** \* **Database Server** is the name, URL or IP of your server PC.
* **JNP Port = 1099** error means that a previous service is running. Kill it. Also, since this is the first port that is tested, it could also mean that you have a mismatch between your host name (in the hosts file) and your actual IP address. Fix it in "/etc/hosts" (linux)
* **Database Port = 1521** error can be solved by restarting DB machine.
* **System** & **Database Passwords** are those defined when you setup your Database.
* **Mail Server** is optional. RUN\_Setup can still finish without it.

### Java Home Error

If you receive the following message:

![JAVA\_HOME was not found](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-MVWAQ9PuO2w1oJDGdJs%2F-MVWFguK8aRoeryUEpQp%2FIS_JAVA_HOME_ERROR.PNG?alt=media\&token=fdd6d0a1-43f0-4e84-ae64-390ffe13f835)

You should check your java environment variables. Check that the JAVA\_HOME system environment variable points to the correct directory.

### Web Port Error

If you receive the following message from the installer:

![Web port error](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-MVWAQ9PuO2w1oJDGdJs%2F-MVWF_d-oJn7MYGMntys%2FAdempiereerror1.png?alt=media\&token=78650211-158b-4051-8153-e47aeb8edd85)

it is likely that you have some other web server running or, if your are using Linux, you need the appropriate privileges.

The default ports are: 80 for http connections and 443 for SSL connections. This message means that the user is not allowed to use the port, likely because it is already used by another application. Change the port to something else. WebPort 8088 and SSL 4443 are recommended. If you are using Linux, remember that ports under 1000 need root privileges. If you are using Oracle database, port 8080 might be used.

### JNP Port 1099 Error

Another possible error is Server Setup Error Error JNP Port (Not correct: JNP Port = 1099) OK

The JNP Port = 1099 error can be caused by another process which is already attached to that TCP port. Take a look what process is using this port and so you can take steps to stop it. It can also be caused by a mismatch between your IP address and the entry in your hosts file. See /etc/hosts(linux) or %SystemRoot%/system32/drivers/etc/hosts(windows).

{% hint style="info" %}
To find the IP address of your server try the following in a command script:Linux /sbin/ifconfigWindows IPCONFIG
{% endhint %}

### JNP Name Not Found Exception

This error is usually related to a DNS problem. It is possible to complete the setup using IP addresses when installing with PostgreSQL. Make sure you have a working DNS environment or add an entry in /etc/hosts(linux) or %SystemRoot%/system32/drivers/etc/hosts(windows).

## See Also

* [Initialize the ADempiere Database](http://wiki.adempiere.net/Initialize_the_ADempiere_Database) is the next thing after Install Server.
* [Launching the ADempiere Application](http://wiki.adempiere.net/Launching_the_ADempiere_Application) to perform the Client-Server client install which is the next thing to do after completing the Database setup.
* [Initial Client Setup](http://wiki.adempiere.net/ManPageX_InitialClientSetup) is the starting business setup within ADempiere.
* [Getting Started](http://wiki.adempiere.net/Getting_Started) Tutorial on how to setup and configure ADempiere for single computer operation (database, application and client all on the same machine).
* [Tutorials](http://wiki.adempiere.net/Tutorials) on many things from basic to advanced.




---

[Next Page](/docs/llms-full.txt/1)

