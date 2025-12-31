# Source: https://docs.vllm.ai/en/stable/examples/online_serving/dashboards/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/online_serving/dashboards.md "Edit this page")

# Monitoring Dashboards[¶](#monitoring-dashboards "Permanent link")

Source <https://github.com/vllm-project/vllm/tree/main/examples/online_serving/dashboards>.

This directory contains monitoring dashboard configurations for vLLM, providing comprehensive observability for your vLLM deployments.

## Dashboard Platforms[¶](#dashboard-platforms "Permanent link")

We provide dashboards for two popular observability platforms:

-   **[Grafana](https://grafana.com)**
-   **[Perses](https://perses.dev)**

## Dashboard Format Approach[¶](#dashboard-format-approach "Permanent link")

All dashboards are provided in **native formats** that work across different deployment methods:

### Grafana (JSON)[¶](#grafana-json "Permanent link")

-   ✅ Works with any Grafana instance (cloud, self-hosted, Docker)
-   ✅ Direct import via Grafana UI or API
-   ✅ Can be wrapped in Kubernetes operators when needed
-   ✅ No vendor lock-in or deployment dependencies

### Perses (YAML)[¶](#perses-yaml "Permanent link")

-   ✅ Works with standalone Perses instances
-   ✅ Compatible with Perses API and CLI
-   ✅ Supports Dashboard-as-Code workflows
-   ✅ Can be wrapped in Kubernetes operators when needed

## Dashboard Contents[¶](#dashboard-contents "Permanent link")

Both platforms provide equivalent monitoring capabilities:

  Dashboard                    Description
  ---------------------------- ------------------------------------------------------
  **Performance Statistics**   Tracks latency, throughput, and performance metrics
  **Query Statistics**         Monitors request volume, query performance, and KPIs

## Quick Start[¶](#quick-start "Permanent link")

First, navigate to this example\'s directory:

    cd examples/online_serving/dashboards

### Grafana[¶](#grafana "Permanent link")

Import the JSON directly into the Grafana UI, or use the API:

    curl -X POST http://grafana/api/dashboards/db \
      -H "Content-Type: application/json" \
      -d @grafana/performance_statistics.json

### Perses[¶](#perses "Permanent link")

Import via the Perses CLI:

    percli apply -f perses/performance_statistics.yaml

## Requirements[¶](#requirements "Permanent link")

-   **Prometheus** metrics from your vLLM deployment
-   **Data source** configured in your monitoring platform
-   **vLLM metrics** enabled and accessible

## Platform-Specific Documentation[¶](#platform-specific-documentation "Permanent link")

For detailed deployment instructions and platform-specific options, see:

-   **[Grafana Documentation](https://github.com/vllm-project/vllm/tree/main/examples/online_serving/dashboards/grafana)** - JSON dashboards, operator usage, manual import
-   **[Perses Documentation](https://github.com/vllm-project/vllm/tree/main/examples/online_serving/dashboards/perses)** - YAML specs, CLI usage, operator wrapping

## Contributing[¶](#contributing "Permanent link")

When adding new dashboards, please:

1.  Provide native formats (JSON for Grafana, YAML specs for Perses)
2.  Update platform-specific README files
3.  Ensure dashboards work across deployment methods
4.  Test with the latest platform versions

## Example materials[¶](#example-materials "Permanent link")

grafana/README.md

# Grafana Dashboards for vLLM Monitoring[¶](#grafana-dashboards-for-vllm-monitoring "Permanent link")

This directory contains Grafana dashboard configurations (as JSON) designed to monitor vLLM performance and metrics.

## Requirements[¶](#requirements_1 "Permanent link") 

-   Grafana 8.0+
-   Prometheus data source configured in Grafana
-   vLLM deployment with Prometheus metrics enabled

## Dashboard Descriptions[¶](#dashboard-descriptions "Permanent link")

-   **performance_statistics.json**: Tracks performance metrics including latency and throughput for your vLLM service.
-   **query_statistics.json**: Tracks query performance, request volume, and key performance indicators for your vLLM service.

## Deployment Options[¶](#deployment-options "Permanent link")

### Manual Import (Recommended)[¶](#manual-import-recommended "Permanent link")

The easiest way to use these dashboards is to manually import the JSON configurations directly into your Grafana instance:

1.  Navigate to your Grafana instance
2.  Click the \'+\' icon in the sidebar
3.  Select \'Import\'
4.  Copy and paste the JSON content from the dashboard files, or upload the JSON files directly

### Grafana Operator[¶](#grafana-operator "Permanent link")

If you\'re using the [Grafana Operator](https://github.com/grafana-operator/grafana-operator) in Kubernetes, you can wrap these JSON configurations in a `GrafanaDashboard` custom resource:

    # Note: Adjust the instanceSelector to match your Grafana instance's labels
    # You can check with: kubectl get grafana -o yaml
    apiVersion: grafana.integreatly.org/v1beta1
    kind: GrafanaDashboard
    metadata:
      name: vllm-performance-dashboard
    spec:
      instanceSelector:
        matchLabels:
          dashboards: grafana  # Adjust to match your Grafana instance labels
      folder: "vLLM Monitoring"
      json: |
        # Replace this comment with the complete JSON content from
        # performance_statistics.json - The JSON should start with 

Then apply to your cluster:

    kubectl apply -f your-dashboard.yaml -n <namespace>

grafana/performance_statistics.json

    ,
            "enable": true,
            "hide": true,
            "iconColor": "rgba(0, 211, 255, 1)",
            "name": "Annotations & Alerts",
            "type": "dashboard"
          }
        ]
      },
      "editable": true,
      "fiscalYearStartMonth": 0,
      "graphTooltip": 0,
      "id": 26,
      "links": [],
      "panels": [
        ,
          "id": 9,
          "panels": [],
          "title": "Graph: E2E latency over time ",
          "type": "row"
        },
        "
          },
          "description": "End-to-End latency of requests, showing average and key percentiles over time.",
          "fieldConfig": ,
              "custom": ,
                "insertNulls": false,
                "lineInterpolation": "linear",
                "lineWidth": 1,
                "pointSize": 5,
                "scaleDistribution": ,
                "showPoints": "auto",
                "spanNulls": true,
                "stacking": ,
                "thresholdsStyle": 
              },
              "decimals": 2,
              "mappings": [],
              "thresholds": ,
                  
                ]
              },
              "unit": "s"
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 1,
          "options": ,
            "tooltip": 
          },
          "pluginVersion": "11.3.0",
          "targets": [
            "
              },
              "editorMode": "code",
              "expr": "rate(vllm:e2e_request_latency_seconds_sum[$__interval]) / rate(vllm:e2e_request_latency_seconds_count[$__interval])",
              "format": "table",
              "legendFormat": "E2E Latency",
              "range": true,
              "refId": "A"
            }
          ],
          "title": "E2E Latency over Time",
          "type": "timeseries"
        },
        "
          },
          "description": "99th percentile of End-to-End request latency over the selected time range.",
          "fieldConfig": ,
              "decimals": 2,
              "displayName": "P99",
              "mappings": [],
              "thresholds": ,
                  
                ]
              },
              "unit": "s"
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 5,
          "options": ,
            "showPercentChange": false,
            "textMode": "auto",
            "wideLayout": true
          },
          "pluginVersion": "11.3.0",
          "targets": [
            
          ],
          "title": "E2E Latency (P99)",
          "type": "stat"
        },
        "
          },
          "description": "90th percentile of End-to-End request latency over the selected time range.",
          "fieldConfig": ,
              "decimals": 2,
              "displayName": "P90",
              "mappings": [],
              "thresholds": ,
                  
                ]
              },
              "unit": "s"
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 4,
          "options": ,
            "showPercentChange": false,
            "textMode": "auto",
            "wideLayout": true
          },
          "pluginVersion": "11.3.0",
          "targets": [
            
          ],
          "title": "E2E Latency (P90)",
          "type": "stat"
        },
        "
          },
          "description": "Average End-to-End request latency over the selected time range.",
          "fieldConfig": ,
              "decimals": 2,
              "displayName": "Average",
              "mappings": [],
              "thresholds": ,
                  
                ]
              },
              "unit": "s"
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 2,
          "options": ,
            "showPercentChange": false,
            "textMode": "auto",
            "wideLayout": true
          },
          "pluginVersion": "11.3.0",
          "targets": [
            
          ],
          "title": "E2E Latency (Avg)",
          "type": "stat"
        },
        "
          },
          "description": "50th percentile (median) of End-to-End request latency over the selected time range.",
          "fieldConfig": ,
              "decimals": 2,
              "displayName": "P50",
              "mappings": [],
              "thresholds": ,
                  
                ]
              },
              "unit": "s"
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 3,
          "options": ,
            "showPercentChange": false,
            "textMode": "auto",
            "wideLayout": true
          },
          "pluginVersion": "11.3.0",
          "targets": [
            
          ],
          "title": "E2E Latency (P50)",
          "type": "stat"
        },
        ,
          "id": 8,
          "panels": [],
          "title": "Graph: TTFT(Time To First Token) over time ",
          "type": "row"
        },
        "
          },
          "description": "Time to first token (TTFT) latency, showing average and key percentiles over time.",
          "fieldConfig": ,
              "custom": ,
                "insertNulls": false,
                "lineInterpolation": "linear",
                "lineWidth": 1,
                "pointSize": 5,
                "scaleDistribution": ,
                "showPoints": "auto",
                "spanNulls": false,
                "stacking": ,
                "thresholdsStyle": 
              },
              "decimals": 2,
              "mappings": [],
              "thresholds": ,
                  
                ]
              },
              "unit": "s"
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 10,
          "options": ,
            "tooltip": 
          },
          "pluginVersion": "11.3.0",
          "targets": [
            
          ],
          "title": "TTFT Over Time",
          "type": "timeseries"
        },
        "
          },
          "description": "99th percentile of Time To First Token latency over the selected time range.",
          "fieldConfig": ,
              "decimals": 2,
              "displayName": "P99",
              "mappings": [],
              "thresholds": ,
                  
                ]
              },
              "unit": "s"
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 14,
          "options": ,
            "showPercentChange": false,
            "textMode": "auto",
            "wideLayout": true
          },
          "pluginVersion": "11.3.0",
          "targets": [
            
          ],
          "title": "TTFT (P99)",
          "type": "stat"
        },
        "
          },
          "description": "90th percentile of Time To First Token latency over the selected time range.",
          "fieldConfig": ,
              "decimals": 2,
              "displayName": "P90",
              "mappings": [],
              "thresholds": ,
                  
                ]
              },
              "unit": "s"
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 13,
          "options": ,
            "showPercentChange": false,
            "textMode": "auto",
            "wideLayout": true
          },
          "pluginVersion": "11.3.0",
          "targets": [
            
          ],
          "title": "TTFT (P90)",
          "type": "stat"
        },
        "
          },
          "description": "Average Time To First Token latency over the selected time range.",
          "fieldConfig": ,
              "decimals": 2,
              "displayName": "Average",
              "mappings": [],
              "thresholds": ,
                  
                ]
              },
              "unit": "s"
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 11,
          "options": ,
            "showPercentChange": false,
            "textMode": "auto",
            "wideLayout": true
          },
          "pluginVersion": "11.3.0",
          "targets": [
            
          ],
          "title": "TTFT (Avg)",
          "type": "stat"
        },
        "
          },
          "description": "50th percentile (median) of Time To First Token latency over the selected time range.",
          "fieldConfig": ,
              "displayName": "P50",
              "mappings": [],
              "thresholds": ,
                  
                ]
              },
              "unit": "s"
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 12,
          "options": ,
            "showPercentChange": false,
            "textMode": "auto",
            "wideLayout": true
          },
          "pluginVersion": "11.3.0",
          "targets": [
            
          ],
          "title": "TTFT (P50)",
          "type": "stat"
        },
        ,
          "id": 7,
          "panels": [],
          "title": "ITL (Iteration Latency / Time Per Output Token) over time.",
          "type": "row"
        },
        "
          },
          "description": "Iteration latency, or average time taken to generate a single output token, with percentiles.",
          "fieldConfig": ,
              "custom": ,
                "insertNulls": false,
                "lineInterpolation": "linear",
                "lineWidth": 1,
                "pointSize": 5,
                "scaleDistribution": ,
                "showPoints": "auto",
                "spanNulls": false,
                "stacking": ,
                "thresholdsStyle": 
              },
              "decimals": 2,
              "mappings": [],
              "thresholds": ,
                  
                ]
              },
              "unit": "s"
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 15,
          "options": ,
            "tooltip": 
          },
          "pluginVersion": "11.3.0",
          "targets": [
            ,
            "
              },
              "editorMode": "code",
              "expr": "histogram_quantile(0.50, sum by(le) (rate(vllm:time_per_output_token_seconds_bucket[$__interval])))",
              "hide": false,
              "instant": false,
              "legendFormat": "ITL (p50)",
              "range": true,
              "refId": "B"
            },
            "
              },
              "editorMode": "code",
              "expr": "histogram_quantile(0.90, sum by(le) (rate(vllm:time_per_output_token_seconds_bucket[$__interval])))",
              "hide": false,
              "instant": false,
              "legendFormat": "ITL (p90)",
              "range": true,
              "refId": "C"
            },
            "
              },
              "editorMode": "code",
              "expr": "histogram_quantile(0.99, sum by(le) (rate(vllm:time_per_output_token_seconds_bucket[$__interval])))",
              "hide": false,
              "instant": false,
              "legendFormat": "ITL (p99)",
              "range": true,
              "refId": "D"
            }
          ],
          "title": "ITL (Time Per Output Token) Over Time",
          "type": "timeseries"
        },
        "
          },
          "description": "90th percentile of Iteration Latency over the selected time range.",
          "fieldConfig": ,
              "decimals": 2,
              "mappings": [],
              "thresholds": ,
                  
                ]
              },
              "unit": "s"
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 18,
          "options": ,
            "showPercentChange": false,
            "textMode": "auto",
            "wideLayout": true
          },
          "pluginVersion": "11.3.0",
          "targets": [
            
          ],
          "title": "ITL (P90)",
          "type": "stat"
        },
        "
          },
          "description": "99th percentile of Iteration Latency over the selected time range.\n\n",
          "fieldConfig": ,
              "decimals": 2,
              "mappings": [],
              "thresholds": ,
                  
                ]
              },
              "unit": "s"
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 19,
          "options": ,
            "showPercentChange": false,
            "textMode": "auto",
            "wideLayout": true
          },
          "pluginVersion": "11.3.0",
          "targets": [
            
          ],
          "title": "ITL (P99)",
          "type": "stat"
        },
        "
          },
          "description": "Average Iteration Latency (time per output token) over the selected time range.",
          "fieldConfig": ,
              "decimals": 2,
              "mappings": [],
              "thresholds": ,
                  
                ]
              },
              "unit": "s"
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 16,
          "options": ,
            "showPercentChange": false,
            "textMode": "auto",
            "wideLayout": true
          },
          "pluginVersion": "11.3.0",
          "targets": [
            
          ],
          "title": "ITL (Avg)",
          "type": "stat"
        },
        "
          },
          "description": "50th percentile (median) of Iteration Latency over the selected time range.",
          "fieldConfig": ,
              "decimals": 2,
              "mappings": [],
              "thresholds": ,
                  
                ]
              },
              "unit": "s"
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 17,
          "options": ,
            "showPercentChange": false,
            "textMode": "auto",
            "wideLayout": true
          },
          "pluginVersion": "11.3.0",
          "targets": [
            
          ],
          "title": "ITL (P50)",
          "type": "stat"
        },
        ,
          "id": 6,
          "panels": [],
          "title": "TPS (Tokens Per Second)",
          "type": "row"
        },
        "
          },
          "description": "Rate of tokens processed per second, including prompt and generation phases.",
          "fieldConfig": ,
              "custom": ,
                "insertNulls": false,
                "lineInterpolation": "linear",
                "lineWidth": 1,
                "pointSize": 5,
                "scaleDistribution": ,
                "showPoints": "auto",
                "spanNulls": false,
                "stacking": ,
                "thresholdsStyle": 
              },
              "mappings": [],
              "thresholds": ,
                  
                ]
              },
              "unit": "tokens/sec (tps)"
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 20,
          "options": ,
            "tooltip": 
          },
          "pluginVersion": "11.3.0",
          "targets": [
            ,
            "
              },
              "editorMode": "code",
              "expr": "rate(vllm:prompt_tokens_total[$__interval])",
              "hide": false,
              "instant": false,
              "legendFormat": "Prompt TPS",
              "range": true,
              "refId": "B"
            },
            "
              },
              "editorMode": "code",
              "expr": "rate(vllm:iteration_tokens_total_count[$__interval])",
              "hide": false,
              "instant": false,
              "legendFormat": "Overall Iteration TPS",
              "range": true,
              "refId": "C"
            }
          ],
          "title": "TPS (Tokens Per Second) Over Time",
          "type": "timeseries"
        }
      ],
      "preload": false,
      "schemaVersion": 40,
      "tags": [],
      "templating": 
          },
          ,
            "label": "Aggregation",
            "name": "agg_method",
            "options": [
              
            ],
            "query": "avg : Average\n0.50 : P50\n0.90 : P90\n0.99 : P99\n0.999 : Max (Approx)",
            "type": "custom"
          },
          ,
            "definition": "label_values(vllm:generation_tokens_total,model_name)",
            "includeAll": true,
            "label": "Deployment_ID",
            "multi": true,
            "name": "Deployment_id",
            "options": [],
            "query": ,
            "refresh": 1,
            "regex": "",
            "type": "query"
          }
        ]
      },
      "time": ,
      "timezone": "browser",
      "uid": "performance-statistics",
      "title": "Performance Statistics",
      "version": 40,
      "weekStart": ""
    }

