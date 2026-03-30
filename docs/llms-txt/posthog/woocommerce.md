# Source: https://posthog.com/docs/libraries/woocommerce.md

# How to set up WooCommerce analytics with PostHog - Docs

Getting traffic, usage, and user behavior data about your WooCommerce site is simple with PostHog. Once set up, PostHog gives you the tools to view [session replays](/docs/session-replay.md) to understand customer behavior, use [experiments](/docs/experiments.md) to improve checkout flows, and run [CSAT surveys](/templates/csat-survey.md) to measure customer experience.

## How to add PostHog to your WooCommerce site

After setting up your WooCommerce site, the easiest way to set up PostHog is to install the free [Insert Headers and Footers](https://wordpress.com/plugins/insert-headers-and-footers) plugin by WPCode.

After doing this, go into the **Code Snippets** section and add a new snippet. Once you're here, get your PostHog snippet with your project token and instance address from [your project settings](https://us.posthog.com/project/settings#snippet). Paste it into the code editor, press **Save**, and activate it.

PostHog will now be capturing pageviews, button clicks, and more. You can also enable and use features like session replays, A/B testing, and surveys.

> Depending on how you host your WooCommerce site, you may also be able to edit the theme function or header file which we detail in our [WordPress docs](/docs/libraries/wordpress.md).

## Tracking conversions in WooCommerce

One of the most important metrics for an ecommerce site is conversion, like adding an item to your cart and completing the checkout.

PostHog has multiple tools to help you track and measure conversions. To do this without code, you can create an action using the toolbar. To do this:

1.  Go to the [toolbar tab](https://us.posthog.com/toolbar) in PostHog, add your domain as an authorized URL, and click **Launch**.
2.  Go to the page on your WooCommerce site with your conversion button, click the lightning icon, then click **New action,** and then the conversion button.
3.  Fill out the details for your action like name and matching, and then click **Create action**. This creates an action you can see in the [data management tab](https://us.posthog.com/data-management/actions) in PostHog.

Once this action is created, you can get an overview of conversions by going to the [web analytics dashboard](https://us.posthog.com/web), clicking **Add conversion goal**, and then choosing your action. This shows you your total conversions, unique conversions, and conversion rate.

![PostHog web analytics dashboard](https://res.cloudinary.com/dmukukwp6/image/upload/Clean_Shot_2024_11_05_at_10_26_11_2x_781d657e6d.png)![PostHog web analytics dashboard](https://res.cloudinary.com/dmukukwp6/image/upload/Clean_Shot_2024_11_05_at_10_25_27_2x_b9618d4a08.png)

To dive deeper into your conversions, you can use [funnels](/docs/product-analytics/funnels.md) to add multiple steps, break down by properties, and see timings.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better