# Source: https://docs.replit.com/billing/managing-spend.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.replit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing Your Spend

> Control AI costs and monitor spending with usage alerts, budgets, Plan Mode, and autonomy settings. Learn strategies to optimize your Replit usage and reduce unnecessary token consumption.

export const CreditPackTable = () => <table>
    <thead>
      <tr>
        <th>Credit Pack</th>
        <th style={{
  textAlign: 'right'
}}>Price</th>
        <th style={{
  textAlign: 'right'
}}>Discount</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>$100 credits</td>
        <td style={{
  textAlign: 'right'
}}>$100</td>
        <td style={{
  textAlign: 'right'
}}>—</td>
      </tr>
      <tr>
        <td>$300 credits</td>
        <td style={{
  textAlign: 'right'
}}>$290</td>
        <td style={{
  textAlign: 'right'
}}>$10 off</td>
      </tr>
      <tr>
        <td>$500 credits</td>
        <td style={{
  textAlign: 'right'
}}>$480</td>
        <td style={{
  textAlign: 'right'
}}>$20 off</td>
      </tr>
      <tr>
        <td>$1,000 credits</td>
        <td style={{
  textAlign: 'right'
}}>$950</td>
        <td style={{
  textAlign: 'right'
}}>$50 off</td>
      </tr>
    </tbody>
  </table>;

export const OrganizationBudgetIncrement = '$500';

You can control your costs on Replit by using built-in budget controls, optimizing how you work with [AI Agent](/replitai/agent), purchasing credit packs, and monitoring your usage patterns. Learn more about [AI billing](/billing/ai-billing).

## Optimize AI costs

AI features like [Agent](/replitai/agent) are powerful tools, but strategic use can help you maximize value while controlling costs. Here are effective ways to reduce AI spending.

### Use Plan Mode for cost-effective collaboration

[Plan Mode](/replitai/plan-mode) is one of the most effective ways to save on AI costs. When you enable Plan Mode, Agent creates a detailed plan without making any code changes. This approach offers several cost benefits:

* **Chat before committing**: Discuss and refine the approach with Agent before any work begins
* **Lower token costs**: Planning conversations use fewer tokens than code generation and editing
* **Precision targeting**: Review and adjust the plan to ensure Agent only works on what matters
* **Iterative refinement**: Get the scope right before spending tokens on implementation

Use [Plan Mode](/replitai/plan-mode) when you're exploring solutions, refining requirements, or want to understand the approach before implementation.

### Control costs with autonomy settings

[Agent's autonomy modes](/replitai/autonomy-level) give you direct control over how much automatic work is performed, which directly impacts your token usage:

* **Lower autonomy modes**: Give you more control over each change, reducing unnecessary edits and token consumption
* **Review before execution**: Monitor what Agent plans to do before it makes changes
* **Selective approval**: Choose which changes to apply, avoiding work that doesn't align with your goals
* **Reduced iterations**: More oversight means fewer correction cycles and wasted tokens

Consider using [lower autonomy settings](/replitai/autonomy-level) when working on critical code, during budget-conscious periods, or when you want to learn from Agent's approach while maintaining tight cost control.

<Tip>
  Combine [Plan Mode](/replitai/plan-mode) with [lower autonomy settings](/replitai/autonomy-level) for maximum cost control. Plan first, then approve changes step by step.
</Tip>

## Purchase credit packs

If you're on a Core or Teams plan and need additional credits beyond your monthly subscription allowance, you can purchase credit packs directly from your billing page. Credit packs have discounts when you buy larger amounts, making them ideal for covering temporary usage spikes or preparing for larger projects.

### Available credit packs

Credit packs are available in four sizes, with increasing discounts on larger purchases:

<CreditPackTable />

### How credit packs work

* **Purchase location**: Available on your billing page for Core and Teams plan customers
* **Expiration**: Credit packs expire six months after the purchase date
* **No renewal**: Credit packs do not automatically renew
* **No rollover**: Unused credits from a pack do not roll over after expiration
* **Automatic usage**: Credits are automatically used from the credit pack that expires earliest first, helping you maximize the value of your purchases

<Note>
  Your usage alerts and budgets will apply to usage after you use any credit packs you may have. If you want to limit your usage to just credits you've purchased in your pack, set any alerts or limits to \$0.01.
</Note>

## Set up alerts and budgets

You can establish monthly usage alerts and budgets for all usage-based billing services to monitor and control your costs.

### Usage alerts

Usage alerts notify you when you reach a specific spending threshold beyond your monthly credits. You'll receive notifications on Replit and via email when you hit your set amount.

For Core accounts, visit your [account page](https://replit.com/account#billing) to set up a usage alert. For organizations, you can set your usage alert via the [usage page](https://replit.com/usage) by selecting **Manage** under **Usage total**.

### Service shutdown limit

When this limit is reached, services will be suspended until the budget is increased or the next billing cycle begins. This will help prevent extra charges.

For Core accounts, visit your [account page](https://replit.com/account#billing) to set up a service shutdown limit.

### Organization budgets

For organizations, you can set your usage budget from the [settings page](https://replit.com/t/replit/settings/billing). Budgets must be in increments of {OrganizationBudgetIncrement}.

<Note>You must have organization admin or owner permissions to enable a monthly usage limit. If you don't have access, contact your organization owner.</Note>

### Organization admin controls

Organization admins can manage AI model access and integrations from the [organization billing settings](https://replit.com/t/replit/settings/billing).

**Disable external AI model integrations**

Enable this setting to block all users in the organization from using external AI model integrations (such as OpenAI, Anthropic, xAI, and Perplexity through Replit's managed connectors).

Enable this setting to block all users in the organization from using Replit-managed AI integrations.