grafana/query_statistics.json

    ,
            "enable": true,
            "hide": true,
            "iconColor": "rgba(0, 211, 255, 1)",
            "name": "Annotations & Alerts",
            "type": "dashboard"
          }
        ]
      },
      "description": "High-level overview of VLLM model deployment behavior and key performance indicators. Designed for Data Scientists and Product Managers to monitor request volume, token throughput, and latency",
      "editable": true,
      "fiscalYearStartMonth": 0,
      "graphTooltip": 0,
      "id": 47,
      "links": [],
      "panels": [
        ,
          "id": 20,
          "panels": [],
          "title": "Request Over Time",
          "type": "row"
        },
        " },
          "fieldConfig": ,
              "custom": ,
                "insertNulls": false,
                "lineInterpolation": "linear",
                "lineWidth": 1,
                "pointSize": 5,
                "scaleDistribution": ,
                "showPoints": "auto",
                "spanNulls": false,
                "stacking": ,
                "thresholdsStyle": 
              },
              "mappings": [],
              "thresholds": , ]
              },
              "unit": "req/s"
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 1,
          "options": ,
            "tooltip": 
          },
          "pluginVersion": "11.3.0",
          "targets": [
            " },
              "editorMode": "code",
              "expr": "sum by (model_name) (\n  rate(vllm:request_success_total[$__rate_interval])\n)",
              "interval": "1",
              "legendFormat": "}",
              "range": true,
              "refId": "A"
            }
          ],
          "title": "Successful Requests Over Time",
          "type": "timeseries"
        },
        " },
          "fieldConfig": ,
              "mappings": [],
              "thresholds": , ]
              },
              "unit": "req/s"
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 2,
          "options": ,
            "showPercentChange": false,
            "textMode": "auto",
            "wideLayout": true
          },
          "pluginVersion": "11.3.0",
          "targets": [
            [$__rate_interval]))",
              "legendFormat": "__auto",
              "range": true,
              "refId": "A"
            }
          ],
          "title": "Requests Avg Rate",
          "type": "stat"
        },
        " },
          "fieldConfig": ,
              "mappings": [
                 }, "type": "value" }
              ],
              "thresholds": , ]
              },
              "unit": "ms"
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 3,
          "options": ,
            "showPercentChange": false,
            "textMode": "auto",
            "wideLayout": true
          },
          "pluginVersion": "11.3.0",
          "targets": [
            [$__rate_interval])))",
              "legendFormat": "__auto",
              "range": true,
              "refId": "A"
            }
          ],
          "title": "p50 Latency",
          "type": "stat"
        },
        " },
          "fieldConfig": ,
              "mappings": [
                 }, "type": "value" }
              ],
              "thresholds": , ]
              },
              "unit": "ms"
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 4,
          "options": ,
            "showPercentChange": false,
            "textMode": "auto",
            "wideLayout": true
          },
          "pluginVersion": "11.3.0",
          "targets": [
            [$__rate_interval])))",
              "legendFormat": "__auto",
              "range": true,
              "refId": "A"
            }
          ],
          "title": "p90 Latency",
          "type": "stat"
        },
        " },
          "fieldConfig": ,
              "mappings": [
                 }, "type": "value" }
              ],
              "thresholds": , ]
              },
              "unit": "ms"
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 5,
          "options": ,
            "showPercentChange": false,
            "textMode": "auto",
            "wideLayout": true
          },
          "pluginVersion": "11.3.0",
          "targets": [
            [$__rate_interval])))",
              "legendFormat": "__auto",
              "range": true,
              "refId": "A"
            }
          ],
          "title": "p99 Latency",
          "type": "stat"
        },
        ,
          "id": 19,
          "panels": [],
          "title": "Size Distribution",
          "type": "row"
        },
        " },
          "fieldConfig": ,
              "custom": ,
                "lineWidth": 1,
                "stacking": 
              },
              "mappings": [],
              "thresholds": , ]
              },
              "unit": "cps"
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 6,
          "options": ,
            "tooltip": 
          },
          "pluginVersion": "11.3.0",
          "targets": [
            [$__rate_interval]))",
              "legendFormat": "} le=}",
              "range": true,
              "refId": "A"
            }
          ],
          "title": "Input Token Size Distribution",
          "type": "histogram"
        },
        " },
          "fieldConfig": ,
              "mappings": [
                 }, "type": "value" }
              ],
              "thresholds": , ]
              },
              "unit": "cps"
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 9,
          "options": ,
            "showPercentChange": false,
            "textMode": "auto",
            "wideLayout": true
          },
          "pluginVersion": "11.3.0",
          "targets": [
            [$__rate_interval])))",
              "legendFormat": "__auto",
              "range": true,
              "refId": "A"
            }
          ],
          "title": "Input Token Size p90",
          "type": "stat"
        },
        " },
          "fieldConfig": ,
              "mappings": [
                 }, "type": "value" }
              ],
              "thresholds": , ]
              },
              "unit": "cps"
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 8,
          "options": ,
            "showPercentChange": false,
            "textMode": "auto",
            "wideLayout": true
          },
          "pluginVersion": "11.3.0",
          "targets": [
            [$__rate_interval])))",
              "legendFormat": "__auto",
              "range": true,
              "refId": "A"
            }
          ],
          "title": "Input Token Size p50",
          "type": "stat"
        },
        " },
          "fieldConfig": ,
              "mappings": [
                 }, "type": "value" }
              ],
              "thresholds": , ]
              },
              "unit": "cps"
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 7,
          "options": ,
            "showPercentChange": false,
            "textMode": "auto",
            "wideLayout": true
          },
          "pluginVersion": "11.3.0",
          "targets": [
            [$__rate_interval]))\n/\nsum(rate(vllm:request_success_total[$__rate_interval]))",
              "legendFormat": "__auto",
              "range": true,
              "refId": "A"
            }
          ],
          "title": "Input Token Size Avg",
          "type": "stat"
        },
        " },
          "fieldConfig": ,
              "mappings": [
                 }, "type": "value" }
              ],
              "thresholds": , ]
              },
              "unit": "cps"
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 10,
          "options": ,
            "showPercentChange": false,
            "textMode": "auto",
            "wideLayout": true
          },
          "pluginVersion": "11.3.0",
          "targets": [
            [$__rate_interval])))",
              "legendFormat": "__auto",
              "range": true,
              "refId": "A"
            }
          ],
          "title": "Input Token Size p99",
          "type": "stat"
        },
        ,
          "id": 18,
          "panels": [],
          "title": "Input Token Over Time",
          "type": "row"
        },
        " },
          "fieldConfig": ,
              "custom": ,
                "insertNulls": false,
                "lineInterpolation": "linear",
                "lineWidth": 1,
                "pointSize": 5,
                "scaleDistribution": ,
                "showPoints": "auto",
                "spanNulls": false,
                "stacking": ,
                "thresholdsStyle": 
              },
              "mappings": [],
              "thresholds": , ]
              },
              "unit": "cps"
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 11,
          "options": ,
            "tooltip": 
          },
          "pluginVersion": "11.3.0",
          "targets": [
            [$__rate_interval]))",
              "legendFormat": "}",
              "range": true,
              "refId": "A"
            }
          ],
          "title": "Input Tokens Over Time",
          "type": "timeseries"
        },
        " },
          "fieldConfig": ,
              "mappings": [
                 }, "type": "value" }
              ],
              "thresholds": , ]
              },
              "unit": "cps"
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 12,
          "options": ,
            "showPercentChange": false,
            "textMode": "auto",
            "wideLayout": true
          },
          "pluginVersion": "11.3.0",
          "targets": [
            [$__rate_interval]))",
              "legendFormat": "__auto",
              "range": true,
              "refId": "A"
            }
          ],
          "title": "Input Tokens/Sec Avg",
          "type": "stat"
        },
        ,
          "id": 17,
          "panels": [],
          "title": "Output Token Over Time",
          "type": "row"
        },
        " },
          "fieldConfig": ,
              "custom": ,
                "insertNulls": false,
                "lineInterpolation": "linear",
                "lineWidth": 1,
                "pointSize": 5,
                "scaleDistribution": ,
                "showPoints": "auto",
                "spanNulls": false,
                "stacking": ,
                "thresholdsStyle": 
              },
              "mappings": [],
              "thresholds": , ]
              },
              "unit": "cps"
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 13,
          "options": ,
            "tooltip": 
          },
          "pluginVersion": "11.3.0",
          "targets": [
            [$__rate_interval]))",
              "legendFormat": "}",
              "range": true,
              "refId": "A"
            }
          ],
          "title": "Output Tokens Over Time",
          "type": "timeseries"
        },
        " },
          "fieldConfig": ,
              "mappings": [
                 }, "type": "value" }
              ],
              "thresholds": , ]
              },
              "unit": "cps"
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 14,
          "options": ,
            "showPercentChange": false,
            "textMode": "auto",
            "wideLayout": true
          },
          "pluginVersion": "11.3.0",
          "targets": [
            [$__rate_interval]))",
              "legendFormat": "__auto",
              "range": true,
              "refId": "A"
            }
          ],
          "title": "Output Tokens/Sec Avg",
          "type": "stat"
        }
      ],
      "preload": false,
      "schemaVersion": 40,
      "tags": [],
      "templating": ,
            "label": "datasource",
            "name": "DS_PROMETHEUS",
            "options": [],
            "query": "prometheus",
            "refresh": 1,
            "type": "datasource"
          },
          ,
            "definition": "label_values(vllm:request_success_total,model_name)",
            "includeAll": true,
            "label": "Deployment_ID",
            "multi": true,
            "name": "Deployment_id",
            "options": [],
            "query": ,
            "refresh": 1,
            "regex": "",
            "sort": 1,
            "type": "query"
          },
          ,
            "hide": 2,
            "label": "Rush Hours Only",
            "name": "rush_hours",
            "options": [
              ,
              
            ],
            "query": "false : All hours, true : Rush hours",
            "type": "custom"
          },
          ,
            "hide": 2,
            "label": "Rush Hours Type",
            "name": "rush_hours_type",
            "options": [
              ,
              ,
              
            ],
            "query": "^All__.*$ : All, ^Static__.*$ : Static, ^Dynamic__.*$ : Dynamic",
            "type": "custom"
          },
          ,
            "hide": 2,
            "name": "query0",
            "options": [],
            "query": "",
            "refresh": 1,
            "regex": "",
            "type": "query"
          }
        ]
      },
      "time": ,
      "timepicker": ,
      "timezone": "browser",
      "title": "Query Statistics_New4",
      "uid": "query-statistics4",
      "version": 2,
      "weekStart": ""
    }

