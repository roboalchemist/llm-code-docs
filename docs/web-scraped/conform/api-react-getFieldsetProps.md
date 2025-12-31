# Source: https://conform.guide/api/react/getFieldsetProps

# getFieldsetProps 

A helper that returns all the props required to make a fieldset element accessible.

``` 
1const props = getFieldsetProps(meta, options);
```

## [\#](/api/react/getFieldsetProps#example)Example 

``` 
1import  from '@conform-to/react';
2
3function Example()  />;
7}
```

## [\#](/api/react/getFieldsetProps#options)Options 

### `ariaAttributes` 

Decide whether to include `aria-describedby` in the result props. Default to [true].

### `ariaInvalid` 

Decide whether the aria attributes should be based on `meta.errors` or `meta.allErrors`. Default to [errors].

### `ariaDescribedBy` 

Append additional [id] to the `aria-describedby` attribute. You can pass `meta.descriptionId` from the field metadata.

## [\#](/api/react/getFieldsetProps#tips)Tips 

### The helper is optional 

The helper is just a convenience function to help reducing boilerplate and make it more readable. You can always use the field metadata directly to set the props of your fieldset element.

``` 
1// Before
2function Example() 
6      name=
7      form=
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

The helper is designed for the native fieldset elements. If you need to use a custom component, you can always make your own helpers.