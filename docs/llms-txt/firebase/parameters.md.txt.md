# Source: https://firebase.google.com/docs/extensions/publishers/parameters.md.txt

Parameters are the mechanism through which a user customizes each installed
instance of an extension. Parameters are like the environment variables for an
extension. The values for parameters can either be
[auto-populated](https://firebase.google.com/docs/extensions/publishers/parameters#auto-populated-parameters) (provided by Firebase after
installation) or [user-configured](https://firebase.google.com/docs/extensions/publishers/parameters#user-configured-parameters) (specified by
the user during installation).

These parameters are available for you to reference in your extension's
functions source code, your `extension.yaml` file, and your `POSTINSTALL.md`
file. Here's the syntax for how to reference a parameter called
`PARAMETER_NAME`:

- Within your functions source code, use the
  [`params` module](https://firebase.google.com/docs/functions/config-env#params) (for example,
  `params.defineInt("PARAMETER_NAME")`)
  or `process.env.PARAMETER_NAME`.

- Within `extension.yaml` and `POSTINSTALL.md`, use
  `${param:PARAMETER_NAME}`.

  After installation, the Firebase console displays the contents of the
  `POSTINSTALL.md` file and populates any parameter references with the
  *actual* values for the installed instance.

## Auto-populated parameters

Each installed instance of an extension automatically has access to several
default auto-populated parameters provided by Firebase (refer to the table
below). These parameter values are either the *default* values for the Firebase
project (like the *default* Storage bucket) or they're extension-specific (like
the extension's instance ID).

All auto-populated parameter values are immutable. They are set at the time of
project creation or extension installation.

