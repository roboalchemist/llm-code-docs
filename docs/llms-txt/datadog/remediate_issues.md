# Source: https://docs.datadoghq.com/bits_ai/bits_ai_sre/remediate_issues.md

---
title: Remediate issues
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Bits AI > Bits AI SRE > Remediate issues
source_url: https://docs.datadoghq.com/bits_ai_sre/remediate_issues/index.html
---

# Remediate issues

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com, ap2.datadoghq.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% callout %}
##### Join the Preview!

Suggested code fixes from the Bits AI Dev Agent is in Preview. Click **Request Access** to join the Preview program.

[Request Access](http://datadoghq.com/product-preview/bits-ai-sre-pilot-features)
{% /callout %}

After Bits AI SRE helps you identify a root cause, it can also help you take action as quickly as possible.

Bits AI SRE integrates with Bits AI Dev Agent to automatically generate code fixes. The Dev Agent connects to GitHub to create production-ready pull requests, iterates on fixes using CI logs and developer feedback, and uses multiple Datadog products to generate contextual fixes.

1. [Set up the Bits AI Dev Agent](https://docs.datadoghq.com/bits_ai/bits_ai_dev_agent/setup/). Then, after Bits AI SRE has determined a code-related root cause, you can automatically receive suggested code fixes.
1. Create a pull request, review it in GitHub, validate the change through CI, and merge when ready to fix the underlying problem.

{% image
   source="https://datadog-docs.imgix.net/images/bits_ai/bits_ai_sre_suggested_code_fix.e580873aea982c3ab1423184f6457e88.png?auto=format"
   alt="Flowchart showing Bits' investigation conclusion and a suggested code fix" /%}
