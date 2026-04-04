# Source: https://virustotal.readme.io/reference/api-v2-v3-migration-guide.md

# API v2 to v3 Migration Guide

# API v3 Migration Guide

[comment]: # "Intro"

Welcome to our VirusTotal API v2 to v3 migration guide. In this documentation you will find all the details on what’s new in API v3, why to migrate and how to do so in the smoothest way. We also included examples for everything. Let’s get started!

[comment]: # "Benefits"

## Why use VT API v3?

The migration guide describes in detail most API v3 benefits, including:

* **Endpoints for all VirusTotal products and scanners**. VT users can access all of VirusTotal’s tools through a single API, simplifying the integration process.
* **User and group management** helping administrators to automate managing access and accounts, as well as tracking usage across your team.
* **Extra relevant information for file, URL, domain and IP reports**. VT API v3 provides additional information for all file, URL, domain and IP reports, including metadata and context.
* **REST-based, with predictable, resource-oriented URLs**. VirusTotal API v3 uses a RESTful architecture, following a standard set of design principles for building web services with HTTP methods accessed through predictable, resource-oriented URLs, making it easier to use and integrate with other tools.
* **MITRE related tactics and techniques seen in file behavior**. API v3 provides information on TTPs used by malware samples, as defined by the MITRE ATT\&CK framework. This helps understanding the potential impact of a sample and how to respond to any threats.
* **More extensive [documentation](https://developers.virustotal.com/reference/overview) and code [examples](https://github.com/VirusTotal/vt-py/tree/master/examples) based on the Python module**. V3 has more extensive documentation and code examples which make it easier for users to get started with the API and integrate it into their workflows.

[comment]: # "Differences"

## Migrating to V3

Migrating from v2 to v3 shouldn’t be painful. Here we highlight all the relevant differences to consider during the migration process.

### Endpoints

The first difference is the URL prefix shared by the endpoints:

| VT API v2                                                           | VT API v3                                                       |
| ------------------------------------------------------------------- | --------------------------------------------------------------- |
| [www.virustotal.com/vtapi/v2/](http://www.virustotal.com/vtapi/v2/) | [www.virustotal.com/api/v3/](http://www.virustotal.com/api/v3/) |

VT API v3 provides many more endpoints than v2 as it covers more use cases. You can find the complete list of v3 endpoints in the official documentation [here](https://developers.virustotal.com/reference/overview).

To assist migration initiatives, the table below shows v2 - v3 endpoint correspondence.

[comment]: # "BigTable"

<table >
<thead>
  <tr>
    <th ><span style="font-weight:bold">Description</span></th>
    <th ><span style="font-weight:bold">VT API v2</span></th>
    <th ><span style="font-weight:bold">VT API v3</span></th>
  </tr>
</thead>
<tbody>
  <tr> 
    <td colspan="3" style="text-align: center"><span><b><a href="https://github.com/VirusTotal/vt-use-cases/blob/main/API%20v2-v3%20Migration%20Guide.md#set1v" target="_blank">Submitting samples, getting file reports, and rescanning files</a></b></span></td>
  </tr>
  <tr>
    <td ><span><b>Submit file (<= 32MB)</b></span></td>
    <td ><a href="https://developers.virustotal.com/v2.0/reference/file-scan" target="_blank">/file/scan</a></td>
    <td ><a href="https://developers.virustotal.com/reference/files-scan" target="_blank">/files</a></td>
  </tr>
  <tr>
    <td ><span><b>Submit file(> 32MB)</b></span></td>
    <td >/<a href="https://developers.virustotal.com/v2.0/reference/file-scan-upload-url" target="_blank">file/scan/upload_url</a> and <a href="https://developers.virustotal.com/v2.0/reference/file-scan" target="_blank">/file/scan</a></td>
    <td ><a href="https://developers.virustotal.com/reference/files-upload-url" target="_blank">/files/upload_url</a> and <a href="https://developers.virustotal.com/reference/files-scan" target="_blank">/files</a></td>
  </tr>
  <tr>
    <td ><span><b>Get file report</b></span></td>
    <td ><a href="https://developers.virustotal.com/v2.0/reference/file-report" target="_blank">/file/report</a> (allinfo parameter)</td>
    <td ><a href="https://developers.virustotal.com/reference/file-info" target="_blank">/files/{id}</a></td>
  </tr>
  <tr>
    <td ><span><b>Rescan file</b></span></td>
    <td ><a href="https://developers.virustotal.com/v2.0/reference/file-rescan" target="_blank">/file/rescan</a></td>
    <td ><a href="https://developers.virustotal.com/reference/files-analyse" target="_blank">/files/{id}/analyse</a></td>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center"><span><b><a href="https://github.com/VirusTotal/vt-use-cases/blob/main/API%20v2-v3%20Migration%20Guide.md#set2" target="_blank">Getting file behaviour reports and downloading network traffic files</a></b></span></td>
  </tr>
  <tr>
    <td ><span><b>Get file behavior report</b></span></td>
    <td ><a href="https://developers.virustotal.com/v2.0/reference/file-behaviour" target="_blank">/file/behaviour</a></td>
    <td ><a href="https://developers.virustotal.com/reference/get-all-behavior-reports-for-a-file" target="_blank">/files/{id}/behaviours</a> and <a href="https://developers.virustotal.com/reference/get-file-behaviours-html" target="_blank">/file_behaviours/{sandbox_id}/html</a></td>
  </tr>
  <tr>
    <td ><span><b>Download PCAP</b></span></td>
    <td ><a href="https://developers.virustotal.com/v2.0/reference/file-network-traffic" target="_blank">/file/network-traffic</a></td>
    <td ><a href="https://developers.virustotal.com/reference/get-file-behaviours-pcap" target="_blank">/file_behaviours/{sandbox_id}/pcap</a></td>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center"><span><b><a href="https://github.com/VirusTotal/vt-use-cases/blob/main/API%20v2-v3%20Migration%20Guide.md#set3" target="_blank">Scanning URLs, getting reports for URLs, domains, and IP addresses</a></b></span></td>
  </tr>
  <tr>
    <td ><span><b>Scan URL</b></span></td>
    <td ><a href="https://developers.virustotal.com/v2.0/reference/url-scan" target="_blank">/url/scan</a></td>
    <td ><a href="https://developers.virustotal.com/reference/scan-url" target="_blank">/urls</a></td>
  </tr>
  <tr>
    <td ><span><b>Get URL report</b></span></td>
    <td ><a href="https://developers.virustotal.com/v2.0/reference/url-report" target="_blank">/url/report</a></td>
    <td ><a href="https://developers.virustotal.com/reference/url-info" target="_blank">/urls/{id}</a></td>
  </tr>
  <tr>
    <td ><span><b>Get domain report</b></span></td>
    <td ><a href="https://developers.virustotal.com/v2.0/reference/domain-report" target="_blank">/domain/report</a></td>
    <td ><a href="https://developers.virustotal.com/reference/domain-info" target="_blank">/domains/{domain}</a></td>
  </tr>
  <tr>
    <td ><span><b>Get IP address report</b></span></td>
    <td ><a href="https://developers.virustotal.com/v2.0/reference/ip-address-report" target="_blank">/ip-address/report</a></td>
    <td ><a href="https://developers.virustotal.com/reference/ip-info" target="_blank">/ip_addresses/{ip}</a></td>
  </tr>  
  <tr>
    <td colspan="3" style="text-align: center"><span><b><a href="https://github.com/VirusTotal/vt-use-cases/blob/main/API%20v2-v3%20Migration%20Guide.md#set4" target="_blank">Feeds for enrichment</a></b></span></td>
  </tr>
  <tr>
    <td ><span><b>Get file feed</b></span></td>
    <td ><a href="https://developers.virustotal.com/v2.0/reference/file-feed" target="_blank">/file/feed</a></td>
    <td ><a href="https://developers.virustotal.com/reference/feeds-file" target="_blank">/feeds/files/{time}</a> and <a href="https://developers.virustotal.com/reference/feeds-file-hourly" target="_blank">/feeds/files/hourly/{time}</a></td>
  </tr>
  <tr>
    <td ><span><b>Getting URL feed</b></span></td>
    <td ><a href="https://developers.virustotal.com/v2.0/reference/url-feed" target="_blank">/url/feed</a></td>
    <td ><a href="https://developers.virustotal.com/reference/feeds-url" target="_blank">/feeds/urls/{time}</a> and <a href="https://developers.virustotal.com/reference/feeds-url-hourly" target="_blank">/feeds/urls/hourly/{time}</a></td>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center"><span><b><a href="https://github.com/VirusTotal/vt-use-cases/blob/main/API%20v2-v3%20Migration%20Guide.md#set5" target="_blank">Getting file clusters and downloading files</a></b></span></td>
  </tr>
  <tr>
    <td ><span><b>Get file clusters</b></span></td>
    <td ><a href="https://developers.virustotal.com/v2.0/reference/file-clusters" target="_blank">/file/clusters</a></td>
    <td ><a href="https://developers.virustotal.com/reference/statsvhash_clusters" target="_blank">/stats/vhash_clusters</a></td>
  </tr>
  <tr>
    <td ><span><b>Download file</b></span></td>
    <td ><a href="https://developers.virustotal.com/v2.0/reference/file-download" target="_blank">/file/download</a></td>
    <td ><a href="https://developers.virustotal.com/reference/files-download" target="_blank">/files/{id}/download</a></td>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center"><span><b><a href="https://github.com/VirusTotal/vt-use-cases/blob/main/API%20v2-v3%20Migration%20Guide.md#set6" target="_blank">VT Intelligence via API</a></b></span></td>
  </tr>
  <tr>
    <td ><span><b>Advanced search</b></span></td>
    <td ><a href="https://developers.virustotal.com/v2.0/reference/file-search" target="_blank">/file/search</a> (only for files)</td>
    <td ><a href="https://developers.virustotal.com/reference/intelligence-search" target="_blank">/intelligence/search</a></td>
  </tr>
</tbody>
</table>

#### Endpoint request

When it comes to requests the main difference is how the API key is sent to the server and the way that resources or entities are referenced. In v2, both the API key and the endpoint references are included in the request parameters, ‘params’. This means that for GET requests, the API key could potentially be exposed to unauthorized parties if the query is intercepted or logged by network monitoring tools or third-party services.

```python
# API v2 - Python GET and POST requests example
params = {'apikey':VT_API_KEY, 'query': query}
response = requests.get(url, params=params)
response = requests.post(url, params=params)
```

API v3 follows REST principles, using predictable resource-oriented URLs that include objects in the URL and specify the API key in the headers. This approach helps to avoid the problem of potentially exposing the API key in GET requests, as was the case with v2.

```python
# API v3 - Python GET and POST requests example
headers = {'accept': 'application/json', 'x-apikey': VT_API_KEY}
response = requests.get(url, headers=headers)
response = requests.post(url, headers=headers)
```

#### Endpoint response

In terms of the responses provided by the server, the approach between API v2 and API v3 is slightly different.

v3 follows the conventional HTTP response codes to indicate success or failure while v2 revolves around the fact that the request was correctly handled by the server. In v2 the existence or availability of the data requested is handled through other parameters in the response, not necessarily through the HTTP status code.

The table below shows different server responses when the object requested doesn't exist in the VirusTotal dataset.

<table >
<thead>
  <tr>
    <th ></th>
    <th ><span style="font-weight:bold">VT API v2</span></th>
    <th ><span style="font-weight:bold">VT API v3</span></th>
  </tr>
</thead>
<tbody>
  <tr>
  	<td colspan="3" style="text-align: center"><span><b>Resource Not Available Yet</b></span></td>
  </tr>
  <tr>
    <td ><span><b>Status</b></span></td>
    <td >200</td>
    <td >400</td>
  </tr>
  <tr>
    <td ><span><b>Response json parameter</b></span></td>
    <td ><span>response_code = 0</span></td>
    <td ><span>error.code = NotAvailableYet</span></td>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center"><span><b>Resource Not Found</b></span></td>
  </tr>
  <tr>
    <td ><span><b>Status</b></span></td>
    <td >200</td>
    <td >404</td>
  </tr>
  <tr>
    <td ><span><b>Response json parameter</b></span></td>
    <td ><span>response_code = -2</span></td>
    <td ><span>error.code = NotFoundError</span></td>
  </tr>
</tbody>
</table>

More details are available in the official documentation: [API v2 responses](https://developers.virustotal.com/v2.0/reference/api-responses), [API v3 responses](https://developers.virustotal.com/reference/api-responses) and [API V3 Errors](https://developers.virustotal.com/reference/errors).

### Basic concepts on data formats

When it comes to data around threats, VirusTotal API v3 provides much more information than v2. v3 introduces new concepts to better structure and handle the data:

* **[Objects](https://developers.virustotal.com/reference/objects)** - An object is any item that can be retrieved or manipulated via API. Every object has a type and an identifier, and the (identifier, type) tuple is unique. The most common object types include 'file', 'url', 'domain' and 'ip' but there are many more depending on the endpoint, such as 'comment', 'graph', 'user', 'submission', 'vote', 'resolution', 'sigma\_rule', 'attack\_technique', 'collection', etc. You can find the type for every object listed on the '**API OBJECTS**' menu on the API v3 official [documentation](https://developers.virustotal.com/reference/overview).

* **[Collections](https://developers.virustotal.com/reference/collections)** - These are sets of objects, usually of the same type. This **concept** should not be confused with the [collection](https://developers.virustotal.com/reference/collections-1) **object** whose type name is also 'collection' and also available only in v3 - for more context refer to this [post](https://blog.virustotal.com/2022/09/vt-collections-citius-altius-fortius.html).

* **[Relationships](https://developers.virustotal.com/reference/relationships)** - This is how VirusTotal API links objects between them. Relationships can exist between objects of the same or different type, and can be 1:1 or 1:N, depending on whether the object is related to a single object or to multiple objects. Relationships are one of the most powerful and representative concepts since they show the full picture of a threat campaign. They also allow enriching a specific object with contextual data from related IOCs.

[VirusTotal Intelligence](https://virustotal.readme.io/docs/virustotal-intelligence-introduction) considers all objects belonging to any of the following five entities: **[file](https://virustotal.readme.io/docs/files)**, **[URL](https://virustotal.readme.io/docs/url-object)**, **[domain](https://virustotal.readme.io/docs/domains-object)**, **[IP](https://virustotal.readme.io/docs/ip-object)** addresses and **[collection](https://virustotal.readme.io/docs/collections-object)**. The **entity** search modifier can be used as part of the v3 [`/intelligence/search`](https://virustotal.readme.io/reference/intelligence-search) endpoint along with any other modifiers. This helps filter results to a particular entity (i.e. **entity:file**). The default entity for any VTI query is 'file'. In v2 the advanced corpus search endpoint ([`/reference/file-search`](https://docs.virustotal.com/v2.0/reference/file-search)) is only available for files.

Focusing on **file** objects, v3 provides much more detailed data than v2 including crowdsourced YARA, Sigma and IDS rules matching the sample, different similarity hashes (including favicon dhash and Tlsh hash among others), popular threat classification, [Detect-It-Easy](https://github.com/horsicq/Detect-It-Easy) data, submissions and scans history, Mach-O and ELF file info, and much more.

Also v2 no longer supports dynamic analysis data through sandbox detonation. In v3 you can find details on sandbox malware detection and classification, services and processes activity, file manipulation, dynamically loaded modules, synchronization mechanisms such as mutexes, commands execution, registry key manipulation, network traffic and detected MITRE TTPs. v2 does not allow downloading artifacts such as memory dump or system events files, available in v3.

When it comes to **URLs** v3 provides extra information on top of the info provided by v2, including associated threat names, number of votes and reputation ratio, web page title, and much more.

The same happens with **domains**. v3 provides additional data such as the entire list of AV detections, votes, popularity ranks, HTTPS certificate, and other relation-based data.

For **IP addresses**, v3 includes data regarding the last HTTPS certificate, whois lookup, detection ratio and the entire list of AV detections, network mask, tags, number of votes and reputation ratio, among other extra features.

### Libraries

Both API versions include several modules in several programming languages, to be integrated with different technologies. Client libraries and third party scripts are available and can be checked in the official documentation: [API Scripts and client libraries](https://virustotal.readme.io/docs/api-scripts-and-client-libraries).

As these are probably two of the most used ones, here you can find our libraries for [Go](https://github.com/VirusTotal/vt-go) and [Python](https://github.com/VirusTotal/vt-py). A library for Java is in progress and will be available very soon.

### Integration with other VT products and features

Every single service in VirusTotal is fully compatible with API v3. This is not necessarily true for v2.

Also please note that some endpoints related to specific products require additional privileges. Not all of them are included in the standard package.

#### VirusTotal Feeds

While v2 is available for file and URL feeds, v3 is ready for all feed formats provided by VirusTotal, including [File Behaviors](https://developers.virustotal.com/reference/file-behaviours), [Domains](https://developers.virustotal.com/reference/domains-4) and [IP addresses](https://developers.virustotal.com/reference/ip-addresses-1) feeds in addition to the [Files](https://developers.virustotal.com/reference/files-2) and [URLs](https://developers.virustotal.com/reference/urls-1) feeds.

File Behaviors feeds, available only in v3, provide a way of downloading artifacts such as OS events or EVTXs, memory dumps, network traffic events or PCAPs and low level reports as well as MITRE tactics and techniques.

#### VirusTotal Private Scanning

API v3 allows you to automate the process of scanning files that can’t be shared with the community via [Private Scanning](https://developers.virustotal.com/reference/private-files-6).

This service provides only v3 endpoints for submitting files, rescanning them, getting the list of private files, their reports and objects related to them and also download dynamic analysis artifacts and behavior reports related to those private samples. For more context on this service, refer to this [documentation](https://virustotal.readme.io/docs/private-scanning).

### VirusTotal Hunting

API v3 has introduced a way to interact with VT Hunting services: [Retrohunt](https://developers.virustotal.com/reference/retrohunt) and [Livehunt](https://developers.virustotal.com/reference/livehunt).

For **Retrohunt**, there are endpoints to search for, create, delete and abort retro-hunt jobs and get the list of files matching the supplied YARA rule.

For **Livehunt**, there are endpoints to search for, create, delete and update YARA rules, and for managing several user and group permissions.

### VirusTotal Alerts

Only API v3 provides interaction capabilities with [VirusTotal Alerts](https://developers.virustotal.com/reference/overview-1), a service for notifying every detection in VirusTotal matching IP addresses, domains or intellectual property included by the user on a watchlist.

Watchlists can be managed by including or removing assets, and notifications can be checked by getting the related alerts that then can be integrated with security monitoring tools in an automated way.

### VirusTotal Graphs

API v3 has introduced a way to search, create, manipulate and delete graphs from VT Graph.

Users and groups access to and manipulation of graphs privileges can be managed and comments on graphs can be checked and created, based on user account privileges.

Available endpoints can be checked in the official documentation [UNIVERSAL API ENDPOINTS -> Graphs](https://developers.virustotal.com/reference/graphs).

### VirusTotal Threat Landscape

API v3 provides interaction with the VirusTotal Threat Landscape through [Collections](https://developers.virustotal.com/reference/collections-5) and [Threat Actors](https://developers.virustotal.com/reference/list-threat-actors) objects.

For collections, only v3 provides endpoints to search for, create, delete and update them, and for collection comments management.

On the other hand, for threat actors, it exposes endpoints to search for specific threat actors or get the entire list of them and other objects related to them. As with collections, there’s no option for v2 to interact with threat actors.

### VirusTotal Augment

The [VirusTotal Augment](https://developers.virustotal.com/reference/widget-overview) widget is an official, compliant and recommended way of incorporating VirusTotal data in third-party applications through a bring-your-own-api-key model. It is a ready to use threat enrichment tool that can be used with all sorts of web based consoles.

Only API v3 allows you to interact with VT Augment:

* For getting a widget rendering URL
* For getting the widget's HTML content

### VirusTotal Monitor

Only API v3 provides access to [VirusTotal Monitor](https://developers.virustotal.com/reference/monitor), which is designed to analyze new samples of goodware, providing early detection of false positives to antivirus companies and software developers.

Even though VT Monitor **is no longer maintained**, the API integration is still active.

### Users and Groups

A highly requested feature not available in API v2 is management for [users and groups](https://developers.virustotal.com/reference/users-groups).

API v3 allows you to see users and groups definition, get other objects related to them, update and delete them. User privileges manipulation, inclusion and exclusion from a group is possible via API and there are also endpoints to check groups and users consumption.

Please note that some endpoints require admin privileges.

[comment]: # "Conclusion"

As a final note, probably the main advantage that API v3 has over v2 is that API v3 is our new VirusTotal’s standard, and some day in the future we will have to sunset v2.