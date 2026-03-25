# Source: https://docs.logrocket.com/reference/accessing-private-assets.md

# Access Private Assets

Expose assets for recordings on private domains

## Accessing Private Assets

#### `baseHref` - String

##### optional (default - `null`)

If clients access your app on a private domain, or the app is built with Ionic, Capacitor, or Cordova, then LogRocket won't be able to fetch CSS/image assets for playback (see [Testing on localhost/VPN](https://docs.logrocket.com/docs/local-development) for more information). To get around this limitation, you can specify a `baseHref` from which LogRocket will fetch assets. Make sure that this domain is publicly accessible, and that it contains the same assets and folder structure as the private domain:

```javascript
LogRocket.init(YOUR_APP_ID, {
  dom: {
    baseHref: 'https://assets.example.com/',
  },
});
```