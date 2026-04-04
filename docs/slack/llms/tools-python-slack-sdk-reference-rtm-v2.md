Source: https://docs.slack.dev/tools/python-slack-sdk/reference/rtm/v2

# Module slack_sdk.rtm.v2

## Classes

`class RTMClient (*,   token: str | None = None,   web_client: [WebClient](../../web/client.html#slack_sdk.web.client.WebClient "slack_sdk.web.client.WebClient") | None = None,   auto_reconnect_enabled: bool = True,   ssl: ssl.SSLContext | None = None,   proxy: str | None = None,   timeout: int = 30,   base_url: str = 'https://slack.com/api/',   headers: dict | None = None,   ping_interval: int = 5,   concurrency: int = 10,   logger: logging.Logger | None = None,   on_message_listeners: List[Callable[[str], None]] | None = None,   on_error_listeners: List[Callable[[Exception], None]] | None = None,   on_close_listeners: List[Callable[[int, str | None], None]] | None = None,   trace_enabled: bool = False,   all_message_trace_enabled: bool = False,   ping_pong_trace_enabled: bool = False)`

Expand source code

```typescript
class RTMClient:
    token: Optional[str]
    bot_id: Optional[str]
    default_auto_reconnect_enabled: bool
    auto_reconnect_enabled: bool
    ssl: Optional[SSLContext]
    proxy: Optional[str]
    timeout: int
    base_url: str
    ping_interval: int
    logger: Logger
    web_client: WebClient

    current_session: Optional[Connection]
    current_session_state: Optional[ConnectionState]
    wss_uri: Optional[str]

    message_queue: Queue
    message_listeners: List[Callable[["RTMClient", dict], None]]
    message_processor: IntervalRunner
    message_workers: ThreadPoolExecutor

    closed: bool
    connect_operation_lock: Lock

    on_message_listeners: List[Callable[[str], None]]
    on_error_listeners: List[Callable[[Exception], None]]
    on_close_listeners: List[Callable[[int, Optional[str]], None]]

    def __init__(
        self,
        *,
        token: Optional[str] = None,
        web_client: Optional[WebClient] = None,
        auto_reconnect_enabled: bool = True,
        ssl: Optional[SSLContext] = None,
        proxy: Optional[str] = None,
        timeout: int = 30,
        base_url: str = WebClient.BASE_URL,
        headers: Optional[dict] = None,
        ping_interval: int = 5,
        concurrency: int = 10,
        logger: Optional[logging.Logger] = None,
        on_message_listeners: Optional[List[Callable[[str], None]]] = None,
        on_error_listeners: Optional[List[Callable[[Exception], None]]] = None,
        on_close_listeners: Optional[List[Callable[[int, Optional[str]], None]]] = None,
        trace_enabled: bool = False,
        all_message_trace_enabled: bool = False,
        ping_pong_trace_enabled: bool = False,
    ):
        self.token = token.strip() if token is not None else None
        self.bot_id = None
        self.default_auto_reconnect_enabled = auto_reconnect_enabled
        # You may want temporarily turn off the auto_reconnect as necessary
        self.auto_reconnect_enabled = self.default_auto_reconnect_enabled
        self.ssl = ssl
        self.proxy = proxy
        self.timeout = timeout
        self.base_url = base_url
        self.headers = headers
        self.ping_interval = ping_interval
        self.logger = logger or logging.getLogger(__name__)
        if self.proxy is None or len(self.proxy.strip()) == 0:
            env_variable = load_http_proxy_from_env(self.logger)
            if env_variable is not None:
                self.proxy = env_variable

        self.web_client = web_client or WebClient(
            token=self.token,
            base_url=self.base_url,
            timeout=self.timeout,
            ssl=self.ssl,
            proxy=self.proxy,
            headers=self.headers,
            logger=logger,
        )

        self.on_message_listeners = on_message_listeners or []

        self.on_error_listeners = on_error_listeners or []
        self.on_close_listeners = on_close_listeners or []

        self.trace_enabled = trace_enabled
        self.all_message_trace_enabled = all_message_trace_enabled
        self.ping_pong_trace_enabled = ping_pong_trace_enabled

        self.message_queue = Queue()

        def goodbye_listener(_self, event: dict):
            if event.get("type") == "goodbye":
                message = "Got a goodbye message. Reconnecting to the server ..."
                self.logger.info(message)
                self.connect_to_new_endpoint(force=True)

        self.message_listeners = [goodbye_listener]
        self.socket_mode_request_listeners = []

        self.current_session = None
        self.current_session_state = ConnectionState()
        self.current_session_runner = IntervalRunner(self._run_current_session, 0.1).start()
        self.wss_uri = None

        self.current_app_monitor_started = False
        self.current_app_monitor = IntervalRunner(
            self._monitor_current_session,
            self.ping_interval,
        )

        self.closed = False
        self.connect_operation_lock = Lock()

        self.message_processor = IntervalRunner(self.process_messages, 0.001).start()
        self.message_workers = ThreadPoolExecutor(max_workers=concurrency)

    # --------------------------------------------------------------
    # Decorator to register listeners
    # --------------------------------------------------------------

    def on(self, event_type: str) -> Callable:
        """Registers a new event listener.

        Args:
            event_type: str representing an event's type (e.g., message, reaction_added)
        """

        def __call__(*args, **kwargs):
            func = args[0]
            if func is not None:
                if isinstance(func, Callable):
                    name = (
                        func.__name__
                        if hasattr(func, "__name__")
                        else f"{func.__class__.__module__}.{func.__class__.__name__}"
                    )
                    inspect_result: inspect.FullArgSpec = inspect.getfullargspec(func)
                    if inspect_result is not None and len(inspect_result.args) != 2:
                        actual_args = ", ".join(inspect_result.args)
                        error = f"The listener '{name}' must accept two args: client, event (actual: {actual_args})"
                        raise SlackClientError(error)

                    def new_message_listener(_self, event: dict):
                        actual_event_type = event.get("type")
                        if event.get("bot_id") == self.bot_id:
                            # SKip the events generated by this bot user
                            return
                        # https://github.com/slackapi/python-slack-sdk/issues/533
                        if event_type == "*" or (actual_event_type is not None and actual_event_type == event_type):
                            func(_self, event)

                    self.message_listeners.append(new_message_listener)
                else:
                    error = f"The listener '{func}' is not a Callable (actual: {type(func).__name__})"
                    raise SlackClientError(error)
            # Not to cause modification to the decorated method
            return func

        return __call__

    # --------------------------------------------------------------
    # Connections
    # --------------------------------------------------------------

    def is_connected(self) -> bool:
        """Returns True if this client is connected."""
        return self.current_session is not None and self.current_session.is_active()

    def issue_new_wss_url(self) -> str:
        """Acquires a new WSS URL using rtm.connect API method"""
        try:
            api_response = self.web_client.rtm_connect()
            return api_response["url"]
        except SlackApiError as e:
            if e.response["error"] == "ratelimited":
                delay = int(e.response.headers.get("Retry-After", "30"))  # Tier1
                self.logger.info(f"Rate limited. Retrying in {delay} seconds...")
                time.sleep(delay)
                # Retry to issue a new WSS URL
                return self.issue_new_wss_url()
            else:
                # other errors
                self.logger.error(f"Failed to retrieve WSS URL: {e}")
                raise e

    def connect_to_new_endpoint(self, force: bool = False):
        """Acquires a new WSS URL and tries to connect to the endpoint."""
        with self.connect_operation_lock:
            if force or not self.is_connected():
                self.logger.info("Connecting to a new endpoint...")
                self.wss_uri = self.issue_new_wss_url()
                self.connect()
                self.logger.info("Connected to a new endpoint...")

    def connect(self):
        """Starts talking to the RTM server through a WebSocket connection"""
        if self.bot_id is None:
            self.bot_id = self.web_client.auth_test()["bot_id"]

        old_session: Optional[Connection] = self.current_session
        old_current_session_state: ConnectionState = self.current_session_state

        if self.wss_uri is None:
            self.wss_uri = self.issue_new_wss_url()

        current_session = Connection(
            url=self.wss_uri,
            logger=self.logger,
            ping_interval=self.ping_interval,
            trace_enabled=self.trace_enabled,
            all_message_trace_enabled=self.all_message_trace_enabled,
            ping_pong_trace_enabled=self.ping_pong_trace_enabled,
            receive_buffer_size=1024,
            proxy=self.proxy,
            on_message_listener=self.run_all_message_listeners,
            on_error_listener=self.run_all_error_listeners,
            on_close_listener=self.run_all_close_listeners,
            connection_type_name="RTM",
        )
        current_session.connect()

        if old_current_session_state is not None:
            old_current_session_state.terminated = True
        if old_session is not None:
            old_session.close()

        self.current_session = current_session
        self.current_session_state = ConnectionState()
        self.auto_reconnect_enabled = self.default_auto_reconnect_enabled

        if not self.current_app_monitor_started:
            self.current_app_monitor_started = True
            self.current_app_monitor.start()

        self.logger.info(f"A new session has been established (session id: {self.session_id()})")

    def disconnect(self):
        """Disconnects the current session."""
        self.current_session.disconnect()

    def close(self) -> None:
        """
        Closes this instance and cleans up underlying resources.
        After calling this method, this instance is no longer usable.
        """
        self.closed = True
        self.disconnect()
        self.current_session.close()

    def start(self) -> None:
        """Establishes an RTM connection and blocks the current thread."""
        self.connect()
        Event().wait()

    def send(self, payload: Union[dict, str]) -> None:
        if payload is None:
            return
        if self.current_session is None or not self.current_session.is_active():
            raise SlackClientError("The RTM client is not connected to the Slack servers")
        if isinstance(payload, str):
            self.current_session.send(payload)
        else:
            self.current_session.send(json.dumps(payload))

    # --------------------------------------------------------------
    # WS Message Processor
    # --------------------------------------------------------------

    def enqueue_message(self, message: str):
        self.message_queue.put(message)
        if self.logger.level <= logging.DEBUG:
            self.logger.debug(f"A new message enqueued (current queue size: {self.message_queue.qsize()})")

    def process_message(self):
        try:
            raw_message = self.message_queue.get(timeout=1)
            if self.logger.level <= logging.DEBUG:
                self.logger.debug(f"A message dequeued (current queue size: {self.message_queue.qsize()})")

            if raw_message is not None:
                message: dict = {}
                if raw_message.startswith("{"):
                    message = json.loads(raw_message)

                def _run_message_listeners():
                    self.run_message_listeners(message)

                self.message_workers.submit(_run_message_listeners)
        except Empty:
            pass

    def process_messages(self) -> None:
        while not self.closed:
            try:
                self.process_message()
            except Exception as e:
                self.logger.exception(f"Failed to process a message: {e}")

    def run_message_listeners(self, message: dict) -> None:
        type = message.get("type")
        if self.logger.level <= logging.DEBUG:
            self.logger.debug(f"Message processing started (type: {type})")
        try:
            for listener in self.message_listeners:
                try:
                    listener(self, message)
                except Exception as e:
                    self.logger.exception(f"Failed to run a message listener: {e}")
        except Exception as e:
            self.logger.exception(f"Failed to run message listeners: {e}")
        finally:
            if self.logger.level <= logging.DEBUG:
                self.logger.debug(f"Message processing completed (type: {type})")

    # --------------------------------------------------------------
    # Internals
    # --------------------------------------------------------------

    def session_id(self) -> Optional[str]:
        if self.current_session is not None:
            return self.current_session.session_id
        return None

    def run_all_message_listeners(self, message: str):
        if self.logger.level <= logging.DEBUG:
            self.logger.debug(f"on_message invoked: (message: {message})")
        self.enqueue_message(message)
        for listener in self.on_message_listeners:
            listener(message)

    def run_all_error_listeners(self, error: Exception):
        self.logger.exception(
            f"on_error invoked (session id: {self.session_id()}, " f"error: {type(error).__name__}, message: {error})"
        )
        for listener in self.on_error_listeners:
            listener(error)

    def run_all_close_listeners(self, code: int, reason: Optional[str] = None):
        if self.logger.level <= logging.DEBUG:
            self.logger.debug(f"on_close invoked (session id: {self.session_id()})")
        if self.auto_reconnect_enabled:
            self.logger.info("Received CLOSE event. Going to reconnect... " f"(session id: {self.session_id()})")
            self.connect_to_new_endpoint()
        for listener in self.on_close_listeners:
            listener(code, reason)

    def _run_current_session(self):
        if self.current_session is not None and self.current_session.is_active():
            session_id = self.session_id()
            try:
                self.logger.info("Starting to receive messages from a new connection" f" (session id: {session_id})")
                self.current_session_state.terminated = False
                self.current_session.run_until_completion(self.current_session_state)
                self.logger.info("Stopped receiving messages from a connection" f" (session id: {session_id})")
            except Exception as e:
                self.logger.exception(
                    "Failed to start or stop the current session" f" (session id: {session_id}, error: {e})"
                )

    def _monitor_current_session(self):
        if self.current_app_monitor_started:
            try:
                self.current_session.check_state()

                if self.auto_reconnect_enabled and (self.current_session is None or not self.current_session.is_active()):
                    self.logger.info(
                        "The session seems to be already closed. Going to reconnect... " f"(session id: {self.session_id()})"
                    )
                    self.connect_to_new_endpoint()
            except Exception as e:
                self.logger.error(
                    "Failed to check the current session or reconnect to the server "
                    f"(session id: {self.session_id()}, error: {type(e).__name__}, message: {e})"
                )
```

