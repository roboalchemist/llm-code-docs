# Source: https://docs.logrocket.com/reference/react-native-redaction-tags.md

# Sanitize View Data

Redact elements by ID

The React Native SDK is a light-weight interface into our native Android and iOS SDKs. For more information on Visual Capture & Replay please see the documentation for the respective platform:

* [Native Android SDK](https://docs.logrocket.com/docs/android#visual-capture--replay)
* [Native iOS SDK](https://docs.logrocket.com/docs/ios#visual-capture--replay)

# Redacting view elements

React Native view elements can be redacted from session replay for a variety of reasons, e.g., to protect private user information. Redacted elements are not transmitted during session capture and do not leave the client device. The LogRocket React Native SDK provides a variety of methods to redact content.

## Use the provided redaction components

The LogRocket React Native SDK provides two helper components with which wrapped child components can be redacted. Using these components is the **recommended approach to redaction** as their implementation will be updated to accommodate any future native platform changes.

### Using the `<LRRedact>` component

A simple way to redact a section of your application without changing the attributes of the target component is to wrap the element with the `<LRRedact>` component.

Note: this component is available as of release 1.12.4.

```jsx JavaScript
import { LRRedact } from '@logrocket/react-native';

<View>
  <Text>Captured part of the screen.</Text>
  <LRRedact>
    <Text>Redacted part of the screen.</Text>
  </LRRedact>
</View>
```

### Using the `<LRNativeIDRedact>` component

On iOS, the SDK also provides the `<LRNativeIDRedact>` component. This component differs from `<LRRedact>` in that it applies the default redaction tag to the `nativeID` attribute of the component, as opposed to `testID`. This component is preferable in circumstances where it is important that the backing native component's accessibility identifier is not affected.

Note: this component is available as of release 1.44.0

## Manually redact view elements

In the event that introducing a wrapping redaction component is undesirable, your existing React Native views can be manually marked for redaction via the view component's props, either by hand or via the `LRRedactProps` helper.

### Using the `LRRedactProps` helper

The`LRRedactProps` helper function can be used in conjunction with the spread operator to generate the appropriate component props based on the native platform.

Note: this component is available as of release 1.12.4.

```jsx JavaScript
import { LRRedactProps } from '@logrocket/react-native';

<View>
  <Text>Captured part of the screen.</Text>
</View>
<View {...LRRedactProps()}>
  <Text>Redacted part of the screen.</Text>
</View>
```

#### `useNativeID` argument

If you'd rather use the `nativeID` property to mark a component for redaction when your app is executing on iOS, you can pass `true` for the the `useNativeID` argument when calling the `LRRedactProps` helper function.

> **:information\_source:** Important usage information
>
> 1. `LRRedactProps` also takes a `redactionTag` string argument, so you'll have to pass either `undefined` or `lr-hide` if you want to use `LRRedactProps` with the default redaction tag *and* `nativeID` property assignment on iOS.
> 2. [`nativeID`](https://reactnative.dev/docs/view#nativeid) is only assignable on [`View`](https://reactnative.dev/docs/view) components. In order to redact a `Button` or other component that is not a subclass of `View`, you will need to wrap it in an `<LRRedact>` component, rather than just applying `LRRedactProps()` to it.

Note: This argument is available as of release 1.44.0

```jsx JavaScript
import { LRRedactProps } from '@logrocket/react-native';

<View>
  <Text>Captured part of the screen.</Text>
</View>
<View {...LRRedactProps(undefined, true)}>
  <Text>Part of the screen redacted via the nativeID property on iOS.</Text>
</View>
```

### Using `testID` to redact views

Apply a `testID` attribute as a prop to any view element you wish to redact from view capture. On iOS, an additional attribute `accessible={false}` is also required for redaction. This property can be applied conditionally by examining`reactNative.Platform.OS`.

For developers on versions before 1.12.4 we recommend introducing a helper function to properly set the attributes.

```jsx JavaScript
import { Platform } from 'react-native';

const LRRedactProps = (redactionTag = 'lr-hide') => (
  Platform.OS === 'ios'
    ? {
      testID: redactionTag,
      accessible: false,
    }
    : { testID: redactionTag }
);

<View {...LRRedactProps()}>
  This view will be hidden using the default lr-hide matcher.
</View>
<View {...LRRedactProps()}>
  This view will be hidden using the custom private matcher.
</View>
<View {...LRRedactProps("something-else")}>
  This view will be captured.
</View>
```

> 🚧 React Native New Architecture changes
>
> Apps transitioning to the React Native New Architecture must supply an additional prop to the target component to ensure redaction functions properly. Specifying this prop prevents React Native from flattening the resulting native view, which is known to interfere with redaction behavior.
>
> ```jsx JavaScript
> <View
>   testID="lr-hide"
>   collapsable={false} // Add this prop!
> >
>   <Text>Redacted content</Text>
> </View>
> ```
>
> We recommend using the provided [redaction wrapper components](https://docs.logrocket.com/reference/react-native-redaction-tags#use-the-provided-redaction-components) , which have been updated for React Native New Architecture compatibility.

### Configuring `redactionTags`

If the element you wish to redact already has a `testID` defined, you can configure test ids other than `lr-hide` to be redacted. This is configured by providing a string array when initializing the SDK as follows:

```jsx JavaScript
LogRocket.init('APP_SLUG', {
  redactionTags: ['private', 'myAddressForm'],
});
```

## Prevent touch event capture on redacted views

In order to prevent touches on redacted views from appearing in session replay, for example, in situations where your app provides a number PIN pad to users, supply the following configuration at SDK initialization.

```jsx captureRedactedViewTouches
LogRocket.init('APP_SLUG', {
  captureRedactedViewTouches: false,
});
```

## Pause View Capture

To completely disable the view capture system call `LogRocket.pauseViewCapture()`. If a capture is already in progress it will not be stopped, but no new view captures will be started until `LogRocket.unpauseViewCapture()` is called.

## Allowlisting

Child elements of redacted view elements can be excluded from redaction, or allowed, using the provided helper components or manually.

### Using the `<LRAllow>` component

The simplest way to permit the capture of view elements which would otherwise be ignored due to a redacted parent element is to wrap the target components with the provided `<LRAllow>` component.

Note: this component is available as of release 1.19.0

```jsx JavaScript
import { LRAllow, LRRedact } from '@logrocket/react-native';

<LRRedact>
  <View>
    <Text>Redacted part of the screen.</Text>
    <LRAllow>
      <Text>Captured part of the screen.</Text>
    </LRAllow>
  </View>
</LRRedact>
```

### Using the `<LRNativeIDAllow>` component

Another way to allow a section of your application without changing the attributes of the allow target is to use the `<LRNativeIDAllow>` component. This component differs from `<LRAllow>` in that it assigns the `nativeID` attribute to the default allow tag value in iOS applications, rather than assigning the `testID` and `accessible` attributes on the component.

Note: this component is available as of release 1.44.0

### Using the `LRAllowProps` helper

In cases where you do not want to introduce a wrapping component, it is recommended to use the `LRAllowProps` helper function in conjunction with the spread operator to generate the appropriate component props based on the executing native platform.

Note: this component is available as of release 1.19.0

```jsx JavaScript
import { LRAllowProps, LRRedact } from '@logrocket/react-native';

<LRRedact>
  <Text>Redacted part of the screen.</Text>
  <View {...LRAllowProps()}>
    <Text>Captured part of the screen.</Text>
  </View>
</LRRedact>
```

#### `useNativeID` argument

If you'd rather use the `nativeID` property to mark a component as allowed when your app is executing on iOS, you can pass `true` for the the `useNativeID` argument when calling the `LRAllowProps` helper function.

> **:information\_source:** Important usage information
>
> 1. `LRAllowProps` also takes a `allowTag` string argument, so you'll have to pass either `undefined` or `lr-show` if you want to use `LRAllowProps` with the default allow tag *and* `nativeID` property assignment on iOS.
> 2. [`nativeID`](https://reactnative.dev/docs/view#nativeid)  is only assignable on [`View`](https://reactnative.dev/docs/view) components. In order to allow a `Button` or other component that is not a subclass of `View`, you will need to wrap it in an `<LRAllow>` component, rather than just applying `LRAllowProps()` to it.

Note: This argument is available as of release 1.44.0

```jsx JavaScript
import { LRAllowProps, LRRedact } from '@logrocket/react-native';

<LRRedact>
  <Text>Redacted part of the screen.</Text>
  <View {...LRAllowProps(undefined, true)}>
    <Text>Part of the screen allowed via nativeID property on iOS</Text>
  </View>
</LRRedact>
```

### Using `testID` to allow views

An appropriate `testID` attribute can be applied to any descendants of redacted view elements to mark them for capture. By default, `lr-show` will mark an element for capture when supplied as the `testID` prop. On iOS, an additional attribute `accessible={true}` is also required to permit capture. This property can be applied conditionally based on the value of `reactNative.Platform.OS`.

### Configuring `allowTags`

If the element you wish to allow already has a `testID` defined, you can configure test ids other than `lr-show` to be allowed. This is configured by providing a string array when initializing the SDK as follows:

```javascript
LogRocket.init('APP_SLUG', {
  allowTags: ['public', 'myHeader'],
});
```