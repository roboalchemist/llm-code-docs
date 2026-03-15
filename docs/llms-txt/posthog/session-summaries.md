# Source: https://posthog.com/docs/posthog-ai/session-summaries.md

# Session replay summaries with PostHog AI - Docs

It's hard to find time to watch all your session recordings, but you don't want to miss out on the insights. PostHog AI can summarize your recordings for you, identifying patterns, errors, and identify key summaries for you to review.

## Summarizing session replay recordings

In the [in-app chat](/docs/posthog-ai/platform-and-chat-ui.md#in-app-chat), you can ask PostHog AI to summarize your session recordings. PostHog AI will pick up on the filters you've applied to the session recordings and use them to summarize the recordings.

PostHog AI will categorize the recordings by behavior patterns and generate a summary report for you to review. You can always ask PostHog AI more questions about the session recordings, and to identify specific recordings for you to review.

While summarizing, PostHog AI displays real-time progress so you can track what's happening. You'll see which phase the summarization is in (fetching data, watching sessions, searching for patterns, or building the report), a progress bar with per-session status, and an ETA countdown during the watching phase.

PostHog AI summarizes your session recordings for you

## Searching for specific recordings

You can also ask PostHog AI to search for specific recordings. For example, you can ask PostHog AI to find all the recordings where a user rage clicked or used the navigation menu.

Start by clicking the icon next to the session recording filters.

PostHog AI searches for specific replays for you

## Summarize session replays in Experiments

You can also summarize session replays directly from the [Experiments](/docs/experiments.md) interface. This helps you understand how users in different experiment variants behave.

To use this feature:

1.  Go to an experiment that has started and has results
2.  Click the **Summarize session replays** button
3.  PostHog AI opens and automatically analyzes user behavior patterns from session replays across your experiment variants

PostHog AI categorizes recordings by variant and identifies behavioral differences, helping you understand not just *what* happened in your experiment, but *why* users responded differently to each variant.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better