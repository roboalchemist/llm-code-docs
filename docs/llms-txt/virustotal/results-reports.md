# Source: https://virustotal.readme.io/docs/results-reports.md

# Reports

Here are the key elements of VirusTotal reports. We'll look at a typical URL report first, then a typical report for files. The last two sections will focus on domain and IP address reports.

[URL Report Summary](#url-report-summary)\
[URL Report Details](#url-report-details)\
[File Report Summary](#file-report-summary)\
[File Report Details](#file-report-details)\
[Domain and IP address reports](#domain-and-ip-address-reports)

# URL report summary

***

![URL Reports summary](https://storage.googleapis.com/vtdocresources/guides/ioc-reputation-enrichment/reports_urlsummary_20231114.png)

After your URL is scanned, you'll see a report that looks like this. Note that this is a sample report and does not reflect the actual ratings of any of the vendors listed. We've numbered the elements in the screenshot above for easy reference. They are:

**1)** The total number of VirusTotal partners who consider this url harmful (in this case, 0) out of the total number of partners who reviewed the file (in this case, 66).

**2)** The URL you scanned. Note that the URL may not match exactly your submission, this is because we canonicalize URLs, i.e. we normalize them in order to make sure that different variations of the same URL do not affect its detections.

**3)** The link to the domain repo which this url belongs to.

**4)** The date and time (UTC) of the review.

**5)** Content type of the resource analysed. For example: html, xml, flash, fla, iecookie, bittorrent, email, outlook, cap.

**6)** Favicon from the domain that belongs to the url scanned.

**7)** You can reanalyse the URL to get an updated report. URLs statuses are updated frequently by VirusTotal as they are distributed by antivirus companies.

**8)** Explore the URL VirusTotal Graph.

**9)** Search for the URL in VirusTotal Intelligence.

**10)** The reputation of the given URL as determined by VirusTotal's Community (registered users). Users sometimes vote on files and URLs submitted to VirusTotal, these users in turn have a reputation themselves, the *community score* condenses the votes performed on a given item weighted by the reputation of the users that casted these votes. Negative (red) scores indicate maliciousness, whereas positive (green) scores reflect harmlessness. The higher the absolute number, the more that you may trust a given score.

# URL report details

***

![URL Reports details](https://storage.googleapis.com/vtdocresources/guides/vt-intelligence/reports_urldetails_20240213.png)

**1)** A list of each reviewing partner and their findings. Possible findings include:

* Clean site: no malware detected.
* Unrated site: the partner never reviewed the given site.
* Malware site: distributes malware.
* Phishing site: the site tries to steal users' credentials.
* Malicious site: the site contains exploits or other malicious artifacts.
* Suspicious site: the partner thinks this site is suspicious. Grey area.
* Spam site: involved in unsolicited email, popups, automatic commenting, etc.

**2)** Additional information about the scanned resource, such as the category of its content, the HTTP response headers returned by the server upon asking for the given URL, etc.

**3)** VirusTotal's backend generates rich relationships: URLs from which a file has been downloaded, whether a given file been seen contained in some other files, what are the parents of a given Portable Executable, domain to IP address mappings over time, etc. *(Feature available only to [Enterprise](http://virustotal.com/go/vt-services-catalog) customers)*

**4)** VirusTotal allows you to perform a comprehensive analysis of a specific URL, extracting crucial information to understand its operation and content. *(Feature available only to [Enterprise](http://virustotal.com/go/vt-services-catalog) customers)*

**5)** Content of the URL: Strings content extracted from the html file. *(Feature available only to [Enterprise](http://virustotal.com/go/vt-services-catalog) customers)*

**6)** Details about the URL telemetry. *(Feature available only to [Enterprise](http://virustotal.com/go/vt-services-catalog) customers)*

**7)** These are comments made by members of the VirusTotal Community. Most recent comments are listed first. This section also records the votes made by members of the VirusTotal Community on this file or URL.

# File report summary

***

When you scan a file or search for a file given its hash, you'll see a report that looks like this:

![File Reports summary](https://storage.googleapis.com/vtdocresources/guides/ioc-reputation-enrichment/reports_filesummary_20231114.png)

Again, this report is a sample only and does not reflect the actual ratings of any vendor listed. And again we have numbered the most characteristic elements in the screenshot above for reference. They are:

**1 and 2)** The total number of VirusTotal partners who consider this file harmful (in this case, 44) out of the total number of partners who reviewed the file (in this case, 60).

**3)** The reputation of the given URL as determined by VirusTotal's Community (registered users). Users sometimes vote on files and URLs submitted to VirusTotal, these users in turn have a reputation themselves, the *community score* condenses the votes performed on a given item weighted by the reputation of the users that casted these votes. Negative (red) scores indicate maliciousness, whereas positive (green) scores reflect harmlessness. The higher the absolute number, the more that you may trust a given score.

**4)** SHA-256 (a cryptographic hash function) is a unique way to identify a file and used in the security industry to unambiguously refer to a particular threat. For more info see:

<https://en.wikipedia.org/wiki/Cryptographic_hash_function>

<https://en.wikipedia.org/wiki/SHA-2>

**5)** File name of last submission, and access to search by file names.

