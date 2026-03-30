# Source: https://conform.guide/api/react/getInputProps

# getInputProps 

A helper that returns all the props required to make an input element accessible.

``` 
1const props = getInputProps(meta, options);
```

## [\#](/api/react/getInputProps#example)Example 

``` 
1import  from '@conform-to/react';
2
3function Example() )} />;
7}
```

## [\#](/api/react/getInputProps#options)Options 

### `type` 

The type of the input. This is used to determine whether a [defaultValue] or [defaultChecked] state is needed.

### `value` 

This is mainly to set the value of the input if the type is `checkbox` or `radio`. But it can also be set to `false` if you want to skip setting the [defaultValue] or [defaultChecked] state, e.g. a controlled input.

### `ariaAttributes` 

Decide whether to include `aria-invalid` and `aria-describedby` in the result props. Default to [true].

### `ariaInvalid` 

Decide whether the aria attributes should be based on `meta.errors` or `meta.allErrors`. Default to [errors].

### `ariaDescribedBy` 

Append additional [id] to the `aria-describedby` attribute. You can pass `meta.descriptionId` from the field metadata.

## [\#](/api/react/getInputProps#tips)Tips 

### The helper is optional 

The helper is just a convenience function to help reducing boilerplate and make it more readable. You can always use the field metadata directly to set the props of your input element.

``` 
1// Before
2function Example() 
6      <input
7        key=
8        id=
9        name=
10        form=
11        defaultValue=
12        aria-invalid=
13        aria-describedby=
14        required=
15        minLength=
16        maxLength=
17        min=
18        max=
19        step=
20        pattern=
21        multiple=
22      />
23      
24      <input
25        type="checkbox"
26        key=
27        id=
28        name=
29        form=
30        value="yes"
31        defaultChecked=
32        aria-invalid=
33        aria-describedby=
36        required=
37      />
38    </form>
39  );
40}
41
42// After
43function Example() 
47      <input )} />
48      
49      <input
50        )}
54      />
55    </form>
56  );
57}
```

### Make your own helper 

The helper is designed for the native input elements. If you need to use a custom component, you can always make your own helpers.