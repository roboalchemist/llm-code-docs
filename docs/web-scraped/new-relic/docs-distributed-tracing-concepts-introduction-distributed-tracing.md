# Source: https://docs.newrelic.com/docs/distributed-tracing/concepts/introduction-distributed-tracing/

Title: Distributed tracing: Track requests across your microservices

URL Source: https://docs.newrelic.com/docs/distributed-tracing/concepts/introduction-distributed-tracing/

Markdown Content:
Distributed tracing: Track requests across your microservices | New Relic Documentation
===============

Opens in a new window Opens an external website Opens an external website in a new window

We use cookies and other tracking technologies - provided by other companies with whom we share your data - to make our website work, improve your experience, and support our marketing efforts, as explained in our [](https://newrelic.com/termsandconditions/privacy)[Privacy Notice](https://newrelic.com/termsandconditions/privacy). By using our website, you agree to our [](https://newrelic.com/termsandconditions/website-terms)[Website Terms of Use](https://newrelic.com/termsandconditions/website-terms). [Privacy Notice](https://newrelic.com/termsandconditions/privacy)

[](https://newrelic.com/)

[Docs](https://docs.newrelic.com/)[Community](https://support.newrelic.com/)[Learn](https://learn.newrelic.com/)

*   [Docs](https://docs.newrelic.com/)
*   [Community](https://support.newrelic.com/)
*   [Learn](https://learn.newrelic.com/)

*   / 
*   [English](https://docs.newrelic.com/docs/distributed-tracing/concepts/introduction-distributed-tracing/)[Español](https://docs.newrelic.com/es/docs/distributed-tracing/concepts/introduction-distributed-tracing/)[Français](https://docs.newrelic.com/fr/docs/distributed-tracing/concepts/introduction-distributed-tracing/)[日本語](https://docs.newrelic.com/jp/docs/distributed-tracing/concepts/introduction-distributed-tracing/)[한국어](https://docs.newrelic.com/kr/docs/distributed-tracing/concepts/introduction-distributed-tracing/)[Português](https://docs.newrelic.com/pt/docs/distributed-tracing/concepts/introduction-distributed-tracing/)   
*   [Log in](https://one.newrelic.com/)[Start now](https://newrelic.com/signup)

[](https://docs.newrelic.com/)

[](https://docs.newrelic.com/)

START HERE

[Get started with New Relic](https://docs.newrelic.com/docs/new-relic-solutions/get-started/intro-new-relic/)

Tutorials and walkthroughs

Guides and best practices

MONITOR YOUR DATA

New Relic Control

AI monitoring

Application performance monitoring

Browser monitoring

eBPF observability

Infrastructure monitoring

Kubernetes monitoring

Log management

Mobile monitoring

Model performance monitoring

Queues and Streams

Network monitoring

OpenTelemetry

SAP Solutions

Serverless monitoring

Streaming Video & Ads

Synthetic monitoring

Website performance monitoring

DATA INSIGHTS

New Relic AI

Alerts

Change tracking

Charts, dashboards, and querying

Cloud Cost Intelligence

CodeStream

Distributed tracing

[Get started with distributed tracing](https://docs.newrelic.com/docs/distributed-tracing/concepts/introduction-distributed-tracing/)

[Planning guide](https://docs.newrelic.com/docs/distributed-tracing/concepts/distributed-tracing-planning-guide/)

[Set up tracing](https://docs.newrelic.com/docs/distributed-tracing/concepts/quick-start/)

[Technical details](https://docs.newrelic.com/docs/distributed-tracing/concepts/how-new-relic-distributed-tracing-works/)

Tracing UI and data

Infinite Tracing

Trace API

Troubleshooting

Errors inbox

New Relic Lens

NRQL

Service Architecture Intelligence

Service level management

Workflow Automation

SECURITY

Interactive application security testing (IAST)

Security RX (Remediation Explorer)

PRODUCT UPDATES

Release notes

What's new?

[End-of-life announcements](https://docs.newrelic.com/eol/)

ADMIN AND DATA

Account & user management

Data and APIs

[Data dictionary](https://docs.newrelic.com/attribute-dictionary/)

Security and privacy

Licenses

Distributed tracing: Track requests across your microservices
=============================================================

Distributed tracing tracks and observes service requests as they flow through distributed systems.

Requests might pass through various services to reach completion, and these services could be in a variety of places: containers, serverless environments, virtual machines, different cloud providers, or on-premises. When you can see the path of an entire request across different services, you can quickly pinpoint failures or performance issues.

Distributed tracing collects data as requests travel from one service to another, recording each segment of the journey as a span. These spans contain important details about each segment of the request and are eventually combined into one trace. The completed trace gives you a picture of the entire request.

[![Image 2: Diagram showing how spans are generated in a distributed trace](https://docs.newrelic.com/images/distributed-tracing_diagram_intro-to-dist-tracing.webp)](https://docs.newrelic.com/images/distributed-tracing_diagram_intro-to-dist-tracing.webp)

Here is an example of a web transaction where agents measure the time spent in each service. Agents then send that timing information to New Relic as spans, and the spans are combined into one distributed trace.

Get started[](https://docs.newrelic.com/docs/distributed-tracing/concepts/introduction-distributed-tracing/#learn-more)
-----------------------------------------------------------------------------------------------------------------------

See these distributed tracing topics:

*   [Distributed tracing setup options](https://docs.newrelic.com/docs/distributed-tracing/concepts/quick-start/)
*   [How does distributed tracing work, and what types of distributed tracing are available?](https://docs.newrelic.com/docs/distributed-tracing/concepts/how-new-relic-distributed-tracing-works/)
*   [How can I troubleshoot requests using the distributed tracing UI?](https://docs.newrelic.com/docs/distributed-tracing/ui-data/understand-use-distributed-tracing-ui/)
*   [How should I plan my rollout of distributed tracing?](https://docs.newrelic.com/docs/distributed-tracing/concepts/distributed-tracing-planning-guide/)
*   [What is the advanced feature called Infinite Tracing?](https://docs.newrelic.com/docs/understand-dependencies/distributed-tracing/infinite-tracing/introduction-infinite-tracing/)

#### On this page

*   [Get started#learn-more](https://docs.newrelic.com/docs/distributed-tracing/concepts/introduction-distributed-tracing/#get-startedlearn-more)

Was this doc helpful?

😁

Yes

🙁

No

[Edit this doc](https://github.com/newrelic/docs-website/blob/develop/src/content/docs/distributed-tracing/concepts/introduction-distributed-tracing.mdx)

Copyright © 2026 New Relic Inc.

[Careers](https://newrelic.com/about/careers)[Terms of Service](https://newrelic.com/termsandconditions/terms)[DMCA Policy](https://newrelic.com/termsandconditions/dmca)[Patent Notice](https://newrelic.com/termsandconditions/patent-notice)[Privacy Notice](https://newrelic.com/termsandconditions/services-notices)Your Privacy Choices[Cookie Policy](https://newrelic.com/termsandconditions/cookie-policy)[UK Slavery Act](https://newrelic.com/termsandconditions/uk-slavery-act)

This site is protected by reCAPTCHA and the Google[Privacy Policy](https://policies.google.com/privacy) and[Terms of Service](https://policies.google.com/terms) apply.
