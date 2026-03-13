# Source: https://docs.logrocket.com/reference/mergeiframes.md

# Capture iframes

Control how iframes are treated during session recording

## Include iframes within the same session recording

#### `mergeIframes` - Boolean

##### optional (default - `false`)

By default, LogRocket will treat iframes as separate tabs in the video replay. If you would like to merge the iframes into a single video, add the following init option to both your main `init()` call *and* the iframe `init()` call.

```javascript Include iFrame within the session recording
LogRocket.init(YOUR_APP_ID, {
  mergeIframes: true,
});
```

# Cross-domain iframes

## Include iframes within the same session recording whose origins are different from their parent window's

#### `parentDomain` - String

##### optional (default - `null`)

#### `childDomains` - Array of strings

##### optional (default - `null`)

With `mergeIframes: true`, LogRocket will still treat cross-domain iframes as separate sessions for video replay. If you would like to merge cross-domain iframes into their parent window's recording, add the following option to your main `init()` call:

```javascript
LogRocket.init(YOUR_APP_ID, {
  mergeIframes: true,
  
  // Indicate the domains of all iframes -- cross- AND same-origin -- included in your main application code
  childDomains: ['https://example.child_frame_domain.com', 'https://example.parent_window_domain.com'],
});
```

Also add the following option to the `init()` calls in all iframes:

```javascript
LogRocket.init(YOUR_APP_ID, {
  mergeIframes: true,
  
  // Indicate the domain of the window in which the iframe is embedded
  parentDomain: 'https://example.parent_window_domain.com',
});
```

> 🚧 Note on the `sandbox` attribute
>
> The LogRocket SDK relies upon being able to access the contents of a rendered iframe in order to record it. If an iframe element is given the `sandbox` attribute to restrict outside access, the `allow-same-origin` rule must be applied in order for the iframe to be recorded:
>
> ```html
> <iframe sandbox="allow-same-origin">
> ```