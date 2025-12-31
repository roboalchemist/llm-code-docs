# Source: https://conform.guide/tutorial

# Tutorial 

In this tutorial, we will start with a basic contact form built with just Remix and Zod. Then, we will show you how to enhance it using Conform.

## [\#](/tutorial#installation)Installation 

Before start, please install conform on your project.

``` 
npm install @conform-to/react @conform-to/zod --save
```

## [\#](/tutorial#initial-setup)Initial setup 

First, let\'s define the schema. Here is a zod schema that we will use to validate the form data:

``` 
import  from 'zod';

const schema = z.object().email('Email is invalid'),
  ),
  message: z.preprocess(
    (value) => (value === '' ? undefined : value),
    z
      .string()
      .min(10, 'Message is too short')
      .max(100, 'Message is too long'),
  ),
});
```

In the action handler, we will parse the form data and validate it with zod. If there is any error, we will return it to the client together with the submitted value.

``` 
1import  from '@remix-run/node';
2import  from 'zod';
3import  from '~/message';
4
5const schema = z.object();
8
9export async function action(: ActionFunctionArgs) ;
26  }
27
28  // We will skip the implementation as it is not important to the tutorial
29  const message = await sendMessage(result.data);
30
31  // Return a form error if the message is not sent
32  if (!message.sent) ,
37    };
38  }
39
40  return redirect('/messages');
41}
```

Then, we will implement the contact form. If the submission result is returned from `useActionData()`, we will display the error message next to each field. The fields are also initialized with the submitted value to persist the form data in case the document is reloaded.

``` 
1import  from '@remix-run/node';
2import  from '@remix-run/react';
3import  from 'zod';
4import  from '~/message';
5
6const schema = z.object();
9
10export async function action(: ActionFunctionArgs) 
13
14export default function ContactUs() </div>
20      <div>
21        <label>Email</label>
22        <input type="email" name="email" defaultValue= />
23        <div></div>
24      </div>
25      <div>
26        <label>Message</label>
27        <textarea name="message" defaultValue= />
28        <div></div>
29      </div>
30      <button>Send</button>
31    </Form>
32  );
33}
```

We are not done yet. Accessibility should never be overlooked. Let\'s make the form more accessible by adding the following attributes:

-   Make sure each label is associated with the input properly with an unique [id]
-   Setup validation attributes similar to the zod schema
-   Configure the [aria-invalid] attribute of the form elements based on the validity
-   Make sure the error message is linked to a form element with the [aria-describedby] attribute

``` 
1import  from '@remix-run/node';
2import  from '@remix-run/react';
3import  from 'zod';
4import  from '~/message';
5
6const schema = z.object();
9
10export async function action(: ActionFunctionArgs) 
13
14export default function ContactUs() 
21    >
22      <div id="contact-error"></div>
23      <div>
24        <label htmlFor="contact-email">Email</label>
25        <input
26          id="contact-email"
27          type="email"
28          name="email"
29          defaultValue=
30          required
31          aria-invalid=
32          aria-describedby=
35        />
36        <div id="contact-email-error"></div>
37      </div>
38      <div>
39        <label htmlFor="contact-message">Message</label>
40        <textarea
41          id="contact-message"
42          name="message"
43          defaultValue=
44          required
45          minLength=
46          maxLength=
47          aria-invalid=
48          aria-describedby=
51        />
52        <div id="contact-email-message"></div>
53      </div>
54      <button>Send</button>
55    </Form>
56  );
57}
```

This is a lot of work even for a simple contact form. It is also error-prone to maintains all the ids. How can we simplify it?

## [\#](/tutorial#introduce-conform)Introduce Conform 

This is where Conform comes in. To begin, we can remove the preprocess from the zod schema as Conform\'s zod integration will automatically strip empty string for you.

``` 
1import  from 'zod';
2
3const schema = z.object()
6    .email('Email is invalid'),
7  message: z
8    .string()
9    .min(10, 'Message is too short')
10    .max(100, 'Message is too long'),
11});
```

Then, we can simplify the action with the `parseWithZod()` helper function. It will parse the form data and return a submission object with either the parsed value or the error.

``` 
1import  from '@conform-to/zod';
2import  from '@remix-run/node';
3import  from 'zod';
4import  from '~/message';
5
6const schema = z.object();
9
10export async function action(: ActionFunctionArgs) );
15
16  // Report the submission to client if it is not successful
17  if (submission.status !== 'success') 
20
21  const message = await sendMessage(submission.value);
22
23  // Return a form error if the message is not sent
24  if (!message.sent) );
28  }
29
30  return redirect('/messages');
31}
```

