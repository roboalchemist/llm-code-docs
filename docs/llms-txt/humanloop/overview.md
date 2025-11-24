# Source: https://humanloop.com/docs/introduction/overview.md

# Overview

> Learn how to integrate Humanloop into your applications using our Python and TypeScript SDKs or REST API.


The Humanloop platform can be accessed through the [API](/docs/v5/api) or through our Python and TypeScript SDKs.

<Cards>
  <Card
    title="TypeScript â"
    icon="fa-brands fa-js"
    href="https://www.npmjs.com/package/humanloop"
  />
  <Card
    title="Python â"
    icon="fa-brands fa-python"
    href="https://pypi.org/project/humanloop/"
  />
  
</Cards>

### Usage Examples

<Tabs>

<Tab title="TypeScript">

```shell title="Installation"
npm install humanloop
```

```typescript title="Example usage"
import { HumanloopClient } from "humanloop";

const humanloop = new HumanloopClient({ apiKey: "YOUR_API_KEY" });

// Check that the authentication was successful
console.log(await humanloop.prompts.list());
```

</Tab>

<Tab title="Python">

```shell title="Installation"
pip install humanloop
```

```python title="Example usage"
from humanloop import Humanloop
hl = Humanloop(api_key="<YOUR Humanloop API KEY>")

# Check that the authentication was successful
print(hl.prompts.list())
```

</Tab>
</Tabs>
