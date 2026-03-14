# Source: https://virustotal.readme.io/docs/private-scanning.md

# Private Scanning

**TL;DR: *See files or URLs through the eyes of VirusTotal without uploading them to the main threat corpus, in other words, without sharing with other VirusTotal users or distributing them beyond your organization. Static, dynamic, network and similarity analysis included for files, as well as automated threat intel enrichment, but it will NOT contain our multi-antivirus or url-scan partners verdicts.***

> ⚠️ **IMPORTANT OBSERVATIONS!**
> Private Scanning does not replace VirusTotal's standard upload experience, you must use the [Private Scanning form](https://www.virustotal.com/gui/private-scanning/.) to keep uploads private. When using Private Scanning:
>
> * Submitted files and URLs do not abandon VirusTotal's infrastructure.
> * All tools acting on the submitted files and URLs run on VirusTotal infrastructure.
> * Submitted files and URLs are not shared with third parties, unless the file or URL is also uploaded to the standard VirusTotal service in addition to Private Scanning.
> * Submitted files and URLs are permanently deleted from our private buckets after their retention period expires (usually 24 hours, although the default value can be set in your organization's Private Scanning preferences).
> * **Analysis reports for submitted files and URLs are only visible to users within your organization (VirusTotal group) and are also permanently deleted after their retention period expires.**
>
> Note that Private Scanning is not meant to substitute VirusTotal's standard crowdsourced community, but rather complement it in very specific and justified instances in which certain files or URLs can't be shared with security vendors and other industry peers. **If Private Scanning clearly suggests that a file or URL is malicious, we encourage you to upload it to [standard VirusTotal](https://www.virustotal.com/) in order to share the threat and its context with other defenders.**

Private Scanning allows you to analyze files and URLs with VirusTotal in a privacy preserving fashion. Files and URLs uploaded via this offering won't be shared with anyone beyond your organization, and will remain in VirusTotal only for a brief period of time. The resulting analyses will be ephemeral too and only visible to your VirusTotal group.

Note that private analyses won't contain antivirus verdicts, they will contain only the output of all the other characterization and contextualization tools that we run, including sandboxes.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/private-scanning/privatescanning_overview_20230929.png",
        null,
        "Private Scanning Overview"
      ],
      "align": "center"
    }
  ]
}
[/block]

As with most of our functionality you have two options to use it, through our [API](https://virustotal.readme.io/reference/private-files-api) or via the web interface. We have also developed a [command-line script](https://storage.googleapis.com/vtcdn/api-scripts/privscan.py) to get you started with automation.

# Accessing the Private Scanning web interface

To access this service you can follow the link at the top of the VirusTotal home view ([https://www.virustotal.com/gui/private-scanning/](https://www.virustotal.com/gui/private-scanning/.)). Note that Private Scanning is a paid offering and you will need specific privileges to access it, please [do not hesitate to request a trial](https://www.virustotal.com/gui/contact-us/premium-services).

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/private-scanning/privatescanning_link_20230929.png",
        null,
        "Private Scanning Link"
      ],
      "align": "center"
    }
  ]
}
[/block]

A drop-down will open showing shortcuts to different views related to Private Scanning. We can highlight the `My latest uploads` option, which will take us to the list of previous private analyses **submitted by you**, or the `My group latest uploads` option, which will take us to the list of previous private analyses **submitted by users in your organization**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/private-scanning/privatescanning_menu_20240110.png",
        null,
        "Private Scanning Menu"
      ],
      "align": "center"
    }
  ]
}
[/block]

In the Private Scanning main view you will see a couple of tabs to switch between the view that allows you to upload a file or URL ("*Scan*") and the view with the list of private analyses ("*Analyses*"). Note that this list only includes analyses of files or URLs submitted by your organization, and note that these reports are only visible to your organization. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/private-scanning/privatescanning_list_20240108.png",
        null,
        "Private Scanning List"
      ],
      "align": "center"
    }
  ]
}
[/block]

# Analyzing using the Private Scanning module

