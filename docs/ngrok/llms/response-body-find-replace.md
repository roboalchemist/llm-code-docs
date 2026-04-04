# Source: https://ngrok.com/docs/traffic-policy/actions/response-body-find-replace.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Response Body Find & Replace Action

> Find and replace text patterns in HTTP response bodies using regular expressions.

export const ConfigField = ({title, type, cel = false, defaultValue = false, required = false, children}) => {
  const id = `config-${title.replace(/\.|\s|\*/g, "_")}`;
  return <div className="field pt-2.5 pb-5 my-2.5 border-gray-50 dark:border-gray-800/50 border-b" style={{
    scrollMarginTop: '120px'
  }} id={id}>
      <div className="flex font-mono group/param-head param-head break-all relative">
        <div className="flex-1 flex content-start py-0.5 mr-5">
          <div className="flex items-center flex-wrap gap-2">
            <div class="absolute -top-1.5">
              <a href={`#${id}`} className="-ml-10 flex items-center opacity-0 border-0 group-hover/param-head:opacity-100 py-2 [.expandable-content_&]:-ml-[2.1rem]" aria-label="Navigate to header">
                ​<div className="w-6 h-6 rounded-md flex items-center justify-center shadow-sm text-gray-400 dark:text-white/50 dark:bg-background-dark dark:brightness-[1.35] dark:ring-1 dark:hover::rightness-150 bg-white ring-1 ring-gray-400/30 dark:ring-gray-700/25 hover:ring-gray-400/60 dark:hover:ring-white/20">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="gray" height="12px" viewBox="0 0 576 512"><path d="M0 256C0 167.6 71.6 96 160 96h72c13.3 0 24 10.7 24 24s-10.7 24-24 24H160C98.1 144 48 194.1 48 256s50.1 112 112 112h72c13.3 0 24 10.7 24 24s-10.7 24-24 24H160C71.6 416 0 344.4 0 256zm576 0c0 88.4-71.6 160-160 160H344c-13.3 0-24-10.7-24-24s10.7-24 24-24h72c61.9 0 112-50.1 112-112s-50.1-112-112-112H344c-13.3 0-24-10.7-24-24s10.7-24 24-24h72c88.4 0 160 71.6 160 160zM184 232H392c13.3 0 24 10.7 24 24s-10.7 24-24 24H184c-13.3 0-24-10.7-24-24s10.7-24 24-24z"></path></svg>
                </div>
              </a>
            </div>
            <div className="font-semibold text-primary dark:text-primary-light overflow-wrap-anywhere">{title}</div>
            <div className="inline items-center gap-2 text-xs font-medium [&_div]:inline [&_div]:mr-2 [&_div]:leading-5 [&_a]:inline [&_a]:mr-2 [&_a]:leading-5">
              {type && <div className="flex items-center px-2 py-0.5 rounded-md bg-gray-100/50 dark:bg-white/5 break-all">
                <span className="text-gray-600 dark:text-gray-200 !font-medium">{type}</span>
              </div>}
              {defaultValue && <div className="flex items-center px-2 py-0.5 rounded-md bg-gray-100/50 dark:bg-white/5 break-all">
                  <span class="text-gray-400 dark:text-gray-500">default:</span>
                  <span className="text-gray-600 dark:text-gray-200 !font-medium">{defaultValue}</span>
                </div>}
              {required && <div className="px-2 py-0.5 rounded-md bg-red-100/50 dark:bg-red-400/10 whitespace-nowrap">
                <span className="text-red-600 dark:text-red-300 !font-medium">Required</span>
              </div>}
              {cel && <a className="px-2 py-0.5 rounded-md !border-none bg-blue-100/50 dark:bg-blue-400/10 whitespace-nowrap" href="/traffic-policy/concepts/cel-interpolation">
                <span className="text-blue-600 dark:text-blue-300 !font-medium">Supports CEL</span>
              </a>}
            </div>
          </div>
        </div>
      </div>
      <div className="mt-4 prose-sm prose-gray dark:prose-invert [&_.prose>p:first-child]:mt-0 [&_.prose>p:last-child]:mb-0">
        {children}
      </div>
    </div>;
};

