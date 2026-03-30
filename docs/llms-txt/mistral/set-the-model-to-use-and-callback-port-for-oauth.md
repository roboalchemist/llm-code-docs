# Set the model to use and callback port for OAuth
MODEL = "mistral-medium-latest"
CALLBACK_PORT = 16010
```

#### Step 2: Set Up Callback Server

We set up a callback server to handle OAuth responses.

```python
def run_callback_server(callback_func):
    # Set up a callback server to handle OAuth responses
    auth_response: dict = {"url": ""}

    class OAuthCallbackHandler(BaseHTTPRequestHandler):
        server_version = "HTTP"
        code = None

        def do_GET(self):
            if "/callback" in self.path:
                try:
                    auth_response["url"] = self.path
                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    callback_func()
                    response_html = "<html><body><p>You may now close this window.</p></body></html>"
                    self.wfile.write(response_html.encode())
                    threading.Thread(target=httpd.shutdown).start()
                except Exception:
                    self.send_response(500)
                    self.end_headers()

    server_address = ("localhost", CALLBACK_PORT)
    httpd = HTTPServer(server_address, OAuthCallbackHandler)
    threading.Thread(target=httpd.serve_forever).start()
    redirect_url = f"http://localhost:{CALLBACK_PORT}/oauth/callback"
    return httpd, redirect_url, auth_response
```

#### Step 3: Define Server URL and Create MCP Client

We define the URL for the remote MCP server and create an MCP client to connect to it.

```python
async def main():
    # Initialize the Mistral client with your API key
    api_key = os.environ["MISTRAL_API_KEY"]
    client = Mistral(api_key)

    # Define the URL for the remote MCP server
    server_url = "https://mcp.linear.app/sse"
    mcp_client = MCPClientSSE(sse_params=SSEServerParams(url=server_url))
```

#### Step 4: Handle Authentication

We handle the authentication process, including setting up a callback event and event loop, checking if authentication is required, and managing the OAuth flow.

```python
    # Set up a callback event and event loop
    callback_event = asyncio.Event()
    event_loop = asyncio.get_event_loop()

    # Check if authentication is required
    if await mcp_client.requires_auth():
        # Set up a callback server and handle OAuth flow
        httpd, redirect_url, auth_response = run_callback_server(
            callback_func=lambda: event_loop.call_soon_threadsafe(callback_event.set)
        )
        try:
            # Build OAuth parameters and get the login URL
            oauth_params = await build_oauth_params(
                mcp_client.base_url, redirect_url=redirect_url
            )
            mcp_client.set_oauth_params(oauth_params=oauth_params)
            login_url, state = await mcp_client.get_auth_url_and_state(redirect_url)

            # Open the login URL in a web browser
            print("Please go to this URL and authorize the application:", login_url)
            webbrowser.open(login_url, new=2)
            await callback_event.wait()

            # Exchange the authorization code for a token
            mcp_client = MCPClientSSE(
                sse_params=SSEServerParams(url=server_url),
                oauth_params=oauth_params,
            )

            token = await mcp_client.get_token_from_auth_response(
                auth_response["url"], redirect_url=redirect_url, state=state
            )
            mcp_client.set_auth_token(token)

        except Exception as e:
            print(f"Error during authentication: {e}")
        finally:
            httpd.shutdown()
            httpd.server_close()
```

#### Step 5: Create a Run Context and Register MCP Client

We create a Run Context for the agent and register the MCP client with it.

```python
    # Create a run context for the agent
    async with RunContext(
        model=MODEL,
    ) as run_ctx:
        # Register the MCP client with the run context
        await run_ctx.register_mcp_client(mcp_client=mcp_client)
```

#### Step 6: Run the Agent and Print Results

Finally, we run the agent with a query and print the results.

```python
        # Run the agent with a query
        run_result = await client.beta.conversations.run_async(
            run_ctx=run_ctx,
            inputs="Tell me which projects do I have in my workspace?",
        )

        # Print the final response
        print(f"Final Response: {run_result.output_as_text}")

if __name__ == "__main__":
    asyncio.run(main())
```

  </TabItem>
</Tabs>

### Streaming Conversations

Streaming conversations with an agent using a local MCP server is similar to non-streaming, but instead of waiting for the entire response, you process the results as they arrive.

Here is a brief example of how to stream conversations:

```python
    # Stream the agent's responses
    events = await client.beta.conversations.run_stream_async(
        run_ctx=run_ctx,
        inputs="Tell me the weather in John's location currently.",
    )

    # Process the streamed events
    run_result = None
    async for event in events:
        if isinstance(event, RunResult):
            run_result = event
        else:
            print(event)

    if not run_result:
        raise RuntimeError("No run result found")

    # Print the results
    print("All run entries:")
    for entry in run_result.output_entries:
        print(f"{entry}")
    print(f"Final model: {run_result.output_as_model}")
```


[Audio & Transcription]
Source: https://docs.mistral.ai/docs/capabilities/audio_and_transcription

Audio input capabilities enable models to chat and understand audio directly, this can be used for both chat use cases via audio or for optimal transcription purposes.

<div style={{ textAlign: 'center' }}>
  <img
    src="/img/audio.png"
    alt="audio_graph"
    width="500"
    style={{ borderRadius: '15px' }}
  />
</div>

### Models with Audio Capabilities
Audio capable models:
- **Voxtral Small** (`voxtral-small-latest`) with audio input for [chat](#chat-with-audio) use cases.
- **Voxtral Mini** (`voxtral-mini-latest`) with audio input for [chat](#chat-with-audio) use cases
- And **Voxtral Mini Transcribe** (`voxtral-mini-latest` via `audio/transcriptions`), with an efficient [transcription](#transcription) only service.

## Chat with Audio

Our Voxtral models are capable of being used for chat use cases with our chat completions endpoint.

### Passing an Audio File

To pass a local audio file, you can encode it in base64 and pass it as a string.

<Tabs groupId="code">
  <TabItem value="python" label="python">

```python

from mistralai import Mistral