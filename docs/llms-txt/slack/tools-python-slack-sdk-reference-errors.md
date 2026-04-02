Source: https://docs.slack.dev/tools/python-slack-sdk/reference/errors

# Module slack_sdk.errors

Errors that can be raised by this SDK

## Classes

`class BotUserAccessError (*args, **kwargs)`

Expand source code

```text
class BotUserAccessError(SlackClientError):
    """Error raised when an 'xoxb-*' token is
    being used for a Slack API method that only accepts 'xoxp-*' tokens.
    """
```

Error raised when an 'xoxb-_' token is being used for a Slack API method that only accepts 'xoxp-_' tokens.

### Ancestors

* [SlackClientError](#slack_sdk.errors.SlackClientError "slack_sdk.errors.SlackClientError")
* builtins.Exception
* builtins.BaseException

`class SlackApiError (message, response)`

Expand source code

```typescript
class SlackApiError(SlackClientError):
    """Error raised when Slack does not send the expected response.

    Attributes:
        response (SlackResponse): The SlackResponse object containing all of the data sent back from the API.

    Note:
        The message (str) passed into the exception is used when
        a user converts the exception to a str.
        i.e. str(SlackApiError("This text will be sent as a string."))
    """

    def __init__(self, message, response):
        msg = f"{message}\nThe server responded with: {response}"
        self.response = response
        super(SlackApiError, self).__init__(msg)
```

Error raised when Slack does not send the expected response.

## Attributes

**`response`** : `SlackResponse`

The SlackResponse object containing all of the data sent back from the API.

## Note

The message (str) passed into the exception is used when a user converts the exception to a str. i.e. str(SlackApiError("This text will be sent as a string."))

### Ancestors (2)

* [SlackClientError](#slack_sdk.errors.SlackClientError "slack_sdk.errors.SlackClientError")
* builtins.Exception
* builtins.BaseException

`class SlackClientConfigurationError (*args, **kwargs)`

Expand source code

```typescript
class SlackClientConfigurationError(SlackClientError):
    """Error raised because of invalid configuration on the client side:
    * when attempting to send messages over the websocket when the connection is closed.
    * when external system (e.g., Amazon S3) configuration / credentials are not correct
    """
```

Error raised because of invalid configuration on the client side: \* when attempting to send messages over the websocket when the connection is closed. \* when external system (e.g., Amazon S3) configuration / credentials are not correct

### Ancestors (3)

* [SlackClientError](#slack_sdk.errors.SlackClientError "slack_sdk.errors.SlackClientError")
* builtins.Exception
* builtins.BaseException

`class SlackClientError (*args, **kwargs)`

Expand source code

```text
class SlackClientError(Exception):
    """Base class for Client errors"""
```

Base class for Client errors

### Ancestors (4)

* builtins.Exception
* builtins.BaseException

### Subclasses

* [BotUserAccessError](#slack_sdk.errors.BotUserAccessError "slack_sdk.errors.BotUserAccessError")
* [SlackApiError](#slack_sdk.errors.SlackApiError "slack_sdk.errors.SlackApiError")
* [SlackClientConfigurationError](#slack_sdk.errors.SlackClientConfigurationError "slack_sdk.errors.SlackClientConfigurationError")
* [SlackClientNotConnectedError](#slack_sdk.errors.SlackClientNotConnectedError "slack_sdk.errors.SlackClientNotConnectedError")
* [SlackObjectFormationError](#slack_sdk.errors.SlackObjectFormationError "slack_sdk.errors.SlackObjectFormationError")
* [SlackRequestError](#slack_sdk.errors.SlackRequestError "slack_sdk.errors.SlackRequestError")
* [SlackTokenRotationError](#slack_sdk.errors.SlackTokenRotationError "slack_sdk.errors.SlackTokenRotationError")

`class SlackClientNotConnectedError (*args, **kwargs)`

Expand source code

```text
class SlackClientNotConnectedError(SlackClientError):
    """Error raised when attempting to send messages over the websocket when the
    connection is closed."""
```

Error raised when attempting to send messages over the websocket when the connection is closed.

### Ancestors (5)

* [SlackClientError](#slack_sdk.errors.SlackClientError "slack_sdk.errors.SlackClientError")
* builtins.Exception
* builtins.BaseException

`class SlackObjectFormationError (*args, **kwargs)`

Expand source code

```text
class SlackObjectFormationError(SlackClientError):
    """Error raised when a constructed object is not valid/malformed"""
```

Error raised when a constructed object is not valid/malformed

### Ancestors (6)

* [SlackClientError](#slack_sdk.errors.SlackClientError "slack_sdk.errors.SlackClientError")
* builtins.Exception
* builtins.BaseException

`class SlackRequestError (*args, **kwargs)`

Expand source code

```text
class SlackRequestError(SlackClientError):
    """Error raised when there's a problem with the request that's being submitted."""
```

Error raised when there's a problem with the request that's being submitted.

### Ancestors (7)

* [SlackClientError](#slack_sdk.errors.SlackClientError "slack_sdk.errors.SlackClientError")
* builtins.Exception
* builtins.BaseException

`class SlackTokenRotationError (api_error: [SlackApiError](#slack_sdk.errors.SlackApiError "slack_sdk.errors.SlackApiError"))`

Expand source code

```typescript
class SlackTokenRotationError(SlackClientError):
    """Error raised when the oauth.v2.access call for token rotation fails"""

    api_error: SlackApiError

    def __init__(self, api_error: SlackApiError):
        self.api_error = api_error
```

Error raised when the oauth.v2.access call for token rotation fails

### Ancestors (8)

* [SlackClientError](#slack_sdk.errors.SlackClientError "slack_sdk.errors.SlackClientError")
* builtins.Exception
* builtins.BaseException

### Class variables

`var api_error : [SlackApiError](#slack_sdk.errors.SlackApiError "slack_sdk.errors.SlackApiError")`

The type of the None singleton.
