# Source: https://docs.firehydrant.com/docs/sentry-event-source.md

# Sentry Event Source

The Sentry Integration for Signals allows users to create events in FireHydrant from alerts in Sentry. Anytime Sentry sends an event to FireHydrant, we’ll evaluate it to see if it matches a rule set up by one of your teams. If there's a match, we’ll alert the team. Learn more about [Alert Rules](/docs/signals/alert-rules)  here.

### Configuring Sentry Webhook

1. In FireHydrant, navigate to the Signals Sources page (Signals > Sources). Here, you’ll find a webhook URL you will use when creating a webhook in Sentry.

<Image alt="Copy the Sentry URL" align="center" width="800px" src="https://files.readme.io/499b3b0-sentry-webhook.jpg">
  Copy the Sentry URL
</Image>

2. In Sentry, navigate to the Integrations page nested under Settings (`https://{your-org}.sentry.io/settings/integrations`). Search for the Webhooks integration and ensure that it's added to your project and enabled.
3. In the Callbacks URL field, enter the Signals webhooks URL that you copied in Step 1.
4. Click "Save Changes" to save your webhook.

### Adding Webhook to an Alert

In Sentry, you can add a webhook as a notification recipient for an Alert.

1. Navigate to the Alerts list using the left sidebar. Find or create an Alert Rule that you want to use to send Signals to FireHydrant.
2. If you're editing an existing Alert Rule, click into the Alert Rule by clicking on the title and then click Edit in the upper right corner.
3. Go to the Set Conditions step when creating or editing an Alert Rule. You can add an Action for "Send a Notification via an Integration." Make sure that Webhooks is the selected integration.
4. Save your rule; your alert is now set up to create Signals in FireHydrant.

### Testing your Sentry Webhook

1. When adding a webhook in Sentry, you can click the “Test” button to send a sample payload to your webhooks.
2. Additionally, when configuring the condition step for your alert rule, you can click Send Test Notification to send an alert-specific payload to FireHydrant.
3. Confirm that FireHydrant received your webhook by visiting **Alerting > Webhook Logs** in the web app. You should see a new event created. You can open the drawer to see the full payload from Sentry.

<Image align="center" src="https://files.readme.io/bfa9684-logs.jpg" />

## Field Mappings/Behaviors

The payload from Sentry will be directly mapped to FireHydrant's [Events Data Model](https://docs.firehydrant.com/docs/events-data-model). The following table explains the behavior once the payload hits our system:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Inbound Parameter
      </th>

      <th>
        FireHydrant Parameter
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `payload.event.event_id`
        *-OR-*
        `payload.message`
      </td>

      <td>
        `idempotency_key` - Checks for an event ID. If not supplied, will use the message as the key. If neither are supplied, then the idempotency key will be empty and a new alert will open
      </td>
    </tr>

    <tr>
      <td>
        `payload.message`
      </td>

      <td>
        `summary` - Uses the `message` if supplied, otherwise defaults to `Alert from Sentry`
      </td>
    </tr>

    <tr>
      <td>
        `payload.project_name` +\
        `payload.culprit`
      </td>

      <td>
        `body` - Will be a concatenation of Sentry project name and culprit if supplied, otherwise an empty string
      </td>
    </tr>

    <tr>
      <td>
        `payload.url`
      </td>

      <td>
        `links`
      </td>
    </tr>

    <tr>
      <td>
        `payload.event.tags`
      </td>

      <td>
        `tags` - FireHydrant will include images from any alerts in the payload that have a `imageURL` parameter
      </td>
    </tr>

    <tr>
      <td />

      <td>
        `status` - Always Open
      </td>
    </tr>
  </tbody>
</Table>

These mappings mean that an inbound webhook from Grafana with the following content:

