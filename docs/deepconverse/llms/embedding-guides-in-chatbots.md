# Source: https://docs.deepconverse.com/product-docs/guides/embedding-guides-in-chatbots.md

# Embedding Guides in Chatbots

Guides can be embedded into the chatbot using the Guide block.&#x20;

{% content-ref url="../conversational-flow-builder/conversation-blocks/guide-blocks/guide-chatbot" %}
[guide-chatbot](https://docs.deepconverse.com/product-docs/conversational-flow-builder/conversation-blocks/guide-blocks/guide-chatbot)
{% endcontent-ref %}

Customers can go through Guides in the chatbot and troubleshoot issues seamlessly. Here is an interaction example.

{% embed url="<https://www.loom.com/share/efd786c888744f63bf883dde9c72924c>" %}

### Events

When a customer goes through a Guide there can be three outcomes.&#x20;

1. Solved
2. Unsolved
3. Skipped

For Solved/Unsolved we track that as an Answer Feedback given for the specific guide that is presented to the customer.&#x20;

You can make use of the emitting events on the transitions if you want to mark the chatbot conversation as Successful or Unsuccessful.&#x20;
