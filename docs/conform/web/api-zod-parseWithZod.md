# Source: https://conform.guide/api/zod/parseWithZod

# parseWithZod 

A helper that returns an overview of the submission by parsing the form data with the provided zod schema.

``` 
1const submission = parseWithZod(payload, options);
```

## [\#](/api/zod/parseWithZod#parameters)Parameters 

### `payload` 

It could be either the [FormData] or [URLSearchParams] object depending on how the form is submitted.

### `options.schema` 

Either a zod schema or a function that returns a zod schema.

### `options.async` 

Set it to [true] if you want to parse the form data with [safeParseAsync] method from the zod schema instead of [safeParse].

### `options.errorMap` 

A zod [error map](https://github.com/colinhacks/zod/blob/master/ERROR_HANDLING.md#contextual-error-map) to be used when parsing the form data.

### `options.formatError` 

A function that let you customize the error structure and include additional metadata as needed.

### `options.disableAutoCoercion` 

Set it to [true] if you want to disable [automatic type coercion](/api/zod/parseWithZod#automatic-type-coercion) and manage how the form data is parsed yourself.

## [\#](/api/zod/parseWithZod#example)Example 

``` 
1import  from '@conform-to/zod'; // Or, if you use zod/v4 or zod/v4-mini, import `@conform-to/zod/v4`.
2import  from '@conform-to/react';
3import  from 'zod';
4
5const schema = z.object();
9
10function Example() ) );
14    },
15  });
16
17  // ...
18}
```

## [\#](/api/zod/parseWithZod#tips)Tips 

### Automatic type coercion 

By default, `parseWithZod` will strip empty value and coerce form value to the correct type by introspecting the schema and inject extra preprocessing steps using the [coerceFormValue](/api/zod/coerceFormValue) helper internally.

If you want to customize this behavior, you can disable automatic type coercion by setting `options.disableAutoCoercion` to `true` and manage it yourself.

``` 
1import  from '@conform-to/zod';
2import  from '@conform-to/react';
3import  from 'zod';
4
5const schema = z.object(
11
12    if (value === '') 
15
16    return Number(value.trim().replace(/,/g, ''));
17  }, z.number()),
18});
19
20function Example() ) );
27    },
28  });
29
30  // ...
31}
```