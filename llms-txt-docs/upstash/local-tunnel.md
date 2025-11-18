# Source: https://upstash.com/docs/workflow/howto/local-development/local-tunnel.md

# Source: https://upstash.com/docs/qstash/howto/local-tunnel.md

# Source: https://upstash.com/docs/workflow/howto/local-development/local-tunnel.md

# Local Tunnel

Upstash Workflow requires your application to be publicly accessible in production.
The recommended approach is running the development server we provide locally and work with local addresses.
An alternative is to making your application publibly accessible so that you can work with the managed Upstash Workflow servers.

The easiest way to make a local URL publically available is [ngrok](https://ngrok.com), a free tunneling service.

Create an account on [dashboard.ngrok.com/signup](https://dashboard.ngrok.com/signup) and follow the [setup instructions](https://dashboard.ngrok.com/get-started/setup) to download the ngrok CLI and connect your account. This process takes only a few minutes and is totally free.

You can connect your account like this:

<Tabs>
  <Tab title="macOS">
    <Frame>
      <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/ngrok_mac_setup.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=b97dd2ce9a636055d0fb70f7b84b5bf1" data-og-width="1260" width="1260" data-og-height="693" height="693" data-path="img/qstash-workflow/ngrok_mac_setup.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/ngrok_mac_setup.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=3df753a45601667ae89c8658d3c48253 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/ngrok_mac_setup.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=766620735f6509619dd325093044e6ed 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/ngrok_mac_setup.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=fcf3a57b8a88fc786855e54e9e1a253e 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/ngrok_mac_setup.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=d088accb952cab4e7fe961b130e1132c 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/ngrok_mac_setup.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=817261037ab60ebd44f90b8fadfb041c 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/ngrok_mac_setup.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=c4de622057b2c6a4679a3f560b332cc6 2500w" />
    </Frame>
  </Tab>

  <Tab title="Windows">
    <Frame>
      <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/ngrok_windows_setup.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=757344c0a66d7d545bc423d323d9345c" data-og-width="1260" width="1260" data-og-height="693" height="693" data-path="img/qstash-workflow/ngrok_windows_setup.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/ngrok_windows_setup.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=1286eb457ab23c519f1c41fd43151c88 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/ngrok_windows_setup.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=8c3be6746de77bdc207a57d165990706 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/ngrok_windows_setup.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=8f3927b79c7268496c02b7c1d2935abc 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/ngrok_windows_setup.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=b437d1540af03f06881153f4c6fe58da 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/ngrok_windows_setup.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=a5c51508451cf37c0015bb1f59e04dbd 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/ngrok_windows_setup.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=987842abc4a3e7b94841882db40078b4 2500w" />
    </Frame>
  </Tab>
</Tabs>

Once you have installed the ngrok CLI, add your ngrok-issued auth token like this:

```bash Terminal theme={"system"}
ngrok config add-authtoken <YOUR-AUTH-TOKEN>
```

and replace `<YOUR-AUTH-TOKEN>` with your actual auth token.

### Start the tunnel

Make your local server available publically by running the following command:

```bash  theme={"system"}
ngrok http <PORT>
```

for example, if your Next.js server is running on port `3000`, the command is:

```bash  theme={"system"}
ngrok http 3000
```

The output will look something like this:

```plaintext  theme={"system"}
Session Status                online
Account                       <YOUR-NAME> (Plan: Free)
Version                       3.1.0
Region                        Europe (eu)
Latency                       -
Web Interface                 http://127.0.0.1:4040
Forwarding                    https://e02f-2a02-810d-af40-5284-b139-58cc-89df-b740.eu.ngrok.io -> http://localhost:3000
Connections                   ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00
```

The long URL in the `Forwarding` line serves the same purpose as your localhost URL, the only difference being that it is publically accessible. We need this URL to make our workflow available to QStash for local development, either as the `baseUrl` parameter or the `UPSTASH_WORKFLOW_URL` environment variable (both options provide the same functionality).

Note: The `UPSTASH_WORKFLOW_URL` environment variable is only necessary for local development. In production, the `baseUrl` parameter is automatically set and can be omitted.

<Tip>
  Ensure that the port of your local server matches the one you're using with ngrok. For example, if your server is
  running on port 8080, use `ngrok http 8080`.
</Tip>
