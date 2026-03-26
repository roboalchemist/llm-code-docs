# Source: https://docs.api7.ai/enterprise/3.2.16.7/reference/configuration-adc.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/reference/configuration-adc.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/reference/configuration-adc.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/reference/configuration-adc.md

# Source: https://docs.api7.ai/enterprise/reference/configuration-adc.md

# Source: https://docs.api7.ai/enterprise/3.8.x/reference/configuration-adc.md

# Source: https://docs.api7.ai/enterprise/3.7.x/reference/configuration-adc.md

# Source: https://docs.api7.ai/enterprise/3.6.x/reference/configuration-adc.md

# Source: https://docs.api7.ai/enterprise/3.5.x/reference/configuration-adc.md

# Source: https://docs.api7.ai/enterprise/3.4.x/reference/configuration-adc.md

# Source: https://docs.api7.ai/enterprise/3.3.x/reference/configuration-adc.md

# Configuration Reference

ADC uses a single configuration file or multiple configuration files to define services, routes, plugins, and other configurations in API7 Enterprise. The configuration file can either be in YAML or JSON format and serves as the single source of truth.

This document provides a sample configuration file that can be used as a reference to create your own configuration files. See the [command reference](https://docs.api7.ai/enterprise/3.3.x/reference/adc.md) for more information on using the configuration file(s) with ADC.

## Sample Configuration File[â](#sample-configuration-file "Direct link to Sample Configuration File")

The following configuration file defines two services with multiple routes and labels, two consumers with key-authentication credentials, and a global rule configuring the Prometheus plugin:

adc.yaml

```
services:
  - name: mockbin Service
    labels:
      deployment: staging
    upstream:
      name: Default Upstream
      scheme: http
      type: roundrobin
      hash_on: vars
      nodes:
        - host: mock.api7.ai
          port: 80
          weight: 100
          priority: 0
      timeout:
        connect: 60
        send: 60
        read: 60
      retry_timeout: 0
      keepalive_pool:
        size: 320
        idle_timeout: 60
        requests: 1000
      pass_host: pass
    strip_path_prefix: true
    routes:
      - uris:
          - /api
        name: api
        methods:
          - GET
        enable_websocket: false
        priority: 0
  - name: httpbin Service
    labels:
      deployment: production
    upstream:
      name: Default Upstream
      scheme: http
      nodes:
        - host: httpbin.org
          port: 80
    routes:
      - uris:
          - /ip
        name: ip
        labels:
          app: catalog
        methods:
          - GET
      - uris:
          - /anything/*
        name: anything
        methods:
          - GET
consumers:
  - username: Jane
    labels:
      organisation: ACME
    credentials:
      - name: primary-key
        labels:
          type: internal
        type: key-auth
        config:
          key: c1_yN0nCWousUfiR4EzfH
        metadata:
          id: 9ae2df2b-e578-46d9-8357-cf7c3cd64d51
  - username: John
    labels:
      organisation: API7.ai
    credentials:
      - name: primary-key
        type: key-auth
        config:
          key: EIul6mAuYkLJ27on1aJD4
        metadata:
          id: c5e8c41e-37c5-4329-87a9-ba2e6916cfe3
global_rules:
  prometheus:
    _meta:
      disable: false
    prefer_name: false
```
