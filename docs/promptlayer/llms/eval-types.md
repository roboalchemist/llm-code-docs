# Source: https://docs.promptlayer.com/features/evaluations/eval-types.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.promptlayer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Eval Types

This page provides an overview of the various evaluation column types available on our platform.

## Primary Types

<img width="450" src="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/prompt-template-eval.png?fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=07caec32568283a87b1c4655fcaf8a7b" data-og-width="1420" data-og-height="1014" data-path="images/prompt-template-eval.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/prompt-template-eval.png?w=280&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=ab17403bdb0bee76a52dacfb6bc3ad0c 280w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/prompt-template-eval.png?w=560&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=552339a61cbc5b2b2fe2eaba622d18c7 560w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/prompt-template-eval.png?w=840&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=6e4f439f5183a137e08c5332404ae5cc 840w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/prompt-template-eval.png?w=1100&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=26e7a998eab2feaffb7e543a4d891a50 1100w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/prompt-template-eval.png?w=1650&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=ff662620bdd87311e8975a449c8d1e4b 1650w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/prompt-template-eval.png?w=2500&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=0878c3a9da469c03c5fe80f8ebeb8c38 2500w" />

### Prompt Template

The *Prompt Template* evaluation type allows you to execute a prompt template from the Prompt Registry. You have the flexibility to select the latest version, a specific label, or a particular version of the prompt template. You also have the ability to assign the input variables based on available inputs from the dataset or other columns. You can override the model parameters that are set in the Prompt Registry. This functionality is particularly useful for testing a prompt template within a larger evaluation pipeline, comparing different model parameters, or implementing an "LLM as a judge" prompt template.

### Custom API Endpoint

The *Custom API Endpoint* enables you to set up a webhook that our system will call (POST) with all the columns to the left of the API endpoint when that cell is executed. As cells are processed sequentially, we will call this endpoint with all the columns to the left as the given payload, and the returned result will be displayed. This feature allows for extensive customization to accommodate specific use cases and integrate with external systems or custom evaluators.

The payload will be in the form of

```json  theme={null}
    {
        data: {
            "column1": "value1",
            "column2": "value2",
            "column3": "value3",
            ...
        }
    }
```

### MCP

