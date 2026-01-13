# Source: https://docs.datadoghq.com/tracing/guide/configure_an_apdex_for_your_traces_with_datadog_apm.md

---
title: Configure Apdex score by service
description: >-
  Learn how to configure Apdex scores for your services to measure user
  satisfaction based on application response times and performance thresholds.
breadcrumbs: Docs > APM > Tracing Guides > Configure Apdex score by service
source_url: >-
  https://docs.datadoghq.com/guide/configure_an_apdex_for_your_traces_with_datadog_apm/index.html
---

# Configure Apdex score by service

[Apdex](https://www.apdex.org/) (Application Performance Index) is an open standard developed by an alliance of companies that defines a standardized method to report, benchmark, and track application performance. Based on user experience satisfaction by measuring the response time of web applications and services, its role is to counterbalance response time average and percentiles which can be misleading when there are extreme data points.

## Definition{% #definition %}

Apdex is a numerical measure of user satisfaction with the performance of enterprise web applications. It converts many measurements into one number on a uniform scale on the [0;1] interval:

- 0 = no users satisfied
- 1 = all users satisfied

To define your Apdex, you need to be an administrator of your Datadog account. First define a time thresholdâ**T**âseparating satisfactory response times from unsatisfactory response times from your web application or service. With one threshold you can then define three categories:

- Satisfied requests have a response time below **T**.
- Tolerated requests have a response time equal to or above **T** and below or equal to **4T**.
- Frustrated requests have a response time above **4T** or returns an error.

Once the threshold is defined and your requests are categorized, the Apdex is defined as:

$$\bo\text"Apdex"=({\bo\text"Satisfied"\text" requests" + {{\bo\text"Tolerated"\text" requests"} / 2}})/{\bo\text"Total"\text" requests"} $$

Selecting the correct threshold is important because the Frustrated requests are 4 times slower than "normal". If T=3 the user waits 3 seconds for a page to load but does not tolerate waiting 12 seconds.

Apdex thresholds must be set by administrators, per service, before Apdex scores calculated.

## Set your Apdex for your traces{% #set-your-apdex-for-your-traces %}

To visualize your web application or service Apdex:

1. In [Software Catalog](https://app.datadoghq.com/services?query=type%3Aweb), hover over your web service and select **Service Page**.

1. Click the **Latency** graph title to open a drop-down menu, and select **Apdex**.

**Note**: The Apdex option is only available for web services.

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/faq/apdex_selection_2.c7e53e25d43ecc35a63d8b73515bcb38.png?auto=format"
      alt="Latency graph drop-down menu showing Apdex option" /%}

1. Use the pencil icon on the top left of your widget to edit your Apdex configuration.

**Note**: You must be an administrator to see this icon.

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/faq/apdex_edit.26ebfc5181541b7b1aa282782eb50396.png?auto=format"
      alt="Pencil icon above Apdex graph, which can be selected to edit tolerable threshold" /%}

1. Enter your threshold to visualize your request distribution.

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/faq/apdex_update.211cd67d9f7e7b42bb95204c2b8ab02b.png?auto=format"
      alt="Apdex Configuration edit screen, showing text box to set tolerable threshold" /%}

1. Save your widget to follow your Apdex evolution over time.

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/faq/apm_save.86fb4f5fcd50202051b0a84fc0ce5d5c.png?auto=format"
      alt="Apdex graph after saving configuration changes" /%}

## Display your Apdex on the Software Catalog{% #display-your-apdex-on-the-software-catalog %}

To display Apdex scores on the [Software Catalog](https://app.datadoghq.com/services), select it in the configuration menu on the upper right corner of the page:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/faq/apdex_service_list.f8920199941f07f7a93d7b707c80bbb3.png?auto=format"
   alt="Apdex Software Catalog" /%}
