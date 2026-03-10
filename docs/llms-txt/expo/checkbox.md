# Source: https://docs.expo.dev/versions/latest/sdk/checkbox

---
title: Checkbox
description: A universal React component that provides basic checkbox functionality.
sourceCodeUrl: 'https://github.com/expo/expo/tree/main/packages/expo-checkbox'
packageName: 'expo-checkbox'
platforms: ['android', 'ios', 'tvos', 'web', 'expo-go']
---

# Expo Checkbox

A universal React component that provides basic checkbox functionality.
Android, iOS, tvOS, Web, Included in Expo Go

`expo-checkbox` provides a basic `boolean` input element for all platforms.

## Installation

```sh
npx expo install expo-checkbox
```

## Usage

```tsx
import { Checkbox } from 'expo-checkbox';
import { useState } from 'react';
import { StyleSheet, Text, View } from 'react-native';

export default function App() {
  const [isChecked, setChecked] = useState(false);

  return (
    <View style={styles.container}>
      <View style={styles.section}>
        <Checkbox style={styles.checkbox} value={isChecked} onValueChange={setChecked} />
        <Text style={styles.paragraph}>Normal checkbox</Text>
      </View>
      <View style={styles.section}>
        <Checkbox
          style={styles.checkbox}
          value={isChecked}
          onValueChange={setChecked}
          color={isChecked ? '#4630EB' : undefined}
        />
        <Text style={styles.paragraph}>Custom colored checkbox</Text>
      </View>
      <View style={styles.section}>
        <Checkbox style={styles.checkbox} disabled value={isChecked} onValueChange={setChecked} />
        <Text style={styles.paragraph}>Disabled checkbox</Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    marginHorizontal: 16,
    marginVertical: 32,
  },
  section: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  paragraph: {
    fontSize: 15,
  },
  checkbox: {
    margin: 8,
  },
});
```

An example of how `expo-checkbox` appears on Android and iOS is shown below:

## API

```js
import { Checkbox } from 'expo-checkbox';
```

## Component

### `Checkbox`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[CheckboxProps](#checkboxprops)\>

CheckboxProps

### `color`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

The tint or color of the checkbox. This overrides the disabled opaque style.

### `disabled`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

If the checkbox is disabled, it becomes opaque and uncheckable.

### `onChange`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: (event: NativeSyntheticEvent<[CheckboxEvent](#checkboxevent)\> | [SyntheticEvent](https://react.dev/reference/react-dom/components/common#react-event-object)<[HTMLInputElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement), [CheckboxEvent](#checkboxevent)\>) => void

Callback that is invoked when the user presses the checkbox.

event: NativeSyntheticEvent<[CheckboxEvent](#checkboxevent)\> | [SyntheticEvent](https://react.dev/reference/react-dom/components/common#react-event-object)<[HTMLInputElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement), [CheckboxEvent](#checkboxevent)\>

A native event containing the checkbox change.

### `onValueChange`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `(value: boolean) => void`

Callback that is invoked when the user presses the checkbox.

`value: boolean`

A boolean indicating the new checked state of the checkbox.

### `value`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean` • Default: `false`

Value indicating if the checkbox should be rendered as checked or not.

#### Inherited Props

-   [ViewProps](https://reactnative.dev/docs/view#props)

## Types

### `CheckboxEvent`

Supported platforms: Android, iOS, tvOS, Web.

| Property | Type | Description |
| --- | --- | --- |
| target | `any` | On native platforms, a `NodeHandle` for the element on which the event has occurred. On web, a DOM node on which the event has occurred. |
| value | `boolean` | A boolean representing checkbox current value. |
