# Source: https://mastra.ai/reference/deployer/netlify

# NetlifyDeployer

The `NetlifyDeployer` class handles packaging, configuration, and deployment by adapting Mastra's output to create an optimized version of your server. It extends the base [`Deployer`](https://mastra.ai/reference/deployer) class with Netlify specific functionality. It enables you to run Mastra within Netlify functions.

## Installation

In order to use `NetlifyDeployer`, you need to install the `@mastra/deployer-netlify` package:

**npm**:

```bash
npm install @mastra/deployer-netlify@latest
```

**pnpm**:

```bash
pnpm add @mastra/deployer-netlify@latest
```

**Yarn**:

```bash
yarn add @mastra/deployer-netlify@latest
```

**Bun**:

```bash
bun add @mastra/deployer-netlify@latest
```

## Usage example

Import `NetlifyDeployer` and set it as the deployer in your Mastra configuration:

```typescript
import { Mastra } from '@mastra/core'
import { NetlifyDeployer } from '@mastra/deployer-netlify'

export const mastra = new Mastra({
  deployer: new NetlifyDeployer(),
})
```

## Output

After running `mastra build`, the deployer generates a `.netlify` folder. The build output includes all agents, tools, and workflows of your project, alongside a special `config.json` file. The `config.json` file configures the behavior of Netlify functions.

```bash
your-project/
└── .netlify/
    └── v1/
        ├── config.json
        └── functions/
            └── api/
                ├── index.mjs
                ├── package.json
                └── node_modules/
```

The `config.json` file contains:

```json
{
  "functions": {
    "directory": ".netlify/v1/functions",
    "node_bundler": "none",
    "included_files": [".netlify/v1/functions/**"]
  },
  "redirects": [
    {
      "force": true,
      "from": "/*",
      "to": "/.netlify/functions/api/:splat",
      "status": 200
    }
  ]
}
```