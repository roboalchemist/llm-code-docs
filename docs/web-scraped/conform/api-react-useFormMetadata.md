# Source: https://conform.guide/api/react/useFormMetadata

# useFormMetadata 

A React hook that returns the form metadata by subscribing to the context set on the [FormProvider](/api/react/FormProvider).

``` 
1const form = useFormMetadata(formId);
```

## [\#](/api/react/useFormMetadata#parameters)Parameters 

### `formId` 

The id attribute that is set on the form element.

## [\#](/api/react/useFormMetadata#returns)Returns 

### `form` 

The form metadata. It is the same object as the one returned by the [useForm](/api/react/useForm) hook.

## [\#](/api/react/useFormMetadata#tips)Tips 

### Better type inference with the `FormId` type 

You can use the `FormId<Schema, FormError>` type instead of `string` to improve the type inference of the form metadata.

``` 
1import  from '@conform-to/react';
2
3type ExampleComponentProps = ;
6
7function ExampleComponent(: ExampleComponentProps) </div>;
12}
```

When rendering your component, you will use the form id provided by Conform, such as `form.id` or `fields.fieldName.formId` which are already typed as `FormId<Schema, FormError>`. This allows typescript to check if the type is compatible and warn you if it doesn\'t. You can still pass a `string`, but you will lose the ability for type checking.

``` 
1import  from '@conform-to/react';
2
3function Example()  />
9      <ExampleComponent formId= />
10    </>
11  );
12}
```

However, the more specific you made with the `FormId` type, the harder it is to reuse the component. If your component have no use of the `Schema` or `FormError` generics, you can keep it simple and type it as `string` as well.

``` 
type ExampleComponentProps = >;
  // If you have a custom error type
  formId: FormId<Record<string, any>, CustomFormError>;
};
```