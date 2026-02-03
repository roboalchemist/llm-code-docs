# Source: https://docs.promptlayer.com/features/prompt-registry/dynamic-release-labels.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.promptlayer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Dynamic Release Labels

Dynamic Release Labels allow you to overload release labels and dynamically route traffic to different prompt versions based on percentages or user segments. 🏷️

For an overview of the benefits and key use cases, check out our [A/B Releases](/why-promptlayer/ab-releases) page.

## Overview

Normally, a release label (e.g., "prod") points to a specific prompt version. Dynamic Release Labels let you overload this mapping and split traffic between multiple versions.

This is powered by the A/B Releases feature. When you create an A/B Release, it dynamically routes requests for the specified release label based on your configuration.

<img src="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/split-release-flowchart.png?fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=91f035220604fe261e20c668908a1c37" alt="Dynamic Release Labels Diagram" data-og-width="1633" width="1633" data-og-height="905" height="905" data-path="images/split-release-flowchart.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/split-release-flowchart.png?w=280&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=27ee1e2b49fd3a5fba33acb6d48efd05 280w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/split-release-flowchart.png?w=560&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=c89165f89df5619709a88486627ab8af 560w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/split-release-flowchart.png?w=840&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=32bbcbe93336aa3d03ac5539324acd45 840w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/split-release-flowchart.png?w=1100&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=89775ebebeda4e249d7802c10bd97aa3 1100w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/split-release-flowchart.png?w=1650&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=2b8d2f1e404ce013db62c9564869b01d 1650w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/split-release-flowchart.png?w=2500&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=5aa3e3f1dfaa514cf0095dd4665ccfd2 2500w" />

## Usage

<video controls width="100%">
  <source src="https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/videos/ab-release.mp4?fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=27a458a417b1f939145de1aec13e7c94" type="video/mp4" data-path="videos/ab-release.mp4" />

  Your browser does not support the video tag.
</video>

1. Navigate to the A/B Releases Registry in the PromptLayer UI.
2. Create a new A/B Release and select the release label to overload (e.g., "prod").
3. See the base prompt version and choose the version(s) to release.
4. Set the traffic percentages for each version.
   * The percentages must add up to 100%.
   * Example: 90% to version 3 (stable), 10% to version 4 (new).
5. (Optional) Add user segments and define which version each segment should receive.
   * Segments are defined using request metadata (e.g., user ID, company).
   * Example: Internal employees receive version 4 (dev) 50% of the time.
6. Save the A/B Release. It will now dynamically route traffic for the specified release label.

**Important**: When [logging requests](/features/prompt-history/tracking-templates), make sure to log the specific version returned, not just the release label. The label will always point to the original version in your logs.

To stop dynamically routing traffic, simply delete the A/B Release. The release label will revert to its base mapping.

***

Dynamic Release Labels give you fine-grained control over prompt version routing. Use them to safely test updates, roll out new versions, and segment users. 🎯
