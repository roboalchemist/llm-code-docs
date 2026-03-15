# Source: https://posthog.com/docs/product-tours/button-actions.md

# Button actions - Docs

**Product tours is in private alpha**

Product Tours is currently in private alpha. [Share your thoughts](https://app.posthog.com/external_surveys/019af5f5-a50e-0000-b10f-e8c30c0b73a0) and we'll reach out with early access.

**Currently only available on the web. Requires `posthog-js` >= v1.324.0.**

Each Product Tour step (or modal announcement) has a primary button and, optionally, a secondary button. Toggle on **custom buttons** in the Product Tour editor to configure your steps with these actions:

## Next step

Default primary button action. Moves your tour to the next step. On the last step, this is labeled **Complete tour** and triggers the `product tour completed` event.

*Not available for announcements.*

## Previous step

Default secondary button behavior - moves your tour to the previous step.

**Note:** if your tour causes users to navigate to another page, this action **will not navigate them back.** In these cases, we recommend disabling the secondary button, or swapping to a different action.

*Not available for announcements.*

## Start tour

Ends the current tour and starts another one. This is great for triggering product tours from [announcements](/docs/product-tours/creating-announcements.md)!

## Open link

Opens a given link in a new tab.

## Dismiss

Dismisses the current tour or announcement. Triggers the `product tour dismissed` event but not the `product tour completed` event.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better