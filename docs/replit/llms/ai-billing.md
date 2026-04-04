# Source: https://docs.replit.com/billing/ai-billing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.replit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Replit AI Billing

> Learn how billing and credits work for Replit AI features including Agent usage, checkpoints, and managing your spend.

export const AgentCheckpointCost = '$0.25';

export const TeamsCredits = '$40';

export const CoreCredits = '$25';

export const NewUserFreeAgentCheckpoints = '10';

Replit AI features use usage-based billing to charge you based on what you build and how much you use our AI-powered tools. This ensures you only pay for the value you receive from Agent.

## Getting started

**All subscribers** receive one-time free Agent checkpoints.

Additional monthly credits automatically apply to AI usage:

* **Core subscribers**: {CoreCredits} per month
* **Teams subscribers**: {TeamsCredits} per user per month

These credits cover Agent and other Replit cloud services like published apps, storage, and databases.

## Agent billing

<Frame>
  <img src="https://mintcdn.com/replit/-6g2hQCrMskerX65/images/billing/checkpoint.png?fit=max&auto=format&n=-6g2hQCrMskerX65&q=85&s=1897730e35c7eec7993b76bacd86bf2d" alt="Replit Agent interface showing chat and checkpoint system" data-og-width="1999" width="1999" data-og-height="1242" height="1242" data-path="images/billing/checkpoint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/-6g2hQCrMskerX65/images/billing/checkpoint.png?w=280&fit=max&auto=format&n=-6g2hQCrMskerX65&q=85&s=4fed09b24054d2a5470c77ce5d4a6b9e 280w, https://mintcdn.com/replit/-6g2hQCrMskerX65/images/billing/checkpoint.png?w=560&fit=max&auto=format&n=-6g2hQCrMskerX65&q=85&s=897980bdfaa7e0ac754b23ba202ffc4a 560w, https://mintcdn.com/replit/-6g2hQCrMskerX65/images/billing/checkpoint.png?w=840&fit=max&auto=format&n=-6g2hQCrMskerX65&q=85&s=785341271486c368d12fb42b239a5129 840w, https://mintcdn.com/replit/-6g2hQCrMskerX65/images/billing/checkpoint.png?w=1100&fit=max&auto=format&n=-6g2hQCrMskerX65&q=85&s=6415d73284d58a851f2ce50471be0481 1100w, https://mintcdn.com/replit/-6g2hQCrMskerX65/images/billing/checkpoint.png?w=1650&fit=max&auto=format&n=-6g2hQCrMskerX65&q=85&s=28d8ca0a270b039477b775fb2fc5eab1 1650w, https://mintcdn.com/replit/-6g2hQCrMskerX65/images/billing/checkpoint.png?w=2500&fit=max&auto=format&n=-6g2hQCrMskerX65&q=85&s=37912693a5ac70fc4af7c5c2511e9b9e 2500w" />
</Frame>

Replit Agent uses **effort-based pricing** that scales with the complexity of your request. You pay based on the actual work Agent performs, ensuring fair pricing whether you're making small tweaks or building complex features. This same pricing applies to all Agent usage, including Plan Mode conversations.

**All Agent interactions are billable** - whether Agent responds with text guidance or makes code changes, there is always a charge, though smaller requests cost less.

### How effort-based pricing works

When you chat with Agent in "Build Mode", it creates **checkpoints** that capture completed work on your request:

* **Simple requests** (like bug fixes or small changes) typically cost less than the previous {AgentCheckpointCost} fixed price
* **Complex builds** (like full features or integrations) are bundled into one checkpoint that may cost more than {AgentCheckpointCost} but reflect the total effort involved
* **One checkpoint per request** eliminates intermediate checkpoints and reduces billing noise
* **Transparent pricing** shows you exactly what you're paying for each completed task

<Info>
  A checkpoint occurs when Agent completes work on your request and implements the requested functionality in your code.
</Info>

