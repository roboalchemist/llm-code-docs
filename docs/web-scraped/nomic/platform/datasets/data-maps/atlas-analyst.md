# Nomic Documentation

Source: https://docs.nomic.ai/platform/datasets/data-maps/atlas-analyst

The Analyst is a data agent for running analytics over your data. It automatically reasons through how to provide explainable answers to questions about your data using powerful tools like vector search and semantic filters.

When running an Advanced Analysis using the Analyst, you are given a view of the data that answers your question with full explainability and guides your data exploration.

New to Nomic? Check out our Quick Start Guide and text analysis guide to create a data map to start using the Atlas Analyst.

## The Atlas Analyst Workflow​

Unlike traditional tools that simply read data and provide answers, the Analyst allows you to understand the context, explore further, and take immediate action based on relevant data gathered during data retrieval.

Ask a Question in Plain Language

Open the Atlas Analyst panel and state your query conversationally.

Observe the Plan

The Analyst outlines its strategy, explaining how it intends to gather relevant data and context using its available tools.

Watch it Gather Context

The Analyst intelligently performs vector searches, text searches, filters, and statistical queries across your data. It will continue querying iteratively as needed until it has sufficient information. These actions are logged for transparency.

Receive an Explainable Answer

Get a written response grounded in your data, potentially including:

- Text summaries and explanations.
- Bulleted lists of key findings or themes.
- Tables summarizing quantitative results.
- Representative examples from your dataset.
- Links directly to the data supporting its findings.
Refine and Take Action

The Analyst highlights the relevant data points on your map. You can then:

- Control the Context: Interactively select semantic regions on the map to bring more specific data into the Analyst's context for further refinement.
- Explore the highlighted subset directly.
- Use the selection to tag data, create slices, or start a new analysis.
- Ask follow-up questions, leveraging the Analyst's support for multi-turn conversations, including compare-and-contrast queries across different data subsets.
## Key Benefits​

Faster Insights: Go from complex questions (like "summarize customer service complaints") to clear, actionable answers in seconds, skipping hours of manual exploration.

Usable Results: The Analyst directly applies filters and selections to your map, letting you instantly interact with the relevant data subset, tag examples, or refine the findings.

Learning Atlas by Example: See how the Analyst constructs searches, queries (including SQL), and filters to answer your specific questions, providing practical examples for your own data exploration techniques.

## Tips for Effective Questions​

To get the most out of the Atlas Analyst, consider these tips for formulating your questions:

Be Conversational: Ask follow-up questions based on the Analyst's previous responses to iterate and dive deeper.

Be Specific: "What are common themes in customer complaints about shipping?" works better than "shipping issues"

Mention Important Topics: The Atlas Analyst can help you dive deeper into the topics present in your data map.

## Availability and Usage Limits​

Available to all Atlas users: Works with both new and existing data maps. Access the Atlas Analyst from any data map in your Atlas dashboard.

## Current Limitations​

Spatial Awareness: The Atlas Analyst cannot interpret visual patterns, clusters, or outliers in the map layout. Visual analysis still requires human assessment.

Selection Capacity: The analyst composes searches and filters to create one selection for an analysis, which may limit its ability to compare and contrast between different cohorts or data segments.

Domain Knowledge: Highly specialized queries may require additional context from the user.

Verification Needed: Users should independently verify critical insights derived from the Atlas Analyst.

- The Atlas Analyst Workflow
- Key Benefits
- Tips for Effective Questions
- Availability and Usage Limits
- Current Limitations