The *MCP Action* allows you to run functions on a remote MCP server. Simply plug in your server URL and auth, select your function and you will be able to call your function with inputs mapped from other cells. For more information about MCP check out [the official MCP docs.](https://modelcontextprotocol.io/introduction)

### Human Input

The *Human Input* evaluation type allows the addition of either numeric or text input where an evaluator can provide feedback via a slider or a text box. This input can then be utilized in subsequent columns in the evaluation pipeline, allowing for the incorporation of human judgment.

### Code Execution

The *Code Execution* evaluation type allows you to write and execute code for each row in your dataset. You can access the data through the `data` variable and return the cell value. Note that stdout will be ignored. There is a `6 minute timeout` for code execution.

Code example to return a list of the names of each column:

<CodeGroup>
  ```py Python theme={null}
  message = "These are my column names: "
  columns = [column_name for column_name in data.keys()]
  return message + str(columns)
  ```

  ```js JavaScript theme={null}
  const message = "These are my column names: ";
  const columns = Object.keys(data);
  return message + JSON.stringify(columns);
  ```
</CodeGroup>

**Python Runtime**

```
The Python runtime runs Python 3.12.0 with no filesystem. Runtime does have network access. Only the standard library is available. Here are the resource quotas:

- Input code size: 1MiB
- Size of stdin: 10MiB
- Size of stdout: 20MiB
- Size of stderr: 10MiB
- Number of environment variables: 100
- Environment variable key size: 4KiB
- Environment variable value size: 100KiB
- Number of arguments: 100
- Argument size: 100KiB
- Memory consumption: 128MiB
```

**JavaScript Runtime**

```
The JavaScript runtime is built on Mozilla's SpiderMonkey engine with no filesystem. Runtime does have network access. It is not node or deno. Available APIs include:

- Legacy Encoding: atob, btoa, decodeURI, encodeURI, decodeURIComponent, encodeURIComponent
- Streams: ReadableStream, ReadableStreamBYOBReader, ReadableStreamBYOBRequest, ReadableStreamDefaultReader, ReadableStreamDefaultController, ReadableByteStreamController, WritableStream, ByteLengthQueuingStrategy, CountQueuingStrategy, TransformStream
- URL: URL, URLSearchParams
- Console: console
- Performance: Performance
- Task: queueMicrotask, setInterval, setTimeout, clearInterval, clearTimeout
- Location: WorkerLocation, location
- JSON: JSON
- Encoding: TextEncoder, TextDecoder, CompressionStream, DecompressionStream
- Structured Clone: structuredClone
- Fetch: fetch, Request, Response, Headers
- Crypto: SubtleCrypto, Crypto, crypto, CryptoKey

Resource Quotas:

- Input code size: 1MiB
- Size of stdin: 10MiB
- Size of stdout: 20MiB
- Size of stderr: 10MiB
- Number of environment variables: 100
- Environment variable key size: 4KiB
- Environment variable value size: 100KiB
- Number of arguments: 100
- Argument size: 100KiB
- Memory consumption: 128MiB
```

### Coding Agent

The *Coding Agent* evaluation type uses an AI coding agent (such as [Claude Code](https://www.claude.com/product/claude-code)) in a secure, sandboxed environment for each row in your dataset. Instead of writing code directly, you provide natural language instructions describing what you want to accomplish, and the AI coding agent handles the implementation.

**How it works:**

You provide a **natural language prompt** describing the task you want to accomplish. The coding agent executes in an isolated sandbox with access to:

* **variables.json** - Automatically injected file containing all column values from previous cells in that row
* **File attachments** - Any files you upload (CSV, JSON, text files, etc.) are available in the sandbox
* **Network access** - Can make API calls and fetch external data

The agent returns the result which populates the cell for that row.

**Example use cases:**

* **Data transformation**: "Parse the JSON response from the API column and extract all user emails into a comma-separated list"
* **File processing**: "Read the attached sales\_data.csv and calculate the total revenue for products in the 'Electronics' category"
* **API integration**: "Use the api\_key from variables.json to fetch user details from [https://api.example.com/users/\{user\_id}](https://api.example.com/users/\{user_id}) and return their account status"

### Conversation Simulator

The *Conversation Simulator* evaluation type automates the back-and-forth between your AI agent and simulated users to test conversational AI performance. This is particularly useful for evaluating multi-turn conversations where context maintenance, goal achievement, and user interaction patterns are critical.

When setting up the conversation simulator:

* Select your AI agent prompt template from the Prompt Registry
* Pass in user details or context variables from your dataset
* Define a test persona that challenges your AI with specific behaviors or constraints

**Example Test Persona:**

```
User is nervous about seeing the doctor, hasn't been in a long time, 
won't share phone number until asked three times for it
```

**Optional Advanced Configuration:**

* **User Goes First**: By default, the AI agent initiates the conversation. You can enable this setting to have the simulated user start the conversation instead.

* **Conversation Samples**: You can provide sample conversations to help guide the simulated user's responses. These samples help maintain consistent voice and interaction patterns, ensuring the simulated user behaves realistically and consistently with your expected user base.

* **Completion Guidance**: Define specific conditions for when the conversation should be considered complete. This is useful for specifying end conditions like tool calls, confirmation messages, or goal achievement (e.g., "End when the assistant calls the submit\_order tool" or "Complete when the user confirms their booking"). You can provide this as a static value or pull it from a dataset column for varied test scenarios.

The conversation results are returned as a JSON list of messages that can then be evaluated using other eval types like LLM Assertions to assess success criteria.

## Simple Evals

<img width="450" src="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/equality-comparison-eval.png?fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=5a3cebcb251c5ef3ae52ed30fa46dc25" data-og-width="1374" data-og-height="1200" data-path="images/equality-comparison-eval.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/equality-comparison-eval.png?w=280&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=0444139c009835ef403b14d0b5bbfe75 280w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/equality-comparison-eval.png?w=560&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=5f9098427b72afc6423d9bddfe98f4e3 560w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/equality-comparison-eval.png?w=840&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=ba2e421e59ab6b08fb1ebbf81e2ceb81 840w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/equality-comparison-eval.png?w=1100&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=5711b8acc659175dcec6febed2e4e0a1 1100w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/equality-comparison-eval.png?w=1650&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=f35229c734cd07bbcb98a8c0dc58bb42 1650w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/equality-comparison-eval.png?w=2500&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=1216baddef957c7d3d8e5a1c12a1d5a5 2500w" />

### Equality Comparison

*Equality Comparison* allows you to compare two different columns as strings. It provides a visual diff if there is a difference between the columns. Note that the diff is not used when calculating the score in that column and the column will be treated as a boolean for the purposes of a score. If there is no difference, it this column return true.

### Contains Value

The *Contains* evaluation type enables you to search for a substring within a column. For instance, you could search for a specific word or phrase within each cell in the column. It is using the python `in` operator to check if the substring is in the cell and is case insensitive.

### Regex Match

The *Regex Match* evaluation type allows you to define a regular expression pattern to search within the column. This provides powerful pattern matching capabilities for complex text analysis tasks.

### Absolute Numeric Distance

The *Absolute Numeric Distance* evaluation type allows you to select two different columns and output the absolute distance between their numeric values in a new column. Both source columns must contain numeric values.

## LLM Evals

<img width="450" src="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/llm-assertion-eval.png?fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=976456d46264b25a382f0f64af731df0" data-og-width="1438" data-og-height="1136" data-path="images/llm-assertion-eval.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/llm-assertion-eval.png?w=280&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=0c745517bed39fc0a164bf82b633fee1 280w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/llm-assertion-eval.png?w=560&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=76fe081c9d4a536734a92fff626a7911 560w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/llm-assertion-eval.png?w=840&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=0ab17c0056aa3f0d78e6cab28801a28a 840w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/llm-assertion-eval.png?w=1100&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=69700d8b72a6350d418d0b10f2a68d9a 1100w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/llm-assertion-eval.png?w=1650&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=cff08cf51793a510cd2ccbb952fe2302 1650w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/llm-assertion-eval.png?w=2500&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=b57ab6fab588583dcb25f07614518805 2500w" />

### Run LLM Assertion

The *LLM Assertion* evaluation type enables you to run an assertion on a column using natural language prompts. You can create prompts such as "Does this contain an API key?", "Is this sensitive content?", or "Is this in English?". Our system uses a backend prompt template that processes your assertion and returns either true or false. Assertions should be framed as questions.

#### Using Template Variables

You can use template variables in your assertions to reference values from other dataset columns. This allows you to create dynamic assertions that adapt based on your data.

Use f-string style syntax with single curly braces: `{variable_name}`

**Example assertions with variables:**

* `"Is the response written in {language}?"`
* `"Does the output discuss {topic}?"`
* `"Is the tone {expected_tone}?"`

When you include variables in your assertion, a mapping interface will appear allowing you to connect each variable to a dataset column. For example, if your assertion is `"Is the response written in {language}?"` and you have a column called `target_language`, you would map `language` → `target_language`.

<Note>
  All variables used in assertions must be mapped to a column. If a variable is not mapped, the evaluation will fail with an error indicating which variable mapping is missing.
</Note>

#### Multiple Assertions

You can add multiple assertions to evaluate different criteria on the same data source. Each assertion is evaluated independently and returns its own true/false result.

### AI Data Extract

The *AI Data Extract* evaluation type uses AI/LLM to extract specific information from data sources. You can describe what you want to extract using natural language queries, whether the content is JSON, XML, or just unstructured text.

Example queries:

* "Extract the product name"
* "Find the customer's email address"
* "Get all mentioned dates"
* "Extract the total price including tax"

### Cosine Similarity

*Cosine Similarity* allows you to compare the vector distance between two columns. The system takes the two columns you supply, converts them into strings, and then embeds them using OpenAI's embedding vectors. It then calculates the cosine similarity, resulting in a number between 0 and 1. This metric is useful for understanding how semantically similar two bodies of text are, which can be valuable in assessing topic adherence or content similarity.

## Helper Functions

<img width="450" src="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/json-extraction-eval.png?fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=361302cfa496153398978f57d0fe3616" data-og-width="1436" data-og-height="1186" data-path="images/json-extraction-eval.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/json-extraction-eval.png?w=280&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=b9cd5e96a623945c9f5f1b5cc420277a 280w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/json-extraction-eval.png?w=560&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=bb4e96cd5503e0b98e501555e53cfc12 560w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/json-extraction-eval.png?w=840&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=cbdb169b93b3b0405655dc9c2e1a219e 840w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/json-extraction-eval.png?w=1100&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=6a9edc0ff841f755d42bda0ad7805ec9 1100w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/json-extraction-eval.png?w=1650&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=9364d1ee413d052a437b8084823dca69 1650w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/json-extraction-eval.png?w=2500&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=741eb4bbbeddb1ef28ce09ad76485c64 2500w" />

### JSON Extraction

The *JSON Extraction* evaluation type allows you to define a JSON path and extract either the first match or all matches in that path. We will automatically cast the source column into a JSON object. This is particularly useful for parsing structured data within your evaluations.

### Parse Value

The *Parse Value* column type enables you to convert another column into one of the following value types: string, number, Boolean, or JSON.

### Apply Diff

The *Apply Diff* evaluation type applies diff patches to original content, similar to git merge operations. This helper function requires two source columns: the original content and a diff patch to apply.

This evaluation type is particularly powerful when combined with code generation workflows or document editing pipelines where AI agents generate incremental changes rather than complete replacements. It enables sophisticated multi-step workflows where agents can review and refine each other's outputs.

Using diff formats often saves context and leads to better results for editing large content.

**Diff Format Details**

The diff patch must be in the standard **unified diff** format, including file headers and hunk headers, as used by tools like `git` and described in the [unidiff documentation](https://pypi.org/project/unidiff/).

If you are using an LLM to generate the diffs, copy and paste the following text into your prompt for format specifics:

```markdown  theme={null}
## Unified Diff Specification (strict unidiff)

Produce a valid **unified diff** with file headers and hunk headers. Only modifications of existing text are supported (no file creation or deletion).

### File headers (required)
- Old (source):  \`--- a/<filename>\`
- New (target):  \`+++ b/<filename>\`
- Use consistent prefixes \`a/\` and \`b/\`.

### Hunk headers (required for every changed region)
- Format: \`@@ -<start_old>,<len_old> +<start_new>,<len_new> @@\`
  - \`<start_old>\` / \`<start_new>\` are 1-based line numbers.
  - \`<len_old>\` / \`<len_new>\` are the line counts for the hunk in old/new.
  - Multiple hunks per file are allowed; order them top-to-bottom.

### Hunk body line prefixes (strict)
- \`' '\` (space)  = unchanged context line
- \`-\`          = line removed from source
- \`+\`          = line added in target
- Preserve original whitespace and line endings exactly.

### Rules
- The concatenation of all **context + removed** lines in each hunk must appear **verbatim and contiguously** in the source file.
- Keep context minimal but sufficient for unambiguous matching (usually 1-3 lines around changes).
- Multiple files may be patched in one diff, but each requires its own \`---\` / \`+++\` headers and hunks.
- If no changes are needed, output an empty string (no diff).

### Example
--- a/essay.txt
+++ b/essay.txt
@@ -1,4 +1,4 @@
 This is a simple essay.
-It has a bad sentence.
+It has a better sentence.
 The end.`}
          title="Copy diff specification"
        />
      </div>
    ),
    render: HelperFunctionBlocks.ApplyDiffBlock,
    weight: 5,
  },
};
```

### Static Value

The *Static Value* evaluation type allows you to pre-populate a column with a specific value. This is useful for adding constant values or context that you may need to use later in one of the other columns in your evaluation pipeline.

### Type Validation

*Type Validation* returns a boolean for the given source column if it fits one of the specified types. The types supported for validation are JSON, number, or SQL. It will return `true` if the value is valid for the specified type, and `false` otherwise. For SQL validation, the system utilizes the [SQLGlot library](https://github.com/tobymao/sqlglot?tab=readme-ov-file#parser-errors).

### Coalesce

The *Coalesce* evaluation type allows you to take multiple different columns and coalesce them, similar to [SQL's COALESCE function](https://www.w3schools.com/sql/func_sqlserver_coalesce.asp).

### Count

The *Count* evaluation type allows you to select a source column and count either the characters, words, or paragraphs within it. This will output a numeric value, which can be useful for analyzing the length or complexity of LLM outputs.

Please reach out to us if you have any other evaluation types you would like to see on the platform. We are always looking to expand our evaluation capabilities to better serve your needs.