```json Sentry Payload
{
  "id": "4702139292",
  "project": "javascript-nextjs",
  "project_name": "javascript-nextjs",
  "project_slug": "javascript-nextjs",
  "logger": null,
  "level": "warning",
  "culprit": "raven.scripts.runner in main",
  "message": "This is an example Python exception",
  "url": "https://some-organization.sentry.io/issues/123456789/?referrer=webhooks_plugin",
  "triggering_rules": [],
  "event": {
    "event_id": "7038dbaacc8d4dd38369d11c32fa0dfa",
    "level": "error",
    "version": "5",
    "type": "default",
    "logentry": {
      "formatted": "This is an example Python exception",
      "message": null,
      "params": null
    },
    "logger": "",
    "modules": {
      "my.package": "1.0.0"
    },
    "platform": "python",
    "timestamp": 1706892630.71,
    "received": 1706892690.711345,
    "environment": "prod",
    "user": {
      "id": "1",
      "email": "sentry@example.com",
      "ip_address": "127.0.0.1",
      "username": "sentry",
      "name": "Sentry",
      "geo": {
        "country_code": "US",
        "city": "San Francisco",
        "region": "CA"
      }
    },
    "request": {
      "url": "http://example.com/foo",
      "method": "GET",
      "data": {
        "hello": "world"
      },
      "query_string": [
        [
          "foo",
          "bar"
        ]
      ],
      "cookies": [
        [
          "foo",
          "bar"
        ],
        [
          "biz",
          "baz"
        ]
      ],
      "headers": [
        [
          "Content-Type",
          "application/json"
        ],
        [
          "Referer",
          "http://example.com"
        ],
        [
          "User-Agent",
          "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36"
        ]
      ],
      "env": {
        "ENV": "prod"
      },
      "inferred_content_type": "application/json",
      "api_target": null,
      "fragment": null
    },
    "contexts": {
      "browser": {
        "name": "Chrome",
        "version": "28.0.1500",
        "type": "browser"
      },
      "client_os": {
        "name": "Windows",
        "version": "8",
        "type": "os"
      }
    },
    "stacktrace": {
      "frames": [
        {
          "function": "build_msg",
          "module": "raven.base",
          "filename": "raven/base.py",
          "abs_path": "/home/ubuntu/.virtualenvs/getsentry/src/raven/raven/base.py",
          "lineno": 303,
          "pre_context": [
            "                frames = stack",
            "",
            "            data.update({",
            "                'sentry.interfaces.Stacktrace': {",
            "                    'frames': get_stack_info(frames,"
          ],
          "context_line": "                        transformer=self.transform)",
          "post_context": [
            "                },",
            "            })",
            "",
            "        if 'sentry.interfaces.Stacktrace' in data:",
            "            if self.include_paths:"
          ],
          "in_app": false,
          "vars": {
            "'culprit'": null,
            "'data'": {
              "'message'": "u'This is a test message generated using ``raven test``'",
              "'sentry.interfaces.Message'": {
                "'message'": "u'This is a test message generated using ``raven test``'",
                "'params'": []
              }
            },
            "'date'": "datetime.datetime(2013, 8, 13, 3, 8, 24, 880386)",
            "'event_id'": "'54a322436e1b47b88e239b78998ae742'",
            "'event_type'": "'raven.events.Message'",
            "'extra'": {
              "'go_deeper'": [
                [
                  "{\"'bar'\":[\"'baz'\"],\"'foo'\":\"'bar'\"}"
                ]
              ],
              "'loadavg'": [
                0.37255859375,
                0.5341796875,
                0.62939453125
              ],
              "'user'": "'dcramer'"
            },
            "'frames'": "<generator object iter_stack_frames at 0x107bcc3c0>",
            "'handler'": "<raven.events.Message object at 0x107bd0890>",
            "'k'": "'sentry.interfaces.Message'",
            "'kwargs'": {
              "'level'": 20,
              "'message'": "'This is a test message generated using ``raven test``'"
            },
            "'public_key'": null,
            "'result'": {
              "'message'": "u'This is a test message generated using ``raven test``'",
              "'sentry.interfaces.Message'": {
                "'message'": "u'This is a test message generated using ``raven test``'",
                "'params'": []
              }
            },
            "'self'": "<raven.base.Client object at 0x107bb8210>",
            "'stack'": true,
            "'tags'": null,
            "'time_spent'": null,
            "'v'": {
              "'message'": "u'This is a test message generated using ``raven test``'",
              "'params'": []
            }
          },
          "colno": null,
          "data": null,
          "errors": null,
          "raw_function": null,
          "image_addr": null,
          "instruction_addr": null,
          "addr_mode": null,
          "package": null,
          "platform": null,
          "source_link": null,
          "symbol": null,
          "symbol_addr": null,
          "trust": null,
          "snapshot": null,
          "lock": null
        },
        {
          "function": "capture",
          "module": "raven.base",
          "filename": "raven/base.py",
          "abs_path": "/home/ubuntu/.virtualenvs/getsentry/src/raven/raven/base.py",
          "lineno": 459,
          "pre_context": [
            "        if not self.is_enabled():",
            "            return",
            "",
            "        data = self.build_msg(",
            "            event_type, data, date, time_spent, extra, stack, tags=tags,"
          ],
          "context_line": "            **kwargs)",
          "post_context": [
            "",
            "        self.send(**data)",
            "",
            "        return (data.get('event_id'),)",
            ""
          ],
          "in_app": false,
          "vars": {
            "'data'": null,
            "'date'": null,
            "'event_type'": "'raven.events.Message'",
            "'extra'": {
              "'go_deeper'": [
                [
                  "{\"'bar'\":[\"'baz'\"],\"'foo'\":\"'bar'\"}"
                ]
              ],
              "'loadavg'": [
                0.37255859375,
                0.5341796875,
                0.62939453125
              ],
              "'user'": "'dcramer'"
            },
            "'kwargs'": {
              "'level'": 20,
              "'message'": "'This is a test message generated using ``raven test``'"
            },
            "'self'": "<raven.base.Client object at 0x107bb8210>",
            "'stack'": true,
            "'tags'": null,
            "'time_spent'": null
          },
          "colno": null,
          "data": null,
          "errors": null,
          "raw_function": null,
          "image_addr": null,
          "instruction_addr": null,
          "addr_mode": null,
          "package": null,
          "platform": null,
          "source_link": null,
          "symbol": null,
          "symbol_addr": null,
          "trust": null,
          "snapshot": null,
          "lock": null
        },
        {
          "function": "captureMessage",
          "module": "raven.base",
          "filename": "raven/base.py",
          "abs_path": "/home/ubuntu/.virtualenvs/getsentry/src/raven/raven/base.py",
          "lineno": 577,
          "pre_context": [
            "        \"\"\"",
            "        Creates an event from ``message``.",
            "",
            "        >>> client.captureMessage('My event just happened!')",
            "        \"\"\""
          ],
          "context_line": "        return self.capture('raven.events.Message', message=message, **kwargs)",
          "post_context": [
            "",
            "    def captureException(self, exc_info=None, **kwargs):",
            "        \"\"\"",
            "        Creates an event from an exception.",
            ""
          ],
          "in_app": false,
          "vars": {
            "'kwargs'": {
              "'data'": null,
              "'extra'": {
                "'go_deeper'": [
                  "[{\"'bar'\":[\"'baz'\"],\"'foo'\":\"'bar'\"}]"
                ],
                "'loadavg'": [
                  0.37255859375,
                  0.5341796875,
                  0.62939453125
                ],
                "'user'": "'dcramer'"
              },
              "'level'": 20,
              "'stack'": true,
              "'tags'": null
            },
            "'message'": "'This is a test message generated using ``raven test``'",
            "'self'": "<raven.base.Client object at 0x107bb8210>"
          },
          "colno": null,
          "data": null,
          "errors": null,
          "raw_function": null,
          "image_addr": null,
          "instruction_addr": null,
          "addr_mode": null,
          "package": null,
          "platform": null,
          "source_link": null,
          "symbol": null,
          "symbol_addr": null,
          "trust": null,
          "snapshot": null,
          "lock": null
        },
        {
          "function": "send_test_message",
          "module": "raven.scripts.runner",
          "filename": "raven/scripts/runner.py",
          "abs_path": "/home/ubuntu/.virtualenvs/getsentry/src/raven/raven/scripts/runner.py",
          "lineno": 77,
          "pre_context": [
            "        level=logging.INFO,",
            "        stack=True,",
            "        tags=options.get('tags', {}),",
            "        extra={",
            "            'user': get_uid(),"
          ],
          "context_line": "            'loadavg': get_loadavg(),",
          "post_context": [
            "        },",
            "    ))",
            "",
            "    if client.state.did_fail():",
            "        print('error!')"
          ],
          "in_app": false,
          "vars": {
            "'client'": "<raven.base.Client object at 0x107bb8210>",
            "'data'": null,
            "'k'": "'secret_key'",
            "'options'": {
              "'data'": null,
              "'tags'": null
            }
          },
          "colno": null,
          "data": null,
          "errors": null,
          "raw_function": null,
          "image_addr": null,
          "instruction_addr": null,
          "addr_mode": null,
          "package": null,
          "platform": null,
          "source_link": null,
          "symbol": null,
          "symbol_addr": null,
          "trust": null,
          "snapshot": null,
          "lock": null
        },
        {
          "function": "main",
          "module": "raven.scripts.runner",
          "filename": "raven/scripts/runner.py",
          "abs_path": "/home/ubuntu/.virtualenvs/getsentry/src/raven/raven/scripts/runner.py",
          "lineno": 112,
          "pre_context": [
            "    print(\"Using DSN configuration:\")",
            "    print(\" \", dsn)",
            "    print()",
            "",
            "    client = Client(dsn, include_paths=['raven'])"
          ],
          "context_line": "    send_test_message(client, opts.__dict__)",
          "in_app": false,
          "vars": {
            "'args'": [
              "'test'",
              "'https://ebc35f33e151401f9deac549978bda11:f3403f81e12e4c24942d505f086b2cad@sentry.io/1'"
            ],
            "'client'": "<raven.base.Client object at 0x107bb8210>",
            "'dsn'": "'https://ebc35f33e151401f9deac549978bda11:f3403f81e12e4c24942d505f086b2cad@sentry.io/1'",
            "'opts'": "<Values at 0x107ba3b00: {'data': None, 'tags': None}>",
            "'parser'": "<optparse.OptionParser instance at 0x107ba3368>",
            "'root'": "<logging.Logger object at 0x107ba5b10>"
          },
          "colno": null,
          "data": null,
          "errors": null,
          "raw_function": null,
          "image_addr": null,
          "instruction_addr": null,
          "addr_mode": null,
          "package": null,
          "platform": null,
          "post_context": null,
          "source_link": null,
          "symbol": null,
          "symbol_addr": null,
          "trust": null,
          "snapshot": null,
          "lock": null
        }
      ]
    },
    "tags": [
      [
        "browser",
        "Chrome 28.0.1500"
      ],
      [
        "browser.name",
        "Chrome"
      ],
      [
        "client_os",
        "Windows 8"
      ],
      [
        "client_os.name",
        "Windows"
      ],
      [
        "environment",
        "prod"
      ],
      [
        "level",
        "error"
      ],
      [
        "sentry:user",
        "id:1"
      ],
      [
        "server_name",
        "web01.example.org"
      ],
      [
        "url",
        "http://example.com/foo"
      ]
    ],
    "extra": {
      "emptyList": [],
      "emptyMap": {},
      "length": 10837790,
      "results": [
        1,
        2,
        3,
        4,
        5
      ],
      "session": {
        "foo": "bar"
      },
      "unauthorized": false,
      "url": "http://example.org/foo/bar/"
    },
    "metadata": {
      "title": "This is an example Python exception",
      "in_app_frame_mix": "system-only"
    },
    "fingerprint": [
      "{{ default }}"
    ],
    "hashes": [
      "3a2b45089d0211943e5a6645fb4cea3f"
    ],
    "culprit": "raven.scripts.runner in main",
    "title": "This is an example Python exception",
    "location": null,
    "_ref": 4506345989931008,
    "_ref_version": 2,
    "_metrics": {
      "bytes.stored.event": 8255
    },
    "nodestore_insert": 1706892691.483273,
    "id": "7038dbaacc8d4dd38369d11c32fa0dfa"
  }
}
```

Will be transposed to the following FireHydrant Signal:

```json Transposed Signal
{
  "summary": "This is an example Python exception",
  "body": "javascript-nextjs raven.scripts.runner in main",
  "level": 1,
  "links": [
    {
      "href": "https://some-organization.sentry.io/issues/123456789/?referrer=webhooks_plugin",
      "text": "Sentry Trigger"
    }
  ],
  "tags": ["browser:Chrome 28.0.1500", "browser.name:Chrome", "client_os:Windows 8", "client_os.name:Windows", "environment:prod", "level:error", "sentry:user:id:1", "server_name:web01.example.org", "url:http://example.com/foo"],
  "idempotency_key": "7038dbaacc8d4dd38369d11c32fa0dfa"
}
```