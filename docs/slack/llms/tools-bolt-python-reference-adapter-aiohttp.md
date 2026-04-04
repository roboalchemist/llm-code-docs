Source: https://docs.slack.dev/tools/bolt-python/reference/adapter/aiohttp

# Module slack_bolt.adapter.aiohttp

## Functions

`async def to_aiohttp_response(bolt_resp: [BoltResponse](../../response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse")) ‑> aiohttp.web_response.Response`

Expand source code

```python
async def to_aiohttp_response(bolt_resp: BoltResponse) -> web.Response:
    content_type = bolt_resp.headers.pop(
        "content-type",
        ["application/json" if bolt_resp.body.startswith("{") else "text/plain"],
    )[0]
    content_type = re.sub(r";\s*charset=utf-8", "", content_type)
    resp = web.Response(
        status=bolt_resp.status,
        body=bolt_resp.body,
        headers=bolt_resp.first_headers_without_set_cookie(),
        content_type=content_type,
    )
    for cookie in bolt_resp.cookies():
        for name, c in cookie.items():
            resp.set_cookie(
                name=name,
                value=c.value,
                max_age=c.get("max-age"),
                expires=c.get("expires"),
                path=c.get("path"),  # type: ignore[arg-type]
                domain=c.get("domain"),
                secure=True,
                httponly=True,
            )
    return resp
```

`async def to_bolt_request(request: aiohttp.web_request.Request) ‑> [AsyncBoltRequest](../../request/async_request.html#slack_bolt.request.async_request.AsyncBoltRequest "slack_bolt.request.async_request.AsyncBoltRequest")`

Expand source code

```python
async def to_bolt_request(request: web.Request) -> AsyncBoltRequest:
    return AsyncBoltRequest(
        body=await request.text(),
        query=request.query_string,
        headers=request.headers,  # type: ignore[arg-type]
    )
```
