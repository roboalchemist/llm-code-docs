# Source: https://conform.guide/api/react/getCollectionProps

# getCollectionProps 

A helper that returns all the props required to make a group of checkboxes or radio buttons accessible.

``` 
1const collectionProps = getCollectionProps(meta, options);
```

## [\#](/api/react/getCollectionProps#example)Example 

``` 
1import  from '@conform-to/react';
2
3function Example() ).map((props) => (
12        <label key= htmlFor=>
13          <input  />
14          <span></span>
15        </label>
16      ))}
17    </>
18  );
19}
```

## [\#](/api/react/getCollectionProps#options)Options 

### `type` 

The type of the collection. It could be [checkbox] or [radio].

### `options` 

The options of the collection. Each option will be treated as the value of the input and used to derive the corresponding [key] or [id].

### `value` 

The helper will return a [defaultValue] unless this is set to `false`, e.g. a controlled input.

### `ariaAttributes` 

Decide whether to include `aria-invalid` and `aria-describedby` in the result props. Default to [true].

### `ariaInvalid` 

Decide whether the aria attributes should be based on `meta.errors` or `meta.allErrors`. Default to [errors].

### `ariaDescribedBy` 

Append additional [id] to the `aria-describedby` attribute. You can pass `meta.descriptionId` from the field metadata.

## [\#](/api/react/getCollectionProps#tips)Tips 

### The helper is optional 

The helper is just a convenience function to help reducing boilerplate and make it more readable. You can always use the field metadata directly to set the props of your checkbox element.

``` 
1// Before
2function Example()  htmlFor=-$`}>
7          <input
8            type="checkbox"
9            key=-$`}
10            id=-$`}
11            name=
12            form=
13            value=
14            defaultChecked=
15            aria-invalid=
16            aria-describedby=
19          />
20          <span></span>
21        </label>
22      ))}
23      x
24    </form>
25  );
26}
27
28// After
29function Example() ).map((props) => (
36        <label key= htmlFor=>
37          <input  />
38          <span></span>
39        </label>
40      ))}
41    </form>
42  );
43}
```

### Make your own helper 

The helper is designed for the native checkbox elements. If you need to use a custom component, you can always make your own helpers.