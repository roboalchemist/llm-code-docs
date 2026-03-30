# Source: https://virustotal.readme.io/docs/graph-documentation.md

# Introduction

VirusTotal Graph is a visualization tool built on top of VirusTotal data set. It understands the relationship between files, URLs, domains, IP addresses and other items encountered in an ongoing investigation. With it, you can pivot intelligently over any of the malware artifacts in your graph and synthesize your findings into a threat map that you can share with your colleagues.

[VirusTotal Graph Overview](https://virustotal.readme.io/docs/graph-overview)\
[VirusTotal Graph search and start new investigation](https://virustotal.readme.io/docs/graph-search)\
[VirusTotal Graph management](https://virustotal.readme.io/docs/graph-management)\
[VirusTotal Graph nodes](https://virustotal.readme.io/docs/graph-nodes)\
[VirusTotal Graph Commonalities and Hunting](https://virustotal.readme.io/docs/graph-commonalities)
[Quick access to relevant graphs to you](#quick-access-to-relevant-graphs-to-you)\
[Toolbar](#toolbar)\
[VirusTotal Graph API](#virustotal-graph-api)

## Quick access to relevant graphs to you

This overview page shows different list of graphs:

* **Your graphs:** It includes your saved graphs and those graphs where you are editor or viewer

![VTGraph yours graphs list](https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphdocumentation_yourgraphs_20231113.png)

* **Latest graphs:** It includes the latest created graphs
* **Top commented graphs:** It includes the graphs that have more comments
* **Top viewed graphs:** It includes the graphs more visited

![VTGraph latest graphs list](https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphdocumentation_latestgraphs_20231113.png)

## Toolbar

For any of the list of graphs you are able to

![VTGraph sort criteria](https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphdocumentation_sortcriteria_20231113.png):  Sort by different criteria

![VTGraph graphs list view](https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphdocumentation_listview_20231113.png)/![VTGraph yours graphs list](https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphdocumentation_gridview_20231113.png) : Switch between list and grid views

## VirusTotal Graph API

As most of our other products, VirusTotal Graph is getting a restful API. The documentation can be found [here](https://virustotal.readme.io/reference/graphs) and a Python library to reduce the learning curve; it is available in our [Github repository](https://github.com/VirusTotal/vt-graph-api).