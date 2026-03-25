# Source: https://posthog.com/docs/llm-analytics/integrations/traceloop-posthog.md

# Integrating with Traceloop - Docs

You can integrate with [Traceloop](https://www.traceloop.com/) and bring data into PostHog for analysis. Additionally, we offer a dashboard template to help you quickly get insights into your LLM product.

## How to install the integration

1.  Sign up for [Traceloop](https://www.traceloop.com/) and add it to your app.
2.  Go to the [integrations page](https://app.traceloop.com/settings/integrations) in your Traceloop dashboard and click on the PostHog card.

3.  Enter in your PostHog host and project token (you can find these in your [PostHog project settings](https://us.posthog.com/settings/project)).
4.  Select the environment you want to connect to PostHog and click **Enable**.

Traceloop will now send events to PostHog under the name `traceloop span`.

## Using the Traceloop dashboard template

Once you've installed the integration, our Traceloop [dashboard template](/docs/product-analytics/dashboards.md) helps you quickly set up relevant insights. You can see an [example dashboard here](https://us.posthog.com/shared/tpX9kUd5BbGkdjxQE8YhCskNuYA7Jw).

To create your own dashboard from a template:

1.  Go the [dashboard tab](https://us.posthog.com/dashboard) in PostHog.
2.  Click the **New dashboard** button in the top right.
3.  Select **LLM metrics – Traceloop** from the list of templates.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better