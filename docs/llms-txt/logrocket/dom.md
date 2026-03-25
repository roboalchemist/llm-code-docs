# Source: https://docs.logrocket.com/reference/dom.md

# Sanitize DOM Data

Control how LogRocket records the DOM

LogRocket records a "video" of your users' sessions by logging diffs in the DOM via [MutationObserver](https://developer.mozilla.org/en-US/docs/Web/API/MutationObserver). The LogRocket SDK will not record `input` elements where `type="password"`; all other elements are captured by default. Sanitization of additional elements can be configured through a number of options, below.

Sanitized elements are rendered in playback with "zebra print" striping. Sanitized data is excluded on the client side, and is never sent back to the LogRocket server.

Network data is sanitized separately from the visual appearance of your site.

## Sanitizing individual elements

#### `data-private`

Elements with the `data-private` attribute are automatically sanitized. The LogRocket SDK will record the dimensions of the element (so that playback renders accurately) but no additional details are recorded about that element or any of its children.

```html Using the data-private attribute
<div data-private>
  This data will <strong>not</strong> be recorded.
</div>
```

Clicks on sanitized elements are not directly detected, but are sometimes visually recognizable in playback. Input fields with the `data-private` attribute will not show user inputs, and there will be no indication that the user is typing.

Sanitized elements can also be hidden fully from playback (no zebra stripes) by setting `data-private="delete"`. This is rarely needed.

#### Lorem Ipsum on individual `input` elements

For `input` and `textarea` elements with `data-private="lipsum"`, the SDK will record the number of characters typed by the user and render them in the playback as if the user were typing [Lorem Ipsum](https://www.lipsum.com/) characters. This option is appropriate for input fields where it is important to know whether the user was actively typing and where exposing the length of the input text does not pose a security risk.

```html Obfuscating text within input elements
<textarea data-private="lipsum"></textarea>
```

## Sanitize all user input fields

#### `inputSanitizer` - Boolean

##### optional (default - `false`)

With this set to `true`, LogRocket will automatically obfuscate all user-input elements like `<input>` and `<select>` from session recordings. None of that data will be recorded or sent to LogRocket.  Note that this includes the following attributes: `mailto` (in an `href`), `alt`, `title`, `aria-label`, and `aria-description`.

```javascript Obfuscate all user inputs
LogRocket.init(YOUR_APP_ID, {
  dom: {
    inputSanitizer: true,
  },
});
```

Nodes can then be allowlisted with the `data-public` attribute. This attribute will not affect existing `data-private` privacy settings.

```html Allowlisting input fields
<input data-public title="this is not private"/>
```

##### Using the Lorem Ipsum sanitizer by default

As with the `data-private` attribute, when the `inputSanitizer` is configured with `"lipsum"`, user input is replaced with [Lorem Ipsum](https://www.lipsum.com/) to simulate content without capturing any actual user input. This option is appropriate for input fields where it is important to know whether the user was typing and where exposing the length of the input text does not pose a security risk.

```Text Replacing all user inputs with Lorem Ipsum
LogRocket.init(YOUR_APP_ID, {
  dom: {
    inputSanitizer: "lipsum",
  },
});
```

> 📘 DOM data and network data are sanitized separately
>
> Sanitizing an input field will not automatically sanitize a network request that is populated with data from that field. [Network requests should be sanitized separately](https://docs.logrocket.com/reference/network).

## Sanitize all text fields

#### `textSanitizer` - Boolean

##### optional (default - `false`)

With this set to `true`, LogRocket will automatically obfuscate all text nodes from all session recordings. None of that data will be recorded or sent to LogRocket.   Note that this includes the following attributes: `mailto`(in an `href`), `alt`, `title`, `aria-label`, and `aria-description`.

Nodes can be allowlisted with the `data-public` attribute. This attribute will not affect existing `data-private` privacy settings.

```javascript Obfuscate all text elements
LogRocket.init(YOUR_APP_ID, {
  dom: {
    textSanitizer: true,
  },
});
```

```html Allowlisting text nodes
<textarea data-public>This is not private</textarea>
```

<br />

![](https://files.readme.io/a8118e1-36421fd-Screen_Shot_2020-01-21_at_3.12.31_PM.png "36421fd-Screen_Shot_2020-01-21_at_3.12.31_PM.png")

<br />

## Sanitize all images

#### `imageSanitizer` - Boolean

##### optional (default - `false`)

With this set to `true`, LogRocket will automatically redact all `<img>` elements from session recordings. None of that data will be recorded or sent to LogRocket.  Note that this includes the following attributes: `alt`, `title`, `aria-label`, and `aria-description`.

```javascript Obfuscate all images
LogRocket.init(YOUR_APP_ID, {
  dom: {
    imageSanitizer: true,
  },
});
```

Nodes can then be allowlisted with the `data-public` attribute. This attribute will not affect existing `data-private` privacy settings.

```html Allowlisting images
<img data-public src="image.png" alt="image that is not private"/>
```

## Sanitize by attribute

#### `privateAttributeBlocklist` String\[]

##### optional (default - `null`)

You may want to disable recording elements based on specific attributes (for example, for third party tracking tools). To achieve this you must pass a list of those attributes to the config. These elements will not be recorded, including all user input on them. They act just like [data-private](https://docs.logrocket.com/docs/privacy).

```javascript
LogRocket.init(YOUR_APP_ID, {
  dom: {
    privateAttributeBlocklist: ['data-hide-this']
  },
});

// will not record: <div data-hide-this></div>
```

## Sanitize by CSS Class Name

#### `privateClassNameBlocklist` String\[]

##### optional (default - `null`)

You may want to disable recording elements based on specific CSS Class Names. To achieve this you must pass a list of those classNames to the initialization config. These elements will not be recorded, including all user input on them. They act just like [data-private](https://docs.logrocket.com/docs/privacy).

```javascript JavaScript
LogRocket.init(YOUR_APP_ID, {
  dom: {
    privateClassNameBlocklist: ['class-hide-this']
  },
});

// will not record: <div class="class-hide-this"></div>
```

## Disable Recording Specific Attributes

#### `hiddenAttributes` String\[]

##### optional (default - `null`)

For more fine-grained control, you can configure LogRocket to ignore specific HTML attributes instead of an entire element by using the `hiddenAttributes` value. For any attribute name matching one of the provided strings, neither the attribute name nor value will be recorded by the SDK.

```javascript JavaScript
LogRocket.init(YOUR_APP_ID, {
  dom: {
    hiddenAttributes: ['hidden-value']
  },
});

// the element:
//  <div hidden-value="foo" shown-value="bar"></div>
// will be recorded as:
//  <div shown-value="bar"></div>
```

## Disable DOM Logging

#### `isEnabled` - Boolean

##### optional (default - `true`)

In the rare scenario in which you would like to disable all DOM recording regardless of class or attribute, you may set `isEnabled` to `false`

> 🚧 Disabling DOM logging will cause session replay to be blank for that page
>
> Network requests, console logs, and a few pieces of performance data will continue to be recorded, but any page recorded with `isEnabled: false` will be completely blank, and will have no clicks or other interaction events recorded at all.

```javascript Disable DOM logging
LogRocket.init(YOUR_APP_ID, {
  dom: {
    isEnabled: false,
  },
});
```

## `_lr-hide` (legacy)

DOM trees containing the `_lr-hide` class are also automatically sanitized, similar to `data-private`. `_lr-hide` is no longer our recommended sanitization technique. Note that DOM trees sanitized via `_lr-hide` are not visualized with zebra stripes, but instead are entirely excluded from the replay visualization.