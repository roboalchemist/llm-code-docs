# Source: https://ngrok.com/docs/traffic-policy/actions/circuit-breaker.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Circuit Breaker Action

> Prevent overload and maintain system reliability by rejecting requests when errors and volume exceed set thresholds.

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

The Circuit Breaker Traffic Policy action helps you maintain system reliability
by rejecting requests when the error rate and request volume within a rolling
window exceed defined thresholds. It pauses traffic temporarily to allow the
system to recover and automatically re-evaluates upstream health before
resuming.

## Configuration reference

The [Traffic Policy](/traffic-policy/) configuration reference for this action.

### Supported phases

`on_http_request`

### Type

`circuit-breaker`

### Configuration fields

<ConfigField title="error_threshold" type="float" required={true} defaultValue="0.5">
  Threshold percentage of errors that must be met before requests are
  rejected.

  Must be a value between `0.0` and `1.0`.
</ConfigField>

<ConfigField title="volume_threshold" type="integer" defaultValue="10">
  Number of requests in a rolling window before checking the error
  threshold.

  Must be a number between `1` and `2,000,000,000`.
</ConfigField>

<ConfigField title="window_duration" type="duration" defaultValue="10s">
  Number of seconds in the rolling window that metrics are retained for.

  Must be a value between `1s` and `2m`.
</ConfigField>

<ConfigField title="tripped_duration" type="duration" defaultValue="10s">
  Number of seconds the system waits after rejecting a request before
  re-evaluating upstream health.

  Must be a value between `1s` and `2m`.
</ConfigField>

<ConfigField title="num_buckets" type="integer">
  Number of buckets that metrics are divided into within the rolling window.

  Fixed at `10`.
</ConfigField>

<ConfigField title="enforce" type="boolean" defaultValue="true">
  Determines if the circuit breaker is active.

  If `false`, the circuit breaker never trips, and no requests are rejected.
</ConfigField>

## Behavior

### Non-terminating action

This is a **Non-terminating action**. It does not return a response, and will allow Traffic Policy processing to continue to the next Action in the chain. All **Cloud Endpoint** Traffic Policies must end with a terminating action. This requirement does not apply to **Agent Endpoints**.

## Examples

### Basic example

This example configuration sets up an endpoint (`hotdog.ngrok.app`) that allows
only 1 request every 60 seconds and trips the circuit breaker for 2 minutes.

#### Example Traffic Policy document

<CodeGroup>
  ```yaml policy.yml theme={null}
  on_http_request:
    - actions:
      - type: "circuit-breaker"
        config:
          error_threshold: 0
          volume_threshold: 1
          window_duration: "60s"
          tripped_duration: "2m"
          enforce: true
  ```

  ```json policy.json theme={null}
  {
    "on_http_request": [
      {
        "actions": [
          {
            "type": "circuit-breaker",
            "config": {
              "error_threshold": 0,
              "volume_threshold": 1,
              "window_duration": "60s",
              "tripped_duration": "2m",
              "enforce": true
            }
          }
        ]
      }
    ]
  }
  ```
</CodeGroup>

#### Start endpoint with Traffic Policy

```bash  theme={null}
ngrok http 8080 --url hotdog.ngrok.app --traffic-policy-file /path/to/policy.yml
```

#### Helper script

```python circuit_breaker.py theme={null}
import requests
import time


url = "https://hotdog.ngrok.app"

attempt = 1

while True:
    try:
        response = requests.get(url)

        # Log the response
        if response.status_code == 200:
            print(f"Attempt {attempt}: Success ({response.status_code})")
        else:
            print(f"Attempt {attempt}: Failure ({response.status_code})")

        # Stop when circuit breaker trips
        if response.status_code == 503:
            print("\nCircuit breaker tripped!")
            break
    except requests.exceptions.RequestException as e:
        print(f"Attempt {attempt}: Error ({e})")
        break

    attempt += 1
    time.sleep(0.01)  # Reduce delay for faster request rate
```

```bash  theme={null}
➜  ~ python3  circuit_breaker.py
Attempt 1: Success (200)
Attempt 2: Failure (503)

Circuit breaker tripped!
```

## Action result variables

The following variables are made available for use in subsequent expressions and
CEL interpolations after the action has run. Variable values will only apply
to the last action execution, results are not concatenated.

<Note>This action does not expose any result variables.</Note>


Built with [Mintlify](https://mintlify.com).