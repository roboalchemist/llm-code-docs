<!-- Source: https://namespace.so/docs/devbox/sessions -->

# Sessions

Sessions provide persistent terminal environments within your devbox that survive browser tab closures and network disconnections.

## What are Sessions?

A **Session** is a named, persistent terminal environment that preserves your terminal state. Sessions allow you to:

- **Detach and reattach**: Disconnect and reconnect later — from the dashboard or the CLI — to find your terminal exactly as you left it
- **Run persistent processes**: Keep long-running processes (servers, watchers, builds) running while disconnected
- **Access anywhere**: Connect to sessions from the web dashboard or your local terminal with the Devbox CLI

## Sessions vs. Regular Terminals

| Feature | Session | Regular Terminal (SSH/Tab) |
| --- | --- | --- |
| Persists after disconnect | Yes | No |
| State preserved on browser close | Yes | No |
| Named and manageable | Yes | No |
| Visible in dashboard sidebar | Yes | No |
| Accessible from CLI | Yes | N/A |

## Creating Sessions

### From the Dashboard

1. Navigate to your devbox in the [Namespace dashboard](https://cloud.namespace.so/workspace/devboxes)
2. In the left sidebar, click **New session** under the Sessions section
3. A new session is created with a randomly generated name and you're automatically connected

### From a Spec File

Sessions can also be defined in a [spec file](/docs/devbox/managing#creating-from-a-spec-file) so they are created automatically when the Devbox starts.

## Managing Sessions

### Viewing Sessions

All active sessions are displayed in the left sidebar of the devbox dashboard.

### Connecting to a Session

**From the Dashboard:**

Click on any session in the sidebar to connect to it. Connecting to a session takes exclusive control — if another browser tab was connected to that session, it will be detached.

**From the CLI:**

Connect to a named session from your local terminal:

```
$

```
devbox session connect my-devbox --session server
```
```

If you omit the Devbox name, an interactive picker is shown:

```
$

```
devbox session connect --session server
```
```

The CLI connection takes exclusive control of the session, just like the dashboard. If the Devbox is paused, it is automatically resumed before connecting.

### Deleting Sessions

Hover over a session in the sidebar and click the close button to delete it. This terminates any running processes in that session.

## Use Cases

### Development Servers

Run your dev server in a session. The server keeps running when you close your browser, and all logs are available when you reconnect.

### Multiple Workstreams

Create separate sessions for different tasks: a dev server, test runner, and general shell. Switch between them instantly without losing context.

### Long-Running Tasks

Start a build or test suite in a session, then disconnect and check the results later.

## Next Steps

**[Remote Development →](/docs/devbox/remote-development)**
Connect to your devbox via SSH, VS Code, Cursor, Zed, or JetBrains.

**[Managing Devboxes →](/docs/devbox/managing)**
Lifecycle operations, machine sizes, workspace defaults, and monitoring.

**[Custom Images →](/docs/devbox/images)**
Build custom base images with your tools and runtimes pre-installed.

Last updated March 26, 2026
