# Source: https://docs.jit.io/docs/contextual-prioritization-context-engine.md

# Contextual prioritization (Context Engine)

## Understanding the 'Context Engine'

### Why do we need a context engine?

In vulnerability management, context is key. While the CVSS severity score measures the potential risk of a vulnerability, it doesn't account for the environment in which the vulnerability exists. For example, a high CVSS score might be less critical if it affects a non-critical part of your infrastructure. In contrast, a medium CVSS score could be more urgent if it impacts a business-critical system.

The Context Engine enhances prioritization by factoring in both the likelihood of exploitation and the potential impact within your specific environment. This ensures that security efforts focus on the most significant risks, not just those with the highest severity scores.

Here is a demo video for using Jit's contextual prioritization:

[block:embed]
{
  "html": "<iframe class=\"embedly-embed\" src=\"//cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2FRNMQb7WEtj0%3Ffeature%3Doembed&display_name=YouTube&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DRNMQb7WEtj0&image=https%3A%2F%2Fi.ytimg.com%2Fvi%2FRNMQb7WEtj0%2Fhqdefault.jpg&type=text%2Fhtml&schema=youtube\" width=\"854\" height=\"480\" scrolling=\"no\" title=\"YouTube embed\" frameborder=\"0\" allow=\"autoplay; fullscreen; encrypted-media; picture-in-picture;\" allowfullscreen=\"true\"></iframe>",
  "url": "https://www.youtube.com/watch?v=RNMQb7WEtj0",
  "title": "Prioritize The Security Issues That Matter With Context Engine",
  "favicon": "https://www.youtube.com/favicon.ico",
  "image": "https://i.ytimg.com/vi/RNMQb7WEtj0/hqdefault.jpg",
  "provider": "https://www.youtube.com/",
  "href": "https://www.youtube.com/watch?v=RNMQb7WEtj0",
  "typeOfEmbed": "youtube"
}
[/block]

<br />

### How the Context Engine Maps, Prioritizes, and Scores

1. **Resource Connection Mapping:**

The Context Engine identifies all resources linked to a particular finding or other resource. Starting with a security finding and the resource where the security finding resides, the engine maps out all connected resources that could influence the exposure of the initial insecure resource.

For example, a GitHub repository might reveal connections to a Lambda function, which in turn is connected to an internet-facing API.

This mapping can be visualized in the context engine graph, which is automatically generated for each security finding once the user has integrated Jit with their AWS environment:

![](https://files.readme.io/7e8eeb2-image.png)

2. **Priority Factor Generation and Propagation:**

Priority Factors are criteria the Context Engine uses to rank the importance of resources and findings based on the characteristics of affected resources, such as being in a production environment or involving sensitive credentials. These factors are assigned to findings and propagate through connected resources.

For example, if an API marked as internet-facing is connected to a Lambda function and a repository, both the Lambda function and the repository inherit the "internet-facing" Priority Factor, ensuring consistent prioritization across the system.

These Priority Factors are automatically assigned to resources by the Context Engine.

Examples of Priority Factors include:

* Database Access
* Production Environment
* Sensitive Credentials
* Internet-facing

There are also manual labels that can be added, like "Business-Critical".

These factors are visible as labels on the resources in the context engine graph:

![](https://files.readme.io/12723af-image.png)

3. **Priority calculation:**

Each Priority Factor in the Context Engine has a specific score which is weighted based on its significance. Jit's risk score assigned to findings and resources is calculated by summing the weights of all relevant Priority Factors.

This score reflects the criticality, taking into account the context provided by these factors. For instance, a finding with priority factors like "Production Environment" and "Critical Severity" would score higher than one with less critical factors, effectively guiding the prioritization process.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a282227fb61223257bb36d38dddd122eac80a0a2c15ffa92258ff0998381d24a-Screenshot_2024-12-27_at_4.59.39_PM.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]