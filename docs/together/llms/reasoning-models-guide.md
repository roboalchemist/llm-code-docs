# Source: https://docs.together.ai/docs/reasoning-models-guide.md

# Reasoning Models Guide

> How reasoning models like DeepSeek-R1 work.

## Reasoning vs. Non-reasoning Models

Reasoning models are trained very differently from their non-reasoning counterparts, and as a result they serve different purposes. Below we'll compare both types of models, details for reasoning models, pros and cons, applications and example use-cases.

Reasoning models like `DeepSeek-R1` are specifically developed to engage in extended, deep analysis of complex challenges. Their strength lies in strategic thinking, developing comprehensive solutions to intricate problems, and processing large amounts of nuanced information to reach decisions. Their high precision and accuracy make them particularly valuable in specialized fields traditionally requiring human expertise, such as mathematics, scientific research, legal work, healthcare, financial analysis.

Non-reasoning models such as `Llama 3.3 70B` or `DeepSeek-V3` are trained for efficient, direct task execution with faster response times and better cost efficiency.

Your application can leverage both types of models: using DeepSeek-R1 to develop the strategic framework and problem-solving approach, while deploying non-reasoning models to handle specific tasks where swift execution and cost considerations outweigh the need for absolute precision.

## Reasoning models use-cases

* **Analyzing and assessing AI model outputs**\
  Reasoning models excel at evaluating responses from other systems, particularly in data validation scenarios. This becomes especially valuable in critical fields like law, where these models can apply contextual understanding rather than just following rigid validation rules.

* **Code analysis and improvement**\
  Reasoning models are great at conducting thorough code reviews and suggesting improvements across large codebases. Their ability to process extensive code makes them particularly valuable for comprehensive review processes.

* **Strategic planning and task delegation**\
  These models shine in creating detailed, multi-stage plans and determining the most suitable AI model for each phase based on specific requirements like processing speed or analytical depth needed for the task.

* **Complex document analysis and pattern recognition**\
  The models excel at processing and analyzing extensive, unstructured documents such as contract agreements, legal reports, and healthcare documentation. They're particularly good at identifying connections between different documents and making connections.

* **Precision information extraction**\
  When dealing with large volumes of unstructured data, these models excel at pinpointing and extracting exactly the relevant information needed to answer specific queries, effectively filtering out noise in search and retrieval processes. This makes them great to use in RAG or LLM augmented internet search use-cases.

* **Handling unclear instructions**\
  These models are particularly skilled at working with incomplete or ambiguous information. They can effectively interpret user intent and will proactively seek clarification rather than making assumptions when faced with information gaps.

## Pros and Cons

Reasoning models excel for tasks where you need:

* High accuracy and dependable decision-making capabilities
* Solutions to complex problems involving multiple variables and ambiguous data
* Can afford higher query latencies
* Have a higher cost/token budget per task

Non-reasoning models are optimal when you need:

* Faster processing speed (lower overall query latency) and lower operational costs
* Execution of clearly defined, straightforward tasks
* Function calling, JSON mode or other well structured tasks


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt