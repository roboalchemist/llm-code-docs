# Source: https://fastapi.tiangolo.com/reference/request/

# `Request` class[&para;](#request-class)

You can declare a parameter in a *path operation function* or dependency to be of type `Request` and then you can access the raw request object directly, without any validation, etc.

You can import it directly from `fastapi`:

`from fastapi import Request
`

Tip

When you want to define dependencies that should be compatible with both HTTP and WebSockets, you can define a parameter that takes an `HTTPConnection` instead of a `Request` or a `WebSocket`.

## 
``            fastapi.Request

[&para;](#fastapi.Request)

`Request(scope, receive=empty_receive, send=empty_send)
`

              Bases: `[HTTPConnection](../httpconnection/#fastapi.requests.HTTPConnection)`

                    Source code in `starlette/requests.py`

203
204
205
206
207
208
209
210

`def __init__(self, scope: Scope, receive: Receive = empty_receive, send: Send = empty_send):
    super().__init__(scope)
    assert scope["type"] == "http"
    self._receive = receive
    self._send = send
    self._stream_consumed = False
    self._is_disconnected = False
    self._form = None
`

### 
``            scope

      `instance-attribute`

[&para;](#fastapi.Request.scope)

`scope = scope
`

### 
``            app

      `property`

[&para;](#fastapi.Request.app)

`app
`

### 
``            url

      `property`

[&para;](#fastapi.Request.url)

`url
`

### 
``            base_url

      `property`

[&para;](#fastapi.Request.base_url)

`base_url
`

### 
``            headers

      `property`

[&para;](#fastapi.Request.headers)

`headers
`

### 
``            query_params

      `property`

[&para;](#fastapi.Request.query_params)

`query_params
`

### 
``            path_params

      `property`

[&para;](#fastapi.Request.path_params)

`path_params
`

### 
``            cookies

      `property`

[&para;](#fastapi.Request.cookies)

`cookies
`

### 
``            client

      `property`

[&para;](#fastapi.Request.client)

`client
`

### 
``            session

      `property`

[&para;](#fastapi.Request.session)

`session
`

### 
``            auth

      `property`

[&para;](#fastapi.Request.auth)

`auth
`

### 
``            user

      `property`

[&para;](#fastapi.Request.user)

`user
`

### 
``            state

      `property`

[&para;](#fastapi.Request.state)

`state
`

### 
``            method

      `property`

[&para;](#fastapi.Request.method)

`method
`

### 
``            receive

      `property`

[&para;](#fastapi.Request.receive)

`receive
`

### 
``            url_for

[&para;](#fastapi.Request.url_for)

`url_for(name, /, **path_params)
`

              Source code in `starlette/requests.py`

184
185
186
187
188
189

`def url_for(self, name: str, /, **path_params: Any) -> URL:
    url_path_provider: Router | Starlette | None = self.scope.get("router") or self.scope.get("app")
    if url_path_provider is None:
        raise RuntimeError("The `url_for` method can only be used inside a Starlette application or with a router.")
    url_path = url_path_provider.url_path_for(name, **path_params)
    return url_path.make_absolute_url(base_url=self.base_url)
`

### 
``            stream

      `async`

[&para;](#fastapi.Request.stream)

`stream()
`

              Source code in `starlette/requests.py`

220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238

`async def stream(self) -> AsyncGenerator[bytes, None]:
    if hasattr(self, "_body"):
        yield self._body
        yield b""
        return
    if self._stream_consumed:
        raise RuntimeError("Stream consumed")
    while not self._stream_consumed:
        message = await self._receive()
        if message["type"] == "http.request":
            body = message.get("body", b"")
            if not message.get("more_body", False):
                self._stream_consumed = True
            if body:
                yield body
        elif message["type"] == "http.disconnect":  # pragma: no branch
            self._is_disconnected = True
            raise ClientDisconnect()
    yield b""
`

### 
``            body

      `async`

[&para;](#fastapi.Request.body)

`body()
`

              Source code in `starlette/requests.py`

240
241
242
243
244
245
246

`async def body(self) -> bytes:
    if not hasattr(self, "_body"):
        chunks: list[bytes] = []
        async for chunk in self.stream():
            chunks.append(chunk)
        self._body = b"".join(chunks)
    return self._body
`

### 
``            json

      `async`

[&para;](#fastapi.Request.json)

`json()
`

              Source code in `starlette/requests.py`

248
249
250
251
252

`async def json(self) -> Any:
    if not hasattr(self, "_json"):  # pragma: no branch
        body = await self.body()
        self._json = json.loads(body)
    return self._json
`

### 
``            form

[&para;](#fastapi.Request.form)

`form(
    *,
    max_files=1000,
    max_fields=1000,
    max_part_size=1024 * 1024
)
`

              Source code in `starlette/requests.py`

289
290
291
292
293
294
295
296
297
298

`def form(
    self,
    *,
    max_files: int | float = 1000,
    max_fields: int | float = 1000,
    max_part_size: int = 1024 * 1024,
) -> AwaitableOrContextManager[FormData]:
    return AwaitableOrContextManagerWrapper(
        self._get_form(max_files=max_files, max_fields=max_fields, max_part_size=max_part_size)
    )
`

### 
``            close

      `async`

[&para;](#fastapi.Request.close)

`close()
`

              Source code in `starlette/requests.py`

300
301
302

`async def close(self) -> None:
    if self._form is not None:  # pragma: no branch
        await self._form.close()
`

### 
``            is_disconnected

      `async`

[&para;](#fastapi.Request.is_disconnected)

`is_disconnected()
`

              Source code in `starlette/requests.py`

304
305
306
307
308
309
310
311
312
313
314
315
316

`async def is_disconnected(self) -> bool:
    if not self._is_disconnected:
        message: Message = {}

        # If message isn't immediately available, move on
        with anyio.CancelScope() as cs:
            cs.cancel()
            message = await self._receive()

        if message.get("type") == "http.disconnect":
            self._is_disconnected = True

    return self._is_disconnected
`

### 
``            send_push_promise

      `async`

[&para;](#fastapi.Request.send_push_promise)

`send_push_promise(path)
`

              Source code in `starlette/requests.py`

318
319
320
321
322
323
324

`async def send_push_promise(self, path: str) -> None:
    if "http.response.push" in self.scope.get("extensions", {}):
        raw_headers: list[tuple[bytes, bytes]] = []
        for name in SERVER_PUSH_HEADERS_TO_COPY:
            for value in self.headers.getlist(name):
                raw_headers.append((name.encode("latin-1"), value.encode("latin-1")))
        await self._send({"type": "http.response.push", "path": path, "headers": raw_headers})
`