perses/README.md

# Perses Dashboards for vLLM Monitoring[¶](#perses-dashboards-for-vllm-monitoring "Permanent link")

This directory contains Perses dashboard configurations designed to monitor vLLM performance and metrics.

## Requirements[¶](#requirements_2 "Permanent link") 

-   Perses instance (standalone or via operator)
-   Prometheus data source configured in Perses
-   vLLM deployment with Prometheus metrics enabled

## Dashboard Format[¶](#dashboard-format "Permanent link")

We provide dashboards in the **native Perses YAML format** that works across all deployment methods:

-   **Files**: `*.yaml` (native Perses dashboard specifications)
-   **Format**: Pure dashboard specifications that work everywhere
-   **Usage**: Works with standalone Perses, API imports, CLI, and file provisioning
-   **Kubernetes**: Directly compatible with Perses Operator

## Dashboard Descriptions[¶](#dashboard-descriptions_1 "Permanent link") 

-   **performance_statistics.yaml**: Performance metrics with aggregated latency statistics
-   **query_statistics.yaml**: Query performance and deployment metrics

## Deployment Options[¶](#deployment-options_1 "Permanent link") 

### Direct Import to Perses[¶](#direct-import-to-perses "Permanent link")

Import the dashboard specifications via Perses API or CLI:

    percli apply -f performance_statistics.yaml

