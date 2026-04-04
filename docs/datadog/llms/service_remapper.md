# Source: https://docs.datadoghq.com/events/pipelines_and_processors/service_remapper.md

---
title: Service Remapper
description: Assign one or more attributes to events as the official service
breadcrumbs: Docs > Event Management > Pipelines and Processors > Service Remapper
---

# Service Remapper

The service remapper processor assigns one or more attributes to your events as the official service.

**Note**: If multiple service remapper processors are applied to a pipeline, only the first one (according to the pipeline's order) is taken into account.

Define the events service remapper processor like so

{% image
   source="https://datadog-docs.imgix.net/images/logs/log_configuration/processor/service_remapper.6d8fe070a5a0aa20851e06695ef54613.png?auto=format"
   alt="Service remapper processor" /%}


