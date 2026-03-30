# Source: https://conform.guide/api/zod/getZodConstraint

# getZodConstraint 

A helper that returns an object containing the validation attributes for each field by introspecting the zod schema.

``` 
1const constraint = getZodConstraint(schema);
```

## [\#](/api/zod/getZodConstraint#parameters)Parameters 

### `schema` 

The zod schema to be introspected.

## [\#](/api/zod/getZodConstraint#example)Example 

``` 
1import  from '@conform-to/zod'; // Or, if you use zod/v4 or zod/v4-mini, import `@conform-to/zod/v4`.
2import  from '@conform-to/react';
3import  from 'zod';
4
5const schema = z.object();
9
10function Example() );
14
15  // ...
16}
```