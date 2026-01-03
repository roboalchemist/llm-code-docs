# Source: https://docs.promptlayer.com/why-promptlayer/evaluation-and-ranking.md

# Scoring & Ranking Prompts

One of the biggest challenges in prompt engineering is understanding if Prompt A performs better than Prompt B. PromptLayer helps you solve this.

Testing in development can only get you so far. We believe the best way to understand your prompts is by analyzing them in production.

Below are some ways you can use PromptLayer to answer the following key questions:

* How much does PromptA vs PromptB cost?
* How often is PromptA used?
* Is PromptA working better than PromptB?
* Which prompts are receiving the most negative user feedback?
* How do I synthetically evaluate my prompts using LLMs?

## A/B Testing

<img src="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/split-release-flowchart.png?fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=91f035220604fe261e20c668908a1c37" alt="Dynamic Release Labels Diagram" data-og-width="1633" width="1633" data-og-height="905" height="905" data-path="images/split-release-flowchart.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/split-release-flowchart.png?w=280&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=27ee1e2b49fd3a5fba33acb6d48efd05 280w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/split-release-flowchart.png?w=560&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=c89165f89df5619709a88486627ab8af 560w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/split-release-flowchart.png?w=840&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=32bbcbe93336aa3d03ac5539324acd45 840w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/split-release-flowchart.png?w=1100&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=89775ebebeda4e249d7802c10bd97aa3 1100w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/split-release-flowchart.png?w=1650&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=2b8d2f1e404ce013db62c9564869b01d 1650w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/split-release-flowchart.png?w=2500&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=5aa3e3f1dfaa514cf0095dd4665ccfd2 2500w" />

PromptLayer is best used as an orchestration & data layer of your prompts.

That means [A/B testing](/why-promptlayer/ab-releases) is easy. Use the [Prompt Registry](/features/prompt-registry) to version templates build different tests and automatically segment versions using [dynamic release labels](/features/prompt-registry/dynamic-release-labels).

## Scoring

*Every PromptLayer request can have multiple "Scores". A score is an integer from 0-100.*

<img src="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/evaluation-score.png?fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=158df803a927d521b3212b90af71d3a2" data-og-width="508" width="508" data-og-height="323" height="323" data-path="images/evaluation-score.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/evaluation-score.png?w=280&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=6f5c631b78ed4c03cfdf13438a76f3a9 280w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/evaluation-score.png?w=560&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=e164d260d5bbf53bb3fcd814e77069d7 560w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/evaluation-score.png?w=840&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=a1c7d7274e6aa5b1eb35d57f731fda6a 840w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/evaluation-score.png?w=1100&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=fde508ed29e0f009fd2786fd2ad97633 1100w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/evaluation-score.png?w=1650&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=e467724dfd24fd7b4e733568f079beb6 1650w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/evaluation-score.png?w=2500&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=c530a2c28a30d9f5e325adfc43d83e60 2500w" />

In PromptLayer, ranking is based on Score values. Scores can be updated via the UI or programmatically, allowing for the creation of named or unnamed scores. For further details, refer to the provided documentation on prompt history, metadata, and request IDs.
The three most common ways to Score to rank your prompts are:

1. **User feedback**: Present a 👍 and 👎 to your users after the completion. A user press of one of those buttons fills in a score of \[100, 0] respectively.
2. **RLHF**: Use our visual dashboard to fill in scores by hand. You can then use this data to decide between prompt templates or to fine-tune.
3. **Synthetic Evaluation**: Use LLMs to score LLMs. After getting a completion, run an evaluation prompt on it and translate that to a score \[0, 100].

   For example, your prompt could be:

   ```
   The following is an AI chat message given to a user:

   {completion}

   --

   We are worried that the chatbot is being rude. 
   How rude is the chat on a scale of 0 to 100?
   ```

## Analytics

After populating Scores as described above, navigate to the Prompt Template page to see how each template stacks up.

<img src="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/all-templates.png?fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=a483c884b1dc47df16f378c2bb833c5f" data-og-width="2000" width="2000" data-og-height="1197" height="1197" data-path="images/all-templates.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/all-templates.png?w=280&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=16ad205e9617fc2ac2dcbabd2d33a7fd 280w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/all-templates.png?w=560&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=92bca6f487cf103cab53ea2b8c1a1bd3 560w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/all-templates.png?w=840&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=2eae855b6e05c4ddcecdd6007ed64828 840w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/all-templates.png?w=1100&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=5eb12de270b9e2b72622f6c376bafba9 1100w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/all-templates.png?w=1650&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=dbebd36756312a0cbcc17f81fafb50da 1650w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/all-templates.png?w=2500&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=d9ae7e8d12a34506f3eba569c2e7cb95 2500w" />

## Pricing

We live in the real world, so money matters. Building a prod LLM system means managing price. Some LLMs are cheaper than other LLMs. Some prompts are cheaper than other prompts.

Each request history page will tell you its individual cost:

<img src="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/individual-cost.png?fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=fab7f26ca7f626a1173f615ac099e9d4" data-og-width="2000" width="2000" data-og-height="604" height="604" data-path="images/individual-cost.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/individual-cost.png?w=280&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=2108cb7659fd1beb04e2565f0c087076 280w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/individual-cost.png?w=560&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=5aa0334f596f3356b683557980c0cf37 560w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/individual-cost.png?w=840&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=e37dc23359fedb3f2ddee91edd62e798 840w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/individual-cost.png?w=1100&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=37bf79a9ffde474efdcf30e9ced570a2 1100w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/individual-cost.png?w=1650&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=22d0f4adad233d25bd8c1948dce3b086 1650w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/individual-cost.png?w=2500&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=eb3404225e1ef120eb35cbf81fec0ac4 2500w" />

You can also see the lifetime cost of a template in the Prompt Registry template page.

<img src="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/lifetime-cost.png?fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=0ddc98b2295ce675adfe43f343f0c064" data-og-width="2000" width="2000" data-og-height="442" height="442" data-path="images/lifetime-cost.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/lifetime-cost.png?w=280&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=1353a80dee3ec5e6f27318ccb786ac69 280w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/lifetime-cost.png?w=560&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=ee1e26db04ae68b6cac1f3409f1f94a7 560w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/lifetime-cost.png?w=840&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=93d62d1014244ce3fd4d5bde4d014988 840w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/lifetime-cost.png?w=1100&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=0712df57aba61d9750129289342fd7fa 1100w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/lifetime-cost.png?w=1650&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=f8ab4a9ccea1135e6d4edb4eef692b17 1650w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/lifetime-cost.png?w=2500&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=b7c6801dcdf9a8f3382df1cac88c83d6 2500w" />


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.promptlayer.com/llms.txt