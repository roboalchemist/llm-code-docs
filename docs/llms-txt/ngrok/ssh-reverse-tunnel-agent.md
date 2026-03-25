# Source: https://ngrok.com/docs/agent/ssh-reverse-tunnel-agent.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# SSH Reverse Tunnel

> Learn how to deliver ngrok's services using SSH Reverse Tunneling rather than the ngrok agent.

SSH reverse tunneling (`ssh -R`) is an alternative mechanism to deliver services
via ngrok without running an [ngrok agent](/agent/) or [Agent
SDK](/agent-sdks/).

The SSH reverse tunnel agent should not be confused with creating remote access
to an SSH server via ngrok. If you want to use ngrok to create access to your
own SSH server for remote access, please refer to the [using ngrok with
ssh](/guides/ssh-rdp/) documentation.

You should only ngrok via SSH if you really can't use an Agent or Agent SDK.
The SSH reverse tunnel agent has [many functional limitations compared to the
ngrok agent](#differences).

## Example usage

### Random HTTP endpoint

```bash  theme={null}
ssh -R 443:localhost:80 v2@connect.ngrok-agent.com http
```

### Custom Domain

```bash  theme={null}
ssh -R example.ngrok.app:443:localhost:8080 v2@connect.ngrok-agent.com http
```

### Basic Auth

```bash  theme={null}
ssh -R 443:localhost:80 v2@connect.ngrok-agent.com http \
  --basic-auth "username1:password1" \
  --basic-auth "username2:password2"
```

### OAuth

When creating a reverse tunnel, you must provide a publicly accessible URL to your traffic policy file, as shown in this example.

First, create the `oauth-policy.yml` file:

```yaml  theme={null}
on_http_request:
  - actions:
      - type: oauth
        config:
          provider: google
```

Store this file at a publicly accessible address online. For example, you could add it to a github repository.

Finally, add your traffic policy to your reverse tunnel using the `--traffic-policy-url` flag.

```bash  theme={null}
ssh -R 443:localhost:80 v2@connect.ngrok-agent.com http --traffic-policy-url=https://some-website/oauth-policy.yml
```

### Forward to non-local service

```bash  theme={null}
ssh -R 0:192.168.1.2:80 v2@connect.ngrok-agent.com http
```

### Random TCP Endpoint

```bash  theme={null}
ssh -R 0:localhost:22 v2@connect.ngrok-agent.com tcp
```

### Fixed TCP Endpoint

```bash  theme={null}
ssh -R 1.tcp.eu.ngrok.io:12345:localhost:3389 connect.eu.ngrok-agent.com tcp
```

### TLS Endpoint

```bash  theme={null}
ssh -R app.example.com:443:localhost:443 v2@connect.ngrok-agent.com tls
```

### Explicit Region Selection

Normally you will connect to ngrok's closest point of presence via the [Global
Load Balancer](/universal-gateway/global-load-balancer/), but you can also
explicitly choose a region.

```bash  theme={null}
ssh -R 443:localhost:80 v2@connect.eu.ngrok-agent.com http
```

## Authentication

