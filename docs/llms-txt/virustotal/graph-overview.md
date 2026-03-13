# Source: https://virustotal.readme.io/docs/graph-overview.md

# Overview

# Overview

***

* [Nodes](https://virustotal.readme.io/docs/graph-nodes)
* [Search and commonalities](https://virustotal.readme.io/docs/graph-commonalities)
* [Graphs Management](https://virustotal.readme.io/docs/graph-management)

VirusTotal Graph is a visualization tool built on top of VirusTotal data set. It understands the relationship between files, URLs, domains, IP addresses and other items encountered in an ongoing investigation. With it, you can pivot intelligently over any of the malware artifacts in your graph and synthesize your findings into a threat map that you can share with your colleagues.

![A VirusTotal graph](https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphoverview_graph_20231113.png) 

# Relationships oriented

***

VirusTotal's backend generates rich relationships: URLs from which a file has been downloaded, whether a given file been seen contained in some other files, what are the parents of a given Portable Executable, domain to IP address mappings over time, etc. Explore all these 30+ inter-item links in a graph, with nodes and arcs that allow you to discover new infrastructure and artifacts leveraged by the subjects of your investigation.

![VirusTotal Graph relations](https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphoverview_relations_20231113.png) 

# Create, collaborate, share

***

Work in the same investigation with your peers, save your investigation graphs and publish your findings either publicly or with your organization.

![VirusTotal Graph share publicly](https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphoverview_sharepublicly_20231113.png) ![VirusTotal Graph share withing our organization](https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphoverview_shareorganization_20231113.png) 

# Find patterns

***

Common patterns and commonalities are very interesting and, in a way, a critical piece in the investigation, this is why we have decided to calculate them on-demand for you. Just select a group of nodes in the graph and click on “Find commonalities” to see a list of common attributes in the selection.

![VirusTotal Graph patterns](https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphoverview_patterns_20231113.png) 

# Seamless integration with VTI search and hunting

***

Expand a node using a VTI search query or download the selected nodes in the graph. VirusTotal Graph works along with their sibling VT tools.

![VirusTotal Graph VTI integration](https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphoverview_vti_20231113.png) 

# Threat cards

***

Hover over any of the nodes in your graph and see a summary of the item with the most representative data in VirusTotal database. Click in the node to see the available expansions, the submission graph, the AV verdicts (for files and urls) and the community comments.

![VirusTotal Graph VTI threat cards](https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphoverview_threatcards_20231113.png) 

# Custom nodes

***

VirusTotal dataset might not know a link between two entities as it might only happen in your environment. VT Graph allow you to manually add this links and furthermore, to add a new node to the graph even when VT doesn’t know about it. Our supported custom types are file, url, domain, IP address, actor, department, email and victim.

![VirusTotal Graph VTI custom nodes](https://storage.googleapis.com/vtdocresources/guides/vt-graph/graphoverview_customnodes_20231113.png)