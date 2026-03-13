# Source: https://www.sigmajs.org/demo/index.html

Title: A cartography of Wikipedia pages around data visualization

URL Source: https://www.sigmajs.org/demo/index.html

Published Time: Tue, 27 May 2025 13:19:03 GMT

Markdown Content:
_2085 nodes , 5409 edges_
-------------------------

Description
-----------

This map represents a _network_ of Wikipedia articles around the topic of "Data visualisation". Each _node_ represents an article, and each edge a ["See also" link](https://en.wikipedia.org/wiki/See_also).

The seed articles were selected by hand by the [Sciences-Po médialab](https://medialab.sciencespo.fr/) team, and the network was crawled using [Seealsology](https://densitydesign.github.io/strumentalia-seealsology/), and then cleaned and enriched manually. This makes the dataset creditable to both the médialab team and [Wikipedia editors](https://en.wikipedia.org/wiki/Wikipedia:Wikipedians).

This web application has been developed by [OuestWare](https://www.ouestware.com/en/), using [react](https://reactjs.org/) and [sigma.js](https://www.sigmajs.org/). You can read the source code [on GitHub](https://github.com/jacomyal/sigma.js/tree/main/packages/demo).

Nodes sizes are related to their [betweenness centrality](https://en.wikipedia.org/wiki/Betweenness_centrality). More central nodes (ie. bigger nodes) are important crossing points in the network. Finally, You can click a node to open the related Wikipedia article.
