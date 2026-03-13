# Source: https://ngrok.com/docs/traffic-policy/actions/set-vars.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Set Vars Action

> Define or update global variables in a Traffic Policy's runtime context.

export const ConfigChildren = ({children}) => {
  return <Accordion title="Show Child Properties">
      {children}
    </Accordion>;
};

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

The **Set Vars** action is used to define or update global variables in a
Traffic Policy's runtime context. Subsequent actions or expressions can
reference these variables for conditional logic through expressions or
dynamic interpolation.

## Configuration reference

This is the [Traffic Policy](/traffic-policy/) configuration
reference for this action.

### Supported phases

`on_http_request`, `on_http_response`, `on_tcp_connect`

### Type

`set-vars`

### Configuration fields

<ConfigField title="vars" type="array of map[string]any" required={true}>
  List of maps that have a key of string and a value of any valid CEL type

  <Note>
    Each map must be of exactly size `1`, and represents one variable where the
    key is the name of the variable:

    ```yaml  theme={null}
    vars:
      - variable_a: value
      - variable_b: value
    ```
  </Note>
</ConfigField>

## Behavior

The `set-vars` action allows you to define your own global variables to be used in future actions or expressions, like this:

<CodeGroup>
  ```yaml policy.yml {6-7, 14} theme={null}
  on_http_request:
    - actions:
        - type: set-vars
          config:
            vars:
              - variable_a: Hello,
              - variable_b: World!
    - actions:
        - type: custom-response
          config:
            status_code: 200
            headers:
              content-type: text/plain
            body: ${vars.variable_a} ${vars.variable_b}
  ```

  ```json policy.json {10,13,29} theme={null}
  {
    "on_http_request": [
      {
        "actions": [
          {
            "type": "set-vars",
            "config": {
              "vars": [
                {
                  "variable_a": "Hello,"
                },
                {
                  "variable_b": "World!"
                }
              ]
            }
          }
        ]
      },
      {
        "actions": [
          {
            "type": "custom-response",
            "config": {
              "status_code": 200,
              "headers": {
                "content-type": "text/plain"
              },
              "body": "${vars.variable_a} ${vars.variable_b}"
            }
          }
        ]
      }
    ]
  }
  ```
</CodeGroup>

After being defined through the `set-vars` action, you can access them through CEL Interpolation or anywhere else that CEL is supported, like expressions.

<Note>
  You can use any valid CEL type as a variable value, including strings, booleans, doubles, null, maps, and lists.
</Note>

### CEL interpolation

Variables also support CEL interpolation (`${<expression>}`) in values,
enabling you to create dynamic values and types:

