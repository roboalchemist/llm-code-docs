# Source: https://docs.jit.io/docs/wiz-integration.md

# Wiz Integration

# Introduction

Integrating **Wiz** with Jit enhances security workflows by synchronizing findings and risks between the two platforms. This integration enables both the creation of Wiz issues directly from Jit and the enrichment of Jit findings with Wiz context, allowing teams to stay informed and act quickly. Learn more about the benefits of the integration [here](https://www.jit.io/blog/announcing-jit-wiz-bridge-the-gap-between-aspm-and-cnapp).

This bi-directional integration enables:

* **Pulling Wiz issues into Jit**: Enrich Jit’s context graph by linking Wiz issues, displaying Wiz risks on the associated finding node.
* **Pushing Jit findings into Wiz**: Relevant security findings identified in Jit are automatically pushed into Wiz as new issues, visible directly in the Wiz platform. ￼

# Integration Setup

**Please refer to Wiz platform documentation for guided integration** [here](https://docs.wiz.io/wiz-docs/docs/jit-integration)

## Quickstart

1. In Jit's web app, navigate to the **Integrations page**:

[block:image]{"images":[{"image":["https://files.readme.io/9961d774b65e38cc7612027fe242d3501d67ee37c082b907240cf1376be0d039-image_15.png",null,"Jit Integration Page w/ Wiz Integration Card"],"align":"center"}]}[/block]

2. Find the "Wiz" card and click "Connect".

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1b335bcf5d3007eca4a38d917954b441c754dc338db7b0a0fc5a55a87a2635ad-Screenshot_2025-06-04_at_16.27.52.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "400px"
    }
  ]
}
[/block]

3. You will be prompted to provide your Wiz **API keys** that should be generated [here](https://docs.wiz.io/wiz-docs/docs/jit-integration)

* Ensure you generate the API keys in the Wiz platform with the necessary permissions before proceeding.

4. After submitting your API keys, the integration will be complete.

## Integration Capabilities

Once the integration is established, Jit and Wiz automatically synchronize findings bidirectionally. Jit findings are pushed into Wiz as issues, and Wiz findings enrich Jit’s context graph.

This synchronization occurs automatically, typically within 24 hours, without requiring manual intervention.

**Jit Findings in Wiz**: Jit findings are automatically pushed into Wiz as issues, giving security teams visibility into code-level risks directly within the Wiz platform.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f25520966ef6b0b329be62e9e45027191caba781c9672235eb652defdaaf10a7-image.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "900px"
    }
  ]
}
[/block]

ℹ️ **Note**: *Matching repositories between Jit and Wiz are required only for the push functionality. If a repository exists in Jit but not in Wiz, findings from that repository will not be pushed to Wiz. However, this does not affect the enrichment of Jit findings with Wiz context*.

***

**Context Enrichment**: Wiz issues will enrich Jit's context graph, linking findings with Wiz’s risk assessment. This provides a comprehensive view of the risks associated with the security issues, visualized in the Jit platform.

![](https://files.readme.io/2f852bcfd467ae264a64c1b62f84897f47cdf636dc0f5903fc4a5ba28da0d4ba-image.png)

This integration helps streamline security workflows, offering real-time insights and an enriched understanding of both platforms' security data.