### Class variables

`var auto_reconnect_enabled : bool`

The type of the None singleton.

`var base_url : str`

The type of the None singleton.

`var bot_id : str | None`

The type of the None singleton.

`var closed : bool`

The type of the None singleton.

`var connect_operation_lock : _thread.lock`

The type of the None singleton.

`var current_session : [Connection](../../socket_mode/builtin/connection.html#slack_sdk.socket_mode.builtin.connection.Connection "slack_sdk.socket_mode.builtin.connection.Connection") | None`

The type of the None singleton.

`var current_session_state : [ConnectionState](../../socket_mode/builtin/connection.html#slack_sdk.socket_mode.builtin.connection.ConnectionState "slack_sdk.socket_mode.builtin.connection.ConnectionState") | None`

The type of the None singleton.

`var default_auto_reconnect_enabled : bool`

The type of the None singleton.

`var logger : logging.Logger`

The type of the None singleton.

`var message_listeners : List[Callable[[[RTMClient](../../rtm_v2/index.html#slack_sdk.rtm_v2.RTMClient "slack_sdk.rtm_v2.RTMClient"), dict], None]]`

The type of the None singleton.

`var message_processor : [IntervalRunner](../../socket_mode/interval_runner.html#slack_sdk.socket_mode.interval_runner.IntervalRunner "slack_sdk.socket_mode.interval_runner.IntervalRunner")`

