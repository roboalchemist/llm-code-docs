# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/troubleshooting-ael-cp/message-size-exceeded.md

# Message size exceeded

If you are using the Spark engine to run an AEL transformation and an error is generated indicating a decoded message was too big for the output buffer, you need to increase the maximum size (2 MB by default) of the message buffers for your AEL environment.

Perform the following steps to increase the message buffer limit:

1. [Stop the AEL daemon](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/configure-the-ael-daemon-for-yarn-mode).
2. Navigate to the `data-integration/adaptive-execution/config` directory and open the `application.properties` file using a text editor.
3. Enter the following incoming WebSocket message buffer properties, setting the same value for each property:

<table data-header-hidden><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>Property</td><td>Value</td></tr><tr><td><strong>daemon.websocket.maxMessageBufferSize</strong></td><td><p>The maximum size (in bytes) for the message buffer on the AEL daemon. For example, to allocate a 4 MB limit, set the memory value as shown here:```<strong>daemon.websocket.maxMessageBufferSize</strong>=4000000</p><pre><code>
&#x3C;/td>&#x3C;/tr>&#x3C;tr>&#x3C;td>

**driver.websocket.maxMessageBufferSize**

\</td>\<td>

The maximum size (in bytes) for the message buffer on the AEL Spark driver. For example, to allocate a 4 MB limit, set the memory value as shown here:\`\`\`
**driver.websocket.maxMessageBufferSize**=4000000 </code></pre></td></tr></tbody></table>

4\. Save and close the file.

5. [Restart the AEL daemon](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/configure-the-ael-daemon-for-yarn-mode).

When the AEL daemon submits the AEL Spark driver application, it passes the driver’s maximum message buffer size value as part of the submit; then, when the driver application is started, it receives the maximum buffer size value sent by the daemon.
