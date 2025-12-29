# Source: https://docs.pipecat.ai/deployment/pipecat-cloud/fundamentals/logging.md

# Logging and Observability

> Obtaining logs and metrics from your agents and sessions

<Warning>
  This section of the documentation is currently work in progress. Please check
  back soon for updates.
</Warning>

## Agent logs

Agent logs are available via both the CLI and Dashboard. You can view logs for a specific agent by running the following command:

```bash  theme={null}
pipecat cloud agent logs my-agent
```

This command accept various filters to help you narrow down the logs you are looking for. For example, you can filter logs by severity level:

```bash  theme={null}
pipecat cloud agent logs my-agent -l ERROR
```

### Session logging

We recommend using the `loguru` library for logging within your agent. This will ensure any logging within your agent associated to the session it is running in.

```python  theme={null}
from loguru import logger

async def bot():
	logger.info("Hello, world!") # will be associated with the session id
```

If you are handling logging manually, you can obtain the active session ID from the `PipecatRunnerArguments` object (or subclass alternative) passed to your `bot()` method:

```python  theme={null}
from pipecat.runner.types import PipecatRunnerArguments

async def bot(args: PipecatRunnerArguments):
	session_id = args.session_id
```

<Note>
  See [the Session Arguments reference](../sdk-reference/session-arguments) for
  more additional SessionArgument types.
</Note>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.pipecat.ai/llms.txt