Now, we can manage all the form metadata with the [useForm](/api/react/useForm) hook. We will also derive the validation attributes from the zod schema using the `getZodConstraint()` helper.

``` 
1import  from '@conform-to/react';
2import  from '@conform-to/zod';
3import  from '@remix-run/node';
4import  from '@remix-run/react';
5import  from 'zod';
6import  from '~/message';
7import  from '~/session';
8
9const schema = z.object();
12
13export async function action(: ActionFunctionArgs) 
16
17export default function ContactUs() );
30
31   return (
32        <Form
33            method="post"
34      
35            id=
36            aria-describedby=
37        >
38            <div id=></div>
39            <div>
40               <label htmlFor=>Email</label>
41               <input
42                    id=
43                    type="email"
44                    name=
45                    defaultValue=
46                    required=
47                    aria-invalid=
48                    aria-describedby=
51                />
52               <div id=></div>
53           </div>
54            <div>
55               <label htmlFor=>Message</label>
56               <textarea
57                    id=
58                    name=
59                    defaultValue=
60                    required=
61                    minLength=
62                    maxLength=
63                    aria-invalid=
64                    aria-describedby=
67                />
68               <div id=></div>
69           </div>
70            <button>Send</button>
71        </Form>
72    );
73}
```

## [\#](/tutorial#improve-validation-experience)Improve validation experience 

Right now the contact form will be validated only when the user submit it. What if we want to give early feedback to the user as they type?

Let\'s setup the `shouldValidate` and `shouldRevalidate` options.

``` 
1import  from '@conform-to/react';
2import  from '@conform-to/zod';
3import  from '@remix-run/node';
8import  from '@remix-run/react';
9import  from '~/message';
10import  from '~/session';
11
12const schema = z.object();
15
16export async function loader(: LoaderFunctionArgs) 
19
20export async function action(: ActionFunctionArgs) 
23
24export default function ContactUs() );
35
36  // ...
37}
```

At this point, our contact form is only validated on the server and takes a round trip to the server to validate the form each time the user types. Let\'s shorten the feedback loop with client validation.

``` 
1import  from '@conform-to/react';
2import  from '@conform-to/zod';
3import  from '@remix-run/node';
4import  from '@remix-run/react';
5import  from '~/message';
6import  from '~/session';
7
8const schema = z.object();
11
12export async function action(: ActionFunctionArgs) 
15
16export default function ContactUs() ) );
25        },
26    });
27
28   return (
29    <Form
30      method="post"
31            id=
32      
33      onSubmit=
34            aria-describedby=
35    >
36      
37    </Form>
38  );
39}
```

## [\#](/tutorial#removing-boilerplate)Removing boilerplate 

It\'s great that Conform can manage all the ids and validation attributes for us. However, it is still a lot of work to setup the form and fields. If you are dealing with native inputs, you can use helpers like [getFormProps](/api/react/getFormProps) and [getInputProps](/api/react/getInputProps) to minimize the boilerplate.

``` 
1import  from '@conform-to/react';
7import  from '@conform-to/zod';
8import  from '@remix-run/node';
9import  from '@remix-run/react';
10import  from '~/message';
11
12const schema = z.object();
15
16export async function action(: ActionFunctionArgs) 
19
20export default function ContactUs() );
25
26  return (
27    <Form method="post" >
28      <div>
29        <label htmlFor=>Email</label>
30        <input )} />
31        <div id=></div>
32      </div>
33      <div>
34        <label htmlFor=>Message</label>
35        <textarea  />
36        <div id=></div>
37      </div>
38      <button>Send</button>
39    </Form>
40  );
41}
```

That\'s it! Here is the complete example that we have built in this tutorial:

``` 
1import  from '@conform-to/react';
7import  from '@conform-to/zod';
8import  from '@remix-run/node';
9import  from '@remix-run/react';
10import  from 'zod';
11import  from '~/message';
12
13const schema = z.object()
16    .email('Email is invalid'),
17  message: z
18    .string()
19    .min(10, 'Message is too short')
20    .max(100, 'Message is too long'),
21});
22
23export async function action(: ActionFunctionArgs) );
26
27  if (submission.status !== 'success') 
30
31  const message = await sendMessage(submission.value);
32
33  if (!message.sent) );
37  }
38
39  return redirect('/messages');
40}
41
42export default function ContactUs() ) );
51    },
52  });
53
54  return (
55    <Form method="post" >
56      <div>
57        <label htmlFor=>Email</label>
58        <input )} />
59        <div id=></div>
60      </div>
61      <div>
62        <label htmlFor=>Message</label>
63        <textarea  />
64        <div id=></div>
65      </div>
66      <button>Send</button>
67    </Form>
68  );
69}
```