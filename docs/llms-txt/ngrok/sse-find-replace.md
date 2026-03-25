# Source: https://ngrok.com/docs/traffic-policy/actions/sse-find-replace.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# SSE Find & Replace Action

> Find and replace text patterns in Server-Sent Events (SSE) streams.

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

The SSE Find & Replace action enables you to modify Server-Sent Events stream content
by finding and replacing text patterns using regular expressions. This is particularly
useful for modifying streaming AI model responses in real-time, such as redacting
sensitive information or transforming content as it streams to clients.

## Configuration reference

The [Traffic Policy](/traffic-policy/) configuration reference for this action.

### Supported phases

`on_event_stream_message`

### Type

`sse-find-replace`

### Configuration fields

<ConfigField title="replacements" type="array" required={true}>
  Array of replacement rules to apply to SSE messages. Rules are applied in order.

  Minimum `1` replacement required.

  <ConfigField title="field" type="string">
    The SSE field to apply the replacement to. Valid values are `data` and `retry`.
    Defaults to `data` if not specified.
    CEL interpolation is supported.
  </ConfigField>

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

When this action executes, it processes each SSE message as it streams through ngrok,
applying replacement rules to the specified fields.

### SSE message structure

Server-Sent Events consist of messages with fields like `data`, `event`, `id`, and `retry`.
This action currently supports modifying the `data` and `retry` fields.

### Pattern matching

The `from` field accepts [RE2 regular expressions](https://github.com/google/re2/wiki/Syntax).
All matches within the specified field are replaced, not just the first occurrence.

### Streaming behavior

Unlike the request/response body find & replace actions, this action processes messages
in real-time as they stream through. Each SSE message is processed independently.

### Capture groups

You can use capture groups in your pattern and reference them in the replacement:

```yaml  theme={null}
replacements:
  - field: data
    from: '"sensitive_id":\s*"([^"]+)"'
    to: '"sensitive_id": "[REDACTED]"'
```

### CEL expressions

The `field`, `from`, and `to` parameters all support CEL interpolation for dynamic values:

```yaml  theme={null}
replacements:
  - field: "${vars.target_field}"
    from: "${vars.pattern}"
    to: "${vars.replacement}"
```

When using CEL in the `from` field, the resulting string must be a valid regular expression.

### Non-terminating action

This is a **Non-terminating action**. It does not return a response, and will allow Traffic Policy processing to continue to the next Action in the chain. All **Cloud Endpoint** Traffic Policies must end with a terminating action. This requirement does not apply to **Agent Endpoints**.

## Examples

### Redacting sensitive data from streaming AI responses

When using streaming AI responses (like OpenAI's chat completions with `stream: true`),
you can redact sensitive information in real-time.

#### Example Traffic Policy document

<CodeGroup>
  ```yaml policy.yml theme={null}
  on_event_stream_message:
    - actions:
        - type: sse-find-replace
          config:
            replacements:
              # Redact SSN patterns in streaming content
              - field: data
                from: "\\d{3}-\\d{2}-\\d{4}"
                to: "[SSN REDACTED]"
              # Redact email addresses
              - field: data
                from: "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}"
                to: "[EMAIL REDACTED]"
  ```

  ```json policy.json theme={null}
  {
    "on_event_stream_message": [
      {
        "actions": [
          {
            "type": "sse-find-replace",
            "config": {
              "replacements": [
                {
                  "field": "data",
                  "from": "\\d{3}-\\d{2}-\\d{4}",
                  "to": "[SSN REDACTED]"
                },
                {
                  "field": "data",
                  "from": "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}",
                  "to": "[EMAIL REDACTED]"
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

### Modifying streaming AI output format

Transform streaming content as it's delivered to clients:

<CodeGroup>
  ```yaml policy.yml theme={null}
  on_event_stream_message:
    - actions:
        - type: sse-find-replace
          config:
            replacements:
              # Add emphasis to certain keywords
              - field: data
                from: "\\b(IMPORTANT|WARNING|NOTE)\\b"
                to: "**$1**"
  ```

  ```json policy.json theme={null}
  {
    "on_event_stream_message": [
      {
        "actions": [
          {
            "type": "sse-find-replace",
            "config": {
              "replacements": [
                {
                  "field": "data",
                  "from": "\\b(IMPORTANT|WARNING|NOTE)\\b",
                  "to": "**$1**"
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

### Filtering profanity from streaming responses

Remove or replace inappropriate content from AI responses in real-time:

<CodeGroup>
  ```yaml policy.yml theme={null}
  on_event_stream_message:
    - actions:
        - type: sse-find-replace
          config:
            replacements:
              - field: data
                from: "\\b(badword1|badword2|badword3)\\b"
                to: "[filtered]"
  ```

  ```json policy.json theme={null}
  {
    "on_event_stream_message": [
      {
        "actions": [
          {
            "type": "sse-find-replace",
            "config": {
              "replacements": [
                {
                  "field": "data",
                  "from": "\\b(badword1|badword2|badword3)\\b",
                  "to": "[filtered]"
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

### Modifying retry behavior

Change the retry interval in SSE streams:

<CodeGroup>
  ```yaml policy.yml theme={null}
  on_event_stream_message:
    - actions:
        - type: sse-find-replace
          config:
            replacements:
              - field: retry
                from: "\\d+"
                to: "5000"
  ```

  ```json policy.json theme={null}
  {
    "on_event_stream_message": [
      {
        "actions": [
          {
            "type": "sse-find-replace",
            "config": {
              "replacements": [
                {
                  "field": "retry",
                  "from": "\\d+",
                  "to": "5000"
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

<ConfigField title="actions.ngrok.sse_find_replace.replacements" type="array">
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
* [Response Body Find & Replace](/traffic-policy/actions/response-body-find-replace) - Modify response bodies


Built with [Mintlify](https://mintlify.com).