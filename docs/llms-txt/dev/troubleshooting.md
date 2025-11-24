# Source: https://dev.writer.com/agent-builder/troubleshooting.md

# Troubleshoot common issues

This page provides troubleshooting suggestions for debugging and observing your agents as you build them.

* [Track an agent's progress through a blueprint](#view-progress-through-a-blueprint)
* [View error and info logs](#view-error-and-info-logs)
* [Add additional log messages](#add-additional-logs)
* [View traces from a block's execution](#view-traces)
* [Inspect an agent's state](#inspect-agent-state)
* [Observe agent usage and performance](#observe-agent-usage-and-performance)

## View progress through a blueprint

Some blocks such as PDF parsing and text generation can take a while to run. As an agent runs, you can view its progress through the blueprint by navigating to the **Blueprint** tab.

The color of a blueprint block's border describes the status of its execution.

* **Green**: The block completed successfully
* **Animated blue**: The block is currently running
* **Red**: The block failed
* **No border**: The block hasn't run yet

The following image shows a blueprint with a PDF parsing block that's currently running. The previous blocks have completed successfully and the following blocks haven't run yet.

<img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/blueprint-progress.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=f4213ab4084c828a555723aa85a84a49" alt="Blueprint tab" data-og-width="3456" width="3456" data-og-height="1796" height="1796" data-path="images/agent-builder/parse-pdf-tutorial/blueprint-progress.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/blueprint-progress.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=0ba61d4c42c8d61b2a8d658765ed3c5f 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/blueprint-progress.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=b2517593f52e6caa8c88ac9d02e96d05 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/blueprint-progress.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=db5f2d3d44a7e87d2bc29245deb0bee2 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/blueprint-progress.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=bfd12e807fa0f820291a108bca526a43 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/blueprint-progress.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=e77294494ac8731601c76d0dfd572524 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/blueprint-progress.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=3c9dbd995b7ab600114ffff490b78fdd 2500w" />

You can also see the progress of the agent in the **Log** status bar. Learn more below.

## View error and info logs

If there are any errors or messages as your agent runs, you'll see an indication in the **Log** bar in the bottom right corner of the page.

You can click the **Log** bar to expand it and see more details.

<img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/log-bar.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=c7d1e33a828f416ed50b75001d1b126b" alt="Log bar" data-og-width="470" width="470" data-og-height="138" height="138" data-path="images/agent-builder/log-bar.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/log-bar.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=3fd622c89a838fb86adfe4337a5a64c5 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/log-bar.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=e4bcf530786f0f7b37f4185d1ff6a11f 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/log-bar.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=4a281b2872c90f6d796702abf9e6f6f2 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/log-bar.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=e443f71b0bcdb0e66702774f0a18e94f 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/log-bar.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=77207d1acd2eb82a7e0e06e7a68c82f6 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/log-bar.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=aabe9739cee4cc7291c4640fd22bc218 2500w" />

### Add additional logs with Log Message blocks

You can add additional custom [**Log message** blocks](/blueprints/logmessage) to the agent for debugging purposes. Log messages are helpful to understand the flow of the agent and the value of state and other variables at a given point in the execution.

To add a log message, add a **Log message** block to the canvas. In the block's configuration panel, update the following fields:

* **Type**: `info` or `error`
* **Message**: The message to log

Below is an example of a log message block during a file parsing process. It logs the file ID before beginning the parsing process, to help you debug if the file isn't found or isn't parsed correctly.

<img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/log-message-block.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=50257a987c9ee9f644934ad7d23154b9" alt="Log message block" data-og-width="3456" width="3456" data-og-height="1812" height="1812" data-path="images/agent-builder/parse-pdf-tutorial/log-message-block.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/log-message-block.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=e7bbe87f37b31d885256d93ec66d2ccd 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/log-message-block.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=bdfad5ebe828513e71e0b54a29ac6658 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/log-message-block.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=68c7cfe2072af78073429cd7da20d7c1 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/log-message-block.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=42f65c0f993982ad6500db79ad1f7d57 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/log-message-block.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=e5292ce9dd9672e3f4a20fee819ce747 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/log-message-block.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=7707883e188b69fc1a4b491758f48726 2500w" />

When the block runs, you'll see the log message in the **Logs** bar at the bottom of the page.

<img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/log-example.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=d30358a416bcd1cd16f52048927c2b31" alt="Log message in logs" data-og-width="1206" width="1206" data-og-height="214" height="214" data-path="images/agent-builder/parse-pdf-tutorial/log-example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/log-example.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=3c86a7252c068a49086800341cb31538 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/log-example.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=f8815c14b327d2cf36f07cc7c93a24a2 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/log-example.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=554878fdc9f95fe8eabbc101fd2d2d51 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/log-example.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=1221f0fead163a3e76726815ae7adf67 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/log-example.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=3c329fec3443ff119337573f2832c853 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/log-example.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=f3e67d125d5cb28946051275e47221f6 2500w" />

### Add additional logs with Python code

You can use python `print` statements and the globally available [`logger` object](https://docs.python.org/3/library/logging.html) to add additional logs to the agent.

```python  theme={null}
print("This is a log message that shows in logs as 'Captured stdout'")
logger.info("This is an info message that shows in logs under 'Captured logs'")
logger.warning("This is a warning message that shows in logs under 'Captured logs'")
logger.error("This is an error message that shows in logs under 'Captured logs'")
```

The following image shows an example of a Python block that logs messages via print statements and the `logger` object.

<img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/python-block-with-logs.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=dc7322c27b3cafabe6f2d546e7e1322d" alt="Python block with logs" data-og-width="2126" width="2126" data-og-height="750" height="750" data-path="images/agent-builder/python-block-with-logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/python-block-with-logs.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=84d9e63e2e2d9df16a1b8b48dad21f79 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/python-block-with-logs.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=f3fd8176654f9c3d1968bcfd15a4e31f 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/python-block-with-logs.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=bf5bb01a016490130f57d0cebe5e7ce4 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/python-block-with-logs.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=3b10f3062d4d060da84e7446733cd60c 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/python-block-with-logs.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=2945ea00ee3b3e525d53bccd5bce1448 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/python-block-with-logs.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=20b11b40e370862f5b8772570854a232 2500w" />

When the block runs, the log messages appear in the **Logs** bar at the bottom of the page.

<img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/python-messages-in-logs.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=14589da590433e2a7fa892af2ebed900" alt="Log messages in logs" data-og-width="3450" width="3450" data-og-height="840" height="840" data-path="images/agent-builder/python-messages-in-logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/python-messages-in-logs.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=4a9dfad07f83ae080810d3d3e7cf63cc 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/python-messages-in-logs.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=87eb3fed5ef3149327c2f308388a26e3 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/python-messages-in-logs.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=07f12519d5c3f6a7159e481584a94451 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/python-messages-in-logs.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=7920a43ea7002a760198d45f533589ca 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/python-messages-in-logs.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=3fb255f5c4257f47b597a2c70daa206f 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/python-messages-in-logs.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=52b199dc819f903175ab38482c97fdb0 2500w" />

## View traces

The log bar shows information about the agent's execution as it runs and after blocks complete. It includes the following:

* The block name
* The status of the block: success, error, or in progress
* A link to view a trace at that point in the execution
* How long the block took to run

<img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/log-bar-in-progress.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=c92edcc12ef2a0dac28721b2a37fb51f" alt="Log bar with traces" data-og-width="3456" width="3456" data-og-height="784" height="784" data-path="images/agent-builder/log-bar-in-progress.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/log-bar-in-progress.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=54323b855ccd0466edffff32121dac4d 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/log-bar-in-progress.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=540c9530241a0b541b452f136203be32 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/log-bar-in-progress.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=143d4f66801ccb9be6632a894fe19397 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/log-bar-in-progress.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=d55a5ed194baec7874a1daae61acf4a0 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/log-bar-in-progress.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=798111cab8d2d538cca1216c13d7bf20 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/log-bar-in-progress.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=772fa74f6f353f017e85eb079629f89d 2500w" />

The trace link opens a new tab with a detailed view of the agent's execution at that point in time. It contains:

* The value resulting from the block's execution, which is then added to the execution environment of the following block
* The return value, if the block has one
* The full execution environment at that point in time
* The call stack

Below is an example of a trace after a **File upload** block has completed.

<img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/trace.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=ba18ca959d92dac335e3922125de09ed" alt="Trace of a file upload block" data-og-width="2684" width="2684" data-og-height="1420" height="1420" data-path="images/agent-builder/trace.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/trace.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=2ea62a84ca2321656ae3d00b3f774ba1 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/trace.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=fa340378a867c7568f42e89904d8bb7a 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/trace.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=eef15f18881445e10c881b78cd801db2 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/trace.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=12fbae381210f5eff0b8be8243a1dc15 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/trace.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=b0172478a0cb1c54df59856672e6e6e9 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/trace.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=8c1b71194d9f85fcc6041d2c0a397f6b 2500w" />

## Inspect agent state

You can use the **State explorer** to view an agent's state variables and their values. This is helpful when you're debugging an agent or need to check the state at a given point in the execution.

To access the state explorer, click the **State explorer** icon in the top right corner of the page.

<img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/state-explorer-icon.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=dc9b3e4865094cbb8ab1c1b016b1393d" alt="State explorer" data-og-width="830" width="830" data-og-height="183" height="183" data-path="images/agent-builder/state-explorer-icon.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/state-explorer-icon.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=c879c37cc482564a6d147017903e4783 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/state-explorer-icon.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=3f059d1a8f0aef068d333aab62ac3eee 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/state-explorer-icon.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=9fc574243187e6eddf1fbd838e21c0d8 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/state-explorer-icon.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=b6244e617a09a9b798cedf1d021f946a 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/state-explorer-icon.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=3a2844ff0e041c4880ddb3f7306038b4 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/state-explorer-icon.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=f31a2f62a7a3b151be20e9c1901f1f42 2500w" />

## Observe agent usage and performance

You can view usage and performance metrics for your agent in the **Observability** tab. To get to this view, select the agent from the [AI Studio homepage](https://app.writer.com/ai-studio) and navigate to the **Observability** tab.

Here, you can view:

* Performance: Requests, errors, latency, and throughput
* Usage: Total requests, tokens, and cost, along with a geographic breakdown of requests
* Logs: Logs from individual requests

<feedback />