To upload and analyze a file or URL privately, go to the "*Scan*" section. There are several ways to get there, either by clicking on the corresponding tab in the main view of Private Scanning, or on the link with the text "*go to upload form*" displayed at the top of any view belonging to Private Scanning, or from the VirusTotal homepage by clicking on the top menu on the option "*Private Scanning*" and then on "*Upload file*" or "*Upload URL*".

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/private-scanning/privatescanning_links1_20240109.png",
        null,
        "Private Scanning Links"
      ],
      "align": "center"
    }
  ]
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/private-scanning/privatescanning_links2_20240110.png",
        null,
        "Private Scanning Link from homepage"
      ],
      "align": "center"
    }
  ]
}
[/block]

## Analyzing a file

> ℹ️ **Compressed files (ZIP, 7z, RAR, tar.bz2, etc)**
>
> 1. It is recommended you unbundle these and scan them individually. This will provide the most thorough analysis. Static analysis will work best with single files.
> 2. In the web interface you may upload a ZIP file less than 3MB with a single bundled file that is password encrypted. This may help bypass Antiviruses checks on the client side.
> 3. Compressed files will be sent to sandboxes and attempts to unencrypted files is done on a best-effort bassis. We will check if the password is `infected`.
> 4. If files in the compressed bundle are extracted, they will appear in the relationships as files you may chose to analyse.

Once you are in the view to scan files, by clicking on the button "*Choose file*" you will be prompted to choose a file from your computer. After the file is chosen you will be requested to confirm the upload.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/private-scanning/privatescanning_choose_file_20240109.png",
        null,
        "Private Scanning Choose a file"
      ],
      "align": "center"
    }
  ]
}
[/block]

You may also set detonation options such as whether the dynamic execution in sandboxes should have internet connectivity, the retention time in days that the files and reports will have, after which they will be deleted, or the region in which you want the files to be temporarily stored.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/private-scanning/privatescanning_options_20250205.png",
        null,
        "Private Scanning Options"
      ],
      "align": "center"
    }
  ]
}
[/block]

With "Enable Live interaction" selected, you can choose the desired sandbox and maximum timeout.

![Live interaction options](https://storage.googleapis.com/vtdocresources/guides/private-scanning/privatescanning_live_interactions_20250205.png)

If the file is already available in the standard VirusTotal open corpus, you will be informed accordingly and you may navigate to the corresponding VirusTotal ENTERPRISE report. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/private-scanning/privatescanning_knownfile_20240109.png",
        null,
        "Private Scanning Known File"
      ],
      "align": "center"
    }
  ]
}
[/block]

As soon as the file is uploaded you'll be redirected to the report view, where you can see the scan progress and preliminary data regarding your file. The full analysis can take several minutes to complete, note that the file will be detonated in multiple sandboxes for a couple of minutes and network traces will be subsequently analyzed with intrusion detection systems. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/private-scanning/privatescanning_report_20240109.png",
        null,
        "Private Scanning Report"
      ],
      "align": "center"
    }
  ]
}
[/block]

With "Enable Live interaction" selected, a link will appear to access the live interaction screen a few seconds after the analysis has been enqueued and started.

![Live interaction link](https://storage.googleapis.com/vtdocresources/guides/private-scanning/privatescanning_liveinteraction_link_20240604.png)

During the live interaction you can stop the analysis prior to the timeout by clicking the "Stop" Button within the live interaction menu.

![Live interaction menu](https://storage.googleapis.com/vtdocresources/guides/private-scanning/privatescanning_liveinteraction_menu_20240604.png)

## Analyzing a URL

In the view for scanning URLs you may specify the URL you want to scan privately. Once introduced, you can run the scan by pressing the *Enter* key.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/private-scanning/privatescanning_scan_url_20240109.png",
        null,
        "Private Scanning Scan a URL"
      ],
      "align": "center"
    }
  ]
}
[/block]

As in the case of file analysis, URL analysis provides some options for configuring your analysis. You can specify the retention period days and select a storage region where the files derived from the analysis will be stored.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/private-scanning/privatescanning_url_options_20240109.png",
        null,
        "Private Scanning URL options"
      ],
      "align": "center"
    }
  ]
}
[/block]

As soon as the URL is uploaded you'll be redirected to the report view, where you can see the scan progress and preliminary data regarding your URL.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/private-scanning/privatescanning_url_analysis_20240109.png",
        null,
        "Private Scanning URL analysis"
      ],
      "align": "center"
    }
  ]
}
[/block]

