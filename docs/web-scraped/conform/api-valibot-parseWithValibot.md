# Source: https://conform.guide/api/valibot/parseWithValibot

# parseWithValibot 

A helper that returns an overview of the submission by parsing the form data with the provided valibot schema.

``` 
1const submission = parseWithValibot(payload, options);
```

## [\#](/api/valibot/parseWithValibot#parameters)Parameters 

### `payload` 

It could be either the [FormData] or [URLSearchParams] object depending on how the form is submitted.

### `options.schema` 

Either a valibot schema or a function that returns a valibot schema.

### `options.info` 

A valibot [parse configuration](https://github.com/fabian-hiller/valibot/blob/main/website/src/routes/guides/(main-concepts)/parse-data/index.mdx#configuration) and [select language](https://github.com/fabian-hiller/valibot/blob/main/website/src/routes/guides/(advanced)/internationalization/index.mdx#select-language) to be used when parsing the form data.

### `options.disableAutoCoercion` 

Set it to [true] if you want to disable [automatic type coercion](/api/valibot/parseWithValibot#automatic-type-coercion) and manage how the form data is parsed yourself.

## [\#](/api/valibot/parseWithValibot#example)Example 

``` 
1import  from '@conform-to/valibot';
2import  from '@conform-to/react';
3import  from 'valibot';
4
5const schema = object();
9
10function Example() ) );
14    },
15  });
16
17  // ...
18}
```

## [\#](/api/valibot/parseWithValibot#tips)Tips 

### Automatic type coercion 

By default, `parseWithValibot` will strip empty value and coerce form value to the correct type by introspecting the schema and inject extra preprocessing steps using the [coerceFormValue](/api/valibot/coerceFormValue) helper internally.

If you want to customize this behavior, you can disable automatic type coercion by setting `options.disableAutoCoercion` to `true` and manage it yourself.

``` 
1import  from '@conform-to/valibot';
2import  from '@conform-to/react';
3import  from 'valibot';
4
5const schema = object(
13
14      if (value === '') 
17
18      return Number(value.trim().replace(/,/g, ''));
19    }),
20    number(),
21  ),
22});
23
24function Example() ) );
31    },
32  });
33
34  // ...
35}
```