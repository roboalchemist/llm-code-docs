# Source: https://www.elastic.co/docs/explore-analyze/workflows

﻿---
title: Workflows
description: Build automated workflows in Kibana to turn data insights into action.
url: https://www.elastic.co/docs/explore-analyze/workflows
products:
  - Elastic Cloud Enterprise
  - Elastic Cloud Hosted
  - Elastic Cloud Serverless
  - Elastic Cloud on Kubernetes
  - Elastic Stack
  - Kibana
applies_to:
  - Elastic Cloud Serverless: Preview
  - Elastic Stack: Preview since 9.3
---

# Workflows
<admonition title="Welcome to the Elastic workflow docs!">
  If you've been using the [Keep HQ workflow docs](https://docs.keephq.dev/workflows/overview), it's time to make the switch. Keep HQ's workflow docs are no longer maintained, and the Elastic workflow docs are now the source of truth for all up-to-date workflow documentation.
</admonition>


## What are workflows

A workflow is a defined sequence of steps designed to achieve a specific outcome through automation. It's a reusable, versionable "recipe" that transforms inputs into actions.

## Why use workflows

Insight into your data isn't enough. The ultimate value lies in action and outcomes. Workflows complete the journey from data to insights to automated outcomes. Your critical operational data already lives in the Elastic cluster: security events, infrastructure metrics, application logs, and business context. Workflows let you automate end-to-end processes to achieve outcomes directly where that data lives, without needing external automation tools.
Workflows address common operational challenges, such as:
- **Alert fatigue**: Automate responses to reduce manual triage.
- **Understaffing**: Enable teams to do more with fewer resources.
- **Manual, repetitive work**: Automate routine tasks consistently.
- **Tool fragmentation**: Eliminate the need to add on external automation tools.

Workflows can handle a wide range of tasks, from simple, repeatable steps to complex processes.

## Who should use workflows

Workflows are for you if you want to cut down on manual effort, speed up response times, and make sure recurring situations are handled consistently.

## Key concepts

Some key concepts to understand while working with workflows:
- **Triggers**: The events or conditions that initiate a workflow. Refer to [Triggers](https://www.elastic.co/docs/explore-analyze/workflows/triggers) to learn more.
- **Steps**: The individual units of logic or action that make up a workflow. Refer to [Steps](https://www.elastic.co/docs/explore-analyze/workflows/steps) to learn more.
- **Data**: How data flows through your workflow, including inputs, constants, context variables, step outputs, and Liquid templating for dynamic values. Refer to [Data and error handling](https://www.elastic.co/docs/explore-analyze/workflows/data) to learn more.


## Workflow structure

Workflows are defined in YAML. In the YAML editor, describe _what_ the workflow should do, and the platform handles execution.
```yaml
# ═══════════════════════════════════════════════════════════════
# METADATA - Identifies and describes the workflow
# ═══════════════════════════════════════════════════════════════
name: My Workflow                   
description: What this workflow does
enabled: true                       
tags: ["demo", "production"]        

# ═══════════════════════════════════════════════════════════════
# CONSTANTS - Reusable values defined once, used throughout
# ═══════════════════════════════════════════════════════════════
consts:
  indexName: "my-index"
  environment: "production"
  alertThreshold: 100
  endpoints:                          # Can be objects/arrays
    api: "https://api.example.com"
    backup: "https://backup.example.com"

# ═══════════════════════════════════════════════════════════════
# INPUTS - Parameters passed when the workflow is triggered
# ═══════════════════════════════════════════════════════════════
inputs:
  - name: environment
    type: string
    required: true
    default: "staging"
    description: "Target environment"
  - name: dryRun
    type: boolean
    default: true

# ═══════════════════════════════════════════════════════════════
# TRIGGERS - How/when the workflow starts
# ═══════════════════════════════════════════════════════════════
triggers:
  - type: manual                     
  # - type: scheduled                 
  #   with:
        every: 1d
  # - type: alert                    

# ═══════════════════════════════════════════════════════════════
# STEPS - The actual workflow logic (executed in order)
# ═══════════════════════════════════════════════════════════════
steps:
  - name: step_one
    type: elasticsearch.search
    with:
      index: "{{consts.indexName}}"  
      query:
        match_all: {}

  - name: step_two
    type: console
    with:
      message: |
        Environment: {{inputs.environment}}             
        Found: {{steps.step_one.output.hits.total.value}}
```


## Learn more

- To create and run your first workflow, refer to [Get started with workflows](https://www.elastic.co/docs/explore-analyze/workflows/get-started).
- Understand how to use the YAML editor in Kibana to define and run your workflows. Refer to [Author workflows](https://www.elastic.co/docs/explore-analyze/workflows/author-workflows) to learn more.