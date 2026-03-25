# Source: https://virustotal.readme.io/docs/vt4browsers.md

# VT4Browsers + Google TI

**VT4Browsers** is our essential browser extension designed to **bring VirusTotal’s intelligence directly into your web activity**. It allows you to quickly check the safety of files before downloading them, scan sites while you browse, and generally vet suspicious elements without leaving your current tab.

> 📘 Note for Google Threat Intelligence users
>
> For users with a valid **Google Threat Intelligence API key**, we have unlocked a **new investigation experience**. You can access the full documentation [here](https://gtidocs.virustotal.com/docs/vt4browsers).

> ⚠️ WARNING!
>
> These are the options enabled by default when installing VT4Browsers for the first time, please take a close look:
>
> * **Scan downloads.** The extension will automatically submit to VirusTotal any files that you download that are not filtered out by other more granular settings. For non-executable files a prompt to confirm the upload will be displayed.
> * **Don’t scan documents.** The extension WILL NOT automatically submit to VirusTotal any documents that you open or download (DOCX, DOC, XLS, XLSX, PDF, etc.)
> * **Send anonymous passive DNS data.** The extension will share with VirusTotal domain name to IP address mappings for any DNS resolutions that your browser performs. VirusTotal WILL NOT link these resolutions to your user or any other piece of information that could identify you.
>
> Make sure you adjust this default configuration to your needs, you can do this in the "Scan and Upload Settings" tab.
>
> Remember you can change any options that you want at any time. Don't forget to check our [Terms of Service](https://cloud.google.com/terms) and [Privacy Policy](https://cloud.google.com/terms/secops/privacy-notice) for additional insights.

The functionality is divided into 4 categories:\
[1. Uploading and scanning files automatically with VirusTotal](#uploading-and-scanning-files-automatically-with-virustotal)\
[2. IoC contextualization with VT AUGMENT](#ioc-contextualization-with-vt-augment)\
[3. Security analyst shortcuts via right-click](#security-analyst-shortcuts-via-right-click)\
[4. Keyboard shortcuts](#keyboard-shortcuts)\
[5. Final remarks](#final-remarks)

# Uploading and scanning files automatically with VirusTotal

***

VT4Browsers can ease the task of submitting downloaded files to VirusTotal so as to have a second opinion by more than 70 antivirus solutions with respect to their maliciousness.

The first thing you will see when installing the extension is the VirusTotal icon in the browser's extensions toolbar. If you click on it you will see there are two different settings tabs. The default tab contains the scanning options:

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/tools/vt4b_initial.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

This will allow you to customize when downloaded or opened files are sent to VirusTotal and your desired level of contribution to the security community. Once you have tweaked your upload and scanning settings, you can continue browsing as usual. Let's take a closer look at the upload settings:

* **Scan downloads with VirusTotal.** \[Active by default] Deactivating this setting will never contribute any files to VirusTotal, thus, you will not see the antivirus scanning results for your downloads. Activating it does not mean that your browser will automatically upload any download to VirusTotal, the submission logic will be governed by the subsequent upload settings:
  * **Don't scan documents (docx, pdf, etc.):** \[Active by default] No matter the rest of upload settings, the extension will not try to upload any downloaded/opened documents to VirusTotal.
  * **Show 'Send to VirusTotal' prompt when downloading files:** \[Inactive by default] Instead of automatically uploading downloaded files to VirusTotal, display a confirmation dialog for each download instance. This will allow you to decide whether you want to scan any files you download prior to the download itself. ATTENTION: at VirusTotal we take privacy very seriously, hence, even if you do not check this option, we will still prompt you to confirm upload of files that are not executables.
  * **Pause downloads when sending to VirusTotal:** \[Inactive by default] By default the extension will not block your downloads, it will submit those files to VirusTotal but the download will proceed as usual. Activating this setting will first perform the pertinent scan and once the VirusTotal report is being displayed you may decide on whether you want to proceed with the download.
* **Send anonymous passive DNS data to VirusTotal:** \[Active by default] You can read more about [passive DNS and its usefulness for the cybersecurity community in the Security Intelligence blog](https://securityintelligence.com/how-to-use-passive-dns-to-inform-your-incident-response/). This setting will automatically submit to VirusTotal the domain name to IP address mappings for any resolutions that your browser performs, be it websites that you visit or any resources that these websites request. None of this data is stored tied to any piece of information that may identify you and each resolution event is treated independently.

As to the actual VirusTotal submission mechanics. When the extension detects a download it will show a bubble where you can see the upload progress and the link to the file report:

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/tools/vt4b_download_popup.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "300px"
    }
  ]
}
[/block]

<br />

With the option to pause downloads you can even choose to resume or cancel your downloads after checking their VirusTotal report:

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/tools/vt4b_download_popup_stop.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "300px"
    }
  ]
}
[/block]

# IoC contextualization with VT AUGMENT

***

The second settings tab contains the options for the [VT AUGMENT widget](https://blog.virustotal.com/2021/05/compliant-easy-and-actionable.html) integration. This functionality automatically identifies IoCs (hashes, domains, IPs and URLs) in websites of your choice and incorporates VirusTotal reputation and threat context in a single pane of glass fashion.

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/tools/vt4b_augment_settings.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

<br />

Automatic IoC contextualization requires you to have a VirusTotal API key. If you do not have one, you can [register for free in the VirusTotal Community](https://www.virustotal.com/gui/join-us). If you already have an account, please refer to your API key view in the top right user menu:

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/tools/vt4browsersvtapikey_20230921.png",
        null,
        "VT4Browsers API key"
      ],
      "align": "center",
      "sizing": "500px"
    }
  ]
}
[/block]

