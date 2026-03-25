# Source: https://conform.guide/api/react/future/FormOptionsProvider

# FormOptionsProvider 

> The `FormOptionsProvider` component is part of Conform\'s future export. These APIs are experimental and may change in minor versions. [Learn more](https://github.com/edmundhung/conform/discussions/954)

A React component that sets default form options for all forms in your application. Use it to configure validation timing or define custom field metadata.

``` 
1import  from '@conform-to/react/future';
2
3export default function App() 
7    </FormOptionsProvider>
8  );
9}
```

## [\#](/api/react/future/FormOptionsProvider#props)Props 

All props are optional. When a prop is not provided, it inherits the default value or from a parent `FormOptionsProvider` if nested.

### `shouldValidate?: 'onSubmit' | 'onBlur' | 'onInput'` 

Determines when validation should run for the first time on a field. Default is `onSubmit`.

This option sets the default validation timing for all forms in your application. Individual forms can override this by passing their own `shouldValidate` option to [useForm](/api/react/future/useForm).

``` 
1<FormOptionsProvider shouldValidate="onBlur">
2  
3</FormOptionsProvider>
```

### `shouldRevalidate?: 'onSubmit' | 'onBlur' | 'onInput'` 

Determines when validation should run again after the field has been validated once. Default is the same as `shouldValidate`.

This is useful when you want an immediate update after the user has interacted with a field. For example, validate on blur initially, but revalidate on every input after the first validation.

``` 
1<FormOptionsProvider shouldValidate="onBlur" shouldRevalidate="onInput">
2  
3</FormOptionsProvider>
```

### `defineCustomMetadata?: <FieldShape, ErrorShape>(metadata: BaseMetadata<FieldShape, ErrorShape>) => CustomMetadata` 

A function that defines custom metadata properties for your form fields. This is particularly useful when integrating with UI libraries or custom form components.

``` 
1import  from '@conform-to/react/future';
5import type  from './components/TextField';
6
7// Define custom metadata properties that matches the type of our custom form components
8function defineCustomMetadata<FieldShape, ErrorShape>(
9  metadata: BaseMetadata<FieldShape, ErrorShape>,
10)  satisfies Partial<React.ComponentProps<typeof TextField>>;
19    },
20  };
21}
22
23// Extend the CustomMetadata interface with our implementation
24// This makes the custom metadata types available on all field metadata objects
25declare module '@conform-to/react/future' 
28}
29
30// Wrap your app with FormOptionsProvider
31<FormOptionsProvider defineCustomMetadata=>
32  <App />
33</FormOptionsProvider>;
```

Once defined, custom metadata properties are available on all field metadata objects:

``` 
1function LoginForm()  = useForm();
5
6  return (
7    <form >
8      
9      <TextField  />
10      <TextField  />
11      <button>Login</button>
12    </form>
13  );
14}
```

### `intentName?: string` 

The name of the submit button field that indicates the submission intent. Default is `'__intent__'`.

This is an advanced option. You typically don\'t need to change this unless you have conflicts with existing field names.

### `serialize(value: unknown) => string | string[] | File | File[] | null | undefined` 

A custom serialization function for converting form data.

This is an advanced option. You typically don\'t need to change this unless you have special serialization requirements.

## [\#](/api/react/future/FormOptionsProvider#tips)Tips 

### Conditional metadata based on field shape 

You can use TypeScript\'s conditional types to restrict custom metadata based on the field shape:

``` 
1function defineCustomMetadata<FieldShape, ErrorShape>(
2  metadata: BaseMetadata<FieldShape, ErrorShape>,
3) >();
11
12      return ,
19        isInvalid: !metadata.valid,
20        errors: metadata.errors?.map((error) => `$`),
21      } satisfies Partial<React.ComponentProps<typeof DateRangePicker>>;
22    },
23  };
24}
25
26declare module '@conform-to/react/future' 
30      ? ReturnType<
31          typeof defineCustomMetadata<FieldShape, ErrorShape>
32        >['dateRangePickerProps']
33      : unknown;
34  }
35}
```