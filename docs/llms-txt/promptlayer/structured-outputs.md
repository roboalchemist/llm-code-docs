# Source: https://docs.promptlayer.com/features/prompt-registry/structured-outputs.md

# Structured Outputs

Structured outputs ensure LLM responses follow specific formats, making them easier to use in your applications. For more advanced structured data requirements, you may also want to check out our [Tool Calling documentation](/features/prompt-registry/tool-calling).

## What are Structured Outputs?

Structured outputs define formats LLMs must follow when generating responses:

* Consistent response formats
* Easier parsing and validation
* More reliable integration with your applications
* Less error handling

Examples include customer records, product information, and analytical results.

## Creating Structured Outputs with JSON Schema

<video controls="controls">
  <source src="https://mintcdn.com/promptlayer/leEzDioSQJUNIopi/videos/schema-editor.mp4?fit=max&auto=format&n=leEzDioSQJUNIopi&q=85&s=a844a9ab537bcbb6324cf7ea66484a4a" type="video/mp4" data-path="videos/schema-editor.mp4" />
</video>

To add a JSON schema to your prompt template:

1. Edit your prompt template
2. Click "Functions & Output"
3. Select "Structured Output"
4. Click "Add Schema"
5. Define your schema structure

### Example: Customer Review Analysis Schema

```json  theme={null}
{
  "type": "object",
  "properties": {
    "sentiment": {
      "type": "string",
      "enum": ["positive", "neutral", "negative"],
      "description": "The overall sentiment of the review"
    },
    "topics": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "List of topics mentioned in the review"
    }
  },
  "required": ["sentiment", "topics"]
}
```

## Schema Configuration Options

### Strict Mode

Strict mode enforces more rigorous schema validation. When enabled, the LLM output must exactly match the schema specification with no additional fields or deviations.

In the schema editor:

1. Toggle "Strict Mode" in the schema settings
2. Ensure your schema is complete and accurate
3. Test with sample inputs

### Additional Properties

Control whether objects can have properties not defined in your schema:

* **Disabled** (default): Only properties you define are allowed
* **Enabled**: Objects can include additional properties beyond those specified

This applies to the root object and all nested objects in your schema.

## String Validation

Add constraints to string fields to ensure proper formatting. The schema editor provides an intuitive interface for configuring these constraints:

<img src="https://mintcdn.com/promptlayer/ZFievX8eHMthPg8f/images/string_constraints.png?fit=max&auto=format&n=ZFievX8eHMthPg8f&q=85&s=239c65f10c1bd63e3ba2047d90f859df" alt="String Constraints Editor" data-og-width="2524" width="2524" data-og-height="1756" height="1756" data-path="images/string_constraints.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/ZFievX8eHMthPg8f/images/string_constraints.png?w=280&fit=max&auto=format&n=ZFievX8eHMthPg8f&q=85&s=fd23e32d9b6eb2ba8d5dbf37db92a802 280w, https://mintcdn.com/promptlayer/ZFievX8eHMthPg8f/images/string_constraints.png?w=560&fit=max&auto=format&n=ZFievX8eHMthPg8f&q=85&s=edf06f9cf771507f118972c507adabeb 560w, https://mintcdn.com/promptlayer/ZFievX8eHMthPg8f/images/string_constraints.png?w=840&fit=max&auto=format&n=ZFievX8eHMthPg8f&q=85&s=5ceec533f2271782d38fccb562d26afe 840w, https://mintcdn.com/promptlayer/ZFievX8eHMthPg8f/images/string_constraints.png?w=1100&fit=max&auto=format&n=ZFievX8eHMthPg8f&q=85&s=a969230c1e610f6a909ceb8c50ed844a 1100w, https://mintcdn.com/promptlayer/ZFievX8eHMthPg8f/images/string_constraints.png?w=1650&fit=max&auto=format&n=ZFievX8eHMthPg8f&q=85&s=a8f4041dad51dfc975ea346e63315026 1650w, https://mintcdn.com/promptlayer/ZFievX8eHMthPg8f/images/string_constraints.png?w=2500&fit=max&auto=format&n=ZFievX8eHMthPg8f&q=85&s=a0db2f699cdc4140adef246f6e92719c 2500w" />

### Length Constraints

Control the minimum and maximum length of strings using the **Min Length** and **Max Length** fields. For example, you might require a username to be between 3-20 characters, or limit a bio field to 500 characters maximum.

### Pattern Matching

