# Source: https://docs.unifygtm.com/reference/signals/lookalike-companies.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unifygtm.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Lookalike Companies

> Find companies similar to your most successful customers.

## Overview

We’ve partnered with [Ocean.io](https://www.ocean.io/) — a leading Lookalike data provider — so you can run automated Plays that target lookalikes of your most successful customers.

The integration is fully managed by Unify and included in your plan, so no additional subscription or setup is required.

## Setup

### Build a new Play

Start by setting up a new Play using the Find Lookalike Companies trigger. You can also get started with our [pre-built template](https://app.unifygtm.com/dashboard/plays?templateType=SEQUENCE_LOOKALIKE_COMPANIES).

<Frame caption="The Find Lookalike Companies trigger node in the Play Builder.">
  <img src="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-build-play.png?fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=c1679fdcaa507618368fab7d31ca6aaf" data-og-width="2304" width="2304" data-og-height="1638" height="1638" data-path="images/reference/signals/lookalikes-build-play.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-build-play.png?w=280&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=ca34496b03f727a920900fbead8159c2 280w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-build-play.png?w=560&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=296543a58626202548c52f8e1fa95654 560w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-build-play.png?w=840&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=7d0c1fdfaa6a0d7a41ec6b6b844b67e6 840w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-build-play.png?w=1100&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=2078f42941b75a1a39fe2d250349ad7f 1100w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-build-play.png?w=1650&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=0023ad84e93d6ebd3eaf39a2635a6d23 1650w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-build-play.png?w=2500&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=1ea4d2cc40d30de8911fb92486569896 2500w" />
</Frame>

### Configure the Trigger

First, configure the seed companies you want to find lookalike companies for. You can do this by adding filters to select companies that meet your criteria,
just like building audiences.

<Frame caption="The criteria panel for a Find Lookalike Companies trigger.">
  <img src="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-criteria-panel.png?fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=c1b6b19abcb96637ada83885fc3594c7" data-og-width="2304" width="2304" data-og-height="1638" height="1638" data-path="images/reference/signals/lookalikes-criteria-panel.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-criteria-panel.png?w=280&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=24108a56f46defdb2a7cd8532d7f35c3 280w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-criteria-panel.png?w=560&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=e082600be56e2e8e51f92f5b6c2b53d1 560w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-criteria-panel.png?w=840&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=ad6e60a9ab61f9bb56dc6b85c4f0fa9d 840w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-criteria-panel.png?w=1100&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=533504120e70cc6efedf3c40f4d4b114 1100w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-criteria-panel.png?w=1650&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=e05e930b767632122fda43bbd544dade 1650w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-criteria-panel.png?w=2500&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=21eddece4a8dbbd255acce80fe6116e9 2500w" />
</Frame>

Next, configure the lookalike companies you want to find for each seed company.
You can set the number of lookalike companies per seed company, minimum relevance score, and more.

The previews on the right will show you a sample of the lookalike companies that will be found based on your configuration.

<Frame caption="The configuration panel for a Find Lookalike Companies trigger.">
  <img src="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-configuration-panel.png?fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=11e4dd11db05b12b7586fa07031668d5" data-og-width="2304" width="2304" data-og-height="1638" height="1638" data-path="images/reference/signals/lookalikes-configuration-panel.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-configuration-panel.png?w=280&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=d476fac45cafa4a90b0276e2e3feb54b 280w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-configuration-panel.png?w=560&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=3a5c06738c881929fe9461124612b10b 560w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-configuration-panel.png?w=840&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=56b0970bee1a35256829f2464863ef41 840w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-configuration-panel.png?w=1100&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=be8f6bd13d7d47c35c2844624973b733 1100w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-configuration-panel.png?w=1650&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=ceb8d2545cdc7e918eee00f519f9bf26 1650w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-configuration-panel.png?w=2500&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=f03b70c53fc8620d588f8a20adcc783e 2500w" />
</Frame>

Build the rest of your Play as you need, then click Publish to begin finding lookalike companies and running them through your Play.
Learn more about building Plays [here](/reference/plays/overview).

## Frequently Asked Questions

<AccordionGroup>
  <Accordion title="How do I see what seed company a lookalike company was based on?">
    Find your lookalike company in the Play Logs.

    <Frame caption="A list of Play Logs.">
      <img src="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-play-logs-list.png?fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=c53e3ff3bd3fe6640fc29b09ebd38559" data-og-width="2304" width="2304" data-og-height="1638" height="1638" data-path="images/reference/signals/lookalikes-play-logs-list.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-play-logs-list.png?w=280&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=d3eb8800359c2472569bb638d5cc207d 280w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-play-logs-list.png?w=560&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=f2c50dd46075512e21ae0aaee0d231c8 560w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-play-logs-list.png?w=840&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=eac3992bab5e864fbb6340d79c25f943 840w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-play-logs-list.png?w=1100&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=a9a1df18ad96711041cc87c582918392 1100w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-play-logs-list.png?w=1650&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=87b61c8cec907d3d07024d3dc69ee4f5 1650w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-play-logs-list.png?w=2500&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=07a3f36c7ae49d8be1ab91e46fdb4bc7 2500w" />
    </Frame>

    Click the Trigger node to see details like the seed company and the relevance score.

    <Frame caption="A log of the Play trigger.">
      <img src="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-play-log.png?fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=30d6035deef5fb8f3f86f3f223ae1e2d" data-og-width="2304" width="2304" data-og-height="1638" height="1638" data-path="images/reference/signals/lookalikes-play-log.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-play-log.png?w=280&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=0ccd3dec36f42830fa4b81fc75f8557c 280w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-play-log.png?w=560&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=3f2791becfdc4bdd1bdcea2ed0cbeec6 560w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-play-log.png?w=840&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=3399dfce5fdb3a29fff6e41b0e4222b8 840w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-play-log.png?w=1100&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=296923899e2d7127d1478c585e685c8a 1100w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-play-log.png?w=1650&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=21d1f9209a0d5c4172b0078a15d18a11 1650w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-play-log.png?w=2500&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=a88e2073261bc2306d1d40f6386e5a13 2500w" />
    </Frame>
  </Accordion>

  <Accordion title="How long does it take for Play Logs to appear for my lookalike companies?">
    Depending on the number of seed companies the Play is running on, it can take up to several hours for Play Logs to appear.
  </Accordion>

  <Accordion title="Do I get charged credits if a lookalike company falls under my exclusion rules?">
    Nope! Lookalike companies that fall under your exclusion rules will not run through the Play, and you will not be charged for them.
  </Accordion>
</AccordionGroup>