The VT Augment functionality allows you to highlight or enrich IoCs (hashes, domains, IPs, URLs) in pages of your choice and works best with [premium API keys](https://virustotal.readme.io/reference/public-vs-premium-api), as these are not rate limited. You can [request a premium API key via our commercial inquiry contact form](https://www.virustotal.com/gui/contact-us/premium-services).

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/tools/vt4b_augment_settings_iocs.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

<br />

You will have to introduce your API key in the "My API key:" input box, once you do so you must click on the floppy disk icon to save the setting. You can then tweak IoC contextualization settings, the extension can perform two distinct tasks:

| **Highlighting**                                                                                                                                                                                                                                                                                                                                                     | **Enrichment**                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The **highlight** feature identifies IoCs and adds a VirusTotal icon next to each IoC. When the icon is clicked an API call is performed to embed the IoC detection ratio and display the [VT AUGMENT widget](https://blog.virustotal.com/2021/05/compliant-easy-and-actionable.html) as a side panel. **API quota is only consumed when you click on an IoC icon.** | For each IoC identified in a site, the **enrichment** feature automatically queries the VT API and embeds the IoC’s security vendors detection ratio/score next to the IoC. Clicking on the VirusTotal icon or detection ratio next to each IoC will then display the [VT AUGMENT widget](https://blog.virustotal.com/2021/05/compliant-easy-and-actionable.html) as a side panel. **This setting can generate API lookup spikes and is only recommended for premium API keys.** |
| ![](https://storage.googleapis.com/vtdocresources/guides/tools/vt4browsershighlighting_20230921.png)                                                                                                                                                                                                                                                                 | ![](https://storage.googleapis.com/vtdocresources/guides/tools/vt4browsersenrichment_20230921.png)                                                                                                                                                                                                                                                                                                                                                                               |

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/tools/vt4browsersvtaugmentreport_20230921.png",
        null,
        "VT4Browsers Augment Report"
      ],
      "align": "center"
    }
  ]
}
[/block]

As said, automatic IoC contextualization works best with [premium API keys](https://virustotal.readme.io/reference/public-vs-premium-api). Free public API keys are limited to 4 lookups/minute and 500 lookups/day. If you try to automatically enrich all the indicators on a given website, enrichment will stop after having enriched 4 IoCs within a minute. Premium API keys are only constrained by your licensed quota and will not face such limitations.

As to the specific highlighting and enrichment options:

* **Highlight ALL sites:** Automatically identifies IoCs in any website that you visit and adds a VirusTotal icon next to each one. When clicking on the logo next to an IoC, a VT API lookup is triggered and the detection ratio/score gets added at the same time that the VT Augment widget side panel gets displayed.
* \*\*Always highlight current site:\*\*Automatically identifies IoCs in the site being viewed, now and in the future. Adds a VirusTotal icon next to each IoC. When clicking on the logo next to an IoC, a VT API lookup is triggered and the detection ratio/score gets added at the same time that the VT Augment widget side panel gets displayed.
* **Always highlight current domain:** Automatically identifies IoCs in any website under the domain being visited, now and in the future. Adds a VirusTotal icon next to each IoC. When clicking on the logo next to an IoC, a VT API lookup is triggered and the detection ratio/score gets added at the same time that the VT Augment widget side panel gets displayed.
* **Enrich ALL sites:** Automatically identifies IoCs in any website that you visit, automatically looks these up against VirusTotal (one API lookup per IoC found) and adds a VirusTotal icon and detection score next to each one. When clicking on the logo and detection score next o an IoC, the VT Augment widget with the full IoC context gets displayed as a side panel.
* **Always enrich current site:** Automatically identifies IoCs in the website that you are visiting, now and in the future, automatically looks these up against VirusTotal (one API lookup per IoC found) and adds a VirusTotal icon and detection score next to each one. When clicking on the logo and detection score next o an IoC, the VT Augment widget with the full IoC context gets displayed as a side panel.
* **Always enrich current domain:** Automatically identifies IoCs in any website under the domain that you are visiting, now and in the future, automatically looks these up against VirusTotal (one API lookup per IoC found) and adds a VirusTotal icon and detection score next to each one. When clicking on the logo and detection score next o an IoC, the VT Augment widget with the full IoC context gets displayed as a side panel.

Some of these highlighting and enrichment actions can be performed via the right-click menu, under the VT4Browsers entry. **Right-clicking on a website will allow you to permanently add the pertinent domain to the automatic highlighting/enrichment settings and will also allow you to perform one-off contextualization for the given website**. More on this in the following section.

> ⚠️ ATTENTION:
>
> By default, the VT Augment widget will be displayed as a side panel on the current page. However, due to [CSP restrictions](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP), some web pages won't allow this behavior. When this happens, the VT Augment contextualization is displayed in a new tab.

### Understanding Detection Colors

VT4Browsers uses a simple color-coding system next to the Indicators of Compromise (IoCs) to give you an immediate visual assessment of the threat level, based on the number of Antivirus (AV) vendor detections on VirusTotal:

* **Green**: Indicates 0 detections. The item is generally considered benign and has no flags from any major security vendor.
* **Orange**: Used when there are 1 to 3 detections from AV vendors. The item is suspicious, and further investigation is recommended to determine the risk.
* **Red**: Used when there are more than 3 detections. The item has a significant number of security flags and is highly likely to be malicious or dangerous.

# Security analyst shortcuts via right-click

***

VT4Browsers adds a right-click menu entry to your browser allowing you to perform common security analyst tasks with a single click:

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/tools/vt4b_rightclick.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px",
      "border": true
    }
  ]
}
[/block]

