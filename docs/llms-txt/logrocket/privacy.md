# Source: https://docs.logrocket.com/docs/privacy.md

# Privacy

Hiding sensitive user information such as passwords, credit cards, and personal data.

We take privacy seriously and understand that there is a tradeoff between having enough information to solve a bug and end-user privacy.

We designed our SDK to allow developers to determine what information to hide from LogRocket reports. We are constantly working to enhance these features, so [let us know](mailto:support@logrocket.com) if there is a privacy feature that you need which we do not support.

## Exclude Data in Videos

Excluded data is **never** sent to LogRocket servers. Once an element is excluded, it cannot be included again on that page.

Data can be excluded using a data attribute of `data-private` any element:

```html Using the data-private attribute
<div data-private>
  This data will <strong>not</strong> be recorded.
</div>
```

### Form inputs

Add the  `data-private` attribute to any `input` or `textarea` DOM element to prevent recording its input. Password fields are never recorded.

Remember to also exclude this data from your network requests.

### Input redaction types

To change the behavior of a private `input` or `textarea` field you can specify a redaction type:

```html Obfuscating text within input elements
<textarea data-private="lipsum"></textarea>
```

`redact`\
This is the default redaction type and equivalent to not having the `data-private` attribute set.  When an input is set to `redact` the user input will not be recorded.

`lipsum`\
When the `data-private` attribute is set to `lipsum`, it will replay as if the user was typing Lorem Ipsum text instead of the actual characters. This option is appropriate for input fields where it is important to know whether the user was actively typing and where exposing the length of the input text does not pose a security risk.

### DOM elements

Add the `data-private` attribute to any DOM element that you wish to obscure from LogRocket. All DOM elements which are children of a hidden/private DOM element will not be recorded.

### Automatically sanitize all text, inputs, and images

The LogRocket SDK can automatically sanitize all text, inputs, and images from your session recordings.

![](https://files.readme.io/36421fd-Screen_Shot_2020-01-21_at_3.12.31_PM.png "Screen Shot 2020-01-21 at 3.12.31 PM.png")

See the [dom API documentation](https://docs.logrocket.com/reference/dom) for details.

# Exclude network data

The LogRocket SDK can exclude request bodies, response bodies, headers, URLs, and anything else sensitive from your session recordings.

See the [network API documentation](https://docs.logrocket.com/reference/network) for details.

# Exclude Redux state

Using a state sanitizer you can drop or redact individual keys or full subtrees of your frontend state store.

See [reduxMiddleware() API documentation](https://docs.logrocket.com/v3.0/reference/redux-middleware-1).

# Exclude Redux actions

Using the reduce middleware, you can drop or redact sensitive state transitions.

See [reduxMiddleware() API documentation](https://docs.logrocket.com/v3.0/reference/redux-middleware-1).

> 👍 Self-Hosted LogRocket
>
> If you prefer to host LogRocket in your own private cloud for privacy reasons, contact us at [support@logrocket.com](mailto:support@logrocket.com)