Use regex patterns to validate string formats. Enter your regular expression in the **Pattern** field to enforce specific formats like alphanumeric usernames with underscores (`^[a-zA-Z0-9_]+$`) or valid phone numbers (`^\+?[1-9]\d{1,14}$`).

### Format Validation

Specify standard formats for automatic validation using the **Select format...** dropdown. This provides built-in validation for common data types like email addresses, URLs, dates, and UUIDs without requiring custom regex patterns.

**Supported formats:**

* `date-time` - ISO 8601 datetime (e.g., "2024-01-15T10:30:00Z")
* `date` - Full date (e.g., "2024-01-15")
* `time` - Time (e.g., "10:30:00")
* `duration` - ISO 8601 duration
* `email` - Email address
* `idn-email` - Internationalized email address
* `hostname` - Valid hostname
* `idn-hostname` - Internationalized hostname
* `ipv4` - IPv4 address
* `ipv6` - IPv6 address
* `uri` - URI/URL
* `uri-reference` - URI reference
* `iri` - Internationalized URI
* `iri-reference` - Internationalized URI reference
* `uuid` - UUID format
* `uri-template` - URI template
* `json-pointer` - JSON pointer
* `relative-json-pointer` - Relative JSON pointer
* `regex` - Regular expression

## Number Validation

Add constraints to number fields to ensure proper validation. The schema editor provides an intuitive interface for configuring these constraints:

<img src="https://mintcdn.com/promptlayer/ZOdPY_5CRt24K1HV/images/number_constraints.png?fit=max&auto=format&n=ZOdPY_5CRt24K1HV&q=85&s=e28a4b00d3126a3ce2216ded3359f4d8" alt="Number Constraints Editor" data-og-width="2468" width="2468" data-og-height="1732" height="1732" data-path="images/number_constraints.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/ZOdPY_5CRt24K1HV/images/number_constraints.png?w=280&fit=max&auto=format&n=ZOdPY_5CRt24K1HV&q=85&s=e50a095f4134f840239195698a5b5adc 280w, https://mintcdn.com/promptlayer/ZOdPY_5CRt24K1HV/images/number_constraints.png?w=560&fit=max&auto=format&n=ZOdPY_5CRt24K1HV&q=85&s=140e132a5eabe0c1a428b19223858ba3 560w, https://mintcdn.com/promptlayer/ZOdPY_5CRt24K1HV/images/number_constraints.png?w=840&fit=max&auto=format&n=ZOdPY_5CRt24K1HV&q=85&s=bbe9e5e3ec385b7c2405e2badbed5752 840w, https://mintcdn.com/promptlayer/ZOdPY_5CRt24K1HV/images/number_constraints.png?w=1100&fit=max&auto=format&n=ZOdPY_5CRt24K1HV&q=85&s=8a9cab7320f234e37d81283d63f373b8 1100w, https://mintcdn.com/promptlayer/ZOdPY_5CRt24K1HV/images/number_constraints.png?w=1650&fit=max&auto=format&n=ZOdPY_5CRt24K1HV&q=85&s=ee5e8f09923f9e6da8e51b86fff9fb14 1650w, https://mintcdn.com/promptlayer/ZOdPY_5CRt24K1HV/images/number_constraints.png?w=2500&fit=max&auto=format&n=ZOdPY_5CRt24K1HV&q=85&s=2385c4f0f4e50c169205329c55a8d223 2500w" />

### Range Constraints

Control the minimum and maximum values using the **Minimum** and **Maximum** fields. For example, you might require an age to be between 0-150, or limit a rating to 1-5 stars.

### Exclusive Boundaries

Use **Exclusive Minimum** and **Exclusive Maximum** checkboxes when you need strict inequalities. For instance, a price field might need to be greater than 0 (not equal to 0), requiring an exclusive minimum.

### Multiple Of

Specify that numbers must be multiples of a particular value using the **Multiple Of** field. This is useful for ensuring prices are rounded to cents (0.01), requiring even numbers (2), or enforcing other step values.

**Example use cases:**

* Age between 0-150 (inclusive)
* Price greater than 0, rounded to cents (exclusive minimum: 0, multipleOf: 0.01)
* Rating from 1-5 stars (inclusive range)

## Array Validation

Control array size and structure.

