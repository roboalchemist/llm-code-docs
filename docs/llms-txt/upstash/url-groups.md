# Source: https://upstash.com/docs/qstash/sdks/ts/examples/url-groups.md

# Source: https://upstash.com/docs/qstash/sdks/py/examples/url-groups.md

# Source: https://upstash.com/docs/qstash/features/url-groups.md

# Source: https://upstash.com/docs/qstash/sdks/ts/examples/url-groups.md

# Source: https://upstash.com/docs/qstash/sdks/py/examples/url-groups.md

# Source: https://upstash.com/docs/qstash/features/url-groups.md

# Source: https://upstash.com/docs/qstash/sdks/ts/examples/url-groups.md

# Source: https://upstash.com/docs/qstash/sdks/py/examples/url-groups.md

# Source: https://upstash.com/docs/qstash/features/url-groups.md

# Source: https://upstash.com/docs/qstash/sdks/ts/examples/url-groups.md

# Source: https://upstash.com/docs/qstash/sdks/py/examples/url-groups.md

# Source: https://upstash.com/docs/qstash/features/url-groups.md

# Source: https://upstash.com/docs/qstash/sdks/ts/examples/url-groups.md

# Source: https://upstash.com/docs/qstash/sdks/py/examples/url-groups.md

# Source: https://upstash.com/docs/qstash/features/url-groups.md

# Source: https://upstash.com/docs/qstash/sdks/ts/examples/url-groups.md

# URL Groups

#### Create a URL Group and add 2 endpoints

```typescript  theme={"system"}
import { Client } from "@upstash/qstash";

const client = new Client({ token: "<QSTASH_TOKEN>" });
const urlGroups = client.urlGroups;
await urlGroups.addEndpoints({
  name: "url_group_name",
  endpoints: [
    { url: "https://my-endpoint-1" },
    { url: "https://my-endpoint-2" },
  ],
});
```

#### Get URL Group by name

```typescript  theme={"system"}
import { Client } from "@upstash/qstash";

const client = new Client({ token: "<QSTASH_TOKEN>" });
const urlGroups = client.urlGroups;
const urlGroup = await urlGroups.get("urlGroupName");
console.log(urlGroup.name, urlGroup.endpoints);
```

#### List URL Groups

```typescript  theme={"system"}
import { Client } from "@upstash/qstash";

const client = new Client({ token: "<QSTASH_TOKEN>" });
const allUrlGroups = await client.urlGroups.list();
for (const urlGroup of allUrlGroups) {
  console.log(urlGroup.name, urlGroup.endpoints);
}
```

#### Remove an endpoint from a URL Group

```typescript  theme={"system"}
import { Client } from "@upstash/qstash";

const client = new Client({ token: "<QSTASH_TOKEN>" });
const urlGroups = client.urlGroups;
await urlGroups.removeEndpoints({
  name: "urlGroupName",
  endpoints: [{ url: "https://my-endpoint-1" }],
});
```

#### Delete a URL Group

```typescript  theme={"system"}
import { Client } from "@upstash/qstash";

const client = new Client({ token: "<QSTASH_TOKEN>" });
const urlGroups = client.urlGroups;
await urlGroups.delete("urlGroupName");
```
