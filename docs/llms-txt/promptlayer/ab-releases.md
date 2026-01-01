# Source: https://docs.promptlayer.com/why-promptlayer/ab-releases.md

# A/B Testing

A/B Releases is a powerful feature that allows you to test different versions of your prompts in production, safely roll out updates, and segment users. 🚀

For technical details and usage instructions, check out the [Dynamic Release Labels](/features/prompt-registry/dynamic-release-labels) page.

## Overview

A/B Releases work by dynamically overloading your release labels. You can split traffic between different prompt versions based on percentages or user segments. This lets you:

* Test new prompt versions with a subset of users before a full rollout
* Gradually release updates to minimize risk
* Segment users to receive specific versions (e.g., beta users, internal employees)

## Use Cases

### Testing Prompt Updates

Have a stable prompt version that's working well but want to test an update? Create an A/B Release!

You can direct a small percentage of traffic (e.g., 20%) to the new version. If there are no issues after a week, you can slowly increase the percentage. This minimizes the risk of rolling out an update to all users at once.

<img src="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/split-release-flowchart.png?fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=91f035220604fe261e20c668908a1c37" alt="Dynamic Release Labels Diagram" data-og-width="1633" width="1633" data-og-height="905" height="905" data-path="images/split-release-flowchart.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/split-release-flowchart.png?w=280&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=27ee1e2b49fd3a5fba33acb6d48efd05 280w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/split-release-flowchart.png?w=560&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=c89165f89df5619709a88486627ab8af 560w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/split-release-flowchart.png?w=840&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=32bbcbe93336aa3d03ac5539324acd45 840w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/split-release-flowchart.png?w=1100&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=89775ebebeda4e249d7802c10bd97aa3 1100w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/split-release-flowchart.png?w=1650&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=2b8d2f1e404ce013db62c9564869b01d 1650w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/split-release-flowchart.png?w=2500&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=5aa3e3f1dfaa514cf0095dd4665ccfd2 2500w" />

### Gradual Rollouts

Ready to roll out a new prompt version but want to minimize risk? Use A/B Releases to gradually ramp up traffic to the new version.

Start with a 5% rollout, then increase to 10%, 25%, 50%, and eventually 100% as you gain confidence in the new version. This staged approach ensures a smooth transition for your users.

### User Segmentation

Want to give certain users access to a dev version of your prompt? A/B Releases make this easy.

Define user segments based on metadata (e.g., user ID, company) and specify which prompt version each segment should receive. This lets you test new versions with beta users or give internal employees access to dev versions.

For example, you could create a segment for internal user IDs and configure their traffic split to be 50% dev version and 50% stable version. Alternatively, you could segment based on the user's subscription level, giving free users access to experimental prompt versions first before rolling them out to paying customers. This allows you to gather feedback and iterate on new features without affecting your premium user base.

***

A/B Releases give you the power to experiment, safely roll out updates, and deliver targeted experiences. Try it out and take control of your prompt releases! 🎉


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.promptlayer.com/llms.txt