<img src="https://mintcdn.com/promptlayer/-9Egue1V4AlXBy8b/images/array_constraints.png?fit=max&auto=format&n=-9Egue1V4AlXBy8b&q=85&s=09346d16c2a841ce0f16e57299eb9179" alt="Array Constraints Editor" data-og-width="2526" width="2526" data-og-height="1760" height="1760" data-path="images/array_constraints.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/-9Egue1V4AlXBy8b/images/array_constraints.png?w=280&fit=max&auto=format&n=-9Egue1V4AlXBy8b&q=85&s=bf4cded0c60202d0eff148cf406ad452 280w, https://mintcdn.com/promptlayer/-9Egue1V4AlXBy8b/images/array_constraints.png?w=560&fit=max&auto=format&n=-9Egue1V4AlXBy8b&q=85&s=9db7ea8067adab28c0e93370d39f7456 560w, https://mintcdn.com/promptlayer/-9Egue1V4AlXBy8b/images/array_constraints.png?w=840&fit=max&auto=format&n=-9Egue1V4AlXBy8b&q=85&s=99d3dc78052584e45e9a3e07ab988e45 840w, https://mintcdn.com/promptlayer/-9Egue1V4AlXBy8b/images/array_constraints.png?w=1100&fit=max&auto=format&n=-9Egue1V4AlXBy8b&q=85&s=e309082af9d6898f4c80c75d43cb8f0c 1100w, https://mintcdn.com/promptlayer/-9Egue1V4AlXBy8b/images/array_constraints.png?w=1650&fit=max&auto=format&n=-9Egue1V4AlXBy8b&q=85&s=9c5842689f695baf6632c628dac7be02 1650w, https://mintcdn.com/promptlayer/-9Egue1V4AlXBy8b/images/array_constraints.png?w=2500&fit=max&auto=format&n=-9Egue1V4AlXBy8b&q=85&s=fc9aac2d71ff838b5e2898607f96fea1 2500w" />

### Size Constraints

Control the minimum and maximum number of items in an array using the **Minimum Items** and **Maximum Items** fields. For example, you might require at least 1 tag but no more than 10, or limit search results to a maximum of 5 items.

**Example use cases:**

* Tags array with 1-10 items
* Top 5 search results (maximum only)
* At least 3 required reviewers (minimum only)

## Nested Objects and Required Fields

Using **Composition** mode you can define complex structures with nested objects and specify which fields are required at each level:

<img src="https://mintcdn.com/promptlayer/-9Egue1V4AlXBy8b/images/composition_mode.png?fit=max&auto=format&n=-9Egue1V4AlXBy8b&q=85&s=15ee0a7a41efb63578c5d5453e822685" alt="Composition Mode Editor" data-og-width="2413" width="2413" data-og-height="1232" height="1232" data-path="images/composition_mode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/-9Egue1V4AlXBy8b/images/composition_mode.png?w=280&fit=max&auto=format&n=-9Egue1V4AlXBy8b&q=85&s=d34ab26559ce4a85cd237e25f9644f7f 280w, https://mintcdn.com/promptlayer/-9Egue1V4AlXBy8b/images/composition_mode.png?w=560&fit=max&auto=format&n=-9Egue1V4AlXBy8b&q=85&s=27ff77ad50b10ba21d0af5cd21f156dc 560w, https://mintcdn.com/promptlayer/-9Egue1V4AlXBy8b/images/composition_mode.png?w=840&fit=max&auto=format&n=-9Egue1V4AlXBy8b&q=85&s=d64fbf78333841fc06c2f06676c828cb 840w, https://mintcdn.com/promptlayer/-9Egue1V4AlXBy8b/images/composition_mode.png?w=1100&fit=max&auto=format&n=-9Egue1V4AlXBy8b&q=85&s=3759633dcfd51f73b7701e6af7ef41c2 1100w, https://mintcdn.com/promptlayer/-9Egue1V4AlXBy8b/images/composition_mode.png?w=1650&fit=max&auto=format&n=-9Egue1V4AlXBy8b&q=85&s=fdd905e01095f1aff390b0f4bdf13f1b 1650w, https://mintcdn.com/promptlayer/-9Egue1V4AlXBy8b/images/composition_mode.png?w=2500&fit=max&auto=format&n=-9Egue1V4AlXBy8b&q=85&s=711903e800f277ae17133279284786ee 2500w" />

In the interactive editor:

1. Create your parent object
2. Add nested properties
3. Toggle "Required" for each field at its level
4. Nest objects as deeply as needed using the "Add Field" button

## Reusable Schema Definitions with \$defs

For complex schemas with repeated structures, use `$defs` to define reusable components:

