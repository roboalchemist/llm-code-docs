# Source: https://posthog.com/docs/toolbar/heatmaps.md

# Heatmaps - Docs

Heatmaps shows you how users are interacting with elements on your website or app.

To start, ensure you enable the capturing of heatmap data in [your project settings](https://us.posthog.com/settings/project-heatmaps#heatmaps) or with the `enable_heatmaps` key in the [JavaScript Web SDK initialization config](/docs/libraries/js/config.md).

Heatmap data is captured along with other events, so it doesn't contribute to your bill, but the clickmap requires [autocapture](/docs/product-analytics/autocapture.md) and the scrollmap requires pageleave events.

You can view heatmaps via the PostHog toolbar, or using the in-app Heatmap tool that's currently an opt-in beta.

## Viewing heatmaps using the toolbar

To view your heatmaps, click the heatmap icon on the toolbar.

There are three kinds of heatmaps in the toolbar:

1.  **Heatmap:** which captures mouse movements, clicks, dead clicks, and rageclicks and shows you a heatmap of these interactions.

2.  **Scrollmap:** which shows you how far users are scrolling down your page.

3.  **Clickmap:** AKA the OG heatmap. It uses autocapture to show you the elements users are clicking on your website.

## Viewing heatmaps in PostHog (beta)

You can also view heatmaps directly in the PostHog. This method is currently in beta and provides almost the same functionality as the toolbar.

Add IPs to Firewall/WAF allowlists (recommended)

For certain features like [heatmaps](/docs/toolbar/heatmaps.md), your Web Application Firewall (WAF) may be blocking PostHog’s requests to your site. Add these IP addresses to your WAF allowlist or rules to let PostHog access your site.

**EU**: `3.75.65.221`, `18.197.246.42`, `3.120.223.253`

**US**: `44.205.89.55`, `52.4.194.122`, `44.208.188.173`

These are public, stable IPs used by PostHog services (e.g., Celery tasks for snapshots).

To view heatmaps in the app:

1.  Enable the [**In-App Heatmaps** feature preview](https://app.posthog.com/settings/user-feature-previews#heatmaps-ui)
2.  Go to the [Heatmaps section in PostHog](https://us.posthog.com/heatmaps)
3.  Type the URL of your website in the **Display URL** field
4.  Optional: Use wildcard URL matching for the **Heatmap data URL** to combine data from similar pages

The in-app heatmap viewer provides the same three types of heatmaps as the toolbar:

1.  **Heatmap:** Visual representation of mouse movements, clicks, dead clicks, and rageclicks
2.  **Scrollmap:** Shows how far users scroll down your page
3.  **Clickmap:** Displays click counts on specific elements with rageclick indicators

All configuration options available in the toolbar (aggregation, viewport accuracy, color palette, fixed positioning) are also available in the in-app version.

You can also generate a screenshot for heatmaps directly from [Session Replay](/docs/session-replay/how-to-watch-recordings.md) by clicking the **View heatmap** button above a recording.

## Heatmaps

The heatmap shows where on the page users are clicking, dead clicking, rageclicking, or moving their mouse. Unlike the clickmap, the user doesn't need to click on a clickable element, so you can see where users are trying to click.

There are multiple options to configure your heatmap.

### Aggregation

The heatmap can show a count of events, or of unique users. The default is to show the count of events.

The unique users count is based on the user's distinct ID, so if a user is using multiple devices or browsers, they are counted as multiple users. This is so that the heatmap can be much faster to load.

The clickmap can be used when you want exact counts.

### Viewport accuracy

You can set a tolerance for the viewport accuracy.

This enables you to view the heatmap on a different sized screen from your users. You can reduce viewport accuracy to include events from different sized screens.

This means that you get more data but the position might not be as accurate.

### Color palette

The default palette for the heatmap is a gradient from red to green. This won't be visible for all users or against all site color themes.

You can change the color palette to a different gradient or to a single color.

### Fixed positioning

Some clicks are on elements that don't move when the page scrolls.

Our JavaScript SDK attempts to detect fixed elements, such as headers or modals, and show those heatmap areas, ignoring the scroll value.

You can change fixed positioning so these clicks move when scrolled or hide them entirely.

## Scrollmaps

The scrollmap uses data from pageview and pageleave events to show how far down the page users are scrolling.

## Clickmaps

With the clickmap, clickable elements on your website will have a red overlay with numbers on them.

Here's an example of our website with the heatmap enabled:

Each number in the top right box of each element represents the total number of clicks in the last 7 days.

The number in the top left of the element is the number of rageclicks.

A rageclick is collected when a user clicks on a static element more than three times in a one-second window.

Numbers at the bottom or top of the screen indicate that there are more elements that are not currently being displayed on the page.

### How to create an action from the clickmap

With the clickmap enabled, click on any element. This opens a menu where you can then create an [action](/docs/data/actions.md) from it.

### Loading more data

If you have many events, you may need to load more data to see everything on the clickmap.

To do this, click on the load more button in the clickmap menu.

### Matching links by their target URL

By default, the toolbar matches clicks using the elements on the page, and not by their target URLs (i.e., `href` attribute).

This is fine for most scenarios where you have static elements with the same target URL.

However, this may not be ideal for dynamic lists that have different target URLs depending on the underlying data.

For example, consider the following screenshot of a list of elements for "Newly seen persons" from the PostHog app:

The "Newly seen persons" shows the most recent list of persons using the app and is constantly being updated as new users use the app.

In the clickmap, we see 106 clicks for the **first element**.

This doesn't mean that the this specific person in the list received 106 clicks, but rather that the first element in the list received 106 clicks, regardless of which person was shown.

If we were interested in the number of clicks each specific person in the list received (regardless of which position they appeared in), then we can turn on "Match links by their target URL" in the clickmap menu.

This matches clicks to elements based on their target URLs.

For example, if we enable this for our previous example, we see much fewer clicks.

This is because we are now seeing clicks on each specific user:

## Combining maps from similar pages using wildcards

If you have similar pages that have dynamic content based on an identifier in the URL (e.g., product pages on an ecommerce site), you can combine their heatmap data using wildcards `*` in the heatmap menu.

For example, if the product pages on an ecommerce site use a URL format of `https://yourwebsite.com/products/product-id`, you can use the wildcard URL `https://yourwebsite.com/products/*` to display a combined heatmap from all the product pages.

## Troubleshooting

### Heatmap is captured, but site is not showing

If you're viewing heatmaps [in-app](https://us.posthog.com/heatmaps) and the heatmap appears over a blank page, your site may be blocking it from being displayed in an `<iframe>`.

In app, PostHog overlays the heatmap over your site in an iframe. You can allow PostHog to place your site in an `<iframe>` by updating your `Content-Security-Policy` header.

| Region | Content Security Policy |
| --- | --- |
| US | Content-Security-Policy: frame-ancestors 'self' https://us.posthog.com; |
| EU | Content-Security-Policy: frame-ancestors 'self' https://eu.posthog.com; |

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better