Instead of an ngrok authtoken, when you use ngrok via the SSH reverse tunnel
agent, it uses a public key for authentication. You'll first need to upload
yours to the [SSH Public Keys page on your ngrok
dashboard](https://dashboard.ngrok.com/tunnels/ssh-keys).

Copy your default SSH public key with:

<Tabs>
  <Tab title="Mac OS">
    ```bash  theme={null}
    cat ~/.ssh/id_rsa.pub | pbcopy
    ```

    or:

    ```bash  theme={null}
    cat ~/.ssh/id_ed25519.pub | pbcopy
    ```
  </Tab>

  <Tab title="Linux">
    ```bash  theme={null}
    cat ~/.ssh/id_rsa.pub
    ```

    or:

    ```bash  theme={null}
    cat ~/.ssh/id_ed25519.pub
    ```
  </Tab>
</Tabs>

## ngrok's SSH public key fingerprints

Public key fingerprints can be used to validate a connection to the ngrok point of presence you're connecting through. These are the RSA public key fingerprints:

* connect.ap.ngrok-agent.com: `SHA256:K/3UwSeIg0JVf9uLVfl4QLEY11tyON/d+QmLfIU0fmk`
* connect.au.ngrok-agent.com: `SHA256:RpCOpodROXqXy4d0SIm7rAqwEUsmmUHA6NAQ6T4EHXY`
* connect.eu.ngrok-agent.com: `SHA256:OeywYk1/2w9cOg8Q3FjbsMOe2Hc9CvxbyBhDdUBBOlQ`
* connect.in.ngrok-agent.com: `SHA256:acotuxa/+tJY2vmK+VeLQIoVOJLQz/VLTmHTJ/0LPaI`
* connect.jp.ngrok-agent.com: `SHA256:/6j2cYqVbjO9YvEKKXTOqHlND72fCms0sdVWClHJAks`
* connect.sa.ngrok-agent.com: `SHA256:Wh3W1ub0J/eda2QcEPbrVgS6mdGxIUrbao9G5zMBvdc`
* connect.us-cal-1.ngrok-agent.com: `SHA256:UwLN719B+xJVKMtcsZL3cqiuY7iYpoxLNg1k5Pqdf2g`
* connect.us.ngrok-agent.com: `SHA256:WuVeeGNOGVrcMe/GcdsTUB135MFCe1/aaVYXrpCxSEM`

## Command syntax

ngrok does its best to honor the syntax of `ssh -R`. You may wish to consult
`man ssh`, and the section devoted to the `-R` option for additional details.
ngrok uses additional command line options to implement features that are not
otherwise available via the `-R` syntax.

Consider the following command:

```bash  theme={null}
ssh -R \
  app.example.com:443:127.0.0.1:8080 \
  v2@connect.ngrok-agent.com \
  http --basic-auth 'user:password'
```

An `ssh -R` command has the following components:

```bash  theme={null}
ssh -R \
  "<remote name>:<remote port>:<local name>:<local port>" \
  <user>@connect.ngrok-agent.com \
  <command> [flags]
```

In this example:

* Remote Name: `app.example.com`. ngrok will listen on the domain 'app.example.com'. You may omit this value. If you do, ngrok chooses a random endpoint name.
* Remote Port: `443`. ngrok will listen for HTTPS traffic on port 443. The only
  valid values for HTTP endpoints are 80 and 443. For TLS endpoints it must be 443. You may `0` and ngrok will simply choose the appropriate port for you.
* Local Name: `127.0.0.1`. This is the local hostname or IP address that traffic will be sent to. It's most commonly `localhost`.
* Local Port: `8080`. This is the local port that traffic will be sent to.
* User: `v2`. ngrok uses the user portion of the command to version the command options. You may omit this value. If you do, ngrok will use the latest version.
* Command: `http`. This the type of endpoint to create. ngrok accepts either `http`, `tls` or `tcp`. This value is required.
* Flags: `--basic-auth 'user:password'`. Run the same command with the `--help` flag to get the list of supported flags or consult the [Agent CLI reference](/agent/cli/).

## Versioning

ngrok uses the user portion of the SSH command to version the CLI syntax. The
latest version is `v2`.

## Differences from the Agent

When you use ngrok via SSH reverse tunnel, you will need to [upload an SSH
public key](#authentication) to authenticate with instead of using an
ngrok authtoken like the agent.

Additionally, you'll find that using ngrok via SSH has many functional
limitations compared to the experience with the agent. An incomplete list of
differences from the ngrok agent includes:

* Your endpoints won't automatically reconnect if there is a network interruption
* There is no equivalent to the agent's [traffic inspection interface](/agent/web-inspection-interface/)
* You can't create endpoints for multiple services with the same command
* You can't [forward to upstream https services](/universal-gateway/http/#https-forwarding)
* You can't create multiple endpoints over the same connection
* You can't [serve file system directories](/universal-gateway/http/#serving-file-directories) with the `file://` protocol
* You can't terminate TLS at the agent when using [end-to-end encryption](/universal-gateway/tls-termination/#end-to-end-encryption)

## Pricing

The SSH reverse tunnel agent is available to all ngrok users at no additional
charge. You only incur costs if resources you provision via its usage incur a
cost. For more information, see the [ngrok Pricing page](https://ngrok.com/pricing).


Built with [Mintlify](https://mintlify.com).