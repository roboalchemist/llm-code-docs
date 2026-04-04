# Source: https://python.useinstructor.com/concepts/index.md

# Instructor Concepts

This section explains the core concepts and features of the Instructor library, organized by category to help you find what you need.

## Core Concepts

These are the fundamental concepts you need to understand to use Instructor effectively:

- [Models](https://python.useinstructor.com/concepts/models/index.md) - Using Pydantic models to define output structures
- [Patching](https://python.useinstructor.com/concepts/patching/index.md) - How Instructor patches LLM clients
- [from_provider](https://python.useinstructor.com/concepts/from_provider/index.md) - Unified interface for creating clients across all providers
- [Migration Guide](https://python.useinstructor.com/concepts/migration/index.md) - Migrating from older patterns to from_provider
- [Types](https://python.useinstructor.com/concepts/types/index.md) - Working with different data types in your models
- [Validation](https://python.useinstructor.com/concepts/validation/index.md) - Validating LLM outputs against your models
- [Prompting](https://python.useinstructor.com/concepts/prompting/index.md) - Creating effective prompts for structured output extraction
- [Multimodal](https://python.useinstructor.com/concepts/multimodal/index.md) - Working with Audio Files, Images and PDFs

## Data Handling and Structures

These concepts relate to defining and working with different data structures:

- [Fields](https://python.useinstructor.com/concepts/fields/index.md) - Working with Pydantic fields and attributes
- [Lists and Arrays](https://python.useinstructor.com/concepts/lists/index.md) - Handling lists and arrays in your models
- [TypedDicts](https://python.useinstructor.com/concepts/typeddicts/index.md) - Using TypedDict for flexible typing
- [Union Types](https://python.useinstructor.com/concepts/unions/index.md) - Working with union types
- [Enums](https://python.useinstructor.com/concepts/enums/index.md) - Using enumerated types in your models
- [Missing](https://python.useinstructor.com/concepts/maybe/index.md) - Handling missing or optional values
- [Alias](https://python.useinstructor.com/concepts/alias/index.md) - Create field aliases
- [Citation](https://python.useinstructor.com/concepts/citation/index.md) - Extract and validate citations from source text

## Streaming Features

These features help you work with streaming responses:

- [Stream Partial](https://python.useinstructor.com/concepts/partial/index.md) - Stream partially completed responses
- [Stream Iterable](https://python.useinstructor.com/concepts/iterable/index.md) - Stream collections of completed objects
- [Raw Response](https://python.useinstructor.com/concepts/raw_response/index.md) - Access the raw LLM response

## Error Handling and Validation

These features help you ensure data quality:

- [Retrying](https://python.useinstructor.com/concepts/retrying/index.md) - Configure automatic retry behavior
- [Validators](https://python.useinstructor.com/concepts/reask_validation/index.md) - Define custom validation logic
- [Hooks](https://python.useinstructor.com/concepts/hooks/index.md) - Add callbacks for monitoring and debugging

## Performance Optimization

These features help you optimize performance:

- [Caching](https://python.useinstructor.com/concepts/caching/index.md) - Cache responses to improve performance
- [Prompt Caching](https://python.useinstructor.com/concepts/prompt_caching/index.md) - Cache prompts to reduce token usage
- [Usage Tokens](https://python.useinstructor.com/concepts/usage/index.md) - Track token usage
- [Parallel Tools](https://python.useinstructor.com/concepts/parallel/index.md) - Run multiple tools in parallel
- [Dictionary Operations](https://python.useinstructor.com/concepts/dictionary_operations/index.md) - Performance optimizations for dictionary operations

## Integration Features

These features help you integrate with other technologies:

- [FastAPI](https://python.useinstructor.com/concepts/fastapi/index.md) - Integrate with FastAPI
- [Type Adapter](https://python.useinstructor.com/concepts/typeadapter/index.md) - Use TypeAdapter with Instructor
- [Templating](https://python.useinstructor.com/concepts/templating/index.md) - Use templates for dynamic prompts
- [Distillation](https://python.useinstructor.com/concepts/distillation/index.md) - Optimize models for production

## Philosophy

- [Philosophy](https://python.useinstructor.com/concepts/philosophy/index.md) - The guiding principles behind Instructor

## How These Concepts Work Together

Instructor is built around a few key ideas that work together:

1. **Define Structure with Pydantic**: Use Pydantic models to define exactly what data you want.
1. **Create Clients with from_provider**: Use the unified interface to create clients for any provider.
1. **Validate and Retry**: Automatically validate responses and retry if necessary.
1. **Process Streams**: Handle streaming responses for real-time updates.

### Typical Workflow

```
sequenceDiagram
    participant User as Your Code
    participant Instructor
    participant LLM as LLM Provider

    User->>Instructor: Define Pydantic model
    User->>Instructor: Create client with from_provider
    User->>Instructor: Call create() with response_model
    Instructor->>LLM: Send structured request
    LLM->>Instructor: Return LLM response
    Instructor->>Instructor: Validate against model

    alt Validation Success
        Instructor->>User: Return validated Pydantic object
    else Validation Failure
        Instructor->>LLM: Retry with error context
        LLM->>Instructor: Return new response
        Instructor->>Instructor: Validate again
        Instructor->>User: Return validated object or error
    end
```

## What to Read Next

- If you're new to Instructor, start with [Models](https://python.useinstructor.com/concepts/models/index.md) and [from_provider](https://python.useinstructor.com/concepts/from_provider/index.md)
- If you're migrating from older patterns, see the [Migration Guide](https://python.useinstructor.com/concepts/migration/index.md)
- If you're having validation issues, check out [Validators](https://python.useinstructor.com/concepts/reask_validation/index.md) and [Retrying](https://python.useinstructor.com/concepts/retrying/index.md)
- For streaming applications, read [Stream Partial](https://python.useinstructor.com/concepts/partial/index.md) and [Stream Iterable](https://python.useinstructor.com/concepts/iterable/index.md)
- To optimize your application, look at [Caching](https://python.useinstructor.com/concepts/caching/index.md) and [Usage Tokens](https://python.useinstructor.com/concepts/usage/index.md)

For practical examples of these concepts, visit the [Cookbook](https://python.useinstructor.com/examples/index.md) section.

See Also

- [Getting Started Guide](https://python.useinstructor.com/getting-started/index.md) - Begin your journey with Instructor
- [Examples](https://python.useinstructor.com/examples/index.md) - Practical implementations of these concepts
- [Integrations](https://python.useinstructor.com/integrations/index.md) - Connect with different LLM providers
