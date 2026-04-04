# Prompting Capabilities

When you first start using Mistral models, your first interaction will revolve around prompts. The art of crafting effective prompts is essential for generating desirable responses from Mistral models or other LLMs. This guide will walk you through example prompts showing four different prompting capabilities:

- Classification
- Summarization
- Personalization
- Evaluation

<a target="_blank" href="https://colab.research.google.com/github/mistralai/cookbook/blob/main/mistral/prompting/prompting_capabilities.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

## Classification

Mistral models can easily **categorize text** into distinct classes. Take a customer support bot for a bank as an illustration: we can establish a series of predetermined categories within the prompt and then instruct Mistral AI models to categorize the customer's question accordingly.

In the following example, when presented with the customer inquiry, Mistral AI models correctly categorizes it as "country support":

<table class="prompt-example">
    <tr>
        <td>User</td>
        <td>I am inquiring about the availability of your cards in the EU, as I am a resident of France and am interested in using your cards. </td>
    </tr>
    <tr>
        <td>Assistant</td>
        <td>country support</td>
    </tr>
</table>


<details>
<summary><b>Prompt</b></summary>

```
You are a bank customer service bot. Your task is to assess customer intent and categorize customer inquiry after <<<>>> into one of the following predefined categories:

card arrival
change pin
exchange rate
country support
cancel transfer
charge dispute

If the text doesn't fit into any of the above categories, classify it as:
customer service

You will only respond with the category. Do not include the word "Category". Do not provide explanations or notes.

####
Here are some examples:

Inquiry: How do I know if I will get my card, or if it is lost? I am concerned about the delivery process and would like to ensure that I will receive my card as expected. Could you please provide information about the tracking process for my card, or confirm if there are any indicators to identify if the card has been lost during delivery?
Category: card arrival
Inquiry: I am planning an international trip to Paris and would like to inquire about the current exchange rates for Euros as well as any associated fees for foreign transactions.
Category: exchange rate
Inquiry: What countries are getting support? I will be traveling and living abroad for an extended period of time, specifically in France and Germany, and would appreciate any information regarding compatibility and functionality in these regions.
Category: country support
Inquiry: Can I get help starting my computer? I am having difficulty starting my computer,and would appreciate your expertise in helping me troubleshoot the issue.
Category: customer service
###

<<<
Inquiry: {insert inquiry text here}
>>>
```

</details>


#### Strategies we used:

- **Few shot learning**: Few-shot learning or in-context learning is when we give a few examples in the prompts, and the LLM can generate corresponding output based on the example demonstrations. Few-shot learning can often improve model performance especially when the task is difficult or when we want the model to respond in a specific manner.
- **Delimiter**: Delimiters like `###`, `<<< >>>` specify the boundary between different sections of the text. In our example, we used `###` to indicate examples and `<<<>>>` to indicate customer inquiry.
- **Role playing**: Providing LLM a role (e.g., "You are a bank customer service bot.") adds personal context to the model and often leads to better performance.

## Summarization
Summarization is a common task for LLMs due to their natural language understanding and generation capabilities. Here is an example prompt we can use to generate interesting questions about an essay and summarize the essay.

<details>
<summary><b>Prompt</b></summary>

```
You are a commentator. Your task is to write a report on an essay.
When presented with the essay, come up with interesting questions to ask, and answer each question.
Afterward, combine all the information and write a report in the markdown format.