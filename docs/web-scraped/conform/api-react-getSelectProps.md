# Source: https://conform.guide/api/react/getSelectProps

# getSelectProps 

A helper that returns all the props required to make an select element accessible.

``` 
1const props = getSelectProps(meta, options);
```

## [\#](/api/react/getSelectProps#example)Example 

``` 
1import  from '@conform-to/react';
2
3function Example()  />;
7}
```

## [\#](/api/react/getSelectProps#options)Options 

### `value` 

The helper will return a [defaultValue] unless this is set to `false`, e.g. a controlled input.

### `ariaAttributes` 

Decide whether to include `aria-invalid` and `aria-describedby` in the result props. Default to [true].

### `ariaInvalid` 

Decide whether the aria attributes should be based on `meta.errors` or `meta.allErrors`. Default to [errors].

### `ariaDescribedBy` 

Append additional [id] to the `aria-describedby` attribute. You can pass `meta.descriptionId` from the field metadata.

## [\#](/api/react/getSelectProps#tips)Tips 

### The helper is optional 

The helper is just a convenience function to help reducing boilerplate and make it more readable. You can always use the field metadata directly to set the props of your select element.

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
16        multiple=
17      />
18    </form>
19  );
20}
21
22// After
23function Example()  />
27    </form>
28  );
29}
```

### Make your own helper 

The helper is designed for the native select elements. If you need to use a custom component, you can always make your own helpers.