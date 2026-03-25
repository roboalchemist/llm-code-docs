# Source: https://conform.guide/api/react/future/memoize

# memoize 

> The `memoize` function is part of Conform\'s future export. These APIs are experimental and may change in minor versions. [Learn more](https://github.com/edmundhung/conform/discussions/954)

A utility function that caches the most recent result of a function call. Use it to prevent redundant API calls during async validation, like username availability checks.

``` 
import  from '@conform-to/react/future';

const memoizedFn = memoize(fn, isEqual);
```

## [\#](/api/react/future/memoize#parameters)Parameters 

### `fn: T` 

The function to memoize. Can be synchronous or asynchronous.

### `isEqual?: (prevArgs: Parameters<T>, nextArgs: Parameters<T>) => boolean` 

Optional custom equality function to compare arguments. Defaults to shallow comparison using `Object.is()`.

``` 
const memoizedFn = memoize(
  async (user: ) => ,
  // Custom equality - only compare by ID
  (prevArgs, nextArgs) => prevArgs[0].id === nextArgs[0].id,
);
```

## [\#](/api/react/future/memoize#returns)Returns 

A memoized function with the same signature as the original function, plus:

### `clearCache(): void` 

Method to manually clear the memoization cache.

## [\#](/api/react/future/memoize#example)Example 

``` 
import  from '@conform-to/react/future';
import  from 'react';

function Example() `);

        if (!response.ok) 

        return null;
      }),
    [],
  );

  const  = useForm() 
      }

      return error;
    },
  });

  // ...
}
```

## [\#](/api/react/future/memoize#tips)Tips 

### Schema-level validation 

`memoize` can also be used directly in schema libraries with async validation support, such as Zod:

``` 
const schema = z.object(),
});
```

### Memoize at the component level 

Always wrap memoized functions in `useMemo` to prevent recreating them on each render:

``` 
const validateUsername = useMemo(() => memoize(isUsernameUnique), []);
```

Avoid defining memoized functions in the global scope, as this can lead to shared state across multiple component instances.