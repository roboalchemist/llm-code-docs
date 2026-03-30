# Source: https://docs.rootly.com/integrations/pulumi.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Pulumi

> Manage Rootly resources using infrastructure as code with the Pulumi provider.

Our Pulumi provider is available at:

[https://www.pulumi.com/registry/packages/rootly/installation-configuration/](https://www.pulumi.com/registry/packages/rootly/installation-configuration/ "https://www.pulumi.com/registry/packages/rootly/installation-configuration/")﻿

## Installing

This package is available for several languages/platforms:

### Node.js (JavaScript/TypeScript)

[](https://www.npmjs.com/package/@rootly/pulumi "https://www.npmjs.com/package/@rootly/pulumi")[https://www.npmjs.com/package/@rootly/pulumi](https://www.npmjs.com/package/@rootly/pulumi "https://www.npmjs.com/package/@rootly/pulumi")﻿﻿

To use from JavaScript or TypeScript in Node.js, install using either npm:

```js  theme={null}
npm install @rootly/pulumi  
```

or yarn:

```js  theme={null}
yarn add @rootly/pulumi  
```

### Python, Go, & .NET

*TBA*

## Creating resources

```js  theme={null}
const rootly = require("@rootly/pulumi")

new rootly.Severity("sev0", {
  name: "SEV0",
  color: "#FF0000"
})

new rootly.Service("elasticsearch_prod", {
  name: "elasticsearch-prod",
  color: "#800080"
})

new rootly.Functionality("add_items_to_card", {
  name: "Add items to card",
  color: "#FFFFFF"
})
```

## Syncing resources

Run the regular `pulumi up` command.


Built with [Mintlify](https://mintlify.com).