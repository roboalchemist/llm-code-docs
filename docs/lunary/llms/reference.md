# Source: https://docs.lunary.ai/docs/integrations/python/reference.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Python SDK Reference

## Classes

| Class                | Description                                               |
| -------------------- | --------------------------------------------------------- |
| `EventQueue`         | A class that represents a queue of events.                |
| `Consumer`           | A class that consumes events from the `EventQueue`.       |
| `UserContextManager` | A context manager for setting and resetting user context. |

## Methods

| Method                                                                                                                                                                                                             | Description                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------- |
| `config(app_id: str \| None = None, verbose: str \| None = None, api_url: str \| None = None, disable_ssl_verify: bool \| None = None)`                                                                            | Configures the SDK with the given parameters.  |
| `track_event(event_type: str, event_name: str, run_id: uuid, parent_run_id: uuid, name: str, input: Any, output: Any, error: Any, token_usage: Any, user_id: str, user_props: Any, tags: Any, extra: Any) -> None` | Tracks an event with the given parameters.     |
| `handle_internal_error(e: Exception) -> None`                                                                                                                                                                      | Handles internal errors.                       |
| `wrap(fn: Callable, type: str, name: str, user_id: str, user_props: Any, tags: Any, input_parser: Callable, output_parser: Callable) -> Callable`                                                                  | Wraps a function with monitoring capabilities. |
| `monitor(object: OpenAIUtils) -> None`                                                                                                                                                                             | Monitors an instance of `OpenAIUtils`.         |
| `identify(user_id: str, user_props: Any) -> UserContextManager`                                                                                                                                                    | Identifies a user and sets the user context.   |

## Decorators

| Decorator                                                                | Description                                     |
| ------------------------------------------------------------------------ | ----------------------------------------------- |
| `agent(name: str, user_id: str, user_props: Any, tags: Any) -> Callable` | A decorator for marking a function as an agent. |
| `tool(name: str, user_id: str, user_props: Any, tags: Any) -> Callable`  | A decorator for marking a function as a tool.   |

## Context Variables

| Variable         | Description                                     |
| ---------------- | ----------------------------------------------- |
| `user_ctx`       | A context variable for storing the user ID.     |
| `user_props_ctx` | A context variable for storing user properties. |

## Environment variables

| Variable             | Description                                                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `LUNARY_PUBLIC_KEY`  | Your project's public key                                                                                          |
| `LUNARY_PRIVATE_KEY` | Your project's private key                                                                                         |
| `LUNARY_VERBOSE`     | Enable verbose logging                                                                                             |
| `LUNARY_API_URL`     | Base URL for the API server. Defaults to `https://api.lunary.ai`; can be customized for self-hosting or local use. |
| `DISABLE_SSL_VERIFY` | Disable SSL verification if set to `True`                                                                          |
