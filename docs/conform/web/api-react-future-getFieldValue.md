# Source: https://conform.guide/api/react/future/getFieldValue

# getFieldValue 

> The `getFieldValue` function is part of Conform\'s future export. These APIs are experimental and may change in minor versions. [Learn more](https://github.com/edmundhung/conform/discussions/954)

A utility function that extracts and validates field values from `FormData` or `URLSearchParams`. It supports type guards for runtime validation and can parse nested objects from field naming conventions.

``` 
import  from '@conform-to/react/future';

const value = getFieldValue(formData, name, options);
```

## [\#](/api/react/future/getFieldValue#parameters)Parameters 

### `formData: FormData | URLSearchParams` 

The form data to extract values from. Can be:

-   A `FormData` object from a form submission
-   A `URLSearchParams` object from a URL query string

### `name: string | FieldName<T>` 

The field name to retrieve. Supports nested field names using dot notation and array indices:

-   `email` â†' retrieves the `email` field
-   `address.city` â†' retrieves the nested `city` field within `address`
-   `items[0]` â†' retrieves the first item in the `items` array

When using a `FieldName<T>` from Conform\'s field metadata, the return type is automatically inferred.

### `options.type?: 'string' | 'file' | 'object'` 

Specifies the expected type of the field value. When set, the function validates the value at runtime and throws an error if the type doesn\'t match.

-   `'string'` - Expects a string value
-   `'file'` - Expects a `File` object
-   `'object'` - Expects a plain object

### `options.array?: boolean` 

When `true`, expects the value to be an array.

### `options.optional?: boolean` 

When `true`, returns `undefined` for missing fields instead of throwing an error. Type validation still applies when the field exists.

## [\#](/api/react/future/getFieldValue#returns)Returns 

The return type depends on the options provided:

  Options                                                                                                                                Return Type
  -------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------
  (none)                                                                                                                                 `unknown`
  ``                `string`
  ``                  `File`
  ``                ``
  ``                   `unknown[]`
  ``   `string[]`
  ``     `File[]`
  ``   `Array<>`
  ``                `... | undefined`

## [\#](/api/react/future/getFieldValue#example)Example 

### Basic field retrieval 

``` 
const formData = new FormData();
formData.append('email', '[email protected]');
formData.append('tags', 'react');
formData.append('tags', 'typescript');

// Get single value
const email = getFieldValue(formData, 'email'); // '[email protected]'

// Get all values as array
const tags = getFieldValue(formData, 'tags', ); // ['react', 'typescript']
```

### Parsing nested objects 

``` 
const formData = new FormData();
formData.append('address.city', 'New York');
formData.append('address.zipcode', '10001');

const address = getFieldValue(formData, 'address', );
// 
```

### Parsing array of objects 

``` 
const formData = new FormData();
formData.append('items[0].name', 'Item 1');
formData.append('items[0].price', '10');
formData.append('items[1].name', 'Item 2');
formData.append('items[1].price', '20');

const items = getFieldValue(formData, 'items', );
// [, ]
```

### With useFormData for live updates 

``` 
1import  from '@conform-to/react/future';
2
3function AddressForm()  = useForm();
5
6  const addressFields = fields.address.getFieldset();
7  // Subscribe to address changes with type inference from field name
8  const address = useFormData(form.id, (formData) =>
9    getFieldValue(formData, fields.address.name, ),
10  );
11
12  return (
13    <form >
14      <input name= />
15      <input name= />
16
17      
18      <pre></pre>
19    </form>
20  );
21}
```