> [!NOTE]
> **Tip:** Both Realtime Database and Cloud Storage allow multiple database instances and buckets, respectively, in a single Firebase project. So, you might want to set up [user-configured parameters](https://firebase.google.com/docs/extensions/publishers/parameters#user-configured-parameters) to ask users to specify *which* instance or bucket they'd like the extension to use (rather than assuming that users want the extension to use the project's *default* instance or bucket).

Even though Firebase auto-populates these parameter values for the extension,
***Firebase doesn't auto-provision the associated products for the user during
installation*** . The user installing the extension must enable the associated
and applicable product(s) in their project before installation. For example, if
your extension involves Cloud Firestore, the user must
[set up Cloud Firestore](https://firebase.google.com/docs/firestore/quickstart#create) in their
project. We recommend notifying your users about these requirements in
the [`PREINSTALL.md`
file](https://firebase.google.com/docs/extensions/publishers/user-documentation#writing-preinstall).

| **Reference for auto-populated parameter** | **Description** | **Parameter value (provided by Firebase)** |
|---|---|---|
| **Parameters with default values from the Firebase project** |||
| `PROJECT_ID` | Unique identifier for the Firebase project in which the extension is installed | Generalized format: `project-id` Example value: `project-123` |
| `DATABASE_URL` | The Firebase project's *default* Realtime Database instance URL | Generalized format: `https://project-id-default-rtdb.firebaseio.com` (US instances) or `https://project-id-default-rtdb.region-code.firebasedatabase.app` (non-US instances) Example value: `https://project-123-default-rtdb.firebaseio.com` |
| `DATABASE_INSTANCE` | The Firebase project's *default* Realtime Database instance name Usually, this value is the same as the project ID, or ends in `-default-rtdb`. | Generalized format: `project-id` Example value: `project-123` |
| `STORAGE_BUCKET` | The Firebase project's *default* Cloud Storage bucket name | Generalized format: `PROJECT_ID.firebasestorage.app` Example value: `project-123.firebasestorage.app` |
| **Parameter with default value from the extension installation** |||
| `EXT_INSTANCE_ID` | Unique identifier for the installed extension instance This value is generated from the [`name` field](https://firebase.google.com/docs/extensions/reference/extension-yaml#basic-info) specified in the `extension.yaml` file. | Generalized format for 1st installed instance (automatically assigned by Firebase; *cannot* be user-modified during installation): `name-from-extension.yaml` Example value: `my-awesome-extension` <br /> Generalized format for 2nd-installed instance and above (automatically assigned by Firebase; *can* be user-modified during installation): `name-from-extension.yaml-4-digit-alphanumeric-hash` Example value: `my-awesome-extension-6m31` |

## User-configured parameters

To enable a user to customize each installed instance of an extension, you can
ask the user to specify parameter values during installation. To request these
values, you set up the prompts in the `params` section of your `extension.yaml`
file.

Here's an example `params` section, followed by a table describing all available
parameter fields.

    # extension.yaml
    ...

    # Parameters (environment variables) for which the user specifies values during installation
    params:
      - param: DB_PATH
        label: Realtime Database path
        description: >-
          What is the Realtime Database path where you will write new text
          for sentiment analysis?
        type: string
        validationRegex: ^\S+$
        validationErrorMessage: Realtime Database path cannot contain spaces.
        example: path/to/posts
        required: true

      - param: TEXT_KEY
        label: Key for text
        description: What is the name of the key that will contain text to be analyzed?
        type: string
        default: textToAnalyze
        required: true

In the `params` section of your `extension.yaml` file, use the following fields
to define a user-configured parameter:

| **Field** | **Type** | **Description** |
|---|---|---|
| `param` *(required)* | string | Name of the parameter |
| `label` *(required)* | string | Short description for the parameter Displayed to the user when they're prompted for the parameter's value |
| `description` *(optional)* | string | Detailed description for the parameter Displayed to the user when they're prompted for the parameter's value Supports markdown |
| `type` *(optional)* | string | Input mechanism for how the user sets the parameter's value (for example, enter text directly or select from dropdown list) Valid values include the following: - `string`: allows free-form text entry (as limited by your [`validationRegex`](https://firebase.google.com/docs/extensions/publishers/parameters#validation-regex-field)) - `select`: allows selection of one entry from a pre-defined list of options. If you specify this value, you must also define the [`options`](https://firebase.google.com/docs/extensions/publishers/parameters#options-field) field. - `multiSelect`: allows selection of one or more entries from a pre-defined list of options. If you specify this value, you must also define the [`options`](https://firebase.google.com/docs/extensions/publishers/parameters#options-field) field. - `selectResource`: allows selection of a specific type of Firebase resource (such as a Cloud Storage bucket) from the user's project. When you specify a parameter of this type, users will get a more user-friendly selection widget in the installation UI; for this reason, use `selectResource` parameters whenever possible. If you specify this value, you must also define the [`resourceType`](https://firebase.google.com/docs/extensions/publishers/parameters#resourcetype-field) field. - `secret`: allows storage of sensitive strings, such as API keys for third-party services. These values will be stored in [Cloud Secret Manager](https://cloud.google.com/secret-manager/). Cloud Secret Manager is a paid service, the use of which might result in charges for users who install your extension. If you use the `secret` parameter type, be sure to document in your [PREINSTALL](https://firebase.google.com/docs/extensions/publishers/user-documentation#writing-preinstall) file that your extension uses Cloud Secret Manager. If this field is omitted, the parameter defaults to `type` of `string`. |
| `options` *(required if parameter [`type`](https://firebase.google.com/docs/extensions/publishers/parameters#type-field) is `select` or `multiSelect`)* | list | List of values from which the user can select Include `label` and `value` fields within the `options` field: - `label` *(string)*: short description of the selectable option - `value` *(string)* : actual value of the selectable option Be sure to put quotes around these strings to prevent unintentional type conversions. The `value` field is required for the `options` field. If `label` is omitted, the list option defaults to display `value`. example syntax ``` options: - label: value: - label: value: - label: value: ``` |
| `resourceType` *(required if parameter [`type`](https://firebase.google.com/docs/extensions/publishers/parameters#type-field) is `selectResource`)* | string | The type of Firebase resource to prompt the user to select. Currently, only Cloud Storage buckets support resource selectors: | Resource type | Type ID | |---|---| | Cloud Storage bucket | `storage.googleapis.com/Bucket` | Unknown `resourceType` values will be ignored and the UI will render the parameter as a free-form `string` input field. |
| `example` *(optional)* | string | Example value for the parameter |
| `validationRegex` *(optional)* *(only applicable when the parameter `type` is `string`)* | string | Regex string for validation of the parameter's user-configured value Regex is compiled using the go library: RE2 For details about validation, refer to [Validation and error messaging](https://firebase.google.com/docs/extensions/publishers/parameters#validation-error-messaging) below. |
| `validationErrorMessage` *(optional)* | string | Error message to display if the [`validationRegex`](https://firebase.google.com/docs/extensions/publishers/parameters#validation-regex-field) fails For details about error messaging, refer to [Validation and error messaging](https://firebase.google.com/docs/extensions/publishers/parameters#validation-error-messaging) below. |
| `default` *(optional)* | string | Default value for the parameter if the user leaves the parameter's value blank If applicable, you can specify an [auto-populated parameter](https://firebase.google.com/docs/extensions/publishers/parameters#auto-populated-parameter) value for the `default` value (for an example, refer to the `IMG_BUCKET` parameter of the [*Resize Images* extension](https://github.com/firebase/extensions/blob/master/storage-resize-images/extension.yaml)). |
| `required` *(optional)* | boolean | Defines whether the user can submit an empty string when they're prompted for the parameter's value If `required` is omitted, this value defaults to `true` (that is, a required parameter). |
| `immutable` *(optional)* | boolean | Defines whether the user can change the parameter's value after installation (for example, if they [reconfigure](https://firebase.google.com/docs/extensions/manage-installed-extensions#reconfigure) the extension) If `immutable` is omitted, this value defaults to `false`. **Note:** If you define a ["location" parameter for the deployed functions of your extension](https://firebase.google.com/docs/extensions/publishers/parameters#functions-deployment-location), then you should include this `immutable` field in its param object. |

### Validation and error messaging for user-configured values

When you set up a parameter with the `type` of `string`, you need to define
appropriate regex validation via the parameter's
[`validationRegex`](https://firebase.google.com/docs/extensions/publishers/parameters#validation-regex-field) field.

Also, for many extensions, a commonly requested parameter value is a database
path or Cloud Storage bucket. Be aware that during install, reconfigure, or
update, the **Extensions service does *not* validate the following at the
time of parameter value *entry*:**

- Whether the specified database or Cloud Storage bucket is set up within the user's Firebase project
- Whether the specified database path exists within the user's database

However, when the extension is actually deploying its resources, the
Firebase console or the Firebase CLI will display an error message if
the referenced database or Cloud Storage bucket is not yet set up in the project.

We strongly recommend that you notify users in the
[`PREINSTALL` file](https://firebase.google.com/docs/extensions/publishers/user-documentation#writing-preinstall)
about these requirements so that when they install your extension, it
successfully installs and works as expected.

## System parameters

System parameters control the basic configuration of an extension's resources.
Since they are meant to control resource configuration,
they are not accessible as environment variables from within your function code.

You don't normally need to declare anything for these parameters in
`extension.yaml`.
They are automatically defined for every extension instance,
and users have the opportunity to set custom values when they install your
extension.

However, if your extension has special resource requirements,
you can set specific values on a per-resource level in `extension.yaml`.
These per-resource configuration settings will override the user's extension
instance-wide settings.
For example:

    resources:
    - name: high_memory_function
      type: firebaseextensions.v1beta.function
      description: >-
        This function needs at least 1GB of memory!
      properties:
        httpsTrigger: {}
        runtime: nodejs18
        availableMemoryMb: 1024
    - name: normal_function
      type: firebaseextensions.v1beta.function
      description: >-
        This function has no special memory requirements. It will use the
        default value, or the value of `firebaseextension.v1beta.function/memory`
      properties:
        httpsTrigger: {}
        runtime: nodejs18

The available system params are:

| Name | Label (human friendly) | Corresponding field in `properties` | Description |
|---|---|---|---|
| firebaseextensions.v1beta.function/location | Location | `location` | What region should Cloud Functions be deployed to? |
| firebaseextensions.v1beta.function/memory | Function memory | `memory` | How many megabytes of memory should be allocated to each function? |
| firebaseextensions.v1beta.function/timeoutSeconds | Function timeout | `timeout` | How many seconds should functions run before timing out? |
| firebaseextensions.v1beta.function/vpcConnectorEgressSettings | VPC Connector Egress | `vpcConnectorEgressSettings` | Controls outgoing traffic when a VPC connector is configured |
| firebaseextensions.v1beta.function/vpcConnector | VPC Connector | `vpcConnector` | Connects Cloud Functions to specified VPC connector. |
| firebaseextensions.v1beta.function/minInstances | Minimum function instances | `minInstances` | The minimum number of instances of this function to run at once |
| firebaseextensions.v1beta.function/maxInstances | Maximum function instances | `maxInstances` | The maximum number of instances of this function to run at once |
| firebaseextensions.v1beta.function/ingressSettings | Ingress Settings | `ingressSettings` | Controls where incoming traffic is accepted from |
| firebaseextensions.v1beta.function/labels | Labels | `labels` | Labels to apply to all resources in the extension |