It's important to note, that in cases where the Agent performed work by answering a question or request, but didn't make code changes (e.g. in Plan Mode), there is still a charge associated with that work, even if there's not a checkpoint shown. Checkpoints are generally only shown to the user when there are code changes completed.

For detailed information about what checkpoints capture and how they work, see [Checkpoints and Rollbacks](/replitai/checkpoints-and-rollbacks).

To understand the cost of sample apps, check out our simple [interactive demo](https://agent-pricing.replit.app/).

<Frame>
  <img src="https://mintcdn.com/replit/-6g2hQCrMskerX65/images/billing/pricing-demo.png?fit=max&auto=format&n=-6g2hQCrMskerX65&q=85&s=968a300b8a4a318388c29037cc5b10e7" alt="Replit Agent pricing demo" data-og-width="4080" width="4080" data-og-height="2296" height="2296" data-path="images/billing/pricing-demo.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/-6g2hQCrMskerX65/images/billing/pricing-demo.png?w=280&fit=max&auto=format&n=-6g2hQCrMskerX65&q=85&s=915a943bf9153ea8fe9ee690c1e0b2ef 280w, https://mintcdn.com/replit/-6g2hQCrMskerX65/images/billing/pricing-demo.png?w=560&fit=max&auto=format&n=-6g2hQCrMskerX65&q=85&s=90a19ee714d4fe62ccbe13f1f0eb041e 560w, https://mintcdn.com/replit/-6g2hQCrMskerX65/images/billing/pricing-demo.png?w=840&fit=max&auto=format&n=-6g2hQCrMskerX65&q=85&s=2ffd6ef0893544e47c664a0f909579f3 840w, https://mintcdn.com/replit/-6g2hQCrMskerX65/images/billing/pricing-demo.png?w=1100&fit=max&auto=format&n=-6g2hQCrMskerX65&q=85&s=edc9ecacc33888cb113967fe04043264 1100w, https://mintcdn.com/replit/-6g2hQCrMskerX65/images/billing/pricing-demo.png?w=1650&fit=max&auto=format&n=-6g2hQCrMskerX65&q=85&s=1df9b6ceb8f99d1c8f13a56c01d2a859 1650w, https://mintcdn.com/replit/-6g2hQCrMskerX65/images/billing/pricing-demo.png?w=2500&fit=max&auto=format&n=-6g2hQCrMskerX65&q=85&s=528b180d954db6d7a6e2914dce512d7c 2500w" />
</Frame>

### Track your usage

You can monitor your Agent spending in real-time:

1. **Agent tab**: View costs for individual checkpoints by hovering over the usage icon
2. **Usage dashboard**: See detailed billing information for the current period
3. **Account settings**: Set up alerts and budgets to control spending

<Tip>
  Usage data can take up to 30 minutes to appear on your usage dashboard.
</Tip>

## Managing your spend

Take control of your AI spending with Replit's built-in budget tools:

* **Usage alerts**: Get notified when you reach spending thresholds
* **Budget limits**: Set hard caps to prevent unexpected charges
* **Real-time tracking**: Monitor costs as you build
* **Credit packs**: Purchase additional credits with discounts on larger purchases. See [Managing Your Spend](/billing/managing-spend) for details.

<CardGroup cols={2}>
  <Card title="Set Up Alerts" href="/billing/managing-spend">
    Configure email notifications when you reach custom spending amounts
  </Card>

  <Card title="Usage Dashboard" href="https://replit.com/usage">
    View detailed breakdowns of your AI and cloud service costs
  </Card>
</CardGroup>

## Next steps

Ready to start building with AI? Here's how to get the most value from your credits:

* **Try Agent first**: Use your free checkpoints to explore Agent's capabilities
* **Start small**: Begin with simple requests to understand effort-based pricing
* **Use Fast mode**: Leverage [Fast mode](/replitai/fast-mode) for quick, targeted edits
* **Set up alerts**: Configure spending notifications before you exceed your credits

Learn more about [Replit's AI tools](/category/replit-ai) or explore our [pricing plans](https://replit.com/pricing).
