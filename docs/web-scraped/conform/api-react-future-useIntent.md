# Source: https://conform.guide/api/react/future/useIntent

# useIntent 

> The `useIntent` function is part of Conform\'s future export. These APIs are experimental and may change in minor versions. [Learn more](https://github.com/edmundhung/conform/discussions/954)

A React hook that returns an intent dispatcher for triggering form actions (validate, reset, update, insert, remove, reorder) without submitting the form. Use it for buttons or controls that need to modify form state.

``` 
import  from '@conform-to/react/future';

const intent = useIntent(formRef);
```

## [\#](/api/react/future/useIntent#parameters)Parameters 

### `formRef: FormRef` 

A reference to the form element. Can be either:

-   A React ref object pointing to a form element (e.g. `React.RefObject<HTMLFormElement>`, `React.RefObject<HTMLButtonElement>`, `React.RefObject<HTMLInputElement>`).
-   A form ID string to target a specific form

## [\#](/api/react/future/useIntent#returns)Returns 

An `IntentDispatcher` object with the following methods:

### `validate(name?: string): void` 

Triggers validation for the entire form or a specific field. If you provide a name that includes nested fields (e.g. `user.email`), it will validate all fields within that fieldset.

-   [name] (optional): Field name to validate. If omitted, validates the entire form.

### `reset(options?): void` 

Resets the form to a specific default value.

-   [options.defaultValue] (optional): The value to reset the form to. If not provided, resets to the default value from `useForm`. Pass `null` to clear all fields, or pass a custom object to reset to a specific state.

### `update(options): void` 

Updates a field or fieldset with new values.

-   [options.name] (optional): Field name to update. If omitted, updates the entire form.
-   [options.index] (optional): Array index when updating array fields.
-   [options.value]: New value for the field or fieldset.

### `insert(options): void` 

Inserts a new item into an array field.

-   [options.name]: Name of the array field.
-   [options.index] (optional): Position to insert at. If omitted, appends to the end.
-   [options.defaultValue] (optional): Default value for the new item.

### `remove(options): void` 

Removes an item from an array field.

-   [options.name]: Name of the array field.
-   [options.index]: Index of the item to remove.

### `reorder(options): void` 

Reorders items within an array field.

-   [options.name]: Name of the array field.
-   [options.from]: Current index of the item.
-   [options.to]: Target index to move the item to.

## [\#](/api/react/future/useIntent#examples)Examples 

### Reusable reset button 

``` 
1import  from 'react';
2import  from '@conform-to/react/future';
3
4function ResetButton()  onClick=>
10      Reset Form
11    </button>
12  );
13}
14
15function MyForm()  = useForm();
19
20  return (
21    <form >
22      <input name="email" type="email" />
23      <input name="password" type="password" />
24      <button>Submit</button>
25      <ResetButton />
26    </form>
27  );
28}
```

### Enter key to add array item 

``` 
1import  from 'react';
2import  from '@conform-to/react/future';
3
4function TagInput(: ) );
15      e.currentTarget.value = '';
16    }
17  };
18
19  return (
20    <input
21      ref=
22      type="text"
23      placeholder="Type and press Enter to add..."
24      onKeyDown=
25    />
26  );
27}
28
29function MyForm()  = useForm(,
34  });
35  const tagFields = fields.tags.getFieldList();
36
37  return (
38    <form >
39      <div>
40        <label>Tags</label>
41        <div>
42          >
44              <input
45                type="hidden"
46                name=
47                defaultValue=
48              />
49              
50            </span>
51          ))}
52        </div>
53        <TagInput name="tags" />
54      </div>
55      <button>Submit</button>
56    </form>
57  );
58}
```

## [\#](/api/react/future/useIntent#tips)Tips 

### External buttons with form association 

You can create intent buttons outside the form using the `form` attribute:

``` 
1import  from 'react';
2import  from '@conform-to/react/future';
3
4function ResetButton(: ) 
12      form=
13      onClick=
14    >
15      Reset Form
16    </button>
17  );
18}
19
20function MyApp()  = useForm();
24
25  return (
26    <>
27      <form >
28        <input name="title" />
29        <input name="description" />
30        <button type="submit">Submit</button>
31      </form>
32
33      
34      <ResetButton form= />
35    </>
36  );
37}
```