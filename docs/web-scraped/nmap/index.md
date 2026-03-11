# Source: https://nmap.org/

Title: Nmap: the Network Mapper - Free Security Scanner

URL Source: https://nmap.org/

Markdown Content:
Nmap: the Network Mapper - Free Security Scanner
===============

[![Image 1](https://nmap.org/shared/images/nst-icons.svg#menu)](https://nmap.org/#menu)[![Image 2](https://nmap.org/shared/images/nst-icons.svg#close)](https://nmap.org/#)[![Image 3: Home page logo](https://nmap.org/images/sitelogo.png)](https://nmap.org/)[Nmap.org](https://nmap.org/)[Npcap.com](https://npcap.com/)[Seclists.org](https://seclists.org/)[Sectools.org](https://sectools.org/)[Insecure.org](https://insecure.org/)![Image 4](https://nmap.org/shared/images/nst-icons.svg#search)

[Download](https://nmap.org/download.html)[Reference Guide](https://nmap.org/book/man.html)[Book](https://nmap.org/book/)[Docs](https://nmap.org/docs.html)[Zenmap GUI](https://nmap.org/zenmap/)[In the Movies](https://nmap.org/movies/)
[Get Nmap 7.98 here](https://nmap.org/download)

News
----

*   Nmap.org has been redesigned! Our new mobile-friendly layout is also on [Npcap.com](https://npcap.com/), [Seclists.org](https://seclists.org/), [Insecure.org](https://insecure.org/), and [Sectools.org](https://sectools.org/). 
*   Nmap 7.90 has been released with Npcap 1.00 along with dozens of other performance improvements, bug fixes, and feature enhancements! [[Release Announcement](https://seclists.org/nmap-announce/2020/1) | [Download page](https://nmap.org/download.html)] 
*   After more than 7 years of development and 170 public pre-releases, we're delighted to announce Npcap version 1.00! [[Release Announcement](https://seclists.org/nmap-announce/2020/0) | [Download page](https://nmap.org/npcap/)] 
*   Nmap 7.80 was released for DEFCON 27! [[release notes](https://seclists.org/nmap-announce/2019/0) | [download](https://nmap.org/download.html)] 
*   Nmap turned 20 years old on September 1, 2017! Celebrate by reading [the original Phrack #51 article](https://nmap.org/p51-11.html). [#Nmap20](https://twitter.com/hashtag/Nmap20)! 
*   Nmap 7.50 is now available! [[release notes](https://seclists.org/nmap-announce/2017/3) | [download](https://nmap.org/download.html)] 
*   Nmap 7 is now available! [[release notes](https://nmap.org/7/) | [download](https://nmap.org/download.html)] 
*   We're pleased to release our new and Improved [Icons of the Web](https://nmap.org/favicon/) project—a 5-gigapixel interactive collage of the top million sites on the Internet! 
*   Nmap has been discovered in two new movies! It's used to [hack Matt Damon's brain in Elysium](https://nmap.org/movies/#elysium) and also to [launch nuclear missiles in G.I. Joe: Retaliation](https://nmap.org/movies/#gijoe)! 
*   We're delighted to announce Nmap 6.40 with 14 new [NSE scripts](https://nmap.org/book/nse.html), hundreds of new [OS](https://nmap.org/book/osdetect.html) and [version detection](https://nmap.org/book/vscan.html) signatures, and many great new features! [[Announcement/Details](https://seclists.org/nmap-announce/2013/1)], [[Download Site](https://nmap.org/download.html)] 
*   We just released Nmap 6.25 with 85 new NSE scripts, performance improvements, better OS/version detection, and more! [[Announcement/Details](https://seclists.org/nmap-hackers/2012/4)], [[Download Site](https://nmap.org/download.html)] 
*   Any release as big as Nmap 6 is bound to uncover a few bugs. We've now fixed them with [Nmap 6.01](https://seclists.org/nmap-hackers/2012/3)! 
*   Nmap 6 is now available! [[release notes](https://nmap.org/6/) | [download](https://nmap.org/download.html)] 
*   The security community has spoken! 3,000 of you shared favorite security tools for our relaunched [SecTools.Org](https://sectools.org/). It is sort of like Yelp for security tools. Are you familiar with all of the [49 new tools](https://sectools.org/tag/new/) in this edition? 
*   [Nmap 5.50 Released](https://seclists.org/nmap-hackers/2011/0): Now with Gopher protocol support! Our first stable release in a year includes 177 NSE scripts, 2,982 OS fingerprints, and 7,319 version detection signatures. Release focuses were the Nmap Scripting Engine, performance, Zenmap GUI, and the Nping packet analysis tool. [[Download page](https://nmap.org/download) | [Release notes](https://seclists.org/nmap-hackers/2011/0)] 
*   Those who missed Defcon can now watch Fyodor and David Fifield demonstrate the power of the Nmap Scripting Engine. They give an overview of NSE, use it to explore Microsoft's global network, write an NSE script from scratch, and hack a webcam--all in 38 minutes! ([Presentation video](https://nmap.org/presentations/BHDC10/)) 
*   _Icons of the Web_: explore favicons for the top million web sites with our [new poster and online viewer](https://nmap.org/favicon). 
*   We're delighted to announce the immediate, free availability of the [Nmap Security Scanner version 5.00](https://nmap.org/5/). Don't miss the [top 5 improvements in Nmap 5](https://nmap.org/5/#5changes). 
*   After years of effort, we are delighted to release [Nmap Network Scanning: The Official Nmap Project Guide to Network Discovery and Security Scanning](https://nmap.org/book/)! 
*   We now have an active Nmap [Facebook page](http://facebook.com/nmap) and [Twitter feed](http://twitter.com/nmap/) to augment the [mailing lists](https://nmap.org/#lists). All of these options offer RSS feeds as well. 

Nmap: Discover your network
===========================

Nmap ("Network Mapper") is a [free and open source](https://nmap.org/npsl/) utility for network discovery and security auditing. Many systems and network administrators also find it useful for tasks such as network inventory, managing service upgrade schedules, and monitoring host or service uptime. Nmap uses raw IP packets in novel ways to determine what hosts are available on the network, what services (application name and version) those hosts are offering, what operating systems (and OS versions) they are running, what type of packet filters/firewalls are in use, and dozens of other characteristics. It was designed to rapidly scan large networks, but works fine against single hosts. Nmap runs on all major computer operating systems, and official binary packages are available for Linux, Windows, and Mac OS X. In addition to the classic command-line Nmap executable, the Nmap suite includes an advanced GUI and results viewer ([Zenmap](https://nmap.org/zenmap/)), a flexible data transfer, redirection, and debugging tool ([Ncat](https://nmap.org/ncat/)), a utility for comparing scan results ([Ndiff](https://nmap.org/ndiff/)), and a packet generation and response analysis tool ([Nping](https://nmap.org/nping/)).

Nmap was named “Security Product of the Year” by Linux Journal, Info World, LinuxQuestions.Org, and Codetalker Digest. It was even featured in [twelve movies](https://nmap.org/movies/), including [The Matrix Reloaded](https://nmap.org/movies/#matrix), [Die Hard 4](https://nmap.org/movies/#diehard4), [Girl With the Dragon Tattoo](https://nmap.org/movies/#gwtdt), and [The Bourne Ultimatum](https://nmap.org/movies/#bourne).

Nmap is ...

*   Nmap Security Port Scanner
*   **Flexible**: Supports dozens of advanced techniques for mapping out networks filled with IP filters, firewalls, routers, and other obstacles. This includes many [port scanning](https://nmap.org/) mechanisms (both TCP & UDP), [OS detection](https://nmap.org/), [version detection](https://nmap.org/), ping sweeps, and more. See the [documentation page](https://nmap.org/). 
*   **Powerful**: Nmap has been used to scan huge networks of literally hundreds of thousands of machines. 
*   **Portable**: Most operating systems are supported, including Linux, Microsoft Windows, FreeBSD, OpenBSD, Solaris, IRIX, Mac OS X, HP-UX, NetBSD, Sun OS, Amiga, and more. 
*   **Easy**: While Nmap offers a rich set of advanced features for power users, you can start out as simply as "nmap-v-A _targethost_". Both traditional command line and graphical (GUI) versions are available to suit your preference. Binaries are available for those who do not wish to compile Nmap from source. 
*   **Free**: The primary goals of the Nmap Project is to help make the Internet a little more secure and to provide administrators/auditors/hackers with an advanced tool for exploring their networks. Nmap is available for [free download](https://nmap.org/), and also comes with full source code that you may modify and redistribute under the terms of the [license](https://nmap.org/data/COPYING). 
*   **Well Documented**: Significant effort has been put into comprehensive and up-to-date man pages, whitepapers, tutorials, and even a whole book! Find them in multiple languages [here](https://nmap.org/). 
*   **Supported**: While Nmap comes with no warranty, it is well supported by a vibrant community of developers and users. Most of this interaction occurs on the [Nmap mailing lists](https://nmap.org/). Most bug reports and questions should be sent to the [nmap-dev list](https://seclists.org/nmap-dev), but only after you read the [guidelines](https://nmap.org/book/man-bugs.html). We recommend that all users subscribe to the low-traffic [nmap-hackers](https://seclists.org/nmap-hackers) announcement list. You can also find Nmap on [Facebook](http://facebook.com/nmap) and [Twitter](http://twitter.com/nmap). For real-time chat, join the #nmap channel on [Freenode](http://freenode.net/) or [EFNet](http://www.efnet.org/). 
*   **Acclaimed**: Nmap has won numerous awards, including "Information Security Product of the Year" by Linux Journal, Info World and Codetalker Digest. It has been featured in hundreds of magazine articles, several movies, dozens of books, and one comic book series. Visit the [press page](https://nmap.org/) for further details. 
*   **Popular**: Thousands of people download Nmap every day, and it is included with many operating systems (Redhat Linux, Debian Linux, Gentoo, FreeBSD, OpenBSD, etc). It is among the top ten (out of 30,000) programs at the Freshmeat.Net repository. This is important because it lends Nmap its vibrant development and user support communities. 

Communication
-------------

Nmap users are encouraged to subscribe to the _Nmap-hackers_ mailing list. It is a low volume (6 posts in 2017), moderated list for the most important announcements about Nmap, Insecure.org, and related projects. You can join more than 128,000 current subscribers by submitting your email address here:

(or subscribe with custom options from the [Nmap-hackers list info page](https://nmap.org/mailman/listinfo/announce))

We also have a development list for more hardcore members (especially programmers) who are interested in helping the project by helping with coding, testing, feature ideas, etc. New (test/beta) versions of Nmap are sometimes released here prior to general availability for QA purposes. You can subscribe at the [Nmap-dev list info page](https://nmap.org/mailman/listinfo/dev).

Both lists are archived (along with many other security lists) at [Seclists.org](https://nmap.org/).

Though it isn't nearly as active as the mailing lists, the official IRC channel is #nmap on [Freenode](http://freenode.net/) (irc.freenode.net).

![Image 5](https://nmap.org/shared/images/nst-icons.svg#search)

[Nmap Security Scanner](https://nmap.org/)
------------------------------------------

*   [Ref Guide](https://nmap.org/book/man.html)
*   [Install Guide](https://nmap.org/book/install.html)
*   [Docs](https://nmap.org/docs.html)
*   [Download](https://nmap.org/download.html)
*   [Nmap OEM](https://nmap.org/oem/)

[Npcap packet capture](https://npcap.com/)
------------------------------------------

*   [User's Guide](https://npcap.com/guide/)
*   [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)
*   [Download](https://npcap.com/#download)
*   [Npcap OEM](https://npcap.com/oem/)

[Security Lists](https://seclists.org/)
---------------------------------------

*   [Nmap Announce](https://seclists.org/nmap-announce/)
*   [Nmap Dev](https://seclists.org/nmap-dev/)
*   [Full Disclosure](https://seclists.org/fulldisclosure/)
*   [Open Source Security](https://seclists.org/oss-sec/)
*   [BreachExchange](https://seclists.org/dataloss/)

[Security Tools](https://sectools.org/)
---------------------------------------

*   [Vuln scanners](https://sectools.org/tag/vuln-scanners/)
*   [Password audit](https://sectools.org/tag/pass-audit/)
*   [Web scanners](https://sectools.org/tag/web-scanners/)
*   [Wireless](https://sectools.org/tag/wireless/)
*   [Exploitation](https://sectools.org/tag/sploits/)

[About](https://insecure.org/)
------------------------------

*   [About/Contact](https://insecure.org/fyodor/)
*   [Privacy](https://insecure.org/privacy.html)
*   [Advertising](https://insecure.org/advertising.html)
*   [Nmap Public Source License](https://nmap.org/npsl/)

[![Image 6](https://nmap.org/shared/images/nst-icons.svg#twitter)](https://twitter.com/nmap "Visit us on Twitter")[![Image 7](https://nmap.org/shared/images/nst-icons.svg#facebook)](https://facebook.com/nmap "Visit us on Facebook")[![Image 8](https://nmap.org/shared/images/nst-icons.svg#github)](https://github.com/nmap/ "Visit us on Github")[![Image 9](https://nmap.org/shared/images/nst-icons.svg#reddit)](https://reddit.com/r/nmap/ "Discuss Nmap on Reddit")
