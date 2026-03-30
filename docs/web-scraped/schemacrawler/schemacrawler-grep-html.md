# Source: https://www.schemacrawler.com/schemacrawler-grep.html

Title: SchemaCrawler

URL Source: https://www.schemacrawler.com/schemacrawler-grep.html

Markdown Content:
SchemaCrawler - Free database schema discovery and comprehension tool
===============

*   [Consulting](https://www.schemacrawler.com/consulting.html)
*   [Download](https://www.schemacrawler.com/downloads.html)
*   [SchemaCrawler](https://www.schemacrawler.com/schemacrawler-grep.html#)[About SchemaCrawler](https://www.schemacrawler.com/index.html)[Readme](https://www.schemacrawler.com/getting-started.html)[Who Uses](https://www.schemacrawler.com/who-uses.html)[Database System Support](https://www.schemacrawler.com/database-support.html)[Distributions and Downloads](https://www.schemacrawler.com/downloads.html)[Change History](https://www.schemacrawler.com/changes-report.html)[License](https://www.schemacrawler.com/license.html)[Building From Source Code](https://www.schemacrawler.com/building.html)[Support and Consulting](https://www.schemacrawler.com/consulting.html) 
*   [Features](https://www.schemacrawler.com/schemacrawler-grep.html#)[Configuration](https://www.schemacrawler.com/config.html)[Text Output](https://www.schemacrawler.com/output.html)[Diff](https://www.schemacrawler.com/diff.html)[Grep](https://www.schemacrawler.com/schemacrawler-grep.html)[Diagramming](https://www.schemacrawler.com/diagramming.html)[Entity-Relationship (ER) Modeling](https://www.schemacrawler.com/entity-modeling.html)[Scripting](https://www.schemacrawler.com/scripting.html)[Lint](https://www.schemacrawler.com/lint.html)[MCP Server](https://www.schemacrawler.com/mcpserver.html)[Serialization](https://www.schemacrawler.com/serialize.html)[Weak Associations](https://www.schemacrawler.com/weak-associations.html)[Offline Snapshots](https://www.schemacrawler.com/offline.html)[Plugins](https://www.schemacrawler.com/plugins.html)[Extensions Using the Data Dictionary](https://www.schemacrawler.com/data-dictionary-extensions.html)[Extensions Using Catalog Attributes](https://www.schemacrawler.com/attributes.html)[SchemaCrawler Interactive Shell](https://www.schemacrawler.com/schemacrawler-shell.html)[Docker Image](https://www.schemacrawler.com/docker-image.html)[SchemaCrawler Report Maven Plugin](https://github.com/schemacrawler/SchemaCrawler-Report-Maven-Plugin)[SchemaCrawler Action for GitHub Actions](https://github.com/schemacrawler/SchemaCrawler-Action)[Security Considerations](https://www.schemacrawler.com/security-considerations.html) 
*   [Resources](https://www.schemacrawler.com/schemacrawler-grep.html#)[Getting Started](https://www.schemacrawler.com/getting-started.html)[Resources](https://www.schemacrawler.com/resources.html)[Metadata Retrieval](https://www.schemacrawler.com/metadata-retrieval)[Code Examples](https://www.schemacrawler.com/code-examples.html)[FAQS](https://www.schemacrawler.com/faq.html)[How-tos](https://www.schemacrawler.com/how-to.html)[Get Help](https://www.schemacrawler.com/consulting.html)[Javadocs](https://javadoc.io/doc/us.fatehi/schemacrawler/)[Project Page on GitHub](http://github.com/schemacrawler/SchemaCrawler) 

![Image 1: Schemacrawler logo](https://www.schemacrawler.com/images/schemacrawler_logo.svg)
SchemaCrawler

Free database schema discovery and comprehension tool

[](https://www.schemacrawler.com/schemacrawler-grep.html#schemacrawler-grep)SchemaCrawler Grep
==============================================================================================

SchemaCrawler is a command-line tool that allows you to search your database for tables and columns that match a regular expression, much like the standard [grep](https://en.wikipedia.org/wiki/Grep) tool.

The SchemaCrawler command-line allows limiting tables, views, columns, stored procedure and function based on regular expressions, in addition to the grep functionality. This can be useful, say, when you want to search through your schema to find all tables that have a CUSTOMER_ID column, for example.

To find tables with certain names, run SchemaCrawler with command-line options similar to `--info-level=standard --command=list --grep-columns=.*\\..*CUSTOMER.*\\..*` This will find table with names that have “CUSTOMER” in them.

To find tables with certain column names, run SchemaCrawler with command-line options similar to `--info-level=standard --command=list --grep-columns=.*\\.CUSTOMER_ID` This will find all tables that have a CUSTOMER_ID column.

For more details, see the grep example in the [SchemaCrawler examples](https://www.schemacrawler.com/downloads.html#running-examples-locally/) download.

* * *

[SchemaCrawler](https://www.schemacrawler.com/) is free and open-source software. **[Donations are appreciated.](https://www.paypal.me/sualeh)**

SchemaCrawler, v17.7.0

 © 2000-2026 Sualeh Fatehi <sualeh@hotmail.com>.

[![Image 2: Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-sa/4.0/)

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). 

![Image 3](blob:http://localhost/2ae2cc6f0544e8fcceb52fb6a599a7ea)

[](https://www.schemacrawler.com/schemacrawler-grep.html)[](https://www.schemacrawler.com/schemacrawler-grep.html)

[](https://www.schemacrawler.com/schemacrawler-grep.html)

[](https://www.schemacrawler.com/schemacrawler-grep.html)
