# Source: https://developers.make.com/custom-apps-documentation/component-blocks/api/handling-responses/error.md

# Error

**Required**: yes\
**Default**: Make shows a generic message

The `error` directive specifies the error type and the error message to show the user.

You can specify different error messages based on different status codes. The error object has the following attributes:

<table><thead><tr><th width="163">Property</th><th width="172.33333333333331">Type</th><th>Description</th></tr></thead><tbody><tr><td>message</td><td>IML string</td><td>An expression that parses an error message from the response body.</td></tr><tr><td>type</td><td>IML string</td><td>An expression that specifies the error type.</td></tr><tr><td>&#x3C;status code></td><td>Error specification</td><td>An object that customizes the error message and type based on the status code.</td></tr></tbody></table>

See [error handling](https://developers.make.com/custom-apps-documentation/app-components/base/error-handling) for more details.

## Properties

### message

**Required**: yes

The `error.message` directive specifies the message that the error will contain. It can be a statically specified string, or it can point to a message in a response body or header.

### type

**Required**: no\
**Default**: RuntimeError

The `error.type` directive specifies a type of error message. Different error types are handled differently by Make. The default error type is `RuntimeError`. See [error handling](https://developers.make.com/custom-apps-documentation/app-components/base/error-handling) for more details.

### \<status-code>

**Required**: no

You can specify custom errors for different status codes by specifying the status code as the key in the `error` directive object and using the same error specification as a value.
