# Source: https://docs.datadoghq.com/dashboards/guide/context-links.md

---
title: Context Links
description: >-
  Connect dashboard widgets to Datadog pages and third-party applications using
  customizable context links with variables.
breadcrumbs: Docs > Dashboards > Graphing Guides > Context Links
---

# Context Links

## Overview{% #overview %}

Dashboards collect data from multiple sources and display this data as visualizations.

You can attach dashboards to [monitor notifications](https://docs.datadoghq.com/monitors/notify/), use them as screenboards to observe key technical or business indicators, or reference them in [runbooks](https://docs.datadoghq.com/notebooks/) to provide additional context. With Dashboards, you can see snapshots of the current state of your platform as well as interactions, so you can preemptively see issues and analyze them more deeply in specialized pages.

The video below demonstrates a user looking at an overview dashboard for a web application. The user identifies a spike on a technical metric, zooms in for details, and accesses the underlying host dashboard to check for possible root causes.

{% video
   url="https://datadog-docs.imgix.net/images/dashboards/guide/context_links/overview.mp4" /%}

This guide introduces **context links** in your dashboards and covers the following:

1. How context links work, and how to adapt them to your exact needs.
1. Example use cases of the context links configuration.

## Introduction to context links{% #introduction-to-context-links %}

Context links bridge dashboard widgets with other pages in Datadog, as well as the third-party applications you have integrated into your workflows.

Users with [edit permissions](https://docs.datadoghq.com/dashboards/configure/#permissions) to dashboards can configure which links are accessible in the link list.

### Default context links{% #default-context-links %}

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/context_links/default-links.f50bfd1e045a80c5a9da8aebdb650242.png?auto=format"
   alt="Default links" /%}

By default, the widget menu displays links to your host, [traces](https://app.datadoghq.com/apm/traces/), and [logs](https://app.datadoghq.com/logs)âalong with links that correspond to the widget's data sources. For example, the menu displays a link to the [**RUM Explorer**](https://app.datadoghq.com/rum/explorer/) if your widget uses [RUM data](https://docs.datadoghq.com/real_user_monitoring/data_collected/). Click **More Related Data Actions** to see additional links in the dropdown menu.

The widget contains links to the following pages:

| Link        | Description                                                                                                                                                                                                                                                                            |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Hosts       | Links to the [Host Map](https://docs.datadoghq.com/infrastructure/hostmap/#overview) if series consists of more than one host. Links to the [Host Dashboard](https://docs.datadoghq.com/getting_started/dashboards/#explore-out-of-the-box-dashboards) if series consists of one host. |
| Containers  | Links to the [Live Container](https://docs.datadoghq.com/infrastructure/livecontainers/) page.                                                                                                                                                                                         |
| Processeses | Links to the [Live Process](https://docs.datadoghq.com/infrastructure/process/?tab=linuxwindows) page.                                                                                                                                                                                 |
| APM Traces  | Opens a side panel displaying underlying traces that link to the [Trace Explorer](https://docs.datadoghq.com/tracing/trace_explorer/?tab=listview).                                                                                                                                    |
| RUM Events  | Links to the [RUM Explorer](https://docs.datadoghq.com/real_user_monitoring/explorer/).                                                                                                                                                                                                |
| Profiles    | Links to the APM [Profile Explorer](https://docs.datadoghq.com/profiler/profile_visualizations/).                                                                                                                                                                                      |
| Logs        | Opens a side panel displaying underlying logs that link to the [Log Explorer](https://docs.datadoghq.com/logs/explorer/).                                                                                                                                                              |

When applicable, context links embed:

- A **filter** that combines the widget filter(s) with template variables (if any) and, for grouped-by queries, the one series users click on.
- A **time range**. For timeseries and heatmap widgets, the time range corresponds to the time bucket for the data point. For other widgets, the time range is the full widget time range.

### Customize context links{% #customize-context-links %}

For any [generic widget](https://docs.datadoghq.com/dashboards/widgets/), enter its edit mode to access its **Context Links** section. You can create your own context links, override default links, and promote or hide links.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/context_links/edit-links.7dbd7d1f3545a494623c578ab5caa8d8.png?auto=format"
   alt="Edit links" /%}

To define custom links or override the default links, specify the link name in the **Label** field and the link path in the **URL** field. Click **+ Add URL Parameter** to use the key-value helper.

#### Context Links variables{% #context-links-variables %}

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/context_links/custom-link.4c09cd3d399706a046207102329fa89d.png?auto=format"
   alt="Set a key-value pair for a URL parameter in the URL" /%}

Available variable types for context links include:

- **Time range variables** `{{timestamp_start}}` and `{{timestamp_end}}`. These variables correspond to the time range of the widget.
- **Query variables** (`{{@MerchantTier}}` and `{{@MerchantTier.value}}` in the example above). These variables are for widgets with grouped queries, and identify the specific group a user clicks on.
- **Dashboard template variables** (`{{$env}}` and `{{$env.value}}` in the example above). These variables identify the current value in use for the template variable when user clicks.
- **`{{tags}}`**, the default combination of all the variables above.

When you have to choose between `{{something}}` and `{{something.value}}`:

- `{{something}}` returns the value prefixed by its key. For example, `env:prod`.
- `{{something.value}}` returns the raw value. For example, `prod`.
- See the example use case to configure multiple variables.

In this example, when you click **View in Acme**, the link directs you to `https://prod.acme.io/search?what=basic&when=1643021787564`.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/context_links/view-in-acme.827e65139829fa6d359c8a4a71652bb9.png?auto=format"
   alt="Example context link to Acme" /%}

The context link:

- Replaces `{{env.value}}` with `prod`
- Replaces `{{@MerchantTier.value}}` with `basic`
- And replaces `{{timestamp_end}}` with `1643021787564`.

#### Bootstrap context link with copy-paste{% #bootstrap-context-link-with-copy-paste %}

{% video
   url="https://datadog-docs.imgix.net/images/dashboards/guide/context_links/override-link.mp4" /%}

For a complex context link that encodes a wide variety of parameters, it can be more convenient to copy-and-paste the entire URL in the **URL** field to bootstrap the configuration and rework the variables from there.

#### URL encoding{% #url-encoding %}

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/context_links/url-encoding.89ccdc659136e962698912efd3a8b00f.png?auto=format"
   alt="Screenshot of a URL and key-value parameters" /%}

Datadog handles URL encoding in context links.

The example above displays a link with a query parameter, `status:error source:nginx {{@shopist.webstore.merchant.tier}}`. Here, `{{@shopist.webstore.merchant.tier}}` is interpreted as `@shopist.webstore.merchant.tier:basic`. The full query parameter is then translated into `&query=status%3Aerror%20source%3Anginx%20%40shopist.webstore.merchant.tier%3Abasic`.

## Example use cases{% #example-use-cases %}

This section contains examples that demonstrate how you can take advantage of context links to integrate your dashboards into your workflows.

### Dashboards links to a customer support solution{% #dashboards-links-to-a-customer-support-solution %}

The following example explains how to create a link from a user in a dashboard to their corresponding Zendesk user page.

#### Context{% #context %}

You use Datadog to monitor your merchant website. Your customer support team uses a dashboard that your [Frontend](https://docs.datadoghq.com/real_user_monitoring/) and [Security](https://docs.datadoghq.com/security/cloud_siem/) teams set up to proactively identify your most engaged customersâor customers with a troublesome experience, and potentially reach out to them.

To accelerate this troubleshooting workflow, the customer support team would like a direct connection between dashboards and a support solution, for example: Zendesk.

#### Approach{% #approach %}

The primary ID that tracks logged users across your platform in Datadog is the user email, which is a facet that appears in some dashboard widgets.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/context_links/zendesk_query.33470de327adf2a9126c099c1a642811.png?auto=format"
   alt="Zendesk Query" /%}

A typical Zendesk link to search for users is `https://acme.zendesk.com/agent/search/1?type=user&q=email%3Ashane%40doe.com`, where the user's email is a search parameter.

Add a variable in the URL, and the templated link becomes `https://acme.zendesk.com/agent/search/1?type=user&q=email:{{@usr.email.value}}`.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/context_links/zendesk_link.c3938a589d7b22bca427629df2d2b60a.png?auto=format"
   alt="Zendesk User Page Context Link" /%}

#### Result{% #result %}

Your customer support team's dashboard widget contains a context link that takes you into the customer support platform with the appropriate context.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/context_links/zendesk_interaction.2d5f972862bafc5486cd88f79e2c694a.png?auto=format"
   alt="Zendesk User Page Context Link" /%}

Clicking the **Zendesk User Page** link directs you to this user's page in Zendesk.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/context_links/zendesk_result.d4503a6eacd7d7a4c74bbda6be79b065.png?auto=format"
   alt="Zendesk Result" /%}

### Dashboard links to the AWS Console{% #dashboard-links-to-the-aws-console %}

The following example explains how to create a link from a host in a dashboard widget to its corresponding Amazon EC2 instance page in the AWS Console.

#### Context{% #context-1 %}

Your platform is hosted on [Amazon EC2](https://docs.datadoghq.com/integrations/amazon_ec2/) instances, and the procedures to upscale and downscale your platform are mostly manual.

You have a dashboard where you've consolidated key health metrics for your infrastructure in Datadog.

To accelerate this operations workflow, you would like a direct connection between this dashboard and your [AWS Console](https://aws.amazon.com/console/)âfor example, to upgrade from `t2.micro` to `t2.large`.

#### Approach{% #approach-1 %}

A typical Amazon EC2 instance summary link is `https://eu-west-3.console.aws.amazon.com/ec2/v2/home?region=eu-west-3#InstanceDetails:instanceId=i-04b737b9f8bf94a94`, where you can read:

- `eu-west-3`: The data center region displayed as a subdomain and a URL parameter.
- `i-04b737b9f8bf94a94`: The host ID displayed as a hash parameter.

If your platform only runs on one region, inject the host ID into the context link template so that `https://eu-west-3.console.aws.amazon.com/ec2/v2/home?region=eu-west-3#InstanceDetails:instanceId={{host.value}}`.

If your platforms runs on multiple regions, your widget configuration depends on the following:

- If the region is part of the query aggregation (for example, in the screenshot below), the templated link is `https://{{region.value}}.console.aws.amazon.com/ec2/v2/home?region={{region.value}}#InstanceDetails:instanceId={{host.value}}`, where `{{region.value}}` is a **query** variable.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/context_links/ec2_query.e3d2e2a794795434016a7a5e2a01c7f3.png?auto=format"
   alt="Amazon EC2 Query" /%}

- If the region is part of the query aggregation (for example, in the screenshot below), the templated link is `https://{{$region.value}}.console.aws.amazon.com/ec2/v2/home?region={{$region.value}}#InstanceDetails:instanceId={{host.value}}`, where `{{region.value}}` is a **template** variable.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/context_links/ec2_query2.84a418c7c9da467d9900d590d7786bce.png?auto=format"
   alt="Amazon EC2 Query" /%}

#### Result{% #result-1 %}

Your dashboard widget contains a link that takes you to the appropriate host in the AWS Console.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/context_links/ec2_interaction.3327f225ea6b8347b0df4095c2a456db.png?auto=format"
   alt="Amazon EC2 Query context link" /%}

Clicking the **Amazon EC2 Instance Summary** link directs you to the Amazon EC2 instance page in the AWS Console.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/context_links/ec2_result.7b72e4c22e774f5c99856346d8bb7f0f.png?auto=format"
   alt="Amazon EC2 Query Result" /%}

### Dashboard links to saved views and remapped attributes in Datadog{% #dashboard-links-to-saved-views-and-remapped-attributes-in-datadog %}

The following example explains how to create a link from a RUM event in a dashboard widget to its corresponding logs.

#### Context{% #context-2 %}

You monitor your corporate website with Datadog. You may use [RUM](https://docs.datadoghq.com/real_user_monitoring/) to understand your users and [Logs](https://docs.datadoghq.com/logs/) to [oversee your API Gateways](https://docs.datadoghq.com/integrations/#cat-log-collection) from a more technical perspective.

Your frontend engineers typically use dashboards with high-level RUM insights. You API Gateways team maintains a [Saved View](https://docs.datadoghq.com/logs/explorer/saved_views/) in the Log Explorer, which is a fine-tuned perspective that the frontend monitoring team relies on to monitor information that is relevant to them.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/context_links/logs-saved-view_result.eb9d046f415995f2954c6ad5359b1f15.jpg?auto=format"
   alt="Logs Saved View result" /%}

To accelerate this troubleshooting workflow, the frontend monitoring teams would like to access the saved view with the current context of the dashboard.

#### Approach to Saved Views{% #approach-to-saved-views %}

[Saved Views](https://docs.datadoghq.com/logs/explorer/saved_views/) define the default query, visualization, and configuration options in the Log Explorer. A typical saved view link is `https://app.datadoghq.com/logs?saved_view=305130`, which encodes the Log Explorer URL under the hood.

You can append the saved view's short link to override any parameter in the resulting Log Explorer URL.

For example, `https://app.datadoghq.com/logs?saved_view=305130&query=@source:nginx @network.client.ip:123.123.12.1` takes you to the [Log Explorer](https://docs.datadoghq.com/logs/explorer/) as if you opened the saved view first, but the default query filter is replaced with `@source:nginx @network.client.ip:123.123.12.1`.

#### Approach to remapping attributes{% #approach-to-remapping-attributes %}

If navigation on your website is anonymous, you may use an IP address as a proxy to identify your users.

You would like to identify the `@session.ip` attribute from your RUM events with the `@network.client.ip` attribute from your logs. The two attributes have different names because they generally have different meanings, but in this context of authentication logs, you can identify both.

To do so, inject the `@session.ip` in a filter based on `@network.client.ip`, and build the appropriate filter `@network.client.ip:{{@session.ip.value}}`.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/context_links/logs-saved-view_query.21c00bdea17faae58819947779a30e5c.png?auto=format"
   alt="Example search query for saved views" /%}

For a RUM dashboard widget displaying insights per session IP and for specific countries, follow this link configuration.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/context_links/logs-saved-view_link.1d863f0ab4138fa38b89572fe389107b.png?auto=format"
   alt="Example URL configuration for saved views" /%}

#### Result{% #result-2 %}

As the API Gateways team updates the saved view to account for the latest updates on incoming logs, the context link remains up-to-date.

Remapping the IP address creates a context link that connects your RUM events with corresponding logs.

### Configure multiple variables{% #configure-multiple-variables %}

The following example explains how to configure multiple variables and conditions in your context link query.

#### Context{% #context-3 %}

Add context links to investigate specific logs or conditions.

- You have multiple tag values with the same context (for example, `env:production OR env:prod`).
- You want to filter down logs to multiple conditions (for example, `env:prod AND service:backend`)

#### Approach{% #approach-2 %}

After you select the template variables you want to troubleshoot, the context link configuration takes those template variables and inserts them into the query. **Note**: The syntax and the parenthesis enclosure impacts the query.

For example, if you want to configure a context link with `service:backend` AND (`env:production` OR `env:prod`), use the following configuration:

```
service:backend (env:{{$env.value}})
```

#### Result{% #result-3 %}

The parenthesis translates the `(env:{{$env.value}})` to `(env:*)` which allows you to enter multiple variables into your context links query.

## Further Reading{% #further-reading %}

- [Design effective executive dashboards with Datadog](https://www.datadoghq.com/blog/datadog-executive-dashboards)
- [Dashboard widget list](https://docs.datadoghq.com/dashboards/widgets)
- [Metrics Units](https://docs.datadoghq.com/metrics/units)
