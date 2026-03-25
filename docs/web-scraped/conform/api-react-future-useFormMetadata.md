# Source: https://conform.guide/api/react/future/useFormMetadata

# useFormMetadata 

> The `useFormMetadata` function is part of Conform\'s future export. These APIs are experimental and may change in minor versions. [Learn more](https://github.com/edmundhung/conform/discussions/954)

A React hook that returns form-level state (errors, valid, touched) from any component within a `FormProvider`. Use it for error summaries or conditional submit buttons.

``` 
import  from '@conform-to/react/future';

const form = useFormMetadata(options);
```

## [\#](/api/react/future/useFormMetadata#parameters)Parameters 

### `options.formId?: string` 

Optional form identifier to target a specific form when multiple forms are rendered. If not provided, uses the nearest form context.

## [\#](/api/react/future/useFormMetadata#returns)Returns 

A `FormMetadata` object containing:

### `id: string` 

The form\'s unique identifier.

### `key: string` 

Unique identifier that changes on form reset.

### `errorId: string` 

Auto-generated ID for associating form-level errors via `aria-describedby`. Follows the pattern `-form-error`.

### `descriptionId: string` 

Auto-generated ID for associating form-level descriptions via `aria-describedby`. Follows the pattern `-form-description`.

### `touched: boolean` 

Whether any field in the form has been touched (through `intent.validate()` or the `shouldValidate` option).

### `valid: boolean` 

Whether the form currently has no validation errors.

### `invalid: boolean` 

> [âš ï¸? Deprecated:] Use `valid` instead. This property will be removed in version 1.11.0.

Whether the form currently has any validation errors. This is equivalent to `!valid`.

### `errors: ErrorShape[] | undefined` 

Form-level validation errors, if any exist.

### `fieldErrors: Record<string, ErrorShape[]>` 

Object containing errors for all touched fields.

### `defaultValue: Record<string, unknown>` 

Initial form values.

### `props: FormProps` 

Form props object for spreading onto the `<form>` element:

``` 

```

### `context: FormContext<FormShape, ErrorShape>` 

Form context object for use with [`FormProvider`](/api/react/future/FormProvider). Required when using [`useField`](/api/react/future/useField) or [`useFormMetadata`](/api/react/future/useFormMetadata) in child components.

### `getField<FieldShape>(name): Field<FieldShape>` 

Method to get metadata for a specific field by name.

### `getFieldset<FieldShape>(name): Fieldset<FieldShape>` 

Method to get a fieldset object for nested object fields.

### `getFieldList<FieldShape>(name): Field[]` 

Method to get an array of field objects for array fields.

## [\#](/api/react/future/useFormMetadata#example)Example 

### Global error summary 

``` 
1import  from '@conform-to/react/future';
2
3function GlobalErrorSummary() 
9
10  return (
11    <div className="error-summary">
12      <h3>Please fix the following errors:</h3>
13      <ul>
14        >
16            <strong>:</strong> 
17          </li>
18        ))}
19      </ul>
20    </div>
21  );
22}
23
24function App()  = useForm() 
30      if (!payload.password) 
33      return error;
34    },
35  });
36
37  return (
38    <FormProvider context=>
39      <form >
40        <GlobalErrorSummary />
41        <div>
42          <label>Email</label>
43          <input name="email" type="email" />
44        </div>
45        <div>
46          <label>Password</label>
47          <input name="password" type="password" />
48        </div>
49        <button type="submit">Submit</button>
50      </form>
51    </FormProvider>
52  );
53}
```

### Custom form component 

``` 
1import  from '@conform-to/react/future';
2
3function CustomForm(: ) 
9      className=
10    >
11      
12       className="error-message">
17              
18            </div>
19          ))}
20        </div>
21      )}
22
23      
24
25      
26      <button
27        type="submit"
28        disabled=
29        className=
30      >
31        
32      </button>
33    </form>
34  );
35}
36
37function App()  = useForm() ,
44  });
45
46  return (
47    <FormProvider context=>
48      <CustomForm>
49        <div>
50          <label>Name</label>
51          <input name="name" />
52        </div>
53        <div>
54          <label>Email</label>
55          <input name="email" type="email" />
56        </div>
57      </CustomForm>
58    </FormProvider>
59  );
60}
```