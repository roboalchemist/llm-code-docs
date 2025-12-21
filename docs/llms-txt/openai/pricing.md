# Source: https://developers.openai.com/codex/pricing.md

# Codex Pricing

<PageHeader
  title="Codex Pricing"
  descriptionClass="mb-12"
  description="Codex is included in your ChatGPT Plus, Pro, Business, Edu, or Enterprise plan."
/>

<div class="codex-pricing-grid">
  <PricingCard
    name="Plus"
    subtitle="Power a few focused coding sessions each week."
    price="$20"
    interval="/month"
    ctaLabel="Get Plus"
    ctaHref="https://chatgpt.com/explore/plus?utm_internal_source=openai_developers_codex"
  >

    - Codex on the web, CLI, IDE Extension, and iOS
    - Cloud-based integrations like automatic code review and Slack
    - The latest models, including GPT-5.2-Codex
    - GPT-5.1-Codex-Mini for up to 4x higher usage limits for local messages
    - Flexibly extend usage with [ChatGPT credits](#credits-overview)
    - Other [ChatGPT features](https://chatgpt.com/pricing) as part of the Plus plan

  </PricingCard>
  <PricingCard
    name="Pro"
    subtitle="Rely on Codex for daily full-time development."
    price="$200"
    interval="/month"
    ctaLabel="Get Pro"
    ctaHref="https://chatgpt.com/explore/pro?utm_internal_source=openai_developers_codex"
    highlight="Everything in Plus and:"
  >

    - Priority-speed processing of requests
    - 6x higher usage limits for local and cloud tasks
    - 10x more cloud-based code reviews
    - Other [ChatGPT features](https://chatgpt.com/pricing) as part of the Pro plan

  </PricingCard>
</div>

<div class="mt-8 codex-pricing-grid">
  <PricingCard
    name="Business"
    subtitle="Bring Codex into your startup or growing business."
    price="$30"
    interval="/user/month"
    ctaLabel="Try for free"
    ctaHref="https://chatgpt.com/team-sign-up?utm_internal_source=openai_developers_codex"
    highlight="Everything in Plus and:"
  >

    - Larger virtual machines to run cloud tasks faster
    - Flexibly extend usage with [ChatGPT credits](#credits-overview)
    - A secure, dedicated workspace with essential admin controls, SAML SSO, and MFA
    - No training on your business data by default. [Learn more](https://openai.com/business-data/)
    - Other [ChatGPT features](https://chatgpt.com/pricing) as part of the Business plan

  </PricingCard>
  <PricingCard
    name="Enterprise & Edu"
    subtitle="Unlock Codex for your entire organization with enterprise-grade functionality."
    interval=""
    ctaLabel="Contact sales"
    ctaHref="https://chatgpt.com/contact-sales?utm_internal_source=openai_developers_codex"
    highlight="Everything in Business and:"
  >

    - Priority-speed processing of requests
    - Enterprise-level security and controls, including SCIM, EKM, user analytics, domain verification, and role-based access controls ([RBAC](https://help.openai.com/en/articles/11750701-rbac))
    - Audit logs and usage monitoring through the [Compliance API](https://chatgpt.com/admin/api-reference#tag/Codex-Tasks)
    - Compliant with data retention and residency controls
    - Other [ChatGPT features](https://chatgpt.com/pricing) as part of the Enterprise plan

  </PricingCard>
</div>

<div class="mt-8 mb-32 codex-pricing-grid">
  <PricingCard
    class="codex-pricing-card--span-two"
    name="API Key"
    subtitle="Great for automation in shared environments like CI."
    price=""
    interval=""
    ctaLabel="Learn more"
    ctaHref="/codex/guides/api-key"
    highlight=""
  >

    - Codex in the CLI, SDK, or IDE Extension
    - No cloud-based features (GitHub code review, Slack, etc.)
    - Delayed access to new models like GPT-5.2-Codex
    - Only pay for the tokens used by Codex based on [API pricing](https://platform.openai.com/docs/pricing)

  </PricingCard>
</div>

## Frequently asked questions

### What are the usage limits for my plan?

The number of Codex messages you can send varies based on the size and complexity of your coding tasks and where you run them. Small scripts or simple functions may only consume a fraction of your allowance, while larger codebases, long-running tasks, or extended sessions that require Codex to hold more context will use significantly more per message.

<div id="usage-limits">

<table>
  <thead>
    <tr>
      <th scope="col"></th>
      <th scope="col" style="text-align:center">
        Local Messages[\*](#shared-limits) / 5h
      </th>
      <th scope="col" style="text-align:center">
        Cloud Tasks[\*](#shared-limits) / 5h
      </th>
      <th scope="col" style="text-align:center">
        Code Reviews / week
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ChatGPT Plus</td>
      <td style="text-align:center">45-225</td>
      <td style="text-align:center">10-60</td>
      <td style="text-align:center">10-25</td>
    </tr>
    <tr>
      <td>ChatGPT Pro</td>
      <td style="text-align:center">300-1500</td>
      <td style="text-align:center">50-400</td>
      <td style="text-align:center">100-250</td>
    </tr>
    <tr>
      <td>ChatGPT Business</td>
      <td style="text-align:center">45-225</td>
      <td style="text-align:center">10-60</td>
      <td style="text-align:center">10-25</td>
    </tr>
    <tr>
      <td>ChatGPT Enterprise &amp; Edu</td>
      <td colspan="3" style="text-align:center">
        No fixed limits — usage scales with [credits](#credits-overview)
      </td>
    </tr>
    <tr>
      <td>API Key</td>
      <td style="text-align:center">
        [Usage-based](https://platform.openai.com/docs/pricing)
      </td>
      <td style="text-align:center">Not available</td>
      <td style="text-align:center">Not available</td>
    </tr>
  </tbody>
</table>

</div>

<a id="shared-limits" class="footnote">
  *The usage limit of local messages and cloud tasks is a **shared five-hour
  window**. Additional weekly limits may apply.
</a>

Enterprise and Edu plans without flexible pricing include the same per-seat usage limits as Plus for most features.

GPT-5.1-Codex-Mini can be used for local tasks, providing up to 4x more usage.

### What happens when you hit usage limits?

ChatGPT Plus and Pro users who reach their usage limit can purchase additional credits to continue working without needing to upgrade their existing plan.

Business, Edu, and Enterprise plans with [flexible pricing](https://help.openai.com/en/articles/11487671-flexible-pricing-for-the-enterprise-edu-and-business-plans) can purchase additional workspace credits to continue using Codex.

If you are approaching usage limits, you can also switch to the GPT-5.1-Codex-Mini model to make your usage limits last longer.

All users may also run extra local tasks using an API key, with usage charged at [standard API rates](https://platform.openai.com/docs/pricing).

### Where can I see my current usage limits?

You can find your current limits in the [Codex usage dashboard](https://chatgpt.com/codex/settings/usage). If you want to see your remaining limits during an active Codex CLI session, you can use `/status`.

### How do credits work?

Credits let you continue using Codex after you reach your included usage limits. Usage draws down from your available credits based on the models and features you use, allowing you to extend work without interruption.

Credits per message vary based on the task size, complexity, and reasoning required. Rates listed in the table are average credit rates and also apply to the respective legacy GPT-5.1, GPT-5.1-Codex-Max, GPT-5, GPT-5-Codex, and GPT-5-Codex-Mini models. Average rates may evolve over time as new capabilities are introduced.

<div id="credits-overview">

|             |      Unit      | GPT-5.2, GPT-5.2-Codex | GPT-5.1-Codex-Mini |
| :---------- | :------------: | :--------------------: | :----------------: |
| Local Tasks |   1 message    |      \~5 credits       |     \~1 credit     |
| Cloud Tasks |   1 message    |      \~25 credits      |   Not available    |
| Code Review | 1 pull request |      \~25 credits      |   Not available    |

</div>

[Learn more about credits in ChatGPT Plus and Pro.](https://help.openai.com/en/articles/12642688-using-credits-for-flexible-usage-in-chatgpt-freegopluspro-sora)  
[Learn more about credits in ChatGPT Business, Enterprise, and Edu.](https://help.openai.com/en/articles/11487671-flexible-pricing-for-the-enterprise-edu-and-business-plans)

### What counts as Code Review usage?

Code Review usage only applies when Codex runs reviews through GitHub — for example, when you tag `@Codex` review in a pull request or enable automatic reviews on your repository. Reviews run locally or outside of GitHub count toward your general usage limits instead.

### What can I do to make my usage limits last longer?

The usage limits and credits above are average rates. You can try the following tips to maximize your limits:

- **Control the size of your prompts.** Be precise with the instructions you give Codex but remove unnecessary context.
- **Reduce the size of your AGENTS.md.** If you work on a larger project you can control the context you are injecting through AGENTS.md files by [nesting them within your repository](/codex/guides/agents-md#layer-project-instructions).
- **Limit the amount of MCPs you use.** Every [MCP](/codex/mcp) you add to Codex adds more context to your messages and drains your usage limits further. Disable any MCP servers when you don’t need them.
- **Switch to GPT-5.1-Codex-Mini for simple tasks.** Using the mini model should extend your usage limits by roughly 4x.