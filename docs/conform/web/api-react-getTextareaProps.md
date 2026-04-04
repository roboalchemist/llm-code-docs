# Source: https://conform.guide/api/react/getTextareaProps

# getTextareaProps 

A helper that returns all the props required to make an textarea element accessible.

``` 
1const props = getTextareaProps(meta, options);
```

## [\#](/api/react/getTextareaProps#example)Example 

``` 
1import  from '@conform-to/react';
2
3function Example()  />;
7}
```

## [\#](/api/react/getTextareaProps#options)Options 

### `value` 

The helper will return a [defaultValue] unless this is set to `false`, e.g. a controlled input.

### `ariaAttributes` 

Decide whether to include `aria-invalid` and `aria-describedby` in the result props. Default to [true].

### `ariaInvalid` 

Decide whether the aria attributes should be based on `meta.errors` or `meta.allErrors`. Default to [errors].

### `ariaDescribedBy` 

Append additional [id] to the `aria-describedby` attribute. You can pass `meta.descriptionId` from the field metadata.

## [\#](/api/react/getTextareaProps#tips)Tips 

### The helper is optional 

The helper is just a convenience function to help reducing boilerplate and make it more readable. You can always use the field metadata directly to set the props of your textarea element.

``` 
1// Before
2function Example() 
7        id=
8        name=
9        form=
10        defaultValue=
11        aria-invalid=
12        aria-describedby=
15        required=
16        minLength=
17        maxLength=
18      />
19    </form>
20  );
21}
22
23// After
24function Example()  />
28    </form>
29  );
30}
```

### Make your own helper 

The helper is designed for the native textarea elements. If you need to use a custom component, you can always make your own helpers.