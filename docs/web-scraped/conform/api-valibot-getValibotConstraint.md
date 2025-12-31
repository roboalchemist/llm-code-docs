# Source: https://conform.guide/api/valibot/getValibotConstraint

# getValibotConstraint 

A helper that returns an object containing the validation attributes for each field by introspecting the valibot schema.

``` 
1const constraint = getValibotConstraint(schema);
```

## [\#](/api/valibot/getValibotConstraint#parameters)Parameters 

### `schema` 

The valibot schema to be introspected.

## [\#](/api/valibot/getValibotConstraint#example)Example 

``` 
1import  from '@conform-to/valibot';
2import  from '@conform-to/react';
3import  from 'valibot';
4
5const schema = object();
9
10function Example() );
14
15  // ...
16}
```