### Perses Operator (Kubernetes)[¶](#perses-operator-kubernetes "Permanent link")

The native YAML format works directly with the Perses Operator:

    kubectl apply -f performance_statistics.yaml -n <namespace>

### File Provisioning[¶](#file-provisioning "Permanent link")

Place the YAML files in a Perses provisioning folder for automatic loading.

perses/performance_statistics.yaml

    kind: PersesDashboard
    metadata:
      name: performance-statistics
      createdAt: 0001-01-01T00:00:00Z
      updatedAt: 0001-01-01T00:00:00Z
      version: 0
      project: ""
    spec:
      display:
        name: Performance Statistics

      variables:
        - kind: ListVariable
          spec:
            display:
              name: Deployment_ID
              hidden: false
            name: Deployment_id
            allowAllValue: true
            allowMultiple: true
            defaultValue:
              - $__all
            sort: alphabetical-asc
            plugin:
              kind: PrometheusLabelValuesVariable
              spec:
                datasource:
                  kind: PrometheusDatasource
                  name: accelerators-thanos-querier-datasource
                labelName: model_name
                matchers:
                  # Any one vllm metric that always carries model_name
                  - vllm:generation_tokens_total

      panels:
        "1":
          kind: Panel
          spec:
            display:
              name: E2E Latency over Time
            plugin:
              kind: TimeSeriesChart
              spec:
                legend:
                  mode: table
                  position: bottom
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource:
                        kind: PrometheusDatasource
                        name: accelerators-thanos-querier-datasource
                      # avg latency by model = sum(rate(sum)) / sum(rate(count))
                      query: >
                        sum by (model_name) (rate(vllm:e2e_request_latency_seconds_sum[$__interval]))
                        /
                        sum by (model_name) (rate(vllm:e2e_request_latency_seconds_count[$__interval]))
                      seriesNameFormat: '}'

        "2":
          kind: Panel
          spec:
            display:
              name: E2E Latency (Avg)
            plugin:
              kind: StatChart
              spec:
                calculation: last-number
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource:
                        kind: PrometheusDatasource
                        name: accelerators-thanos-querier-datasource
                      query: >
                        (sum by (model_name) (increase(vllm:e2e_request_latency_seconds_sum[$__range])))
                        /
                        (sum by (model_name) (increase(vllm:e2e_request_latency_seconds_count[$__range])))

        "3":
          kind: Panel
          spec:
            display:
              name: E2E Latency (P50)
            plugin:
              kind: StatChart
              spec:
                calculation: last-number
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource:
                        kind: PrometheusDatasource
                        name: accelerators-thanos-querier-datasource
                      query: >
                        histogram_quantile(
                          0.50,
                          sum by (le, model_name) (
                            rate(vllm:e2e_request_latency_seconds_bucket[$__interval])
                          )
                        )

        "4":
          kind: Panel
          spec:
            display:
              name: E2E Latency (P90)
            plugin:
              kind: StatChart
              spec:
                calculation: last-number
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource:
                        kind: PrometheusDatasource
                        name: accelerators-thanos-querier-datasource
                      query: >
                        histogram_quantile(
                          0.90,
                          sum by (le, model_name) (
                            rate(vllm:e2e_request_latency_seconds_bucket[$__interval])
                          )
                        )

        "5":
          kind: Panel
          spec:
            display:
              name: E2E Latency (P99)
            plugin:
              kind: StatChart
              spec:
                calculation: last-number
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource:
                        kind: PrometheusDatasource
                        name: accelerators-thanos-querier-datasource
                      query: >
                        histogram_quantile(
                          0.99,
                          sum by (le, model_name) (
                            rate(vllm:e2e_request_latency_seconds_bucket[$__interval])
                          )
                        )

        "6":
          kind: Panel
          spec:
            display:
              name: TTFT over Time
            plugin:
              kind: TimeSeriesChart
              spec:
                legend:
                  mode: table
                  position: bottom
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource:
                        kind: PrometheusDatasource
                        name: accelerators-thanos-querier-datasource
                      query: >
                        sum by (model_name) (rate(vllm:time_to_first_token_seconds_sum[$__interval]))
                        /
                        sum by (model_name) (rate(vllm:time_to_first_token_seconds_count[$__interval]))
                      seriesNameFormat: '}'

        "7":
          kind: Panel
          spec:
            display:
              name: TTFT (Avg)
            plugin:
              kind: StatChart
              spec:
                calculation: last-number
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource:
                        kind: PrometheusDatasource
                        name: accelerators-thanos-querier-datasource
                      query: >
                        (sum by (model_name) (increase(vllm:time_to_first_token_seconds_sum[$__range])))
                        /
                        (sum by (model_name) (increase(vllm:time_to_first_token_seconds_count[$__range])))

        "8":
          kind: Panel
          spec:
            display:
              name: TTFT (P50)
            plugin:
              kind: StatChart
              spec:
                calculation: last-number
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource:
                        kind: PrometheusDatasource
                        name: accelerators-thanos-querier-datasource
                      query: >
                        histogram_quantile(
                          0.50,
                          sum by (le, model_name) (
                            rate(vllm:time_to_first_token_seconds_bucket[$__interval])
                          )
                        )

        "9":
          kind: Panel
          spec:
            display:
              name: TTFT (P90)
            plugin:
              kind: StatChart
              spec:
                calculation: last-number
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource:
                        kind: PrometheusDatasource
                        name: accelerators-thanos-querier-datasource
                      query: >
                        histogram_quantile(
                          0.90,
                          sum by (le, model_name) (
                            rate(vllm:time_to_first_token_seconds_bucket[$__interval])
                          )
                        )

        "10":
          kind: Panel
          spec:
            display:
              name: TTFT (P99)
            plugin:
              kind: StatChart
              spec:
                calculation: last-number
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource:
                        kind: PrometheusDatasource
                        name: accelerators-thanos-querier-datasource
                      query: >
                        histogram_quantile(
                          0.99,
                          sum by (le, model_name) (
                            rate(vllm:time_to_first_token_seconds_bucket[$__interval])
                          )
                        )

        "11":
          kind: Panel
          spec:
            display:
              name: ITL (Time per Output Token) over Time
            plugin:
              kind: TimeSeriesChart
              spec:
                legend:
                  mode: table
                  position: bottom
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource:
                        kind: PrometheusDatasource
                        name: accelerators-thanos-querier-datasource
                      query: >
                        sum by (model_name) (rate(vllm:time_per_output_token_seconds_sum[$__interval]))
                        /
                        sum by (model_name) (rate(vllm:time_per_output_token_seconds_count[$__interval]))
                      seriesNameFormat: '}'
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource:
                        kind: PrometheusDatasource
                        name: accelerators-thanos-querier-datasource
                      query: >
                        histogram_quantile(
                          0.50,
                          sum by (le, model_name) (
                            rate(vllm:time_per_output_token_seconds_bucket[$__interval])
                          )
                        )
                      seriesNameFormat: '} p50'
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource:
                        kind: PrometheusDatasource
                        name: accelerators-thanos-querier-datasource
                      query: >
                        histogram_quantile(
                          0.90,
                          sum by (le, model_name) (
                            rate(vllm:time_per_output_token_seconds_bucket[$__interval])
                          )
                        )
                      seriesNameFormat: '} p90'
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource:
                        kind: PrometheusDatasource
                        name: accelerators-thanos-querier-datasource
                      query: >
                        histogram_quantile(
                          0.99,
                          sum by (le, model_name) (
                            rate(vllm:time_per_output_token_seconds_bucket[$__interval])
                          )
                        )
                      seriesNameFormat: '} p99'

        "12":
          kind: Panel
          spec:
            display:
              name: ITL (Avg)
            plugin:
              kind: StatChart
              spec:
                calculation: last-number
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource:
                        kind: PrometheusDatasource
                        name: accelerators-thanos-querier-datasource
                      query: >
                        (sum by (model_name) (increase(vllm:time_per_output_token_seconds_sum[$__range])))
                        /
                        (sum by (model_name) (increase(vllm:time_per_output_token_seconds_count[$__range])))

        "13":
          kind: Panel
          spec:
            display:
              name: ITL (P50)
            plugin:
              kind: StatChart
              spec:
                calculation: last-number
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource:
                        kind: PrometheusDatasource
                        name: accelerators-thanos-querier-datasource
                      query: >
                        histogram_quantile(
                          0.50,
                          sum by (le, model_name) (
                            rate(vllm:time_per_output_token_seconds_bucket[$__interval])
                          )
                        )

        "14":
          kind: Panel
          spec:
            display:
              name: ITL (P90)
            plugin:
              kind: StatChart
              spec:
                calculation: last-number
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource:
                        kind: PrometheusDatasource
                        name: accelerators-thanos-querier-datasource
                      query: >
                        histogram_quantile(
                          0.90,
                          sum by (le, model_name) (
                            rate(vllm:time_per_output_token_seconds_bucket[$__interval])
                          )
                        )

        "15":
          kind: Panel
          spec:
            display:
              name: ITL (P99)
            plugin:
              kind: StatChart
              spec:
                calculation: last-number
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource:
                        kind: PrometheusDatasource
                        name: accelerators-thanos-querier-datasource
                      query: >
                        histogram_quantile(
                          0.99,
                          sum by (le, model_name) (
                            rate(vllm:time_per_output_token_seconds_bucket[$__interval])
                          )
                        )

        "16":
          kind: Panel
          spec:
            display:
              name: TPS (Tokens/sec) over Time
            plugin:
              kind: TimeSeriesChart
              spec:
                legend:
                  mode: table
                  position: bottom
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource:
                        kind: PrometheusDatasource
                        name: accelerators-thanos-querier-datasource
                      query: >
                        sum by (model_name) (rate(vllm:generation_tokens_total[$__interval]))
                      seriesNameFormat: '} generation'
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource:
                        kind: PrometheusDatasource
                        name: accelerators-thanos-querier-datasource
                      query: >
                        sum by (model_name) (rate(vllm:prompt_tokens_total[$__interval]))
                      seriesNameFormat: '} prompt'
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource:
                        kind: PrometheusDatasource
                        name: accelerators-thanos-querier-datasource
                      # overall iteration tokens/sec if exposed
                      query: >
                        rate(vllm:iteration_tokens_total_count[$__interval])
                      seriesNameFormat: 'iteration overall'

        "17":
          kind: Panel
          spec:
            display:
              name: KV Cache Usage (avg %)
            plugin:
              kind: StatChart
              spec:
                calculation: last-number
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource:
                        kind: PrometheusDatasource
                        name: accelerators-thanos-querier-datasource
                      # Multiply by 100 so we can read it as a percentage without setting a unit (avoids CUE unit conflicts)
                      query: >
                        100 * avg(vllm:kv_cache_usage_perc)

        "18":
          kind: Panel
          spec:
            display:
              name: Running Requests by Pod
            plugin:
              kind: TimeSeriesChart
              spec:
                legend:
                  mode: table
                  position: bottom
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource:
                        kind: PrometheusDatasource
                        name: accelerators-thanos-querier-datasource
                      query: >
                        sum by (pod) (vllm:num_requests_running)
                      seriesNameFormat: '}'

        "19":
          kind: Panel
          spec:
            display:
              name: Waiting Requests by Pod
            plugin:
              kind: TimeSeriesChart
              spec:
                legend:
                  mode: table
                  position: bottom
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource:
                        kind: PrometheusDatasource
                        name: accelerators-thanos-querier-datasource
                      query: >
                        sum by (pod) (vllm:num_requests_waiting)
                      seriesNameFormat: '}'

        "20":
          kind: Panel
          spec:
            display:
              name: Running Requests (sum)
            plugin:
              kind: StatChart
              spec:
                calculation: last-number
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource:
                        kind: PrometheusDatasource
                        name: accelerators-thanos-querier-datasource
                      query: sum(vllm:num_requests_running)

        "21":
          kind: Panel
          spec:
            display:
              name: Waiting Requests (sum)
            plugin:
              kind: StatChart
              spec:
                calculation: last-number
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource:
                        kind: PrometheusDatasource
                        name: accelerators-thanos-querier-datasource
                      query: sum(vllm:num_requests_waiting)

      layouts:
        - kind: Grid
          spec:
            display:
              title: Overview
            items:
              - x: 0
                y: 0
                width: 6
                height: 3
                content:    # KV cache %
              - x: 6
                y: 0
                width: 6
                height: 3
                content:    # running sum
              - x: 12
                y: 0
                width: 6
                height: 3
                content:    # waiting sum

        - kind: Grid
          spec:
            display:
              title: E2E Latency
            items:
              - x: 0
                y: 1
                width: 10
                height: 6
                content: 
              - x: 10
                y: 1
                width: 7
                height: 3
                content: 
              - x: 17
                y: 1
                width: 7
                height: 3
                content: 
              - x: 10
                y: 4
                width: 7
                height: 3
                content: 
              - x: 17
                y: 4
                width: 7
                height: 3
                content: 

        - kind: Grid
          spec:
            display:
              title: TTFT
            items:
              - x: 0
                y: 8
                width: 10
                height: 6
                content: 
              - x: 10
                y: 8
                width: 7
                height: 3
                content: 
              - x: 17
                y: 8
                width: 7
                height: 3
                content: 
              - x: 10
                y: 11
                width: 7
                height: 3
                content: 
              - x: 17
                y: 11
                width: 7
                height: 3
                content: 

        - kind: Grid
          spec:
            display:
              title: ITL (Time per Output Token)
            items:
              - x: 0
                y: 15
                width: 10
                height: 6
                content: 
              - x: 10
                y: 15
                width: 7
                height: 3
                content: 
              - x: 17
                y: 15
                width: 7
                height: 3
                content: 
              - x: 10
                y: 18
                width: 7
                height: 3
                content: 
              - x: 17
                y: 18
                width: 7
                height: 3
                content: 

        - kind: Grid
          spec:
            display:
              title: TPS (Prompt / Generation / Iteration)
            items:
              - x: 0
                y: 22
                width: 14
                height: 6
                content: 

        - kind: Grid
          spec:
            display:
              title: Per-Pod Request State
            items:
              - x: 0
                y: 28
                width: 12
                height: 6
                content: 
              - x: 12
                y: 28
                width: 12
                height: 6
                content: 