The Response Body Find & Replace action enables you to modify HTTP response body content
by finding and replacing text patterns using regular expressions. This is useful for
redacting sensitive information in responses, transforming data formats, or modifying
AI model outputs before they reach clients.

## Configuration reference

The [Traffic Policy](/traffic-policy/) configuration reference for this action.

### Supported phases

`on_http_response`

### Type

`response-body-find-replace`

### Configuration fields

<ConfigField title="replacements" type="array" required={true}>
  Array of replacement rules to apply to the response body. Rules are applied in order.

  Minimum `1` replacement required.

  <ConfigField title="from" type="string" required={true} cel={true}>
    Regular expression pattern to match. Supports [RE2 syntax](https://github.com/google/re2/wiki/Syntax).
    CEL interpolation is supported for dynamic patterns.
  </ConfigField>

  <ConfigField title="to" type="string" cel={true}>
    Replacement string. Use `$1`, `$2`, etc. to reference capture groups from the pattern.
    CEL interpolation is supported for dynamic replacements.
    If omitted or empty, matched text is deleted.
  </ConfigField>
</ConfigField>

## Behavior

When this action executes, it buffers the entire response body, applies all replacement
rules in order, and updates the `Content-Length` header if present.

### Pattern matching

The `from` field accepts [RE2 regular expressions](https://github.com/google/re2/wiki/Syntax).
All matches in the body are replaced, not just the first occurrence.

### Capture groups

You can use capture groups in your pattern and reference them in the replacement:

```yaml  theme={null}
replacements:
  - from: "error_code: ([0-9]+)"
    to: "error_code: HIDDEN"
```

### CEL expressions

Both `from` and `to` fields support CEL interpolation for dynamic values:

```yaml  theme={null}
replacements:
  - from: "${vars.sensitive_pattern}"
    to: "[REDACTED by ${req.headers['x-request-id']}]"
```

When using CEL in the `from` field, the resulting string must be a valid regular expression.

### Content-Length handling

After replacements are applied, the action automatically updates the `Content-Length`
header to reflect the new body size.

### Ordering

Replacement rules are applied in the order they are specified. Later rules operate
on the result of earlier rules.

### Non-terminating action

This is a **Non-terminating action**. It does not return a response, and will allow Traffic Policy processing to continue to the next Action in the chain. All **Cloud Endpoint** Traffic Policies must end with a terminating action. This requirement does not apply to **Agent Endpoints**.

## Examples

### Redacting sensitive data from AI responses

The following configuration redacts personal information from AI model responses.

#### Example Traffic Policy document

<CodeGroup>
  ```yaml policy.yml theme={null}
  on_http_response:
    - actions:
        - type: response-body-find-replace
          config:
            replacements:
              # Redact SSN patterns
              - from: "\\b\\d{3}-\\d{2}-\\d{4}\\b"
                to: "[SSN REDACTED]"
              # Redact credit card numbers
              - from: "\\b\\d{4}[- ]?\\d{4}[- ]?\\d{4}[- ]?\\d{4}\\b"
                to: "[CARD REDACTED]"
              # Redact phone numbers
              - from: "\\b\\d{3}[-.\\s]?\\d{3}[-.\\s]?\\d{4}\\b"
                to: "[PHONE REDACTED]"
  ```

  ```json policy.json theme={null}
  {
    "on_http_response": [
      {
        "actions": [
          {
            "type": "response-body-find-replace",
            "config": {
              "replacements": [
                {
                  "from": "\\b\\d{3}-\\d{2}-\\d{4}\\b",
                  "to": "[SSN REDACTED]"
                },
                {
                  "from": "\\b\\d{4}[- ]?\\d{4}[- ]?\\d{4}[- ]?\\d{4}\\b",
                  "to": "[CARD REDACTED]"
                },
                {
                  "from": "\\b\\d{3}[-.\\s]?\\d{3}[-.\\s]?\\d{4}\\b",
                  "to": "[PHONE REDACTED]"
                }
              ]
            }
          }
        ]
      }
    ]
  }
  ```
</CodeGroup>

#### Example response

Before (original response body):

```text  theme={null}
Here's the customer information:
- SSN: 123-45-6789
- Credit Card: 4111-1111-1111-1111
- Phone: 555-123-4567
```

After (modified response body):

```text  theme={null}
Here's the customer information:
- SSN: [SSN REDACTED]
- Credit Card: [CARD REDACTED]
- Phone: [PHONE REDACTED]
```

### Adding disclaimers to AI responses

Append legal disclaimers or warnings to AI-generated content:

<CodeGroup>
  ```yaml policy.yml theme={null}
  on_http_response:
    - expressions:
        - "res.headers['content-type'].contains('application/json')"
      actions:
        - type: response-body-find-replace
          config:
            replacements:
              - from: '"content":\s*"([^"]*)"(\s*})'
                to: '"content": "$1\n\n---\nDisclaimer: This response was generated by AI and may contain errors."$2'
  ```

  ```json policy.json theme={null}
  {
    "on_http_response": [
      {
        "expressions": [
          "res.headers['content-type'].contains('application/json')"
        ],
        "actions": [
          {
            "type": "response-body-find-replace",
            "config": {
              "replacements": [
                {
                  "from": "\"content\":\\s*\"([^\"]*)\"(\\s*})",
                  "to": "\"content\": \"$1\\n\\n---\\nDisclaimer: This response was generated by AI and may contain errors.\"$2"
                }
              ]
            }
          }
        ]
      }
    ]
  }
  ```
</CodeGroup>

### Sanitizing error messages

Remove internal error details from responses before sending to clients:

<CodeGroup>
  ```yaml policy.yml theme={null}
  on_http_response:
    - expressions:
        - "res.status_code >= 500"
      actions:
        - type: response-body-find-replace
          config:
            replacements:
              - from: '"stack_trace":\s*"[^"]*"'
                to: '"stack_trace": "[HIDDEN]"'
              - from: '"internal_error":\s*"[^"]*"'
                to: '"internal_error": "[HIDDEN]"'
  ```

  ```json policy.json theme={null}
  {
    "on_http_response": [
      {
        "expressions": [
          "res.status_code >= 500"
        ],
        "actions": [
          {
            "type": "response-body-find-replace",
            "config": {
              "replacements": [
                {
                  "from": "\"stack_trace\":\\s*\"[^\"]*\"",
                  "to": "\"stack_trace\": \"[HIDDEN]\""
                },
                {
                  "from": "\"internal_error\":\\s*\"[^\"]*\"",
                  "to": "\"internal_error\": \"[HIDDEN]\""
                }
              ]
            }
          }
        ]
      }
    ]
  }
  ```
</CodeGroup>

## Action result variables

The following variables are made available for use in subsequent expressions and
CEL interpolations after the action has run. Variable values will only apply
to the last action execution, results are not concatenated.

<ConfigField title="actions.ngrok.response_body_find_replace.replacements" type="array">
  Array of objects describing which replacement rules matched.

  <ConfigField title="replacement_index" type="integer">
    The zero-based index of the replacement rule that matched.
  </ConfigField>

  <ConfigField title="matched_content" type="string">
    The first matched content from this replacement rule.
  </ConfigField>
</ConfigField>

## Related actions

* [Request Body Find & Replace](/traffic-policy/actions/request-body-find-replace) - Modify request bodies
* [SSE Find & Replace](/traffic-policy/actions/sse-find-replace) - Modify Server-Sent Events streams


Built with [Mintlify](https://mintlify.com).