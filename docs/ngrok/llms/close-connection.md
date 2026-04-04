# Source: https://ngrok.com/docs/traffic-policy/actions/close-connection.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Close Connection Action

> Forcibly close connections to an endpoint.

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

The Close Connection Traffic Policy action lets you forcibly close connections
to an endpoint when certain conditions are met, for example, when the number of
requests exceeds a given limit (to mitigate DDoS attacks).

This action can be used with other actions such as [rate-limit](/traffic-policy/actions/rate-limit) and [deny](/traffic-policy/actions/deny).

## Configuration reference

The [Traffic Policy](/traffic-policy/) configuration reference for this action.

### Supported phases

`on_http_request`, `on_tcp_connect`

### Type

`close-connection`

### Configuration fields

<Note>This action does not have any configuration fields.</Note>

## Behavior

When this action is executed, connection to the endpoint is closed immediately.

This can be useful for dealing with DDoS attacks.

### Terminating action

This is a **terminating action**. It will return a response and cause Traffic Policy processing to end without executing any further Actions.

## Examples

### Basic example

This basic example configuration will guide you through setting up an endpoint on ngrok (`hotdog.ngrok.app`) and closing the connection to the endpoint.

<Steps>
  <Step title="Save the following Traffic Policy document to a file called policy.yml">
    ```yaml policy.yml theme={null}
    on_http_request:
    - name: "Immediately close connection"
      expressions:
        - req.url.path.startsWith("/dc")
      actions:
        - type: close-connection
    ```
  </Step>

  <Step title="Start the endpoint with the Traffic Policy">
    ```bash  theme={null}
    ngrok http 8080 --url hotdog.ngrok.app --traffic-policy-file ./policy.yml
    ```
  </Step>

  <Step title="Send a request to the endpoint">
    ```bash  theme={null}
    curl http://hotdog.ngrok.app/dc
    ```

    You should see something similar to the following:

    ```bash  theme={null}
    curl: (16) Error in the HTTP2 framing layer
    ```

    This is expected as the connection is closed immediately.
  </Step>
</Steps>

## Action result variables

The following variables are made available for use in subsequent expressions and
CEL interpolations after the action has run. Variable values will only apply
to the last action execution, results are not concatenated.

<Note>This action does not set any variables after it has been executed.</Note>


Built with [Mintlify](https://mintlify.com).