# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/embed-and-extend-pentaho-functionality-cp/embed-reporting-functionality/other-embedding-scenarios.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/embed-and-extend-pentaho-functionality-cp/embed-reporting-functionality/other-embedding-scenarios.md

# Other embedding scenarios

Pentaho offers many embeddable structures, not just the Pentaho Reporting engine engine. You can also embed or extend the Pentaho Analyzer engine (Mondrian), the Pentaho BI Platform, part or all of Pentaho Data Integration (Kettle), and the Weka data mining engine. This section is focused on reporting, however, so the below scenarios only involve the reporting components of Pentaho Business Analytics.

## Build a custom reporting tool

The examples in this section have covered simple scenarios that don't involve a high degree of user interactivity. It's easy to imagine how far you can expand the example code, even to the point of building your own client tools. On a slightly smaller scale, you could build a report-generation program that merely takes some parameters from a user, then silently emails the report to designated recipients via the Java mail component. You could also design a reporting daemon or service that listens for incoming requests and outputs reports to a web server.

Pentaho Report Designer is built on the Pentaho Reporting engine, as is the interactive reporting functionality built into the Pentaho User Console in the BI Platform. If you need a graphical report creation tool, it would be easier to modify Report Designer than it would be to rewrite it from scratch. For web-based interactive reporting, you will have an easier time embedding the entire BI Platform than trying to isolate and embed just the interactive component

## Hack the Pentaho Report Designer

Perhaps you do not need to create a whole new content creation program around the Pentaho Reporting engine; instead, you can enhance or reduce the functionality of Pentaho Report Designer to match your needs.

Report Designer is both modular and extensible, so you can remove or disable large portions of it, or create your own custom data sources, output formats, formulas, and functions. You can also customize Report Designer with your own background images, icons, language, and splash screen

## Embed the Pentaho BI platform

If your web-based reporting application needs scripting, scheduling, and security functionality, it makes more sense to embed the slightly larger Pentaho BI Platform instead of writing a large amount of your own code to add to the Pentaho Reporting engine. The BI Platform contains powerful scripting and automation capabilities, an email component, report bursting functionality, user authorization and authentication features, and a cron-compatible scheduling framework.

The BI Platform is the heart of the larger Pentaho Server, which is a complete J2EE web application that provides engines for Pentaho Reporting, Data Integration, and Analyzer, as well as a fully customizable web-based user interface that offers interactive reporting, real-time Analyzer views, and interactive dashboard creation.

The Pentaho Server is fully customizable, so your options range from simple rebranding to removing entire components or developing your own plugins to add major user-facing functionality.
