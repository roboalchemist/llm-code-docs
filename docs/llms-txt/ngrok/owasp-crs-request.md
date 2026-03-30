# Source: https://ngrok.com/docs/traffic-policy/actions/owasp-crs-request.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# OWASP CRS Request Action

> Block common web attacks with the `owasp-crs-request` action in Traffic Policy.

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

export const YouTubeEmbed = ({className, title, videoId, ...props}) => {
  return <div className={`relative aspect-video mb-3 ${className}`} {...props}>
      <iframe src={`https://www.youtube.com/embed/${videoId}`} allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen className="absolute inset-0 w-full h-full" title={title} />
    </div>;
};

The `owasp-crs-request` action enables rule processing on incoming HTTP requests to your endpoint.
To use rule processing to block malicious HTTP *responses*, enable the [OWASP CRS Response action](/traffic-policy/actions/owasp-crs-response/).

<Tip>
  **Use both OWASP CRS actions for comprehensive protection.**

  The Request action protects against malicious client requests (such as SQL injection and XSS attacks).
  The Response action protects against data leaks or vulnerabilities in your upstream service's responses (such as exposed SQL error messages and sensitive data).

  Together, they provide defense-in-depth security for both incoming and outgoing traffic.
</Tip>

[OWASP](https://owasp.org/) stands for the Open Web Application Security
Project, an online community that, among other things, maintains annual lists of
the most critical web application security risks. The [OWASP Core Rule
Set](https://owasp.org/www-project-modsecurity-core-rule-set/) (CRS) is a set of
attack detection rules exposed for use in your Traffic Policies.
It includes protections against attacks like SQL Injection, Cross Site
Scripting, Local File Inclusion, and many others.

<YouTubeEmbed videoId="HHxj5VGFTEA" title="Block web attacks with ngrok's OWASP CRS Request" />

### Configuration reference

This is the [Traffic Policy](/traffic-policy/) configuration
reference for this action.

#### Supported phases

`on_http_request`

#### Type

`owasp-crs-request`

#### Configuration fields

<ConfigField title="on_error" type="string" required={true}>
  <p>Behavior if there is an error processing rules. Must be one of either <code>"continue"</code> or <code>"halt"</code> (default <code>"halt"</code>).</p>
  <p>More information can be found in the [Managing Fallback Behavior](#managing-fallback-behavior-on-error) section.</p>
</ConfigField>

<ConfigField title="process_body" type="bool" required={false}>
  <p>If <code>true</code>, rules for the request body are evaluated. Default is <code>false</code>.</p>
  <p>See [Body Processing](#body-processing) for details and limitations.</p>
</ConfigField>

<ConfigField title="exclude_rule_ids" type="array of integers" required={false}>
  <p>List of OWASP CRS rule IDs to exclude from evaluation.</p>
  <p>The minimum value is <code>900000</code> and the maximum value is <code>999999</code>.</p>
</ConfigField>

## Behavior

This action evaluates rules for request headers and body (when `process_body` is enabled), and each matching rule adds to the overall score of a request. If the score exceeds the set score threshold, the action will block the request.

The tallying process is called Anomaly Scoring, and is detailed on [the CRS website.](https://coreruleset.org/docs/2-how-crs-works/2-1-anomaly_scoring/)

This action costs **10 [Traffic Policy Units (TPUs)](/pricing-limits/traffic-policy-unit-pricing/)** per request evaluated.

### Default behavior

The default behavior for this action is based on the following [Coraza](https://coraza.io/) directives and rules from v4.14.0 of the CRS:

* [coraza.conf-recommended](https://github.com/corazawaf/coraza/blob/main/coraza.conf-recommended)
* [crs-setup.conf.example](https://github.com/corazawaf/coraza-coreruleset/blob/main/rules/%40crs-setup.conf.example)
* [@owasp\_crs/\*.conf](https://github.com/corazawaf/coraza-coreruleset/tree/main/rules/%40owasp_crs)

Included in these rules is an inbound anomaly score threshold of 5 and a [paranoia level](https://coreruleset.org/docs/2-how-crs-works/2-2-paranoia_levels/) of 1.

### Managing fallback behavior (`on_error`)

If `on_error` is set to `halt` (default) and the action encounters an error while evaluating rules, the Traffic Policy chain will halt and no further actions will be executed. For example, if you have a `log` action after the `owasp-crs-request` action, the `log` action will not be run and the error will be returned.

However, if `on_error` is set to `continue`, actions that appear after the `owasp-crs-request` action will still be executed even if the `owasp-crs-request` action encounters an error.

### Body processing

When `process_body` is enabled, ngrok buffers and evaluates rules against the first 4KB of the body. If the body is larger than 4KB, the portion after the first 4KB is ignored.

<Note>
  Enabling `process_body` buffers the request body in memory, which may increase latency for large payloads.
</Note>

### Rule exclusion

When `exclude_rule_ids` is configured, ngrok skips evaluation of the specified rule IDs. This allows you to disable specific OWASP CRS rules that may be causing false positives in your environment.

### Inbound anomaly score threshold exceeded

If the anomaly score accumulated from matching rules exceeds the threshold, ngrok blocks the request with a `HTTP 403` response. The request does not make it to your upstream.

### Failure to process the body successfully

If ngrok is unable to read the request body successfully, ngrok blocks the request with a `HTTP 500` response. The request does not make it to your upstream.

### Non-terminating action

This is a **Non-terminating action**. It does not return a response, and will allow Traffic Policy processing to continue to the next Action in the chain. All **Cloud Endpoint** Traffic Policies must end with a terminating action. This requirement does not apply to **Agent Endpoints**.

## Examples

### Running in block mode

The following configuration demonstrates how to run the `owasp-crs-request` action in block mode.

#### Example Traffic Policy document

<CodeGroup>
  ```yaml policy.yml {5} theme={null}
  on_http_request:
    - actions:
        - type: owasp-crs-request
          config:
            on_error: halt
  ```

  ```json policy.json {8} theme={null}
  {
    "on_http_request": [
      {
        "actions": [
          {
            "type": "owasp-crs-request",
            "config": {
              "on_error": "halt"
            }
          }
        ]
      }
    ]
  }
  ```
</CodeGroup>

### Example request that ngrok would block

In this example, a connection attempt to `example.ngrok.app` using the
`curl` command, and ngrok blocks the request returning back [ERR\_NGROK\_3700](/errors/err_ngrok_3700/)

```curl  theme={null}
$ curl --http1.1 -X POST https://example.ngrok.app/\
  -H "User-Agent: Mozilla/5.0" \
  -H "Content-Type: application/json" \
  -d '{"q": "<script>alert(1)</script>"}'
```

```html  theme={null}
<!DOCTYPE html>
<html class="h-full" lang="en-US" dir="ltr">
  <head>
    <link rel="preload" href="https://cdn.ngrok.com/static/fonts/euclid-square/EuclidSquare-Regular-WebS.woff" as="font" type="font/woff" crossorigin="anonymous" />
    <link rel="preload" href="https://cdn.ngrok.com/static/fonts/euclid-square/EuclidSquare-RegularItalic-WebS.woff" as="font" type="font/woff" crossorigin="anonymous" />
    <link rel="preload" href="https://cdn.ngrok.com/static/fonts/euclid-square/EuclidSquare-Medium-WebS.woff" as="font" type="font/woff" crossorigin="anonymous" />
    <link rel="preload" href="https://cdn.ngrok.com/static/fonts/euclid-square/EuclidSquare-Semibold-WebS.woff" as="font" type="font/woff" crossorigin="anonymous" />
    <link rel="preload" href="https://cdn.ngrok.com/static/fonts/euclid-square/EuclidSquare-MediumItalic-WebS.woff" as="font" type="font/woff" crossorigin="anonymous" />
    <link rel="preload" href="https://cdn.ngrok.com/static/fonts/ibm-plex-mono/IBMPlexMono-Text.woff" as="font" type="font/woff" crossorigin="anonymous" />
    <link rel="preload" href="https://cdn.ngrok.com/static/fonts/ibm-plex-mono/IBMPlexMono-TextItalic.woff" as="font" type="font/woff" crossorigin="anonymous" />
    <link rel="preload" href="https://cdn.ngrok.com/static/fonts/ibm-plex-mono/IBMPlexMono-SemiBold.woff" as="font" type="font/woff" crossorigin="anonymous" />
    <link rel="preload" href="https://cdn.ngrok.com/static/fonts/ibm-plex-mono/IBMPlexMono-SemiBoldItalic.woff" as="font" type="font/woff" crossorigin="anonymous" />
    <meta charset="utf-8">
    <meta name="author" content="ngrok">
    <meta name="description" content="ngrok is the fastest way to put anything on the internet with a single command.">
    <meta name="robots" content="noindex, nofollow">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link id="style" rel="stylesheet" href="https://cdn.dev-ngrok.com/static/css/error.css">
    <noscript>The request was blocked by the WAF. (ERR_NGROK_3700)</noscript>
    <script id="script" src="https://cdn.dev-ngrok.com/static/js/error.js" type="text/javascript"></script>
  </head>
  <body class="h-full" id="ngrok">
    <div id="root" data-payload="eyJjZG5CYXNlIjoiaHR0cHM6Ly9jZG4uZGV2LW5ncm9rLmNvbS8iLCJjb2RlIjoiMzcwMCIsIm1lc3NhZ2UiOiJUaGUgcmVxdWVzdCB3YXMgYmxvY2tlZCBieSB0aGUgV0FGLiIsInRpdGxlIjoiRm9yYmlkZGVuIn0="></div>
  </body>
</html>
```

### Running in test mode

The following configuration demonstrates how to run the `owasp-crs-request` action in test mode where rules are evaluated but blocks are not enforced.

#### Example Traffic Policy document

<CodeGroup>
  ```yaml policy.yml {5} theme={null}
  on_http_request:
    - actions:
        - type: owasp-crs-request
          config:
            on_error: continue
        - type: log
          config:
            metadata:
              message: OWASP CRS request action would be ${actions.ngrok.owasp_crs_request.decision} for ${req.url}
              error_code: ${actions.ngrok.owasp_crs_request.error.code}
              error_message: ${actions.ngrok.owasp_crs_request.error.message}
              matched_rules_first_id: ${actions.ngrok.owasp_crs_request.matched_rules[0].id}
              matched_rules_first_message: ${actions.ngrok.owasp_crs_request.matched_rules[0].message}
              matched_rules_first_data: ${actions.ngrok.owasp_crs_request.matched_rules[0].data}
  ```

  ```json policy.json {8} theme={null}
  {
    "on_http_request": [
      {
        "actions": [
          {
            "type": "owasp-crs-request",
            "config": {
              "on_error": "continue"
            }
          },
          {
            "type": "log",
            "config": {
              "metadata": {
                "message": "OWASP CRS request action would be ${actions.ngrok.owasp_crs_request.decision} for ${req.url}",
                "error_code": "${actions.ngrok.owasp_crs_request.error.code}",
                "error_message": "${actions.ngrok.owasp_crs_request.error.message}",
                "matched_rules_first_id": "${actions.ngrok.owasp_crs_request.matched_rules[0].id}",
                "matched_rules_first_message": "${actions.ngrok.owasp_crs_request.matched_rules[0].message}",
                "matched_rules_first_data": "${actions.ngrok.owasp_crs_request.matched_rules[0].data}"
              }
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

<ConfigField title="actions.ngrok.owasp_crs_request.decision" type="string">
  <p>The action taken for this request.</p>

  <ConfigEnum label="Possible values">
    <ConfigEnumOption>`allow` - If the request was permitted.</ConfigEnumOption>
    <ConfigEnumOption>`deny` - If the request was denied.</ConfigEnumOption>
  </ConfigEnum>
</ConfigField>

<ConfigField title="actions.ngrok.owasp_crs_request.anomaly_score" type="int">
  <p>
    The total anomaly score for the request. If it equals to or exceeds the set threshold, it will
    block the request.
  </p>
</ConfigField>

<ConfigField title="actions.ngrok.owasp_crs_request.anomaly_score_threshold" type="int">
  <p>
    The total anomaly score threshold for the request. By default, it is set to 5.
  </p>
</ConfigField>

<ConfigField title="actions.ngrok.owasp_crs_request.matched_rules" type="array of objects">
  <p>The list of all rules matched by this request that have a non-zero score.</p>

  <ConfigChildren>
    <ConfigField title="matched_rules[i].id" type="int">
      <p>
        The ID of the rule.
      </p>
    </ConfigField>

    <ConfigField title="matched_rules[i].message" type="string">
      <p>
        The text message describing the rule.
      </p>
    </ConfigField>

    <ConfigField title="matched_rules[i].severity" type="string">
      <p>
        The [severity](https://coraza.io/docs/seclang/actions/#severity) of the matched rule.
      </p>
    </ConfigField>

    <ConfigField title="matched_rules[i].data" type="string">
      <p>
        Any extra data about the rule and how it matched the request.
      </p>
    </ConfigField>
  </ConfigChildren>
</ConfigField>

<ConfigField title="actions.ngrok.owasp_crs_request.error.code" type="string">
  <p>
    A machine-readable code describing an error that occurred during the
    action's execution.
  </p>
</ConfigField>

<ConfigField title="actions.ngrok.owasp_crs_request.error.message" type="string">
  <p>
    A human-readable message providing details about an error that occurred
    during the action's execution.
  </p>
</ConfigField>


Built with [Mintlify](https://mintlify.com).