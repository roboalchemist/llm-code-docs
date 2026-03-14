# Source: https://virustotal.readme.io/reference/overview.md

# VirusTotal API v3 Overview

> 🚧 Commonly missed
>
> **Looking for more API quota and additional threat context?**\
> [Contact us](https://www.virustotal.com/gui/contact-us/premium-services) to learn more about our [offerings for professionals](https://assets.virustotal.com/vt-360-outcomes.pdf) and try out the [VT ENTERPRISE](https://www.virustotal.com/gui/services-overview) Threat Intelligence Suite.
>
> **Looking for your VirusTotal API key?**\
> Jump to [your personal API key](https://www.virustotal.com/gui/my-apikey) view while signed in to VirusTotal. By the way, you might want to use it in conjunction with [VirusTotal's browser extension](https://blog.virustotal.com/2022/03/vt4browsers-any-indicator-every-detail.html) to automatically contextualize IoCs on interfaces of your choice.
>
> **Do you want to integrate into Splunk, Palo Alto Cortex XSOAR or other technologies?**\
> Enrich your security events, automatically triage alerts and boost detection confidence leveraging our ubiquitous integrations in 3rd-party platforms such as [Splunk SOAR](https://splunkbase.splunk.com/app/5865), [Splunk SIEM](https://splunkbase.splunk.com/app/6654), [XSOAR](https://cortex.marketplace.pan.dev/marketplace/?q=virustotal), [Crowdstrike](https://www.crowdstrike.com/resources/data-sheets/virustotal-integration/), [Chronicle SOAR](https://integrations.siemplify.co/doc/virustotal-v3) and others ([see more](https://developers.virustotal.com/reference/technology-integrations)).

API version 3 is now the default and encouraged way to programmatically interact with VirusTotal. It greatly improves [API version 2](https://developers.virustotal.com/v2.0/reference), which, for the time being, will not be deprecated. This new API was designed with ease of use and uniformity in mind and it is inspired in the <http://jsonapi.org/> specification.

This API follows the [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) principles and has predictable, resource-oriented URLs. It uses JSON for requests and responses, including errors.

While older API endpoints are still available and will not be deprecated, we encourage you to migrate your workloads to this new version. It exposes far richer data in terms of: IoC relationships, sandbox dynamic analysis information, static information for files, YARA Livehunt & Retrohunt management, crowdsourced detection details, etc.

## Most popular API endpoints

* [Upload a file for scanning](https://virustotal.readme.io/reference/files-scan): analysis your file with 70+ antivirus products, 10+ dynamic analysis sandboxes and a myriad of other security tools to produce a threat score and relevant context to understand it.
* [Get a file report by hash](https://virustotal.readme.io/reference/file-info): given a {md5, sha1, sha256} hash, retrieves the pertinent analysis report including threat reputation and context produced by 70+ antivirus products, 10+ dynamic analysis sandboxes and a myriad of other security tools and datasets.
* [Scan URL](https://virustotal.readme.io/reference/scan-url): analysis your URL with 70+ antivirus products/blocklists and a myriad of other security tools to produce a threat score and relevant context to understand it.
* [Get a URL analysis report](https://virustotal.readme.io/reference/url-info): given a URL, retrieves the pertinent analysis report including threat reputation and context produced by 70+ antivirus products/blocklists and a myriad of other security tools and datasets.
* [Get a domain report](https://virustotal.readme.io/reference/domain-info): given a domain, retrieves the pertinent analysis report including threat reputation and context produced by 70+ antivirus products/blocklists and a myriad of other security tools and datasets.
* [Get an IP address report](https://virustotal.readme.io/reference/ip-info): given an IP address, retrieves the pertinent analysis report including threat reputation and context produced by 70+ antivirus products/blocklists and a myriad of other security tools and datasets.