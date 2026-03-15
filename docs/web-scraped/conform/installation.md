# Source: https://conform.guide/installation

# Installation 

To use Conform, you need to install it along with the schema library you want to support.

## [\#](/installation#zod)Zod 

If you are using [Zod](https://zod.dev/), install the validation helper library that supports Zod schemas.

``` 
npm install @conform-to/react @conform-to/zod zod
```

To validate FormData, use `parseWithZod`.

``` 
import  from '@conform-to/react';
import  from '@conform-to/zod'; // Or, if you use zod/v4 or zod/v4-mini, import `@conform-to/zod/v4`.
import  from 'zod'; // Or, zod/v4 or zod/v4-mini

const schema = z.object();

function ExampleForm() ] = useForm() );
    },
  });

  // ...
}
```

## [\#](/installation#valibot)Valibot 

If you are using [Valibot](https://valibot.dev/), install the validation helper library that supports Valibot schemas.

``` 
npm install @conform-to/react @conform-to/valibot valibot
```

To validate FormData, use `parseWithValibot`.

``` 
import  from '@conform-to/react';
import  from '@conform-to/valibot';
import  from 'valibot';

const schema = object();

function ExampleForm() ] = useForm() );
    },
  });

  // ...
}
```

## [\#](/installation#yup)Yup 

If you are using [Yup](https://github.com/jquense/yup), install the validation helper library that supports Yup schemas.

``` 
npm install @conform-to/react @conform-to/yup yup
```

To validate FormData, use `parseWithYup`.

``` 
import  from '@conform-to/react';
import  from '@conform-to/yup';
import * as yup from 'yup';

const schema = yup.object();

function ExampleForm() ] = useForm() );
    },
  });

  // ...
}
```