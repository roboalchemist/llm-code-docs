# Source: https://reactnative.dev/docs/textinput.md

# TextInput

A foundational component for inputting text into the app via a keyboard. Props provide configurability for several features, such as auto-correction, auto-capitalization, placeholder text, and different keyboard types, such as a numeric keypad.

The most basic use case is to plop down a `TextInput` and subscribe to the `onChangeText` events to read the user input. There are also other events, such as `onSubmitEditing` and `onFocus` that can be subscribed to. A minimal example:

Two methods exposed via the native element are `.focus()` and `.blur()` that will focus or blur the TextInput programmatically.

Note that some props are only available with `multiline={true/false}`. Additionally, border styles that apply to only one side of the element (e.g., `borderBottomColor`, `borderLeftWidth`, etc.) will not be applied if `multiline=true`. To achieve the same effect, you can wrap your `TextInput` in a `View`:

`TextInput` has a border at the bottom of its view by default. This border has its padding set by the background image provided by the system, and it cannot be changed. Solutions to avoid this are to either not set height explicitly, in which case the system will take care of displaying the border in the correct position, or to not display the border by setting `underlineColorAndroid` to transparent.

Note that on Android performing text selection in an input can change the app's activity `windowSoftInputMode` param to `adjustResize`. This may cause issues with components that have position: 'absolute' while the keyboard is active. To avoid this behavior either specify `windowSoftInputMode` in AndroidManifest.xml ( <https://developer.android.com/guide/topics/manifest/activity-element.html> ) or control this param programmatically with native code.

***

# Reference

## Props[​](#props "Direct link to Props")

### [View Props](/docs/view.md#props)[​](#view-props "Direct link to view-props")

