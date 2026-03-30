# Source: https://posthog.com/docs/surveys/viewing-results.md

# Viewing survey results - Docs

Survey results can be viewed in two places:

1.  On the survey page, in the "Results" tab.
2.  By creating your own [insights](/docs/product-analytics/insights.md).

## 1\. On the survey page

You can view your results by selecting your survey from the [surveys tab](https://app.posthog.com/surveys). You'll see data on:

-   How many users have seen the survey.
-   How many users have dismissed the survey.
-   Responses.

Depending your [question type](/docs/surveys/creating-surveys.md#question-type), you may also see charts with your responses.

For rating and multiple choice questions, you can click on any bar in the chart to filter responses by that answer. For rating questions, a single click filters by that score. For multiple choice questions, click once to select a choice, then click again to confirm the filter. Click an active filter to clear it, or click a different bar to switch.

For rating questions (including NPS), the trend charts include an **Open as new insight** button. Click it to save the chart as a new insight, which you can then add to a [dashboard](/docs/product-analytics/dashboards.md).

Each question card also includes a **Copy response key** button. This copies the question's response key (e.g., `$survey_response_{question_id}`) to your clipboard. You can use this key when building custom [insights](/docs/product-analytics/insights.md) or setting up [destinations](/docs/surveys/destinations.md) like Slack notifications.

![Sample survey results](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/surveys/survey-results-sample-light-mode.png)![Sample survey results](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/surveys/survey-results-sample-dark-mode.png)

## 2\. Creating your own insights

To create insights from survey results, navigate to the [insights tab](https://app.posthog.com/insights) and click on `New insights` button.

There are four survey-related events you can create insights from:

1.  `survey shown` - fires when a survey is displayed to a user
2.  `survey sent` - fires when a user responds to a question
3.  `survey dismissed` - fires when a user explicitly closes the survey
4.  `survey abandoned` - (for surveys with partial completion enabled) fires when a user navigates away from the page before completing the survey

When creating an insight, select any of these events. To see data for a specific survey, create a filter using the `Survey ID` or `Survey Name` properties.

Depending on your [question type](/docs/surveys/creating-surveys.md#question-type), you may also find it helpful to breakdown results by the response.

**You can do that by using the built-in SQL function `getSurveyResponse(question_index, question_id, is_multiple_choice)`**.

-   `question_index` is the 0-based position of the question in the survey. So the first question has an index of 0, the second has an index of 1, etc.
-   `question_id` is the ID of the question. Optional - use if if not all responses are being shown with only the index.
-   `is_multiple_choice` is a boolean that is `true` if the question is a multiple choice question, and `false` otherwise. Optional, only needed for multiple choice questions.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better