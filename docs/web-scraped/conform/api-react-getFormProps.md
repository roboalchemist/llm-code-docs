# Source: https://conform.guide/api/react/getFormProps

# getFormProps 

A helper that returns all the props required to make a form element accessible.

``` 
1const props = getFormProps(form, options);
```

## [\#](/api/react/getFormProps#example)Example 

``` 
1import  from '@conform-to/react';
2
3function Example()  />;
7}
```

## [\#](/api/react/getFormProps#options)Options 

### `ariaAttributes` 

Decide whether to include `aria-describedby` in the result props. Default to [true].

### `ariaInvalid` 

Decide whether the aria attributes should be based on `meta.errors` or `meta.allErrors`. Default to [errors].

### `ariaDescribedBy` 

Append additional [id] to the `aria-describedby` attribute. You can pass `meta.descriptionId` from the field metadata.

## [\#](/api/react/getFormProps#tips)Tips 

### The helper is optional 

The helper is just a convenience function to help reducing boilerplate and make it more readable. You can always use the form metadata directly to set the props of your form element.

``` 
1// Before
2function Example() 
6      onSubmit=
7      noValidate=
8      aria-describedby=
9    />
10  );
11}
12
13// After
14function Example()  />;
16}
```

### Make your own helper 

The helper is designed for the native form elements. If you need to use a custom component, you can always make your own helpers.