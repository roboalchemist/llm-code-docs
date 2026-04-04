# Source: https://conform.guide/api/zod/coerceFormValue

# unstable_coerceFormValue 

> The `coerceFormValue` function is also available as part of Conform\'s future export. [Check it out](/api/zod/future/coerceFormValue) if you want to use it with other future APIs.

A helper that enhances the schema with extra preprocessing steps to strip empty value and coerce form value to the expected type.

``` 
const enhancedSchema = coerceFormValue(schema, options);
```

The following rules will be applied by default:

1.  If the value is an empty string / file, pass `undefined` to the schema
2.  If the schema is `z.number()`, trim the value and cast it with the `Number` constructor
3.  If the schema is `z.boolean()`, treat the value as `true` if it equals to `on` (Browser default `value` of a checkbox / radio button)
4.  If the schema is `z.date()`, cast the value with the `Date` constructor
5.  If the schema is `z.bigint()`, trim the value and cast it with the `BigInt` constructor

## [\#](/api/zod/coerceFormValue#parameters)Parameters 

### `schema` 

The zod schema to be enhanced.

### `options.defaultCoercion` 

Optional. Set it if you want to [override the default behavior](/api/zod/coerceFormValue#override-default-behavior).

### `options.customize` 

Optional. Use it to [define custom coercion](/api/zod/coerceFormValue#define-custom-coercion) for a specific schema.

## [\#](/api/zod/coerceFormValue#example)Example 

``` 
import  from '@conform-to/zod'; // Or, import `@conform-to/zod/v4`.
import  from '@conform-to/react';
import  from 'zod';

const schema = coerceFormValue(
  z.object(),
);

function Example() ) );
    },
  });

  // ...
}
```

## [\#](/api/zod/coerceFormValue#tips)Tips 

### Override default behavior 

You can override the default coercion by specifying the `defaultCoercion` mapping in the options.

``` 
const schema = coerceFormValue(
  z.object(),
  

        const result = value.trim();

        // Treat it as `undefined` if the value is empty
        if (result === '') 

        return result;
      },

      // Override the default coercion with `z.number()`
      number: (value) => 

        // Trim and remove commas before casting it to number
        return Number(value.trim().replace(/,/g, ''));
      },

      // Disable coercion for `z.boolean()`
      boolean: false,
    },
  },
);
```

### Default values 

`coerceFormValue` will always strip empty values to `undefined`. If you need a default value, use `.transform()` to define a fallback value that will be returned instead.

``` 
const schema = z.object();
```

### Define custom coercion 

You can customize coercion for a specific schema by setting the `customize` option.

``` 
import  from '@conform-to/zod';
import  from '@conform-to/react';
import  from 'zod';

const metadata = z.object();

const schema = coerceFormValue(
  z.object(),
  

          // Parse the value as JSON
          return JSON.parse(value);
        };
      }

      // Return `null` to keep the default behavior
      return null;
    },
  },
);
```