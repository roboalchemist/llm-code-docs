# Source: https://docs.pipecat.ai/cli/tail.md

# tail

> A terminal dashboard for monitoring Pipecat sessions in real-time

**Tail** is a terminal dashboard for monitoring your Pipecat sessions in real-time with logs, conversations, metrics, and audio levels all in one place.

With Tail you can:

* 📜 Follow system logs in real time
* 💬 Track conversations as they happen
* 🔊 Monitor user and agent audio levels
* 📈 Keep an eye on service metrics and usage
* 🖥️ Run locally as a pipeline runner or connect to a remote session

**Usage:**

```shell  theme={null}
pipecat tail [OPTIONS]
```

**Options:**

<ParamField path="--url / -u" type="string">
  WebSocket URL to connect to. Defaults to `ws://localhost:9292`.
</ParamField>

## How to Use Tail

* Add `pipecat-ai-cli` to your project's dependencies.

* Update your Pipecat code to include the `TailObserver`:

  ```python  theme={null}
  from pipecat_cli.tail import TailObserver

  task = PipelineTask(
      pipeline,
      observers=[TailObserver()]
  )
  ```

* Start the Tail app separately:

  ```bash  theme={null}
  # Connect to local session (default)
  pipecat tail

  # Connect to remote session
  pipecat tail --url wss://my-bot.example.com
  ```


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.pipecat.ai/llms.txt