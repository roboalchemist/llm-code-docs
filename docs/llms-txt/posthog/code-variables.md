# Source: https://posthog.com/docs/error-tracking/code-variables.md

# Code variables - Docs

PostHog SDK can automatically capture the state of local variables when an exception occurs, giving you a debugger-like view of your application at the time of the error.

When enabled, PostHog captures the values of variables from each frame in the stack trace, eliminating the need to reproduce errors locally just to understand what values were present when the exception was thrown.

![Error tracking code variables](https://res.cloudinary.com/dmukukwp6/image/upload/pasted_image_2025_11_13_T08_33_54_608_Z_019b9c4f02.png)![Error tracking code variables](https://res.cloudinary.com/dmukukwp6/image/upload/pasted_image_2025_11_13_T08_25_03_421_Z_07ba9b7242.png)

The variables account\_balance, email, user\_id, and username and their values

## How it works

1.  **Variable extraction**: Local variables are extracted from each frame in the stack trace
2.  **Scope filtering**: Only frames from your application code (not third-party libraries) are included
3.  **Type mapping**: Simple types like strings, numbers, and booleans are directly mapped. Complex objects are JSON-serialized when possible. Otherwise their type name is shown
4.  **Truncation**: Long values are automatically truncated to keep event sizes manageable
5.  **Security**: Sensitive variable names are masked or excluded based on configurable patterns

The captured variables appear alongside the stack trace in PostHog, allowing you to inspect the exact state of your application at the moment of the error.

### Masking

Masking replaces the values of sensitive variables with a redacted placeholder while still showing the variable name. This is useful for variables like `password`, `api_key`, or `access_token` where you want to know the variable exists in the stack trace, but don't want to expose its actual value.

![Error tracking code variables masking](https://res.cloudinary.com/dmukukwp6/image/upload/pasted_image_2025_11_13_T08_28_21_412_Z_a69c250ada.png)![Error tracking code variables masking](https://res.cloudinary.com/dmukukwp6/image/upload/pasted_image_2025_11_13_T08_28_46_274_Z_b5813ee9b8.png)

The secret's value is masked

### Ignoring

Ignoring completely excludes variables from being captured. This is useful for internal framework variables, temporary data, or variables that don't provide debugging value. Ignored variables won't appear in the captured stack trace at all.

### SDK support

Each SDK provides platform-specific configuration options. See the platform-specific documentation for details:

-   [Python](/docs/error-tracking/code-variables/python.md)

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better