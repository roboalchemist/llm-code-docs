# Source: https://conform.guide/validation

# Validation 

Conform supports different validation modes. In this section, we will walk you through how to validate a form based on different requirements.

## [\#](/validation#server-validation)Server Validation 

You can validate a form [fully server side]. It is not limited to form submission but also works when user is typing or leaving a field. This allows you to exclude the validation logic from the client bundle. But network latency might be a concern if you want to validate while user is typing.

``` 
1import  from '@conform-to/react';
2import  from '@conform-to/zod';
3import  from 'zod';
4
5export async function action(: ActionArgs) ),
12  });
13
14  if (submission.status !== 'success') 
17
18  return await signup(data);
19}
20
21export default function Signup() );
32
33  // ...
34}
```

## [\#](/validation#client-validation)Client Validation 

You can always reuse the validation logic on the client side for instant feedback.

``` 
1import  from '@conform-to/react';
2import  from '@conform-to/zod';
3
4// Move the schema definition out of action
5const schema = z.object();
9
10export async function action(: ActionArgs) );
13
14  // ...
15}
16
17export default function Signup() ) );
27    },
28  });
29
30  // ...
31}
```

## [\#](/validation#async-validation)Async Validation 

Conform supports async validation in a slightly different way. Instead of sending a request to another endpoint, we will simply fallback to server validation when needed.

Here is an example which validates if the email is unique.

``` 
1import  from '@conform-to/zod';
2
3// Instead of sharing a schema, prepare a schema creator
4function createSchema(
5  options?: ,
8) );
27              return;
28            }
29
30            // If it reaches here, then it must be validating on the server
31            // Return the result as a promise so Zod knows it's async instead
32            return options.isEmailUnique(email).then((isUnique) => );
38              }
39            });
40          }),
41        ),
42    }),
43    // ...
44}
45
46export function action() ,
54        }),
55
56       // Enable async validation on the server
57    // We won't set `async: true` on the client
58    // as client validation must be synchronous
59        async: true,
60    });
61
62   // ...
63}
64
65export default function Signup() ) );
74        },
75    });
76
77   // ...
78}
```

## [\#](/validation#skipping-validation)Skipping Validation 

As the schema validates all fields together. This could be expensive especially with async validation. One solution is to minimize the validation by checking the submission intent.

``` 
1import  from '@conform-to/zod';
2
3function createSchema(
4  // The `intent` will be provieded by the `parseWithZod` helper
5  intent: Intent | null,
6  options?: ,
9) );
28              return;
29            }
30
31            if (typeof options?.isEmailUnique !== 'function') );
37              return;
38            }
39
40            return options.isEmailUnique(email).then((isUnique) => );
46              }
47            });
48          }),
49        ),
50    }),
51    // ...
52}
53
54export async function action(: ActionArgs) ,
63            }),
64
65       async: true,
66    });
67
68   // ...
69}
70
71export default function Signup() ) );
80        },
81    });
82
83   // ...
84}
```