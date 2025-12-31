# Source: https://conform.guide/api/react/future/useControl

# useControl 

> The `useControl` hook is part of Conform\'s future export. These APIs are experimental and may change in minor versions. [Learn more](https://github.com/edmundhung/conform/discussions/954)

A React hook that syncs custom UI components with Conform by bridging them to a hidden native input. Use it when integrating components like date pickers, rich selects, or toggles from UI libraries.

For details on when you need this hook, see the [UI Libraries Integration Guide](/api/integration/ui-libraries).

``` 
import  from '@conform-to/react/future';

const control = useControl(options);
```

## [\#](/api/react/future/useControl#options)Options 

### `defaultValue?: string | string[] | File | File[]` 

The initial value of the base input. It will be used to set the value when the input is first registered.

``` 
// e.g. Text input
const control = useControl();
// e.g. Multi-select
const control = useControl();
```

### `defaultChecked?: boolean` 

Whether the base input should be checked by default. It will be applied when the input is first registered.

``` 
const control = useControl();
```

### `value?: string` 

The value of a checkbox or radio input when checked. This sets the value attribute of the base input.

``` 
const control = useControl();
```

### `onFocus?: () => void` 

A callback function that is triggered when the base input is focused. Use this to delegate focus to a custom input.

``` 
const control = useControl(,
});
```

## [\#](/api/react/future/useControl#returns)Returns 

A control object. This gives you access to the state of the input with helpers to emulate native form events.

### `value: string | undefined` 

Current value of the base input. Undefined if the registered input is a multi-select, file input, or checkbox group.

### `options: string[] | undefined` 

Selected options of the base input. Defined only when the registered input is a multi-select or checkbox group.

### `checked: boolean | undefined` 

Checked state of the base input. Defined only when the registered input is a single checkbox or radio input.

### `files: File[] | undefined` 

Selected files of the base input. Defined only when the registered input is a file input.

### `register: (element: HTMLInputElement | HTMLSelectElement | HTMLTextareaElement | Array<HTMLInputElement>) => void` 

Registers the base input element(s). Accepts a single input or an array for groups.

### `change(value: string | string[] | boolean | File | File[] | FileList | null): void` 

Programmatically updates the input value and emits both [change](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event) and [input](https://developer.mozilla.org/en-US/docs/Web/API/Element/input_event) events.

### `blur(): void` 

Emits [blur](https://developer.mozilla.org/en-US/docs/Web/API/Element/blur_event) and [focusout](https://developer.mozilla.org/en-US/docs/Web/API/Element/focusout_event) events. Does not actually move focus.

### `focus(): void` 

Emits [focus](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/focus) and [focusin](https://developer.mozilla.org/en-US/docs/Web/API/Element/focusin_event) events. This does not move the actual keyboard focus to the input. Use `element.focus()` instead if you want to move focus to the input.

## [\#](/api/react/future/useControl#example)Example 

### Checkbox / Switch 

``` 
1import  from '@conform-to/react/future';
2import  from '@conform-to/react';
3import  from './custom-checkbox-component';
4
5function Example() ,
10  });
11  const control = useControl();
14
15  return (
16    <>
17      <input
18        type="checkbox"
19        name=
20        ref=
21        hidden
22      />
23      <Checkbox
24        checked=
25        onChange=
26        onBlur=
27      >
28        Subscribe to newsletter
29      </Checkbox>
30    </>
31  );
32}
```

### Multi-select 

``` 
1import  from '@conform-to/react/future';
2import  from '@conform-to/react';
3import  from './custom-select-component';
4
5function Example() ,
10  });
11  const control = useControl();
14
15  return (
16    <>
17      <select
18        name=
19        ref=
20        multiple
21        hidden
22      />
23      <Select
24        value=
25        onChange=
26        onBlur=
27      >
28        <Option value="blog">Blog</Option>
29        <Option value="tutorial">Tutorial</Option>
30        <Option value="guide">Guide</Option>
31      </Select>
32    </>
33  );
34}
```

### File input 

``` 
1import  from '@conform-to/react/future';
2import  from '@conform-to/react';
3import  from './custom-file-input-component';
4function Example() 
13        ref=
14        hidden
15      />
16      <DropZone
17        files=
18        onChange=
19        onBlur=
20      />
21    </>
22  );
23}
```

## [\#](/api/react/future/useControl#tips)Tips 

### Progressive enhancement 

If you care about supporting form submissions before JavaScript loads, set `defaultValue`, `defaultChecked`, or `value` directly on the base input. This ensures correct values are included in the form submission. Otherwise, `useControl` will handle it once the app is hydrated.

``` 
// Input
<input
  type="email"
  name=
  defaultValue=
  ref=
  hidden
/>

// Select
<select
  name=
  defaultValue=
  ref=
  hidden
>
  <option value=""></option>
   value=>
      
    </option>
  ))}
</select>

// Textarea
<textarea
  name=
  defaultValue=
  ref=
  hidden
/>
```

### Checkbox / Radio groups 

You can register multiple checkbox or radio inputs as a group by passing an array of elements to `register()`. This is useful when the setup renders a set of native inputs that you want to re-use without re-implementing the group logic:

``` 
<CustomCheckboxGroup
  ref=>
  value=
  onChange=
  onBlur=
/>
```

If you don\'t need to re-use the existing native inputs, you can always represent the group with a single hidden multi-select or text input. For complete examples, see the checkbox and radio group implementations in the [React Aria example](/examples/react-aria/).