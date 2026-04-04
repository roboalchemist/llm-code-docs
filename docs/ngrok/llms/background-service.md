# Source: https://ngrok.com/docs/guides/site-to-site-connectivity/background-service.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Install ngrok as a Background Service

> Install ngrok as a service so it stays running.

You can install ngrok in your customer's network as a native background system service.
This ensures the ngrok agent starts on boot and restarts if it crashes for any reason.

Installing ngrok as a service helps you recover connectivity in the case of unexpected software or hardware failures.
When you do so, ngrok starts all endpoints defined in the configuration file.

```bash  theme={null}
ngrok service install --config /etc/ngrok.yml
ngrok service start
```

<Note>
  In most cases, installing ngrok as a service requires administrator privileges.
</Note>

## What's next

* [Eliminate single points of failure with redundant agents](/guides/site-to-site-connectivity/redundant-agents) to achieve high availability.


Built with [Mintlify](https://mintlify.com).