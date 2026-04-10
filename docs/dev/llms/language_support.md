# Source: https://dev.writer.com/home/language_support.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Language support

> Palmyra LLM supports 30+ languages including Arabic, French, Spanish, Hindi, and Chinese. View MMLU and BLEU benchmark scores for multilingual text generation.

Writer Palmyra LLM supports over 30 languages, including Arabic, French, Spanish, Hindi, Simplified Chinese, Traditional Chinese, and more. This page provides an overview of capabilities, performance benchmarks, and prompting examples on how to use these features.

When it comes to multi-language capabilities, there are two primary categories to consider: generation and translation. Generation typically refers to the ability to understand/create content, answer questions, and converse, all within the same language. Translation typically refers to the ability to transform text to and from English, where either the input or output language is English.

This page displays two of the many benchmarks used to evaluate multi-language performance in Palmyra LLMs. Writer Palmyra has the highest performance of any production LLM in the Holistic Evaluation of Language Models, an LLM evaluation framework developed by Stanford CRFM to serve as a living benchmark for the community, continuously updated with new scenarios, metrics, and models. While there are limited benchmarks available for evaluating text generation and translation in different languages, Palmyra has achieved some of the highest scores in both MMLU (Massive Multitask Language Understanding) and BLEU (Bilingual Evaluation Understudy) for other languages.

One benchmark that Writer uses to evaluate text generation performance is [MMLU](https://arxiv.org/abs/2009.03300). The [MLMM evaluation](https://arxiv.org/pdf/2307.16039.pdf) covers 57 tasks including elementary mathematics, U.S. history, computer science, law, and more. To attain high accuracy on this test, models must possess extensive world knowledge and problem-solving ability.

One benchmark that Writer uses to evaluate text translation performance is [BLEU](https://aclanthology.org/P02-1040.pdf). [Any BLEU score higher than 60](https://cloud.google.com/translate/automl/docs/evaluate#interpretation) indicates a higher quality translation than a human translation.

While Palmyra's core competency lies in the text generation realm, translation use cases are possible. However, it's important to exercise caution in languages where benchmarks aren't yet established. The team values transparency, and potential users should be aware of this caveat.

Therefore, any outputs or usage of Writer LLM should always include guidance from a human expert. The team continuously evaluates and refines capabilities, and learning happens with customers.

| Language            | MMLU/MLMM | BLEU (source \ English) |
| :------------------ | :-------- | :---------------------- |
| Arabic              | 68.9      | 61.2                    |
| Bengali             | 63.3      | 54.4                    |
| Bulgarian           | 76.3      | 64.2                    |
| Chinese simplified  | 71.7      | 63.8                    |
| Chinese traditional | 73.7      | 57.0                    |
| Croatian            | 64.9      | 66.4                    |
| Czech               | -         | 52.5                    |
| Danish              | 77.7      | 70.5                    |
| Dutch               | 73.6      | 73.9                    |
| English             | 70.2      | -                       |
| Finnish             | -         | 68.9                    |
| French              | 69.1      | 63.1                    |
| German              | 70.4      | 71.3                    |
| Greek               | -         | 60.4                    |
| Hebrew              | -         | 67.8                    |
| Hindi               | 77.9      | 68.4                    |
| Hungarian           | 67.7      | 65.3                    |
| Indonesian          | 67.8      | 63.5                    |
| Italian             | 72.5      | 70.9                    |
| Japanese            | 73.5      | 66.8                    |
| Korean              | -         | 56.8                    |
| Lithuanian          | -         | 59.3                    |
| Polish              | -         | 60.6                    |
| Portuguese          | -         | 66.2                    |
| Romanian            | 70.9      | 67.6                    |
| Russian             | 75.1      | 65.2                    |
| Spanish             | 72.5      | 79.3                    |
| Swahili             | -         | 62.8                    |
| Swedish             | -         | 63.2                    |
| Thai                | -         | 54.7                    |
| Turkish             | 64.1      | 57.5                    |
| Ukrainian           | 75.2      | 68.0                    |
| Vietnamese          | 72.5      | 60.3                    |

# Dialect support

Writer Palmyra LLM also supports outputting in specific language dialects. The best results come from using a prompt with the following characteristics:

1. The prompt itself is in the desired language and dialect
2. The prompt clearly describes the type of dialect, for example, "It's essential that you use the Spanish spoken in Spain."
3. The prompt provides specific examples of the dialect, both vocabulary and grammatical differences

The following example, although not in the desired language for simplicity's sake, is an example of an optimal prompt that asks for a translation in Spanish spoken in Spain.

```text  theme={null}
Hello, good afternoon! I need you to help me translate the following text. It's essential that you use the Spanish spoken in Spain. For example, you should use words like "coche" and/or "patata" instead of "carro" and/or "pap." Additionally, you need to pay attention to grammatical differences, such as the use of "voy a por" (Spain) instead of "voy por" (Latin America), or the structure of sentences like "hoy he comido una manzana" instead of "hoy comí una manzana." I prefer that you use "vosotros" (speak) instead of "ustedes" (speak), unless it's necessary to write very formally. 
```

> Here is the text to translate:\
> \[text you want translated]

```

## Basic prompt examples

### Translation

> Read the content of this source. Provide me with a translation of all its contents in French: https://writer.com/blog/ai-guardrails/

### Text generation

> Please write a blog post about the importance of productivity for small businesses in Arabic.

### Native multi-language support

> 人工知能の歴史と大規模言語モデルの開発について、短い段落を書いてください。読者はビジネステクノロジーニュースに興味がありますが、技術的なバックグラウンドはありません。技術的な概念を8年生の読解レベルで簡潔に説明してください。
```
