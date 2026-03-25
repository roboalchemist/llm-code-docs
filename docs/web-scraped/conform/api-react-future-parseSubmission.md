# Source: https://conform.guide/api/react/future/parseSubmission

# parseSubmission 

> The `parseSubmission` function is part of Conform\'s future export. These APIs are experimental and may change in minor versions. [Learn more](https://github.com/edmundhung/conform/discussions/954)

A utility function that parses `FormData` or `URLSearchParams` into a structured submission with nested payload and intent. Field names follow these conventions:

-   `name` â†' ``
-   `object.property` â†' ` }`
-   `array[0]` â†' ``
-   `items[]` â†' ``

``` 
import  from '@conform-to/react/future';

const submission = parseSubmission(formData, options);
```

## [\#](/api/react/future/parseSubmission#parameters)Parameters 

### `formData: FormData | URLSearchParams` 

The form data to parse, typically from:

-   Request: `await request.formData()` or `new URLSearchParams(request.url)`
-   Form element: `new FormData(form)`
-   URL: `new URLSearchParams(searchString)`

### `options.intentName?: string` 

The name of the submit button field that indicates the submission intent. Defaults to `__INTENT__`.

### `options.skipEntry?: (name: string) => boolean` 

A function to exclude specific form fields from being parsed. Return `true` to skip the entry.

## [\#](/api/react/future/parseSubmission#returns)Returns 

A `Submission` object containing:

### `payload: Record<string, unknown>` 

The parsed form values structured as nested objects and arrays based on field naming conventions.

### `fields: string[]` 

List of field names that were present in the form data.

### `intent: string | null` 

The submission intent (button value) if an intent button was found, otherwise `null`.

## [\#](/api/react/future/parseSubmission#example)Example 

### React Router Action function 

``` 
1export async function action(: Route.ActionArgs) 
7
8// You can also do this with clientAction
9export async function clientAction(: Route.ActionArgs) 
```

### Next.js Server Action function 

``` 
1export async function createUser(prevState: unknown, formData: FormData) 
```

### Client-side live value subscription 

``` 
1function MyForm() >
11      <input name="user.name" />
12      <input name="user.email" />
13
14      
15      <pre></pre>
16    </form>
17  );
18}
```