**6)** Tags.

**7)** The date and time (UTC) of the review.

**8)** Icon for the file type.

**9)** Button to reanalyse the file.

**10)** Search for similar files. *(Feature available only to [Enterprise](http://virustotal.com/go/vt-services-catalog) customers)*

**11)** Download sample. *(Feature available only to [Enterprise](http://virustotal.com/go/vt-services-catalog) customers)*

**12)** Explore the file in VirusTotal Graph.

# File report details

***

![File Reports details](https://storage.googleapis.com/vtdocresources/guides/ioc-reputation-enrichment/reports_filedetails_20231114.png)

**1)** A list of each reviewing partner and their findings. Possible findings are:

* Undetected: The given engine does not detect the file as malicious.
* Suspicious:  The given engine flags the file as suspicious.
* Unable to process file type: The given engine does not understand the type of file submitted and so will not produce verdicts for it.
* Timeout: The given engine reached VirusTotal's time execution limit when processing the file and so no verdicts were recorded for it.

**2)** Displays more information about the item being reviewed. For instance, for an Office document file this might list VBA code streams seen in document macros and other file type specific information. Similarly, VirusTotal specific metadata such as first submission and last submission dates, upload file names, etc are also recorded in this section.

**3)** VirusTotal's backend generates rich relationships: URLs from which a file has been downloaded, whether a given file been seen contained in some other files, what are the parents of a given Portable Executable, domain to IP address mappings over time, etc.

**4)** The samples submitted to VirusTotal get executed automatically in a controlled (sandboxed) environment and the actions performed are recorded in order to give the analyst a high level overview of what the sample is doing.

**5)** Content of the file: Strings and hexadecimal content extracted from the file. Preview of the full content is available depending of the filetype(pdf, docx, etc) *(Feature available only to [Enterprise](http://virustotal.com/go/vt-services-catalog) customers)*

**6)** Detailed listing about the submissions of this file with information like origin countries and dates. *(Feature available only to [Enterprise](http://virustotal.com/go/vt-services-catalog) customers)*

**7)** These are comments made by members of the VirusTotal Community. Most recent comments are listed first. This section also records the votes made by members of the VirusTotal Community on this file or URL.

**8)** List of Analyses with the detections evolution and the option to click on Previous Analyses. *(Feature available only to [Enterprise](http://virustotal.com/go/vt-services-catalog) customers)*

**9)** Copy detections as plain text to the clipboard. *(Feature available only to [Enterprise](http://virustotal.com/go/vt-services-catalog) customers)*

# Domain and IP address reports

***

Unlike file and URL reports, network location views do not record partner verdicts for the resource under consideration. Instead, these reports condense all of the recent activity that VirusTotal has seen for the resource under consideration, as well as contextual information about it. These details include:

* Autonomous System and location country for IP addresses.
* Passive DNS replication information: all the IP-domain name mappings that VirusTotal has seen over time for the item being studied. These resolutions are performed when contacting URLs submitted to VirusTotal for scanning, when executing files in sandboxes, through partnerships with third-parties, etc.
* Whois lookups: registered users or assignees of an Internet resource, such as a domain name, an IP address block, or an autonomous system, but is also used for a wider range of other information.
* Observed subdomains: domains seen hierarchically under another domain stored in VirusTotal.
* Sibling domains: domains at the same hierarchical level as the domain being studied.
* URLs: latest URLs seen under the domain or IP address being studied. Note that the date reflected in this section is not the date at which the URL was contacted but rather the date of the last report that we have for the resource, this might be more recent or older than the retrieval date.
* Downloaded files: latest files that have been retrieved from URLs sitting at the domain or IP address under study. Note that the date recorded in this section is not the date at which the file was downloaded but rather the date of the last report that we have for the resource.
* Communicating files: latest files that, through their execution in a sandboxed virtual environment, have been seen to perform some kind of communication with the IP address or domain under consideration. Note that the date recorded in this section is not the date at which the communication took place but rather the date of the last report that we have for the resource.
* Files referring: VirusTotal will inspect the strings contained in files submitted to the service and apply certain regular expressions to these in order to identify domains and IP addresses. This section records files that have referenced the domain or IP address under consideration. Note that the date recorded in this section is not the date at which the file that give raise to the relationship was submitted but rather the date of the last report that we have for the resource.