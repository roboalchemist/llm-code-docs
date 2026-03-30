# Source: https://conform.guide/api/valibot/conformValibotMessage

# conformValibotMessage 

A set of custom messages to control the validation behavior. This is useful if you need async validation for one of the fields.

## [\#](/api/valibot/conformValibotMessage#options)Options 

### `conformValibotMessage.VALIDATION_SKIPPED` 

This message is used to indicate that the validation is skipped and Conform should use the previous result instead.

### `conformValibotMessage.VALIDATION_UNDEFINED` 

This message is used to indicate that the validation is not defined and Conform should fallback to server validation.

## [\#](/api/valibot/conformValibotMessage#example)Example 

You can skip an validation to use the previous result. On client validation, you can indicate the validation is not defined to fallback to server validation.

``` 
1import type  from '@conform-to/react';
2import  from '@conform-to/react';
3import  from '@conform-to/valibot';
4import  from 'valibot';
15
16function createBaseSchema(intent: Intent | null) );
30}
31
32function createServerSchema(
33  intent: Intent | null,
34  options: ,
35) ) => options.isEmailUnique(email),
42        'Email is already used',
43      ),
44      ['email'],
45    ),
46  );
47}
48
49function createClientSchema(intent: Intent | null) 
63
64export async function action() ,
72      }),
73  });
74
75  // Send the submission back to the client if the status is not successful
76  if (submission.status !== 'success') 
79
80  // ...
81}
82
83function ExampleForm() ] = useForm() );
89    },
90  });
91
92  // ...
93}
```