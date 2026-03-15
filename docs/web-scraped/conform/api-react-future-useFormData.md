# Source: https://conform.guide/api/react/future/useFormData

# useFormData 

> The `useFormData` hook is part of Conform\'s future export. These APIs are experimental and may change in minor versions. [Learn more](https://github.com/edmundhung/conform/discussions/954)

A React hook that subscribes to live form values and derives state from them. Unlike `useForm`, it updates on every input change (but re-renders only when the result changes). Use it for dirty checking, computed values, or conditional UI.

``` 
import  from '@conform-to/react/future';

const result = useFormData(formRef, selector, options);
```

To detect form updates, the hook listens to:

-   Form events: `input`, `focusout`, `submit`, and `reset`
-   DOM mutations:
    -   When inputs are mounted or unmounted
    -   When the `name`, `form`, or `data-conform` attributes change

> Manual changes to input values (e.g. `input.value = 'foo'`) are not tracked unless they also trigger an event or update the `data-conform` attribute.

## [\#](/api/react/future/useFormData#parameters)Parameters 

### `fromRef?: FormRef` 

A reference to the form to observe. You can pass either:

-   A ref object from `useRef()`, pointing to a form-associated element (e.g. `<form>`, `<input>`, `<button>`, etc.)
-   A string ID of a form element

### `selector?: (formData: FormData | URLSearchParams, lastResult?: Result) => Result` 

A function that derives a value from the current form data. It receives:

-   The current form data, which may be:
    -   a `URLSearchParams` object if the `acceptFiles` option is not set or `false`
    -   a `FormData` object if `acceptFiles: true`
    -   `null` â€" on the server, or on the client if the form is not available
-   The previously returned value (or undefined on first render)

The hook will re-run the selector whenever the form changes, and trigger a re-render only if the returned value is not deeply equal to the previous one.

### `options.acceptFiles?: boolean` 

Set to `true` to preserve file inputs and receive a `FormData` object in the selector. If omitted or `false`, the selector receives a `URLSearchParams` object, where all values are coerced to strings.

## [\#](/api/react/future/useFormData#returns)Returns 

The Value returned by your select function. Its type is fully generic and reflects what you extract from the form.

## [\#](/api/react/future/useFormData#example)Example 

### Derive a single field value 

``` 
1const name = useFormData(formRef, (formData) => formData?.get('name') ?? '');
2
3return <p>Hello, !</p>;
```

### Compute a summary from multiple fields 

``` 
1const total = useFormData(formRef, (formData) => , 0);
9});
10
11return <p>Total: $</p>;
```

### Conditionally show a section based on the form data 

``` 
1const isSubscribed = useFormData(
2  formRef,
3  (formData) => formData?.get('subscribe') === 'on' ?? false,
4);
5
6return (
7  <>
8    <label>
9      <input type="checkbox" name="subscribe" />
10      Subscribe to newsletter
11    </label>
12
13    
14  </>
15);
```

## [\#](/api/react/future/useFormData#tips)Tips 

### You can use any form-related element as the reference 

You don\'t need to pass a reference to the `<form>` element itself. The hook will resolve the associated form automatically, either by:

-   the `form` attribute (e.g. `<button form="my-form">`)
-   or by traversing up the DOM to find the closest `<form>` ancestor

For example, here\'s how you might disable an [Add to Cart] button if the item is already selected in the form:

``` 
1function AddToCartButton(: )  disabled=>
10      Add to Cart
11    </button>
12  );
13}
```