Inherits [View Props](/docs/view.md#props).

***

### `allowFontScaling`[​](#allowfontscaling "Direct link to allowfontscaling")

Specifies whether fonts should scale to respect Text Size accessibility settings. The default is `true`.

| Type |
| ---- |
| bool |

***

### `autoCapitalize`[​](#autocapitalize "Direct link to autocapitalize")

Tells `TextInput` to automatically capitalize certain characters. This property is not supported by some keyboard types such as `name-phone-pad`.

* `characters`: all characters.
* `words`: first letter of each word.
* `sentences`: first letter of each sentence (*default*).
* `none`: don't auto capitalize anything.

| Type                                             |
| ------------------------------------------------ |
| enum('none', 'sentences', 'words', 'characters') |

***

### `autoComplete`[​](#autocomplete "Direct link to autocomplete")

Specifies autocomplete hints for the system, so it can provide autofill. On Android, the system will always attempt to offer autofill by using heuristics to identify the type of content. To disable autocomplete, set `autoComplete` to `off`.

The following values work across platforms:

* `additional-name`
* `address-line1`
* `address-line2`
* `birthdate-day` (iOS 17+)
* `birthdate-full` (iOS 17+)
* `birthdate-month` (iOS 17+)
* `birthdate-year` (iOS 17+)
* `cc-csc` (iOS 17+)
* `cc-exp` (iOS 17+)
* `cc-exp-day` (iOS 17+)
* `cc-exp-month` (iOS 17+)
* `cc-exp-year` (iOS 17+)
* `cc-number`
* `country`
* `current-password`
* `email`
* `family-name`
* `given-name`
* `honorific-prefix`
* `honorific-suffix`
* `name`
* `new-password`
* `off`
* `one-time-code`
* `postal-code`
* `street-address`
* `tel`
* `username`

iOS

The following values work on iOS only:

* `cc-family-name` (iOS 17+)
* `cc-given-name` (iOS 17+)
* `cc-middle-name` (iOS 17+)
* `cc-name` (iOS 17+)
* `cc-type` (iOS 17+)
* `nickname`
* `organization`
* `organization-title`
* `url`

Android

The following values work on Android only:

* `gender`
* `name-family`
* `name-given`
* `name-middle`
* `name-middle-initial`
* `name-prefix`
* `name-suffix`
* `password`
* `password-new`
* `postal-address`
* `postal-address-country`
* `postal-address-extended`
* `postal-address-extended-postal-code`
* `postal-address-locality`
* `postal-address-region`
* `sms-otp`
* `tel-country-code`
* `tel-device`
* `tel-national`
* `username-new`

| Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| enum('additional-name', 'address-line1', 'address-line2', 'birthdate-day', 'birthdate-full', 'birthdate-month', 'birthdate-year', 'cc-csc', 'cc-exp', 'cc-exp-day', 'cc-exp-month', 'cc-exp-year', 'cc-number', 'country', 'current-password', 'email', 'family-name', 'given-name', 'honorific-prefix', 'honorific-suffix', 'name', 'new-password', 'off', 'one-time-code', 'postal-code', 'street-address', 'tel', 'username', 'cc-family-name', 'cc-given-name', 'cc-middle-name', 'cc-name', 'cc-type', 'nickname', 'organization', 'organization-title', 'url', 'gender', 'name-family', 'name-given', 'name-middle', 'name-middle-initial', 'name-prefix', 'name-suffix', 'password', 'password-new', 'postal-address', 'postal-address-country', 'postal-address-extended', 'postal-address-extended-postal-code', 'postal-address-locality', 'postal-address-region', 'sms-otp', 'tel-country-code', 'tel-device', 'tel-national', 'username-new') |

***

### `autoCorrect`[​](#autocorrect "Direct link to autocorrect")

If `false`, disables auto-correct. The default value is `true`.

| Type |
| ---- |
| bool |

***

### `autoFocus`[​](#autofocus "Direct link to autofocus")

If `true`, focuses the input. The default value is `false`.

| Type |
| ---- |
| bool |

***

### 🗑️ `blurOnSubmit`[​](#️-bluronsubmit "Direct link to ️-bluronsubmit")

Deprecated

Note that `submitBehavior` now takes the place of `blurOnSubmit` and will override any behavior defined by `blurOnSubmit`. See [submitBehavior](/docs/textinput.md#submitbehavior).

If `true`, the text field will blur when submitted. The default value is true for single-line fields and false for multiline fields. Note that for multiline fields, setting `blurOnSubmit` to `true` means that pressing return will blur the field and trigger the `onSubmitEditing` event instead of inserting a newline into the field.

| Type |
| ---- |
| bool |

***

### `caretHidden`[​](#carethidden "Direct link to carethidden")

If `true`, caret is hidden. The default value is `false`.

| Type |
| ---- |
| bool |

***

### `clearButtonMode`iOS[​](#clearbuttonmode-ios "Direct link to clearbuttonmode-ios")

When the clear button should appear on the right side of the text view. This property is supported only for single-line TextInput component. The default value is `never`.

| Type                                                       |
| ---------------------------------------------------------- |
| enum('never', 'while-editing', 'unless-editing', 'always') |

***

### `clearTextOnFocus`iOS[​](#cleartextonfocus-ios "Direct link to cleartextonfocus-ios")

If `true`, clears the text field automatically when editing begins.

| Type |
| ---- |
| bool |

***

### `contextMenuHidden`[​](#contextmenuhidden "Direct link to contextmenuhidden")

If `true`, context menu is hidden. The default value is `false`.

| Type |
| ---- |
| bool |

***

### `dataDetectorTypes`iOS[​](#datadetectortypes-ios "Direct link to datadetectortypes-ios")

Determines the types of data converted to clickable URLs in the text input. Only valid if `multiline={true}` and `editable={false}`. By default no data types are detected.

You can provide one type or an array of many types.

Possible values for `dataDetectorTypes` are:

* `'phoneNumber'`
* `'link'`
* `'address'`
* `'calendarEvent'`
* `'none'`
* `'all'`

| Type                                                                                                                                                     |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| enum('phoneNumber', 'link', 'address', 'calendarEvent', 'none', 'all'), ,array of enum('phoneNumber', 'link', 'address', 'calendarEvent', 'none', 'all') |

***

### `defaultValue`[​](#defaultvalue "Direct link to defaultvalue")

Provides an initial value that will change when the user starts typing. Useful for use-cases where you do not want to deal with listening to events and updating the value prop to keep the controlled state in sync.

| Type   |
| ------ |
| string |

***

### `disableKeyboardShortcuts`iOS[​](#disablekeyboardshortcuts-ios "Direct link to disablekeyboardshortcuts-ios")

If `true`, the keyboard shortcuts (undo/redo and copy buttons) are disabled.

| Type | Default |
| ---- | ------- |
| bool | `false` |

***

### `cursorColor`Android[​](#cursorcolor-android "Direct link to cursorcolor-android")

When provided it will set the color of the cursor (or "caret") in the component. Unlike the behavior of `selectionColor` the cursor color will be set independently from the color of the text selection box.

| Type                     |
| ------------------------ |
| [color](/docs/colors.md) |

***

### `disableFullscreenUI`Android[​](#disablefullscreenui-android "Direct link to disablefullscreenui-android")

When `false`, if there is a small amount of space available around a text input (e.g. landscape orientation on a phone), the OS may choose to have the user edit the text inside of a full screen text input mode. When `true`, this feature is disabled and users will always edit the text directly inside of the text input. Defaults to `false`.

| Type |
| ---- |
| bool |

***

### `editable`[​](#editable "Direct link to editable")

If `false`, text is not editable. The default value is `true`.

| Type |
| ---- |
| bool |

***

### `enablesReturnKeyAutomatically`iOS[​](#enablesreturnkeyautomatically-ios "Direct link to enablesreturnkeyautomatically-ios")

If `true`, the keyboard disables the return key when there is no text and automatically enables it when there is text. The default value is `false`.

| Type |
| ---- |
| bool |

***

### `enterKeyHint`[​](#enterkeyhint "Direct link to enterkeyhint")

Determines what text should be shown to the return key. Has precedence over the `returnKeyType` prop.

The following values work across platforms:

* `done`
* `next`
* `search`
* `send`
* `go`

*Android Only*

The following values work on Android only:

* `previous`

*iOS Only*

The following values work on iOS only:

* `enter`

| Type                                                              |
| ----------------------------------------------------------------- |
| enum('enter', 'done', 'next', 'previous', 'search', 'send', 'go') |

***

### `importantForAutofill`Android[​](#importantforautofill-android "Direct link to importantforautofill-android")

Tells the operating system whether the individual fields in your app should be included in a view structure for autofill purposes on Android API Level 26+. Possible values are `auto`, `no`, `noExcludeDescendants`, `yes`, and `yesExcludeDescendants`. The default value is `auto`.

* `auto`: Let the Android System use its heuristics to determine if the view is important for autofill.
* `no`: This view isn't important for autofill.
* `noExcludeDescendants`: This view and its children aren't important for autofill.
* `yes`: This view is important for autofill.
* `yesExcludeDescendants`: This view is important for autofill, but its children aren't important for autofill.

| Type                                                                       |
| -------------------------------------------------------------------------- |
| enum('auto', 'no', 'noExcludeDescendants', 'yes', 'yesExcludeDescendants') |

***

### `inlineImageLeft`Android[​](#inlineimageleft-android "Direct link to inlineimageleft-android")

If defined, the provided image resource will be rendered on the left. The image resource must be inside `/android/app/src/main/res/drawable` and referenced like

```
<TextInput
 inlineImageLeft='search_icon'
/>
```

| Type   |
| ------ |
| string |

***

### `inlineImagePadding`Android[​](#inlineimagepadding-android "Direct link to inlineimagepadding-android")

Padding between the inline image, if any, and the text input itself.

| Type   |
| ------ |
| number |

***

### `inputAccessoryViewID`iOS[​](#inputaccessoryviewid-ios "Direct link to inputaccessoryviewid-ios")

An optional identifier which links a custom [InputAccessoryView](/docs/inputaccessoryview.md) to this text input. The InputAccessoryView is rendered above the keyboard when this text input is focused.

| Type   |
| ------ |
| string |

***

### `inputAccessoryViewButtonLabel`iOS[​](#inputaccessoryviewbuttonlabel-ios "Direct link to inputaccessoryviewbuttonlabel-ios")

An optional label that overrides the default [InputAccessoryView](/docs/inputaccessoryview.md) button label.

By default, the default button label is not localized. Use this property to provide a localized version.

| Type   |
| ------ |
| string |

***

### `inputMode`[​](#inputmode "Direct link to inputmode")

Works like the `inputmode` attribute in HTML, it determines which keyboard to open, e.g. `numeric` and has precedence over `keyboardType`.

Support the following values:

* `none`
* `text`
* `decimal`
* `numeric`
* `tel`
* `search`
* `email`
* `url`

| Type                                                                        |
| --------------------------------------------------------------------------- |
| enum('decimal', 'email', 'none', 'numeric', 'search', 'tel', 'text', 'url') |

***

### `keyboardAppearance`iOS[​](#keyboardappearance-ios "Direct link to keyboardappearance-ios")

Determines the color of the keyboard.

| Type                             |
| -------------------------------- |
| enum('default', 'light', 'dark') |

***

### `keyboardType`[​](#keyboardtype "Direct link to keyboardtype")

Determines which keyboard to open, e.g.`numeric`.

See screenshots of all the types [here](https://davidl.fr/blog/keyboard-react-native-ios-android#all-react-native-keyboard-type-examples-i-os-on-the-left-android-on-the-right).

The following values work across platforms:

* `default`
* `number-pad`
* `decimal-pad`
* `numeric`
* `email-address`
* `phone-pad`
* `url`

*iOS Only*

The following values work on iOS only:

* `ascii-capable`
* `numbers-and-punctuation`
* `name-phone-pad`
* `twitter`
* `web-search`

*Android Only*

The following values work on Android only:

* `visible-password`

| Type                                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| enum('default', 'email-address', 'numeric', 'phone-pad', 'ascii-capable', 'numbers-and-punctuation', 'url', 'number-pad', 'name-phone-pad', 'decimal-pad', 'twitter', 'web-search', 'visible-password') |

***

### `lineBreakStrategyIOS`iOS[​](#linebreakstrategyios-ios "Direct link to linebreakstrategyios-ios")

Set line break strategy on iOS 14+. Possible values are `none`, `standard`, `hangul-word` and `push-out`.

| Type                                                        | Default  |
| ----------------------------------------------------------- | -------- |
| enum(`'none'`, `'standard'`, `'hangul-word'`, `'push-out'`) | `'none'` |

***

### `lineBreakModeIOS`iOS[​](#linebreakmodeios-ios "Direct link to linebreakmodeios-ios")

Set line break mode on iOS. Possible values are `wordWrapping`, `char`, `clip`, `head`, `middle` and `tail`.

| Type                                                                       | Default          |
| -------------------------------------------------------------------------- | ---------------- |
| enum(`'wordWrapping'`, `'char'`, `'clip'`, `'head'`, `'middle'`, `'tail'`) | `'wordWrapping'` |

***

### `maxFontSizeMultiplier`[​](#maxfontsizemultiplier "Direct link to maxfontsizemultiplier")

Specifies largest possible scale a font can reach when `allowFontScaling` is enabled. Possible values:

* `null/undefined` (default): inherit from the parent node or the global default (0)
* `0`: no max, ignore parent/global default
* `>= 1`: sets the `maxFontSizeMultiplier` of this node to this value

| Type   |
| ------ |
| number |

***

### `maxLength`[​](#maxlength "Direct link to maxlength")

Limits the maximum number of characters that can be entered. Use this instead of implementing the logic in JS to avoid flicker.

| Type   |
| ------ |
| number |

***

### `multiline`[​](#multiline "Direct link to multiline")

If `true`, the text input can be multiple lines. The default value is `false`.

note

It is important to note that this aligns the text to the top on iOS, and centers it on Android. Use with `textAlignVertical` set to `top` for the same behavior in both platforms.

| Type |
| ---- |
| bool |

***

### `numberOfLines`[​](#numberoflines "Direct link to numberoflines")

note

`numberOfLines` on iOS is only available on the [New Architecture](/architecture/landing-page.md)

Sets the maximum number of lines for a `TextInput`. Use it with multiline set to `true` to be able to fill the lines.

| Type   |
| ------ |
| number |

***

### `onBlur`[​](#onblur "Direct link to onblur")

Callback that is called when the text input is blurred.

note

If you are attempting to access the `text` value from `nativeEvent` keep in mind that the resulting value you get can be `undefined` which can cause unintended errors. If you are trying to find the last value of TextInput, you can use the [`onEndEditing`](/docs/textinput.md#onendediting) event, which is fired upon completion of editing.

| Type                                   |
| -------------------------------------- |
| `({nativeEvent: TargetEvent}) => void` |

***

### `onChange`[​](#onchange "Direct link to onchange")

Callback that is called when the text input's text changes.

| Type                                                  |
| ----------------------------------------------------- |
| (`{nativeEvent: {eventCount, target, text}}`) => void |

***

### `onChangeText`[​](#onchangetext "Direct link to onchangetext")

Callback that is called when the text input's text changes. Changed text is passed as a single string argument to the callback handler.

| Type     |
| -------- |
| function |

***

### `onContentSizeChange`[​](#oncontentsizechange "Direct link to oncontentsizechange")

Callback that is called when the text input's content size changes.

Only called for multiline text inputs.

| Type                                                       |
| ---------------------------------------------------------- |
| (`{nativeEvent: {contentSize: {width, height} }}`) => void |

***

### `onEndEditing`[​](#onendediting "Direct link to onendediting")

Callback that is called when text input ends.

| Type     |
| -------- |
| function |

***

### `onPressIn`[​](#onpressin "Direct link to onpressin")

Callback that is called when a touch is engaged.

| Type                                  |
| ------------------------------------- |
| `({nativeEvent: PressEvent}) => void` |

***

### `onPressOut`[​](#onpressout "Direct link to onpressout")

Callback that is called when a touch is released.

| Type                                  |
| ------------------------------------- |
| `({nativeEvent: PressEvent}) => void` |

***

### `onFocus`[​](#onfocus "Direct link to onfocus")

Callback that is called when the text input is focused.

| Type                                   |
| -------------------------------------- |
| `({nativeEvent: TargetEvent}) => void` |

***

### `onKeyPress`[​](#onkeypress "Direct link to onkeypress")

Callback that is called when a key is pressed. This will be called with object where `keyValue` is `'Enter'` or `'Backspace'` for respective keys and the typed-in character otherwise including `' '` for space. Fires before `onChange` callbacks. Note: on Android only the inputs from soft keyboard are handled, not the hardware keyboard inputs.

| Type                                        |
| ------------------------------------------- |
| (`{nativeEvent: {key: keyValue} }`) => void |

***

### `onLayout`[​](#onlayout "Direct link to onlayout")

Invoked on mount and on layout changes.

| Type                                   |
| -------------------------------------- |
| `({nativeEvent: LayoutEvent}) => void` |

***

### `onScroll`[​](#onscroll "Direct link to onscroll")

Invoked on content scroll. May also contain other properties from `ScrollEvent` but on Android `contentSize` is not provided for performance reasons.

| Type                                                |
| --------------------------------------------------- |
| (`{nativeEvent: {contentOffset: {x, y} }}`) => void |

***

### `onSelectionChange`[​](#onselectionchange "Direct link to onselectionchange")

Callback that is called when the text input selection is changed.

| Type                                                  |
| ----------------------------------------------------- |
| (`{nativeEvent: {selection: {start, end} }}`) => void |

***

### `onSubmitEditing`[​](#onsubmitediting "Direct link to onsubmitediting")

Callback that is called when the text input's submit button is pressed.

| Type                                                  |
| ----------------------------------------------------- |
| (`{nativeEvent: {text, eventCount, target}}`) => void |

Note that on iOS this method isn't called when using `keyboardType="phone-pad"`.

***

### `placeholder`[​](#placeholder "Direct link to placeholder")

The string that will be rendered before text input has been entered.

| Type   |
| ------ |
| string |

***

### `placeholderTextColor`[​](#placeholdertextcolor "Direct link to placeholdertextcolor")

The text color of the placeholder string.

| Type                     |
| ------------------------ |
| [color](/docs/colors.md) |

***

### `readOnly`[​](#readonly "Direct link to readonly")

If `true`, text is not editable. The default value is `false`.

| Type |
| ---- |
| bool |

***

### `returnKeyLabel`Android[​](#returnkeylabel-android "Direct link to returnkeylabel-android")

Sets the return key to the label. Use it instead of `returnKeyType`.

| Type   |
| ------ |
| string |

***

### `returnKeyType`[​](#returnkeytype "Direct link to returnkeytype")

Determines how the return key should look. On Android you can also use `returnKeyLabel`.

*Cross platform*

The following values work across platforms:

* `done`
* `go`
* `next`
* `search`
* `send`

*Android Only*

The following values work on Android only:

* `none`
* `previous`

*iOS Only*

The following values work on iOS only:

* `default`
* `emergency-call`
* `google`
* `join`
* `route`
* `yahoo`

| Type                                                                                                                              |
| --------------------------------------------------------------------------------------------------------------------------------- |
| enum('done', 'go', 'next', 'search', 'send', 'none', 'previous', 'default', 'emergency-call', 'google', 'join', 'route', 'yahoo') |

### `rejectResponderTermination`iOS[​](#rejectrespondertermination-ios "Direct link to rejectrespondertermination-ios")

If `true`, allows TextInput to pass touch events to the parent component. This allows components such as SwipeableListView to be swipeable from the TextInput on iOS, as is the case on Android by default. If `false`, TextInput always asks to handle the input (except when disabled). The default value is `true`.

| Type |
| ---- |
| bool |

***

### `rows`Android[​](#rows-android "Direct link to rows-android")

Sets the number of lines for a `TextInput`. Use it with multiline set to `true` to be able to fill the lines.

| Type   |
| ------ |
| number |

***

### `scrollEnabled`iOS[​](#scrollenabled-ios "Direct link to scrollenabled-ios")

If `false`, scrolling of the text view will be disabled. The default value is `true`. Only works with `multiline={true}`.

| Type |
| ---- |
| bool |

***

### `secureTextEntry`[​](#securetextentry "Direct link to securetextentry")

If `true`, the text input obscures the text entered so that sensitive text like passwords stay secure. The default value is `false`. Does not work with `multiline={true}`.

| Type |
| ---- |
| bool |

***

### `selection`[​](#selection "Direct link to selection")

The start and end of the text input's selection. Set start and end to the same value to position the cursor.

| Type                                  |
| ------------------------------------- |
| object: `{start: number,end: number}` |

***

### `selectionColor`[​](#selectioncolor "Direct link to selectioncolor")

The highlight, selection handle and cursor color of the text input.

| Type                     |
| ------------------------ |
| [color](/docs/colors.md) |

***

### `selectionHandleColor`Android[​](#selectionhandlecolor-android "Direct link to selectionhandlecolor-android")

Sets the color of the selection handle. Unlike `selectionColor`, it allows the selection handle color to be customized independently of the selection's color.

| Type                     |
| ------------------------ |
| [color](/docs/colors.md) |

***

### `selectTextOnFocus`[​](#selecttextonfocus "Direct link to selecttextonfocus")

If `true`, all text will automatically be selected on focus.

| Type |
| ---- |
| bool |

***

### `showSoftInputOnFocus`[​](#showsoftinputonfocus "Direct link to showsoftinputonfocus")

When `false`, it will prevent the soft keyboard from showing when the field is focused. The default value is `true`.

| Type |
| ---- |
| bool |

***

### `smartInsertDelete`iOS[​](#smartinsertdelete-ios "Direct link to smartinsertdelete-ios")

If `false`, the iOS system will not insert an extra space after a paste operation neither delete one or two spaces after a cut or delete operation.

| Type | Default |
| ---- | ------- |
| bool | `true`  |

***

### `spellCheck`iOS[​](#spellcheck-ios "Direct link to spellcheck-ios")

If `false`, disables spell-check style (i.e. red underlines). The default value is inherited from `autoCorrect`.

| Type |
| ---- |
| bool |

***

### `submitBehavior`[​](#submitbehavior "Direct link to submitbehavior")

When the return key is pressed,

For single line inputs:

* `'newline'` defaults to `'blurAndSubmit'`
* `undefined` defaults to `'blurAndSubmit'`

For multiline inputs:

* `'newline'` adds a newline
* `undefined` defaults to `'newline'`

For both single line and multiline inputs:

* `'submit'` will only send a submit event and not blur the input
* `'blurAndSubmit`' will both blur the input and send a submit event

| Type                                       |
| ------------------------------------------ |
| enum('submit', 'blurAndSubmit', 'newline') |

***

### `textAlign`[​](#textalign "Direct link to textalign")

Align the input text to the left, center, or right sides of the input field.

Possible values for `textAlign` are:

* `left`
* `center`
* `right`

| Type                            |
| ------------------------------- |
| enum('left', 'center', 'right') |

***

### `textContentType`iOS[​](#textcontenttype-ios "Direct link to textcontenttype-ios")

Give the keyboard and the system information about the expected semantic meaning for the content that users enter.

note

[`autoComplete`](#autocomplete), provides the same functionality and is available for all platforms. You can use [`Platform.select`](/docs/next/platform#select) for differing platform behaviors.

Avoid using both `textContentType` and `autoComplete`. For backwards compatibility, `textContentType` takes precedence when both properties are set.

You can set `textContentType` to `username` or `password` to enable autofill of login details from the device keychain.

`newPassword` can be used to indicate a new password input the user may want to save in the keychain, and `oneTimeCode` can be used to indicate that a field can be autofilled by a code arriving in an SMS.

To disable autofill, set `textContentType` to `none`.

Possible values for `textContentType` are:

* `none`
* `addressCity`
* `addressCityAndState`
* `addressState`
* `birthdate` (iOS 17+)
* `birthdateDay` (iOS 17+)
* `birthdateMonth` (iOS 17+)
* `birthdateYear` (iOS 17+)
* `countryName`
* `creditCardExpiration` (iOS 17+)
* `creditCardExpirationMonth` (iOS 17+)
* `creditCardExpirationYear` (iOS 17+)
* `creditCardFamilyName` (iOS 17+)
* `creditCardGivenName` (iOS 17+)
* `creditCardMiddleName` (iOS 17+)
* `creditCardName` (iOS 17+)
* `creditCardNumber`
* `creditCardSecurityCode` (iOS 17+)
* `creditCardType` (iOS 17+)
* `emailAddress`
* `familyName`
* `fullStreetAddress`
* `givenName`
* `jobTitle`
* `location`
* `middleName`
* `name`
* `namePrefix`
* `nameSuffix`
* `newPassword`
* `nickname`
* `oneTimeCode`
* `organizationName`
* `password`
* `postalCode`
* `streetAddressLine1`
* `streetAddressLine2`
* `sublocality`
* `telephoneNumber`
* `URL`
* `username`

| Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| enum('none', 'addressCity', 'addressCityAndState', 'addressState', 'birthdate', 'birthdateDay', 'birthdateMonth', 'birthdateYear', 'countryName', 'creditCardExpiration', 'creditCardExpirationMonth', 'creditCardExpirationYear', 'creditCardFamilyName', 'creditCardGivenName', 'creditCardMiddleName', 'creditCardName', 'creditCardNumber', 'creditCardSecurityCode', 'creditCardType', 'emailAddress', 'familyName', 'fullStreetAddress', 'givenName', 'jobTitle', 'location', 'middleName', 'name', 'namePrefix', 'nameSuffix', 'newPassword', 'nickname', 'oneTimeCode', 'organizationName', 'password', 'postalCode', 'streetAddressLine1', 'streetAddressLine2', 'sublocality', 'telephoneNumber', 'URL', 'username') |

***

### `passwordRules`iOS[​](#passwordrules-ios "Direct link to passwordrules-ios")

When using `textContentType` as `newPassword` on iOS we can let the OS know the minimum requirements of the password so that it can generate one that will satisfy them. In order to create a valid string for `PasswordRules` take a look to the [Apple Docs](https://developer.apple.com/password-rules/).

tip

If passwords generation dialog doesn't appear please make sure that:

* AutoFill is enabled: **Settings** → **Passwords & Accounts** → toggle "On" the **AutoFill Passwords**,
* iCloud Keychain is used: **Settings** → **Apple ID** → **iCloud** → **Keychain** → toggle "On" the **iCloud Keychain**.

| Type   |
| ------ |
| string |

***

### `style`[​](#style "Direct link to style")

Note that not all Text styles are supported, an incomplete list of what is not supported includes:

* `borderLeftWidth`
* `borderTopWidth`
* `borderRightWidth`
* `borderBottomWidth`
* `borderTopLeftRadius`
* `borderTopRightRadius`
* `borderBottomRightRadius`
* `borderBottomLeftRadius`

[Styles](/docs/style.md)

| Type                        |
| --------------------------- |
| [Text](/docs/text.md#style) |

***

### `textBreakStrategy`Android[​](#textbreakstrategy-android "Direct link to textbreakstrategy-android")

Set text break strategy on Android API Level 23+, possible values are `simple`, `highQuality`, `balanced` The default value is `highQuality`.

| Type                                      |
| ----------------------------------------- |
| enum('simple', 'highQuality', 'balanced') |

***

### `underlineColorAndroid`Android[​](#underlinecolorandroid-android "Direct link to underlinecolorandroid-android")

The color of the `TextInput` underline.

| Type                     |
| ------------------------ |
| [color](/docs/colors.md) |

***

### `value`[​](#value "Direct link to value")

The value to show for the text input. `TextInput` is a controlled component, which means the native value will be forced to match this value prop if provided. For most uses, this works great, but in some cases this may cause flickering - one common cause is preventing edits by keeping value the same. In addition to setting the same value, either set `editable={false}`, or set/update `maxLength` to prevent unwanted edits without flicker.

| Type   |
| ------ |
| string |

## Methods[​](#methods "Direct link to Methods")

### `.focus()`[​](#focus "Direct link to focus")

tsx

```
focus();
```

Makes the native input request focus.

### `.blur()`[​](#blur "Direct link to blur")

tsx

```
blur();
```

Makes the native input lose focus.

### `clear()`[​](#clear "Direct link to clear")

tsx

```
clear();
```

Removes all text from the `TextInput`.

***

### `isFocused()`[​](#isfocused "Direct link to isfocused")

tsx

```
isFocused(): boolean;
```

Returns `true` if the input is currently focused; `false` otherwise.

# Known issues

* [react-native#19096](https://github.com/facebook/react-native/issues/19096): Doesn't support Android's `onKeyPreIme`.
* [react-native#19366](https://github.com/facebook/react-native/issues/19366): Calling .focus() after closing Android's keyboard via back button doesn't bring keyboard up again.
* [react-native#26799](https://github.com/facebook/react-native/issues/26799): Doesn't support Android's `secureTextEntry` when `keyboardType="email-address"` or `keyboardType="phone-pad"`.
