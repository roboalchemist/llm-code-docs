# Source: https://beeceptor.com/docs/local-tunneling-by-exposing-service-port/

Title: Local Tunneling | Beeceptor

URL Source: https://beeceptor.com/docs/local-tunneling-by-exposing-service-port/

Published Time: Tue, 10 Mar 2026 12:20:10 GMT

Markdown Content:
[Local Tunneling](https://beeceptor.com/local-tunnel/) is a great way to bind a web service running on your localhost to a public endpoint. This is mainly useful when you want to expose the service running on your development machine to a dependent team member (like UI developers). In addition, this is quite helpful when you are developing a callback or a webhook to receive notifications from external services.

Tunneling with Beeceptor[​](https://beeceptor.com/docs/local-tunneling-by-exposing-service-port/#tunneling-with-beeceptor "Direct link to Tunneling with Beeceptor")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

![Image 1: beeceptor--port-forwarding](https://beeceptor.com/docs/assets/images/local-tunnel-connectivity-architecture-794b809cd2b129d51b80fd85ace1ed1b.png#no-border)

Beeceptor's Local Tunnel establishes a secure connection from your local server to the internet, allowing external access without complex network configuration. It uses port 443 for all communications.

Beeceptor enables this use-case by giving you a public URL on the Internet. All the requests hitting the Beeceptor endpoint will be routed to the local machine's port, and the response will be served back to the caller.

All of the requests and responses are visible on the endpoint dashboard as usual. Any request that gets matched up with a mocking rule will get a mocked response (i.e., it won't go through tunneling). The Beeceptor CLI is an easy-to-install developer tool that helps you connect your localhost port with Beeceptor's endpoint. It works on all platforms (macOS, Windows, Linux). You can install it using NPM or download it as an independent executable file.

Step 1: Enable tunneling[​](https://beeceptor.com/docs/local-tunneling-by-exposing-service-port/#step-1-enable-tunneling "Direct link to Step 1: Enable tunneling")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you are on a Free plan, this step is not required. For convenience, Beeceptor CLI manages this for you.

Open the endpoint dashboard and enable tunneling for the endpoint.

Step 2: Installation[​](https://beeceptor.com/docs/local-tunneling-by-exposing-service-port/#step-2-installation "Direct link to Step 2: Installation")
-------------------------------------------------------------------------------------------------------------------------------------------------------

The Beeceptor CLI is a developer tool to help you connect the localhost port with Beeceptor's public endpoint. It is easy to install, and works on all platforms (macOS, Windows, and Linux). The Beeceptor CLI can be installed using NPM or downloaded as an independent executable file.

### Option 1: Install via NPM (Node package manager)[​](https://beeceptor.com/docs/local-tunneling-by-exposing-service-port/#option-1-install-via-npm-node-package-manager "Direct link to Option 1: Install via NPM (Node package manager)")

You can install Beeceptor CLI using Node's package manager. It is published on NPM as `beeceptor-cli`. If you have NPM/NodeJs installed, copy and run the following command:

`npm i beeceptor-cli -g`

or

`yarn global add beeceptor-cli`

Refer to [npmjs.com/package/beeceptor-cli](https://www.npmjs.com/package/beeceptor-cli) for more details.

### Option 2: Download standalone executable[​](https://beeceptor.com/docs/local-tunneling-by-exposing-service-port/#option-2-download-standalone-executable "Direct link to Option 2: Download standalone executable")

You can download the Beeceptor CLI by clicking on the following links. Ensure that you pick the right platform.

**Download Links**

**Decompress**

The downloaded file is a `tar.gz` file. You can decompress it using the following command:

`tar -xvf <path-to-tar-file.tag.gz>`

Step 3: Run the Beeceptor CLI[​](https://beeceptor.com/docs/local-tunneling-by-exposing-service-port/#step-3-run-the-beeceptor-cli "Direct link to Step 3: Run the Beeceptor CLI")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you have installed via NPM simply type the following to get started:

`beeceptor-cli -p port-number`

![Image 2: beeceptor-local-tunnel-create-endpoint](https://beeceptor.com/docs/assets/images/beeceptor-cli-create-tunnel-7b4bea8e826a9cbd43f5153a27583ccd.gif)

_Note: You may be asked to update the CLI if it is an obsolete version._

### Run from downloaded binaries[​](https://beeceptor.com/docs/local-tunneling-by-exposing-service-port/#run-from-downloaded-binaries "Direct link to Run from downloaded binaries")

Run the CLI using following command. Here you pass the localhost port using `-p` parameter.

**Windows**: Open Power Shell or Command Prompt to run the following:

`beeceptor-cli-windows -p port-number`

**Mac**: Open Terminal app and run the following:

`./beeceptor-cli-macos -p port-number`

**Linux**: Open bash or shell and run the following:

`./beeceptor-cli-linux -p port-number`

Step 4: Pick an endpoint[​](https://beeceptor.com/docs/local-tunneling-by-exposing-service-port/#step-4-pick-an-endpoint "Direct link to Step 4: Pick an endpoint")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Create a new free endpoint[​](https://beeceptor.com/docs/local-tunneling-by-exposing-service-port/#create-a-new-free-endpoint "Direct link to Create a new free endpoint")

When you pick this, the CLI will assign you a unique endpoint that will route all requests to your localhost at specified port.

![Image 3: localhost-tunnel-free](https://beeceptor.com/docs/assets/images/beeceptor-free-tunnel-localhost-82b9c12a9091090c250a32717ca9d1d4.png)

_Note: This option follows the Free plan's limits (50 requests/day). If you need more requests, consider upgrading and authorize the upgraded endpoint._

After installing the Beeceptor CLI, you must connect it with your Beeceptor endpoint. To do so, run the following command in the terminal with `-p` option and specify a port number on `localhost`.

Next, you are required to authorize. You’ll be prompted to launch your web-browser. Once logged in, you can grant or link a Beeceptor endpoint with this client-machine's authentication request. When you see a message _"Now tunneling requests from... to this machine's port xxxx."_, you are all set to receive requests from Internet to your local machine.

Example command to run: `./beeceptor-cli-macos -p 9006`

![Image 4: authorize-cli](https://beeceptor.com/docs/assets/images/beeceptor-cli-authorize-252f5e3be9c385edf94f1a873ad4514a.png)

Step 5: Ready to receive requests[​](https://beeceptor.com/docs/local-tunneling-by-exposing-service-port/#step-5-ready-to-receive-requests "Direct link to Step 5: Ready to receive requests")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You are all set! Any request sent to your Beeceptor's endpoint will now be routed to this port on localhost. The response served by the local service, will be sent back to the caller.

CLI Parameters[​](https://beeceptor.com/docs/local-tunneling-by-exposing-service-port/#cli-parameters "Direct link to CLI Parameters")
--------------------------------------------------------------------------------------------------------------------------------------

| CLI Parameter | Description |
| --- | --- |
| `-h` | Specifies the hostname or IP address of the local server to establish a connection. The default value is 127.0.0.1. |
| `-p` | **Required**. Specifies the port number on the local server where the connection will be established. |
| `--https` | Enables the use of HTTPS for the connection to the specified host and port. By default, the connection uses HTTP. |
| `--headless` | Prints the authentication URL to the shell, rather than opening it in a web browser. |
| `-e` | Use the `-e` flag to specify the endpoint name in the non-interactive mode. |
| `-t` | Use the `-t` flag to provide the authentication token in the non-interactive mode. |

Non-Interactive Connections[​](https://beeceptor.com/docs/local-tunneling-by-exposing-service-port/#non-interactive-connections "Direct link to Non-Interactive Connections")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The Beeceptor CLI supports both _interactive_ and _non-interactive_ connection modes. While the interactive mode prompts you to select an endpoint and authenticate during runtime, the _non-interactive_ mode allows you to connect directly to a specific endpoint by supplying required parameters in the command.

This is particularly useful when you want to:

*   Run Beeceptor CLI inside scripts or CI/CD pipelines.
*   Automate local tunnel connections without manual prompts.
*   Quickly connect to a known endpoint using pre-approved credentials.

**Obtaining a Token**

You must run the Beeceptor CLI in interactive mode for the first time to generate an authentication token. After approval, the authentication token will appear in the Beeceptor UI, but it remains available to copy only for a few minutes.

1.   Run the Beeceptor CLI once in interactive mode and proceed with first time approval. Ensure that the flow is completed and CLI is connected.
2.   Go to your [Beeceptor Local Tunnels page](https://app.beeceptor.com/account/local-tunnels) and you will see already approved clients table.
3.   A newly generated token will appear in the _Token_ column. These tokens are available to copy for only a few minutes after approval.

![Image 5: copy-cli-token](https://beeceptor.com/docs/assets/images/beeceptor-cli-token-copying-57b906bb29884a237eb1748e1b4ffed2.png)

**Example Command**

Below is an example command of a non-interactive connection. Use the `-e` flag to specify the endpoint name and the `-t` flag to provide the authentication token that you copied.

`beeceptor-cli -p 3000 -h localhost -e endpoint-name -t your-token-value`

Key considerations[​](https://beeceptor.com/docs/local-tunneling-by-exposing-service-port/#key-considerations "Direct link to Key considerations")
--------------------------------------------------------------------------------------------------------------------------------------------------

1.   **Timeout Handling:** The service running on the local port must respond within 60 seconds. Failure to respond within this timeframe results in a timeout, leading to an error response.

2.   **Mocking Rule Priority:** Mocking rules take precedence over local tunneling. If an incoming request matches a predefined mocking rule, it is processed accordingly, and does not proceed to the local service. This feature is useful for selectively mocking specific requests while handling others locally.

3.   **Connection Errors:** If the local service is inaccessible, you may encounter errors indicating a failure to connect, such as `Failed to connect to host (refused)`.

4.   **Concurrency and Rate Limiting:** The system permits a maximum of 8 simultaneous requests for tunneling. Exceeding this cap triggers rate limiting with an error response as `429 - Too many requests`.

5.   **Protocol Specification:** By default, the Beeceptor Command Line Interface (CLI) establishes connections using the HTTP protocol. To force HTTPS, include the `--https` option when executing the CLI command.

6.   **Headless Mode:** If you're using Beeceptor CLI on a server that doesn't have a user interface or web browser, use the `--headless` option. This approach prints the authentication URL in the shell. You can copy this URL and open it on a device with web access to complete the authentication process.

7.   **Reconnect:** If the network disconnects, Beeceptor CLI will automatically retry the connection a limited number of times. If the connection is restored, the command continues running. If all retry attempts fail, the process will terminate.

macOS Warning[​](https://beeceptor.com/docs/local-tunneling-by-exposing-service-port/#macos-warning "Direct link to macOS Warning")
-----------------------------------------------------------------------------------------------------------------------------------

If you're using the Beeceptor CLI on macOS, you might run into macOS security blocks that prevent the app from running. macOS uses a security feature called Gatekeeper to block applications that haven't been notarized by Apple. When you first try to launch the Beeceptor CLI, you might see a message like this:

![Image 6: macos-warning](https://beeceptor.com/docs/assets/images/beeceptor-cli-macos-click-done-89ee8440d1f5e253dc8e73e4cf2c6526.png)

macOS blocking Beeceptor CLI execution

Click Done on this message to dismiss it for now.

We'll fix it in the next steps.:

1.   Open the Apple menu and select System Settings.
2.   Click on _Privacy & Security_ in the sidebar.
3.   Scroll to the Security section on the right.
4.   If you see "beeceptor-cli-macos" was blocked, click **Allow Anyway** to allow it. ![Image 7: macos-warning](https://beeceptor.com/docs/assets/images/beeceptor-cli-macos-warning-e925fe1204e611ef78ee3cbff3014cbf.png)

Allow Beeceptor CLI from the Privacy & Security settings.

5.   Rerun the CLI

This is a one-time setup. You won't have to repeat these steps unless the app is updated or moved.

Note:

*   macOS ARM64: This refers to Macs with Apple Silicon chips, like the M1, M2, M3, and M4, which are based on the ARM architecture.
*   macOS x64 (or x86_64): This refers to Macs with Intel processors, which use the x64 architecture.

Security Warning for Tunnel URLs[​](https://beeceptor.com/docs/local-tunneling-by-exposing-service-port/#security-warning-for-tunnel-urls "Direct link to Security Warning for Tunnel URLs")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When a Beeceptor tunnel URL is opened in a web browser, Beeceptor shows a temporary security page before redirecting to the tunneled content. This interstitial warning helps prevent phishing or misuse of shared tunnel links and creates awareness for users that the page is being served through a Beeceptor tunnel.

![Image 8: beeceptor-tunnel-browser-warning](https://beeceptor.com/docs/assets/images/tunnel-interstitial-page-5e4e6c06e61fd5d8afd628c6a012f258.png)

This warning appears only for browser-based requests, ensuring developers can continue using tools like cURL, Postman, or command-line scripts without interruption. This safeguard cannot be disabled and is designed to keep tunnel usage safe while allowing seamless API testing and sharing during development.
