# Source: https://docs.fluentd.org/deployment/rpc.md

# Source: https://docs.fluentd.org/0.12/deployment/rpc.md

# RPC

This article explains how `Fluentd` handles HTTP RPC.

## Overview

HTTP RPC is one way of managing fluentd instance. Several provided RPCs are replacement of [signals](https://docs.fluentd.org/0.12/deployment/signals). The response body is JSON format.

On signal unsupported environment, e.g. Windows, you can use RPC instead of signals.

## Configuration

RPC is off by default. If you want to enable RPC, set `rpc_endpoint` in `<system>` section.

```
<system>
  rpc_endpoint 127.0.0.1:24444
</system>
```

After that, you can access to RPC like below.

```
$ curl http://127.0.0.1:24444/api/plugins.flushBuffers
{"ok":true}
```

## RPCs

### /api/processes.interruptWorkers

Replacement of signal's [SIGINT](https://docs.fluentd.org/0.12/signals#sigint-or-sigterm). Stop the daemon.

### /api/processes.killWorkers

Replacement of signal's [SIGTERM](https://docs.fluentd.org/0.12/signals#sigint-or-sigterm). Stop the daemon.

### /api/plugins.flushBuffers

Replacement of signal's [SIGUSR1](https://docs.fluentd.org/0.12/signals#sigusr1). Flushes buffered messages.

### /api/config.reload

Replacement of signal's [SIGHUP](https://docs.fluentd.org/0.12/signals#sighup). reload configuration.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.
