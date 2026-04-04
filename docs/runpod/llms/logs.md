# Source: https://docs.runpod.io/serverless/development/logs.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.runpod.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Monitor logs

> View and access logs for Serverless endpoints and workers.

<Frame alt="Serverless logs">
  <img src="https://mintcdn.com/runpod-b18f5ded/_BeZqveqZvW4ISvJ/images/serverless-logs.png?fit=max&auto=format&n=_BeZqveqZvW4ISvJ&q=85&s=aa2b08ee974dd939eb3354caa8710c51" data-og-width="1624" width="1624" data-og-height="1244" height="1244" data-path="images/serverless-logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/runpod-b18f5ded/_BeZqveqZvW4ISvJ/images/serverless-logs.png?w=280&fit=max&auto=format&n=_BeZqveqZvW4ISvJ&q=85&s=58b779b937b83f0575789d2a5a8f9a4f 280w, https://mintcdn.com/runpod-b18f5ded/_BeZqveqZvW4ISvJ/images/serverless-logs.png?w=560&fit=max&auto=format&n=_BeZqveqZvW4ISvJ&q=85&s=3b11162df0c0017741a09bcc2c7c13ae 560w, https://mintcdn.com/runpod-b18f5ded/_BeZqveqZvW4ISvJ/images/serverless-logs.png?w=840&fit=max&auto=format&n=_BeZqveqZvW4ISvJ&q=85&s=dba58423fbbaf2840ecae5d2342eb611 840w, https://mintcdn.com/runpod-b18f5ded/_BeZqveqZvW4ISvJ/images/serverless-logs.png?w=1100&fit=max&auto=format&n=_BeZqveqZvW4ISvJ&q=85&s=9c2572f20a2e8dbe41a08d3cce929e67 1100w, https://mintcdn.com/runpod-b18f5ded/_BeZqveqZvW4ISvJ/images/serverless-logs.png?w=1650&fit=max&auto=format&n=_BeZqveqZvW4ISvJ&q=85&s=2c8b84e31e7247fdff2295d770e369b3 1650w, https://mintcdn.com/runpod-b18f5ded/_BeZqveqZvW4ISvJ/images/serverless-logs.png?w=2500&fit=max&auto=format&n=_BeZqveqZvW4ISvJ&q=85&s=16ad29b9bc59f93ed5d0992621d685cc 2500w" />
</Frame>

Runpod provides comprehensive logging capabilities for Serverless endpoints and workers. You can view real-time and historical logs through the Runpod console to help you monitor, debug, and troubleshoot your applications.

To learn how to write structured logs from your handler functions, see [Write logs](/serverless/development/write-logs).

## Endpoint logs

<Note>
  Endpoint logs are retained for 90 days, after which they are automatically removed from the system. If you need to retain logs indefinitely, you can [write them to a network volume](#persistent-log-storage) or an external service.
</Note>

Endpoint logs are automatically collected from your worker instances and streamed to Runpod's centralized logging system. These logs include:

* **Standard output (stdout)** from your handler functions.
* **Standard error (stderr)** from your applications.
* **System messages** related to worker lifecycle events.
* **Framework logs** from the Runpod SDK. To learn more about the Runpod logging library, see the [Runpod SDK documentation](/tutorials/sdks/python/101/error).

Logs are streamed in near real-time with only a few seconds of lag.

<Warning>
  If your worker generates excessive output, logs may be throttled and dropped to prevent system overload. See [Log throttling](#log-throttling) for more information.
</Warning>

To view endpoint logs:

1. Navigate to your Serverless endpoint in the [Runpod console](https://console.runpod.io/serverless).
2. Click on the **Logs** tab.
3. View real-time and historical logs.
4. Use the search and filtering capabilities to find specific log entries.
5. Download logs as text files for offline analysis.

## Worker logs

Worker logs are temporary logs that exist only on the specific server where the worker is running. These logs are not throttled, but are not persistent, and are removed when a worker terminates.

To view worker logs:

1. Navigate to your Serverless endpoint in the [Runpod console](https://console.runpod.io/serverless).
2. Click on the **Workers** tab.
3. Click on a worker to view its logs and request history.
4. Use the search and filtering capabilities to find specific log entries.
5. Download logs as text files for offline analysis.

## Troubleshooting

### Missing logs

If logs are not appearing in the Logs tab:

1. **Check log throttling**: Excessive logging may trigger throttling.
2. **Verify output streams**: Ensure you're writing to stdout/stderr.
3. **Check worker status**: Logs only appear for successfully initialized workers.
4. **Review retention period**: Logs older than 90 days are automatically removed.

### Log throttling

To avoid log throttling, follow these best practices:

1. **Reduce log verbosity** in production environments.
2. **Use structured logging** to make logs more efficient.
3. **Implement log sampling** for high-frequency events.
4. **Store detailed logs** in network volumes instead of console output.
