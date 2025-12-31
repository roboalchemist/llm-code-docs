# Source: https://conform.guide/api/react/future/FormProvider

# FormProvider 

> The `FormProvider` component is part of Conform\'s future export. These APIs are experimental and may change in minor versions. [Learn more](https://github.com/edmundhung/conform/discussions/954)

A React component that provides form context to child components. Required for [useField](/api/react/future/useField) and [useFormMetadata](/api/react/future/useFormMetadata) hooks.

``` 
1import  from '@conform-to/react/future';
2
3export default function SomeParent()  = useForm();
5
6  return <FormProvider context=></FormProvider>;
7}
```

## [\#](/api/react/future/FormProvider#props)Props 

### `context` 

The form context. It is created with [useForm](/api/react/future/useForm) and can be accessed through `form.context`.

## [\#](/api/react/future/FormProvider#tips)Tips 

### FormProvider can be nested 

This is useful if you need to have one form inside another due to layout constraints.

``` 
1import  from '@conform-to/react/future';
2
3function Layout()  = useForm();
5
6  return (
7    <FormProvider context=>
8      <aside>
9        <form >
10          <Field name= />
11          <button>Search</button>
12        </form>
13      </aside>
14      <main></main>
15    </FormProvider>
16  );
17}
18
19function LoginForm()  = useForm();
21
22  return (
23    <Layout>
24      <FormProvider context=>
25        <form >
26          <Field name= />
27          <Field name= />
28          <button>Login</button>
29        </form>
30      </FormProvider>
31    </Layout>
32  );
33}
34
35function Field() );
38
39  return <input name= form= />;
40}
```