<img src="https://mintcdn.com/promptlayer/-9Egue1V4AlXBy8b/images/defs.png?fit=max&auto=format&n=-9Egue1V4AlXBy8b&q=85&s=308db576ca16f5aa77ca1ef493a18694" alt="Schema Definitions Editor" data-og-width="2398" width="2398" data-og-height="1746" height="1746" data-path="images/defs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/-9Egue1V4AlXBy8b/images/defs.png?w=280&fit=max&auto=format&n=-9Egue1V4AlXBy8b&q=85&s=5a78596f821cc5f940db7ca57cf26bac 280w, https://mintcdn.com/promptlayer/-9Egue1V4AlXBy8b/images/defs.png?w=560&fit=max&auto=format&n=-9Egue1V4AlXBy8b&q=85&s=e6b566252670d74c652e9ace1889dd9f 560w, https://mintcdn.com/promptlayer/-9Egue1V4AlXBy8b/images/defs.png?w=840&fit=max&auto=format&n=-9Egue1V4AlXBy8b&q=85&s=9054ea98e43fed4045c9906aa9252fbb 840w, https://mintcdn.com/promptlayer/-9Egue1V4AlXBy8b/images/defs.png?w=1100&fit=max&auto=format&n=-9Egue1V4AlXBy8b&q=85&s=9c052bd7a0a0bc189a5bb5e809aae593 1100w, https://mintcdn.com/promptlayer/-9Egue1V4AlXBy8b/images/defs.png?w=1650&fit=max&auto=format&n=-9Egue1V4AlXBy8b&q=85&s=4ae6e4bf4790b6d50e485606a707ab06 1650w, https://mintcdn.com/promptlayer/-9Egue1V4AlXBy8b/images/defs.png?w=2500&fit=max&auto=format&n=-9Egue1V4AlXBy8b&q=85&s=e2db5097498e92b98a7cd6e5cba685af 2500w" />

### Using \$defs in the Interactive Editor

1. Click "Add Definition" at the bottom of the schema editor
2. Name your definition (e.g., "Person", "Address")
3. Define its structure like any other object
4. Reference it using the **Select \$ref** dropdown:

<img src="https://mintcdn.com/promptlayer/ZOdPY_5CRt24K1HV/images/select_ref.png?fit=max&auto=format&n=ZOdPY_5CRt24K1HV&q=85&s=1a26ec527d143913026360e4cd9d1cf4" alt="Select $ref dropdown" data-og-width="2242" width="2242" data-og-height="706" height="706" data-path="images/select_ref.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/ZOdPY_5CRt24K1HV/images/select_ref.png?w=280&fit=max&auto=format&n=ZOdPY_5CRt24K1HV&q=85&s=b5805c1cff30241aa3753477da33bc20 280w, https://mintcdn.com/promptlayer/ZOdPY_5CRt24K1HV/images/select_ref.png?w=560&fit=max&auto=format&n=ZOdPY_5CRt24K1HV&q=85&s=99e0e4a2eb8cc14974d6a942cec1cce4 560w, https://mintcdn.com/promptlayer/ZOdPY_5CRt24K1HV/images/select_ref.png?w=840&fit=max&auto=format&n=ZOdPY_5CRt24K1HV&q=85&s=833110da5083ca362e0b7d2fda68fea2 840w, https://mintcdn.com/promptlayer/ZOdPY_5CRt24K1HV/images/select_ref.png?w=1100&fit=max&auto=format&n=ZOdPY_5CRt24K1HV&q=85&s=fb46a29b482d339d556470884ade8ff0 1100w, https://mintcdn.com/promptlayer/ZOdPY_5CRt24K1HV/images/select_ref.png?w=1650&fit=max&auto=format&n=ZOdPY_5CRt24K1HV&q=85&s=b247c69d3842844bec4f0e519de538e4 1650w, https://mintcdn.com/promptlayer/ZOdPY_5CRt24K1HV/images/select_ref.png?w=2500&fit=max&auto=format&n=ZOdPY_5CRt24K1HV&q=85&s=f5c850375e8e3e576c06238d5aab98d8 2500w" />

**Benefits:**

* Avoid duplicating complex structures
* Maintain consistency across your schema
* Easier to update common patterns

## Using Variables in Structured Outputs

You can make your schemas dynamic by using template variables:

<Note>
  Variables in structured outputs only work with Jinja2 format with the Jinja2 option enabled. F-string format isn't supported.
</Note>

### Interactive Mode

When using the interactive schema editor, you can add variables in two ways:

1. **For enum values**: Click the enum field and toggle the switch to "Use Variable"

<video controls width="100%">
  <source src="https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/videos/enum-variable.mp4?fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=8204f793ad78917e11de88062de84b46" type="video/mp4" data-path="videos/enum-variable.mp4" />

  Your browser does not support the video tag.
</video>

