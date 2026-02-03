# Source: https://docs.datadoghq.com/events/pipelines_and_processors/remapper.md

---
title: Remapper
description: >-
  Remap source attributes or tags to target attributes or tags with optional
  type casting
breadcrumbs: Docs > Event Management > Pipelines and Processors > Remapper
---

# Remapper

## Overview{% #overview %}

The remapper processor remaps any source attribute(s) or tags to another target attribute or tag. For example, remap `user` by `firstname` to target your logs in the Events Explorer:

{% image
   source="https://datadog-docs.imgix.net/images/logs/processing/processors/attribute_post_remapping.76a842ae0273ecc992f47af965a2a377.png?auto=format"
   alt="Attribute after remapping" /%}

Additional constraints, such as `:` or `,`, are not allowed in the target tag/attribute name.

If the target of the remapper is an attribute, the remapper can also try to cast the value to a new type (`String`, `Integer` or `Double`). If the cast is not possible, the original type is kept.

**Note**: The decimal separator for `Double` need to be `.`.

Define the remapper processor on the [**Pipelines** page](https://app.datadoghq.com/event/settings/pipelines). For example, remap `user` to `user.firstname`.

{% image
   source="https://datadog-docs.imgix.net/images/logs/log_configuration/processor/remapper.4ed74daa20b10135620936d0f5410b4c.png?auto=format"
   alt="Attribute remapper processor" /%}
