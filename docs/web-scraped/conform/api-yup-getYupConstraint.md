# Source: https://conform.guide/api/yup/getYupConstraint

# getYupConstraint 

A helper that returns an object containing the validation attributes for each field by introspecting the yup schema.

``` 
1const constraint = getYupConstraint(schema);
```

## [\#](/api/yup/getYupConstraint#parameters)Parameters 

### `schema` 

The yup schema to be introspected.

## [\#](/api/yup/getYupConstraint#example)Example 

``` 
1import  from '@conform-to/yup';
2import  from '@conform-to/react';
3import * as yup from 'yup';
4
5const schema = yup.object();
9
10function Example() );
14
15  // ...
16}
```