# Source: https://dev.writer.com/home/generative-ai-overview.md

# Understand generative AI

> Learn how generative AI works and how to leverage Writer's models, safety, and best practices for building AI-powered applications.

This guide explains how generative AI works and how to use it effectively with Writer's platform.

Writer's generative AI enables applications to create text, images, and other content based on patterns learned from training data. Unlike traditional programming where you write explicit instructions, Writer's AI learns to generate appropriate responses by understanding context, patterns, and relationships in data.

## How generative AI works

Generative AI operates through a multi-step process that transforms your input into meaningful output:

![Generative AI Overview](https://files.readme.io/265b781-Overview_of_the_generative_AI_workflow.png)

### Core components

**Prompts** are the instructions you give to the AI model. They can be short questions, detailed instructions, or examples of the desired output format. Learn effective [prompting techniques](/home/prompting) to get the results you want.

**Foundation models** are large neural networks trained on vast amounts of text data. Writer offers [multiple Palmyra models](/home/models) with different capabilities, from fast text generation to advanced reasoning and tool calling.

**Tokenization** breaks down your input into smaller units (tokens) that the model can process. Understanding [tokens and pricing](/home/tokens) helps you improve costs and performance.

**Neural network processing** is where the model analyzes patterns, context, and relationships to determine the most appropriate response based on its training.

**Safety filtering** checks generated content for harmful, biased, or inappropriate material. Writer includes [built-in safety features](/home/toxic-check) to ensure responsible AI usage.

## Writer's model capabilities

### Palmyra models

Writer's [Palmyra models](/home/models) provide different capabilities optimized for various use cases. [Palmyra X5](/home/models#palmyra-x5) is the latest and most advanced model with a 1M token context window, adaptive reasoning, and speed and cost efficiency. There are also specialized models for specific use cases, such as [Palmyra Med](/home/models#palmyra-med) for medical and healthcare applications, and [Palmyra Fin](/home/models#palmyra-fin) for finance.

### Specialized features

* **Tool calling**: Enable models to use [external tools and APIs](/agent-builder/tool-calling-intro) for enhanced functionality
* **Vision capabilities**: Process and analyze images alongside text using [vision tools](/home/analyze-images)
* **Knowledge Graph integration**: Connect to your data sources for accurate, contextual responses using [Knowledge Graph](/home/knowledge-graph-concepts)
* **Streaming**: Get responses in real-time for better user experience with [streaming](/home/streaming)

## Best practices

### Prompt engineering

* **Be specific**: Provide clear, detailed instructions for what you want
* **Use examples**: Show the model the format or style you're looking for
* **Provide context**: Give relevant background information
* **Iterate and refine**: Test different approaches to improve results
* **Learn more**: Explore [prompting techniques](/home/prompting) for advanced strategies

### Safety and reliability

* **Review outputs**: Always check generated content before using it
* **Set boundaries**: Define what the AI should and shouldn't do
* **Monitor performance**: Track quality and adjust as needed
* **Handle errors gracefully**: Plan for cases where the AI doesn't perform as expected

### Performance optimization

* **Choose appropriate models**: Select the right [Palmyra model](/home/models) for your use case
* **Optimize prompts**: Use clear, concise language and follow [common prompting strategies](/home/prompting)
* **Manage context length**: Stay within [token limits](/home/tokens) for best performance
* **Use streaming**: Enable [streaming responses](/home/streaming) for real-time delivery
* **Fine-tune parameters**: Adjust [model parameters](/home/model-parameters) for optimal results

## Getting started with Writer

To begin using Writer's generative AI in your applications:

1. **Choose a model** from [Writer's available models](/home/models) that fits your needs
2. **Design effective prompts** using [prompting techniques](/home/prompting)
3. **Test and iterate** to improve performance
4. **Implement safety measures** using Writer's [built-in safety features](/home/toxic-check)
5. **Monitor and optimize** for ongoing success

## Next steps

* Start with the [API quickstart](/home/quickstart) to get up and running
* Explore [Writer's models](/home/models) to find the right fit for your use case
* Learn [prompting techniques](/home/prompting) for better results
* Understand [model parameters](/home/model-parameters) for fine-tuning
* See how to [integrate with your applications](/home/integrations-overview)
* Build [no-code agents](/home/applications) for rapid prototyping
* Connect your data with [Knowledge Graph](/home/knowledge-graph-concepts) for accurate responses
