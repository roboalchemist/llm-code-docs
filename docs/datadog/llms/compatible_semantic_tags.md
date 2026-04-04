# Source: https://docs.datadoghq.com/dashboards/guide/compatible_semantic_tags.md

---
title: Compatible semantic tags
description: >-
  Use meaning-driven semantic color palettes that automatically map compatible
  tags to consistent colors across charts.
breadcrumbs: Docs > Dashboards > Graphing Guides > Compatible semantic tags
---

# Compatible semantic tags

## Overview{% #overview %}

For compatible series of data, Datadog can map colors to meaning. When a compatible tag is detected, Datadog suggests the Semantic color palette. This automatically maps data to meaning-driven colors.

**Note**: To use the Semantic color palette, a query must be grouped with a single set of tags.

### Map compatible tags to colors based on their meaning{% #map-compatible-tags-to-colors-based-on-their-meaning %}

For example, an error status code is mapped to red, and success to green.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/compatible_semantic_tags/semantic_option.6203ca3703f830799328b4e58b9df529.png?auto=format"
   alt="Semantic color option in the graph editor" /%}

### Ensure consistent coloring across charts{% #ensure-consistent-coloring-across-charts %}

Charts with a semantic palette use the same, stable color for each tag. This allows you to easily trace a given tag across different graphs.

### Grouping behavior{% #grouping-behavior %}

Queries grouped with a single set of tags are supported. If multiple groupers are used with the semantic palette, coloring is consistent, but not meaning-driven.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/compatible_semantic_tags/multiple_tags.d6f1bcf27d49a53ee4a16592f6799b3b.png?auto=format"
   alt="Example of multiple tag graph using semantic palette" /%}

For example, consider a query that uses both the `Status` and `Service` tags. Even if the semantic palette is selected, the colors in the chart no longer correspond to a specific meaning (as in, red no longer necessarily indicates "bad"). However, each status/service combination retains consistent coloring for all charts.

## Supported tag keys{% #supported-tag-keys %}

| Tag key                               | Description                                                                                                                                                                                                                                                                                                    |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `status`                              | Used by [Logs standard attributes](https://docs.datadoghq.com/logs/log_configuration/attributes_naming_convention/#reserved-attributes) and [Datadog Security](https://docs.datadoghq.com/security/) for severity level. Also supports generic success, fail, pass, error for convenience with custom metrics. |
| `http.status_code`                    | Standard tag used in many integrations. Colors are assigned based on HTTP status code family (1xx, 2xx, 3xx, 4xx, 5xx)                                                                                                                                                                                         |
| `@ci.status`                          | Used by [CI Visibility](https://docs.datadoghq.com/continuous_integration/)                                                                                                                                                                                                                                    |
| `@test.status`                        | Used by [Test Optimization](https://docs.datadoghq.com/tests/)                                                                                                                                                                                                                                                 |
| `@static_analysis.result.status`      | Used by [Code Security](https://docs.datadoghq.com/security/code_security/)                                                                                                                                                                                                                                    |
| `@static_analysis.result.k9_severity` | Used by [Code Security](https://docs.datadoghq.com/security/code_security/) and [CSM IaC](https://docs.datadoghq.com/security/cloud_security_management/setup/iac_scanning)                                                                                                                                    |
| `@dependency.severity`                | Used by [Code Security](https://docs.datadoghq.com/security/code_security/)                                                                                                                                                                                                                                    |
| `@deployment.status`                  | Used by [CD Visibility](https://docs.datadoghq.com/continuous_delivery/)                                                                                                                                                                                                                                       |
| `@evaluation.status`                  | Used by [Quality Gates](https://docs.datadoghq.com/quality_gates/)                                                                                                                                                                                                                                             |
| `evaluation`                          | Used by [Cloud Security](https://www.datadoghq.com/product/cloud-security-management/)                                                                                                                                                                                                                         |
| `severity`                            | Used by [Cloud Security](https://www.datadoghq.com/product/cloud-security-management/)                                                                                                                                                                                                                         |
| `@resource.status_code`               | Used by [RUM & Session Replay](https://docs.datadoghq.com/real_user_monitoring/). Uses the same colors as `http.status_code`.                                                                                                                                                                                  |
| `@error.resource.status_code`         | Used by [RUM & Session Replay](https://docs.datadoghq.com/real_user_monitoring/). Uses the same colors as `http.status_code`.                                                                                                                                                                                  |
| `@batch.status`                       | Used by [Synthetic Monitoring](https://docs.datadoghq.com/synthetics/) for test batch results.                                                                                                                                                                                                                 |
| `@suite.status`                       | Used by [Synthetic Monitoring](https://docs.datadoghq.com/synthetics/) for test suite results.                                                                                                                                                                                                                 |
| `@result.status`                      | Used by [Synthetic Monitoring](https://docs.datadoghq.com/synthetics/) for test run results.                                                                                                                                                                                                                   |

## Further reading{% #further-reading %}

- [Selecting the right colors for your graphs](https://docs.datadoghq.com/dashboards/guide/widget_colors/#categorical-palettes)
