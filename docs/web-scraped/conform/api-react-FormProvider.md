# Source: https://conform.guide/api/react/FormProvider

# FormProvider 

A React component that renders a [Context Provider](https://react.dev/reference/react/createContext#provider) for the form context. It is required if you want to use [useField](/api/react/useField) or [useFormMetadata](/api/react/useFormMetadata) hook.

``` 
1import  from '@conform-to/react';
2
3export default function SomeParent() ></FormProvider>;
7}
```

## [\#](/api/react/FormProvider#props)Props 

### `context` 

The form context. It is created with [useForm](/api/react/useForm) and can be accessed through `form.context`.

## [\#](/api/react/FormProvider#tips)Tips 

### FormProvider does not need to be a direct parent of the form 

You are free to put your inputs anywhere outside of the form as long as they are associated through the [form attribute](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement#instance_properties_related_to_the_parent_form).

``` 
1function Example() >
5      <div>
6        <form id= />
7      </div>
8      <div>
9        <input name= form= />
10      </div>
11    </FormProvider>
12  );
13}
```

### FormProvider can be nested 

This is useful if you need to have one form inside another due to layout constraints.

``` 
1import  from '@conform-to/react';
2
3function Field() );
6
7  return <input name= form= />;
8}
9
10function Parent() );
12  return (
13    <FormProvider context=>
14      <form id= />
15
16      <Field name= />
17      <Child />
18    </FormProvider>
19  );
20}
21
22function Child() );
24
25  return (
26    <FormProvider context=>
27      <form id= />
28      <Field name= />
29
30      
31      <Field name= formId="parent" />
32    </FormProvider>
33  );
34}
```