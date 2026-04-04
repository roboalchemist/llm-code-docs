# Source: https://conform.guide/api/valibot/future/coerceFormValue

# coerceFormValue 

> The `coerceFormValue` function is part of Conform\'s future export. These APIs are experimental and may change in minor versions. [Learn more](https://github.com/edmundhung/conform/discussions/954)

A helper that enhances the schema with extra preprocessing steps to strip empty value and coerce form value to the expected type.

``` 
import  from '@conform-to/valibot/future';

const enhancedSchema = coerceFormValue(schema, options);
```

The following rules will be applied by default:

1.  If the value is an empty string / file, pass `undefined` to the schema
2.  If the schema is `v.number()`, trim the value and cast it with the `Number` constructor
3.  If the schema is `v.boolean()`, treat the value as `true` if it equals to `on` (Browser default `value` of a checkbox / radio button)
4.  If the schema is `v.date()`, cast the value with the `Date` constructor
5.  If the schema is `v.bigint()`, trim the value and cast the value with the `BigInt` constructor

## [\#](/api/valibot/future/coerceFormValue#parameters)Parameters 

### `schema` 

The valibot schema to be enhanced.

### `options.defaultCoercion` 

Optional. Set it if you want to [override the default behavior](/api/valibot/future/coerceFormValue#override-default-behavior).

### `options.customize` 

Optional. Use it to [define custom coercion](/api/valibot/future/coerceFormValue#define-custom-coercion) for a specific schema.

## [\#](/api/valibot/future/coerceFormValue#example)Example 

``` 
import  from '@conform-to/valibot/future';
import  from '@conform-to/react';
import * as v from 'valibot';
import  from './jsonSchema';

const schema = coerceFormValue(
  v.object(),
);

function Example() );

  // ...
}
```

## [\#](/api/valibot/future/coerceFormValue#tips)Tips 

### Override default behavior 

You can override the default coercion by specifying the `defaultCoercion` mapping in the options.

``` 
const schema = coerceFormValue(
  v.object(),
  

        // Trim and remove commas before casting it to number
        return Number(value.trim().replace(/,/g, ''));
      },

      // Disable coercion for `boolean()`
      boolean: false,
    },
  },
);
```

### Default values 

`coerceFormValue` will always strip empty values to `undefined`. If you need a default value, use `optional()` to define a fallback value that will be returned instead.

``` 
const schema = v.object();
```

### Define custom coercion 

You can customize coercion for a specific schema by setting the `customize` option.

``` 
import  from '@conform-to/valibot/future';
import * as v from 'valibot';

const metadata = v.object();

const schema = coerceFormValue(
  v.object(),
  

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