# Source: https://docs.snowflake.com/en/release-notes/2026/other/2026-01-26-ai-parse-document-images-preview.md

# Jan 26, 2026: Extract images from documents using AI_PARSE_DOCUMENT (Preview)

The AI_PARSE_DOCUMENT AI Function can now extract images embedded in PDF and Word documents, alongside text, data, and
layout elements. Extracted images can be written to stages or
passed directly to other Cortex AI Functions for further analysis.

This new capability unlocks a number of advanced use cases, including:

* *Enrich data*: Extract images from documents to add visual context for deeper insights.
* *Multimodal RAG*: Combine images and text for retrieval-augmented generation (RAG) to improve model responses.
* *Image classification*: Use extracted images with AI_EXTRACT or AI_COMPLETE for automatic tagging and analysis.
* *Knowledge bases*: Build richer repositories by including both text and images for better search and reasoning.
* *Compliance*: Extract and analyze images (e.g., charts, signatures) for regulatory and audit workflows.

There is no additional cost for image extraction beyond the standard page-based billing for AI_PARSE_DOCUMENT.

For more information, see [Cortex AI Functions: Image extraction with AI_PARSE_DOCUMENT](../../../user-guide/snowflake-cortex/image-extraction.md).
