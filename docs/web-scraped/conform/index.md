# Source: https://conform.guide/

# Overview 

Conform is a type-safe form validation library utilizing web fundamentals to progressively enhance HTML Forms with full support for server frameworks like [Remix](https://remix.run) and [Next.js](https://nextjs.org).

## [\#](/#features)Features 

-   Progressive enhancement first APIs
-   Type-safe field inference
-   Fine-grained subscription
-   Built-in accessibility helpers
-   Automatic type coercion with Zod

## [\#](/#the-gist)The Gist 

Conform gives you control over the form submission lifecycle from client to the server and exposes the form state through the `useForm()` hook. It does not restrict your form\'s markup and works with any valid HTML form. The form value will be captured from the DOM using the [FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData) Web API and is synced through event delegation.

``` 
1import  from '@conform-to/react';
2import  from '@conform-to/zod';
3import  from 'zod';
4import  from './your-auth-library';
5import  from './your-server-framework';
6
7// Define a schema for your form
8const schema = z.object();
12
13// Optional: Server action handler
14export async function action() );
17
18  // Send the submission back to the client if the status is not successful
19  if (submission.status !== 'success') 
22
23  const session = await login(submission.value);
24
25  // Send the submission with addional error message if login fails
26  if (!session) );
30  }
31
32  return redirect('/dashboard');
33}
34
35// Client form component
36export default function LoginForm() ) );
48    },
49  });
50
51  return (
52    <form method="post" id= onSubmit=>
53      <div></div>
54      <div>
55        <label>Username</label>
56        <input type="text" name= />
57        <div></div>
58      </div>
59      <div>
60        <label>Password</label>
61        <input type="password" name= />
62        <div></div>
63      </div>
64      <button>Login</button>
65    </form>
66  );
67}
```