# Source: https://conform.guide/api/react/future/useForm

# useForm 

> The `useForm` function is part of Conform\'s future export. These APIs are experimental and may change in minor versions. [Learn more](https://github.com/edmundhung/conform/discussions/954)

The main React hook for Conform. It manages validation state (errors, touched, valid) that updates on events like submit or blur, not on every keystroke. This keeps re-renders minimal.

``` 
import  from '@conform-to/react/future';

const  = useForm(options);
```

## [\#](/api/react/future/useForm#options)Options 

A configuration object with the following properties:

### `id?: string` 

Optional form identifier. If not provided, a unique ID is automatically generated with [useId()](https://react.dev/reference/react/useId).

### `key?: string` 

Optional key for form state reset. When the key changes, the form resets to its initial state.

### `schema?: StandardSchemaV1<FormShape, Value>` 

Optional [standard schema](https://standardschema.dev/) for validation (e.g., Zod, Valibot, Yup). Removes the need for manual `onValidate` setup.

### `defaultValue?: DefaultValue<FormShape>` 

Initial form values. Can be a partial object matching your form structure.

### `constraint?: Record<string, ValidationAttributes>` 

HTML validation attributes for fields (`required`, `minLength`, `pattern`, etc.).

### `shouldValidate?: 'onSubmit' | 'onBlur' | 'onInput'` 

When to start validation. Defaults to `'onSubmit'`.

### `shouldRevalidate?: 'onSubmit' | 'onBlur' | 'onInput'` 

When to revalidate fields that have been touched. Defaults to same as `shouldValidate`.

### `lastResult?: SubmissionResult<ErrorShape> | null` 

Server-side submission result for form state synchronization.

### `onValidate?: ValidateHandler<ErrorShape, Value>` 

Custom validation handler. Can be skipped if using the `schema` property, or combined with schema to customize validation errors.

### `onError?: ErrorHandler<ErrorShape>` 

Error handling callback triggered when validation errors occur. By default, it focuses the first invalid field.

### `onSubmit?: SubmitHandler<ErrorShape, Value>` 

Form submission handler called when the form is submitted with no validation errors.

### `onInput?: InputHandler` 

Input event handler for custom input event logic.

### `onBlur?: BlurHandler` 

Blur event handler for custom focus handling logic.

## [\#](/api/react/future/useForm#returns)Returns 

The hook returns an object with four properties:

### `form: FormMetadata<ErrorShape>` 

Form-level metadata and state. See [`useFormMetadata`](/api/react/future/useFormMetadata) for complete documentation.

### `fields: Fieldset<FormShape>` 

Fieldset object containing all form fields as properties. Equivalent to calling `form.getFieldset()` without a name. Access field metadata via `fields.fieldName`. See [`useField`](/api/react/future/useField) for field metadata documentation.

### `intent: IntentDispatcher` 

Intent dispatcher for programmatic form actions. Same functionality as [`useIntent`](/api/react/future/useIntent) but already connected to this form.

## [\#](/api/react/future/useForm#examples)Examples 

### Basic form setup 

``` 
1import  from '@conform-to/react/future';
2
3function ContactForm()  = useForm()  else if (!payload.email.includes('@')) 
11
12      return error;
13    },
14  });
15
16  return (
17    <form >
18      <div>
19        <label htmlFor=>Email</label>
20        <input
21          type="email"
22          id=
23          name=
24          defaultValue=
25        />
26        <div></div>
27      </div>
28      <button type="submit">Submit</button>
29    </form>
30  );
31}
```

### With schema validation 

``` 
1import  from '@conform-to/react/future';
2import  from 'zod';
3
4const schema = z.object();
8
9function LoginForm()  = useForm();
13
14  return (
15    <form >
16      <input
17        type="email"
18        name=
19        defaultValue=
20      />
21      <div></div>
22      <input
23        type="password"
24        name=
25        defaultValue=
26      />
27      <div></div>
28
29      <button type="submit" disabled=>
30        Login
31      </button>
32    </form>
33  );
34}
```

### Using intent dispatcher 

``` 
1import  from '@conform-to/react/future';
2
3function DynamicForm()  = useForm(,
8  });
9  const items = fields.items.getFieldList();
10
11  return (
12    <form >
13      >
15          <label htmlFor=>Item </label>
16          <input
17            id=
18            name=
19            defaultValue=
20          />
21          <div></div>
22
23          <button
24            type="button"
25            onClick=)}
26          >
27            Remove
28          </button>
29        </div>
30      ))}
31
32      <button
33        type="button"
34        onClick=)}
35      >
36        Add Item
37      </button>
38
39      <button>Submit</button>
40    </form>
41  );
42}
```

## [\#](/api/react/future/useForm#tips)Tips 

### Field access patterns 

Choose the appropriate pattern based on your needs:

-   [Static fields]: Use `fields.fieldName` directly
-   [Dynamic field]: Use `form.getField(name)`, `form.getFieldset(name)` or `form.getFieldList(name)` to access fields by name
-   [Field components]: Use [`useField`](/api/react/future/useField) or [`useFormMetadata`](/api/react/future/useFormMetadata) in child components