# Private Scanning file reports

Once the analysis concludes, you will have access to a file report, but as mentioned previously, private analyses won't contain antivirus verdicts, they will only contain the output of all the other analysis and contextualization tools that we have in VirusTotal, including sandboxes:

* Matches from your active Livehunt rules or from Livehunt rules that have been shared with you.
* Crowdsourced {YARA, SIGMA, IDS, AI} rule matching to produce flags and detections.
* Static and behavioural pattern analysis relevant to produce maliciousness determinations.
* Static tooling such as file signature extractors, file type identification, file format dissection, document macro decoders, strings analysis, etc.
* Dynamic analysis (detonation) in multiple sandboxes. Support for Windows, Mac OS X, Linux and Android. Process, file system, memory, network, etc. analysis.
* Behaviour and static feature mapping to MITRE ATT\&CK matrix.
* Malware configuration extractors and decryptors.
* Threat intel enrichment for all extracted IoCs (embedded IPs, contacted domains, download URLs, etc.).
* Clustering and similarity analysis, including attribution to campaigns, toolkit and actors through similar files.

The reports are made up of several tabs. The **detection tab** displays granular flags coming from crowdsourced {YARA, SIGMA, IDS, AI} matching, as well as sandbox execution verdicts. You may hover over matched rules to open them in a sidebar and export them to improve your security controls.  

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/private-scanning/privatescanning_detection_20240109.png",
        null,
        "Private Scanning Detection"
      ],
      "align": "center"
    }
  ]
}
[/block]

The **details tab** records features extracted through static analysis, this includes, but is not limited to:

* Basic properties: hashes, similarity hashes, file type identification, file size, compiler and packer identification.
* Capabilities and indicators: verbose insights into interesting functionality and properties from a cybersecurity point of view.
* File signature: signature and countersignature chain, software publisher, original file names, etc.
* File format dissectors: PE sections, imports, exports, document macro decoders, etc.

All of the highlighted properties are pivotable, meaning that clicking on them will launch a standard VirusTotal ENTERPRISE search across the entire VirusTotal corpus to locate other (non-private) files that exhibit the same property. This is extremely useful to identify other variants of the same attack and gather further context, including potential campaigns or actors tied to the threat.

The **relations tab** lists any related IoCs observed during static and dynamic analysis of the file, these can be used for hunting, remediation and containment purposes, as well as to proactively protect your organization by blocking them in your security solutions. Some of the relationships include:

* Execution parents: files that have been seen dropping the file under study when executed in a sandbox.
* Dropped files: files that are dropped when the file under consideration is detonated in a sandbox.
* Embedded {domains, IPs, URLs}: network IoCs seen within the binary body of the file under consideration, e.g. as a string.
* Contacted {domains, IPs, URLs}: network resources to which the file reaches out when executed in multiple sandboxes.
* Download URLs: Any URLs that standard VirusTotal has seen delivering the file under consideration.

Whenever these related IoCs are present in the standard VirusTotal corpus, they are automatically enriched with reputation and threat context coming from VirusTotal ENTERPRISE: security vendor detection ratios, geolocation, in-the-wild prevalence, etc. Moreover, all these related IoCs that are present in the standard VirusTotal corpus are pivotable, meaning that clicking on them will open the IoC report on the standard VirusTotal ENTERPRISE web interface to help you gather further context.

As a final remark relative to the relations tab, note that when you upload a compressed bundle and it contains a file that is already in the VirusTotal corpus, we'll let you know so you can pivot to the standard VirusTotal ENTERPRISE report.

The **behavior tab** displays the execution report summaries for all sandboxes that act on the file. The summary includes notions such as: MITRE ATT\&CK TTPs, file system actions, registry actions, process and service actions, synchronization mechanisms and signals (e.g. mutexes created), network communications, screenshots, etc. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/private-scanning/privatescanning_behavior_20230929.png",
        null,
        "Private Scanning Behavior"
      ],
      "align": "center"
    }
  ]
}
[/block]

 

