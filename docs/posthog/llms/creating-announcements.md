# Source: https://posthog.com/docs/product-tours/creating-announcements.md

# Make an announcement - Docs

**Product tours is in private alpha**

Product Tours is currently in private alpha. [Share your thoughts](https://app.posthog.com/external_surveys/019af5f5-a50e-0000-b10f-e8c30c0b73a0) and we'll reach out with early access.

**Currently only available on the web. Requires `posthog-js` >= v1.324.0.**

Announcements are single-step messages for when you don't need a full multi-step tour. Buttons can open links or trigger a product tour, making announcements a great entry point for onboarding flows.

## Modal announcements

Popups for important messages like feature launches, changelogs, or welcome messages. Modals can be positioned anywhere on screen and support rich content with buttons.

![Modal announcement example](https://res.cloudinary.com/dmukukwp6/image/upload/Screenshot_2026_01_16_at_12_44_39_PM_b1e4fb4ce4.png)

To create one:

1.  Go to [Product tours](https://app.posthog.com/product_tours)
2.  Click **New** and select **Announcement**
3.  Enter a name and click **Create**

## Banner announcements

Top-of-page alerts for less intrusive messages like promotions or maintenance notices. Banners can be sticky (stay visible while scrolling) or static.

![Banner announcement example](https://res.cloudinary.com/dmukukwp6/image/upload/Screenshot_2026_01_16_at_12_44_14_PM_1614e763bf.png)

To create one:

1.  Go to [Product tours](https://app.posthog.com/product_tours)
2.  Click **New** and select **Banner**
3.  Enter a name and click **Create**

### Banner settings

Banners have additional configuration options:

-   **Position**: Choose between sticky (stays visible while scrolling), static (scrolls with content), or custom (inject into a specific container element using a CSS selector).
-   **Click action**: Set what happens when users click the banner – open a link, trigger another product tour, or do nothing.
-   **Animate in**: When enabled (default), the banner slides in from the top with a brief animation. This is useful in preventing an abrupt layout shift when the banner loads.

## Targeting

Announcements use the same targeting options as product tours. See [Targeting](/docs/product-tours/targeting.md) for details.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better