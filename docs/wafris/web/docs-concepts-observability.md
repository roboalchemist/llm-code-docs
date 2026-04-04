# Source: https://wafris.org/docs/concepts/observability/

Title: Observability

URL Source: https://wafris.org/docs/concepts/observability/

Markdown Content:
[](https://wafris.org/docs/concepts/observability/#context) Context
-------------------------------------------------------------------

It’s often a significant challenge for dev, sec and ops teams to understand both what’s happening _right now_ with requests hitting a site, but also what’s happening in reponse to changes in rules or configurations.

Traditionally, admins end up pulling data from logging systems, directly monitoring their application and copying and pasting data from one tool to another.

[](https://wafris.org/docs/concepts/observability/#request-observability) Request Observability
-----------------------------------------------------------------------------------------------

Wafris clients in managed mode report request data metrics to Wafris Hub. The most recent time-window data is used for real-time reporting and any older data discarded.

* * *
