# Source: https://dev.writer.com/home/pricing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Pricing

> View pricing for Writer AI models. Compare costs per million tokens for Palmyra models including X5, X4, Med, Fin, Creative, and Vision.

<Info>
  For any custom pricing, **[contact Sales](https://go.writer.com/contact-sales)**.
</Info>

## Base model

The table below outlines our [base model](/home/models#models), which is focused on text input and output. The input and output prices are displayed per 1M tokens unless otherwise specified.

| Model name                                                    | Model ID                 | Input / 1M | Output / 1M |
| ------------------------------------------------------------- | ------------------------ | ---------- | ----------- |
| [Palmyra X5](/home/models#palmyra-x5)                         | `palmyra-x5`             | \$0.60     | \$6.00      |
| [Palmyra X4](/home/models#palmyra-x4)                         | `palmyra-x4`             | \$2.50     | \$10.00     |
| [Palmyra X 003 Instruct](/home/models#palmyra-x-003-instruct) | `palmyra-x-003-instruct` | \$7.50     | \$22.50     |
| [Palmyra Med](/home/models#palmyra-med)                       | `palmyra-med`            | \$5.00     | \$12.00     |
| [Palmyra Fin](/home/models#palmyra-fin)                       | `palmyra-fin`            | \$5.00     | \$12.00     |
| [Palmyra Creative](/home/models#palmyra-creative)             | `palmyra-creative`       | \$5.00     | \$12.00     |

## WRITER Agent

The table below outlines pricing for LLM usage in [WRITER Agent](https://support.writer.com/article/235-ask-writer), an intelligent interface that turns complexity into scale with repeatable, data-driven playbooks connected to the systems where work happens.

| Input / 1M | Output / 1M |
| ---------- | ----------- |
| \$5.00     | \$12.00     |

## Palmyra Vision

The table below outlines pricing for [Palmyra Vision](/home/models#palmyra-vision), which takes in a variety of inputs and produces text as an output. The input and output price is for 1M tokens unless otherwise specified.

| Type  | Input          | Output / 1M |
| ----- | -------------- | ----------- |
| Image | \$0.005/image  | \$8.00      |
| Video | \$0.005/second | \$8.00      |
| Text  | \$7.50/1M      | \$22.50     |

## Knowledge Graph

The table below outlines pricing for [Knowledge Graph](/home/knowledge-graph), Writer's graph-based RAG.

| Capability              | Cost                          |
| ----------------------- | ----------------------------- |
| Knowledge Graph hosting | \$0.085/gb of storage per day |
| Data extraction         | \$0.00015/page                |
| File parsing (OCR)      | \$0.055/page                  |
| Web Access              | \$0.12/page                   |

Data connectors for Knowledge Graph are available for Enterprise plans. To learn, more please [contact Sales](https://go.writer.com/contact-sales).

## Tools API

The table below outlines pricing for the [Tools API](/api-reference/tool-api/), which provides utilities for pre-processing and comprehending text.

| Tool                                             | Cost         |
| ------------------------------------------------ | ------------ |
| [PDF parser](/api-reference/tool-api/pdf-parser) | \$0.055/page |

## Translation API

The [Translation API](/api-reference/translation-api/translate) provides utilities for translating text. The cost is:

* **Input**: \$20.00/100k words

## Deprecated models

The table below show pricing for deprecated models. See the [deprecation policy](/home/models#deprecation-policy) for more information.

| Model name             | Deprecation date | Input / 1M | Output / 1M |
| ---------------------- | ---------------- | ---------- | ----------- |
| Palmyra Fin 32k        | 2025-03-03       | \$5.00     | \$12.00     |
| Palmyra X 002 32k      | 2024-09-06       | \$1.00     | \$2.00      |
| Palmyra X 32k Instruct | 2024-09-06       | \$1.00     | \$2.00      |
| Palmyra X 002 Instruct | 2024-09-06       | \$1.00     | \$2.00      |

## Deprecated tools

The table below shows pricing for deprecated tools. See the [deprecation policy](/home/models#deprecation-policy) for more information.

| Tool               | Deprecation date | Cost                                        | Migration guide                                                           |
| ------------------ | ---------------- | ------------------------------------------- | ------------------------------------------------------------------------- |
| AI detection       | 2025-12-22       | \$0.03 per request                          | —                                                                         |
| Medical comprehend | 2025-12-22       | \$0.02 per 1M words input (no output costs) | [Migrate to LLM tool](/api-reference/migration-guides/comprehend-medical) |