Let's take a closer look at the shortcuts available:

* **Scan selected link:** If you have right-clicked on a link in a website, this option will allow you to scan the destination link URL with VirusTotal, to get a maliciousness assessment by more than 70 security vendors and blocklists.
* **Scan current page:** Submit the website being viewed to VirusTotal, to get a maliciousness assessment on the URL by more than 70 security vendors and blocklists.
* **Search selected hash:** Provided that you have highlighted an MD5, SHA1 or SHA256 hash in a website, this option will open up the pertinent VirusTotal report for the corresponding file, if present in VirusTotal.
* **Insert text/hash to search:** Allows you to type in an MD5, SHA1 or SHA256 hash, or rather some comment tag or [advanced VirusTotal Intelligence](https://www.virustotal.com/gui/intelligence-overview) search to query VirusTotal.
* **Always highlight current domain:** This is a shortcut for the IoC contextualization functionality described in the previous section. For any websites under the domain being viewed, VT4Browsers will add a VirusTotal lookup icon next to each IoC identified within the site, now and in the future. Upon clicking such VirusTotal lookup icon a VT API lookup will be performed and the icon will get extended with the security vendors detection score for the IoC at the same time that the full analysis widget will be displayed as a side panel.
* **Always enrich current domain:** This is a shortcut for the IoC contextualization functionality described in the previous section. For any websites under the domain being viewed, VT4Browsers will automatically look up the pertinent IoC in VirusTotal and incorporate the security vendors detection score, now and in the future. Upon clicking the security vendors detection score a full analysis widget will be displayed as a side panel with the most relevant VirusTotal context for the pertinent threat.
* **One-off highlighting of IoCs in current page:** This is a shortcut for the IoC contextualization functionality described in the previous section. For any IoCs found in the website being viewed, VT4Browsers will add a VirusTotal lookup icon next to each, as a one-off task. Upon clicking such VirusTotal lookup icon a VT API lookup will be performed and the icon will get extended with the security vendors detection score for the IoC at the same time that the full analysis widget will be displayed as a side panel.
* **One-off enrichment of IoCs in current page:** This is a shortcut for the IoC contextualization functionality described in the previous section. For any IoC found under the domain being viewed, VT4Browsers will automatically look up the pertinent IoC in VirusTotal and incorporate the security vendors detection score, as a one-off task. Upon clicking the security vendors detection score a full analysis widget will be displayed as a side panel with the most relevant VirusTotal context for the pertinent threat.
* **VT Intelligence multi-search for IoCs in current page:** This option will automatically identify any IoCs (hashes, domains, IPs, URLs) in the website being viewed and will launch a [VT Intelligence search](https://www.virustotal.com/gui/intelligence-overview) for those in a new tab.
* **VT Graph for IoCs in current page:** This option will automatically identify any IoCs (hashes, domains, IPs, URLs) in the website being viewed and will display them as a threat graph in [VT Graph](https://www.virustotal.com/gui/graph-overview).

# Keyboard shortcuts

***

VT4Browsers lets you easily perform the following actions via keyboard shortcuts:

* **One-off highlighting** of IoCs on current page.
* **One-off enrichment** of IoCs on current page.

Assign your preferred keyboard commands on your browser settings:

* **Chrome**: Go to chrome://extensions/shortcuts

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/tools/vt4b_shortcuts.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

* **Firefox**: Go to about:addons and click on "Manage Extension Shortcuts"

![](https://storage.googleapis.com/vtdocresources/guides/tools/vt4b_shortcuts_ff.png)

<br />

# Final remarks

***

Once again, please remember that you can adjust your security community contribution preferences in the VT4Browsers settings at any time:

[block:image]
{
  "images": [
    {
      "image": [
        "https://storage.googleapis.com/vtdocresources/guides/tools/vt4b_initial_empty.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

Additionally, make sure you read our[Terms of Service](https://cloud.google.com/terms) and [Privacy Policy](https://cloud.google.com/terms/secops/privacy-notice) before using this or any other VirusTotal products or services.