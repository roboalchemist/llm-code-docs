# Source: https://conform.guide/api/valibot/future/formatResult

# formatResult 

> The `formatResult` function is part of Conform\'s future export. These APIs are experimental and may change in minor versions. [Learn more](https://github.com/edmundhung/conform/discussions/954)

A helper that transforms Valibot validation results into Conform\'s error format for form handling.

``` 
import  from '@conform-to/valibot/future';

const error = formatResult(result);
```

## [\#](/api/valibot/future/formatResult#parameters)Parameters 

### `result: SafeParseResult<GenericSchema | GenericSchemaAsync>` 

The Valibot validation result to be formatted. This should be the result from `v.safeParse()`.

### `options.includeValue?: boolean` 

Optional. Set to `true` if you want both the error and the parsed value returned in an object. This is useful when you are parsing the form value manually and still want to access the parsed value in the `onSubmit` handler on the `useForm` hook.

### `options.formatIssues?: (issue: BaseIssue<unknown>[], name: string) => ErrorShape[]` 

Optional. A function to customize how valibot issues are formatted for each field. This is particularly useful if you want to include additional information from the `BaseIssue` object in the error messages, or if you need to support internationalization.

``` 
const error = formatResult(result, ));
  },
});
```

## [\#](/api/valibot/future/formatResult#returns)Returns 

It returns the formatted error object by default:

``` 
FormError<string> | null;
```

If `includeValue` is set to `true`, it returns an object containing both the error and the parsed value instead:

``` 

```

## [\#](/api/valibot/future/formatResult#example)Example 

### Format Valibot validation result on the server 

``` 
import  from '@conform-to/valibot/future';
import  from '@conform-to/react/future';
import * as v from 'valibot';

const schema = z.object();

export async function action() ),
    };
  }

  // Submission succeeded, process the parsed value with `result.data`
}
```

## [\#](/api/valibot/future/formatResult#tips)Tips 

### Customize error shapes 

The `useForm` hook offers built-in support of standard schema through the `schema` option. However, if you need to customize the error shapes, you will need to use the `onValidate` option instead and format the result manually with `formatResult`.

``` 
import  from '@conform-to/react/future';
import  from '@conform-to/valibot/future';
import * as v from 'valibot';

const schema = v.object();

function Example()  = useForm() " is invalid: $`,
          );
        },
      });
    },
    onSubmit(event, ) ,
  });

  // ...
}
```