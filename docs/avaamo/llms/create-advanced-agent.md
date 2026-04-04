# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/create-advanced-agent.md

# Create Advanced agent

{% hint style="info" %}
**Note**: You can create Advanced agents only if it is enabled in your account. Contact Avaamo Support for further assistance.&#x20;
{% endhint %}

In its fundamental nature, an Advanced agent achieves the core objective of a "Conversational Assistant" by involving the user in a dialogue closely resembling human interaction.&#x20;

It utilizes an advanced inference engine behind the scenes to boost user experience and takes on a personalized approach, understanding nuances in the conversation, and transforming interactions from a robotic demeanor to a more pleasurable and "conversational" experience for the user.

For developers, this translates to a substantial reduction in the amount of training data needed for the agent to comprehend user queries. Consequently, an `Advanced agent` stands out as distinctly superior, more intelligent, and more personalized compared to a `Classic agent`. The following illustrations depict a comparison of training data between a `Classic agent` and an `Advanced agent`:

|                                                                                                                        Classic agent                                                                                                                       |                                                                                                                       Advanced agent                                                                                                                       |
| :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| <img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FeDSpekbePOODlJ3BW8dP%2Fimage.png?alt=media&#x26;token=be3fe3a2-0572-4e1a-95ac-bb77b54523af" alt="" data-size="original"> | <img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fcbl7SfijnBlT1LkckXPN%2Fimage.png?alt=media&#x26;token=1b83f4e1-7486-437b-b53f-a5c6e39d9f61" alt="" data-size="original"> |

## Key features

### **Human-like conversation**

`Advanced agent` responses are not limited to simple one-word responses but can include detailed explanations, descriptions, or discussions, depending on the complexity of the question. It makes your agent more intuitive and user-friendly, simulating human-like interactions.

### **Deep semantic understanding**

`Advanced agents` can comprehend the meaning of language beyond surface-level syntax by understanding the context, and relationships between words, and grasping the nuances of language semantics. This implies there is a massive reduction in the amount of training data required by the agent to understand the user query.

The following illustration demonstrates how an `Advanced agent` is capable of understanding different nuances and variations of "create and incident" training data:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FwLF0k0m5K3JOv32AH6T0%2Fimage.png?alt=media&#x26;token=9ebc4da9-fb3e-491b-aefa-2448b625c4d9" alt=""><figcaption></figcaption></figure>

### **Conversational memory**

`Advanced agents` can remember and maintain context throughout a conversation. This enables the system to understand references, callbacks, and evolving topics within the dialogue.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FkNgm38Pb4nUqJDIZF7YT%2Fimage.png?alt=media\&token=7ffe6c10-19ad-47cc-a57a-708186af9cb1)

## Quick preview

Here's a quick sneak peek at the `Advanced agent`:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FEEpYdnCSYQpHFO5DkHUK%2FAdvanced-agent.gif?alt=media&#x26;token=61f45231-84df-483e-abfb-05e481c7b354" alt=""><figcaption></figcaption></figure>

## Create an Advanced agent

{% hint style="info" %}
**Note**: Ensure you have met the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
{% endhint %}

* In the Avaamo Platform UI, click the **Agents** option in the top menu, navigate to the **Development** tab, and select **Advanced Agent** under **Create.**
* Specify the `Agent name, Agent description`and `Agent avatar` for the `Advanced agent`. See [Create Classic agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills), for more information on these fields.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FAqp70YIFlXKFAMF9BTP5%2Fimage.png?alt=media&#x26;token=69772f07-9173-4cc3-818e-f8df14bc89ae" alt=""><figcaption></figcaption></figure>

## Skill in an Advanced agent

A newly created Advanced agent has the `Greetings, Frustration, Unhandled and Smalltalk` skills in it by default. You can configure this skill as required. See [Built-in skills](https://docs.avaamo.com/user-guide/how-to/add-skills-to-agent#built-in-skills), for more information.

All custom skills supported in the `Classic agent` are available in the `Advanced agent` also. See [Add skills to agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills-to-agent), for more information.&#x20;

{% hint style="info" %}
**Note**: The[ Import skills](https://docs.avaamo.com/user-guide/how-to/add-skills-to-agent#import-skills) option is available only in `Classic agents`.&#x20;
{% endhint %}

## Training an Advanced agent

The Advanced agent can comprehend numerous nuances and variations in user queries. The process of adding training data, such as in the [Invocation intent of a Dialog skill ](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-invocation-intent)or a [Q\&A skill ](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/dynamic-q-and-a/build-and-manage-dynamic-q-and-a-skill/add-questions-and-answers), remains consistent with that of the `Classic agent`. However, there is a significant reduction in the volume of training data required.

The best way to train the agent is to start with a minimal set of meaningful training data, perform testing, and then iteratively train and build the agent.

1. Start with a small set of training data
2. Test with a few sets of users&#x20;
3. Add additional training as required
4. Perform UAT with UAT users. This gives an idea of the actual production use case testing
5. Add additional training as required
6. Roll it out to the production users
7. Monitor and improvise

For example, here in the invocation intent of a Dialog skill, "create an incident" training data can handle  variations such as "require assistance for a problem" without any additional training. In such cases, it is not required to add additional training data.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FwLF0k0m5K3JOv32AH6T0%2Fimage.png?alt=media&#x26;token=9ebc4da9-fb3e-491b-aefa-2448b625c4d9" alt=""><figcaption></figcaption></figure>

## What is not supported in Advanced agent?

Currently, except for the following modules, all other modules available for the `Classic agent` apply to the `Advanced agent` too:

* [Import skills](https://docs.avaamo.com/user-guide/how-to/add-skills-to-agent#import-skills) &#x20;
* [Dictionaries](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-dictionaries)
* All operations of Skills store - [Publish](https://docs.avaamo.com/user-guide/build-skills/manage-skill/publish-skill-to-skills-store#publish-skill), [Re-publish](https://docs.avaamo.com/user-guide/build-skills/manage-skill/publish-skill-to-skills-store#republish-skill), [Re-import ](https://docs.avaamo.com/user-guide/build-skills/manage-skill/import-and-re-import-skills#re-import-skill)skills
* [Entities](https://docs.avaamo.com/user-guide/overview-and-concepts/entity-types)

## Migrating to Advanced agent

* Currently migrating from a `Classic agent` to an `Advanced agent` is a manual process. Contact your dedicated Customer Success Manager for further assistance.
* Importing a `Classic agent` into an `Advanced agent` is not supported.&#x20;
