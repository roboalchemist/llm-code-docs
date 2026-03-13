# Source: https://ngrok.com/docs/traffic-policy/actions/log.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Log Action

> The Log action enables you to log metadata to ngrok's eventing system.

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

The **Log** Traffic Policy action enables you to leverage ngrok's
[eventing system](/obs) to introduce observability into your Traffic Policy
documents.

## Configuration reference

The [Traffic Policy](/traffic-policy/) configuration
reference for this action.

### Supported phases

* `on_tcp_connect`
* `on_http_request`
* `on_http_response`

### Action type

`log`

### Configuration fields

<ConfigField title="metadata" type="map[string]any" required={true} cel={true}>
  A key-value map of metadata that you would like to include in your events
  for this action.
</ConfigField>

## Behavior

<Tabs>
  <Tab title="on_tcp_connect" label="on_tcp_connect">
    ### Event logs

    When this action is executed, the specified metadata will be collected on the
    [tcp\_connection\_closed.v0](/obs/events/reference/#tcp-connection-closedv0) event
    under the `traffic_policy.logs` key.
  </Tab>

  <Tab title="on_http_request" label="on_http_request">
    ### Event logs

    When this action is executed, the specified metadata will be collected on the
    [http\_request\_complete.v0](/obs/events/reference/#http-request-completev0) event
    under `traffic_policy.logs` key.
  </Tab>
</Tabs>

### Non-terminating action

This is a **Non-terminating action**. It does not return a response, and will allow Traffic Policy processing to continue to the next Action in the chain. All **Cloud Endpoint** Traffic Policies must end with a terminating action. This requirement does not apply to **Agent Endpoints**.

## Examples

### Logging with CEL interpolation

The following [Traffic Policy](/traffic-policy/)
configuration will log a message with the endpoint identifier for every request.

#### Example Traffic Policy document

<CodeGroup>
  ```yaml policy.yml theme={null}
  on_http_request:
    - actions:
        - type: log
          config:
            metadata:
              message: Log action executed.
              endpoint_id: ${endpoint.id}
  ```

  ```json policy.json theme={null}
  {
    "on_http_request": [
      {
        "actions": [
          {
            "type": "log",
            "config": {
              "metadata": {
                "message": "Log action executed.",
                "endpoint_id": "${endpoint.id}"
              }
            }
          }
        ]
      }
    ]
  }
  ```
</CodeGroup>

#### Example request

```bash  theme={null}
$ curl https://example.ngrok.app
```

Once the request has completed, and you have properly configured an
event destination, you should see an event appear with the following payload:

```jsx  theme={null}
{
  "event_id": "ev_25X3yFS6TDkig1KDJWIc4nnJO0c",
  "event_type": "http_request_complete.v0",
  "event_timestamp": "2024-06-23T23:44:16Z",
  "account_id": "ac_2OtNvAlhso10Gx6a7eupzX3F98q",
  "object": {
    "traffic_policy": {
      "logs": [
        {
          "metadata": {
            "message": "Log action executed.",
            "endpoint_id": "ep_2bhsN2VP8W4pTkaMSrhyj0SRf8J"
          }
        }
      ]
    }
  }
}
```

## Action result variables

The following variables are made available for use in subsequent expressions and
CEL interpolations after the action has run. Variable values will only apply
to the last action execution, results are not concatenated.

<ConfigField title="actions.ngrok.log.metadata" type="object">
  A key-value map containing metadata that was logged during the action.
  Each key represents a metadata attribute, and the value provides its
  corresponding details.
</ConfigField>


Built with [Mintlify](https://mintlify.com).