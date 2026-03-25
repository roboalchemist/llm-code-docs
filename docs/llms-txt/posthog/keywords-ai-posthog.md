# Source: https://posthog.com/docs/llm-analytics/integrations/keywords-ai-posthog.md

# Integrating with Keywords AI - Docs

You can integrate with [Keywords AI](https://www.keywordsai.co) and bring data into PostHog for analysis. Additionally, we offer a dashboard template to help you quickly get insights into your LLM product.

## How to install the integration

1.  Sign up for [Keywords AI](https://keywordsai.co/) and add it to your app.
2.  Copy PostHog host and project token from your [PostHog project settings](https://us.posthog.com/settings/project).
3.  In your Keywords AI requests in your code, add the following parameters:

PostHog AI

```
{
// other parameters
"posthog_integration": {
        "posthog_api_key": "<ph_project_token>",
        "posthog_base_url": "https://us.i.posthog.com"
    }
}
```

Keywords AI will now send events to PostHog under the name `keywords_ai_api_logging`. They send events as soon as they're available.

## Using the Keywords AI dashboard template

Once you've installed the integration, our Keywords AI [dashboard template](/docs/product-analytics/dashboards.md) helps you quickly set up relevant insights. You can see an [example dashboard here](https://us.posthog.com/shared/p1AymhS7EEm97nZOGA8nWmsdshhzYA).

To create your own dashboard from a template:

1.  Go the [dashboard tab](https://us.posthog.com/dashboard) in PostHog.
2.  Click the **New dashboard** button in the top right.
3.  Select **LLM metrics – Keywords AI** from the list of templates.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better