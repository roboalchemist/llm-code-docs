# Source: https://dev.writer.com/home/integrations-overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Explore integrations

This guide provides an overview of Writer's integrations with popular AI frameworks and platforms. After reading this guide, you can choose the right integration for your specific use case and development needs.

Writer integrates with several leading AI frameworks and cloud platforms to provide flexible deployment options and enhanced capabilities. Each integration offers unique benefits depending on your infrastructure, development preferences, and specific requirements.

## Compare integrations

| Integration               | Best for                    | Key benefits                                   |
| ------------------------- | --------------------------- | ---------------------------------------------- |
| **Amazon Bedrock**        | Enterprise AWS environments | Serverless scaling, AWS ecosystem integration  |
| **Amazon Strands Agents** | Multi-agent AI applications | Agent orchestration, durable sessions          |
| **LangChain**             | Complex AI workflows        | Tool integration, data source connections      |
| **Traceloop/OpenLLMetry** | Production monitoring       | Observability, debugging, performance tracking |
| **Instructor**            | Structured data extraction  | Pydantic validation, retry mechanisms          |

## Amazon Bedrock

[Amazon Bedrock](https://aws.amazon.com/bedrock/) is a fully managed service for building and scaling generative AI applications. Writer's Palmyra X5 and X4 models are available on Bedrock, enabling you to use AWS's infrastructure and ecosystem to build and scale your applications.

<Tabs>
  <Tab title="Key benefits">
    * **Serverless scaling**: automatic scaling based on demand
    * **AWS ecosystem integration**: integration with other AWS services
    * **Enterprise security**: built-in security and compliance features
    * **Cross-region inference**: distribute traffic across multiple AWS regions
  </Tab>

  <Tab title="Ideal use cases">
    * Large-scale enterprise applications
    * AWS-native development workflows
    * Applications requiring automatic scaling
    * Organizations with existing AWS infrastructure
  </Tab>
</Tabs>

<Card title="Get started" icon="rocket">
  [Learn how to use Writer with Amazon Bedrock](/home/integrations/bedrock)
</Card>

## Amazon Strands Agents

[Amazon Strands Agents](https://strandsagents.com/latest/) is a platform for building sophisticated multi-agent AI applications that require orchestration and collaboration.

Strands Agents SDK enables you to create AI applications using a model-driven approach with multiple agents working together. Writer models integrate with the Strands ecosystem.

<Tabs>
  <Tab title="Key benefits">
    * **Multi-agent orchestration**: coordinate multiple AI agents in complex workflows
    * **Durable session management**: maintain state across agent interactions
    * **Asynchronous support**: handle concurrent operations efficiently
    * **Model-driven approach**: define agent behavior through configuration
  </Tab>

  <Tab title="Ideal use cases">
    * Research and content creation pipelines
    * Customer service automation with multiple specialized agents
    * Complex decision-making workflows
    * Applications requiring agent collaboration
  </Tab>
</Tabs>

<Card title="Get started" icon="rocket">
  [Learn how to use Writer with Amazon Strands Agents](/home/integrations/strands)
</Card>

## LangChain

[LangChain](https://www.langchain.com/) provides a framework for developing applications powered by language models. Writer's integration allows you to use Writer's capabilities within the LangChain ecosystem alongside other tools and data sources.

<Tabs>
  <Tab title="Key benefits">
    * **Tool integration**: connect Writer with external tools and APIs
    * **Data source connections**: integrate with databases, files, and web sources
    * **Chain composition**: build complex workflows with multiple components
    * **Ecosystem compatibility**: works with the broader LangChain tool ecosystem
  </Tab>

  <Tab title="Ideal use cases">
    * Research assistants with web search capabilities
    * Document processing pipelines
    * Custom AI applications with multiple data sources
    * Applications requiring extensive tool integration
  </Tab>
</Tabs>

<Card title="Get started" icon="rocket">
  [Learn how to use Writer with LangChain](/home/integrations/langchain)
</Card>

## Traceloop/OpenLLMetry

[OpenLLMetry](https://openllmetry.com/) provides observability for LLM applications through OpenTelemetry-compatible tracing. It offers detailed insights into your Writer API usage, performance characteristics, and debugging capabilities.

<Tabs>
  <Tab title="Key benefits">
    * **Comprehensive observability**: track prompts, completions, and token usage
    * **OpenTelemetry compatibility**: works with any OpenTelemetry-compatible backend
    * **Performance insights**: monitor latency, throughput, and error rates
    * **Debugging capabilities**: trace issues across complex AI workflows
  </Tab>

  <Tab title="Ideal use cases">
    * Production AI applications
    * Applications requiring performance monitoring
    * Complex AI workflows needing debugging
    * Organizations with existing observability stacks
  </Tab>
</Tabs>

<Card title="Get started" icon="rocket">
  [Learn how to use Writer with OpenLLMetry](/home/integrations/openllmetry)
</Card>

## Instructor

[Instructor](https://github.com/instructor-ai/instructor) provides a high-level framework for getting structured outputs from language models. It offers built-in retry mechanisms, Pydantic validation, and prompt optimization specifically designed for structured data extraction.

<Tabs>
  <Tab title="Key benefits">
    * **Structured data extraction**: convert unstructured text into validated data structures
    * **Built-in retry logic**: automatic error handling and retry mechanisms
    * **Pydantic validation**: type-safe data validation and parsing
    * **Prompt optimization**: automatic prompt minimization and optimization
  </Tab>

  <Tab title="Ideal use cases">
    * Data extraction from documents and text
    * API response parsing and validation
    * Content analysis and classification
    * Data repair and cleaning workflows
  </Tab>
</Tabs>

<Card title="Get started" icon="rocket">
  [Learn how to use Writer with Instructor](/home/integrations/instructor)
</Card>

## Next steps

Once you've chosen an integration:

1. **Set up your development environment** with the required dependencies
2. **Follow the integration-specific guide** to implement Writer in your application
3. **Test your implementation** with sample data and workflows
4. **Deploy to production** following best practices for your chosen platform

For additional help, see the [API Quickstart](/home/quickstart) or explore the [SDKs documentation](/home/sdks) for language-specific implementation details.
