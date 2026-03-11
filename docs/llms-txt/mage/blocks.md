# Source: https://docs.mage.ai/design/blocks.md

# Source: https://docs.mage.ai/ai/blocks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Building, Configuring, and Automating with LLMs

> Learn how to create, configure, and run AI Blocks in Mage to generate text, produce structured outputs, write and validate code, and trigger other pipelines—empowering you to build advanced RAG and automation workflows with ease.

export const ProOnly = ({button = 'Get started for free', description = 'Try our fully managed solution to access this advanced feature.', source = 'documentation', title = 'Only in Mage Pro.'}) => <a href={`https://cloud.mage.ai/sign-up?source=${source}`} className="block my-4 px-5 py-4 overflow-hidden rounded-xl flex gap-3 border border-emerald-500/20 bg-emerald-50/50 dark:border-emerald-500/30 dark:bg-emerald-500/10" target="_blank">
    <div style={{
  display: 'flex',
  alignItems: 'center',
  width: '100%'
}}>
      <div className="text-sm prose min-w-0 text-emerald-900 dark:text-emerald-200" style={{
  flex: 1
}}>
        {title}
        <p className="normal">{description}</p>
      </div>

      <div> </div>

      <div>
        <ProButton label={button} href={`https://cloud.mage.ai/sign-up?source=${source}`} />
      </div>
    </div>
  </a>;

export const ProButton = ({href, label = 'Get started with Mage Pro for free', source = 'documentation'}) => <div style={{
  height: 32,
  position: 'relative'
}}>
    <a target="_blank" className="group px-4 py-1.5 relative inline-flex items-center text-sm font-medium rounded-full" href={href ?? `https://cloud.mage.ai/sign-up?source=${source}`}>
      <span className="absolute inset-0 bg-primary-dark dark:bg-primary-light/10 border-primary-light/30 rounded-full dark:border group-hover:opacity-[0.9] dark:group-hover:border-primary-light/60">
      </span>

      <div className="mr-0.5 space-x-2.5 flex items-center">
        <span class="z-10 text-white dark:text-primary-light">
          {label}
        </span>

        <svg width="3" height="24" viewBox="0 -9 3 24" class="h-5 rotate-0 overflow-visible text-white/90 dark:text-primary-light">
          <path d="M0 0L3 3L0 6" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path>
        </svg>
      </div>
    </a>
  </div>;

<ProOnly source="rag-pipeline" />

<Frame>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/28pRdPk2DAQ" title="AI Blocks" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

## 1. What is an AI Block?

An **AI block** is a special type of block in a Mage pipeline that uses a Large Language Model (LLM) to:

* Generate text or code
* Return structured data in a defined schema
* Trigger other pipelines as tools
* Validate outputs before passing them downstream

AI blocks are configured in **YAML** and can be designed to:

* Write and validate executable code
* Produce structured outputs for downstream blocks
* Decide which other pipelines to trigger and pass them variables

They integrate directly with Mage’s orchestration engine, allowing AI-generated outputs to be chained together, validated, and reused.

***

## 2. How to Use an AI Block

1. **Add a new block** in your Mage pipeline and set its type to `ai`.
2. **Write a prompt** — the main instruction for the AI.
3. **Optionally define output settings**:
   * **Code generation** (`output.code`)
   * **Structured JSON schema** (`output.format`)
4. **(Optional) Configure tools** to allow the AI to trigger other pipelines.
5. **Run the pipeline** — Mage will send your prompt and configuration to the AI model, validate the output (if specified), and pass it to the next blocks.

**Minimal example:**

```yaml  theme={"system"}
prompt: Summarize the input text in two sentences
```

***

## 3. AI Block Configuration

### 3.1 Basic Structure

```yaml  theme={"system"}
prompt: |
  Enter what you want AI to do
output:
  # Choose either `code` or `format`, not both
  code:
    save: true
    validation: Ensure this code runs without errors
  format:
    name:
      type: string
      description: The name of the person
    age:
      type: integer
      minimum: 0
validation: Validation prompt for output
tools:
  prompt: A prompt to decide which pipeline(s) to trigger
  required: false
  pipelines:
    - uuid: pipeline_uuid
      description: Description of the pipeline
      blocks:
        - uuid: block_uuid
      variables:
        user_id:
          type: string
```

***

### 3.2 Fields

#### **prompt** (Required)

The instruction to send to the AI model.

* Supports multi-line strings with `|`.
* Example:

```yaml  theme={"system"}
prompt: |
  Write a haiku about the moon.
```

#### **output**

Controls how the AI’s response is validated and structured.

1. **Code Output**

```yaml  theme={"system"}
output:
  code:
    save: true # Save generated code for reuse
    validation: Ensure no syntax errors
    language: sql # Optional, e.g., python or sql
    profile: default # SQL connection profile from io_config.yaml
    client: postgres # SQL client type
```

2. **Structured Format Output**

```yaml  theme={"system"}
output:
  format:
    title:
      type: string
      description: Blog post title
    tags:
      type: array
      items:
        type: string
    published:
      type: boolean
  validation: Ensure all fields are present and valid
```

3. **Unstructured Output**

```yaml  theme={"system"}
output: ''
```

***

#### **tools**

Lets the AI trigger other pipelines as part of execution.

```yaml  theme={"system"}
tools:
  prompt: Select a pipeline to process this request
  required: true
  pipelines:
    - uuid: abc123
      description: Cleans and normalizes customer data
      blocks:
        - uuid: block_1
      variables:
        customer_id:
          type: string
```

***

## 4. JSON Schema Support for Structured Outputs

The `output.format` and `variables` fields use **JSON Schema draft-07** (subset) to define:

* `type` — string, number, integer, boolean, array, object
* `description` — field description
* `enum` — allowed values
* `items` — item schema for arrays
* `minItems`, `maxItems` — constraints for arrays
* `pattern` — regex validation for strings
* `required` — list of required keys
* `oneOf`, `anyOf`, `allOf` — branching validation
* `$ref`, `$defs` — recursive or modular schemas

**Example:**

```yaml  theme={"system"}
output:
  format:
    email:
      type: string
      format: email
    signup_date:
      type: string
      format: date-time
```

***

## 5. Best Practices

* Use **`output.code`** only when expecting executable code.
* Use **`output.format`** for predictable structured outputs.
* Avoid defining both `code` and `format` in the same block.
* Use **multi-line prompts** with `|` for readability.
* Only include fields you need — minimal configs run faster.
* Always include a `validation` prompt for critical outputs.
* When chaining pipelines, define `variables` clearly for tool execution.

***

## 6. Example Configurations

**Minimal AI Block**

```yaml  theme={"system"}
prompt: Summarize this document in bullet points
```

**AI Block with Structured Output**

```yaml  theme={"system"}
prompt: Extract customer details from the text
output:
  format:
    name:
      type: string
      description: Customer's full name
    email:
      type: string
      format: email
    phone:
      type: string
      pattern: "^[0-9\\-]+$"
  validation: Ensure all fields are filled
```

**AI Block Triggering Another Pipeline**

```yaml  theme={"system"}
prompt: Analyze sales data and decide next action
tools:
  prompt: Choose a data processing pipeline
  required: true
  pipelines:
    - uuid: sales_analysis_001
      description: Processes daily sales data
      blocks:
        - uuid: clean_data_block
      variables:
        date:
          type: string
          format: date
```


Built with [Mintlify](https://mintlify.com).