The activity summary toolbar also allows you to access more technical assets such as network execution traces (PCAPs), detailed dynamic reports (e.g. API calls), windows event logs, memory dumps, etc.

 

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/private-scanning/privatescanning_activity_20230929.png",
        null,
        "Private Scanning"
      ],
      "align": "center"
    }
  ]
}
[/block]

 

The **community tab** will list any VirusTotal collections that contain a hash for the file under consideration, as well as any threat actors related to those collections.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/private-scanning/privatescanning_community_20230929.png",
        null,
        "Private Scanning"
      ],
      "align": "center"
    }
  ]
}
[/block]

# Locating similar files and expanding context

One of the most useful and differentiated features of Private Scanning is pivoting to other similar files in the open VirusTotal ENTERPRISE corpus. This can be done by acting on the similarity icon in the file summary block, multiple similarity analysis techniques are available:

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/private-scanning/privatescanning_similar_20240109.png",
        null,
        "Private Scanning Similar"
      ],
      "align": "center"
    }
  ]
}
[/block]

 

By jumping to other similar files you may understand industry reputation and naming for other variants of the threat, commonalities and in-the-wild patterns, lookup and submission activity (telemetry) for related files, etc.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/private-scanning/privatescanning_distributionvectors_20230929.png",
        null,
        "Private Scanning"
      ],
      "align": "center"
    }
  ]
}
[/block]

 
With the similar files you can also leverage VT DIFF to automatically build YARA rules for the pertinent malware toolkit and you may gain further insights on the corresponding threat campaign and actors behind it:

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/private-scanning/privatescanning_actors_20230929.png",
        null,
        "Private Scanning Actors"
      ],
      "align": "center"
    }
  ]
}
[/block]

# Deleting files and analysis reports

The files and their analysis reports in Private Scanning have an expiration date as mentioned above, and are deleted once their retention period expires. However, you can delete both the file and its report even before that time expires. For this purpose go to the report header and open the menu "*More*". There you will find the options to either delete only the file and keep the report (until its retention period ends), or to delete the file and its report immediately:

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/private-scanning/privatescanning_delete_20240110.png",
        null,
        "Private Scanning Delete"
      ],
      "align": "center"
    }
  ]
}
[/block]

# Private Scanning URL reports

Once the analysis of a URL concludes, you will have access to its URL report. Private analyses won't contain antivirus verdicts, but they will contain the output of other analysis and contextualization tools that we have in VirusTotal:

The **details tab** displays additional information about the scanned resource, such as the HTTP response headers and body info returned by the server upon asking for the given URL, the list of all redirections until the final URL is reached, etc.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/private-scanning/privatescanning_url_details_20240109.png",
        null,
        "Private Scanning URL details"
      ],
      "align": "center"
    }
  ]
}
[/block]

The **behavior tab** displays useful information such as page statistics, cookies, HTTP transactions, a screenshot, etc.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/private-scanning/privatescanning_url_behavior_20240109.png",
        null,
        "Private Scanning URL behavior"
      ],
      "align": "center"
    }
  ]
}
[/block]

# Private Analysis Workflow

| Task          | Description                                                 | Duration                       | Dependency |
| :------------ | :---------------------------------------------------------- | :----------------------------- | :--------- |
| Upload        | User uploads sample, analysis ID generated.                 | 1 to 30 seconds; avg 3 seconds | None       |
| Prefilter     | Detect which sandbox to send sample to.                     | 1 to 60 seconds; avg 5sec      | Upload     |
| Sandboxes     | Detonate in sandboxes.                                      | 4 to 15 minutes, avg 7min      | Prefilter  |
| Sigma         | Analyze logs against sigma rules.                           | 1 min                          | Sandboxes  |
| IDS           | Analyze network traffic PCAP with snort and suricata rules. | 2-5 min                        | Sandboxes  |
| MalwareConfig | Extract malware config and payloads from memory dumps.      | 2-5 min                        | Sandboxes  |

# Final technical highlights

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/private-scanning/privatescanning_highlights_20230929.png",
        null,
        "Private Scanning Final Highlights"
      ],
      "align": "center"
    }
  ]
}
[/block]

> ❓ **Looking for a benefit analysis?**
> You may want to share the [Private Scanning brief](https://assets.virustotal.com/vt-brief-private-scanning.pdf) with your stakeholders or leadership in order to justify its value.