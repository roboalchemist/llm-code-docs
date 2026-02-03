# Source: https://docs.unifygtm.com/reference/agents/response-types.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unifygtm.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Agent Response Types

> Control how Unify Agents respond to your questions.

## Overview

A single Agent can answer multiple questions, each with different response types.
Unify ensures that Agents adhere to the response types you specify to give
you fine-grained control over AI.

<Tip>Unify Agents know what they don't know. If the Agent cannot find an
answer to your question, it will respond accordingly.</Tip>

<Frame caption="An example of an Agent using various response types.">
  <img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/agents/agent-response-types.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=112343d2875c85a30d4e3c6a17572968" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/agents/agent-response-types.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/agents/agent-response-types.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=00093adf2b7f7dcd417567a78120db5a 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/agents/agent-response-types.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=b2037a079d72d9e8a4b0ccdf031f4037 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/agents/agent-response-types.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=08df70916e4de9ac5ae4213ec0c3a975 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/agents/agent-response-types.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=515e30938e02a1ec422e82038bfe1e75 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/agents/agent-response-types.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=c2f515386b92652ddf504209e82dbb60 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/agents/agent-response-types.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=ccf3595d0092584d5a55e25b732d5611 2500w" />
</Frame>

## Response types

### True / False

Agents will respond with either `True` or `False` to a question of this type. This is best for simple questions:

* *Does this company have an office in San Francisco?*
* *Is there a pricing page on this company's website?*

### Number

Agents will respond with a number to a question of this type. This is best for questions that require a numerical answer:

* *What was the revenue for this company last year?*
* *How many years of full-time experience does this person have?*

### Select

Agents will respond with a *single* option from a list that you specify.
This is best for multiple-choice questions:

* *Is this company B2B, B2C, or B2G?*
  * Options: `B2B`, `B2C`, `B2G`
  * Answer: `B2B`

In some cases, you may want the Agent to respond with *multiple* options from the list you provided.
Click the `Allow multiple options` checkbox to enable this.
When enabled, the Agent will respond with zero, one, or multiple options.

* *Which of the following funding rounds has this company completed?*
  * Options: `Seed`, `Series A`, `Series B`, `Series C`, `Series D`, `Series E`
  * Answer: `Seed`, `Series A`
