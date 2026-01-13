# Source: https://docs.datadoghq.com/bits_ai/bits_ai_sre/help_bits_learn.md

---
title: Help Bits learn
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Bits AI > Bits AI SRE > Help Bits learn
source_url: https://docs.datadoghq.com/bits_ai_sre/help_bits_learn/index.html
---

# Help Bits learn

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com, ap2.datadoghq.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

Reviewing Bits' findings helps Bits learn from any mistakes it makes, enabling it to produce faster and more accurate investigations in the future.

At the end of an investigation, let Bits know whether the conclusion it made was correct.

{% image
   source="https://datadog-docs.imgix.net/images/bits_ai/help_bits_ai_learn_1.ea0f70661c8335644bb5875a7e534bca.png?auto=format"
   alt="An investigation conclusion with buttons to rate the conclusion helpful or unhelpful highlighted" /%}

If the conclusion was inaccurate, provide Bits with the correct root cause. Ensure your feedback:

- Identifies the actual root cause (not just observed effects or symptoms)
- Specifies relevant services, components, or metrics
- Includes telemetry links that point to the root cause

**Example high-quality root cause feedback**: "High memory usage in auth-service pod due to memory leak in session cache, causing OOM kills every 2 hours starting at 2025-11-15 14:30 UTC. This is evidenced by `https://app.datadoghq.com/logs?<rest_of_link>`"

In addition, you can review steps that Bits took throughout the investigation and refine its behavior by selecting:

- **Improve This Step**: Share a link to a more effective query for Bits to use next time
- **Always Take This Step**: Tell Bits that this query was helpful and to run it again next time

{% image
   source="https://datadog-docs.imgix.net/images/bits_ai/bits_ai_sre_step_feedback.0be8ad3fc5a2b44ef80ced6e3ebcf3aa.png?auto=format"
   alt="A research step with options to provide feedback" /%}

### Manage memories{% #manage-memories %}

Every piece of feedback you give generates a **memory**. Bits uses these memories to enhance future investigations by recalling relevant patterns, queries, and corrections. You can navigate to the [Monitor Management](https://app.datadoghq.com/bits-ai/monitors/supported) page to view and delete memories in the **Memories** column.
