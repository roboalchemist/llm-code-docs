# Source: https://posthog.com/docs/product-tours/managing-tours.md

# Launch and manage tours - Docs

**Product tours is in private alpha**

Product Tours is currently in private alpha. [Share your thoughts](https://app.posthog.com/external_surveys/019af5f5-a50e-0000-b10f-e8c30c0b73a0) and we'll reach out with early access.

**Currently only available on the web. Requires `posthog-js` >= v1.324.0.**

## Launching a tour

Tours won't show until you launch them, regardless of targeting method.

1.  Go to your tour in [Product tours](https://app.posthog.com/product_tours)
2.  Click **Launch**

### Auto-launch

When auto-launch is enabled, the tour automatically shows when a user meets all targeting conditions.

If auto-launch is disabled, the tour won't show automatically. This is useful if you want to trigger tours programmatically or from other tours.

## Stopping a tour

To stop a running tour, click **Stop**. The tour stops showing immediately.

## Editing live tours

You can edit a running tour. Changes auto-save to a draft as you work – they aren't published until you click **Save**. Click **Cancel** to discard your draft.

If you close your browser with unpublished changes, a banner appears on the tour view page with options to **Continue editing** or **Discard** the draft.

You can edit:

-   Content changes (text, images, buttons)
-   Targeting changes (URL, user filters)
-   Appearance changes (colors, positioning)

## Duplicating tours

Duplicate any tour to create a copy with the same content, targeting, and settings. The duplicate is created as a draft.

1.  Go to your tour in [Product tours](https://app.posthog.com/product_tours)
2.  Click the **...** menu and select **Duplicate**

## Archiving tours

Archive a tour when you no longer need it. Archived tours:

-   Stop showing to users immediately
-   Remain in the archived tab for reference
-   Keep their analytics data
-   Can be restored if needed

Running tours must be stopped before they can be archived.

## Deleting tours

Delete permanently removes a tour and cannot be undone. Stop running tours before deleting them.

> **Note:** Tour interaction events in your data are not affected by deletion. Only the tour configuration is removed.

## Restoring archived tours

Restore an archived tour to make it active again. Click **Restore** in the tour's **...** menu. After restoring, you can launch the tour again.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better