The type of the None singleton.

`var message_queue : queue.Queue`

The type of the None singleton.

`var message_workers : concurrent.futures.thread.ThreadPoolExecutor`

The type of the None singleton.

`var on_close_listeners : List[Callable[[int, str | None], None]]`

The type of the None singleton.

`var on_error_listeners : List[Callable[[Exception], None]]`

The type of the None singleton.

`var on_message_listeners : List[Callable[[str], None]]`

The type of the None singleton.

`var ping_interval : int`

The type of the None singleton.

`var proxy : str | None`

The type of the None singleton.

`var ssl : ssl.SSLContext | None`

The type of the None singleton.

`var timeout : int`

The type of the None singleton.

`var token : str | None`

The type of the None singleton.

`var web_client : [WebClient](../../web/client.html#slack_sdk.web.client.WebClient "slack_sdk.web.client.WebClient")`

The type of the None singleton.

`var wss_uri : str | None`

The type of the None singleton.

### Methods

`def close(self) ‑> None`

Expand source code

```python
def close(self) -> None:
    """
    Closes this instance and cleans up underlying resources.
    After calling this method, this instance is no longer usable.
    """
    self.closed = True
    self.disconnect()
    self.current_session.close()
```

Closes this instance and cleans up underlying resources. After calling this method, this instance is no longer usable.

