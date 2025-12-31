# Source: https://firebase.google.com/docs/reference/js/ai.thinkingconfig.md.txt

# ThinkingConfig interface

Configuration for "thinking" behavior of compatible Gemini models.

Certain models utilize a thinking process before generating a response. This allows them to reason through complex problems and plan a more coherent and accurate answer.

**Signature:**  

    export interface ThinkingConfig 

## Properties

|                                                      Property                                                       |  Type   |                                                                                                                                                                                                                                                                                 Description                                                                                                                                                                                                                                                                                 |
|---------------------------------------------------------------------------------------------------------------------|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [includeThoughts](https://firebase.google.com/docs/reference/js/ai.thinkingconfig.md#thinkingconfigincludethoughts) | boolean | Whether to include "thought summaries" in the model's response.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [thinkingBudget](https://firebase.google.com/docs/reference/js/ai.thinkingconfig.md#thinkingconfigthinkingbudget)   | number  | The thinking budget, in tokens.This parameter sets an upper limit on the number of tokens the model can use for its internal "thinking" process. A higher budget may result in higher quality responses for complex tasks but can also increase latency and cost.If you don't specify a budget, the model will determine the appropriate amount of thinking based on the complexity of the prompt.An error will be thrown if you set a thinking budget for a model that does not support this feature or if the specified budget is not within the model's supported range. |

## ThinkingConfig.includeThoughts

Whether to include "thought summaries" in the model's response.

Thought summaries provide a brief overview of the model's internal thinking process, offering insight into how it arrived at the final answer. This can be useful for debugging, understanding the model's reasoning, and verifying its accuracy.

**Signature:**  

    includeThoughts?: boolean;

## ThinkingConfig.thinkingBudget

The thinking budget, in tokens.

This parameter sets an upper limit on the number of tokens the model can use for its internal "thinking" process. A higher budget may result in higher quality responses for complex tasks but can also increase latency and cost.

If you don't specify a budget, the model will determine the appropriate amount of thinking based on the complexity of the prompt.

An error will be thrown if you set a thinking budget for a model that does not support this feature or if the specified budget is not within the model's supported range.

**Signature:**  

    thinkingBudget?: number;