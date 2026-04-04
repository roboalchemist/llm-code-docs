# Source: https://docs.turso.tech/cli/headless-mode.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Headless Mode

The Turso CLI will automatically attempt to open a browser, or wait for further instructions when interacting with various commands.

You can opt out of this behaviour by passing the `--headless` flag with operations:

```bash  theme={null}
turso auth login --headless
```

<Note>
  If you're using Windows with WSL or a remote CI/CD environment, pass the `--headless` flag.
</Note>
