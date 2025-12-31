# Source: https://reactnative.dev/docs/usecolorscheme.md

# useColorScheme

tsx

```
import {useColorScheme} from 'react-native';
```

The `useColorScheme` React hook provides and subscribes to color scheme updates from the [`Appearance`](/docs/appearance.md) module. The return value indicates the current user preferred color scheme. The value may be updated later, either through direct user action (e.g. theme selection in device settings) or on a schedule (e.g. light and dark themes that follow the day/night cycle).

### Supported color schemes[​](#supported-color-schemes "Direct link to Supported color schemes")

* `"light"`: The user prefers a light color theme.
* `"dark"`: The user prefers a dark color theme.
* `null`: The user has not indicated a preferred color theme.

***

## Example[​](#example "Direct link to Example")

You can find a complete example that demonstrates the use of this hook alongside a React context to add support for light and dark themes to your application in [`AppearanceExample.js`](https://github.com/facebook/react-native/blob/main/packages/rn-tester/js/examples/Appearance/AppearanceExample.js).
