# Source: https://docs.unifygtm.com/best-practices/prompting.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unifygtm.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Best Practices: Writing AI Prompts

## Section 1: General Tips

Unify has multiple AI features that can be used to improve qualification and outreach outcomes. To set yourself up for success, we recommend a few general principles for prompting when using these features:

* **Clear Instructions:** Be explicit about what you want the AI to do. Providing a clear set of instructions will help the AI understand what you want to accomplish and what steps to follow to complete the task(s).
* **Length =/= Quality:** Writing an overly detailed or essay length prompt does not mean that the AI will provide a better response. Excessive information can be detrimental unless it is properly structured and explained, as it can lead to confusion and misinterpretation of the prompt.
* **Provide Context:** Assume AI does not know your industry, company, or product as well as you do. Provide relevant context as you reference information about your company or your goals. For example, if you are referencing a niche keyword, provide a brief explanation of what it means, how it relates to your business, and the task you are giving the AI.

## Section 2: AI Agents

There are two primary ways that you can provide information and instruction to Unify's AI Agents.

### Questions

* **Questions:** Questions are the minimum required input to run an AI Agent. You can ask any question about a Company or Person and select the type of response you want the Agent to provide (e.g., True/False, Text, Multi-Select, Number).
* **What information to provide:** In the question, only include the research question you want the Agent to answer. Avoid adding clarifying information or instructions to keep it focused.

### Guidance

* **When to use:** Guidance is an optional field for AI Agents that enables you to provide additional context or instructions to the AI Agent. When asking more complex questions, when you have a set of instructions or requirements that you want the AI Agent to follow, or when you want to provide clarification on the research question, guidance is the best way to provide that information.
* **How To Structure Guidance:** Similar to Prompts, Guidance should be clear, concise, and specific. Use the guidance to provide specific directions about each question that you are asking, and additional context if there is a specific way that you want the AI Agent to conduct its research. For example, if you want the AI Agent to only use information from a specific source, you can include that information in the guidance. Or, if you want to provide more direction on when the AI Agent should select a specific answer for a multi select response type, that information should also be included in the guidance.

## Section 3: Smart Snippets

Smart Snippets are a powerful way to personalize messaging to your prospects.

* **Provide Context (Again!):** The model can only act on what you provide. This means you should specify the information you want to create copy from, select template variables to reference, or add Agent template variables to the Smart Snippet. Additionally, provide context around the template variable to create a coherent prompt. Think of template variables as placeholders for information and write sentences or blurbs surrounding those variables.
* **Adding References:** A common mistake is referencing information that you haven't provided to the model, which can lead to incorrect responses. To prevent this, ensure that if you're referencing data provided through a template variable or Agent output, you include that template variable in the Snippet.

### Agent Outputs in Smart Snippets

Using Agents to conduct research and then incorporating that research into a Smart Snippet is a great way to hyper-personalize your messaging. To use this feature effectively:

* **Separation of Concerns:** Use the Agent to conduct research only, and use the Snippet to generate the copy. Each feature is optimized for its respective task.
* **Structure the Snippet prompt around the Agent variables:** When writing a Smart Snippet prompt with Agent output template variables, provide context and labels about what each Agent output contains so the Snippet can handle it accordingly. For example, if you have an Agent Question that asks for a True/False or Number answer, write your prompt using the Agent template variable as a placeholder in your sentences to provide context to the Snippet.
  * For example, if your Agent question was "What is the most recent product launch from this company?", your Snippet prompt should be something like: "Research indicates that this company just launched `{{Agent Question}}`. Write a sentence to congratulate them on the launch."

## Section 4: AI Research

AI Research is a powerful way to automate and customize research that you want to conduct about any company that you are engaging. AI Research is powered by Unify's Observation Model, which is the system that Unify uses to run completely customized research for your company on your prospects.

### Prompting AI Research

Writing prompts for AI Research is slightly different from writing prompts for AI Agents, as AI Research is designed to read as much relevant information as possible before generating a report for you. We recommend following the style of the Observation prompts we generated for you as a starting point. To prompt for AI Research, follow these guidelines:

* **Pick a General Signal:** The goal with an Observation prompt is to describe a specific piece of information to the system that you'd like to monitor for any given company. For example, if you know that a company using a specific technology has a high likelihood of becoming your customer, an Observation for that could be: "Company uses an outbound sequencer (Outreach, Salesloft, Apollo, etc.) and a data/intent source (ZoomInfo, 6sense, Bombora, Clearbit, Demandbase, G2 Intent)."

* **Test and Iterate:** Once you've written your prompt, take advantage of the settings page to generate examples and see what the resulting reports look like.
