# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.params.md.txt

# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.md.txt

## Functions

|                                                                      Function                                                                      |                                                                                                                                                                                                                Description                                                                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [defineBoolean(name, options)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.md#paramsdefineboolean) | Declare a boolean parameter.                                                                                                                                                                                                                                                                                                                                                                                                               |
| [defineInt(name, options)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.md#paramsdefineint)         | Declare an integer parameter.                                                                                                                                                                                                                                                                                                                                                                                                              |
| [defineJsonSecret(name)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.md#paramsdefinejsonsecret)    | Declares a secret parameter that retrieves a structured JSON object in Cloud Secret Manager. This is useful for managing groups of related configuration values, such as all settings for a third-party API, as a single unit.The secret value must be a valid JSON string. At runtime, the value will be automatically parsed and returned as a JavaScript object. If the value is not set or is not valid JSON, an error will be thrown. |
| [defineList(name, options)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.md#paramsdefinelist)       | Declare a list parameter.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [defineSecret(name)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.md#paramsdefinesecret)            | Declares a secret param, that will persist values only in Cloud Secret Manager. Secrets are stored internally as bytestrings. Use`ParamOptions.as`to provide type hinting during parameter resolution.                                                                                                                                                                                                                                     |
| [defineString(name, options)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.md#paramsdefinestring)   | Declare a string parameter.                                                                                                                                                                                                                                                                                                                                                                                                                |
| [multiSelect(options)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.md#paramsmultiselect)           | Create a multi-select input from a series of values.                                                                                                                                                                                                                                                                                                                                                                                       |
| [multiSelect(options)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.md#paramsmultiselect)           | Create a multi-select input from map of labels to values.                                                                                                                                                                                                                                                                                                                                                                                  |
| [select(options)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.md#paramsselect)                     | Create a select input from a series of values.                                                                                                                                                                                                                                                                                                                                                                                             |
| [select(optionsWithLabels)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.md#paramsselect)           | Create a select input from a map of labels to values.                                                                                                                                                                                                                                                                                                                                                                                      |

## Classes

|                                                                     Class                                                                      | Description |
|------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class) |             |

## Interfaces

|                                                                              Interface                                                                               |                                                                                                             Description                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [MultiSelectInput](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.multiselectinput.md#paramsmultiselectinput_interface) | Specifies that a parameter's value should be determined by having the user select a subset from a list of pre-canned options interactively at deploy time. Will result in errors if used on parameters of type other than`string[]`. |
| [SelectInput](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.selectinput.md#paramsselectinput_interface)                | Specifies that a parameter's value should be determined by having the user select from a list of pre-canned options interactively at deploy time.                                                                                    |
| [SelectOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.selectoptions.md#paramsselectoptions_interface)          | One of the options provided to a`SelectInput`, containing a value and optionally a human-readable label to display in the selection interface.                                                                                       |
| [TextInput](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.textinput.md#paramstextinput_interface)                      | Specifies that a parameter's value should be determined by prompting the user to type it in interactively at deploy time. Input that does not match the provided validationRegex, if present, will be retried.                       |

## Variables

|                                                               Variable                                                                |                                                                          Description                                                                          |
|---------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [BUCKET_PICKER](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.md#paramsbucket_picker)   | Autogenerate a list of buckets in a project that a user can select from.                                                                                      |
| [databaseURL](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.md#paramsdatabaseurl)       | A built-in parameter that resolves to the default RTDB database URL associated with the project, without prompting the deployer. Empty string if none exists. |
| [declaredParams](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.md#paramsdeclaredparams) |                                                                                                                                                               |
| [gcloudProject](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.md#paramsgcloudproject)   | A built-in parameter that resolves to the Cloud project ID, without prompting the deployer.                                                                   |
| [projectID](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.md#paramsprojectid)           | A built-in parameter that resolves to the Cloud project ID associated with the project, without prompting the deployer.                                       |
| [storageBucket](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.md#paramsstoragebucket)   | A builtin parameter that resolves to the Cloud storage bucket associated with the function, without prompting the deployer. Empty string if not defined.      |

## Type Aliases

|                                                            Type Alias                                                             |                                         Description                                         |
|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| [ParamOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.md#paramsparamoptions) | Configuration options which can be used to customize the prompting behavior of a parameter. |

## params.defineBoolean()

Declare a boolean parameter.

**Signature:**  

    export declare function defineBoolean(name: string, options?: ParamOptions<boolean>): BooleanParam;

### Parameters

| Parameter |                                                                     Type                                                                     |                            Description                             |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| name      | string                                                                                                                                       | The name of the environment variable to use to load the parameter. |
| options   | [ParamOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.md#paramsparamoptions)\<boolean\> | Configuration options for the parameter.                           |

**Returns:**

BooleanParam

A parameter with a`boolean`return type for`.value`.

## params.defineInt()

Declare an integer parameter.

**Signature:**  

    export declare function defineInt(name: string, options?: ParamOptions<number>): IntParam;

### Parameters

| Parameter |                                                                    Type                                                                     |                            Description                             |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| name      | string                                                                                                                                      | The name of the environment variable to use to load the parameter. |
| options   | [ParamOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.md#paramsparamoptions)\<number\> | Configuration options for the parameter.                           |

**Returns:**

IntParam

A parameter with a`number`return type for`.value`.

## params.defineJsonSecret()

Declares a secret parameter that retrieves a structured JSON object in Cloud Secret Manager. This is useful for managing groups of related configuration values, such as all settings for a third-party API, as a single unit.

The secret value must be a valid JSON string. At runtime, the value will be automatically parsed and returned as a JavaScript object. If the value is not set or is not valid JSON, an error will be thrown.

**Signature:**  

    export declare function defineJsonSecret<T = any>(name: string): JsonSecretParam<T>;

### Parameters

| Parameter |  Type  |                            Description                             |
|-----------|--------|--------------------------------------------------------------------|
| name      | string | The name of the environment variable to use to load the parameter. |

**Returns:**

JsonSecretParam\<T\>

A parameter whose`.value()`method returns the parsed JSON object. \`\`\`

## params.defineList()

Declare a list parameter.

**Signature:**  

    export declare function defineList(name: string, options?: ParamOptions<string[]>): ListParam;

### Parameters

| Parameter |                                                                      Type                                                                       |                            Description                             |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| name      | string                                                                                                                                          | The name of the environment variable to use to load the parameter. |
| options   | [ParamOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.md#paramsparamoptions)\<string\[\]\> | Configuration options for the parameter.                           |

**Returns:**

ListParam

A parameter with a`string[]`return type for`.value`.

## params.defineSecret()

Declares a secret param, that will persist values only in Cloud Secret Manager. Secrets are stored internally as bytestrings. Use`ParamOptions.as`to provide type hinting during parameter resolution.

**Signature:**  

    export declare function defineSecret(name: string): SecretParam;

### Parameters

| Parameter |  Type  |                            Description                             |
|-----------|--------|--------------------------------------------------------------------|
| name      | string | The name of the environment variable to use to load the parameter. |

**Returns:**

SecretParam

A parameter with a`string`return type for`.value`.

## params.defineString()

Declare a string parameter.

**Signature:**  

    export declare function defineString(name: string, options?: ParamOptions<string>): StringParam;

### Parameters

| Parameter |                                                                    Type                                                                     |                            Description                             |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| name      | string                                                                                                                                      | The name of the environment variable to use to load the parameter. |
| options   | [ParamOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.md#paramsparamoptions)\<string\> | Configuration options for the parameter.                           |

**Returns:**

StringParam

A parameter with a`string`return type for`.value`.

## params.multiSelect()

Create a multi-select input from a series of values.

**Signature:**  

    export declare function multiSelect(options: string[]): MultiSelectInput;

### Parameters

| Parameter |    Type    | Description |
|-----------|------------|-------------|
| options   | string\[\] |             |

**Returns:**

[MultiSelectInput](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.multiselectinput.md#paramsmultiselectinput_interface)

## params.multiSelect()

Create a multi-select input from map of labels to values.

**Signature:**  

    export declare function multiSelect(options: Record<string, string>): MultiSelectInput;

### Parameters

| Parameter |           Type           | Description |
|-----------|--------------------------|-------------|
| options   | Record\<string, string\> |             |

**Returns:**

[MultiSelectInput](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.multiselectinput.md#paramsmultiselectinput_interface)

## params.select()

Create a select input from a series of values.

**Signature:**  

    export declare function select<T>(options: T[]): SelectInput<T>;

### Parameters

| Parameter | Type  | Description |
|-----------|-------|-------------|
| options   | T\[\] |             |

**Returns:**

[SelectInput](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.selectinput.md#paramsselectinput_interface)\<T\>

## params.select()

Create a select input from a map of labels to values.

**Signature:**  

    export declare function select<T>(optionsWithLabels: Record<string, T>): SelectInput<T>;

### Parameters

|     Parameter     |        Type         | Description |
|-------------------|---------------------|-------------|
| optionsWithLabels | Record\<string, T\> |             |

**Returns:**

[SelectInput](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.selectinput.md#paramsselectinput_interface)\<T\>

## params.BUCKET_PICKER

Autogenerate a list of buckets in a project that a user can select from.

**Signature:**  

    BUCKET_PICKER: ResourceInput

## params.databaseURL

A built-in parameter that resolves to the default RTDB database URL associated with the project, without prompting the deployer. Empty string if none exists.

**Signature:**  

    databaseURL: Param<string>

## params.declaredParams

**Signature:**  

    declaredParams: SecretOrExpr[]

## params.gcloudProject

A built-in parameter that resolves to the Cloud project ID, without prompting the deployer.

**Signature:**  

    gcloudProject: Param<string>

## params.projectID

A built-in parameter that resolves to the Cloud project ID associated with the project, without prompting the deployer.

**Signature:**  

    projectID: Param<string>

## params.storageBucket

A builtin parameter that resolves to the Cloud storage bucket associated with the function, without prompting the deployer. Empty string if not defined.

**Signature:**  

    storageBucket: Param<string>

## params.ParamOptions

Configuration options which can be used to customize the prompting behavior of a parameter.

**Signature:**  

    export type ParamOptions<T extends string | number | boolean | string[]> = Omit<ParamSpec<T>, "name" | "type">;