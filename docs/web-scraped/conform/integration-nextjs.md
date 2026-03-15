# Source: https://conform.guide/integration/nextjs

# Next.js 

Here is a login form example integrating with [Next.js](https://nextjs.org). You can find the full example [here](/examples/nextjs).

``` 
1// schema.ts
2import  from 'zod';
3
4export const loginSchema = z.object();
```

``` 
1'use server'; // action.ts
2
3import  from 'next/navigation';
4import  from '@conform-to/zod';
5import  from '@/app/schema';
6
7export async function login(prevState: unknown, formData: FormData) );
11
12  if (submission.status !== 'success') 
15
16  redirect('/dashboard');
17}
```

``` 
1'use client'; // form.tsx
2
3import  from '@conform-to/react';
4import  from '@conform-to/zod';
5import  from 'react-dom';
6import  from '@/app/actions';
7import  from '@/app/schema';
8
9export function LoginForm() ) );
18    },
19
20    // Validate the form on blur event triggered
21    shouldValidate: 'onBlur',
22    shouldRevalidate: 'onInput',
23  });
24
25  return (
26    <form id= onSubmit= action= noValidate>
27      <div>
28        <label>Email</label>
29        <input
30          type="email"
31          key=
32          name=
33          defaultValue=
34        />
35        <div></div>
36      </div>
37      <div>
38        <label>Password</label>
39        <input
40          type="password"
41          key=
42          name=
43          defaultValue=
44        />
45        <div></div>
46      </div>
47      <label>
48        <div>
49          <span>Remember me</span>
50          <input
51            type="checkbox"
52            key=
53            name=
54            defaultChecked=
55          />
56        </div>
57      </label>
58      <button>Login</button>
59    </form>
60  );
61}
```