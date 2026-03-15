# Source: https://conform.guide/api/react/useField

# useField 

A React hook that returns the field metadata by subscribing to the context set on the [closest] [FormProvider](/api/react/FormProvider).

``` 
1const [meta, form] = useField(name, options);
```

## [\#](/api/react/useField#parameters)Parameters 

### `name` 

The name of the field.

### `options` 

[Optional] with only one option at the moment. If you have a nested form context and you would like to access a field that are not from the closest [FormProvider](/api/react/FormProvider), you can pass a `formId` to make sure the right field metadata is returned.

## [\#](/api/react/useField#returns)Returns 

### `meta` 

The field metadata. This is equivalent to `fields.fieldName` with the [useForm](/api/react/useForm) hook.

### `form` 

The form metadata. It is the same object as the one returned by the [useForm](/api/react/useForm) or [useFormMetadata](/api/react/useFormMetadata) hook.

## [\#](/api/react/useField#tips)Tips 

### Better type-safety with the `FieldName` type 

You can use the `FieldName<FieldSchema, FormSchema, FormError>` type instead of `string` to improve the type inference of the field and form metadata returned.

``` 
1import  from '@conform-to/react';
2
3type ExampleComponentProps = ;
6
7function ExampleComponent(: ExampleComponentProps) </div>;
12}
```

When rendering your component, you will use the name provided by Conform, such as `fields.fieldName.name` which is already typed as `FieldName<FieldSchema, FormSchema, FormError>`. This allows typescript to check if the type is compatible and warn you if it doesn\'t. You can still pass a `string`, but you will lose the ability for type checking.

``` 
1import  from '@conform-to/react';
2
3function Example()  />;
7}
```

However, the more specific you made with the `FieldName` type, the harder it is to reuse the component. If your component have no use for some of the generics, you can always omit them.

``` 
type ExampleComponentProps = >;
  // If you have a custom error type
  name: FieldName<number, any, CustomFormError>;
};
```