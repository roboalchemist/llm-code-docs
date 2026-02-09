# Source: https://docs.agent.ai/llm-models.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# LLM Models

> Agent.ai provides a number of LLM models that are available for use.

## **LLM Models**

Selecting the right Large Language Model (LLM) for your application is a critical decision that impacts performance, cost, and user experience. This guide provides a comprehensive comparison of leading LLMs to help you make an informed choice based on your specific requirements.

## How to Select the Right LLM

When choosing an LLM, consider these key factors:

1. **Task Complexity**: For complex reasoning, research, or creative tasks, prioritize models with high accuracy scores (8-10), even if they're slower or more expensive. For simpler, routine tasks, models with moderate accuracy (6-8) but higher speed may be sufficient.
2. **Response Time Requirements**: If your application needs real-time interactions, prioritize models with speed ratings of 8-10. Customer-facing applications generally benefit from faster models to maintain engagement.
3. **Context Needs**: If your application processes long documents or requires maintaining extended conversations, select models with context window ratings of 8 or higher. Some specialized tasks might work fine with smaller context windows.
4. **Budget Constraints**: Cost varies dramatically across models. Free and low-cost options (0-2 on our relative scale) can be excellent for startups or high-volume applications, while premium models (5+) might be justified for mission-critical enterprise applications where accuracy is paramount.
5. **Specific Capabilities**: Some models excel at particular tasks like code generation, multimodal understanding, or multilingual support. Review the use cases to find models that specialize in your specific needs.

The ideal approach is often to start with a model that balances your primary requirements, then test alternatives to fine-tune performance. Many organizations use multiple models: premium options for complex tasks and more affordable models for routine operations.

## Vendor Overview

**OpenAI**: Offers the most diverse range of models with industry-leading capabilities, though often at premium price points, with particular strengths in reasoning and multimodal applications.

**Anthropic (Claude)**: Focuses on highly reliable, safety-aligned models with exceptional context length capabilities, making them ideal for document analysis and complex reasoning tasks.

**Google**: Provides models with impressive context windows and competitive pricing, with the Gemini series offering particularly strong performance in creative and analytical tasks.

**Perplexity**: Specializes in research-oriented models with unique web search integration, offering free access to powerful research capabilities and real-time information.

**Other Vendors**: Offer open-source and specialized models that provide strong performance at minimal or no cost, making advanced AI accessible for deployment in resource-constrained environments.

## OpenAI Models

| Model        | Speed | Accuracy | Context Window | Relative Cost | Use Cases                                                                                                                                                                          |
| ------------ | :---: | :------: | :------------: | :-----------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GPT-4o       |   9   |     9    |        9       |       3       | • Multimodal assistant for text, audio, and images<br /> • Complex reasoning and coding tasks<br /> • Cost-sensitive deployments                                                   |
| GPT-4o-Mini  |   10  |     8    |        9       |       1       | • Real-time chatbots and high-volume applications<br /> • Long-context processing<br /> • General AI assistant tasks where affordability and speed are prioritized                 |
| GPT-4 Vision |   5   |     9    |        5       |       5       | • Image analysis and description<br /> • High-accuracy general assistant tasks<br /> • Creative and technical writing with visual context                                          |
| o1           |   6   |    10    |        9       |       4       | • Tackling highly complex problems in science, math, and coding<br /> • Advanced strategy or research planning<br /> • Scenarios accepting high latency/cost for superior accuracy |
| o1 Mini      |   8   |     8    |        9       |       1       | • Coding assistants and developer tools<br /> • Reasoning tasks that need efficiency over broad knowledge<br /> • Applications requiring moderate reasoning but faster responses   |
| o3 Mini      |   9   |     9    |        9       |       1       | • General-purpose chatbot for coding, math, science<br /> • Developer integrations<br /> • High-throughput AI services                                                             |
| GPT-4.5      |   5   |    10    |        9       |       10      | • Mission-critical AI tasks requiring top-tier intelligence<br /> • Highly complex problem solving or content generation<br /> • Multi-modal and extended context applications     |

## Anthropic (Claude) Models

