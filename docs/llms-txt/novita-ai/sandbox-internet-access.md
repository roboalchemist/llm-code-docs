# Source: https://novita.ai/docs/guides/sandbox-internet-access.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Internet access

export const SandboxConfigHint = () => {
  if (typeof document === "undefined") {
    return null;
  } else {
    return <Note>Before running the example code in this document, please ensure you have properly configured environment variables. For details, please refer to <a href="/guides/sandbox-your-first-agent-sandbox#configure-environment-variables">Configure Environment Variables</a>.</Note>;
  }
};

Every sandbox has access to the internet and can be reached by a public URL.

<SandboxConfigHint />

## Sandbox public URL

Every sandbox has a public URL that can be used to access running services inside the sandbox.

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox } from 'novita-sandbox/code-interpreter'

  const sandbox = await Sandbox.create()

  // You need to always pass a port number to get the host
  const host = sandbox.getHost(3000)
  console.log(`https://${host}`)

  // Example output:
  // https://3000-idpw1qdrbcciscn2r8lw7-82b888ba.sandbox.novita.ai

  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.code_interpreter import Sandbox

  sandbox = Sandbox.create()

  # You need to always pass a port number to get the host
  host = sandbox.get_host(3000)
  print(f'https://{host}')

  # Example output:
  # https://3000-i9y92beaqiyor8x3josfy-82b888ba.sandbox.novita.ai

  sandbox.kill()
  ```
</CodeGroup>

The first leftmost part of the host is the port number we passed to the method.

## Connecting to a server running inside the sandbox

You can start a server inside the sandbox and connect to it using the approach above.

In this example we will start a simple HTTP server that listens on port 3000 and responds with the content of the directory where the server is started.

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox } from 'novita-sandbox/code-interpreter'

  const sandbox = await Sandbox.create()

  // Start a simple HTTP server inside the sandbox.
  const commandHandle = await sandbox.commands.run('python -m http.server 3000', { background: true })
  const host = sandbox.getHost(3000)
  const url = `https://${host}`
  console.log('Server started at:', url)

  // Fetch data from the server inside the sandbox.
  const response = await fetch(url);
  const data = await response.text();
  console.log('Response from server inside sandbox:', data);

  // Kill the server process inside the sandbox.
  await commandHandle.kill()

  // Example output:
  // Server started at: https://3000-ibbw4zmqp38s77v1vbykj-d0b9e1e2.sandbox.novita.ai
  // Response from server inside sandbox: <!DOCTYPE HTML>
  // <html lang="en">
  // <head>
  // <meta charset="utf-8">
  // <title>Directory listing for /</title>
  // </head>
  // <body>
  // <h1>Directory listing for /</h1>
  // <hr>
  // <ul>
  // <li><a href=".bash_logout">.bash_logout</a></li>
  // <li><a href=".bashrc">.bashrc</a></li>
  // <li><a href=".profile">.profile</a></li>
  // </ul>
  // <hr>
  // </body>
  // </html>

  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.code_interpreter import Sandbox

  sandbox = Sandbox.create()

  # Start a simple HTTP server inside the sandbox.
  command_handle = sandbox.commands.run("python -m http.server 3000", background=True)
  host = sandbox.get_host(3000)
  url = f"https://{host}"
  print('Server started at:', url)

  # Fetch data from the server inside the sandbox.
  response = sandbox.commands.run(f"curl {url}")
  data = response.stdout
  print("Response from server inside sandbox:", data)

  # Kill the server process inside the sandbox.
  command_handle.kill()

  # Example output:
  # Server started at: https://3000-i0iq56w6786bz91034h8l-82b888ba.sandbox.novita.ai
  # Response from server inside sandbox: <!DOCTYPE HTML>
  # <html lang="en">
  # <head>
  # <meta charset="utf-8">
  # <title>Directory listing for /</title>
  # </head>
  # <body>
  # <h1>Directory listing for /</h1>
  # <hr>
  # <ul>
  # <li><a href=".bash_logout">.bash_logout</a></li>
  # <li><a href=".bashrc">.bashrc</a></li>
  # <li><a href=".profile">.profile</a></li>
  # </ul>
  # <hr>
  # </body>
  # </html>

  sandbox.kill()
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).