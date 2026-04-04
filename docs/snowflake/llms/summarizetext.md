# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/summarizetext.md

# SummarizeText 2025.10.9.21

## Bundle

com.snowflake.openflow.runtime | runtime-llm-processors-nar

## Description

This processor uses a Large Language Model (LLM) to summarize the content of a FlowFile. It sends the content to an LLM service and writes the summary back to the FlowFile or as an attribute.

## Tags

ai, llm, openflow, summarization, text processing

## Input Requirement

REQUIRED

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| Content | The content to be summarized. FlowFile attributes may be referenced via Expression Language, and the contents of the FlowFile may be referenced via the flowfile_content variable. E.g., ${flowfile_content} |
| LLM Provider Service | The provider service for sending evaluation prompts to LLM |
| Max File Size | The maximum size of a FlowFile that can be summarized. If the FlowFile is larger than this, it will be routed to ‘failure’. |
| Output Strategy | Determines response output destination |
| Results Attribute | The name of the attribute to write the response to. |

## Relationships

| Name | Description |
| --- | --- |
| failure | FlowFiles that cannot be processed are routed to this relationship |
| success | FlowFiles that are successfully processed are routed to this relationship |