perses/query_statistics.yaml

    kind: PersesDashboard
    metadata:
      name: query-statistics
      createdAt: 0001-01-01T00:00:00Z
      updatedAt: 0001-01-01T00:00:00Z
      version: 0
      project: ""
    spec:
      display:
        name: Query Statistics_New

      variables:
        - kind: ListVariable
          spec:
            name: NS
            display: 
            allowMultiple: false
            defaultValue: llm-d
            plugin:
              kind: PrometheusLabelValuesVariable
              spec:
                datasource: 
                labelName: namespace
                matchers:
                  - up

        - kind: ListVariable
          spec:
            name: SVC
            display: 
            allowMultiple: false
            defaultValue: vllm-qwen2-0-5b-sim
            plugin:
              kind: PrometheusLabelValuesVariable
              spec:
                datasource: 
                labelName: service
                matchers:
                  - up

        - kind: ListVariable
          spec:
            name: MODEL
            display: 
            allowAllValue: true
            allowMultiple: true
            defaultValue: ["$__all"]
            plugin:
              kind: PrometheusLabelValuesVariable
              spec:
                datasource: 
                labelName: model_name
                matchers:
                  - vllm:request_success_total

      panels:

        # --- Core (works on Simulator & Real) ---
        core_running_now:
          kind: Panel
          spec:
            display: 
            plugin:  }
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource: 
                      query: sum(vllm:num_requests_running) or vector(0)
                      minStep: "15s"

        core_waiting_now:
          kind: Panel
          spec:
            display: 
            plugin:  }
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource: 
                      query: sum(vllm:num_requests_waiting) or vector(0)
                      minStep: "15s"

        core_kv_usage_now:
          kind: Panel
          spec:
            display: 
            plugin:  }
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource: 
                      query: avg(vllm:kv_cache_usage_perc) or vector(0)
                      minStep: "15s"

        core_running_ts:
          kind: Panel
          spec:
            display: 
            plugin:
              kind: TimeSeriesChart
              spec:
                legend: 
                visual: 
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource: 
                      query: sum by (service) (vllm:num_requests_running) or vector(0)
                      minStep: "15s"

        core_waiting_ts:
          kind: Panel
          spec:
            display: 
            plugin:
              kind: TimeSeriesChart
              spec:
                legend: 
                visual: 
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource: 
                      query: sum by (service) (vllm:num_requests_waiting) or vector(0)
                      minStep: "15s"

        core_targets_up:
          kind: Panel
          spec:
            display: 
            plugin:  }
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource: 
                      query: count(up == 1) or vector(0)
                      minStep: "15s"

        # --- KV Cache as Percent (works on Simulator & Real) ---
        core_kv_usage_pct_now:
          kind: Panel
          spec:
            display: 
            plugin:  }
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource: 
                      # multiply by 100 to present percentage; omit format.unit to avoid schema conflicts
                      query: (avg(vllm:kv_cache_usage_perc) * 100) or vector(0)
                      minStep: "15s"

        core_kv_usage_pct_ts:
          kind: Panel
          spec:
            display: 
            plugin:
              kind: TimeSeriesChart
              spec:
                legend: 
                visual: 
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource: 
                      query: (avg by (service) (vllm:kv_cache_usage_perc) * 100) or vector(0)
                      minStep: "15s"

        # --- Per-Pod breakdowns (works on Simulator & Real) ---
        per_pod_running_ts:
          kind: Panel
          spec:
            display: 
            plugin:
              kind: TimeSeriesChart
              spec:
                legend: 
                visual: 
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource: 
                      query: sum by (pod) (vllm:num_requests_running) or vector(0)
                      minStep: "15s"

        per_pod_waiting_ts:
          kind: Panel
          spec:
            display: 
            plugin:
              kind: TimeSeriesChart
              spec:
                legend: 
                visual: 
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource: 
                      query: sum by (pod) (vllm:num_requests_waiting) or vector(0)
                      minStep: "15s"

        per_pod_kv_pct_ts:
          kind: Panel
          spec:
            display: 
            plugin:
              kind: TimeSeriesChart
              spec:
                legend: 
                visual: 
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource: 
                      # if your exporter labels kv metric with pod (the sim does), this works; otherwise it will just return empty
                      query: (avg by (pod) (vllm:kv_cache_usage_perc) * 100) or vector(0)
                      minStep: "15s"

        # --- Real vLLM only (zeros on simulator) ---
        real_req_rate_ts:
          kind: Panel
          spec:
            display: 
            plugin:
              kind: TimeSeriesChart
              spec:
                legend: 
                visual: 
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource: 
                      query: sum by (model_name) (rate(vllm:request_success_total[$__interval])) or vector(0)
                      minStep: "15s"

        real_p50:
          kind: Panel
          spec:
            display: 
            plugin:  }
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource: 
                      query: histogram_quantile(0.50, sum by (le, model_name) (rate(vllm:e2e_request_latency_seconds_bucket[$__interval]))) or vector(0)
                      minStep: "15s"

        real_p90:
          kind: Panel
          spec:
            display: 
            plugin:  }
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource: 
                      query: histogram_quantile(0.90, sum by (le, model_name) (rate(vllm:e2e_request_latency_seconds_bucket[$__interval]))) or vector(0)
                      minStep: "15s"

        real_p99:
          kind: Panel
          spec:
            display: 
            plugin:  }
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource: 
                      query: histogram_quantile(0.99, sum by (le, model_name) (rate(vllm:e2e_request_latency_seconds_bucket[$__interval]))) or vector(0)
                      minStep: "15s"

        real_input_tokens_ts:
          kind: Panel
          spec:
            display: 
            plugin:
              kind: TimeSeriesChart
              spec:
                legend: 
                visual: 
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource: 
                      query: sum by (model_name) (rate(vllm:prompt_tokens_total[$__interval])) or vector(0)
                      minStep: "15s"

        real_output_tokens_ts:
          kind: Panel
          spec:
            display: 
            plugin:
              kind: TimeSeriesChart
              spec:
                legend: 
                visual: 
            queries:
              - kind: TimeSeriesQuery
                spec:
                  plugin:
                    kind: PrometheusTimeSeriesQuery
                    spec:
                      datasource: 
                      query: sum by (model_name) (rate(vllm:generation_tokens_total[$__interval])) or vector(0)
                      minStep: "15s"

      layouts:
        - kind: Grid
          spec:
            display: 
            items:
              -  }
              -  }
              -  }
              -  }
              -  }
              -  }

        - kind: Grid
          spec:
            display: 
            items:
              -  }
              -  }

        - kind: Grid
          spec:
            display: 
            items:
              -  }
              -  }
              -  }

        - kind: Grid
          spec:
            display: 
            items:
              -  }
              -  }
              -  }
              -  }
              -  }
              -  }