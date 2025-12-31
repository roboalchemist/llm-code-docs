# Source: https://conform.guide/api/react/useInputControl

# useInputControl 

A React hook that let you control the browser events to be dispatched. It is useful if you want to hook up a custom input to Conform.

``` 
1const control = useInputControl(metaOrOptions);
```

## [\#](/api/react/useInputControl#example)Example 

``` 
1import  from '@conform-to/react';
2import  from './custom-ui';
3
4function Example() 
11      value=
12      onChange=
13      onFocus=
14      onBlur=
15    >
16      <Option value="red">Red</Option>
17      <Option value="green">Green</Option>
18      <Option value="blue">Blue</Option>
19    </Select>
20  );
21}
```

## [\#](/api/react/useInputControl#parameters)Parameters 

### `metaOrOptions` 

The field metadata or an options object that includes `key`, `name`, `formId` and `initialValue`.

## [\#](/api/react/useInputControl#returns)Returns 

An input control object. This gives you access to both the input value and helpers to simulate browser events programmatically.

### `value` 

The current value of the input, used for setting up a controlled input.

### `change(value: string)` 

Updates the input value and simulates both the [change](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event) and [input](https://developer.mozilla.org/en-US/docs/Web/API/Element/input_event) events. Use this when you need to change the input value programmatically.

### `blur()` 

Simulates the [blur](https://developer.mozilla.org/en-US/docs/Web/API/Element/blur_event) and [focusout](https://developer.mozilla.org/en-US/docs/Web/API/Element/focusout_event) events as if the user left the input. This does not actually removes keyboard focus from the current element; it just triggers the events.

### `focus()` 

Simulates the [focus](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/focus) and [focusin](https://developer.mozilla.org/en-US/docs/Web/API/Element/focusin_event) events as if the user focused on the input. This does not move the actual keyboard focus to the input. Use native DOM methods like `inputElement.focus()` for real focus control.

## [\#](/api/react/useInputControl#tips)Tips 

### Focus delegation 

Conform will focus on the first invalid input element if submission failed. However, this might not work if your have a custom input. To fix this, you can forward the focus from the input element by listening to the focus event and trigger `element.focus()` on the desired element.

``` 
1import  from '@conform-to/react';
2import  from './custom-ui';
3
4function Example() 
13            defaultValue=
14            className="sr-only"
15            tabIndex=
16            onFocus=
17        />
18        <Select
19            ref=
20            value=
21            onChange=
22            onFocus=
23            onBlur=
24        >
25            <Option value="red">Red</Option>
26            <Option value="green">Green</Option>
27            <Option value="blue">Blue</Option>
28        </Select>
29    <>
30  );
31}
```

In the example above, we set up a hidden input manually instead of passing a `name` prop to the custom select component due to no control over the inner input rendered by the custom input. The input is visually hidden but still focusable thanks to the [sr-only] class from [tailwindcss](https://tailwindcss.com/docs/screen-readers#screen-reader-only-elements). When the input is focused, we delegate the focus to the custom input by calling `inputRef.current?.focus()`.

If you are not using tailwindcss, please look for a similar utility from your preferred styling solution or you can apply the following style based on the implementation of the [sr-only] class:

``` 
1const style = ;
```