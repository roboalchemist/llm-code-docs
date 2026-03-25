# Source: https://conform.guide/api/yup/parseWithYup

# parseWithYup 

A helper that returns an overview of the submission by parsing the form data with the provided yup schema.

``` 
1const submission = parseWithYup(payload, options);
```

## [\#](/api/yup/parseWithYup#parameters)Parameters 

### `payload` 

It could be either the [FormData] or [URLSearchParams] object depending on how the form is submitted.

### `options` 

#### `schema` 

Either a yup schema or a function that returns a yup schema.

#### `async` 

Set it to [true] if you want to parse the form data with [validate] method from the yup schema instead of [validateSync].

## [\#](/api/yup/parseWithYup#example)Example 

``` 
1import  from '@conform-to/yup';
2import  from '@conform-to/react';
3import * as yup from 'yup';
4
5const schema = yup.object();
9
10function Example() ) );
14    },
15  });
16
17  // ...
18}
```