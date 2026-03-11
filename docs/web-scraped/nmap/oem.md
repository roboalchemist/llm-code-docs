# Source: https://nmap.org/oem/

Title: Nmap OEM Edition—Redistribution License

URL Source: https://nmap.org/oem/

Markdown Content:
[Download](https://nmap.org/download.html)[Reference Guide](https://nmap.org/book/man.html)[Book](https://nmap.org/book/)[Docs](https://nmap.org/docs.html)[Zenmap GUI](https://nmap.org/zenmap/)[In the Movies](https://nmap.org/movies/)
The [Nmap Security Scanner](https://nmap.org/) is a network discovery tool uses raw IP packets in novel ways to determine what hosts are available on the network, what services (application name and version) those hosts are offering, what operating systems (and OS versions) they are running, what type of packet filters/firewalls are in use, and dozens of other characteristics. and security auditing. It has been [continuously developed and improved](https://nmap.org/changelog) since the first release in 1997.

Nmap is free for end users, and is trusted by millions of them. But the [free Nmap license](https://nmap.org/npsl) does not allow redistribution of Nmap with proprietary hardware or software products. For more than 20 years we have funded the project by selling OEM licenses to companies who want to embed Nmap within their products to handle network scanning. All major operating systems are supported, including binary packages for Windows, Linux, and Mac OS. The Windows package is an exclusive OEM Edition, custom tailored for this purpose with special features such as silent installer.

Top Nmap OEM Redistribution License Features

*   **Redistribution rights**—The [free Nmap license](https://nmap.org/npsl) does not allow redistribution or use of Nmap within proprietary hardware or software products, but an Nmap OEM License allows for unlimited redistribution either within a product line or across the whole company's product portfolio.
*   **Windows OEM Edition Builds**—We provide special builds for OEM customers utilizing the Microsoft Windows platform. These include a silent installer which also silently installs our [Npcap OEM](https://npcap.com/oem/) Windows library for raw packet capture and transmission. It omits the Zenmap GUI (which licensees almost never need), cutting the installer size by more than half. It also reports itself as Nmap OEM so end-users who notice it on the add/remove Software screen or similar know that it's the officially licensed version of Nmap. 
*   **Commercial support**—Nmap OEM maintenance plans include commercial support to ensure any bugs you find are fixed promptly and all your technical questions answered.
*   **Regular updates**—Nmap OEM maintenance plans also include update rights, so you always have access to the latest releases. We are constantly releasing updates with performance enhancements, bug fixes, and new features you can learn about from [our changelog](https://nmap.org/changelog).
*   **Continuity**—Nmap OEM licensees have a contract guaranteeing the availability and terms for their Nmap OEM usage, while the terms and restrictions for the [free Nmap license](https://nmap.org/npsl/) change from time to time. Licensing revenue also funds continued Nmap development and improvements.

This license is for companies that wish to redistribute or use Nmap within the products they distribute. Folks only wanting to use Nmap themselves or within their organization can already [download and use it for free](https://nmap.org/download.html). It is possible that some end-users might still want to buy Nmap OEM for solely internal use. Perhaps they want the silent Windows installer, or commercial support, or just want to help fund the project. If this is the case, please contact [sales@nmap.com](mailto:sales@nmap.com) and we will consider implementing a program similar to our [Npcap OEM Internal-Use License](https://npcap.com/oem/internal.html).

Nmap OEM releases are always made in conjunction with normal releases and the version numbers are the same. In fact, Nmap OEM licensees on non-Windows platforms (including Linux and Mac OS X) simply use our standard Nmap builds (or build it themselves). A special OEM build isn't really needed for those platforms since those Nmap builds already support silent installation and they have no need for the Npcap Windows driver.

Nmap OEM Licensees may use any Nmap features except for the Zenmap GUI, which is generally not relevant for OEM customers and is stripped out of our Windows OEM builds to reduce installer size. Some of the most valuable features include:

*   **[Host Discovery](https://nmap.org/book/host-discovery.html)**—determine which hosts are up and available on the network.
*   **[Port Scanning](https://nmap.org/book/port-scanning.html)**—determine which TCP/UDP ports are open.
*   **[OS Detection](http://nmap.org/book/osdetect.html)**—guess the remote operating system and device type based on TCP/IP stack characteristics.
*   **[Version Detection](http://nmap.org/book/vscan.html.)**—interrogate open ports to determine the running protocol, application, and version number if possible.
*   **[Nmap Scripting Engine](http://nmap.org/nsedoc/)**—a growing library of more than 500 scripts for enhanced network discovery and vulnerability assessment. For example, it can be used to query windows machines for exact OS or detect dozens of common vulnerabilities.

Our recommended integration approach is to install Nmap on the end-user system using the silent-install feature and then have your application execute Nmap when needed, requesting XML formatted results (-oX) which you would then parse with any XML parser. The license also allows other integration approaches, such as parsing of Nmap's normal output format, processing Nmap data files directly, or even integrating Nmap source code into your application.

Please note that this whole page describes the licenses that we currently sell. Previously sold licenses may have different terms and those are the terms which apply. If you have questions about your specific license, please contact [sales@nmap.com](mailto:sales@nmap.com).

To keep things simple our standard Nmap license involves no per-seat royalties--just a reasonable one-time license buy-out fee and an optional annual maintenance fee which includes all new Nmap releases as well as commercial support. That maintenance fee never increases for as long as you keep renewing. We also offer a term license which includes redistribution rights and maintenance for a quarterly fee which must be paid every 3 months for as long as you are selling new products containing Nmap. The term license fee never increases either.

Prices are in U.S. Dollars (USD) based on the size of company buying the license, broken into four tiers. This is because larger companies are usually able to derive more value from Nmap OEM by leveraging it at a greater scale. Larger companies generally cost us more to support as well. Prices are based on the whole company size, not just an individual division or development team. The prices are locked in after purchase, so they don't increase as companies grow later.

*   Our **Nmap OEM Enterprise Redistribution License** is for our largest customers. The perpetual license to use Nmap OEM in a product line or category costs $119,980, plus an optional annual maintenance fee of $29,980. The quarterly term license option (which includes maintenance) costs $17,980 every 3 months.

*   Our **Nmap OEM Mid-Sized Company Redistribution License** provides a discount for mid-sized customers. The perpetual license to use Nmap OEM in all company products costs $89,980, plus an optional annual maintenance fee of $22,980. The quarterly term license option (which includes maintenance) costs $13,980 every 3 months. To qualify for this license, a company must meet all these criteria:

    1.   500 or fewer employees 
    2.   Revenue (not profit) less than US$200 million in their most recent fiscal year 
    3.   If publicly traded, their market capitalization must be less than $1 billion 

*   Our **Nmap OEM Small/Startup Company Redistribution License** covers the smallest of our customers. The perpetual license to use Nmap OEM in all company products costs US$59,980, plus an optional annual maintenance fee of $17,980. The quarterly term license option (which includes maintenance) costs $9,980 per 3 months. To qualify for this license, a company must have 50 or fewer employees and no more than US$10 million revenue in the most recent fiscal year. Subsidiaries of larger companies only qualify for the small/startup license if the parent company also qualifies as such.

All perpetual licenses include a six-month trial period during which you can cancel for any reason and receive a full refund of all money paid (including maintenance). The term license is only a 3-month commitment and can also be terminated with a full refund during the first 30 days of the initial quarter. We also provide the [standard version of Nmap](https://nmap.org/download.html) that you can fully test internally before purchase.

The rights Nmap OEM customers enjoy are spelled out in the [license certificate that we send to customers](https://nmap.org/oem/docs/Nmap-OEM-Software-Redistribution-License-Certificate.pdf) (filled out of course). It includes support, indemnification, warranty, updates, etc. We also offer a contract version ([PDF format](https://nmap.org/oem/docs/Nmap-License-Contract.pdf), [editable MS Word document](https://nmap.org/oem/docs/Nmap-License-Contract.docx)) for companies who prefer a contract signed by both parties.

Licensees who wish to use Nmap on Windows should use our special Nmap OEM packages. Each release has a self-installer named nmap-VERSION-setup.exe and a zip package named nmap-VERSION-win32.zip. We recommend packaging the self-installer and then calling it in silent mode during your own installer's execution. This handles upgrades, dependencies (like Npcap and MS Visual C++ redistributable packages), registry setting, and so forth. But the zip option is also available for manual installation. Installation instructions for both package formats are [available here](https://nmap.org/book/inst-windows.html).

The Windows OEM packages can be found in [this distribution directory](https://nmap.org/oem/dist/?C=M&O=D). If you don't remember your company's username and password, please contact [sales@nmap.com](mailto:sales@nmap.com). Be sure to download the latest version unless you specifically require an older one. Note that updating Nmap to later versions requires a maintenance (support and upgrades) subscription. If you aren't sure whether you have an active maintenance subscription, email [sales@nmap.com](mailto:sales@nmap.com) and we'll check for you.

Nmap OEM licenses also include redistribution rights to our [Npcap OEM](https://npcap.com/oem/redist.html) Windows packet capturing and transmission software if you are only using it for Nmap. You only need to buy an Npcap OEM redistribution license if you want to use Npcap directly from your (non-Nmap) software. Npcap OEM is included with our Nmap OEM Windows builds and licensees with Nmap update rights also receive new Npcap OEM versions as they are released. This can be handy in case a licensee wants to ship a newer version of Npcap than the one which comes with Nmap, or if they just want to test new Npcap releases before they are integrated into Nmap. You can [download Npcap OEM here](https://npcap.com/oem/dist/) using your Nmap OEM download credentials.

Licensees distributing our official Linux or Mac OS X binary packages, or those who compile Nmap themselves on any platform, should [download the standard version of Nmap](https://nmap.org/download.html) instead. We do not currently supply official OEM builds on these platforms because the special features aren't very relevant on those platforms. Licensees may also install Nmap using third-party software repositors (such as using “apt-get nmap” on Ubuntu Linux or “yum install nmap” on Red Hat Linux. Keep in mind that third party software repositories do not always keep their Nmap packages up to date. Some of them are frequently years behind the latest Nmap releases.

The Nmap OEM program is mostly about a different license allowing for redistribution as well as commercial support and other benefits. The software itself is identical on most platforms, and even the special Windows OEM edition only differs in a few small ways such as the silent installer support and Npcap OEM inclusion. So Nmap OEM uses the standard (and extensive) Nmap documentation. The primary documentation is the Nmap book, [Nmap Network Scanning](https://nmap.org/book/), which is now available in its entirety for free online. It's also available through standard booksellers. Further documentation is available from the [Nmap documentation page](https://nmap.org/docs.html).

Licensees with an active maintenance (support and updates) subscription have special access to report bugs or ask Nmap technical support questions. If you are a licensee and don't have the support contact information, please email [sales@nmap.com](mailto:sales@nmap.com) and we will send it to you.

While we hope to set up an online order form for immediate purchase, we currently have a more manual process. To buy an Nmap OEM license, you or your preferred reseller should send a message to [sales@nmap.com](mailto:sales@nmap.com) with the following information:

1.   Your company name if it isn't obvious from your email address or email signature. We need the end user company name if you are a reseller.
2.   Which license you want. This depends on your current company size as [described here](https://nmap.org/oem/#licensing) and would be either the **Nmap OEM Enterprise Redistribution License**, **Nmap OEM Mid-Sized Company Redistribution License**, or **Nmap OEM Small/Startup Company Redistribution License**.
3.   If this is the **Enterprise Redistribution License**, the license covers a named product line or category. Please include the product line name or category that you are interested in shipping with Nmap OEM. This is not needed for the smaller company licenses since those companies usually have fewer products.
4.   Do you want the perpetual license or quarterly term license? The term license is paid every 3 months until you cease redistributing Nmap OEM and notify us of license termination. Companies choosing the quarterly license must either set up auto-payments or pay the automated invoices that we email to them. We can handle initial vendor onboarding for the term license, but not individual (per payment) purchase orders, enterprise payment portals, etc.
5.   If it's a perpetual license, do you want 5 years of updates and support (with a 20% prepayment discount) or 1 year of maintenance (with possible renewals later), or no maintenance at all? The term license always includes maintenance as part of the quarterly fee.

Once we receive your request, we will send a contract draft and formal quote with instructions for payment by wire transfer, ACH direct deposit, check, or PayPal. You can pay that directly or begin your company's procurement process for vendor onboarding, purchase order request, etc.

As soon as a contract is signed, we will activate your license and send you the following:

*   Account credentials for you and your team to download current and (if you purchased updates) future Nmap OEM and Npcap releases. We send these to everyone, but they are only needed if you will be shipping Nmap on the Windows OS. 
*   Contacts for submitting support requests (assuming you purchased support). Support includes bug reports as well as any technical questions you might have about Nmap. 

1.   **Is maintenance (support and updates) optional?**

For our normal (perpetual) license, maintenance is optional but highly recommended because it extends the perpetual license to include all new versions released during the maintenance period. And Nmap is under very active development. You can read about all our [recent performance improvements, feature enhancements, and bug fixes](https://nmap.org/changelog). Maintenance also includes commercial support whenever you need it as well as priority with new feature requests. And the price never increases as long as you don't let it lapse for more than 120 days.

For our quarterly term license, maintenance (including all updates and commercial support) is included along with redistribution rights in the single quarterly fee (which never increases).

2.   **Is the first year of maintenance included in the perpetual license fee?**

No. While we strongly recommend maintenance for the reasons given in the last question, some of our customs choose to decline even the first year of maintenance. Others choose the 5-year prepaid options for a 20% discount. Quoting the license and maintenance costs separately allows customers to buy exactly what they want.

3.   **Do you sell through resellers?**

Yes, we are happy to sell through your preferred reseller. We regularly work with [SoftwareONE](https://www.softwareone.com/), [SHI International](https://www.shi.com/), and dozens of others. Just ask your reseller to contact [sales@nmap.com](mailto:sales@nmap.com) on your behalf with the information requested in [Purchase Process](https://nmap.org/oem/#purchase).

4.   **Since Nmap on Windows requires the [Npcap packet capturing software](https://npcap.com/) do we also need to buy an [Npcap OEM redistribution license](https://npcap.com/oem/redist.html) to use with Nmap?**

No. All Nmap OEM contracts already include full rights to redistribute Npcap OEM or use it for testing/development **if Npcap is only being used with Nmap**. Npcap OEM is already included with the Windows executable Nmap OEM installer and the Nmap OEM Win32 Zip file. You can also download Npcap OEM using your Nmap OEM credentials as described in [the download section](https://nmap.org/oem/#download).

Please note that an Nmap OEM license does not confer distribution rights to use Npcap OEM with non-Nmap software. For that you would need the [Npcap OEM redistribution license](https://npcap.com/oem/redist.html), but at least you would receive an existing-customer discount. Please email [sales@nmap.com](mailto:sales@nmap.com) for details.

5.   **What are the standard license terms? What if they don’t work for us?**

Our standard license terms are available in the [license certificate we send to customers](https://nmap.org/oem/docs/Nmap-OEM-Software-Redistribution-License-Certificate.pdf) (filled out of course).

While many customers prefer our newer certificate approach because it's quicker and removes the need to review and sign a contract, others prefer a contract signed by both parties. Our standard Nmap OEM perpetual redistribution license contract template is available as a [PDF](https://nmap.org/oem/docs/Nmap-OEM-Software-Redistribution-License-Contract.pdf), or [editable MS Word version](https://nmap.org/oem/docs/Nmap-OEM-Software-Redistribution-License-Contract.docx). This is a different format (since both parties sign), but most of the actual license text and provisions are the same.

Our standard terms are quite generous and work as is for most of our customers. We provide indemnification and allow virtually unlimited use of the Npcap OEM technology in your covered products. We also provide source code in case you desire to make any changes or just better understand Npcap's workings. The agreements include a 6-month trial period during which you can terminate for any reason and receive a full refund of all money paid (including any maintenance fees).

When companies need very minor changes, we can normally accommodate them quickly by modifying the license certificate or contract. If your legal department wants to make many changes, the contract version is probably better. Please note that extensively marking up the contract will require significant legal review time on our side, and changes which substantially increase our obligations will increase the license fee too. Major markups are only allowed for the Mid-Sized or Enterprise license sizes. Customers interested in the Small/Startup license will have to limit themselves to a small number of minor changes or upgrade to the mid-sized license prices.

Some companies wish to use their own contract as a base instead of ours. While this is possible, it always increases the legal review time and the license cost. Redlining our standard contract is preferable.

6.   **What if Nmap OEM doesn't work out for us? Do you offer a trial license or a way to return it for a refund?**

Our [license certificate](https://nmap.org/oem/docs/Nmap-OEM-Software-Redistribution-License-Certificate.pdf) (Section 5.4) includes a 6-month period from the software delivery date during which you can cease redistributing Nmap OEM and request a full refund for any reason. Refunds include any maintenance fees already paid as well as any license fees, and they are provided within 30 days. So you don't lose a penny if you aren't happy with Nmap OEM or if the project you hoped to use it for doesn't pan out. Any licenses you have already granted to end users remain valid. While most customers choose our redistribution license certificate, the contract version of our licenses also includes this 6-month refund provision (see [license terms](https://nmap.org/oem/#faq-terms)).

We also offer the [free (non-OEM) version of Nmap](https://nmap.org/) for download and testing. While this version doesn't allow redistribution within commercial products and lacks some convenience features of Nmap OEM (such as the silent installer), it can be helpful for pre-purchase functionality testing since most of its functionality is identical.

7.   **Are there any limits or extra fees based on how many copies of Nmap OEM we redistribute or install?**

No. You can distribute and install as many copies of Nmap OEM as you wish as part of products covered by your license for no additional fees.

8.   **If our company size increases to a higher tier, or if Nmap prices go up in general, will we have to pay more?**

No. The optional annual maintenance fee for perpetual licenses and the quarterly license fee for term licenses are set based on your company size and the current prices at the time you buy the license. They don't increase for as long as you choose to renew.

9.   **My company is huge, but only 5 people are on the development team for the product which needs Nmap. Can we qualify for the startup rate?**

No. The license tiers are based on the whole company (or parent company) size. This is because large companies often have the financial and market power to leverage far more value out of Nmap than a tiny company can, even when the development team sizes for an individual product are similar.