`def connect(self)`

Expand source code

```python
def connect(self):
    """Starts talking to the RTM server through a WebSocket connection"""
    if self.bot_id is None:
        self.bot_id = self.web_client.auth_test()["bot_id"]

    old_session: Optional[Connection] = self.current_session
    old_current_session_state: ConnectionState = self.current_session_state

    if self.wss_uri is None:
        self.wss_uri = self.issue_new_wss_url()

    current_session = Connection(
        url=self.wss_uri,
        logger=self.logger,
        ping_interval=self.ping_interval,
        trace_enabled=self.trace_enabled,
        all_message_trace_enabled=self.all_message_trace_enabled,
        ping_pong_trace_enabled=self.ping_pong_trace_enabled,
        receive_buffer_size=1024,
        proxy=self.proxy,
        on_message_listener=self.run_all_message_listeners,
        on_error_listener=self.run_all_error_listeners,
        on_close_listener=self.run_all_close_listeners,
        connection_type_name="RTM",
    )
    current_session.connect()

    if old_current_session_state is not None:
        old_current_session_state.terminated = True
    if old_session is not None:
        old_session.close()

    self.current_session = current_session
    self.current_session_state = ConnectionState()
    self.auto_reconnect_enabled = self.default_auto_reconnect_enabled

    if not self.current_app_monitor_started:
        self.current_app_monitor_started = True
        self.current_app_monitor.start()

    self.logger.info(f"A new session has been established (session id: {self.session_id()})")
```

