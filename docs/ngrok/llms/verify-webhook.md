# Source: https://ngrok.com/docs/traffic-policy/actions/verify-webhook.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Verify Webhook Action

> Validate incoming webhook signatures against a known secret to ensure authenticity.

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

The **Verify Webhook** Traffic Policy action enables you to validate incoming webhook signatures against a known secret to ensure authenticity. Depending on the verification result, it either forwards the request to the next action or rejects it, safeguarding your endpoints from unauthorized or tampered webhooks.

## Configuration reference

This is the [Traffic Policy](/traffic-policy/) configuration
reference for this action.

### Supported directions

* `on_http_request`

### Type

`verify-webhook`

### Configuration fields

<ConfigField title="provider" type="string" required={true}>
  <p>The name of the provider to verify webhook requests from.</p>
  <p>Value must be a [supported provider](#supported-providers) identifier.</p>
</ConfigField>

<ConfigField title="secret" type="string" required={true} cel={true}>
  <p>The secret key used to validate webhook requests from the specified provider.</p>
  <p>Supports [CEL Interpolation](/traffic-policy/concepts/cel-interpolation).</p>
</ConfigField>

<ConfigField title="enforce" type="bool" required={false}>
  <p>When `true`, the request will be halted if the webhook is not valid and no further actions will run. However when `false`, subsequent actions will run even if the webhook was not valid.</p>
  <p>Default <code>true</code>.</p>
</ConfigField>

## Behavior

The **verify-webhook** action ensures the authenticity of incoming webhook requests by validating their signatures against a known secret. Upon receiving a request, the action performs the signature verification. If verification succeeds, the request proceeds through the action chain. If it fails, the request is terminated with a `403 Forbidden` response, unless `enforce` is set to `false`, in which case the request proceeds without termination.

### Verification process

* **Signature Validation**: The action validates incoming webhook signature to confirm the request originates from the configured provider and that the payload has not been tampered with.
* **Request Handling**: If the webhook verification is successful, the request is forwarded to the next action. If the verification fails, the request chain is terminated with a `403` response.
* **Configurable Enforcement**: By default, verification failures result in termination. However, setting `enforce: false` allows unverified requests to proceed, while logging the verification result. This option is useful for debugging, testing, and crafting your own custom responses with action result variables.

### Endpoint verification

Some webhook providers require an initial endpoint verification challenge to validate that your application is legitimate before sending webhook events. The **verify-webhook** action automatically handles endpoint verification challenges for supported providers.

* Supported providers:
  * Twitter
  * Worldline
  * Xero
  * Zoom

#### Replay prevention with timestamp tolerance

To prevent replay attacks, ngrok verifies that the webhook’s timestamp falls within an acceptable range.

#### Secret handling and encryption

All secrets used for webhook verification are encrypted at config validation. When ngrok processes a requests the secret is decrypted.

### Non-terminating action

This is a **Non-terminating action**. It does not return a response, and will allow Traffic Policy processing to continue to the next Action in the chain. All **Cloud Endpoint** Traffic Policies must end with a terminating action. This requirement does not apply to **Agent Endpoints**.

## Supported providers

Currently, these integration guides refer to modules.

| Provider                    | Provider Identifier     | Integration Guide                                                                                    |
| --------------------------- | ----------------------- | ---------------------------------------------------------------------------------------------------- |
| AfterShip                   | `aftership`             | [Documentation](/integrations/webhooks/aftership-webhooks)                                           |
| Airship                     | `airship`               | [Documentation](/integrations/webhooks/airship-webhooks)                                             |
| Alchemy                     | `alchemy`               | [Documentation](https://docs.alchemy.com/reference/notify-api-quickstart)                            |
| Amazon SNS                  | `sns`                   | [Documentation](/integrations/webhooks/amazon-sns-webhooks)                                          |
| Autodesk Platform Services  | `autodesk`              | [Documentation](/integrations/webhooks/autodesk-webhooks)                                            |
| Bitbucket                   | `bitbucket`             | [Documentation](/integrations/webhooks/bitbucket-webhooks)                                           |
| Bolt                        | `bolt`                  | [Documentation](https://help.bolt.com/developers/guides/webhooks/hook-verification/)                 |
| Box                         | `box`                   | [Documentation](/integrations/webhooks/box-webhooks)                                                 |
| Brex                        | `brex`                  | [Documentation](/integrations/webhooks/brex-webhooks)                                                |
| Buildkite                   | `buildkite`             | [Documentation](/integrations/webhooks/buildkite-webhooks)                                           |
| Calendly                    | `calendly`              | [Documentation](/integrations/webhooks/calendly-webhooks)                                            |
| Castle                      | `castle`                | [Documentation](/integrations/webhooks/castle-webhooks)                                              |
| Chargify                    | `chargify`              | [Documentation](/integrations/webhooks/chargify-webhooks)                                            |
| CircleCI                    | `circleci`              | [Documentation](/integrations/webhooks/circleci-webhooks)                                            |
| Clearbit                    | `clearbit`              | [Documentation](/integrations/webhooks/clearbit-webhooks)                                            |
| Clerk                       | `clerk`                 | [Documentation](/integrations/webhooks/clerk-webhooks)                                               |
| Coinbase                    | `coinbase`              | [Documentation](/integrations/webhooks/coinbase-webhooks)                                            |
| Contentful                  | `contentful`            | [Documentation](/integrations/webhooks/contentful-webhooks)                                          |
| DocuSign                    | `docusign`              | [Documentation](/integrations/webhooks/docusign-webhooks)                                            |
| Dropbox                     | `dropbox`               | [Documentation](/integrations/webhooks/dropbox-webhooks)                                             |
| Facebook Graph API          | `facebook_graph_api`    | [Documentation](/integrations/webhooks/facebook-webhooks)                                            |
| Facebook Messenger          | `facebook_messenger`    | [Documentation](/integrations/webhooks/facebook-messenger-webhooks)                                  |
| Frame.io                    | `frameio`               | [Documentation](/integrations/webhooks/frameio-webhooks)                                             |
| GitHub                      | `github`                | [Documentation](/integrations/webhooks/github-webhooks)                                              |
| GitLab                      | `gitlab`                | [Documentation](/integrations/webhooks/gitlab-webhooks)                                              |
| Go1                         | `go1`                   | [Documentation](https://www.go1.com/developers/partners/concepts/webhook-signature-authentification) |
| Heroku                      | `heroku`                | [Documentation](/integrations/webhooks/heroku-webhooks)                                              |
| Hosted Hooks                | `hostedhooks`           | [Documentation](/integrations/webhooks/hostedhooks-webhooks)                                         |
| HubSpot                     | `hubspot`               | [Documentation](/integrations/webhooks/hubspot-webhooks)                                             |
| Hygraph (Formerly GraphCMS) | `graphcms`              | [Documentation](/integrations/webhooks/hygraph-webhooks)                                             |
| Instagram                   | `instagram`             | [Documentation](/integrations/webhooks/instagram-webhooks)                                           |
| Intercom                    | `intercom`              | [Documentation](/integrations/webhooks/intercom-webhooks)                                            |
| Jira                        | `jira`                  | [Documentation](/integrations/webhooks/jira-webhooks)                                                |
| Launch Darkly               | `launch_darkly`         | [Documentation](/integrations/webhooks/launchdarkly-webhooks)                                        |
| Linear                      | `linear`                | [Documentation](/integrations/webhooks/linear-webhooks)                                              |
| Mailchimp                   | `mailchimp`             | [Documentation](/integrations/webhooks/mailchimp-webhooks)                                           |
| Mailgun                     | `mailgun`               | [Documentation](/integrations/webhooks/mailgun-webhooks)                                             |
| Microsoft Teams             | `microsoft_teams`       | [Documentation](/integrations/webhooks/teams-webhooks)                                               |
| Modern Treasury             | `modern_treasury`       | [Documentation](/integrations/webhooks/modern-treasury-webhooks)                                     |
| MongoDB                     | `mongodb`               | [Documentation](/integrations/webhooks/mongodb-webhooks)                                             |
| Mux                         | `mux`                   | [Documentation](/integrations/webhooks/mux-webhooks)                                                 |
| Orb                         | `orb`                   | [Documentation](https://developer.withorb.com/docs/orb-docs/webhooks)                                |
| Orbit                       | `orbit`                 | [Documentation](/integrations/webhooks/orbit-webhooks)                                               |
| PagerDuty                   | `pagerduty`             | [Documentation](/integrations/webhooks/pagerduty-webhooks)                                           |
| Pinwheel                    | `pinwheel`              | [Documentation](/integrations/webhooks/pinwheel-webhooks)                                            |
| Plivo                       | `plivo`                 | [Documentation](/integrations/webhooks/plivo-webhooks)                                               |
| Pusher                      | `pusher`                | [Documentation](/integrations/webhooks/pusher-webhooks)                                              |
| SendGrid                    | `sendgrid`              | [Documentation](/integrations/webhooks/sendgrid-webhooks)                                            |
| Sentry                      | `sentry`                | [Documentation](/integrations/webhooks/sentry-webhooks)                                              |
| Shopify                     | `shopify`               | [Documentation](/integrations/webhooks/shopify-webhooks)                                             |
| Signal Sciences             | `signal_sciences`       | [Documentation](/integrations/webhooks/signalsciences-webhooks)                                      |
| Slack                       | `slack`                 | [Documentation](/integrations/webhooks/slack-webhooks)                                               |
| Sonatype Nexus              | `sonatype`              | [Documentation](/integrations/webhooks/sonatype-nexus-webhooks)                                      |
| Square                      | `square`                | [Documentation](/integrations/webhooks/square-webhooks)                                              |
| Stripe                      | `stripe`                | [Documentation](/integrations/webhooks/stripe-webhooks)                                              |
| Svix                        | `svix`                  | [Documentation](/integrations/webhooks/svix-webhooks)                                                |
| Terraform                   | `terraform`             | [Documentation](/integrations/webhooks/terraform-webhooks)                                           |
| TikTok                      | `tiktok`                | [Documentation](/integrations/webhooks/tiktok-webhooks)                                              |
| Trend Micro Conformity      | `trendmicro_conformity` | [Documentation](/integrations/webhooks/trendmicro-webhooks)                                          |
| Twilio                      | `twilio`                | [Documentation](/integrations/webhooks/twilio-webhooks)                                              |
| Twitter                     | `twitter`               | [Documentation](/integrations/webhooks/twitter-webhooks)                                             |
| Typeform                    | `typeform`              | [Documentation](/integrations/webhooks/typeform-webhooks)                                            |
| VMware Workspace            | `vmware`                | [Documentation](/integrations/webhooks/vmware-webhooks)                                              |
| Webex                       | `webex`                 | [Documentation](/integrations/webhooks/webex-webhooks)                                               |
| WhatsApp                    | `whatsapp`              | [Documentation](/integrations/webhooks/whatsapp-webhooks)                                            |
| Worldline                   | `worldline`             | [Documentation](/integrations/webhooks/worldline-webhooks)                                           |
| Xero                        | `xero`                  | [Documentation](/integrations/webhooks/xero-webhooks)                                                |
| Zendesk                     | `zendesk`               | [Documentation](/integrations/webhooks/zendesk-webhooks)                                             |
| Zoom                        | `zoom`                  | [Documentation](/integrations/webhooks/zoom-webhooks)                                                |

## Examples

### Basic example

This example configuration sets up an endpoint (`gitlab-webhook-example.ngrok.app`) that receives webhook requests from GitLab. The **Verify Webhook** action checks the authenticity of the request using a shared secret. If the request is verified, a custom response is sent back with a status `200 OK` and a plain text confirmation message.

#### Example Traffic Policy document

<CodeGroup>
  ```yaml policy.yml theme={null}
  on_http_request:
    - actions:
        - type: verify-webhook
          config:
            provider: gitlab
            secret: secret!
        - type: custom-response
          config:
            status_code: 200
            headers:
              content-type: text/plain
            body: GitLab webhook verified
  ```

  ```json policy.json theme={null}
  {
    "on_http_request": [
      {
        "actions": [
          {
            "type": "verify-webhook",
            "config": {
              "provider": "gitlab",
              "secret": "secret!"
            }
          },
          {
            "type": "custom-response",
            "config": {
              "status_code": 200,
              "headers": {
                "content-type": "text/plain"
              },
              "body": "GitLab webhook verified"
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
ngrok http 8080 --url gitlab-webhook-example.ngrok.app --traffic-policy-file /path/to/policy.yml
```

```bash  theme={null}
$ curl --location --request POST 'https://gitlab-webhook-example.ngrok.app/' \
--header 'X-Gitlab-Token: secret!'
> POST / HTTP/2
> Host: gitlab-webhook-example.ngrok.app
> User-Agent: curl/[version]
> Accept: */*
> X-Gitlab-Token: secret!
...
```

This request will first be processed by the Verify Webhook action. If the GitLab webhook verification is successful, ngrok will return a `200 OK` response with the message GitLab webhook verified.

```bash  theme={null}
HTTP/2 200 OK
content-type: text/plain
GitLab webhook verified
```

## Action result variables

The following variables are made available for use in subsequent expressions and
CEL interpolations after the action has run. Variable values will only apply
to the last action execution, results are not concatenated.

<ConfigField title="actions.ngrok.verify_webhook.verified" type="bool">
  <p>Indicates whether or not the request was successfully verified.</p>
</ConfigField>

<ConfigField title="actions.ngrok.verify_webhook.error.code" type="string">
  <p>Code for an error that occurred during the invocation of an action.</p>
</ConfigField>

<ConfigField title="actions.ngrok.verify_webhook.error.message" type="string">
  <p>Message for an error that occurred during the invocation of an action.</p>
</ConfigField>


Built with [Mintlify](https://mintlify.com).