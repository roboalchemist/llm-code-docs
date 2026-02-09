# Source: https://www.mintlify.com/docs/ai/assistant.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.mintlify.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Assistant

> Add AI-powered chat to your docs that answers questions, cites sources, and generates code examples.

<Info>
  The assistant is automatically enabled on [Pro and Enterprise plans](https://mintlify.com/pricing?ref=assistant).
</Info>

## About the assistant

The assistant answers questions about your documentation through natural language queries. Users access the assistant on your documentation site, so they can find answers quickly and succeed with your product even if they don't know where to look.

The assistant uses agentic RAG (retrieval-augmented generation) with tool calling. When users ask questions, the assistant:

* **Searches and retrieves** relevant content from your documentation to provide accurate answers.
* **Cites sources** and provides navigable links to take users directly to referenced pages.
* **Generates copyable code examples** to help users implement solutions from your documentation.

You can view assistant usage through your dashboard to understand user behavior and documentation effectiveness. Export and analyze query data to help identify:

* Frequently asked questions that might need better coverage.
* Content gaps where users struggle to find answers.
* Popular topics that could benefit from additional content.

### How indexing works

The assistant automatically indexes your published documentation to answer questions accurately. When you publish changes, the assistant immediately indexes new, updated, or deleted content. The assistant does not index draft branches or preview deployments.

By default, the assistant does not index hidden pages. To include hidden pages in the assistant's index, set `seo.indexing: "all"` in your `docs.json`. See [Hidden pages](/organize/hidden-pages#search-seo-and-ai-indexing) for more information.

### How the assistant handles unknown questions

The assistant only answers questions based on information in your documentation. If it cannot find relevant information after searching, it responds that it doesn't have enough information to answer.

You can [set a deflection email](/ai/assistant#set-deflection-email) so that the assistant provides your support email to users whose questions it cannot answer. This gives users a path forward, even if the documentation doesn't address their specific question.

## Configure the assistant

The assistant is active on Pro and Enterprise plans by default.

Manage the assistant from the [Assistant Configurations](https://dashboard.mintlify.com/products/assistant/settings) page of your dashboard. Enable or disable the assistant, configure response handling, add default questions, and manage your message allowance.

### Enable or disable the assistant

Toggle the assistant status to enable or disable the assistant for your documentation site.

<Frame>
  <img src="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-light.png?fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=723881f19ac3ad665a774eeb6f3b8652" alt="The assistant status toggle in the dashboard." className="block dark:hidden" data-og-width="2038" width="2038" data-og-height="338" height="338" data-path="images/assistant/status-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-light.png?w=280&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=324018ab573007ce00dea0256aec2789 280w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-light.png?w=560&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=08fa6f1070c0dfc73518d184244fab09 560w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-light.png?w=840&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=9396ddf191ca4433612550f1a6d8aa74 840w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-light.png?w=1100&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=08b1fcdd73408ae3aa2d441a1ad7b370 1100w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-light.png?w=1650&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=210932e2ffa0ed0f37e67cee7f9f5991 1650w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-light.png?w=2500&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=8a9373c2ccd834e7d146b06164874a8d 2500w" />

  <img src="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-dark.png?fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=8c7ae23c57d3db8f67a649b0f09d45c4" alt="The assistant status toggle in the dashboard." className="hidden dark:block" data-og-width="2040" width="2040" data-og-height="338" height="338" data-path="images/assistant/status-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-dark.png?w=280&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=0989add1e16e03d0f516c2d0e3271cc7 280w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-dark.png?w=560&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=af084192f28f689c1506a15750e50167 560w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-dark.png?w=840&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=7b36249ad898762cae73b78c8bc97477 840w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-dark.png?w=1100&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=a224b83ac59895b6ce7884c90a24842d 1100w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-dark.png?w=1650&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=161b1e9ac9cbf2c1b678fa59240d99cb 1650w, https://mintcdn.com/mintlify/qxFvxlkWYrjV0OaV/images/assistant/status-dark.png?w=2500&fit=max&auto=format&n=qxFvxlkWYrjV0OaV&q=85&s=8d5763ab56eba1c7d97c987b60b3148b 2500w" />
</Frame>

### Set deflection email

In the Response Handling section, enable the assistant to redirect unanswered questions to your support team.

Specify an email address for the assistant to give to users if it cannot answer their question. You can also enable a "Contact support" button to appear in the assistant chat panel.

<Frame>
  <img src="https://mintcdn.com/mintlify/RnZ31raTBKoRr5sX/images/assistant/deflection-light.png?fit=max&auto=format&n=RnZ31raTBKoRr5sX&q=85&s=d63b7b91381f5f2ca86790610fe4337b" alt="The assistant deflection panel in the dashboard. Assistant deflection is toggled on and support@mintlify.com is set as the deflection email." className="block dark:hidden" data-og-width="1096" width="1096" data-og-height="564" height="564" data-path="images/assistant/deflection-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/RnZ31raTBKoRr5sX/images/assistant/deflection-light.png?w=280&fit=max&auto=format&n=RnZ31raTBKoRr5sX&q=85&s=46f7e3aa3dc69c4d37f8535152ceefa5 280w, https://mintcdn.com/mintlify/RnZ31raTBKoRr5sX/images/assistant/deflection-light.png?w=560&fit=max&auto=format&n=RnZ31raTBKoRr5sX&q=85&s=1b1d58555eda5701d533065d29dedab6 560w, https://mintcdn.com/mintlify/RnZ31raTBKoRr5sX/images/assistant/deflection-light.png?w=840&fit=max&auto=format&n=RnZ31raTBKoRr5sX&q=85&s=7ee8e65867a1a62b7d372dd97d2488cb 840w, https://mintcdn.com/mintlify/RnZ31raTBKoRr5sX/images/assistant/deflection-light.png?w=1100&fit=max&auto=format&n=RnZ31raTBKoRr5sX&q=85&s=36ed8b9208d7828462761631ff99efa2 1100w, https://mintcdn.com/mintlify/RnZ31raTBKoRr5sX/images/assistant/deflection-light.png?w=1650&fit=max&auto=format&n=RnZ31raTBKoRr5sX&q=85&s=df54ea17bc0c316dd8cc5fa7e7dc660c 1650w, https://mintcdn.com/mintlify/RnZ31raTBKoRr5sX/images/assistant/deflection-light.png?w=2500&fit=max&auto=format&n=RnZ31raTBKoRr5sX&q=85&s=8f03a830c621363a4b6a38c0653eca8c 2500w" />

  <img src="https://mintcdn.com/mintlify/RnZ31raTBKoRr5sX/images/assistant/deflection-dark.png?fit=max&auto=format&n=RnZ31raTBKoRr5sX&q=85&s=f422e292dd30a1a3a488048ba176dddd" alt="The assistant deflection panel in the dashboard. Assistant deflection is toggled on and support@mintlify.com is set as the deflection email." className="hidden dark:block" data-og-width="1098" width="1098" data-og-height="566" height="566" data-path="images/assistant/deflection-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/RnZ31raTBKoRr5sX/images/assistant/deflection-dark.png?w=280&fit=max&auto=format&n=RnZ31raTBKoRr5sX&q=85&s=87c1c87115f53dbcecdfd2ca5cc19f97 280w, https://mintcdn.com/mintlify/RnZ31raTBKoRr5sX/images/assistant/deflection-dark.png?w=560&fit=max&auto=format&n=RnZ31raTBKoRr5sX&q=85&s=02dcbdcf22672919bb38a55311db1d38 560w, https://mintcdn.com/mintlify/RnZ31raTBKoRr5sX/images/assistant/deflection-dark.png?w=840&fit=max&auto=format&n=RnZ31raTBKoRr5sX&q=85&s=f43ade9ffa049ec20d1863be83170c96 840w, https://mintcdn.com/mintlify/RnZ31raTBKoRr5sX/images/assistant/deflection-dark.png?w=1100&fit=max&auto=format&n=RnZ31raTBKoRr5sX&q=85&s=0fd294e10c00b0283b66c490bb38728e 1100w, https://mintcdn.com/mintlify/RnZ31raTBKoRr5sX/images/assistant/deflection-dark.png?w=1650&fit=max&auto=format&n=RnZ31raTBKoRr5sX&q=85&s=8649f39ec8f1332565c4dc650ebe805d 1650w, https://mintcdn.com/mintlify/RnZ31raTBKoRr5sX/images/assistant/deflection-dark.png?w=2500&fit=max&auto=format&n=RnZ31raTBKoRr5sX&q=85&s=d4c56a134908e69181b8d642512fbf9b 2500w" />
</Frame>

### Search domains

In the Response Handling section, configure domains that the assistant can search for additional context when answering questions.

* Domains must be publicly available.
* Domains that require JavaScript to load are not supported.

<Frame>
  <img src="https://mintcdn.com/mintlify/2qBICQFhOKqkes42/images/assistant/search-domains-light.png?fit=max&auto=format&n=2qBICQFhOKqkes42&q=85&s=a15d483e0eee1b9a55a8ff6583a7d331" alt="The assistant search domains panel enabled in the dashboard. The assistant is configured to search the mintlify.com/pricing domain." className="block dark:hidden" data-og-width="838" width="838" data-og-height="624" height="624" data-path="images/assistant/search-domains-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/2qBICQFhOKqkes42/images/assistant/search-domains-light.png?w=280&fit=max&auto=format&n=2qBICQFhOKqkes42&q=85&s=4d0f83ce02f20d008ff2982e72b6fd8b 280w, https://mintcdn.com/mintlify/2qBICQFhOKqkes42/images/assistant/search-domains-light.png?w=560&fit=max&auto=format&n=2qBICQFhOKqkes42&q=85&s=1d31072115522e70f390229e45527c52 560w, https://mintcdn.com/mintlify/2qBICQFhOKqkes42/images/assistant/search-domains-light.png?w=840&fit=max&auto=format&n=2qBICQFhOKqkes42&q=85&s=f2b78a7af12600435e38de9ea4f88a60 840w, https://mintcdn.com/mintlify/2qBICQFhOKqkes42/images/assistant/search-domains-light.png?w=1100&fit=max&auto=format&n=2qBICQFhOKqkes42&q=85&s=1827537e6852dff79befbb8ac3c80be9 1100w, https://mintcdn.com/mintlify/2qBICQFhOKqkes42/images/assistant/search-domains-light.png?w=1650&fit=max&auto=format&n=2qBICQFhOKqkes42&q=85&s=64f378dcf125bc9fe48d5a916b45d7e4 1650w, https://mintcdn.com/mintlify/2qBICQFhOKqkes42/images/assistant/search-domains-light.png?w=2500&fit=max&auto=format&n=2qBICQFhOKqkes42&q=85&s=edeb2cc12e36a04f96ac085e59cbd419 2500w" />

  <img src="https://mintcdn.com/mintlify/2qBICQFhOKqkes42/images/assistant/search-domains-dark.png?fit=max&auto=format&n=2qBICQFhOKqkes42&q=85&s=ae032b581c467630c044b073b583dded" alt="The assistant search domains panel enabled in the dashboard. The assistant is configured to search the mintlify.com/pricing domain." className="hidden dark:block" data-og-width="838" width="838" data-og-height="626" height="626" data-path="images/assistant/search-domains-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/2qBICQFhOKqkes42/images/assistant/search-domains-dark.png?w=280&fit=max&auto=format&n=2qBICQFhOKqkes42&q=85&s=b3b4378d2925d1d0b7628111ceec659e 280w, https://mintcdn.com/mintlify/2qBICQFhOKqkes42/images/assistant/search-domains-dark.png?w=560&fit=max&auto=format&n=2qBICQFhOKqkes42&q=85&s=266a3ffe7fb2c18bc367cfd37b8a31bb 560w, https://mintcdn.com/mintlify/2qBICQFhOKqkes42/images/assistant/search-domains-dark.png?w=840&fit=max&auto=format&n=2qBICQFhOKqkes42&q=85&s=48585cc7e9b11d42382b470517bec6ed 840w, https://mintcdn.com/mintlify/2qBICQFhOKqkes42/images/assistant/search-domains-dark.png?w=1100&fit=max&auto=format&n=2qBICQFhOKqkes42&q=85&s=33b7800ff2eef66a1ff1671cad223468 1100w, https://mintcdn.com/mintlify/2qBICQFhOKqkes42/images/assistant/search-domains-dark.png?w=1650&fit=max&auto=format&n=2qBICQFhOKqkes42&q=85&s=1a6a7c6ce03629355444678429d355ed 1650w, https://mintcdn.com/mintlify/2qBICQFhOKqkes42/images/assistant/search-domains-dark.png?w=2500&fit=max&auto=format&n=2qBICQFhOKqkes42&q=85&s=d4dadaf805eed0a685e9bf088ba10edc 2500w" />
</Frame>

For more precise control over what the assistant can search, use filtering syntax.

* **Domain-level filtering**
  * `example.com`: Search only the `example.com` domain
  * `docs.example.com`: Search only the `docs.example.com` subdomain
  * `*.example.com`: Search all subdomains of `example.com`
* **Path-level filtering**
  * `docs.example.com/api`: Search all pages under the `/api` subpath
* **Multiple patterns**
  * Add multiple entries to target different sections of sites

### Add sample questions

Help your users begin conversations with the assistant by adding starter questions. Add commonly asked questions or questions about topics that you want your users to know about. Click **Ask AI** for recommended questions based on your documentation.

<Frame>
  <img src="https://mintcdn.com/mintlify/2qBICQFhOKqkes42/images/assistant/search-suggestions-light.png?fit=max&auto=format&n=2qBICQFhOKqkes42&q=85&s=f2e40f177d289259f24644e5f1372a7d" alt="The search suggestions panel in the dashboard with starter questions enabled and populated with three questions." className="block dark:hidden" data-og-width="1410" width="1410" data-og-height="752" height="752" data-path="images/assistant/search-suggestions-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/2qBICQFhOKqkes42/images/assistant/search-suggestions-light.png?w=280&fit=max&auto=format&n=2qBICQFhOKqkes42&q=85&s=9c8421dc725f3634d778850cb501c3a8 280w, https://mintcdn.com/mintlify/2qBICQFhOKqkes42/images/assistant/search-suggestions-light.png?w=560&fit=max&auto=format&n=2qBICQFhOKqkes42&q=85&s=bd39e45cd5439606a68457d6ab073d09 560w, https://mintcdn.com/mintlify/2qBICQFhOKqkes42/images/assistant/search-suggestions-light.png?w=840&fit=max&auto=format&n=2qBICQFhOKqkes42&q=85&s=7fbdf150d9fcf2cef49e34408350f570 840w, https://mintcdn.com/mintlify/2qBICQFhOKqkes42/images/assistant/search-suggestions-light.png?w=1100&fit=max&auto=format&n=2qBICQFhOKqkes42&q=85&s=33e4e778f2b8a4b0c33723203a395f80 1100w, https://mintcdn.com/mintlify/2qBICQFhOKqkes42/images/assistant/search-suggestions-light.png?w=1650&fit=max&auto=format&n=2qBICQFhOKqkes42&q=85&s=726d35b99d57a41f51d3e8b8c786320a 1650w, https://mintcdn.com/mintlify/2qBICQFhOKqkes42/images/assistant/search-suggestions-light.png?w=2500&fit=max&auto=format&n=2qBICQFhOKqkes42&q=85&s=5e243be2f7ef13bbb6860a4372563735 2500w" />

  <img src="https://mintcdn.com/mintlify/2qBICQFhOKqkes42/images/assistant/search-suggestions-dark.png?fit=max&auto=format&n=2qBICQFhOKqkes42&q=85&s=6a9bdfcc55dbe36c1fe30c877bcb414d" alt="The search suggestions panel in the dashboard with starter questions enabled and populated with three questions." className="hidden dark:block" data-og-width="1410" width="1410" data-og-height="752" height="752" data-path="images/assistant/search-suggestions-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/2qBICQFhOKqkes42/images/assistant/search-suggestions-dark.png?w=280&fit=max&auto=format&n=2qBICQFhOKqkes42&q=85&s=2b205e20377319941ee7deecab6ecbfa 280w, https://mintcdn.com/mintlify/2qBICQFhOKqkes42/images/assistant/search-suggestions-dark.png?w=560&fit=max&auto=format&n=2qBICQFhOKqkes42&q=85&s=1bdf10dec6e677086d9b4772b670c065 560w, https://mintcdn.com/mintlify/2qBICQFhOKqkes42/images/assistant/search-suggestions-dark.png?w=840&fit=max&auto=format&n=2qBICQFhOKqkes42&q=85&s=eb65c3cad03eb77ef752e7dae78f9087 840w, https://mintcdn.com/mintlify/2qBICQFhOKqkes42/images/assistant/search-suggestions-dark.png?w=1100&fit=max&auto=format&n=2qBICQFhOKqkes42&q=85&s=80989463643f3d709ada2914cbc4c32a 1100w, https://mintcdn.com/mintlify/2qBICQFhOKqkes42/images/assistant/search-suggestions-dark.png?w=1650&fit=max&auto=format&n=2qBICQFhOKqkes42&q=85&s=69e0804fe76e88d7edb0182b052b29da 1650w, https://mintcdn.com/mintlify/2qBICQFhOKqkes42/images/assistant/search-suggestions-dark.png?w=2500&fit=max&auto=format&n=2qBICQFhOKqkes42&q=85&s=1a017e24104bfe039bb13bd9f5307081 2500w" />
</Frame>

## Manage billing

The assistant uses tiered message allowances. A message is any user interaction with the assistant that receives a correct response. If you have unused messages, up to half of your message allowance can carry over to the next billing cycle. For example, if you have a 1,000 message allowance and you use 300 messages, 500 messages carry over to the next billing cycle giving you a total of 1,500 messages for the next billing cycle.

By default, the assistant allows overages. You can disable overages to avoid incurring additional costs for usage beyond your tier. If you reach your message allowance with overages disabled, the assistant is unavailable until your message allowance resets. If you allow overages, each message beyond your allowance incurs an overage charge, but occasional overages may be cheaper than upgrading to a higher tier depending on your usage.

### Change your assistant tier

Assistant tiers determine your monthly message allowance and pricing.

View and change your current tier on the [Billing tab](https://dashboard.mintlify.com/products/assistant/settings/billing) of the assistant page in your dashboard.

In the **Spending Controls** section, select your preferred tier from the dropdown menu.

**Upgrade your tier:**

* Your new message allowance is available immediately.
* You pay a prorated difference for the current billing cycle.

**Downgrade your tier:**

* Your message allowance updates immediately.
* Pricing changes take effect at the start of your next billing cycle.
* Unused messages from your current tier **do not** carry over.

### Allow overages

If you want to disallow overages, disable them in the **Billing Controls** section of the [Billing tab](https://dashboard.mintlify.com/products/assistant/settings/billing) of the assistant page in your dashboard.

### Set usage alerts

In the Billing Controls section, set usage alerts to receive an email when you reach a certain percentage of your message allowance.

## Connect apps

In the connect apps section, add the assistant to your [Discord](/ai/discord) server and [Slack](/ai/slack-bot) workspace to allow users to get answers from your documentation on those platforms.

## Assistant insights

Use assistant insights to understand how users interact with your documentation and identify improvement opportunities.

The [assistant page](https://dashboard.mintlify.com/products/assistant) shows usage trends for the month to date. View more detailed insights on the [analytics](/optimize/analytics#assistant) page.

## Make content AI ingestible

Structure your documentation to help the assistant provide accurate, relevant answers. Clear organization and comprehensive context benefit both human readers and AI understanding.

<Card title="Structure and organization">
  * Use semantic markup.
  * Write descriptive headings for sections.
  * Create a logical information hierarchy.
  * Use consistent formatting across your docs.
  * Include comprehensive metadata in page frontmatter.
  * Break up long blocks of text into shorter paragraphs.
</Card>

<Card title="Context">
  * Define specific terms and acronyms when first introduced.
  * Provide sufficient conceptual content about features and procedures.
  * Include examples and use cases.
  * Cross-reference related topics.
  * Add [hidden pages](/organize/hidden-pages) with additional context that users don't need, but the assistant can reference.
</Card>

## Use the assistant

Users have multiple ways to start a conversation with the assistant. Each method opens a chat panel on the right side of your docs. Users can ask any question and the assistant searches your documentation for an answer. If the assistant cannot retrieve relevant information, the assistant responds that it cannot answer the question.

Add the assistant as a bot to your [Slack workspace](/ai/slack-bot) or [Discord server](/ai/discord) so that your community can ask questions without leaving their preferred platform.

### UI placement

The assistant appears in two locations: as a button next to the search bar and as a bar at the bottom of the page.

<Columns cols={2}>
  <Frame caption="Assistant button next to the search bar.">
    <img
      src="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-light.png?fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=716582bc54eaea73cb53d26b36a74fb4"
      className="block dark:hidden"
      style={{
  width: '268px',
  height: 'auto',
}}
      alt="Search bar and assistant button in light mode."
      data-og-width="1806"
      width="1806"
      data-og-height="322"
      height="322"
      data-path="images/assistant/assistant-button-light.png"
      data-optimize="true"
      data-opv="3"
      srcset="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-light.png?w=280&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=9ae2bace996e8301def4d07a3151764b 280w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-light.png?w=560&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=70cde876f7f7ee59c07594108203c93c 560w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-light.png?w=840&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=95f1633b5e41b8b279a8923f7a1fa075 840w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-light.png?w=1100&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=11b8f8f14bdeb252e9ba07d622834146 1100w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-light.png?w=1650&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=b2c08d4d0573c75a3493e6dfd282dd56 1650w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-light.png?w=2500&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=fc092ff8b664ce5842067bca8bd531c7 2500w"
    />

    <img
      src="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-dark.png?fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=34096a771f492853e59eef654567b081"
      className="hidden dark:block"
      style={{
  width: '268px',
  height: 'auto',
}}
      alt="Search bar and assistant button in dark mode."
      data-og-width="1806"
      width="1806"
      data-og-height="324"
      height="324"
      data-path="images/assistant/assistant-button-dark.png"
      data-optimize="true"
      data-opv="3"
      srcset="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-dark.png?w=280&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=1b8226b14933399c53d7975e02ad7d9d 280w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-dark.png?w=560&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=400dff40f5e394fd2d85a52066592e26 560w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-dark.png?w=840&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=00d387ddc8a0336bbac7e21b1130dfa1 840w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-dark.png?w=1100&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=860463b82aa2db420d87af6138c61e66 1100w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-dark.png?w=1650&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=0c15a237b868f23fad34f7838bdc3579 1650w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/assistant/assistant-button-dark.png?w=2500&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=1e88586f53b4f6f07b8336a77f0f940f 2500w"
    />
  </Frame>

  <Frame caption="Assistant button at the bottom of the page.">
    <img
      src="https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/assistant-bar-light.png?fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=920b62e97a4a24a5aa7a29d9306b3762"
      className="block dark:hidden"
      style={{
  width: '268px',
  height: 'auto',
}}
      alt="Assistant bar in light mode."
      data-og-width="656"
      width="656"
      data-og-height="112"
      height="112"
      data-path="images/assistant/assistant-bar-light.png"
      data-optimize="true"
      data-opv="3"
      srcset="https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/assistant-bar-light.png?w=280&fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=b592e20464907a8f591759fc628faa2c 280w, https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/assistant-bar-light.png?w=560&fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=00a3cbb30deeab06e985fd36ec070006 560w, https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/assistant-bar-light.png?w=840&fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=8c78e1f6c7da55ad7a9d9110bbbe431c 840w, https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/assistant-bar-light.png?w=1100&fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=879307a77a65cecd8d35d0a73401f8eb 1100w, https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/assistant-bar-light.png?w=1650&fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=3a16dd9e8cd05db89cf1b12fc495be03 1650w, https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/assistant-bar-light.png?w=2500&fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=52c17d0e07220fd4bec99086f0215bdb 2500w"
    />

    <img
      src="https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/assistant-bar-dark.png?fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=f597be3a1c8a95a8a72aaae4f799981f"
      className="hidden dark:block"
      style={{
  width: '268px',
  height: 'auto',
}}
      alt="Assistant bar in dark mode."
      data-og-width="656"
      width="656"
      data-og-height="112"
      height="112"
      data-path="images/assistant/assistant-bar-dark.png"
      data-optimize="true"
      data-opv="3"
      srcset="https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/assistant-bar-dark.png?w=280&fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=aff4afdb4d4339de3cf7c2acf2e1b776 280w, https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/assistant-bar-dark.png?w=560&fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=7fd24008342893062a3db37999d2e6ba 560w, https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/assistant-bar-dark.png?w=840&fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=be5b3af4d709c1b076d241056a11abeb 840w, https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/assistant-bar-dark.png?w=1100&fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=286cefd2326f70eb6e234d898cf1aa2b 1100w, https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/assistant-bar-dark.png?w=1650&fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=cdaa4b744b73ac71837bc70ef9f0a08e 1650w, https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/assistant-bar-dark.png?w=2500&fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=b59c7dbc8ae09c574aac03c354a2c62c 2500w"
    />
  </Frame>
</Columns>

### Keyboard shortcut

Open the assistant chat panel with the keyboard shortcut <kbd>Command</kbd> + <kbd>I</kbd> on macOS and <kbd>Ctrl</kbd> + <kbd>I</kbd> on Windows.

### Highlight text

Highlight text on a page and click the **Add to assistant** pop up button to open the assistant chat panel and add the highlighted text as context. You can add multiple text snippets or code blocks to the assistant's context.

<Frame>
  <img src="https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/highlight-light.png?fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=13c93b72e4f6b21800e31a55f85c3690" alt="The Add to assistant button above highlighted text in light mode." className="block dark:hidden" data-og-width="786" width="786" data-og-height="236" height="236" data-path="images/assistant/highlight-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/highlight-light.png?w=280&fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=f2081346acaa6ea128feaff35c2e2ba4 280w, https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/highlight-light.png?w=560&fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=b5cd9a1656a14fc6e720e5874194179e 560w, https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/highlight-light.png?w=840&fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=86caed0801dc62579653d75c0df5d928 840w, https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/highlight-light.png?w=1100&fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=ac1ae0534c50d1857ec10f49b998e93a 1100w, https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/highlight-light.png?w=1650&fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=f3e69965c56a8458b3568a2e2dcbc2f9 1650w, https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/highlight-light.png?w=2500&fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=13eae222f45b05babe4c7cc36d26e20b 2500w" />

  <img src="https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/highlight-dark.png?fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=73ef7699810025a73fce4dc125fea683" alt="The Add to assistant button above highlighted text in dark mode." className="hidden dark:block" data-og-width="786" width="786" data-og-height="236" height="236" data-path="images/assistant/highlight-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/highlight-dark.png?w=280&fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=c4f4705666cbc698e53bca0c3899cd43 280w, https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/highlight-dark.png?w=560&fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=859920be853135da0ac0efee5ccb3b0a 560w, https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/highlight-dark.png?w=840&fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=0fd93a0fe91d0146ecab8e56f8c204c5 840w, https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/highlight-dark.png?w=1100&fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=c0a4a49fb334eeaa213ebc70448e7663 1100w, https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/highlight-dark.png?w=1650&fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=5aed16d9f8682b297610e4510486fa2a 1650w, https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/highlight-dark.png?w=2500&fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=46c40ae732ee7962a53bb16a6610b1ce 2500w" />
</Frame>

### Code blocks

Click the **Ask AI** button in a code block to open the assistant chat panel and add the code block as context. You can add multiple code blocks or text snippets to the assistant's context.

<Frame>
  <img src="https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/code-block-light.png?fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=d9b3cbecca1416291915ded538315d05" alt="The Ask AI button in a code block in light mode." className="block dark:hidden" data-og-width="1190" width="1190" data-og-height="408" height="408" data-path="images/assistant/code-block-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/code-block-light.png?w=280&fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=e2052ab50a100dacd4e09357f0688f00 280w, https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/code-block-light.png?w=560&fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=3222cf3923f04541d4b76136e02254df 560w, https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/code-block-light.png?w=840&fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=050cf85c21d504ac1b85bcd82275567b 840w, https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/code-block-light.png?w=1100&fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=fdac44c8dad6ee7b376db82043f1614c 1100w, https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/code-block-light.png?w=1650&fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=f963a55e201b42a47948cfad4fcb1ce2 1650w, https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/code-block-light.png?w=2500&fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=4f3ef5e4c30052d5b722afac6fc30d75 2500w" />

  <img src="https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/code-block-dark.png?fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=1e5ffae5032208ff67d2a725b48fdafd" alt="The Ask AI button in a code block in dark mode." className="hidden dark:block" data-og-width="1190" width="1190" data-og-height="408" height="408" data-path="images/assistant/code-block-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/code-block-dark.png?w=280&fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=1644b0243c58cf9e10a3bab748a2b7c5 280w, https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/code-block-dark.png?w=560&fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=ced0907d9c1f6be554937009fc572635 560w, https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/code-block-dark.png?w=840&fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=348da2c5424198950de1329c7a336824 840w, https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/code-block-dark.png?w=1100&fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=da663cc1507c24d98e3f238a35241ee4 1100w, https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/code-block-dark.png?w=1650&fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=507ea9c7461f37d047d4b12cb18d7df2 1650w, https://mintcdn.com/mintlify/Gt7y__uLw46fbQ_E/images/assistant/code-block-dark.png?w=2500&fit=max&auto=format&n=Gt7y__uLw46fbQ_E&q=85&s=98feb18c32398423e783865e6c7a8120 2500w" />
</Frame>

### URLs

Open the assistant with a URL query parameter to create deep links that guide users to specific information or share assistant conversations with pre-filled questions.

* **Open the assistant**: Append `?assistant=open` to open the assistant chat panel when the page loads.
  * Example: [https://mintlify.com/docs?assistant=open](https://mintlify.com/docs?assistant=open)
* **Open with a pre-filled query**: Append `?assistant=YOUR_QUERY` to open the assistant and automatically submit a question.
  * Example: [https://mintlify.com/docs?assistant=explain webhooks](https://mintlify.com/docs?assistant=explain%20webhooks)

## Troubleshooting

<Accordion title="Assistant chat bar not visible">
  If the assistant UI is not visible in specific browsers, you may need to submit a false positive report to [EasyList](https://easylist.to). Browsers that use the EasyList Cookies List like Brave and Comet sometimes block the assistant or other UI elements. The EasyList Cookies List includes a domain-specific rule that hides fixed elements on certain domains to block cookie banners. This rule inadvertently affects legitimate UI components.

  Submit a false positive report to [EasyList](https://github.com/easylist/easylist) to request removal of the rule. This resolves the issue for all users once the filter list updates.
</Accordion>