Starts talking to the RTM server through a WebSocket connection

`def connect_to_new_endpoint(self, force: bool = False)`

Expand source code

```python
def connect_to_new_endpoint(self, force: bool = False):
    """Acquires a new WSS URL and tries to connect to the endpoint."""
    with self.connect_operation_lock:
        if force or not self.is_connected():
            self.logger.info("Connecting to a new endpoint...")
            self.wss_uri = self.issue_new_wss_url()
            self.connect()
            self.logger.info("Connected to a new endpoint...")
```

Acquires a new WSS URL and tries to connect to the endpoint.

`def disconnect(self)`

Expand source code

```python
def disconnect(self):
    """Disconnects the current session."""
    self.current_session.disconnect()
```

Disconnects the current session.

`def enqueue_message(self, message: str)`

Expand source code

```python
def enqueue_message(self, message: str):
    self.message_queue.put(message)
    if self.logger.level <= logging.DEBUG:
        self.logger.debug(f"A new message enqueued (current queue size: {self.message_queue.qsize()})")
```

`def is_connected(self) ‑> bool`

Expand source code

```python
def is_connected(self) -> bool:
    """Returns True if this client is connected."""
    return self.current_session is not None and self.current_session.is_active()
```

Returns True if this client is connected.

`def issue_new_wss_url(self) ‑> str`

Expand source code

```python
def issue_new_wss_url(self) -> str:
    """Acquires a new WSS URL using rtm.connect API method"""
    try:
        api_response = self.web_client.rtm_connect()
        return api_response["url"]
    except SlackApiError as e:
        if e.response["error"] == "ratelimited":
            delay = int(e.response.headers.get("Retry-After", "30"))  # Tier1
            self.logger.info(f"Rate limited. Retrying in {delay} seconds...")
            time.sleep(delay)
            # Retry to issue a new WSS URL
            return self.issue_new_wss_url()
        else:
            # other errors
            self.logger.error(f"Failed to retrieve WSS URL: {e}")
            raise e
```

Acquires a new WSS URL using rtm.connect API method

`def on(self, event_type: str) ‑> Callable`

Expand source code

```typescript
def on(self, event_type: str) -> Callable:
    """Registers a new event listener.

    Args:
        event_type: str representing an event's type (e.g., message, reaction_added)
    """

    def __call__(*args, **kwargs):
        func = args[0]
        if func is not None:
            if isinstance(func, Callable):
                name = (
                    func.__name__
                    if hasattr(func, "__name__")
                    else f"{func.__class__.__module__}.{func.__class__.__name__}"
                )
                inspect_result: inspect.FullArgSpec = inspect.getfullargspec(func)
                if inspect_result is not None and len(inspect_result.args) != 2:
                    actual_args = ", ".join(inspect_result.args)
                    error = f"The listener '{name}' must accept two args: client, event (actual: {actual_args})"
                    raise SlackClientError(error)

                def new_message_listener(_self, event: dict):
                    actual_event_type = event.get("type")
                    if event.get("bot_id") == self.bot_id:
                        # SKip the events generated by this bot user
                        return
                    # https://github.com/slackapi/python-slack-sdk/issues/533
                    if event_type == "*" or (actual_event_type is not None and actual_event_type == event_type):
                        func(_self, event)

                self.message_listeners.append(new_message_listener)
            else:
                error = f"The listener '{func}' is not a Callable (actual: {type(func).__name__})"
                raise SlackClientError(error)
        # Not to cause modification to the decorated method
        return func

    return __call__
```

