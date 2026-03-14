# Source: https://docs.snowflake.com/en/release-notes/2025/other/2025-08-07-cortex-aisql-ai-transcribe.md

# Aug 07, 2025: Cortex AI_TRANSCRIBE (*Preview*)

The AI_TRANSCRIBE function, now in available in preview in [select regions](../../../user-guide/snowflake-cortex/aisql.md),
provides SQL-native speech-to-text AI processing at scale. With AI_TRANSCRIBE, you can extract insights from customer
care interactions, healthcare consultations, and business meeting recordings. Files can be processed directly from
object storage, avoiding data movement, and no infrastructure management is required, so you can get started right away.

AI_TRANSCRIBE lets you:

* Perform simple text transcription for basic needs, extract word-level timestamps for precise navigation, or
  automatically identify speakers for multi-speaker content analysis.
* Build comprehensive customer intelligence pipelines that transcribe support calls and combine with AI_SENTIMENT for
  instant sentiment analysis.
* Streamline compliance and quality monitoring by transcribing customer service calls with speaker identification,
  enabling automated labeling of issues using AI_CLASSIFY.
* Generate executive meeting summaries that automatically identify key speakers, extract decision points, and create
  structured reports from board meetings or stakeholder calls using AI_TRANSCRIBE and AI_AGG.
* Build multilingual content processing workflows that transcribe international customer interactions and combine with
  other AI Functions for comprehensive global customer experience analysis.

For more information, see [Cortex AI Functions: Audio](../../../user-guide/snowflake-cortex/ai-audio.md) and [AI_TRANSCRIBE](../../../sql-reference/functions/ai_transcribe.md).
