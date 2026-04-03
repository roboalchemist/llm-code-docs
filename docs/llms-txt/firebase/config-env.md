# Source: https://firebase.google.com/docs/functions/config-env.md.txt

<br />

Often you'll need additional configuration for your functions, such as third-party API keys or tuneable settings. TheFirebaseSDK forCloud Functionsoffers built-in environment configuration to make it easy to store and retrieve this type of data for your project.

You can choose between these options:

- **Parameterized configuration**(recommended for most scenarios). This provides strongly-typed environment configuration with parameters that are validated at deploy time, which prevents errors and simplifies debugging.
- File-based configuration of**environment variables** . With this approach, you manually create a[dotenv](https://www.npmjs.com/package/dotenv)file for loading environment variables.

For most use cases, parameterized configuration is recommended. This approach makes configuration values available both at runtime and deploy time, and deployment is blocked unless all parameters have a valid value. Conversely, configuration with environment variables is not available at deploy time.
| **Caution:** Environment configuration with`functions.config`was deprecated in version 6.0.0, and will be decommissioned in the next major release.**After December 2025, new deployments with`functions.config()`will fail.** If you are using`functions.config()`,[migrate your configuration](https://firebase.google.com/docs/functions/config-env#migrate-config)as soon as possible.

## Parameterized configuration

Cloud Functions for Firebaseprovides an interface for defining configuration parameters declaratively inside your codebase. The value of these parameters is available both during function deployment, when setting deployment and runtime options, and during execution. This means that the CLI will block deployment unless all parameters have a valid value.  

### Node.js

    const { onRequest } = require('firebase-functions/v2/https');
    const { defineInt, defineString } = require('firebase-functions/params');

    // Define some parameters
    const minInstancesConfig = defineInt('HELLO_WORLD_MININSTANCES');
    const welcomeMessage = defineString('WELCOME_MESSAGE');

    // To use configured parameters inside the config for a function, provide them
    // directly. To use them at runtime, call .value() on them.
    export const helloWorld = onRequest(
      { minInstances: minInstancesConfig },
    (req, res) => {
        res.send(`${welcomeMessage.value()}! I am a function.`);
      }
    );

### Python

    from firebase_functions import https_fn
    from firebase_functions.params import IntParam, StringParam

    MIN_INSTANCES = IntParam("HELLO_WORLD_MIN_INSTANCES")
    WELCOME_MESSAGE = StringParam("WELCOME_MESSAGE")

    # To use configured parameters inside the config for a function, provide them
    # directly. To use them at runtime, call .value() on them.
    @https_fn.on_request(min_instances=MIN_INSTANCES)
    def hello_world(req):
        return https_fn.Response(f'{WELCOME_MESSAGE.value()}! I am a function!')

When deploying a function with parameterized configuration variables, the Firebase CLI first attempts to load their values from local .env files. If they are not present in those files and no`default`is set, the CLI will prompt for the values during deployment, and then automatically save their values to a`.env`file named`.env.<project_ID>`in your`functions/`directory:  

    $ firebase deploy
    i  functions: preparing codebase default for deployment
    ? Enter a string value for ENVIRONMENT: prod
    i  functions: Writing new parameter values to disk: .env.projectId
    ...
    $ firebase deploy
    i  functions: Loaded environment variables from .env.projectId

Depending on your development workflow, it may be useful to add the generated`.env.<project_ID>`file to version control.

### Using parameters in global scope

During deployment, your functions code is loaded and inspected before your parameters have actual values. This means that fetching parameter values during global scope results in deployment failure. For cases where you want to use a parameter to initialize a global value, use the initialization callback`onInit()`. This callback runs before any functions run in production but is not be called during deploy time, so it is a safe place to access a parameter's value.  

### Node.js

    const { GoogleGenerativeAI } = require('@google/generative-ai');
    const { defineSecret } = require('firebase-functions/params');
    const { onInit } = require('firebase-functions/v2/core');

    const apiKey = defineSecret('GOOGLE_API_KEY');

    let genAI;
    onInit(() => {
      genAI = new GoogleGenerativeAI(apiKey.value());
    })

### Python

    from firebase_functions.core import init
    from firebase_functions.params import StringParam, PROJECT_ID
    import firebase_admin
    import vertexai

    location = StringParam("LOCATION")

    x = "hello"

    @init
    def initialize():
      # Note: to write back to a global, you'll need to use the "global" keyword
      # to avoid creating a new local with the same name.
      global x
      x = "world"
      firebase_admin.initialize_app()
      vertexai.init(PROJECT_ID.value, location.value)

If you use parameters of the type`Secret`, note that they are available only in the process of functions that have bound the secret. If a secret is bound only in some functions, check whether`secret.value()`is falsy before using it.

### Configure CLI behavior

Parameters can be configured with an`Options`object that controls how the CLI will prompt for values. The following example sets options to validate the format of a phone number, to provide a simple selection option, and to populate a selection option automatically from the Firebase project:  

### Node.js

    const { defineString } = require('firebase-functions/params');

    const welcomeMessage = defineString('WELCOME_MESSAGE', {default: 'Hello World',
    description: 'The greeting that is returned to the caller of this function'});

    const onlyPhoneNumbers = defineString('PHONE_NUMBER', {
      input: {
        text: {
          validationRegex: /\d{3}-\d{3}-\d{4}/,
          validationErrorMessage: "Please enter
    a phone number in the format XXX-YYY-ZZZZ"
        },
      },
    });

    const selectedOption = defineString('PARITY', {input: params.select(["odd", "even"])});

    const memory = defineInt("MEMORY", {
      description: "How much memory do you need?",
      input: params.select({ "micro": 256, "chonky": 2048 }),
    });

    const extensions = defineList("EXTENSIONS", {
      description: "Which file types should be processed?",
      input: params.multiSelect(["jpg", "tiff", "png", "webp"]),
    });

    const storageBucket = defineString('BUCKET', {
      description: "This will automatically
    populate the selector field with the deploying Cloud Project's
    storage buckets",
      input: params.PICK_STORAGE_BUCKET,
    });

### Python

    from firebase_functions.params import (
        StringParam,
        ListParam,
        TextInput,
        SelectInput,
        SelectOptions,
        ResourceInput,
        ResourceType,
    )

    MIN_INSTANCES = IntParam("HELLO_WORLD_MIN_INSTANCES")

    WELCOME_MESSAGE = StringParam(
        "WELCOME_MESSAGE",
        default="Hello World",
        description="The greeting that is returned to the caller of this function",
    )

    ONLY_PHONE_NUMBERS = StringParam(
        "PHONE_NUMBER",
        input=TextInput(
            validation_regex="\d{3}-\d{3}-\d{4}",
            validation_error_message="Please enter a phone number in the format XXX-YYY-XXX",
        ),
    )

    SELECT_OPTION = StringParam(
        "PARITY",
        input=SelectInput([SelectOptions(value="odd"), SelectOptions(value="even")]),
    )

    STORAGE_BUCKET = StringParam(
        "BUCKET",
        input=ResourceInput(type=ResourceType.STORAGE_BUCKET),
        description="This will automatically populate the selector field with the deploying Cloud Project's storage buckets",
    )

### Parameter types

Parameterized configuration provides strong typing for parameter values, and also support secrets from Cloud Secret Manager. Supported types are:

- Secret
- String
- Boolean
- Integer
- Float
- List (Node.js)
- JSON Secret (Node.js)

See the[`params`namespace reference](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params)for information on the functions for defining parameters.

### Parameter values and expressions

Firebase evaluates your parameters both at deploy time and while your function is executing. Due to these dual environments, some extra care must be taken when comparing parameter values, and when using them to set[runtime options](https://firebase.google.com/docs/functions/manage-functions?gen=2nd#set-runtime-options)for your functions.

To pass a parameter to your function as a runtime option, pass it directly:  

### Node.js

    const { onRequest } = require('firebase-functions/v2/https');
    const { defineInt } = require('firebase-functions/params');
    const minInstancesConfig = defineInt('HELLO\_WORLD\_MININSTANCES');

    export const helloWorld = onRequest(
      { minInstances: minInstancesConfig },
      (req, res) => {
        //...

### Python

    from firebase_functions import https_fn
    from firebase_functions.params import IntParam

    MIN_INSTANCES = IntParam("HELLO_WORLD_MIN_INSTANCES")

    @https_fn.on_request(min_instances=MIN_INSTANCES)
    def hello_world(req):
        ...

Additionally, if you need to compare against a parameter in order to know what option to pick, you'll need to use built-in comparators instead of checking the value:  

### Node.js

    const { onRequest } = require('firebase-functions/v2/https');
    const environment = params.defineString('ENVIRONMENT', {default: 'dev'});

    // use built-in comparators
    const minInstancesConfig = environment.equals('PRODUCTION').thenElse(10, 1);
    export const helloWorld = onRequest(
      { minInstances: minInstancesConfig },
      (req, res) => {
        //...

### Python

    from firebase_functions import https_fn
    from firebase_functions.params import IntParam, StringParam

    ENVIRONMENT = StringParam("ENVIRONMENT", default="dev")
    MIN_INSTANCES = ENVIRONMENT.equals("PRODUCTION").then(10, 0)

    @https_fn.on_request(min_instances=MIN_INSTANCES)
    def hello_world(req):
        ...

Parameters and parameter expressions that are only used at runtime can be accessed with their`value`function:  

### Node.js

    const { onRequest } = require('firebase-functions/v2/https');
    const { defineString } = require('firebase-functions/params');
    const welcomeMessage = defineString('WELCOME_MESSAGE');

    // To use configured parameters inside the config for a function, provide them
    // directly. To use them at runtime, call .value() on them.
    export const helloWorld = onRequest(
    (req, res) => {
        res.send(`${welcomeMessage.value()}! I am a function.`);
      }
    );

### Python

    from firebase_functions import https_fn
    from firebase_functions.params import StringParam

    WELCOME_MESSAGE = StringParam("WELCOME_MESSAGE")

    @https_fn.on_request()
    def hello_world(req):
        return https_fn.Response(f'{WELCOME_MESSAGE.value()}! I am a function!')

### Built-in parameters

The Cloud Functions SDK offers three pre-defined parameters, available from the`firebase-functions/params`subpackage:  

### Node.js

- `projectID`--- the Cloud project in which the function is running.
- `databaseURL`--- the URL of the Realtime Database instance associated with the function (if enabled on the Firebase project).
- `storageBucket`--- the Cloud Storage bucket associated with the function (if enabled on the Firebase project).

### Python

- `PROJECT_ID`--- the Cloud project in which the function is running.
- `DATABASE_URL`--- the URL of the Realtime Database instance associated with the function (if enabled on the Firebase project).
- `STORAGE_BUCKET`--- the Cloud Storage bucket associated with the function (if enabled on the Firebase project).

These function like user-defined string parameters in all respects, except that, since their values are always known to the Firebase CLI, their values will never be prompted for on deployment nor saved to`.env`files.

### Secret parameters

Parameters of type`Secret`, defined using`defineSecret()`, represent string parameters which have a value stored in Cloud Secret Manager. Instead of checking against a local`.env`file and writing a new value to the file if missing, secret parameters check against existence in Cloud Secret Manager, and interactively prompt for the value of a new secret during deployment.

Secret parameters must be bound to individual functions that should have access to them:  

### Node.js

    const { onRequest } = require('firebase-functions/v2/https');
    const { defineSecret } = require('firebase-functions/params');
    const discordApiKey = defineSecret('DISCORD_API_KEY');

    export const postToDiscord = onRequest(
      { secrets: [discordApiKey] },
      (req, res) => {
      const apiKey = discordApiKey.value();
        //...

### Python

    from firebase_functions import https_fn
    from firebase_functions.params import SecretParam

    DISCORD_API_KEY = SecretParam('DISCORD_API_KEY')

    @https_fn.on_request(secrets=[DISCORD_API_KEY])
    def post_to_discord(req):
        api_key = DISCORD_API_KEY.value

Because the values of secrets are hidden until execution of the function, you cannot use them while configuring your function.

### Structured JSON secrets

If you have multiple configuration values that are logically related (for example, settings for a third-party service), you can store them together as a structured JSON object within a single secret using`defineJsonSecret()`. This approach can help organize your configuration and make more efficient use of the Cloud Secret Manager free tier by storing a group of related configuration values in a single secret.

The value stored in Secret Manager must be a valid JSON string. The SDK will automatically parse the JSON string into a JavaScript object when you access`.value()`.

**Example:**  

    const { onRequest } = require('firebase-functions/v2/https');
    const { defineJsonSecret } = require('firebase-functions/params');

    // Define a single secret to hold all configuration for some API
    const someApiConfig = defineJsonSecret('SOMEAPI_CONFIG');

    exports.myApi = onRequest(
      { secrets: [someApiConfig] },
      (req, res) => {
        // someApiConfig.value() automatically parses the JSON secret
        const { apiKey, webhookSecret, clientId } = someApiConfig.value();

        // Now you can use apiKey, webhookSecret, clientId
        // ...
      }
    );

To create the`SOMEAPI_CONFIG`secret, you would set its value in Secret Manager to a JSON string like:  

    {
      "apiKey": "key_...",
      "webhookSecret": "secret_...",
      "clientId": "client_..."
    }

If the secret value is not valid JSON, accessing`someApiConfig.value()`will throw an error at runtime.

## Environment variables

Cloud Functions for Firebasesupports the[dotenv](https://www.npmjs.com/package/dotenv)file format for loading environment variables specified in a`.env`file to your application runtime. Once deployed, the environment variables can be read via the[`process.env`](https://nodejs.org/docs/latest-v16.x/api/process.html#processenv)interface (in Node.js-based projects) or[`os.environ`](https://docs.python.org/3/library/os.html#os.environ)(in Python-based projects).
| **Note:** If you prefer a flow in which function deployment is blocked when any values are missing from your environment configuration, consider using[parameterized configuration](https://firebase.google.com/docs/functions/config-env#params).

To configure your environment this way, create a`.env`file in your project, add the desired variables, and deploy:

1. Create a`.env`file in your`functions/`directory:

       # Directory layout:
       #   my-project/
       #     firebase.json
       #     functions/
       # .env
       #       package.json
       #       index.js

2. Open the`.env`file for edit, and add the desired keys. For example:

       PLANET=Earth
       AUDIENCE=Humans

3. Deploy functions and verify that environment variables were loaded:

   ```
   firebase deploy --only functions
   # ...
   # i functions: Loaded environment variables from .env.
   # ...
   ```

Once your your custom environment variables are deployed, your function code can access them:  

### Node.js

    // Responds with "Hello Earth and Humans"
    exports.hello = onRequest((request, response) => {
      response.send(`Hello ${process.env.PLANET} and ${process.env.AUDIENCE}`);
    });

### Python

    import os

    @https_fn.on_request()
    def hello(req):
        return https_fn.Response(
            f"Hello {os.environ.get('PLANET')} and {os.environ.get('AUDIENCE')}"
        )

### Deploying multiple sets of environment variables

If you need an alternative set of environment variables for your Firebase projects (such as staging vs production), create a`.env.`**<project or
[alias](https://firebase.google.com/docs/cli#project_aliases)>**file and write your project-specific environment variables there. The environment variables from`.env`and project-specific`.env`files (if they exist) will be included in all deployed functions.

For example, a project could include these three files containing slightly different values for development and production:

|------------------------------|---------------------|----------------------|
| `.env`                       | `.env.dev`          | `.env.prod`          |
| PLANET=Earth AUDIENCE=Humans | AUDIENCE=Dev Humans | AUDIENCE=Prod Humans |

Given the values in those separate files, the set of environment variables deployed with your functions will vary depending on your target project:  

    $ firebase use dev
    $ firebase deploy --only functions
    i functions: Loaded environment variables from .env, .env.dev.
    # Deploys functions with following user-defined environment variables:
    #   PLANET=Earth
    #   AUDIENCE=Dev Humans

    $ firebase use prod
    $ firebase deploy --only functions
    i functions: Loaded environment variables from .env, .env.prod.
    # Deploys functions with following user-defined environment variables:
    #   PLANET=Earth
    #   AUDIENCE=Prod Humans

### Reserved environment variables

Some environment variable keys are reserved for internal use. Do not use any of these keys in your`.env`files:

- All keys starting with X_GOOGLE_
- All keys starting EXT_
- All keys starting with FIREBASE_
- Any key from the following list:
- CLOUD_RUNTIME_CONFIG
- ENTRY_POINT
- GCP_PROJECT
- GCLOUD_PROJECT
- GOOGLE_CLOUD_PROJECT
- FUNCTION_TRIGGER_TYPE
- FUNCTION_NAME
- FUNCTION_MEMORY_MB
- FUNCTION_TIMEOUT_SEC
- FUNCTION_IDENTITY
- FUNCTION_REGION
- FUNCTION_TARGET
- FUNCTION_SIGNATURE_TYPE
- K_SERVICE
- K_REVISION
- PORT
- K_CONFIGURATION

### Store and access sensitive configuration information

Environment variables stored in`.env`files can be used for function configuration, but you should not consider them a secure way to store sensitive information such as database credentials or API keys. This is especially important if you check your`.env`files into source control.

To help you store sensitive configuration information,Cloud Functions for Firebaseintegrates withGoogle Cloud[Secret Manager](https://cloud.google.com/secret-manager). This encrypted service stores configuration values securely, while still allowing easy access from your functions when needed.
| **Note:** Secret Manageris a paid service, with a free tier. See[How secrets are billed](https://firebase.google.com/docs/functions/config-env#secrets-billing)for more information.

#### Create and use a secret

To create a secret, use theFirebaseCLI.
| **Note:** Make sure not to use any[reserved environment variable names](https://firebase.google.com/docs/functions/config-env#reserved-names)for your secrets.

**To create and use a secret:**

1. From the root of your local project directory, run the following command:

   ```
   firebase functions:secrets:set SECRET_NAME
   ```

   <br />

2. Enter a value for<var translate="no">SECRET_NAME</var>.

   The CLI echoes a success message and warns that you must deploy functions for the change to take effect.
3. Before deploying, make sure your functions code allows the function to access the secret using the`secrets`option:

   ### Node.js

   ```
   const { onRequest } = require('firebase-functions/v2/https');

   exports.processPayment = onRequest(
     { secrets: ["SECRET_NAME"] },
     (req, res) => {
       const myBillingService = initializeBillingService(
         // reference the secret value
         process.env.SECRET_NAME
       );
       // Process the payment
     }
   );
   ```

   ### Python

       import os
       from firebase_functions import https_fn

       @https_fn.on_request(secrets=["SECRET_NAME"])
       def process_payment(req):
           myBillingService = initialize_billing(key=os.environ.get('SECRET_NAME'))
           # Process the payment
           ...

4. DeployCloud Functions:

   ```
   firebase deploy --only functions
   ```

   Now you'll be able to access it like any other environment variable. Conversely, if another function that does not specify the secret tries to access the secret, it receives an undefined value:  

   ### Node.js

       exports.anotherEndpoint = onRequest((request, response) => {
         response.send(`The secret API key is ${process.env.SECRET_NAME}`);
         // responds with "The secret API key is undefined" because the `secrets` option is missing
       });

   ### Python

       @https_fn.on_request()
       def another_endpoint(req):
           return https_fn.Response(f"The secret API key is {os.environ.get("SECRET_NAME")}")
           # Responds with "The secret API key is None" because the `secrets` parameter is missing.

Once your function is deployed, it will have access to the secret value.*Only* functions that specifically include a secret in their`secrets`option will have access to that secret as an environment variable. This helps you make sure that secret values are only available where they're needed, reducing the risk of accidentally leaking a secret.

#### Managing secrets

Use theFirebaseCLI to manage your secrets. While managing secrets this way, keep in mind that some CLI changes require you to modify and/or redeploy associated functions. Specifically:

- Whenever you set a new value for a secret, you must redeploy all functions that reference that secret for them to pick up the latest value.
- If you delete a secret, make sure that none of your deployed functions references that secret. Functions that use a secret value that has been deleted will fail silently.

Here's a summary of theFirebaseCLI commands for secret management:  

```
# Change the value of an existing secret
firebase functions:secrets:set SECRET_NAME

# Set secret from file
firebase functions:secrets:set SECRET_NAME --data-file file.json

# Validate secret value as json
cat file.json | firebase functions:secrets:set SECRET_NAME --format=json

# Pipe from stdin and set secret
cat file.json | firebase functions:secrets:set SECRET_NAME --format=json

# View the value of a secret
functions:secrets:access SECRET_NAME

# Destroy a secret
functions:secrets:destroy SECRET_NAME

# View all secret versions and their state
functions:secrets:get SECRET_NAME

# Automatically clean up all secrets that aren't referenced by any of your functions
functions:secrets:prune
```

For the`access`and`destroy`commands, you can provide the optional version parameter to manage a particular version. For example:  

```
functions:secrets:access SECRET_NAME[@VERSION]
```

For more information about these operations, pass`-h`with the command to view CLI help.

#### How secrets are billed

Secret Managerallows 6 active secret[versions](https://cloud.google.com/secret-manager/docs/overview#version)at no cost. This means that you can have 6 secrets per month in a Firebase project at no cost.

By default, theFirebaseCLI attempts to automatically destroy unused secret versions where appropriate, such as when you deploy functions with a new version of the secret. Also, you can actively clean up unused secrets using`functions:secrets:destroy`and`functions:secrets:prune`.

Secret Managerallows 10,000 unbilled monthly access operations on a secret. Function instances read only the secrets specified in their`secrets`option every time they cold start. If you have a lot of function instances reading a lot of secrets, your project may exceed this allowance, at which point you'll be charged $0.03 per 10,000 access operations.

For more information, see[Secret ManagerPricing](https://cloud.google.com/secret-manager/pricing).

## Emulator support

Environment configuration with dotenv is designed to interoperate with a local[Cloud Functionsemulator](https://firebase.google.com/docs/emulator-suite/connect_functions).

When using a localCloud Functionsemulator, you can override environment variables for your project by setting up a`.env.local`file. Contents of`.env.local`take precedence over`.env`and the project-specific`.env`file.

For example, a project could include these three files containing slightly different values for development and local testing:

|------------------------------|---------------------|-----------------------|
| `.env`                       | `.env.dev`          | `.env.local`          |
| PLANET=Earth AUDIENCE=Humans | AUDIENCE=Dev Humans | AUDIENCE=Local Humans |

When started in the local context, the emulator loads the environment variables as shown:  

      $ firebase emulators:start
      i  emulators: Starting emulators: functions
      # Starts emulator with following environment variables:
      #  PLANET=Earth
      #  AUDIENCE=Local Humans

### Secrets and credentials in theCloud Functionsemulator

TheCloud Functionsemulator supports the use of secrets to[store and access sensitive configuration information](https://firebase.google.com/docs/functions/config-env#create-secret). By default, the emulator will try to access your production secrets using[application default credentials](https://cloud.google.com/docs/authentication/production). In certain situations like CI environments, the emulator may fail to access secret values due to permission restrictions.

Similar toCloud Functionsemulator support for environment variables, you can override secrets values by setting up a`.secret.local`file. This makes it easy for you to test your functions locally, especially if you don't have access to the secret value.

## Migrate from runtime configuration

If you have been using environment configuration with`functions.config`,**you must migrate your existing configuration to a supported format before the end of 2025, when`functions.config`will be decommissioned.** After December 2025, new deployments with`functions.config`will fail.

For most use cases, parameterized configuration is recommended. This approach makes configuration values available both at runtime and deploy time, and deployment is blocked unless all parameters have a valid value.

### Migrate to the`params`subpackage

If you have been using environment configuration with`functions.config`, you can migrate your existing configuration by refactoring it as[parameterized configuration](https://firebase.google.com/docs/functions/config-env#params). For example:

**Before: 1st gen**  

    const functions = require("firebase-functions/v1");

    exports.date = functions.https.onRequest((req, res) => {
      const date = new Date();
      const formattedDate =
    date.toLocaleDateString(functions.config().dateformat);

      // ...
    });

**After: 2nd gen**  

    const {onRequest} = require("firebase-functions/v2/https");
    const {defineString} = require("firebase-functions/params");

    const dateFormat = defineString("DATE_FORMAT");

    exports.date = onRequest((req, res) => {
      const date = new Date();
      const formattedDate = date.toLocaleDateString(dateFormat.value());

      // ...
    });

### Migrating Nested Configuration

If your`functions.config()`usage involved nested objects, the`defineJsonSecret`parameter type offers a straightforward migration path. You can store the entire JSON structure from`functions.config()`directly in a single secret.

For example, if you had:

**Before: 1st gen**  

    const functions = require("firebase-functions/v1");

    exports.myFunction = functions.https.onRequest((req, res) => {
      const apiKey = functions.config().someapi.key;
      const webhookSecret = functions.config().someapi.webhookSecret;
      // ...
    });

You can migrate by storing the entire`someapi`object as a JSON string in a secret named`SOMEAPI_CONFIG`and use`defineJsonSecret`:

**After: 2nd gen**  

    const {onRequest} = require("firebase-functions/v2/https");
    const {defineJsonSecret} = require("firebase-functions/params");

    const someApiConfig = defineJsonSecret("SOMEAPI_CONFIG");

    exports.myFunction = onRequest(<mark>{ secrets: [someApiConfig] }</mark>, (req, res) => {
      const apiKey = someApiConfig.value().key;
      const webhookSecret = someApiConfig.value().webhookSecret;
      // ...
    });

Note that, unlike`functions.config()`, any secret defined with`defineSecret`or`defineJsonSecret`must be explicitly bound to the function using the`{
secrets: [...] }`option to be accessible at runtime.

This preserves the configuration structure and minimizes code changes. You can use the Firebase CLI to help export your existing`functions.config()`JSON and set it as the value for the new secret. See[Managing secrets](https://firebase.google.com/docs/functions/config-env?gen=2nd#managing_secrets)for instructions on setting secret values, including how to set JSON secrets from a file or stdin.

### Set parameter values

The first time you deploy, the Firebase CLI prompts for all values of parameters, and save the values in a dotenv file. To export your`functions.config`values, run`firebase functions:config:export`.

For additional safety, you can also specify parameter[types](https://firebase.google.com/docs/functions/config-env?gen=2nd#parameter_types)and[validation rules](https://firebase.google.com/docs/functions/config-env?gen=2nd#configure_behavior).

### Special case: API Keys

The`params`module integrates with Cloud Secret Manager, which provides fine-grained access control to sensitive values like API keys. See[secret parameters](https://firebase.google.com/docs/functions/config-env?gen=2nd#secret-parameters)and[Structured JSON Secrets](https://firebase.google.com/docs/functions/config-env?gen=2nd#json-secrets)for more information.

## Automatically populated environment variables

There are environment variables that are automatically populated in the functions runtime and in locally emulated functions. These include[those populated byGoogle Cloud](https://cloud.google.com/functions/docs/configuring/env-var#nodejs_10_and_subsequent_runtimes), as well as a Firebase-specific environment variable:

`process.env.FIREBASE_CONFIG`: Provides the following Firebase project config info:  

    {
      databaseURL: 'https://<var translate="no">DATABASE_NAME</var>.firebaseio.com',
      storageBucket: '<var translate="no">PROJECT_ID</var>`.firebasestorage.app`',
      projectId: '<var translate="no">PROJECT_ID</var>'
    }

Note that the values in your actual Firebase configuration might vary depending on the resources you've provisioned in your project.

This configuration is applied automatically when you initialize the Firebase Admin SDK with no arguments. If you are writing functions in JavaScript, initialize like this:  

    const admin = require('firebase-admin');
    admin.initializeApp();

If you are writing functions in TypeScript, initialize like this:  

    import * as functions from 'firebase-functions/v1';
    import * as admin from 'firebase-admin';
    import 'firebase-functions/v1';
    admin.initializeApp();

If you need to initialize the Admin SDK with the default project configuration using service account credentials, you can load the credentials from a file and add them to`FIREBASE_CONFIG`like this:  

    serviceAccount = require('./serviceAccount.json');

    const adminConfig = JSON.parse(process.env.FIREBASE_CONFIG);
    adminConfig.credential = admin.credential.cert(serviceAccount);
    admin.initializeApp(adminConfig);