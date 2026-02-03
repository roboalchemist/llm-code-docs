# Source: https://docs.datadoghq.com/continuous_integration/explorer/search_syntax.md

# Source: https://docs.datadoghq.com/continuous_delivery/explorer/search_syntax.md

---
title: CD Visibility Explorer Search Syntax
description: Search all of your deployment executions.
breadcrumbs: >-
  Docs > Continuous Delivery Visibility > Explore CD Visibility Deployments > CD
  Visibility Explorer Search Syntax
---

# CD Visibility Explorer Search Syntax

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% callout %}
##### Join the Preview!

CD Visibility is in Preview. If you're interested in this feature, complete the form to request access.

[Request Access](https://docs.google.com/forms/d/e/1FAIpQLScNhFEUOndGHwBennvUp6-XoA9luTc27XBwtSgXhycBVFM9yA/viewform?usp=sf_link)
{% /callout %}

## Overview{% #overview %}

A query filter is composed of terms and operators.

There are two types of terms:

- A **single term** is a single word such as `test` or `hello`.

- A **sequence** is a group of words surrounded by double quotes, such as `"hello dolly"`.

To combine multiple terms into a complex query, you can use any of the following case sensitive Boolean operators:

| **Operator** | **Description**                                                                                        | **Example**                  |
| ------------ | ------------------------------------------------------------------------------------------------------ | ---------------------------- |
| `AND`        | **Intersection**: both terms are in the selected events (if nothing is added, AND is taken by default) | authentication AND failure   |
| `OR`         | **Union**: either term is contained in the selected events                                             | authentication OR password   |
| `-`          | **Exclusion**: the following term is NOT in the event (apply to each individual raw text search)       | authentication AND -password |

## Further reading{% #further-reading %}

- [Getting Started with Search in Datadog](https://docs.datadoghq.com/getting_started/search/)
- [Learn about facets](https://docs.datadoghq.com/continuous_delivery/explorer/facets)
