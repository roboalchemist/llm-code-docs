# Source: https://docs.embedchain.ai/contribution/docs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.embedchain.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 📝 Documentation

> Contribute to Embedchain docs

<Info>
  **Prerequisite** You should have installed Node.js (version 18.10.0 or
  higher).
</Info>

Step 1. Install Mintlify on your OS:

<CodeGroup>
  ```bash npm theme={null}
  npm i -g mintlify
  ```

  ```bash yarn theme={null}
  yarn global add mintlify
  ```
</CodeGroup>

Step 2. Go to the `docs/` directory (where you can find `mint.json`) and run the following command:

```bash  theme={null}
mintlify dev
```

The documentation website is now available at `http://localhost:3000`.

### Custom Ports

Mintlify uses port 3000 by default. You can use the `--port` flag to customize the port Mintlify runs on. For example, use this command to run in port 3333:

```bash  theme={null}
mintlify dev --port 3333
```

You will see an error like this if you try to run Mintlify in a port that's already taken:

```md  theme={null}
Error: listen EADDRINUSE: address already in use :::3000
```

## Mintlify Versions

Each CLI is linked to a specific version of Mintlify. Please update the CLI if your local website looks different than production.

<CodeGroup>
  ```bash npm theme={null}
  npm i -g mintlify@latest
  ```

  ```bash yarn theme={null}
  yarn global upgrade mintlify
  ```
</CodeGroup>
