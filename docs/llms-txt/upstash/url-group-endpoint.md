# Source: https://upstash.com/docs/qstash/howto/url-group-endpoint.md

# Create URL Groups and Endpoints

QStash allows you to group multiple APIs together into a single namespace,
called a `URL Group` (Previously, it was called `Topics`).
Read more about URL Groups [here](/qstash/features/url-groups).

There are two ways to create endpoints and URL Groups: The UI and the REST API.

## UI

Go to [console.upstash.com/qstash](https://console.upstash.com/qstash) and click
on the `URL Groups` tab. Afterwards you can create a new URL Group by giving it a name.
Keep in mind that URL Group names are restricted to alphanumeric, underscore, hyphen
and dot characters.

<img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/create_topic.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=68c281bd86e518fce7f6018d6a38160b" alt="" data-og-width="1996" width="1996" data-og-height="864" height="864" data-path="img/qstash/create_topic.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/create_topic.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=908f1973fd926d6172c75d854193a385 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/create_topic.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=80665304d01412bbf0ed3bb7590912e5 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/create_topic.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=4b2ebbf61a9a38b45e55521568f53584 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/create_topic.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=3c02da12cb02666fe0c62a898432dc24 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/create_topic.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=211dae323006945ee942903033f08cf7 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/create_topic.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=fb00f65816c97514b4075de0484ed73c 2500w" />

After creating the URL Group, you can add endpoints to it:

<img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/create_endpoint.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=e40121a341fc89481d4a565d8a1b4914" alt="" data-og-width="2032" width="2032" data-og-height="744" height="744" data-path="img/qstash/create_endpoint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/create_endpoint.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=1e1b84f2ea55ee98c305b249ffa49be1 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/create_endpoint.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=d5d2c9de6268c73dcfb24a3ac09b3516 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/create_endpoint.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=69517e5abb5f8dc5f78a0710b642ddfe 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/create_endpoint.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=2bd9ce24b74e39b8cc72674c2d4e142e 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/create_endpoint.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=f0b5a0f10b451ed0e4ba4abc5bb0b630 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/create_endpoint.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=fffde447eba91eedb319aa1f74c2b41b 2500w" />

## API

You can create a URL Group and endpoint using the [console](https://console.upstash.com/qstash) or [REST API](/qstash/api/url-groups/add-endpoint).

<CodeGroup>
  ```bash cURL theme={"system"}
  curl -XPOST https://qstash.upstash.io/v2/topics/:urlGroupName/endpoints \
    -H "Authorization: Bearer <token>" \
    -H "Content-Type: application/json" \
    -d '{
      "endpoints": [
        {
          "name": "endpoint1",
          "url": "https://example.com"
        },
        {
          "name": "endpoint2",
          "url": "https://somewhere-else.com"
        }
      ]
    }'
  ```

  ```typescript Typescript theme={"system"}
  import { Client } from "@upstash/qstash";

  const client = new Client({ token: "<QSTASH_TOKEN>" });
  const urlGroups = client.urlGroups;
  await urlGroups.addEndpoints({
    name: "urlGroupName",
    endpoints: [
      { name: "endpoint1", url: "https://example.com" },
      { name: "endpoint2", url: "https://somewhere-else.com" },
    ],
  });
  ```

  ```python Python theme={"system"}
  from qstash import QStash

  client = QStash("<QSTASH_TOKEN>")
  client.url_group.upsert_endpoints(
      url_group="url-group-name",
      endpoints=[
          {"name": "endpoint1", "url": "https://example.com"},
          {"name": "endpoint2", "url": "https://somewhere-else.com"},
      ],
  )
  ```
</CodeGroup>
