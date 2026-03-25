# Source: https://docs.snowflake.com/en/release-notes/2026/other/2026-01-22-ai-filter-ga.md

# Jan 22, 2026: AI_FILTER for filtering with natural language predicates (*General availability*)

The AI_FILTER function, now generally available, provides a new AI-powered semantic filtering capability that lets you express complex filters in plain, natural language. No rigid keywords, regex, or brittle rules are required.

With AI_FILTER, business users and data teams can filter data based on meaning and intent, not just text matches. This
unlocks faster analysis and more intuitive queries, and dramatically reduces the effort required to translate business
questions into SQL logic.

AI_FILTER use cases include:

* Customer feedback analysis: Filter reviews, surveys, or support tickets by sentiment or intent (for example,
  “customers who were frustrated with delivery delays”).
* Trust & safety and moderation: Identify content that violates policies or expresses risky behavior without enumerating
  endless keywords.
* Sales and CRM insights: Surface deal notes or call transcripts that indicate buying intent, objections, or churn risk.
* Marketing and brand monitoring: Find mentions that express positive or negative brand perception, campaign reactions,
  or competitor comparisons.
* Operational review and quality analysis: Filter internal reports or incident notes based on root cause, severity, or
  outcome described in natural language.

For example, the following query filters the REVIEWS table to include only reviews where the reviewer enjoyed the restaurant:

```sqlexample
SELECT * FROM reviews
   WHERE AI_FILTER(PROMPT('The reviewer enjoyed the restaurant: {0}', review));
```

For more information, see [AI_FILTER](../../../sql-reference/functions/ai_filter.md).