| Model                         | Speed | Accuracy | Context Window | Relative Cost | Use Cases                                                                                                                                                     |
| ----------------------------- | :---: | :------: | :------------: | :-----------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Claude 3.7 Sonnet             |   8   |     9    |        9       |       2       | • Advanced coding and debugging assistant<br /> • Complex analytical tasks<br /> • Fast turnaround on detailed answers                                        |
| Claude 3.5 Sonnet             |   7   |     8    |        9       |       2       | • General-purpose AI assistant for long documents<br /> • Coding help and Q\&A<br /> • Everyday reasoning tasks with high reliability and alignment           |
| Claude 3.5 Sonnet Multi-Modal |   7   |     8    |        9       |       2       | • Image understanding in French or English<br /> • Multi-modal customer support<br /> • Research assistants combining text and visual data                    |
| Claude Opus                   |   6   |     7    |        9       |       9       | • High-precision analysis for complex queries<br /> • Long-form content summarization or generation<br /> • Enterprise scenarios requiring strict reliability |

## Google Models

| Model                          | Speed | Accuracy | Context Window | Relative Cost | Use Cases                                                                                                                                                               |
| ------------------------------ | :---: | :------: | :------------: | :-----------: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gemini 2.0 Pro                 |   7   |    10    |        8       |       5       | • Expert code generation and debugging<br /> • Complex prompt handling and multi-step reasoning<br /> • Cutting-edge research applications requiring maximum accuracy   |
| Gemini 2.0 Flash               |   9   |     9    |       10       |       1       | • Interactive agents and chatbots<br /> • General enterprise AI tasks at scale<br /> • Large-context processing up to \~1M tokens                                       |
| Gemini 2.0 Flash Thinking Mode |   8   |     9    |       10       |       2       | • Improved reasoning in QA and problem-solving<br /> • Explainable AI scenarios<br /> • Tasks requiring a balance of speed and reasoning accuracy                       |
| Gemini 1.5 Pro                 |   7   |     9    |       10       |       1       | • Sophisticated coding and mathematical problem solving<br /> • Processing extremely large contexts<br /> • Use cases tolerating higher cost/latency for higher quality |
| Gemini 1.5 Flash               |   9   |     7    |       10       |       1       | • Real-time assistants and chat services<br /> • Handling lengthy inputs<br /> • General tasks requiring decent reasoning at minimal cost                               |
| Gemma 7B It                    |   10  |     6    |        4       |       1       | • Italian-language chatbot and content generation<br /> • Lightweight reasoning and coding help<br /> • On-device or private deployments                                |
| Gemma2 9B It                   |   9   |     7    |        5       |       1       | • Multilingual assistant<br /> • Developer assistant on a budget<br /> • Text analysis with moderate complexity                                                         |

## Perplexity Models

| Model                    | Speed | Accuracy | Context Window | Relative Cost | Use Cases                                                                                                                                                           |
| ------------------------ | :---: | :------: | :------------: | :-----------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Perplexity               |   10  |     7    |        4       |       1       | • Quick factual Q\&A with web citations<br /> • Fast information lookups<br /> • General knowledge queries for free                                                 |
| Perplexity Deep Research |   3   |     9    |       10       |       1       | • In-depth research reports on any topic<br /> • Complex multi-hop questions requiring reasoning and evidence<br /> • Scholarly or investigative writing assistance |

## Open Source Models

| Model            | Speed | Accuracy | Context Window | Relative Cost | Use Cases                                                                                                                                                                   |
| ---------------- | :---: | :------: | :------------: | :-----------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DeepSeek R1      |   7   |     9    |        9       |       1       | • Advanced reasoning engine for math and code<br /> • Integrating into Retrieval-Augmented Generation pipelines<br /> • Open-source AI deployments needing strong reasoning |
| Llama 3.3 70B    |   8   |     9    |        9       |       1       | • Versatile technical and creative assistant<br /> • High-quality AI for smaller setups<br /> • Resource-efficient deployment                                               |
| Mixtral 8×7B 32K |   9   |     8    |        8       |       1       | • General-purpose open-source chatbot<br /> • Long document analysis and retrieval QA<br /> • Scenarios needing both efficiency and quality on modest hardware              |

## Model Deprecation

In the **LLM Engine** dropdown, there's a section labeled **"Legacy Models Soon To Be Deprecated"**. These are models we plan to remove soon, and we’ll automatically migrate agents using them to a recommended alternative.
