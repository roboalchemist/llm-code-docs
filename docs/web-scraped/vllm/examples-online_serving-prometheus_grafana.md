# Source: https://docs.vllm.ai/en/stable/examples/online_serving/prometheus_grafana/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/online_serving/prometheus_grafana.md "Edit this page")

# Prometheus and Grafana[¶](#prometheus-and-grafana "Permanent link")

Source <https://github.com/vllm-project/vllm/tree/main/examples/online_serving/prometheus_grafana>.

This is a simple example that shows you how to connect vLLM metric logging to the Prometheus/Grafana stack. For this example, we launch Prometheus and Grafana via Docker. You can checkout other methods through [Prometheus](https://prometheus.io/) and [Grafana](https://grafana.com/) websites.

Install:

-   [`docker`](https://docs.docker.com/engine/install/)
-   [`docker compose`](https://docs.docker.com/compose/install/linux/#install-using-the-repository)

## Launch[¶](#launch "Permanent link")

Prometheus metric logging is enabled by default in the OpenAI-compatible server. Launch via the entrypoint:

    vllm serve mistralai/Mistral-7B-v0.1 \
        --max-model-len 2048

Launch Prometheus and Grafana servers with `docker compose`:

    docker compose up

Submit some sample requests to the server:

    wget https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered/resolve/main/ShareGPT_V3_unfiltered_cleaned_split.json

    vllm bench serve \
        --model mistralai/Mistral-7B-v0.1 \
        --tokenizer mistralai/Mistral-7B-v0.1 \
        --endpoint /v1/completions \
        --dataset-name sharegpt \
        --dataset-path ShareGPT_V3_unfiltered_cleaned_split.json \
        --request-rate 3.0

Navigating to [`http://localhost:8000/metrics`](http://localhost:8000/metrics) will show the raw Prometheus metrics being exposed by vLLM.

## Grafana Dashboard[¶](#grafana-dashboard "Permanent link")

Navigate to [`http://localhost:3000`](http://localhost:3000). Log in with the default username (`admin`) and password (`admin`).

### Add Prometheus Data Source[¶](#add-prometheus-data-source "Permanent link")

Navigate to [`http://localhost:3000/connections/datasources/new`](http://localhost:3000/connections/datasources/new) and select Prometheus.

On Prometheus configuration page, we need to add the `Prometheus Server URL` in `Connection`. For this setup, Grafana and Prometheus are running in separate containers, but Docker creates DNS name for each container. You can just use `http://prometheus:9090`.

Click `Save & Test`. You should get a green check saying \"Successfully queried the Prometheus API.\".

### Import Dashboard[¶](#import-dashboard "Permanent link")

Navigate to [`http://localhost:3000/dashboard/import`](http://localhost:3000/dashboard/import), upload `grafana.json`, and select the `prometheus` datasource. You should see a screen that looks like the following:

[![Grafana Dashboard Image](https://i.imgur.com/R2vH9VW.png)](https://i.imgur.com/R2vH9VW.png)

## Example materials[¶](#example-materials "Permanent link")

docker-compose.yaml

    # docker-compose.yaml
    version: "3"

    services:
      prometheus:
        image: prom/prometheus:latest
        extra_hosts:
          - "host.docker.internal:host-gateway"     # allow a direct connection from container to the local machine
        ports:
          - "9090:9090"   # the default port used by Prometheus
        volumes:
          - $/prometheus.yaml:/etc/prometheus/prometheus.yml # mount Prometheus config file

      grafana:
        image: grafana/grafana:latest
        depends_on:
          - prometheus
        ports:
          - "3000:3000" # the default port used by Grafana

grafana.json

    ,
            "enable": true,
            "hide": true,
            "iconColor": "rgba(0, 211, 255, 1)",
            "name": "Annotations & Alerts",
            "target": ,
            "type": "dashboard"
          }
        ]
      },
      "description": "Monitoring vLLM Inference Server",
      "editable": true,
      "fiscalYearStartMonth": 0,
      "graphTooltip": 0,
      "id": 1,
      "links": [],
      "liveNow": false,
      "panels": [
        "
          },
          "description": "End to end request latency measured in seconds.",
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
              "unit": "s"
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 9,
          "options": ,
            "tooltip": 
          },
          "targets": [
            "
              },
              "disableTextWrap": false,
              "editorMode": "builder",
              "expr": "histogram_quantile(0.99, sum by(le) (rate(vllm:e2e_request_latency_seconds_bucket[$__rate_interval])))",
              "fullMetaSearch": false,
              "includeNullMetadata": false,
              "instant": false,
              "legendFormat": "P99",
              "range": true,
              "refId": "A",
              "useBackend": false
            },
            "
              },
              "disableTextWrap": false,
              "editorMode": "builder",
              "expr": "histogram_quantile(0.95, sum by(le) (rate(vllm:e2e_request_latency_seconds_bucket[$__rate_interval])))",
              "fullMetaSearch": false,
              "hide": false,
              "includeNullMetadata": false,
              "instant": false,
              "legendFormat": "P95",
              "range": true,
              "refId": "B",
              "useBackend": false
            },
            "
              },
              "disableTextWrap": false,
              "editorMode": "builder",
              "expr": "histogram_quantile(0.9, sum by(le) (rate(vllm:e2e_request_latency_seconds_bucket[$__rate_interval])))",
              "fullMetaSearch": false,
              "hide": false,
              "includeNullMetadata": false,
              "instant": false,
              "legendFormat": "P90",
              "range": true,
              "refId": "C",
              "useBackend": false
            },
            "
              },
              "disableTextWrap": false,
              "editorMode": "builder",
              "expr": "histogram_quantile(0.5, sum by(le) (rate(vllm:e2e_request_latency_seconds_bucket[$__rate_interval])))",
              "fullMetaSearch": false,
              "hide": false,
              "includeNullMetadata": false,
              "instant": false,
              "legendFormat": "P50",
              "range": true,
              "refId": "D",
              "useBackend": false
            },
            "
              },
              "editorMode": "code",
              "expr": "rate(vllm:e2e_request_latency_seconds_sum[$__rate_interval])\n/\nrate(vllm:e2e_request_latency_seconds_count[$__rate_interval])",
              "hide": false,
              "instant": false,
              "legendFormat": "Average",
              "range": true,
              "refId": "E"
            }
          ],
          "title": "E2E Request Latency",
          "type": "timeseries"
        },
        "
          },
          "description": "Number of tokens processed per second",
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
              }
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 8,
          "options": ,
            "tooltip": 
          },
          "targets": [
            "
              },
              "disableTextWrap": false,
              "editorMode": "builder",
              "expr": "rate(vllm:prompt_tokens_total[$__rate_interval])",
              "fullMetaSearch": false,
              "includeNullMetadata": false,
              "instant": false,
              "legendFormat": "Prompt Tokens/Sec",
              "range": true,
              "refId": "A",
              "useBackend": false
            },
            "
              },
              "disableTextWrap": false,
              "editorMode": "builder",
              "expr": "rate(vllm:generation_tokens_total[$__rate_interval])",
              "fullMetaSearch": false,
              "hide": false,
              "includeNullMetadata": false,
              "instant": false,
              "legendFormat": "Generation Tokens/Sec",
              "range": true,
              "refId": "B",
              "useBackend": false
            }
          ],
          "title": "Token Throughput",
          "type": "timeseries"
        },
        "
          },
          "description": "Inter token latency in seconds.",
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
              "unit": "s"
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 10,
          "options": ,
            "tooltip": 
          },
          "targets": [
            "
              },
              "disableTextWrap": false,
              "editorMode": "builder",
              "expr": "histogram_quantile(0.99, sum by(le) (rate(vllm:inter_token_latency_seconds_bucket[$__rate_interval])))",
              "fullMetaSearch": false,
              "includeNullMetadata": false,
              "instant": false,
              "legendFormat": "P99",
              "range": true,
              "refId": "A",
              "useBackend": false
            },
            "
              },
              "disableTextWrap": false,
              "editorMode": "builder",
              "expr": "histogram_quantile(0.95, sum by(le) (rate(vllm:inter_token_latency_seconds_bucket[$__rate_interval])))",
              "fullMetaSearch": false,
              "hide": false,
              "includeNullMetadata": false,
              "instant": false,
              "legendFormat": "P95",
              "range": true,
              "refId": "B",
              "useBackend": false
            },
            "
              },
              "disableTextWrap": false,
              "editorMode": "builder",
              "expr": "histogram_quantile(0.9, sum by(le) (rate(vllm:inter_token_latency_seconds_bucket[$__rate_interval])))",
              "fullMetaSearch": false,
              "hide": false,
              "includeNullMetadata": false,
              "instant": false,
              "legendFormat": "P90",
              "range": true,
              "refId": "C",
              "useBackend": false
            },
            "
              },
              "disableTextWrap": false,
              "editorMode": "builder",
              "expr": "histogram_quantile(0.5, sum by(le) (rate(vllm:inter_token_latency_seconds_bucket[$__rate_interval])))",
              "fullMetaSearch": false,
              "hide": false,
              "includeNullMetadata": false,
              "instant": false,
              "legendFormat": "P50",
              "range": true,
              "refId": "D",
              "useBackend": false
            },
            "
              },
              "editorMode": "code",
              "expr": "rate(vllm:inter_token_latency_seconds_sum[$__rate_interval])\n/\nrate(vllm:inter_token_latency_seconds_count[$__rate_interval])",
              "hide": false,
              "instant": false,
              "legendFormat": "Mean",
              "range": true,
              "refId": "E"
            }
          ],
          "title": "Inter Token Latency",
          "type": "timeseries"
        },
        "
          },
          "description": "Number of requests in RUNNING, WAITING, and SWAPPED state",
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
              "unit": "none"
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 3,
          "options": ,
            "tooltip": 
          },
          "targets": [
            "
              },
              "disableTextWrap": false,
              "editorMode": "builder",
              "expr": "vllm:num_requests_running",
              "fullMetaSearch": false,
              "includeNullMetadata": true,
              "instant": false,
              "legendFormat": "Num Running",
              "range": true,
              "refId": "A",
              "useBackend": false
            },
            "
              },
              "disableTextWrap": false,
              "editorMode": "builder",
              "expr": "vllm:num_requests_waiting",
              "fullMetaSearch": false,
              "hide": false,
              "includeNullMetadata": true,
              "instant": false,
              "legendFormat": "Num Waiting",
              "range": true,
              "refId": "C",
              "useBackend": false
            }
          ],
          "title": "Scheduler State",
          "type": "timeseries"
        },
        "
          },
          "description": "P50, P90, P95, and P99 TTFT latency in seconds.",
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
              "unit": "s"
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 5,
          "options": ,
            "tooltip": 
          },
          "targets": [
            "
              },
              "disableTextWrap": false,
              "editorMode": "builder",
              "expr": "histogram_quantile(0.99, sum by(le) (rate(vllm:time_to_first_token_seconds_bucket[$__rate_interval])))",
              "fullMetaSearch": false,
              "hide": false,
              "includeNullMetadata": false,
              "instant": false,
              "legendFormat": "P99",
              "range": true,
              "refId": "A",
              "useBackend": false
            },
            "
              },
              "disableTextWrap": false,
              "editorMode": "builder",
              "expr": "histogram_quantile(0.95, sum by(le) (rate(vllm:time_to_first_token_seconds_bucket[$__rate_interval])))",
              "fullMetaSearch": false,
              "includeNullMetadata": false,
              "instant": false,
              "legendFormat": "P95",
              "range": true,
              "refId": "B",
              "useBackend": false
            },
            "
              },
              "disableTextWrap": false,
              "editorMode": "builder",
              "expr": "histogram_quantile(0.9, sum by(le) (rate(vllm:time_to_first_token_seconds_bucket[$__rate_interval])))",
              "fullMetaSearch": false,
              "hide": false,
              "includeNullMetadata": false,
              "instant": false,
              "legendFormat": "P90",
              "range": true,
              "refId": "C",
              "useBackend": false
            },
            "
              },
              "disableTextWrap": false,
              "editorMode": "builder",
              "expr": "histogram_quantile(0.5, sum by(le) (rate(vllm:time_to_first_token_seconds_bucket[$__rate_interval])))",
              "fullMetaSearch": false,
              "hide": false,
              "includeNullMetadata": false,
              "instant": false,
              "legendFormat": "P50",
              "range": true,
              "refId": "D",
              "useBackend": false
            },
            "
              },
              "editorMode": "code",
              "expr": "rate(vllm:time_to_first_token_seconds_sum[$__rate_interval])\n/\nrate(vllm:time_to_first_token_seconds_count[$__rate_interval])",
              "hide": false,
              "instant": false,
              "legendFormat": "Average",
              "range": true,
              "refId": "E"
            }
          ],
          "title": "Time To First Token Latency",
          "type": "timeseries"
        },
        "
          },
          "description": "Percentage of used cache blocks by vLLM.",
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
              "unit": "percentunit"
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 4,
          "options": ,
            "tooltip": 
          },
          "targets": [
            "
              },
              "editorMode": "code",
              "expr": "vllm:kv_cache_usage_perc",
              "instant": false,
              "legendFormat": "GPU Cache Usage",
              "range": true,
              "refId": "A"
            }
          ],
          "title": "Cache Utilization",
          "type": "timeseries"
        },
        "
          },
          "description": "Heatmap of request prompt length",
          "fieldConfig": ,
                "scaleDistribution": 
              }
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 12,
          "options": ,
            "color": ,
            "exemplars": ,
            "filterValues": ,
            "legend": ,
            "rowsFrame": ,
            "tooltip": ,
            "yAxis": 
          },
          "pluginVersion": "11.2.0",
          "targets": [
            "
              },
              "disableTextWrap": false,
              "editorMode": "builder",
              "expr": "sum by(le) (increase(vllm:request_prompt_tokens_bucket[$__rate_interval]))",
              "format": "heatmap",
              "fullMetaSearch": false,
              "includeNullMetadata": true,
              "instant": false,
              "legendFormat": "}",
              "range": true,
              "refId": "A",
              "useBackend": false
            }
          ],
          "title": "Request Prompt Length",
          "type": "heatmap"
        },
        "
          },
          "description": "Heatmap of request generation length",
          "fieldConfig": ,
                "scaleDistribution": 
              }
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 13,
          "options": ,
            "color": ,
            "exemplars": ,
            "filterValues": ,
            "legend": ,
            "rowsFrame": ,
            "tooltip": ,
            "yAxis": 
          },
          "pluginVersion": "11.2.0",
          "targets": [
            "
              },
              "disableTextWrap": false,
              "editorMode": "builder",
              "expr": "sum by(le) (increase(vllm:request_generation_tokens_bucket[$__rate_interval]))",
              "format": "heatmap",
              "fullMetaSearch": false,
              "includeNullMetadata": true,
              "instant": false,
              "legendFormat": "}",
              "range": true,
              "refId": "A",
              "useBackend": false
            }
          ],
          "title": "Request Generation Length",
          "type": "heatmap"
        },
        "
          },
          "description": "Number of finished requests by their finish reason: either an EOS token was generated or the max sequence length was reached.",
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
              }
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 11,
          "options": ,
            "tooltip": 
          },
          "targets": [
            "
              },
              "disableTextWrap": false,
              "editorMode": "builder",
              "expr": "sum by(finished_reason) (increase(vllm:request_success_total[$__rate_interval]))",
              "fullMetaSearch": false,
              "includeNullMetadata": true,
              "instant": false,
              "interval": "",
              "legendFormat": "__auto",
              "range": true,
              "refId": "A",
              "useBackend": false
            }
          ],
          "title": "Finish Reason",
          "type": "timeseries"
        },
        "
          },
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
              }
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 14,
          "options": ,
            "tooltip": 
          },
          "targets": [
            "
              },
              "disableTextWrap": false,
              "editorMode": "code",
              "expr": "rate(vllm:request_queue_time_seconds_sum[$__rate_interval])",
              "fullMetaSearch": false,
              "includeNullMetadata": true,
              "instant": false,
              "legendFormat": "__auto",
              "range": true,
              "refId": "A",
              "useBackend": false
            }
          ],
          "title": "Queue Time",
          "type": "timeseries"
        },
        "
          },
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
              }
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 15,
          "options": ,
            "tooltip": 
          },
          "targets": [
            "
              },
              "disableTextWrap": false,
              "editorMode": "code",
              "expr": "rate(vllm:request_prefill_time_seconds_sum[$__rate_interval])",
              "fullMetaSearch": false,
              "includeNullMetadata": true,
              "instant": false,
              "legendFormat": "Prefill",
              "range": true,
              "refId": "A",
              "useBackend": false
            },
            "
              },
              "editorMode": "code",
              "expr": "rate(vllm:request_decode_time_seconds_sum[$__rate_interval])",
              "hide": false,
              "instant": false,
              "legendFormat": "Decode",
              "range": true,
              "refId": "B"
            }
          ],
          "title": "Requests Prefill and Decode Time",
          "type": "timeseries"
        },
        "
          },
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
              }
            },
            "overrides": []
          },
          "gridPos": ,
          "id": 16,
          "options": ,
            "tooltip": 
          },
          "targets": [
            "
              },
              "disableTextWrap": false,
              "editorMode": "code",
              "expr": "rate(vllm:request_max_num_generation_tokens_sum[$__rate_interval])",
              "fullMetaSearch": false,
              "includeNullMetadata": true,
              "instant": false,
              "legendFormat": "Tokens",
              "range": true,
              "refId": "A",
              "useBackend": false
            }
          ],
          "title": "Max Generation Token in Sequence Group",
          "type": "timeseries"
        }
      ],
      "refresh": "",
      "schemaVersion": 39,
      "tags": [],
      "templating": ,
            "hide": 0,
            "includeAll": false,
            "label": "datasource",
            "multi": false,
            "name": "DS_PROMETHEUS",
            "options": [],
            "query": "prometheus",
            "queryValue": "",
            "refresh": 1,
            "regex": "",
            "skipUrlSync": false,
            "type": "datasource"
          },
          ,
            "datasource": "
            },
            "definition": "label_values(model_name)",
            "hide": 0,
            "includeAll": false,
            "label": "model_name",
            "multi": false,
            "name": "model_name",
            "options": [],
            "query": ,
            "refresh": 1,
            "regex": "",
            "skipUrlSync": false,
            "sort": 0,
            "type": "query"
          }
        ]
      },
      "time": ,
      "timepicker": ,
      "timezone": "",
      "title": "vLLM",
      "uid": "b281712d-8bff-41ef-9f3f-71ad43c05e9b",
      "version": 8,
      "weekStart": ""
    }

prometheus.yaml

    # prometheus.yaml
    global:
      scrape_interval: 5s
      evaluation_interval: 30s

    scrape_configs:
      - job_name: vllm
        static_configs:
          - targets:
              - 'host.docker.internal:8000'