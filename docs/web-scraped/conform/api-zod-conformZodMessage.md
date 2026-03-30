# Source: https://conform.guide/api/zod/conformZodMessage

# conformZodMessage 

A set of custom messages to control the validation behavior. This is useful if you need async validation for one of the fields.

## [\#](/api/zod/conformZodMessage#options)Options 

### `conformZodMessage.VALIDATION_SKIPPED` 

This message is used to indicate that the validation is skipped and Conform should use the previous result instead.

### `conformZodMessage.VALIDATION_UNDEFINED` 

This message is used to indicate that the validation is not defined and Conform should fallback to server validation.

## [\#](/api/zod/conformZodMessage#example)Example 

Here is a signup form example which validates if the email is unique.

``` 
1import type  from '@conform-to/react';
2import  from '@conform-to/react';
3import  from '@conform-to/zod'; // Or, if you use zod/v4 or zod/v4-mini, import `@conform-to/zod/v4`.
4import  from 'zod';
5
6// Instead of sharing a schema, prepare a schema creator
7function createSchema(
8  // The `intent` will be provided by the `parseWithZod` helper
9  intent: Intent | null,
10  options?: ,
13) );
31              return;
32            }
33
34            if (typeof options?.isEmailUnique !== 'function') );
40              return;
41            }
42
43            return options.isEmailUnique(email).then((isUnique) => );
49              }
50            });
51          }),
52        ),
53    })
54    .and(
55      z
56        .object(),
58          confirmPassword: z.string(),
61        })
62        .refine((data) => data.password === data.confirmPassword, ),
66    );
67}
68
69export async function action() ,
78      }),
79    async: true,
80  });
81
82  if (submission.status !== 'success') 
85
86  // ...
87}
88
89export default function Signup() ) );
98    },
99  });
100
101  // ...
102}
```