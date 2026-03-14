# Source: https://virustotal.readme.io/reference/widget-overview.md

# Overview

The [VT Augment widget](https://blog.virustotal.com/2021/05/compliant-easy-and-actionable.html) is an official, compliant and recommended way of integrating VirusTotal data in third-party applications through a **bring-your-own-api-key model**. It is fast and simple. Most importantly, it does not require you to build fancy view templates or parse complex API objects, the information is rendered in an iframe served by VirusTotal and can be customized to match your product's theme.

VT Augment enriches the most common observables used to describe threat campaigns: files/hashes, URLs, domains and IP addresses. The contextual information is not only limited to threat reputation, it also encompasses advanced IoC relationships, VirusTotal submission metadata, static properties, etc. Moreover, it embeds a threat graph that can even be leveraged by junior analysts to perform a quick initial assessment of a suspicious artifact.

You can see VT Augment in action in the following SIEM-like demo environment, **click on the VirusTotal icon next to each observable**:
<https://www.virustotal.com/ui/widget/demo/dedicated?full=1>

Benefits:

* Helps your users achieve the single pane of glass epiphany, no need to jump between tabs.
* Ensures compliance with VirusTotal's Terms of Service.
* No advanced coding required, minimal engineering resources needed to integrate.
* Stays seamlessly up-to-date with the latest advances in VirusTotal.
* Ties together two disparate products creating a single workflow experience, effortlessly, including advanced investigative pivots.