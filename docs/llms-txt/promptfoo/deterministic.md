# Source: https://www.promptfoo.dev/docs/configuration/expected-outputs/deterministic/

# Deterministic Metrics for LLM Output Validation

These metrics are created by logical tests that are run on LLM output.

| Assertion Type | Returns true if... |
| --- | --- |
| [assert-set](#assert-set) | A configurable threshold of grouped assertions pass |
| [classifier](#classifier) | HuggingFace classifier returns expected class above threshold |
| [contains](#contains) | output contains substring |
| [contains-all](#contains-all) | output contains all list of substrings |
| [contains-any](#contains-any) | output contains any of the listed substrings |
| [contains-json](#contains-json) | output contains valid JSON (optional JSON schema validation) |
| [contains-html](#contains-html) | output contains HTML content |
| [contains-sql](#contains-sql) | output contains valid SQL |
| [contains-xml](#contains-xml) | output contains valid XML |
| [cost](#cost) | Inference cost is below a threshold |
| [equals](#equality) | output matches exactly |
| [f-score](#f-score) | F-score is above a threshold |
| [finish-reason](#finish-reason) | model stopped for the expected reason |
| [icontains](#icontains) | output contains substring, case insensitive |
| [icontains-all](#icontains-all) | output contains all list of substrings, case insensitive |
| [icontains-any](#icontains-any) | output contains any of the listed substrings, case insensitive |
| [is-html](#is-html) | output is valid HTML |
| [is-json](#is-json) | output is valid JSON (optional JSON schema validation) |
| [is-sql](#is-sql) | output is valid SQL |
| [is-valid-function-call](#is-valid-function-call) | Ensure that any JSON LLM output adheres to the schema specified in the `functions` configuration of the provider. This is implemented for a subset of providers. Learn more about the [Google Vertex provider](/docs/providers/vertex/#function-calling-and-tools), [Google AIStudio provider](/docs/providers/google/#function-calling), [Google Live provider](/docs/providers/google/#function-calling-example), and [OpenAI provider](/docs/providers/openai/#using-tools-and-functions). |
| [tool-call-f1](#tool-call-f1) | The `tool-call-f1` assertion computes the F1 score comparing the set of tool calls by the LLM with an expected set of tool calls. This metric is useful for evaluating agentic LLM applications where you want to measure how accurately the model selects the right tools. |
| [javascript](#javascript) | See [JavaScript assertions](/docs/configuration/expected-outputs/javascript/) |
| [latency](#latency) | Checks if span durations in a trace that match a given pattern are within acceptable limits. |
| [trace-span-count](#trace-span-count) | Checks if at least one LLM call was made. |
| [trace-span-duration](#trace-span-duration) | Checks if span durations in a trace are within acceptable limits. |
| [trace-error-spans](#trace-error-spans) | Detects error spans in a trace and ensures the error rate is within acceptable limits. |
| [webhook](#webhook) | Sends the LLM output to a specified webhook URL for custom validation. |
| [rouge-n](#rouge-n) | Checks if the Rouge-N score between the LLM output and expected value is above a given threshold. |
| [bleu](#bleu) | Checks if the BLEU score between the LLM output and expected value is above a given threshold. |
| [gleu](#gleu) | Checks if the GLEU score between the LLM output and expected value is above a given threshold. |
| [meteor](#meteor) | Checks if the METEOR score between the LLM output and expected value is above a given threshold. |
| [f-score](#f-score) | F-score (also F1 score) is used for measuring classification accuracy when you need to balance between being correct and being complete. |
| [finish-reason](#finish-reason) | Checks if the model stopped generating for the expected reason. |
| [is-refusal](#is-refusal) | Checks if the LLM output indicates that the model refused to perform the requested task. |
| [similar](#similar) | Checks if the LLM output is semantically similar to the expected value using embedding similarity. |
| [pi](#pi) | Uses Pi Labs' preference scoring model as an alternative to LLM-as-a-judge for evaluation. |
| [classifier](#classifier) | Runs the LLM output through any HuggingFace text classification model. |
| [assert-set](#assert-set) | Groups multiple assertions together with configurable success criteria. |
| [select-best](#select-best) | Compares multiple outputs in the same test case and selects the best one. |

## See Also

- [JavaScript Assertions](/docs/configuration/expected-outputs/javascript/) - Using custom JavaScript functions for validation
- [Python Assertions](/docs/configuration/expected-outputs/python/) - Using custom Python functions for validation
- [Model-Graded Metrics](/docs/configuration/expected-outputs/model-graded/) - Using LLMs to evaluate other LLMs
- [Configuration Reference](/docs/configuration/reference/) - Complete configuration options
- [Guardrails](/docs/configuration/expected-outputs/guardrails/) - Setting up safety guardrails for LLM outputs