2. **For text/string values**: Type `{{ variable_name }}` directly in any text field

<video controls width="100%">
  <source src="https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/videos/text-variable.mp4?fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=155b80a9ca346d9469c8b09140232e6e" type="video/mp4" data-path="videos/text-variable.mp4" />

  Your browser does not support the video tag.
</video>

### JSON Mode

Variables must be in quotes, except for enum variables:

```json  theme={null}
{
  "type": "object",
  "properties": {
    "sentiment": {
      "type": "string",
      "enum": {name: "sentiment_options", type: "enum_variable"},
      "description": "The sentiment of the {{ content_type }}"
    },
    "topics": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "List of topics mentioned in the {{ document_type }}"
    }
  }
}
```

When running the prompt, provide your variables:

```python  theme={null}
response = pl.run(
   prompt_name="content_analyzer",
   input_variables={
       "text": "I really enjoyed the new restaurant downtown. The food was amazing and the service was excellent.",
       "sentiment_options": ["positive", "neutral", "negative"],
       "document_type": "review",
       "content_type": "customer feedback"
   }
)
```

### Variable Use Cases

**Dynamic validation constraints:**

```json  theme={null}
{
  "type": "object",
  "properties": {
    "username": {
      "type": "string",
      "minLength": "{{ min_username_length }}",
      "maxLength": "{{ max_username_length }}",
      "description": "Username with configurable length"
    }
  }
}
```

**Context-dependent descriptions:**

```json  theme={null}
{
  "type": "object",
  "properties": {
    "analysis": {
      "type": "string",
      "description": "Analysis of {{ document_type }} for {{ use_case }}"
    }
  }
}
```

For more information on template variables, see our [Template Variables documentation](/features/prompt-registry/template-variables).

## Dynamic Schema Injection with Variable Type

For advanced use cases, you can inject entire schema sections dynamically at runtime using the `variable` type. This allows you to define different schemas based on runtime conditions without creating multiple prompt templates.

### How It Works

1. In the schema editor, select "variable" as the type for a field
2. Specify a variable name (e.g., `userSchema`)
3. At runtime, pass the complete schema object for that variable

### Example: Dynamic User Schema

In your prompt template schema:

```json  theme={null}
{
  "type": "object",
  "properties": {
    "user_data": {
      "type": "variable",
      "name": "userSchema"
    },
    "metadata": {
      "type": "object",
      "properties": {
        "timestamp": { "type": "string" },
        "version": { "type": "string" }
      }
    }
  }
}
```

At runtime, provide the complete schema:

```python  theme={null}
response = pl.run(
   prompt_name="dynamic_processor",
   input_variables={
       "userSchema": {
           "type": "object",
           "properties": {
               "name": { "type": "string" },
               "age": { "type": "number" },
               "preferences": {
                   "type": "array",
                   "items": { "type": "string" }
               }
           },
           "required": ["name", "age"]
       }
   }
)
```

The `user_data` field will be replaced entirely with the schema you provide, allowing different structures for different use cases.

### Use Cases for Dynamic Schemas

**Multi-tenant applications:**

```python  theme={null}
# Different schema per customer
customer_schemas = {
    "enterprise": {
        "type": "object",
        "properties": {
            "company_name": { "type": "string" },
            "department": { "type": "string" },
            "employee_count": { "type": "number" }
        }
    },
    "individual": {
        "type": "object",
        "properties": {
            "name": { "type": "string" },
            "age": { "type": "number" }
        }
    }
}

response = pl.run(
    prompt_name="user_analyzer",
    input_variables={
        "userSchema": customer_schemas[customer_type]
    }
)
```

**Dynamic form processing:**

```python  theme={null}
# Schema based on form configuration
form_schema = build_schema_from_config(form_config)

response = pl.run(
    prompt_name="form_processor",
    input_variables={
        "formSchema": form_schema
    }
)
```

### Important Notes

* Variable schemas only work with Jinja2 template format
* The entire field is replaced with the provided schema object
* Ensure the injected schema is valid JSON schema syntax
* The injected schema inherits the `additionalProperties` setting from the parent

## Best Practices

* **For enum values:** Use `{name: "variable_name", type: "enum_variable"}` in JSON mode or the variable selector in interactive mode
* **For text variables:** Include them within quotes as `{{ variable_name }}` in both modes
* **For dynamic schemas:** Use `type: "variable"` with a descriptive variable name
* Only Jinja2 format works for variables in structured outputs
* Ensure all variables used in the schema are provided
* Use proper JSON formatting with variables


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.promptlayer.com/llms.txt