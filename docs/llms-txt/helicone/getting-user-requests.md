# Source: https://docs.helicone.ai/guides/cookbooks/getting-user-requests.md

# Getting User Requests

> Use the Request API to retrieve user-specific requests, allowing you to monitor, debug, and track costs for individual users.

The [Request API](/rest/request/post-v1requestquery) allows you to build a request, where you can specify filtering criteria to retrieve all requests made by a user.

<Note>
  **API Endpoint Note:** This guide uses the `/v1/request/query` endpoint which is optimized for small to medium datasets.

  For **large datasets or bulk exports**, use the [/v1/request/query-clickhouse](/rest/request/post-v1requestquery-clickhouse) endpoint instead, which has a different filter structure:

  * `/query` uses `request` wrapper: `{"filter": {"request": {"user_id": {...}}}}`
  * `/query-clickhouse` uses `request_response_rmt` wrapper: `{"filter": {"request_response_rmt": {"user_id": {...}}}}`
</Note>

<Frame>
  <img src="https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/example-user-request.png?fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=dd4eaf668f2ce44202c6f67ce069967b" alt="Helicone Request API example showing how you can built a request and specify filtering criteria and other advanced capabilities." data-og-width="1440" width="1440" data-og-height="796" height="796" data-path="images/use-cases/example-user-request.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/example-user-request.png?w=280&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=d98f2e0cf2b44091d53a49cb9fe2e275 280w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/example-user-request.png?w=560&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=9ec39ee87acaf1eb79b0ea25fce339be 560w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/example-user-request.png?w=840&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=7cc180dbe391c777b5c44bf91f404272 840w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/example-user-request.png?w=1100&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=617bd6a9d141b018ed099a01e9977376 1100w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/example-user-request.png?w=1650&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=c6863bb488a5ecd107dcc1a8c5b85933 1650w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/use-cases/example-user-request.png?w=2500&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=afc8cae8044df2531451d9c1ad53b0b4 2500w" />
</Frame>

## Use Cases

* Monitor your user's usage pattern and behavior.
* Access user-specific requests to pinpoint the errors and bebug more efficiently.
* Track requests and costs per user to facilitate better cost control.
* Detect unusual or potentially harmful user behaviors.

## Retrieving Requests by User ID

Here's an example to get all the requests where `user_id` is `abc@email.com`.

```bash  theme={null}
curl --request POST \
  --url https://api.helicone.ai/v1/request/query \
  --header "Content-Type: application/json" \
  --header "authorization: Bearer $HELICONE_API_KEY" \
  --data '{
  "filter": {
    "request": {
      "user_id": {
        "equals": "abc@email.com"
      }
    }
  }
}'
```

<Tip>
  By using the [Request API](/rest/request/post-v1requestquery), the code
  snippet will dynamically populate on the page, so you can copy and paste.{" "}
</Tip>

## Adding Additional Filters

You can structure your query to add any number of filters.

**Note**: To add multiple filters, change the filter to a branch and nest the ANDs/ORs as an abstract syntax tree.

```bash  theme={null}
curl --request POST \
  --url https://api.helicone.ai/v1/request/query \
  --header "Content-Type: application/json" \
  --header "authorization: Bearer $HELICONE_API_KEY" \
  --data '{
  "filter": {
    "operator": "and",
    "right": {
      "request": {
        "model": {
          "contains": "gpt-4o-mini"
        }
      }
    },
    "left": {
      "request": {
        "user_id": {
          "equals": "abc@email.com"
        }
      }
    }
  }
}'
```

***

<Accordion title="Need more help?">
  Additional questions or feedback? Reach out to
  [help@helicone.ai](mailto:help@helicone.ai) or [schedule a
  call](https://cal.com/team/helicone/helicone-discovery) with us.
</Accordion>
