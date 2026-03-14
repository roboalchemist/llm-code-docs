# Source: https://docs.anyscale.com/platform/workspaces/workspaces-ports.md

# Workspace ports

[View Markdown](/platform/workspaces/workspaces-ports.md)

# Workspace ports

Workspaces automatically expose ports opened inside a workspace, making them accessible from your browser. This enables a secure and seamless interaction with various services and applications running within your workspace.

## How it works[​](#how-it-works "Direct link to How it works")

1. When you start a service or application that opens a port within your workspace, Anyscale automatically detects it.
2. The detected port is then securely forwarded and made available through your browser.
3. You can access these ports directly from the Anyscale console, without needing to configure any additional networking or port forwarding.

## Benefits[​](#benefits "Direct link to Benefits")

* **Automatic detection**: No manual configuration required for port forwarding.
* **Secure access**: Anyscale encrypts and authenticates all connections through your organization.
* **Seamless integration**: Easily interact with services such as TensorBoard or custom web applications running in your workspace.

## Use workspace ports[​](#use-ports "Direct link to Use workspace ports")

To use workspace ports:

1. Start your service or application within the workspace as you normally would.
2. The port automatically appears in the Anyscale console under the **Open ports** section of your workspace.
3. Click on the port link to open the service in a new browser tab.

## Running services like TensorBoard[​](#tensorboard "Direct link to Running services like TensorBoard")

To run TensorBoard:

1. Install TensorBoard in your workspace if it's not already available:
   <!-- -->
   ```
   pip install tensorboard
   ```
2. Start TensorBoard, specifying your log directory:
   <!-- -->
   ```
   tensorboard --logdir=/path/to/logs --port=6006
   ```
3. The TensorBoard interface automatically becomes available in the Ports section of your workspace, typically on port 6006.
4. Click on the port link to open TensorBoard in a new browser tab.

This seamless integration allows you to visualize your machine learning experiments without leaving the Anyscale environment.

note

Some ports in your workspace may already be open when you start it. Anyscale uses these ports internally for various system functions and services. While these ports are visible, they're reserved for internal use and shouldn't be modified or closed.

# Accessing ports using the CLI

In addition to accessing ports through the Anyscale console, you can also use the Anyscale CLI to create SSH tunnels for port forwarding. This method allows you to access workspace ports directly from your local machine. See [`anyscale workspace_v2 ssh`](/reference/workspaces.md#anyscale-workspace_v2-ssh).

To access a port using the CLI:

1. Open a terminal on your local machine.

2. Use the following command structure:

   ```
   anyscale workspace_v2 ssh -n <workspace-name> -- -L <local-port>:localhost:<workspace-port>
   ```

   Replace `<workspace-name>` with your workspace name, `<local-port>` with the port you want to use on your local machine, and `<workspace-port>` with the port number in your workspace.

3. For example, to forward port 9000 from your workspace to port 9000 on your local machine:

   ```
   anyscale workspace_v2 ssh -n my-workspace -- -L 9000:localhost:9000
   ```

4. Once you establish the SSH tunnel, you can access the service running on that port by opening a browser and navigating to `http://localhost:9000` or whatever port you specified.

This method is particularly useful for accessing services that require a local connection or for using local development tools with your workspace.

note

Remember to keep the terminal window open while you're using the forwarded port. Closing the terminal terminates the SSH tunnel and the port forwarding.
