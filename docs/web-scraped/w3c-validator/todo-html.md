# Source: https://validator.w3.org/todo.html

Title: Development Roadmap for The W3C Markup Validation Service

URL Source: https://validator.w3.org/todo.html

Markdown Content:
W3C Markup Validator Roadmap
----------------------------

This page holds the development roadmap for the [W3C Markup Validation Service](https://validator.w3.org/).

*   We use [GitHub](https://github.com/w3c/markup-validator/issues) to track bugs and feature requests.
*   This roadmap only gives a high-level overview of what each generation of the validator changed from the others. For a detailed list of features and changes in past releases, see the [News](https://validator.w3.org/whatsnew.html) page.
*   If you would like to discuss this roadmap, or request new features, please join the [www-validator mailing list](http://lists.w3.org/Archives/Public/www-validator/).

### High-Level Objectives

*   Provide the web with a one-stop service for Web Quality check 
*   Help raise quality for (m)any kind(s) of Web content 
*   Build a positive culture of Web Quality 
*   Future-proof our services (new formats, new usage) 
*   Leverage Communities energy 
*   Remain the trusted source by professionals 
*   Find the right balance between accuracy and user-friendliness 

### Roadmap

#### Multi-engine validator

The current validator is mostly based on an DTD parser, with an XML parser used only for some checks. It also plugs into an html5 parser for the validation of HTML5 content. In the future, other engines should be used to check compound XML documents (with NVDL+relax, XML Schema, Schematron - using e.g the relaxed engine)

The following flowchart describes the validation engine architecture, as it is now, and as we envision it in the near future.

[![Image 1: validator flow chart: now and next generation](https://validator.w3.org/images/roadmap/validators-chart-small.png)](https://validator.w3.org/images/roadmap/validators-chart.png)

(follow link to enlarge, or download the vector-based [graffle](https://validator.w3.org/images/roadmap/validators-chart.graffle), [PDF](https://validator.w3.org/images/roadmap/validators-chart.pdf) or [SVG](https://validator.w3.org/images/roadmap/validators-chart.svg) version)

##### Milestones

@@ TODO @@ add these as Bugzilla entries

1.   Interface with an NVDL+RelaxNG engine for validation of compound XML documents (coding the interface will be similar to the one done for hTML5 engine)

2.   Choose the right NVDL+RelaxNG engine. relaxed and validator.nu provide such capability, and of course there is the option to roll our own (jing, etc).

3.   Change check code to send multiple-namespace XML documents to NVDL+RelaxNG engine

4.   Interface with the feed validator, RDF validator and CSS validator programatically (instead of redirecting, as done today)

#### Mulitilingual tool

The Markup Validator receives 1M requests per day, and is only in English. Making it multiligual would make the tool easier to use for web developers and designers worldwide. Although this may be technically tricky (given the number of message/engine sources), the community would be very excited in participating in the translation effort.

#### Site-wide services

The markup validator currently checks a single page. Some companion software (such as the log validator) could be made into a web service to provide crawling, batch validation, scheduled checks etc.

#### Check beyond markup

This may be in the roadmap for Unicorn rather than the markup validator, but it fits in the "long-term" vision of developing the W3C Web Quality services. Checking of RDDL, RDFa, microformats and other rich markup are in scope. Many other checks could be added to the validators, such as:

*   document cacheability 
*   spell checking 
*   semantic extraction 
*   accessibility evaluation 

#### Less finger pointing, more problem solving

Most of our tools, and especially the "star" HTML validator, have a binary "valid/invalid" way of presenting their results. While this is useful for some, it tends to make people look away from the "big picture" of web quality. A new one-stop quality checker could help bring a paradigm shift by showing diverse aspects of web quality, while systematically suggesting solutions for every problem. This would involve working with designers to find ways to present aggregated quality information in a clear and positive manner.

### Past Releases Roadmap

0.8.x The 0.8.0 release sees the validator code reorganized around a more modular architecture, adding better XML checking capabilities. In 0.8.5, HTML5 checking capabilities were added by interfacing with the validator.nu engine.0.7.x The 0.7.0 release reorganized the validator to use templates, making it easier to produce different outputs (hence the development of an API). 0.7.0 through 0.7.4 included mostly bug fixes and documentation updates.0.6.x The 0.6.0 release, in 2002, kicked in a new phase of open source development for the validator, including a number of bug fixes. 0.6.0 through 0.6.7 included mostly bug fixes and documentation updates.Versions Prior to 0.6.0 Versioning up to version 0.5.x was only done as a development mechanism, and the validator was not following a strict release cycle.
