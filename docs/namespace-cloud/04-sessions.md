# Sessions - Persistent Terminal Environments

Sessions are named, persistent terminal environments within devboxes that maintain their state even after browser disconnections.

## Core Functionality

Sessions allow users to:

- Detach and reattach to find the terminal exactly as left
- Run continuous processes
- Access environments from either the web dashboard or CLI

## Key Distinctions

Sessions differ from regular terminals in that they:

- Preserve state after disconnect
- Survive browser closures
- Are named and manageable
- Appear in the dashboard sidebar with CLI accessibility

## Creation Methods

### Via Dashboard

Click "New session" in the sidebar.

### Via Spec File

Define sessions in spec files for automatic creation when devboxes start:

```yaml
sessions:
  - name: server
    command: npm start
  - name: test
    command: npm test
```

## Access and Management

### Dashboard

Sessions display in the dashboard sidebar and can be connected to by clicking them.

### CLI

Connect via commands like:

```bash
devbox session connect my-devbox --session server
```

### Deletion

A close button appears when hovering over sessions in the sidebar.

## Primary Use Cases

The documentation highlights three main applications:

1. **Persistent servers**: Running development servers that persist when browsers close

2. **Multiple workstreams**: Managing multiple workstreams through separate sessions

3. **Long-running tasks**: Executing long-running tasks that can be checked later

## Related Documentation

- Remote development
- Custom images
- Devbox lifecycle management