<CodeGroup>
  ```yaml policy.yml {6} theme={null}
  on_http_request:
    - actions:
        - type: set-vars
          config:
            vars:
              - message: Your IP is ${conn.client_ip}!
  ```

  ```json policy.json {10} theme={null}
  {
    "on_http_request": [
      {
        "actions": [
          {
            "type": "set-vars",
            "config": {
              "vars": [
                {
                  "message": "Your IP is ${conn.client_ip}!"
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

CEL-interpolated strings that are exactly of the form `"${vars.<name>}"` will resolve to the evaluated type.

Strings that contain CEL-interpolated substrings within them such as `sample ${conn.tls.client.pem} here` will convert all CEL-interpolated substrings to strings

### Scoping

Variables you define in the `set-vars` action are scoped to the Traffic Policy
and are not accessible outside of it.

Variables defined in each of the three phases
(`on_http_request`, `on_http_response`, `on_tcp_connect`) are scoped to that
phase, and cannot be accessed in other phases.

### Referencing other variables and macros

CEL-interpolated strings may reference all other variables and macros available
to Traffic Policies. This also includes variables previously defined in the
same or previous `set-vars` actions. This allows for powerful dynamic behavior
and customization of your Traffic Policy.

### Non-terminating action

This is a **Non-terminating action**. It does not return a response, and will allow Traffic Policy processing to continue to the next Action in the chain. All **Cloud Endpoint** Traffic Policies must end with a terminating action. This requirement does not apply to **Agent Endpoints**.

## Examples

### Basic example

The following [Traffic Policy](/traffic-policy/) configuration is an example configuration of the `set-vars` action.

#### Example Traffic Policy document

<CodeGroup>
  ```yaml policy.yml theme={null}
  on_http_request:
    - actions:
        - type: set-vars
          config:
            vars:
              - sample_string: bar
              - sample_double: 1.5
              - sample_bool: true
              - sample_null: null
              - sample_list:
                  - 1
                  - 2
                  - 3
              - sample_map:
                  key: value
              - sample_nested_map:
                  key:
                    - value1
                    - value2
    - expressions:
        - vars.sample_bool == true
      actions:
        - type: custom-response
          config:
            status_code: 200
            headers:
              content-type: text/plain
            body: ${vars.sample_string} ${vars.sample_double} ${vars.sample_list[0]} ${vars.sample_map.key} ${vars.sample_nested_map.key[1]}
  ```

  ```json policy.json theme={null}
  {
    "on_http_request": [
      {
        "actions": [
          {
            "type": "set-vars",
            "config": {
              "vars": [
                {
                  "sample_string": "bar"
                },
                {
                  "sample_double": 1.5
                },
                {
                  "sample_bool": true
                },
                {
                  "sample_null": null
                },
                {
                  "sample_list": [
                    1,
                    2,
                    3
                  ]
                },
                {
                  "sample_map": {
                    "key": "value"
                  }
                },
                {
                  "sample_nested_map": {
                    "key": [
                      "value1",
                      "value2"
                    ]
                  }
                }
              ]
            }
          }
        ]
      },
      {
        "expressions": [
          "vars.sample_bool == true"
        ],
        "actions": [
          {
            "type": "custom-response",
            "config": {
              "status_code": 200,
              "headers": {
                "content-type": "text/plain"
              },
              "body": "${vars.sample_string} ${vars.sample_double} ${vars.sample_list[0]} ${vars.sample_map.key} ${vars.sample_nested_map.key[1]}"
            }
          }
        ]
      }
    ]
  }
  ```
</CodeGroup>

### CEL interpolation example

The following [Traffic Policy](/traffic-policy/) configuration is an example of using CEL-interpolation with the `set-vars` action.

#### Example Traffic Policy document

<CodeGroup>
  ```yaml policy.yml theme={null}
  on_http_request:
    - actions:
        - type: set-vars
          config:
            vars:
              - sample_string: 'x-foo header: ${request.headers[''x-foo'']}'
              - sample_uint: ${uint(1.5) + 10u}
              - sample_int: ${int(50.5)}
              - sample_map:
                  pem: ${conn.tls.client.pem}
  ```

  ```json policy.json theme={null}
  {
    "on_http_request": [
      {
        "actions": [
          {
            "type": "set-vars",
            "config": {
              "vars": [
                {
                  "sample_string": "x-foo header: ${request.headers['x-foo']}"
                },
                {
                  "sample_uint": "${uint(1.5) + 10u}"
                },
                {
                  "sample_int": "${int(50.5)}"
                },
                {
                  "sample_map": {
                    "pem": "${conn.tls.client.pem}"
                  }
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

### Setting vars based on previous vars example

The following [Traffic Policy](/traffic-policy/) configuration is an example of setting vars based on previous vars with the `set-vars` action.

Variables are determined in the order in which they are listed in the configuration list.

#### Example Traffic Policy document

<CodeGroup>
  ```yaml policy.yml {4-28} theme={null}
  on_http_request:
    - actions:
        - type: set-vars
          config:
            vars:
              - accepted_models:
                  - openai/o1
                  - openai/4o
                  - openai/4o-mini
              - models: ${actions.ngrok.http_request.res.body}
              - models: ${vars.models.filter(model, model.id in vars.accepted_models)}
              - models: ${vars.models.filter(model, model.latency < 100)}
              - models: ${vars.models.sort(x, y, x.latency < y.latency)}
  ```

  ```json policy.json theme={null}
  {
    "on_http_request": [
      {
        "actions": [
          {
            "type": "set-vars",
            "config": {
              "vars": [
                {
                  "accepted_models": [
                    "openai/o1",
                    "openai/4o",
                    "openai/4o-mini"
                  ]
                },
                {
                  "models": "${actions.ngrok.http_request.res.body}"
                },
                {
                  "models": "${vars.models.filter(model, model.id in vars.accepted_models)}"
                },
                {
                  "models": "${vars.models.filter(model, model.latency < 100)}"
                },
                {
                  "models": "${vars.models.sort(x, y, x.latency < y.latency)}"
                }
              ]
            }
          }
        ]
      }
    ]
  }
  ```

  ```json policy.json theme={null}
  {
    "on_http_request": [
      {
        "actions": [
          {
            "type": "set-vars",
            "config": {
              "vars": [
                {
                  "accepted_models": [
                    "openai/o1",
                    "openai/4o",
                    "openai/4o-mini"
                  ]
                },
                {
                  "models": "${actions.ngrok.http_request.res.body}"
                },
                {
                  "models": "${vars.models.filter(model, model.id in vars.accepted_models)}"
                },
                {
                  "models": "${vars.models.filter(model, model.latency < 100)}"
                },
                {
                  "models": "${vars.models.sort(x, y, x.latency < y.latency)}"
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


Built with [Mintlify](https://mintlify.com).