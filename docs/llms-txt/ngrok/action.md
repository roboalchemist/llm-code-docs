# Source: https://ngrok.com/docs/traffic-policy/variables/action.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Action Variables

> Reference documentation for action variables provided by Traffic Policy actions for use in subsequent rules and expressions.

export const ConfigEnumOption = ({children}) => {
  return <div className="space-y-2 px-4 py-2 list-none">{children}</div>;
};

export const ConfigEnum = ({label, children}) => {
  return <div className="m-0 flex flex-shrink-0 list-none flex-col divide-y divide-gray-200 self-start rounded-md border border-gray-200 p-0 dark:divide-gray-800 dark:border-gray-800 [&_li+li]:mt-0 [&_li]:py-2 list-none">
      <div className="px-4 py-2 font-semibold list-none">
        {label ? label : "Possible enum values"}
      </div>
      {children}
    </div>;
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

export const ConfigChildren = ({open = false, children}) => {
  const [isOpen, setIsOpen] = useState(open);
  return <div>
      <button type="button" className="flex items-center rounded-xl px-3 py-1.5 overflow-hidden text-gray-700 dark:text-gray-300 border border-gray-200 dark:border-white/[0.07] bg-background-light dark:bg-background-dark hover:bg-gray-600/5 dark:hover:bg-gray-200/5" onClick={() => setIsOpen(!isOpen)}>
        {!isOpen && "Show Child Properties"}
        {isOpen && "Hide Child Properties"}
      </button>
      {isOpen && <div className="m-0 mt-2 flex flex-shrink-0 list-none flex-col divide-y divide-gray-200 self-start rounded-md border border-gray-200 p-0 dark:divide-gray-800 dark:border-gray-800 [&_li]:p-4">
          {children}
        </div>}
    </div>;
};

export const Config = ({children}) => {
  return <div className="m-0 flex flex-shrink-0 list-none flex-col divide-y divide-gray-200 self-start p-0 dark:divide-gray-800">
      {children}
    </div>;
};

The following variables are made available for use in subsequent expressions and
CEL interpolations after the action has run. Variable values will only apply
to the last action execution, results are not concatenated.

### Add Headers

<Config>
  <ConfigField title="actions.ngrok.add_headers.headers_added" type="object">
    <p>Map of headers that were added by the action.</p>
  </ConfigField>
</Config>

### AI Gateway

<Config>
  <ConfigField title="actions.ngrok.ai_gateway.status" type="string">
    <p>
      Overall outcome of the action: <code>"success"</code> or <code>"error"</code>.
    </p>
  </ConfigField>

  <ConfigField title="actions.ngrok.ai_gateway.error" type="object">
    <p>
      Error details. Only present when <code>status</code> is <code>"error"</code>.
    </p>

    <ConfigChildren>
      <ConfigField title="error.code" type="string">
        <p>Error code (e.g., <code>"ERR\_NGROK\_3807"</code>).</p>
      </ConfigField>

      <ConfigField title="error.message" type="string">
        <p>Error message describing the failure.</p>
      </ConfigField>
    </ConfigChildren>
  </ConfigField>

  <ConfigField title="actions.ngrok.ai_gateway.client" type="object">
    <p>
      Information about the client request.
    </p>

    <ConfigChildren>
      <ConfigField title="client.method" type="string">
        <p>HTTP method from the client request.</p>
      </ConfigField>

      <ConfigField title="client.path" type="string">
        <p>Request path from the client.</p>
      </ConfigField>

      <ConfigField title="client.request_headers" type="object">
        <p>Client request headers (API key/auth headers trimmed to avoid leaking).</p>
      </ConfigField>

      <ConfigField title="client.user_agent" type="string">
        <p>User-Agent header from the client.</p>
      </ConfigField>

      <ConfigField title="client.model" type="string">
        <p>Client-requested model field.</p>
      </ConfigField>

      <ConfigField title="client.models" type="array of strings">
        <p>Client-requested models field.</p>
      </ConfigField>

      <ConfigField title="client.api_key_hash" type="string">
        <p>Trimmed client-supplied api key to avoid leaking while still being able to correlate it with the full key if you have it.</p>
      </ConfigField>

      <ConfigField title="client.rejected_models" type="array of objects">
        <p>Models the client requested but were excluded.</p>

        <ConfigChildren>
          <ConfigField title="rejected_models[i].model" type="string">
            <p>Model the client requested but was excluded.</p>
          </ConfigField>

          <ConfigField title="rejected_models[i].reason" type="string">
            <p>Explanation for why it was rejected.</p>
          </ConfigField>
        </ConfigChildren>
      </ConfigField>
    </ConfigChildren>
  </ConfigField>

  <ConfigField title="actions.ngrok.ai_gateway.input_ngrok_tokens" type="integer">
    <p>Input token count calculated by ngrok (used for billing).</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.ai_gateway.output_ngrok_tokens" type="integer">
    <p>Output token count calculated by ngrok (used for billing).</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.ai_gateway.gateway_latency_ms" type="integer">
    <p>Time added by gateway logic in milliseconds. Excludes time the gateway spend waiting on the upstream provider(s) to respond.</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.ai_gateway.model_selection" type="array of objects">
    <p>
      Details about the model selection process.
    </p>

    <ConfigChildren>
      <ConfigField title="model_selection[i].strategy" type="string">
        <p>The resolved strategy expression.</p>
      </ConfigField>

      <ConfigField title="model_selection[i].error" type="string">
        <p>Error if strategy evaluation failed.</p>
      </ConfigField>

      <ConfigField title="model_selection[i].candidates_returned" type="array of strings">
        <p>Models returned by the strategy expression.</p>
      </ConfigField>

      <ConfigField title="model_selection[i].candidates_after_allowed_filter" type="array of strings">
        <p>List after .disabled, only\_allow\_configured\_\* filters.</p>
      </ConfigField>

      <ConfigField title="model_selection[i].candidates_after_client_filter" type="array of strings">
        <p>List after filtering by client-requested models.</p>
      </ConfigField>

      <ConfigField title="model_selection[i].models_to_try" type="array of strings">
        <p>Final list of models to try.</p>
      </ConfigField>
    </ConfigChildren>
  </ConfigField>

  <ConfigField title="actions.ngrok.ai_gateway.models_tried" type="array of objects">
    <p>
      Models attempted in chronological order.
    </p>

    <ConfigChildren>
      <ConfigField title="models_tried[i].model" type="string">
        <p>Model identifier.</p>
      </ConfigField>

      <ConfigField title="models_tried[i].provider" type="string">
        <p>Provider Provider identifier for the model tried.</p>
      </ConfigField>

      <ConfigField title="models_tried[i].author" type="string">
        <p>Author identifier for the model tried (may be empty).</p>
      </ConfigField>

      <ConfigField title="models_tried[i].api_key_selection" type="array of objects">
        <p>Details about API key selection for this model.</p>

        <ConfigChildren>
          <ConfigField title="api_key_selection[i].strategy" type="string">
            <p>Strategy used for API key selection.</p>
          </ConfigField>

          <ConfigField title="api_key_selection[i].error" type="string">
            <p>Error if strategy failed.</p>
          </ConfigField>

          <ConfigField title="api_key_selection[i].keys_to_try" type="array of strings">
            <p>List of trimmed keys to try.</p>
          </ConfigField>
        </ConfigChildren>
      </ConfigField>

      <ConfigField title="models_tried[i].requests_made" type="array of objects">
        <p>List of requests made for this model.</p>

        <ConfigChildren>
          <ConfigField title="requests_made[i].status" type="string">
            <p>Request outcome: <code>"success"</code> or <code>"error"</code>.</p>
          </ConfigField>

          <ConfigField title="requests_made[i].error" type="string">
            <p>Error message if request failed.</p>
          </ConfigField>

          <ConfigField title="requests_made[i].upstream_input_tokens" type="integer">
            <p>Input token count reported by the upstream provider.</p>
          </ConfigField>

          <ConfigField title="requests_made[i].upstream_output_tokens" type="integer">
            <p>Output token count reported by the upstream provider.</p>
          </ConfigField>

          <ConfigField title="requests_made[i].request" type="object">
            <p>Details of the request made by the gateway</p>

            <ConfigChildren>
              <ConfigField title="request.url" type="string">
                <p>Request URL.</p>
              </ConfigField>

              <ConfigField title="request.api_key" type="string">
                <p>Partially redacted API key for safe display and correlation with the full key.</p>
              </ConfigField>
            </ConfigChildren>
          </ConfigField>

          <ConfigField title="requests_made[i].response" type="object">
            <p>Response details.</p>

            <ConfigChildren>
              <ConfigField title="response.status_code" type="integer">
                <p>HTTP status code.</p>
              </ConfigField>

              <ConfigField title="response.headers" type="object">
                <p>Response headers.</p>
              </ConfigField>

              <ConfigField title="response.body_on_error" type="string">
                <p>Only populated on failure, truncated to 1KB.</p>
              </ConfigField>
            </ConfigChildren>
          </ConfigField>

          <ConfigField title="requests_made[i].upstream_latency" type="object">
            <p>Upstream latency measurements.</p>

            <ConfigChildren>
              <ConfigField title="upstream_latency.time_to_first_byte_ms" type="integer">
                <p>Milliseconds until first byte of response received.</p>
              </ConfigField>

              <ConfigField title="upstream_latency.total_ms" type="integer">
                <p>Milliseconds until request fully completed.</p>
              </ConfigField>
            </ConfigChildren>
          </ConfigField>
        </ConfigChildren>
      </ConfigField>
    </ConfigChildren>
  </ConfigField>

  <ConfigField title="actions.ngrok.ai_gateway.success" type="object">
    <p>
      Details of the successful model. Only present when <code>status</code> is <code>"success"</code>.
    </p>

    <ConfigChildren>
      <ConfigField title="success.model_index" type="integer">
        <p>Index into the <code>models\_tried</code> array for the successful model.</p>
      </ConfigField>

      <ConfigField title="success.request_index" type="integer">
        <p>Index into <code>requests\_made</code> array for the successful request.</p>
      </ConfigField>

      <ConfigField title="success.model" type="string">
        <p>Model that successfully handled the request (e.g., <code>"gpt-4"</code>).</p>
      </ConfigField>

      <ConfigField title="success.provider" type="string">
        <p>Provider identifier for the successful model.</p>
      </ConfigField>

      <ConfigField title="success.author" type="string">
        <p>Author identifier for the successful model. May be empty.</p>
      </ConfigField>
    </ConfigChildren>
  </ConfigField>
</Config>

### Basic Auth

<Config>
  <ConfigField title="actions.ngrok.basic_auth.credentials.presented" type="bool" required={false}>
    <p>Whether there were Basic Auth credentials presented in the Authorization header.</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.basic_auth.credentials.username" type="string" required={false}>
    <p>The username of the credentials presented.</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.basic_auth.credentials.authorized" type="bool" required={false}>
    <p>Whether the presented basic auth credentials were authorized for this request.</p>
  </ConfigField>
</Config>

### Compress Response

<Config>
  <ConfigField title="actions.ngrok.compress.already_compressed" type="boolean">
    <p>
      Indicates whether the body was already compressed before the action was
      applied. Returns <code>true</code> if no further compression was
      performed.
    </p>
  </ConfigField>

  <ConfigField title="actions.ngrok.compress.negotiated_algorithm" type="string">
    <p>
      The compression algorithm selected and applied by the action, based on the
      client's request and action configuration.
    </p>
  </ConfigField>
</Config>

### HTTP Request

<Config>
  <ConfigField title="actions.ngrok.http_request.error.code" type="string" />

  <ConfigField title="actions.ngrok.http_request.error.message" type="string">
    <p>
      Message for an error that occurred during the invocation of an action.
    </p>
  </ConfigField>

  <ConfigField title="actions.ngrok.http_request.attempts" type="array of objects">
    <p>
      A list of HTTP responses for each request attempt.
    </p>

    <ConfigChildren>
      <ConfigField title="attempts[i].resolved_ip" type="string">
        <p>
          The IP address of the host returning the response.
        </p>
      </ConfigField>

      <ConfigField title="attempts[i].response_header" type="object">
        <p>
          A map of HTTP response headers.
        </p>
      </ConfigField>

      <ConfigField title="attempts[i].response_status_code" type="int">
        <p>
          The HTTP Status code for the response attempt.
        </p>
      </ConfigField>

      <ConfigField title="attempts[i].response_time_ms" type="string">
        <p>
          Time it took to receive the response.
        </p>
      </ConfigField>
    </ConfigChildren>
  </ConfigField>

  <ConfigField title="actions.ngrok.http_request.req" type="object">
    <p>
      The HTTP request.
    </p>

    <ConfigChildren>
      <ConfigField title="req.method" type="string">
        <p>
          The HTTP method of the request.
        </p>
      </ConfigField>

      <ConfigField title="req.header" type="object">
        <p>
          A map of HTTP request headers.
        </p>
      </ConfigField>

      <ConfigField title="req.url" type="string">
        <p>
          The request url.
        </p>
      </ConfigField>

      <ConfigField title="req.body" type="string">
        <p>
          The request body.
        </p>
      </ConfigField>
    </ConfigChildren>
  </ConfigField>

  <ConfigField title="actions.ngrok.http_request.res" type="object">
    <p>
      The last attempted HTTP response. Unlike `actions.ngrok.attempts[i]` this variable also contains the response body.
    </p>

    <ConfigChildren>
      <ConfigField title="res.resolved_ip" type="string">
        <p>
          The IP address of the host returning the response.
        </p>
      </ConfigField>

      <ConfigField title="res.header" type="object">
        <p>
          A map of HTTP response headers.
        </p>
      </ConfigField>

      <ConfigField title="res.status_code" type="int">
        <p>
          The HTTP Status code for the response.
        </p>
      </ConfigField>

      <ConfigField title="res.time_ms" type="string">
        <p>
          Time it took to receive the response.
        </p>
      </ConfigField>

      <ConfigField title="res.body" type="string">
        <p>
          The response body
        </p>
      </ConfigField>
    </ConfigChildren>
  </ConfigField>
</Config>

### JWT Validation

<Config>
  <ConfigField title="actions.ngrok.jwt_validation.tokens" type="array of objects">
    <p>The list of JSON Web Tokens (JWTs) processed by the action.</p>

    <ConfigChildren>
      <ConfigField title="tokens[i].header" type="object">
        <p>
          The header portion of the JWT, parsed into a key-value map containing
          metadata about the token.
        </p>
      </ConfigField>

      <ConfigField title="tokens[i].location" type="string">
        <p>
          The part of the HTTP request where the JWT was located (for example,{" "}
          <code>header</code>, <code>body</code>).
        </p>
      </ConfigField>

      <ConfigField title="tokens[i].location_property" type="string">
        <p>
          The specific header or body field that contained the JWT (for example,{" "}
          <code>"Authorization"</code>).
        </p>
      </ConfigField>

      <ConfigField title="tokens[i].payload" type="object">
        <p>
          The payload portion of the JWT, parsed into a key-value map
          representing the claims.
        </p>
      </ConfigField>

      <ConfigField title="tokens[i].signature" type="string">
        <p>
          The signature portion of the JWT, encoded in base64, used for
          verifying token integrity.
        </p>
      </ConfigField>

      <ConfigField title="tokens[i].verified" type="boolean">
        <p>
          Indicates whether the token passed verification. Returns{" "}
          <code>true</code> if verified successfully.
        </p>
      </ConfigField>
    </ConfigChildren>
  </ConfigField>

  <ConfigField title="actions.ngrok.jwt_validation.error.code" type="string">
    <p>
      A machine-readable code describing an error that occurred during the
      action's execution.
    </p>
  </ConfigField>

  <ConfigField title="actions.ngrok.jwt_validation.error.message" type="string">
    <p>
      A human-readable message providing details about an error that occurred
      during the action's execution.
    </p>
  </ConfigField>
</Config>

### Log

<Config>
  <ConfigField title="actions.ngrok.log.metadata" type="object">
    <p>
      A key-value map containing metadata that was logged during the action.
      Each key represents a metadata attribute, and the value provides its
      corresponding details.
    </p>
  </ConfigField>
</Config>

### OAuth

<Config>
  <ConfigField title="actions.ngrok.oauth.error.code" type="string">
    <p>Code for an error that occurred during the invocation of an action.</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.oauth.error.message" type="string">
    <p>
      Message for an error that occurred during the invocation of an action.
    </p>
  </ConfigField>

  <ConfigField title="actions.ngrok.oauth.identity.id" type="string">
    <p>Unique identifier for the ngrok Identity entity</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.oauth.identity.email" type="string">
    <p>Email address of the authorized user from the provider.</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.oauth.identity.name" type="string">
    <p>Name for the authorized user from the provider.</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.oauth.identity.provider_user_id" type="string">
    <p>Identifier for the authorized user from the provider.</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.oauth.identity.current_provider_session_id" type="string">
    <p>The current Identity session identifier for this request.</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.oauth.access_token" type="string">
    <p>The access token from the provider.</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.oauth.refresh_token" type="string">
    <p>The refresh token from the provider.</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.oauth.expires_at" type="string">
    <p>Timestamp when the current session will expire.</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.oauth.session_timed_out" type="boolean">
    <p>Returns true when the session timed out.</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.oauth.session_max_duration_reached" type="boolean">
    <p>Returns true when the current session reached the max duration.</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.oauth.userinfo_refreshed" type="boolean">
    <p>Returns true when ngrok updates the user information on the identity.</p>
  </ConfigField>
</Config>

### OpenID Connect (OIDC)

<Config>
  <ConfigField title="actions.ngrok.oidc.error.code" type="string">
    <p>Code for an error that occurred during the invocation of an action.</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.oidc.error.message" type="string">
    <p>
      Message for an error that occurred during the invocation of an action.
    </p>
  </ConfigField>

  <ConfigField title="actions.ngrok.oidc.identity.id" type="string">
    <p>Unique identifier for the ngrok Identity entity</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.oidc.identity.email" type="string">
    <p>Email address of the authorized user from the provider.</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.oidc.identity.name" type="string">
    <p>Name for the authorized user from the provider.</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.oidc.identity.provider_user_id" type="string">
    <p>Identifier for the authorized user from the provider.</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.oidc.identity.current_session_id" type="string">
    <p>The current Identity session identifier for this request.</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.oidc.identity_token" type="string">
    <p>The identity token from the provider for the current user.</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.oidc.access_token" type="string">
    <p>The access token from the provider.</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.oidc.refresh_token" type="string">
    <p>The refresh token from the provider.</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.oidc.expires_at" type="string">
    <p>Timestamp when the current session will expire.</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.oidc.session_timed_out" type="boolean">
    <p>Returns true when the session timed out.</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.oidc.session_max_duration_reached" type="boolean">
    <p>Returns true when the current session reached the max duration.</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.oidc.userinfo_refreshed" type="boolean">
    <p>Returns true when ngrok updates the user information on the identity.</p>
  </ConfigField>
</Config>

### Rate Limit

<Config>
  <ConfigField title="actions.ngrok.rate_limit.bucket_key" type="string">
    <p>The key used for bucketing requests. This is the key used to group and track requests in the rate-limiting process, ensuring that the same bucket is subject to the rate limit across multiple requests.</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.rate_limit.limited" type="boolean">
    <p>Indicates whether the request was limited by the rate limit. If  `true`, the request was rate-limited based on the configured limits for the specified bucket.</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.rate_limit.error.code" type="string">
    <p>A machine-readable code describing an error that occurred during the action's execution.</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.rate_limit.error.message" type="string">
    <p>A human-readable message providing details about an error that occurred during the action's execution.</p>
  </ConfigField>
</Config>

### Redirect

<Config>
  <ConfigField title="actions.ngrok.redirect.matches" type="array of strings">
    <p>A list of elements that were matched during redirection. These represent the request components (for example, path or query parameters) that triggered the action and resulted in the redirect.</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.redirect.url" type="string">
    <p>The URL to which the traffic was redirected. This is the destination URL returned as part of the redirect response after the action was executed.</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.redirect.error.code" type="string">
    <p>A machine-readable code describing an error that occurred during the action's execution.</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.redirect.error.message" type="string">
    <p>A human-readable message providing details about an error that occurred during the action's execution.</p>
  </ConfigField>
</Config>

### Remove Headers

<Config>
  <ConfigField title="actions.ngrok.remove_headers.headers_removed" type="array of strings">
    <p>A list of headers that were successfully removed by the action.</p>
  </ConfigField>
</Config>

### Restrict IPs

<Config>
  <ConfigField title="actions.ngrok.restrict_ips.action" type="string">
    <p>The action taken for this request.</p>

    <ConfigEnum label="Possible values">
      <ConfigEnumOption>`allow` - If the request was permitted.</ConfigEnumOption>
      <ConfigEnumOption>`deny` - If the request was denied.</ConfigEnumOption>
    </ConfigEnum>
  </ConfigField>

  <ConfigField title="actions.ngrok.restrict_ips.matched_cidr" type="string">
    <p>The CIDR block that matched the incoming client's IP address. If no match was found, this value will be empty.</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.restrict_ips.error.code" type="string">
    <p>A machine-readable code describing an error that occurred during the action's execution.</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.restrict_ips.error.message" type="string">
    <p>A human-readable message providing details about an error that occurred during the action's execution.</p>
  </ConfigField>
</Config>

### URL Rewrite

<Config>
  <ConfigField title="actions.ngrok.url_rewrite.matches" type="array of strings">
    <p>List of elements that matched the URL before the rewrite action was applied. These can be specific parts of the URL, such as the domain, path, or query parameters, that were matched based on the action configuration.</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.url_rewrite.url" type="string">
    <p>The final URL after the rewrite action has been applied. This is the new URL to which the original request is redirected after the specified modifications have been made.</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.url_rewrite.error.code" type="string">
    <p>A machine-readable code describing an error that occurred during the action's execution.</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.url_rewrite.error.message" type="string">
    <p>A human-readable message providing details about an error that occurred during the action's execution.</p>
  </ConfigField>
</Config>

### Verify Webhook

<Config>
  <ConfigField title="actions.ngrok.verify_webhook.verified" type="bool">
    <p>Indicates whether or not the request was successfully verified.</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.verify_webhook.error.code" type="string">
    <p>Code for an error that occurred during the invocation of an action.</p>
  </ConfigField>

  <ConfigField title="actions.ngrok.verify_webhook.error.message" type="string">
    <p>Message for an error that occurred during the invocation of an action.</p>
  </ConfigField>
</Config>


Built with [Mintlify](https://mintlify.com).