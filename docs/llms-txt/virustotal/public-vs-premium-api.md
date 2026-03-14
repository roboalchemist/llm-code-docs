# Source: https://virustotal.readme.io/reference/public-vs-premium-api.md

# Public vs Premium API

While many of the endpoints and features provided by the VirusTotal API are freely accessible to all registered users, many are restricted to our premium customers only. Those endpoints and features constitute the VirusTotal Premium API and they will be appropriately identified in this reference. If you are interested in using our Premium API please [contact us](https://www.virustotal.com/gui/contact-us/premium-services).

The premium API is a component of [VirusTotal's advanced services for professionals](https://www.virustotal.com/gui/services-overview).

The Public API, on the other hand, is a set of endpoints available for everyone to use at no cost. The only thing you need in order to use the Public API is to sign up to VirusTotal Community and obtain your API key as described in [Getting started](https://virustotal.readme.io/reference/getting-started).

> ❗️ Public API constraints and restrictions
>
> The Public API is limited to **500 requests per day and a rate of 4 requests per minute**.\
> The Public API **must not** be used in commercial products or services.\
> The Public API **must not** be used in business workflows that do not contribute new files.\
> You are not allowed to register multiple accounts to overcome the aforementioned limitations.

> 📘 Premium API highlights
>
> The Premium API does not have request rate or daily allowance limitations, limits are governed by your licensed service step.\
> The Premium API returns more threat context and exposes advanced threat hunting and malware discovery endpoints and functionality.\
> The Premium API is governed by an SLA that guarantees readiness of data.

The Premium API powers the following **popular use cases**:

* Automatic **security telemetry (alerts/events) enrichment** leading to alert triage, threat intelligence driven orchestration and proactive threat hunting.
* Full characterization of **any kind of threat campaign observable: files, hashes, URLs, domains, IPs, SSL Certificates, etc.**
* **Integration with SIEM, SOAR, EDR or AV for enrichment**, not detection, purposes. Achieving the single pane of glass epiphany.
* Implementation of **programmatic workflows** to assist in incident response, leading to faster, more accurate and more confident decisions.
* **Downloading of files for further study and dissection offline**, in in-house sandboxes, analysis pipelines, etc.
* **Automatic ingestion of YARA rule notifications** to build custom threat feeds, cover security stack blindspots and to derive IoCs that can be used to proactively neutralize threat campaigns.

Specifically, it has the following **advantages over the Public API**:

* Allows you to choose a request rate and daily quota allowance that best suits your needs.
* Enables you to download submitted samples for further research, along with the network traffic captures they generate upon execution and their detailed execution reports.
* Will return further details and context about the observables processed by VirusTotal, for instance: VBA code stream warnings for documents, source metadata, ExifTool output, IDS output for recorded network traces, domain popularity rankings, SSL certificates, etc.
* Includes metadata generated exclusively by VirusTotal: first submission date of a given file, list of file names with which a file was submitted to VirusTotal, submission countries, prevalence, etc.
* Will give you access to behavior information about files, produced by executing Windows PEs, DMGs, Mach-Os and APKs in a virtualized sandbox environment.
* Exposes whitelisting and [trusted source](http://blog.virustotal.com/2015/02/a-first-shot-at-false-positives.html) information.
* Allows you to perform property to sample queries: reverse searches such as *give me all samples that are detected with the following signature*, *give me all samples that are detected by more than 10 engines*, *give me all samples that contain a given PE section with the following hash*, etc. these search modifiers can be combined to build complex requests.
* Allows you to perform property to URL/domain/IP address queries: reverse searches such as *give me all domains registered by the same attacker*, *give me all domains with a DNS A record TTL lower than 5 seconds*, etc.
* Exposes file clustering and file similarity search calls.
* Exposes rich relationships that are not available in the Public API, e.g. embedded domains, embedded IP addresses, contacted domains, etc.
* Permits you to programmatically interact with [VT Hunting](https://www.virustotal.com/gui/hunting-overview), including retrieval of YARA rule notifications or automatic launching of retrohunt jobs. (Requires additional VTI subscription)
* Has a strict Service License Agreement (SLA) that guarantees availability and readiness of data.