Registers a new event listener.

## Args

**`event_type`**

str representing an event's type (e.g., message, reaction\_added)

`def process_message(self)`

Expand source code

```python
def process_message(self):
    try:
        raw_message = self.message_queue.get(timeout=1)
        if self.logger.level <= logging.DEBUG:
            self.logger.debug(f"A message dequeued (current queue size: {self.message_queue.qsize()})")

        if raw_message is not None:
            message: dict = {}
            if raw_message.startswith("{"):
                message = json.loads(raw_message)

            def _run_message_listeners():
                self.run_message_listeners(message)

            self.message_workers.submit(_run_message_listeners)
    except Empty:
        pass
```

`def process_messages(self) ‑> None`

Expand source code

```python
def process_messages(self) -> None:
    while not self.closed:
        try:
            self.process_message()
        except Exception as e:
            self.logger.exception(f"Failed to process a message: {e}")
```

`def run_all_close_listeners(self, code: int, reason: str | None = None)`

Expand source code

```python
def run_all_close_listeners(self, code: int, reason: Optional[str] = None):
    if self.logger.level <= logging.DEBUG:
        self.logger.debug(f"on_close invoked (session id: {self.session_id()})")
    if self.auto_reconnect_enabled:
        self.logger.info("Received CLOSE event. Going to reconnect... " f"(session id: {self.session_id()})")
        self.connect_to_new_endpoint()
    for listener in self.on_close_listeners:
        listener(code, reason)
```

`def run_all_error_listeners(self, error: Exception)`

Expand source code

```python
def run_all_error_listeners(self, error: Exception):
    self.logger.exception(
        f"on_error invoked (session id: {self.session_id()}, " f"error: {type(error).__name__}, message: {error})"
    )
    for listener in self.on_error_listeners:
        listener(error)
```

`def run_all_message_listeners(self, message: str)`

Expand source code

```python
def run_all_message_listeners(self, message: str):
    if self.logger.level <= logging.DEBUG:
        self.logger.debug(f"on_message invoked: (message: {message})")
    self.enqueue_message(message)
    for listener in self.on_message_listeners:
        listener(message)
```

`def run_message_listeners(self, message: dict) ‑> None`

Expand source code

```typescript
def run_message_listeners(self, message: dict) -> None:
    type = message.get("type")
    if self.logger.level <= logging.DEBUG:
        self.logger.debug(f"Message processing started (type: {type})")
    try:
        for listener in self.message_listeners:
            try:
                listener(self, message)
            except Exception as e:
                self.logger.exception(f"Failed to run a message listener: {e}")
    except Exception as e:
        self.logger.exception(f"Failed to run message listeners: {e}")
    finally:
        if self.logger.level <= logging.DEBUG:
            self.logger.debug(f"Message processing completed (type: {type})")
```

`def send(self, payload: dict | str) ‑> None`

Expand source code

```python
def send(self, payload: Union[dict, str]) -> None:
    if payload is None:
        return
    if self.current_session is None or not self.current_session.is_active():
        raise SlackClientError("The RTM client is not connected to the Slack servers")
    if isinstance(payload, str):
        self.current_session.send(payload)
    else:
        self.current_session.send(json.dumps(payload))
```

`def session_id(self) ‑> str | None`

Expand source code

```python
def session_id(self) -> Optional[str]:
    if self.current_session is not None:
        return self.current_session.session_id
    return None
```

`def start(self) ‑> None`

Expand source code

```python
def start(self) -> None:
    """Establishes an RTM connection and blocks the current thread."""
    self.connect()
    Event().wait()
```

Establishes an RTM connection and blocks the current thread.
