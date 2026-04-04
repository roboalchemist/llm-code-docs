# Source: https://www.sigmajs.org/

Title: Sigma.js

URL Source: https://www.sigmajs.org/

Published Time: Tue, 27 May 2025 13:19:02 GMT

Markdown Content:
Sigma.js
===============
- [x] ![Image 1: Toggle menu](https://www.sigmajs.org/img/icon-menu.svg)![Image 2: Toggle menu](https://www.sigmajs.org/img/icon-close.svg) 

[![Image 3](https://www.sigmajs.org/img/logo-sigma-ruby.svg)**sigma****.js**](https://www.sigmajs.org/#)

*   **[Documentation](https://www.sigmajs.org/docs)**
*   [Examples](https://www.sigmajs.org/storybook)
*   [Architecture](https://www.sigmajs.org/#architecture)
*   [Quick start](https://www.sigmajs.org/#quickstart)
*   [Use cases](https://www.sigmajs.org/#usecases)
*   [FAQ](https://www.sigmajs.org/#faq)
*   [Go further](https://www.sigmajs.org/#gofurther)
*   [In the wild](https://www.sigmajs.org/#inthewild)

*   [![Image 4: GitHub](https://www.sigmajs.org/img/logo-github.svg)GitHub](https://github.com/jacomyal/sigma.js)
*   [![Image 5: Mastodon](https://www.sigmajs.org/img/logo-mastodon.svg)Mastodon](https://vis.social/@sigmajs)
*   [![Image 6: StackOverflow](https://www.sigmajs.org/img/logo-stackoverflow.svg)StackOverflow](https://stackoverflow.com/questions/tagged/sigma.js)

*   [![Image 7: Documentation](https://www.sigmajs.org/img/logo-documentation.svg)](https://www.sigmajs.org/docs)
*   [![Image 8: Code examples using Storybook](https://www.sigmajs.org/img/logo-storybook.svg)](https://www.sigmajs.org/storybook)
*   [![Image 9: GitHub](https://www.sigmajs.org/img/logo-github.svg)](https://github.com/jacomyal/sigma.js)
*   [![Image 10: Mastodon](https://www.sigmajs.org/img/logo-mastodon.svg)](https://vis.social/@sigmajs)
*   [![Image 11: StackOverflow](https://www.sigmajs.org/img/logo-stackoverflow.svg)](https://stackoverflow.com/questions/tagged/sigma.js)

![Image 12](https://www.sigmajs.org/img/logo-sigma-ruby.svg)sigma.js
====================================================================

_**a JavaScript library aimed at visualizing graphs of thousands of nodes and edges**_

See sigma.js in action
----------------------

Click here to explore a network of Wikipedia pages about data visualization.

[open demo](https://www.sigmajs.org/demo/index.html)[open demo sources](https://github.com/jacomyal/sigma.js/tree/main/packages/demo)

restore overlay over demo

Architecture
------------

Sigma.js is a modern JavaScript library for rendering and interacting with network graphs in the browser. It works in symbiosis with [graphology](https://graphology.github.io/), a multipurpose graph manipulation library.

![Image 13](https://www.sigmajs.org/img/logo-graphology.svg)

### graphology

_handles **graph data model & algorithms**_

+

![Image 14](https://www.sigmajs.org/img/logo-sigma-ruby.svg)

### sigma.js

_handles **graph rendering & interactions**_

=

![Image 15](https://www.sigmajs.org/img/icon-app.svg)

### your ♥ web app

Quick start
-----------

I want sigma.js in my existing project:

`npm install graphology sigma`
Learn more on the [quickstart guide](https://www.sigmajs.org/docs/quickstart)

I start from nothing:

[Try this CodeSandbox](https://codesandbox.io/p/sandbox/sigma-template-82mpns)

Use cases
---------

[](https://www.sigmajs.org/storybook/?path=/story/load-gexf-file--story)

Display
-------

The most basic use case: you have a graph dataset, with colors, sizes and positions for each node. For instance, you exported a [GEXF graph file](https://gexf.net/) from [Gephi](https://gephi.org/). You want to visualize it using on a web page.

[Open in Storybook](https://www.sigmajs.org/storybook/?path=/story/load-gexf-file--story)

[](https://www.sigmajs.org/storybook/?path=/story/use-reducers--story)

Explore
-------

You want to add interaction, so that your users can dig into the graph. You want to add a search field, and allow users to see the neighborhood of a node when hovering it.

[Open in Storybook](https://www.sigmajs.org/storybook/?path=/story/use-reducers--story)

[](https://www.sigmajs.org/storybook/?path=/story/mouse-manipulations--story)

Interact
--------

You are developing a web application where users can create and manipulate graphs. You need users to be able to create nodes on click, and to drag and drop nodes.

[Open in Storybook](https://www.sigmajs.org/storybook/?path=/story/mouse-manipulations--story)

[](https://www.sigmajs.org/storybook/?path=/story/custom-rendering--story)

Customize
---------

You need to personalize the way your graphs are rendered. You need to display some nodes with pictures in them, and others differently.

[Open in Storybook](https://www.sigmajs.org/storybook/?path=/story/custom-rendering--story)

Frequently asked questions
--------------------------

*   ### How can I obtain drawable data from a CSV?

You will process the data with graphology, then render it with sigma.js. You can look at [this example](https://www.sigmajs.org/storybook/?path=/story/csv-to-network-map--story) for instance.

*   ### What graph algorithms are implemented in sigma.js?

None in sigma.js, but graphology has a lot, from [ForceAtlas2 layout](https://graphology.github.io/standard-library/layout-forceatlas2.html) to [various metrics](https://graphology.github.io/standard-library/metrics.html) or even [community detection](https://graphology.github.io/standard-library/communities-louvain.html). **You can see an overview [in the documentation](https://graphology.github.io/standard-library/).**

*   ### Why should I use sigma.js and not [d3.js](https://d3js.org/)?

Sigma.js renders graphs using WebGL. It allows drawing larger graphs faster than with Canvas or SVG based solutions. It also makes custom rendering way harder to develop. If you have small graphs (like a few hundreds of nodes and edges) and/or if you need very customized rendering, then **d3.js is indeed a best fit for you**.

*   ### Can I use sigma.js in my [React](https://reactjs.org/) application?

Yes, the best way is certainly to use the [@react-sigma](https://github.com/sim51/react-sigma). The example on top of this page is developed using it, you can check the [sourcecode](https://github.com/jacomyal/sigma.js/tree/main/packages/demo) to get an idea.

*   ### And within an [Angular](https://angular.io/) application?

Yes it is possible, but harder, because we do not have a wrapper yet. So you will have to bind sigma.js lifecycle to your app manually. It is not necessarily too difficult though, please take a look on [this repository](https://github.com/sim51/ng-sigma-example) which offers a quick example.

Go further
----------

### I want to know more

Look at [the documentation](https://www.sigmajs.org/docs).

### I have a problem

Ask your questions on [StackOverflow](https://stackoverflow.com/questions/tagged/sigma.js), or report bugs by [opening a new GitHub issue](https://github.com/jacomyal/sigma.js/issues/new/choose).

### I want to help

Contributions are welcome! Reading [our contribution guide](https://github.com/jacomyal/sigma.js/blob/main/CONTRIBUTING.md) is a good start. You can also help us investigating [existing issues](https://github.com/jacomyal/sigma.js/issues) or answering [questions on StackOverflow](https://stackoverflow.com/questions/tagged/sigma.js).

In the wild
-----------

Here are a selection of applications and websites using sigma.js.

[](https://gephi.org/gephi-lite)

### Gephi Lite

a graph visualization and exploration web application

[](https://graphcommons.com/)

### GraphCommons

a collaborative platform for mapping, analyzing, and sharing data-networks

[](https://ouestware.gitlab.io/retina)

### Retina

a web application to help sharing graph visualizations online

[](https://polinode.com/)

### Polinode

a software to collect, visualize and analyze connected data

[](https://gdotv.com/)

### G.V()

a software to write, debug, test and analyze Gremlin graph databases

[](https://github.com/medialab/ipysigma)

### ipysigma

a Jupyter widget to render networks in the result of a notebook cell

[](https://hyphe.medialab.sciences-po.fr/)

### Hyphe

a web corpus curation tool featuring a research-driven web crawler

[](https://kenelyze.com/)

### Kenelyze

an interactive network analysis and data visualization platform

[](https://github.com/SpecterOps/BloodHound)

### BloodHound

a security analysis tool for uncovering hidden Active Directory and Azure relationships

[](https://www.scovery.com/)

### Scovery

a tool for visualizing the digital footprint of companies on the Internet

[](https://www.marvel-graphs.net/)

### MARVEL graphs

a website featuring interactive maps of Marvel's characters and creators

[](https://helveg.net//)

### Helveg

a tool for visualizing and exploring the structure of C# codebases

![Image 16](https://www.sigmajs.org/img/logo-sigma-ruby.svg)**sigma****.js** is published by [Sciences-Po médialab](https://medialab.sciencespo.fr/en/) and [OuestWare](https://ouestware.com/en).

*   [documentation](https://www.sigmajs.org/docs)
*   [@sigmajs@vis.social on mastodon](https://vis.social/@sigmajs)
*   [github.com/jacomyal/sigma.js](https://github.com/jacomyal/sigma.js)

It is developed under [the MIT License](https://github.com/jacomyal/sigma.js/blob/main/LICENSE.txt).

This website uses [Hauroa Sans](https://themeui.net/hauora-sans-free-font/), [Public Sans](https://public-sans.digital.gov/) and [Cascadia Code](https://github.com/microsoft/cascadia-code) fonts.

![Image 17](https://matomo.ouestware.com/matomo.php?idsite=26&rec=1&action_name=Homepage&send_image=0)
