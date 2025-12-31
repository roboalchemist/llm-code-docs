# Source: https://conform.guide/integration/remix

# Remix 

Here is a login form example integrating with [Remix](https://remix.run/). You can find the full example [here](/examples/remix).

``` 
1import  from '@conform-to/react';
2import  from '@conform-to/zod';
3import type  from '@remix-run/node';
4import  from '@remix-run/node';
5import  from '@remix-run/react';
6import  from 'zod';
7
8const schema = z.object();
13
14export async function action(: ActionArgs) );
17
18  if (submission.status !== 'success') 
21
22  // ...
23}
24
25export default function Login() ) );
35    },
36
37    // Validate the form on blur event triggered
38    shouldValidate: 'onBlur',
39    shouldRevalidate: 'onInput',
40  });
41
42  return (
43    <Form method="post" id= onSubmit= noValidate>
44      <div>
45        <label>Email</label>
46        <input
47          type="email"
48          key=
49          name=
50          defaultValue=
51        />
52        <div></div>
53      </div>
54      <div>
55        <label>Password</label>
56        <input
57          type="password"
58          key=
59          name=
60          defaultValue=
61        />
62        <div></div>
63      </div>
64      <label>
65        <div>
66          <span>Remember me</span>
67          <input
68            type="checkbox"
69            key=
70            name=
71            defaultChecked=
72          />
73        </div>
74      </label>
75      <hr />
76      <button>Login</button>
77    </Form>
78  );
79}
```

## [\#](/integration/remix#tips)Tips 

### The default value might be out of sync if you reset the form from the action 

If the default value of the form comes from the loader and you are trying to reset the form on the action, there is a chance you will see the form reset to the previous default value. As Conform will reset the form the moment action data is updated while Remix is still revalidating the loader data. To fix this, you can wait for the state to be `idle` (e.g. `navigation.state` or `fetcher.state`) before passing the `lastResult` to Conform like this:

``` 
1export default function Example()  = useLoaderData<typeof loader>();
3  const lastResult = useActionData<typeof action>();
4  const navigation = useNavigation();
5  const [form, fields] = useForm();
17
18  // ...
19}
```