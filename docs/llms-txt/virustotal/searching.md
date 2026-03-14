# Source: https://virustotal.readme.io/docs/searching.md

# Searching

The search feature is free and available to any user. Every time a scan is requested by users, VirusTotal stores the analyses and report. This allows users to query for reports given an MD5, SHA1, SHA256 or URL and render them without having to resubmit the items (whether URLs or files) for scanning. VirusTotal also allows you to search through the comments that users have posted on files and URLs, inspect our passive DNS data, and retrieve threat intelligence details regarding domains and IP addresses.

The search functionality should not be used in commercial products or services. Additionally, this search feature should not be used as a programmatic interface to retrieve VirusTotal reports. We will ban any script using this interface as if it were an API. If you want to use VirusTotal's dataset programmatically, you should be looking at the [VirusTotal API](https://virustotal.readme.io/reference/overview).

If you are looking for more advanced search capabilities, VirusTotal also offers a premium service called VirusTotal Intelligence. Intelligence allows you to go from sample characteristics (such as antivirus detection names, size, file type, binary content, behaviour patterns or drive-by-download URLs) to a list of samples matching your criteria. These malware samples can be downloaded for further scrutiny. The VirusTotal Intelligence platform contains other features such as [YARA rule matching](https://virustotal.github.io/yara-x/) on VirusTotal's live submissions and sample clustering.

The VirusTotal search form allows you to search for file scan reports, URL scan reports, IP address information, domain information. You can also search the VirusTotal Community for users and comments.

# Searching for file scan reports

***

To search for the last VirusTotal report on a given file, just enter its hash. Currently the allowed hashes are MD5, SHA1 and SHA256.

![Searching for a hash](https://storage.googleapis.com/vtdocresources/guides/vt-intelligence/img/searching_hashsearch_20231117.png)

The most recent report is displayed, the historical evolution of files is available in [VirusTotal Intelligence](https://www.virustotal.com/gui/intelligence-overview).

# Searching for URL scan reports

***

![Searching for an URL](https://storage.googleapis.com/vtdocresources/guides/vt-intelligence/img/searching_urlsearch_20231117.png)

URL searches are simple: Type in the given URL, and the web application will normalize it and compare it with the items in VirusTotal's dataset and return the most recent report on it. Make sure the URL starts with the protocol, i.e. *http* or *https*.

# Searching for IP address information

***

VirusTotal runs its own passive DNS replication service, built by storing the DNS resolutions performed as we visit URLs and execute malware samples submitted by users. To retrieve the information we have on a given IP address, just type it into the search box.

This report includes other details, such as all the incidents related to the IP address: malware samples downloaded from the given server, files or other IPs and URLs communicating with it, etc.

# Searching for domain information

***

To retrieve the information we have on a given domain just type the domain in the search box. This report includes several details, such as all the incidents seen related to the domain: malware samples downloaded from the given domain, files or other IPs and URLs communicating with it, etc.

![Searching for a domain](https://storage.googleapis.com/vtdocresources/guides/vt-intelligence/img/searching_domainsearch_20231117.png)

# Searching for VirusTotal Community users

***

To find the profile page for any VirusTotal Community member, go to the search box and enter their nickname preceded by the "@" symbol. For example: @VirusTotalTeam.

![Searching for an user](https://storage.googleapis.com/vtdocresources/guides/vt-intelligence/img/searching_usersearch_20231117.png)