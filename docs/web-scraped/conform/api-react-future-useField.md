# Source: https://conform.guide/api/react/future/useField

# useField 

> The `useField` function is part of Conform\'s future export. These APIs are experimental and may change in minor versions. [Learn more](https://github.com/edmundhung/conform/discussions/954)

A React hook that returns field metadata from any component within a `FormProvider`. Use it to build reusable field components without prop drilling.

``` 
import  from '@conform-to/react/future';

const field = useField(name, options);
```

## [\#](/api/react/future/useField#parameters)Parameters 

### `name: FieldName<FieldShape>` 

The name of the input field.

### `options.formId?: string` 

Optional form identifier to target a specific form when multiple forms are rendered. If not provided, uses the nearest form context.

## [\#](/api/react/future/useField#returns)Returns 

A `Field` object containing field metadata and state:

### `id: string` 

The field\'s unique identifier, automatically generated as `-field-`.

### `name: FieldName<FieldShape>` 

The field name path exactly as provided. The FieldName type is just a branded string type to help with TypeScript inference.

### `formId: string` 

The form\'s unique identifier for associating field via the `form` attribute.

### `descriptionId: string` 

Auto-generated ID for associating field descriptions via `aria-describedby`.

### `errorId: string` 

Auto-generated ID for associating field errors via `aria-describedby`.

### `defaultValue: string` 

The field\'s default value as a string. Returns an empty string `''` when:

-   No default value is set (field value is `null` or `undefined`)
-   The field value cannot be serialized to a string (e.g., objects or arrays)

### `defaultOptions: string[]` 

Default selected options for multi-select fields or checkbox group. Returns an empty array `[]` when:

-   No default options are set (field value is `null` or `undefined`)
-   The field value cannot be serialized to a string array (e.g., nested objects or arrays of objects)

### `defaultChecked: boolean` 

Default checked state for checkbox inputs. Returns `true` if the field value is `'on'`. For radio buttons, compare the field\'s `defaultValue` with the radio button\'s value attribute instead.

### `touched: boolean` 

Whether this field has been touched (through `intent.validate()` or the `shouldValidate` option).

### `valid: boolean` 

Whether this field currently has no validation errors.

### `invalid: boolean` 

> [âš ï¸? Deprecated:] Use `valid` instead. This property will be removed in version 1.11.0.

Whether this field currently has validation errors. This is equivalent to `!valid`.

### `errors: ErrorShape[] | undefined` 

Array of validation error messages for this field.

### `fieldErrors: Record<string, ErrorShape[]>` 

Object containing errors for all touched subfields.

### `ariaInvalid: boolean | undefined` 

Boolean value for the `aria-invalid` attribute. Indicates whether the field has validation errors for screen readers. This is `true` when the field has errors, `undefined` otherwise.

### `ariaDescribedBy: string | undefined` 

String value for the `aria-describedby` attribute. Contains the `errorId` when the field is invalid, `undefined` otherwise. If you need to reference both help text and errors, merge with `descriptionId` manually (e.g., `$ $`).

### Validation Attributes 

HTML validation attributes automatically derived from schema constraints:

-   `required?: boolean`
-   `minLength?: number`
-   `maxLength?: number`
-   `pattern?: string`
-   `min?: string | number`
-   `max?: string | number`
-   `step?: string | number`
-   `multiple?: boolean`

### `getFieldset(): Fieldset<FieldShape>` 

Method to get nested fieldset for object fields under this field.

### `getFieldList(): Field[]` 

Method to get array of fields for list/array fields under this field.

## [\#](/api/react/future/useField#example)Example 

### Dynamic field components 

``` 
1import  from '@conform-to/react/future';
2
3interface FieldProps 
8
9function FormField(: FieldProps) `}>
14      <label htmlFor=>
15        
16        
17      </label>
18
19      <input
20        id=
21        name=
22        type=
23        defaultValue=
24        required=
25        minLength=
26        maxLength=
27        pattern=
28        min=
29        max=
30        step=
31        aria-invalid=
32        aria-describedby=
33      />
34
35       className="field-errors">
37           className="error-message">
39              
40            </p>
41          ))}
42        </div>
43      )}
44    </div>
45  );
46}
47
48// Usage
49function MyForm()  = useForm();
53
54  return (
55    <FormProvider context=>
56      <form >
57        <FormField name="firstName" label="First Name" />
58        <FormField name="email" label="Email" type="email" />
59        <FormField name="age" label="Age" type="number" />
60      </form>
61    </FormProvider>
62  );
63}
```

### Nested field access 

``` 
1import  from '@conform-to/react/future';
2
3function AddressFields(: ) >Street Address</label>
13        <input
14          id=
15          name=
16          defaultValue=
17          required=
18        />
19        </div>
21        )}
22      </div>
23
24      <div>
25        <label htmlFor=>City</label>
26        <input
27          id=
28          name=
29          defaultValue=
30          required=
31        />
32        </div>
34        )}
35      </div>
36
37      <div>
38        <label htmlFor=>ZIP Code</label>
39        <input
40          id=
41          name=
42          defaultValue=
43          pattern=
44          required=
45        />
46        </div>
48        )}
49      </div>
50    </fieldset>
51  );
52}
```

### Array field handling 

``` 
1import  from '@conform-to/react/future';
2
3function TagInput(: ) >
12          <input name= defaultValue= />
13          </span>
15          )}
16        </div>
17      ))}
18    </div>
19  );
20}
```

## [\#](/api/react/future/useField#tips)Tips 

### Accessibility 

The hook provides auto-generated IDs for proper ARIA associations:

-   Use `id` for the input element and `htmlFor` on the label
-   Use `descriptionId` for help text (`aria-describedby`)
-   Use `errorId` for error messages (`aria-describedby`)