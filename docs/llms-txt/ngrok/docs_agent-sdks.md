# Source: https://ngrok.com/docs/agent-sdks/index.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Agent SDKs

> Learn about ngrok Agent SDKs for embedding ngrok directly into your applications using Go, JavaScript, Python, and Rust libraries.

Agent SDKs enable you to embed ngrok directly into your application. They allow
you to programmatically create ngrok endpoints. You handle connections from
ngrok's cloud service just as if you opened a socket to listen on a port.

## Example usage

<Tabs>
  <Tab title="Go">
    1. Install the SDK:

       ```sh  theme={null}
       go get golang.ngrok.com/ngrok/v2
       ```

    2. Add the following to your app:

       ```go  theme={null}
       import "golang.ngrok.com/ngrok/v2"

       func connectNgrok() {
           fwd, err := ngrok.Forward(context.Background(),
               ngrok.WithUpstream("http://localhost:8085"),
           )
           if err != nil {
               log.Fatal(err)
           }
           log.Println("Available at:", fwd.URL())
           select {}
       }
       ```

    3. Set your authtoken and restart your app:

       ```sh  theme={null}
       export NGROK_AUTHTOKEN=<token>
       ```
  </Tab>

  <Tab title="JavaScript">
    1. Install the SDK:

       ```sh  theme={null}
       npm install @ngrok/ngrok
       ```

    2. Add the following to your app:

       ```js  theme={null}
       const ngrok = require("@ngrok/ngrok");

       async function forwardToApp() {
         const forwarder = await ngrok.forward({
           addr: "localhost:8085",
           authtoken_from_env: true,
         });
         console.log(`Available at: ${forwarder.url()}`);
       }
       ```

    3. Set your authtoken and restart your app:

       ```sh  theme={null}
       export NGROK_AUTHTOKEN=<token>
       ```
  </Tab>

  <Tab title="Python">
    1. Install the SDK:

       ```sh  theme={null}
       pip install ngrok
       ```

    2. Add the following to your app:

       ```python  theme={null}
       import ngrok

       def connect_ngrok():
           forwarder = ngrok.forward("localhost:8085", authtoken_from_env=True)
           print(f"Available at: {forwarder.url()}")
       ```

    3. Set your authtoken and restart your app:

       ```sh  theme={null}
       export NGROK_AUTHTOKEN=<token>
       ```
  </Tab>

  <Tab title="Rust">
    1. Install the SDK:

       ```sh  theme={null}
       cargo add ngrok
       ```

    2. Add the following to your app:

       ```rust  theme={null}
       use ngrok::config::ForwarderBuilder;
       use ngrok::prelude::*;
       use url::Url;

       async fn connect_ngrok() -> Result<(), Box<dyn std::error::Error + Send + Sync>> {
           let sess = ngrok::Session::builder()
               .authtoken_from_env()
               .connect()
               .await?;

           let mut listener = sess
               .http_endpoint()
               .listen_and_forward(Url::parse("http://localhost:8085")?)
               .await?;

           println!("Available at: {:?}", listener.url());

           let _ = listener.join().await;
           Ok(())
       }
       ```

    3. Set your authtoken and restart your app:

       ```sh  theme={null}
       export NGROK_AUTHTOKEN=<token>
       ```
  </Tab>
</Tabs>

## Supported languages

| Language   | Docs                                                               | Quickstart                                      | Repository                                                                     | Status |
| ---------- | ------------------------------------------------------------------ | ----------------------------------------------- | ------------------------------------------------------------------------------ | ------ |
| Go         | [ngrok-go docs](https://pkg.go.dev/golang.ngrok.com/ngrok/v2)      | [ngrok-go quickstart](/getting-started/go/)     | [github.com/ngrok/ngrok-go](https://github.com/ngrok/ngrok-go)                 | Stable |
| Rust       | [ngrok-rust docs](https://docs.rs/ngrok/latest/ngrok/)             | [ngrok-rust quickstart](/getting-started/rust/) | [github.com/ngrok/ngrok-rust](https://github.com/ngrok/ngrok-rust)             | Stable |
| Python     | [ngrok-python docs](https://ngrok.github.io/ngrok-python/)         |                                                 | [github.com/ngrok/ngrok-python](https://github.com/ngrok/ngrok-python)         | Stable |
| JavaScript | [ngrok-javascript docs](https://ngrok.github.io/ngrok-javascript/) |                                                 | [github.com/ngrok/ngrok-javascript](https://github.com/ngrok/ngrok-javascript) | Stable |
| Java       |                                                                    |                                                 | [github.com/ngrok/ngrok-java](https://github.com/ngrok/ngrok-java)             | Alpha  |

## When to use Agent SDKs

Agent SDKs are often a better fit for your use case over using the [ngrok
agent](/agent/). This is especially true when running ngrok with
production apps. Agent SDKs are a better choice if:

* You don't want to manage the lifetime of a separate agent process
* You don't want to bundle and distribute the ngrok agent
* The ngrok agent doesn't run on your target platform
* The ngrok agent's resource requirements are too high for your target platform
* You want fine-grained programmatic control over the agent's functionality

## Pricing

The agent SDKs are available to all ngrok users at no additional charge. You
only incur costs if the resources provisioned by the SDKs incur a cost. For more information, see the [ngrok Pricing page](https://ngrok.com/pricing).


Built with [Mintlify](https://mintlify.com).