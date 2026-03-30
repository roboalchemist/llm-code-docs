# Source: https://docs.logrocket.com/reference/expo-initialize-sdk.md

# Initializing The SDK

### Expo Web

For Expo web deployments, the LogRocket Javascript Web SDK must be used. See our [web initialization](https://docs.logrocket.com/reference/init) and follow Web SDK guides from there. Note that the Web SDK can only be imported in Web builds of your app.

### Expo Mobile

Initializing the SDK is as simple as importing the package and running the initialization method.  A good place to initialize the SDK is in a `useEffect` hook in your top-level Application component.

Replace `<APP_SLUG>` with your LogRocket application slug, located in our [dashboard's quick start guides](https://app.logrocket.com/r/settings/setup).

```typescript
import React, { useEffect } from 'react';
import LogRocket from '@logrocket/react-native';

const App = () => {
  useEffect(() => {
    LogRocket.init('<APP_SLUG>');
  }, []);
  // Your application entry
};
```