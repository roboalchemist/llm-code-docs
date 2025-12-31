# Source: https://conform.guide/api/react/future/isDirty

# isDirty 

> The `isDirty` function is part of Conform\'s future export. These APIs are experimental and may change in minor versions. [Learn more](https://github.com/edmundhung/conform/discussions/954)

A utility function that checks whether current form data differs from default values. Use it with `useFormData` for unsaved changes warnings or disabling save buttons.

``` 
import  from '@conform-to/react/future';

const dirty = isDirty(formData, options);
```

## [\#](/api/react/future/isDirty#parameters)Parameters 

### `formData: FormData | URLSearchParams | Record<string, unknown> | null` 

The current form data to compare. It can be:

-   A `FormData` object
-   A `URLSearchParams` object
-   A plain object that was parsed from form data (i.e. `submission.payload`)

### `options.defaultValue?: Record<string, unknown> | null` 

An object representing the default values of the form to compare against. Defaults to an empty object if not provided.

### `options.serialize?: (value: unknown) => string | File | undefined` 

A function to serialize values in defaultValue before comparing them to the form data. If not provided, a default serializer is used that behaves as follows:

-   boolean:
    -   true â†' \'on\'
    -   false â†' undefined
-   Date:
    -   Converted to ISO string (`.toISOString()`)
-   number / bigint:
    -   Converted to string using `.toString()`
-   string / File:
    -   Returned as-is

### `options.skipEntry?: (name: string) => boolean` 

A function to exclude specific fields from the comparison. Useful for ignoring hidden inputs like CSRF tokens.

``` 
isDirty(formData, );
```

### `options.intentName?: string` 

If set, any entry matching this name will be ignored during comparison. This is useful when using an intent input to distinguish between multiple actions.

## [\#](/api/react/future/isDirty#returns)Returns 

-   `true` if the current form data is different from the default values
-   `false` if it matches
-   `undefined` if formData is `null`

## [\#](/api/react/future/isDirty#example)Example 

### Enable a submit button only if the form is dirty 

``` 
1const dirty = useFormData(
2  formRef,
3  (formData) => isDirty(formData, ) ?? false,
4);
5
6return (
7  <button type="submit" disabled=>
8    Save changes
9  </button>
10);
```

### Submit the form only if the form is dirty 

``` 
1const [form, fields] = useForm()) 
8
9    // Handle submission
10  },
11});
```

### Process form submission on the server only if the form is dirty 

``` 
export async function action() );

  if (submission.status !== 'success') 

  if (isDirty(submission.payload, )) 

  return redirect('/success');
}
```