# Source: https://docs.logrocket.com/reference/init.md

# Initialize SDK

Initialize LogRocket and start recording sessions

Call `init()` with your appID to configure and start LogRocket. You can find your appID on [https://app.logrocket.com](https://app.logrocket.com) under Settings > Project Setup.

```javascript
LogRocket.init('YOUR_APP_ID');
```

<Callout icon="🚧" theme="warn">
  Call `init` as early on the page as possible. Some recording data may be lost if it is called too late.
</Callout>

`init()` can also be called conditionally, if necessary:

```javascript
if (condition === true) {
  LogRocket.init([...]);
}
```

This function takes an optional second parameter that can be used to affect recording behavior. The options are listed in detail in their corresponding pages in the JavaScript Web SDK section.

<br />