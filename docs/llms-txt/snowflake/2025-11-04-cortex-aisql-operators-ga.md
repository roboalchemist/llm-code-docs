# Source: https://docs.snowflake.com/en/release-notes/2025/other/2025-11-04-cortex-aisql-operators-ga.md

# Nov 04, 2025: Cortex AI Functions (*General availability*)

Snowflake announces the general availability of Cortex AI Functions, delivering production-ready AI capabilities within the
Snowflake SQL engine.

Cortex Functions give you the ability to unify structured and unstructured analytics within a single platform and
accelerate intelligent application development. With AI Functions, you can build scalable, multimodal AI pipelines
that run entirely inside Snowflake, enabling text, image, audio, and video intelligence without external services or
data movement.

Four Cortex AI Functions, previously available in preview, become generally available today:

* [AI_CLASSIFY](../../../sql-reference/functions/ai_classify.md): Classifies a text or image input into a single or multiple
  user-defined categories based on plain-language category definitions.
* [AI_TRANSCRIBE](../../../sql-reference/functions/ai_transcribe.md): Transcribes audio and video files stored in a stage,
  extracting text, timestamps, and speaker information. See the separate [AI_TRANSCRIBE announcement](2025-11-04-cortex-ai-transcribe-ga.md) to see what’s new.
* [AI_EMBED](../../../sql-reference/functions/ai_embed.md): Generates an embedding vector for a text or image input, which
  can be used for similarity search, clustering, and classification tasks.
* [AI_SIMILARITY](../../../sql-reference/functions/ai_similarity.md): Calculates the embedding similarity between two inputs
  without needing to explicitly create the embedding vectors.

These functions join three Cortex AI Functions that were already generally available:

* [AI_TRANSLATE](../../../sql-reference/functions/ai_translate.md): Translates text from one language to another using
  state-of-the-art language models.
* [AI_EXTRACT](../../../sql-reference/functions/ai_extract.md): Extracts information from text, documents, and images
  based on user-defined extraction instructions.
* [AI_SENTIMENT](../../../sql-reference/functions/ai_sentiment.md): Analyzes the overall and category sentiment in text.
