# Source: https://firebase.google.com/docs/admin/setup.md.txt

The Admin SDK is a set of server libraries that lets you interact with
Firebase from privileged environments to perform actions like:

- Perform queries and mutations on a Firebase Data Connect service for bulk data management and other operations with full admin privileges.
- Read and write Realtime Database data with full admin privileges.
- Programmatically send Firebase Cloud Messaging messages using a simple, alternative approach to the Firebase Cloud Messaging server protocols.
- Generate and verify Firebase auth tokens.
- Access Google Cloud resources like Cloud Storage buckets and Cloud Firestore databases associated with your Firebase projects.
- Create your own simplified admin console to do things like look up user data or change a user's email address for authentication.

If you are interested in using the Node.js SDK as a client for end-user access
(for example, in a Node.js desktop or IoT application), as opposed to admin
access from a privileged environment (like a server), you should instead follow
the [instructions for setting up the client JavaScript SDK](https://firebase.google.com/docs/web/setup).

Here is a feature matrix showing what Firebase features are supported in each
language:

| Feature | Node.js | Java | Python | Go | C# |
|---|:---:|:---:|:---:|:--:|:--:|
| [Custom Token Minting](https://firebase.google.com/docs/auth/admin/create-custom-tokens) |   |   |   |   |   |
| [ID Token Verification](https://firebase.google.com/docs/auth/admin/verify-id-tokens) |   |   |   |   |   |
| [User Management](https://firebase.google.com/docs/auth/admin/manage-users) |   |   |   |   |   |
| [Control Access With Custom Claims](https://firebase.google.com/docs/auth/admin/custom-claims) |   |   |   |   |   |
| [Refresh Token Revocation](https://firebase.google.com/docs/auth/admin/manage-sessions) |   |   |   |   |   |
| [Import Users](https://firebase.google.com/docs/auth/admin/import-users) |   |   |   |   |   |
| [Session Cookie Management](https://firebase.google.com/docs/auth/admin/manage-cookies) |   |   |   |   |   |
| [Generating Email Action Links](https://firebase.google.com/docs/auth/admin/email-action-links) |   |   |   |   |   |
| [Managing SAML/OIDC provider configurations](https://cloud.google.com/identity-cp/docs/managing-providers-programmatically) |   |   |   |   |   |
| [Multi-tenancy support](https://cloud.google.com/identity-platform/docs/multi-tenancy) |   |   |   |   |   |
| [Firebase Data Connect](https://firebase.google.com/docs/data-connect/admin-sdk) |   |   |   |   |   |
| [Realtime Database](https://firebase.google.com/docs/database/admin/start) |   |   |   | \* |   |
| [Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/server#firebase-admin-sdk-for-fcm) |   |   |   |   |   |
| [FCM Multicast](https://firebase.google.com/docs/cloud-messaging/send/admin-sdk#send-messages-to-multiple-devices) |   |   |   |   |   |
| [Manage FCM Topic Subscriptions](https://firebase.google.com/docs/cloud-messaging/manage-topics) |   |   |   |   |   |
| [Cloud Storage](https://firebase.google.com/docs/storage/admin/start) |   |   |   |   |   |
| [Cloud Firestore](https://firebase.google.com/docs/firestore) |   |   |   |   |   |
| [Enqueue functions with Cloud Tasks](https://firebase.google.com/docs/functions/task-functions) |   |   |   |   |   |
| Project Management |   |   |   |   |   |
| [Security Rules](https://firebase.google.com/docs/rules/manage-deploy) |   |   |   |   |   |
| [ML Model Management](https://firebase.google.com/docs/ml/manage-hosted-models) |   |   |   |   |   |
| [Firebase Remote Config](https://firebase.google.com/docs/remote-config/automate-rc) |   |   |   |   |   |
| [Firebase App Check](https://firebase.google.com/docs/app-check/custom-provider) |   |   |   |   |   |
| [Firebase Extensions](https://firebase.google.com/docs/extensions/publishers/lifecycle-events) |   |   |   |   |

> [!NOTE]
> **Note:** The Realtime Database API in the Go Admin SDK currently does not support realtime event listeners. This means there is no provision for adding event listeners to a database reference in order to automatically receive realtime update notifications. Instead, in Go, updates should be proactively fetched by explicitly invoking read operations.

To learn more about Admin SDK integration for these uses, see the corresponding
[Realtime Database](https://firebase.google.com/docs/database/admin/start),
[FCM](https://firebase.google.com/docs/cloud-messaging/server#firebase-admin-sdk-for-fcm),
[Authentication](https://firebase.google.com/docs/auth/admin),
[Remote Config](https://firebase.google.com/docs/remote-config/automate-rc#modify_remote_config_using_the_firebase_admin_sdk),
and [Cloud Storage](https://firebase.google.com/docs/storage/admin/start) documentation.
The rest of this page focuses on basic setup for the Admin SDK.

## Prerequisites

- Make sure that you have a server app.

- Make sure that your server runs the following depending on which Admin SDK
  that you use:

  - Admin Node.js SDK --- Node.js 18+ (recommend Node.js 20+)  
    Node.js 18 support is deprecated.
  - Admin Java SDK --- Java 8+
  - Admin Python SDK --- Python 3.9+ (recommend Python 3.10+)  
    Python 3.9 support is deprecated.
  - Admin Go SDK --- Go 1.23+
  - Admin .NET SDK --- .NET Framework 4.6.2+ or .NET Standard 2.0 or .NET 6.0+ (recommend .NET 8.0+)  
    .NET 6.0 and 7.0 support is deprecated.

## Set up a Firebase project and service account

To use the Firebase Admin SDK, you'll need the following:

- A Firebase project.
- A Firebase Admin SDK service account to communicate with Firebase. This service account is created automatically when you create a Firebase project or add Firebase to a Google Cloud project.
- A configuration file with your service account's credentials.

If you don't already have a Firebase project, you need to create one in the
[Firebase console](https://console.firebase.google.com/). Visit
[Understand Firebase Projects](https://firebase.google.com/docs/projects/learn-more) to learn more about
Firebase projects.
**Create a Firebase project**

### New to Firebase or Cloud


Follow these steps if you're new to Firebase or Google Cloud.  

You can also follow these steps if you want to create a wholly new
Firebase project (and its underlying Google Cloud project).

1. Sign into the [Firebase console](https://console.firebase.google.com/).
2. Click the button to create a new Firebase project.
3. In the text field, enter a **project name**.

   If you're part of a Google Cloud org, you can optionally select which
   folder you create your project in.

   > [!CAUTION]
   > Your project name is used as a display name in Firebase interfaces, and Firebase auto-creates a unique project ID based on this project name. Note that you can optionally click the **Edit** icon now to set your preferred project ID, but you cannot change this ID after project creation. Learn about [how Firebase uses the
   > project ID](https://firebase.google.com/docs/projects/learn-more#project-id).

4. If prompted, review and accept the [Firebase terms](https://firebase.google.com/terms), then click **Continue**.
5. *(Optional)* Enable AI assistance in the Firebase console (called "Gemini in Firebase"), which can help you get started and streamline your development process.
6. *(Optional)* Set up Google Analytics for your project,
   which enables an optimal experience using these Firebase products:
   [Firebase A/B Testing](https://firebase.google.com/docs/ab-testing),
   [Cloud Messaging](https://firebase.google.com/docs/cloud-messaging),
   [Crashlytics](https://firebase.google.com/docs/crashlytics),
   [In-App Messaging](https://firebase.google.com/docs/in-app-messaging), and
   [Remote Config](https://firebase.google.com/docs/remote-config)
   (including
   [Personalization](https://firebase.google.com/docs/remote-config/personalization)).

   Either select an existing
   [Google Analytics account](https://support.google.com/analytics/answer/1009618)
   or create a new account. If you create a new account, select your
   [Analytics reporting location](https://firebase.google.com/docs/projects/locations),
   then accept the data sharing settings and Google Analytics terms
   for your project.

   > [!NOTE]
   > You can always set up Google Analytics later in the [*Integrations* tab](https://console.firebase.google.com/project/_/settings/integrations) of your *Project settings*.

7. Click **Create project**.

Firebase creates your project, provisions some initial resources, and
enables important APIs. When the process completes, you'll be taken to the
overview page for your Firebase project in the Firebase console.

### Existing Cloud project


Follow these steps if you want to start using Firebase with an existing
Google Cloud project. Learn more about and troubleshoot
["adding
Firebase" to an existing Google Cloud project](https://firebase.google.com/docs/projects/use-firebase-with-existing-cloud-project).

1. Sign into the [Firebase console](https://console.firebase.google.com/) with the account that gives you access to the existing Google Cloud project.
2. Click the button to create a new Firebase project.
3. At the bottom of the page, click **Add Firebase to Google Cloud project**.
4. In the text field, start entering the **project name** of the existing project, and then select the project from the displayed list.
5. Click **Open project**.
6. If prompted, review and accept the [Firebase terms](https://firebase.google.com/terms), then click **Continue**.
7. *(Optional)* Enable AI assistance in the Firebase console (called "Gemini in Firebase"), which can help you get started and streamline your development process.
8. *(Optional)* Set up Google Analytics for your project,
   which enables an optimal experience using these Firebase products:
   [Firebase A/B Testing](https://firebase.google.com/docs/ab-testing),
   [Cloud Messaging](https://firebase.google.com/docs/cloud-messaging),
   [Crashlytics](https://firebase.google.com/docs/crashlytics),
   [In-App Messaging](https://firebase.google.com/docs/in-app-messaging), and
   [Remote Config](https://firebase.google.com/docs/remote-config)
   (including
   [Personalization](https://firebase.google.com/docs/remote-config/personalization)).

   Either select an existing
   [Google Analytics account](https://support.google.com/analytics/answer/1009618)
   or create a new account. If you create a new account, select your
   [Analytics reporting location](https://firebase.google.com/docs/projects/locations),
   then accept the data sharing settings and Google Analytics terms
   for your project.

   > [!NOTE]
   > You can always set up Google Analytics later in the [*Integrations* tab](https://console.firebase.google.com/project/_/settings/integrations) of your *Project settings*.

9. Click **Add Firebase**.

Firebase
[adds
Firebase to your existing project](https://firebase.google.com/docs/projects/use-firebase-with-existing-cloud-project#faq_what-happens-when-add-firebase).
When the process completes, you'll be taken to the overview page for your
Firebase project in the Firebase console.

## Add the SDK

If you are setting up a new project, you need to install the SDK for the
language of your choice.

### Node.js

The Firebase Admin Node.js SDK is available on npm. If you don't already
have a `package.json` file, create one via `npm init`. Next, install the
`firebase-admin` npm package and save it to your `package.json`:

```
npm install firebase-admin --save
```

To use the module in your application, `require` it from any JavaScript
file:

    const { initializeApp } = require('firebase-admin/app');

If you are using ES2015, you can `import` the module:

    import { initializeApp } from 'firebase-admin/app';

### Java

The Firebase Admin Java SDK is published to the Maven central repository.
To install the library, declare it as a dependency in your `build.gradle`
file:

    dependencies {
      implementation 'com.google.firebase:firebase-admin:9.8.0'
    }

If you use Maven to build your application, you can add the following
dependency to your `pom.xml`:

    <dependency>
      <groupId>com.google.firebase</groupId>
      <artifactId>firebase-admin</artifactId>
      <version>9.8.0</version>
    </dependency>

### Python

The Firebase Admin Python SDK is available via
[pip](https://pypi.python.org/pypi/pip).
You can install the library for all users via `sudo`:

```
sudo pip install firebase-admin
```

Or, you can install the library for just the current user by passing the `--user` flag:

```
pip install --user firebase-admin
```

### Go

The Go Admin SDK can be installed using the `go get` utility:

    # Install the latest version:
    go get firebase.google.com/go/v4@latest

    # Or install a specific version:
    go get firebase.google.com/go/v4@4.19.0

### C#

The .NET Admin SDK can be installed using the .NET package manager:

```
Install-Package FirebaseAdmin -Version 3.4.0
```

Alternatively, install it using the `dotnet` command-line utility:

```
dotnet add package FirebaseAdmin --version 3.4.0
```

Or, you can install it by adding the following package reference entry to
your `.csproj` file:

    <ItemGroup>
      <PackageReference Include="FirebaseAdmin" Version="3.4.0" />
    </ItemGroup>

## Initialize the SDK

Once you have created a Firebase project, you can initialize the SDK with
[Google Application Default Credentials](https://cloud.google.com/docs/authentication/production#providing_credentials_to_your_application).
Because default credentials lookup is fully automated in Google environments,
with no need to supply environment variables or other configuration, this way of
initializing the SDK is strongly recommended for applications running in Google
environments such as Firebase App Hosting, Cloud Run, App Engine, and
Cloud Functions for Firebase.

To optionally specify initialization options for services such as Realtime Database,
Cloud Storage, or Cloud Functions, use the `FIREBASE_CONFIG`
environment variable. If the content of the `FIREBASE_CONFIG` variable begins
with a `{` it will be parsed as a JSON object. Otherwise the SDK assumes that
the string is the path of a JSON file containing the options.

> [!NOTE]
> **Note:** The `FIREBASE_CONFIG` environment variable is included automatically in App Hosting backends and Cloud Functions for Firebase functions.

### Node.js

    const app = initializeApp();

### Java

    FirebaseApp.initializeApp();

### Python

    default_app = firebase_admin.initialize_app()

### Go

    app, err := firebase.NewApp(context.Background(), nil)
    if err != nil {
    	log.Fatalf("error initializing app: %v\n", err)
    }https://github.com/firebase/firebase-admin-go/blob/4f7026f0837678ceb33ab2d2c145a0d18d9952fd/snippets/init.go#L60-L63

### C#

    FirebaseApp.Create();

Once it is initialized, you can use the Admin SDK to accomplish
the following types of tasks:

- [Implement custom authentication](https://firebase.google.com/docs/auth/admin)
- [Manage your Firebase Authentication users](https://firebase.google.com/docs/auth/admin/manage-users)
- [Perform administrative queries and mutations on a Firebase Data Connect
  service](https://firebase.google.com/docs/data-connect/admin-sdk).
- [Read and write data from the Realtime Database](https://firebase.google.com/docs/database/admin/start)
- [Send Firebase Cloud Messaging
  messages](https://firebase.google.com/docs/cloud-messaging/admin/send-messages)

### Using an OAuth 2.0 refresh token

The Admin SDK also provides a credential which allows you to authenticate
with a [Google OAuth2](https://developers.google.com/identity/protocols/OAuth2)
refresh token:

### Node.js

    const myRefreshToken = '...'; // Get refresh token from OAuth2 flow

    initializeApp({
      credential: refreshToken(myRefreshToken),
      databaseURL: 'https://<DATABASE_NAME>.firebaseio.com'
    });

### Java

    FileInputStream refreshToken = new FileInputStream("path/to/refreshToken.json");

    FirebaseOptions options = FirebaseOptions.builder()
        .setCredentials(GoogleCredentials.fromStream(refreshToken))
        .setDatabaseUrl("https://<DATABASE_NAME>.firebaseio.com/")
        .build();

    FirebaseApp.initializeApp(options);

### Python

    cred = credentials.RefreshToken('path/to/refreshToken.json')
    default_app = firebase_admin.initialize_app(cred)

### Go

    opt := option.WithCredentialsFile("path/to/refreshToken.json")
    config := &firebase.Config{ProjectID: "my-project-id"}
    app, err := firebase.NewApp(context.Background(), config, opt)
    if err != nil {
    	log.Fatalf("error initializing app: %v\n", err)
    }https://github.com/firebase/firebase-admin-go/blob/4f7026f0837678ceb33ab2d2c145a0d18d9952fd/snippets/init.go#L47-L52

### C#

    FirebaseApp.Create(new AppOptions()
    {
        Credential = GoogleCredential.FromFile("path/to/refreshToken.json"),
    });

> [!NOTE]
> **Note:** OAuth 2.0 refresh tokens are not supported for connecting to Cloud Firestore.

### Initialize the SDK in non-Google environments

If you are working in a non-Google server environment in which default
credentials lookup can't be fully automated, you can initialize the SDK
with an exported service account key file.

> [!IMPORTANT]
> **Important:** Extremely high security awareness is required when working with service account keys, as they are vulnerable to certain types of threats. See [Best practices for managing service account keys](https://cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).

Firebase projects support Google
[service accounts](https://console.firebase.google.com/project/_/settings/serviceaccounts/adminsdk),
which you can use to call Firebase
server APIs from your app server or trusted environment. If you're developing
code locally or deploying your application on-premises,
you can use credentials obtained
via this service account to authorize server requests.

To authenticate a service account and authorize it
to access Firebase services, you must generate a private key file in JSON
format.

**To generate a private key file for your service account:**

1. In the Firebase console, open
   **Settings \> [Service Accounts](https://console.firebase.google.com/project/_/settings/serviceaccounts/adminsdk)**.

2. Click **Generate New Private Key** , then confirm by clicking **Generate Key**.

3. Securely store the JSON file containing the key.

When authorizing via a service account, you have two choices for providing the
credentials to your application. You can either set the
<var translate="no">GOOGLE_APPLICATION_CREDENTIALS</var> environment variable, or you can
explicitly pass the path to the service account key in code.
The first option is more secure and is strongly recommended.

**To set the environment variable:**

Set the environment variable <var translate="no">GOOGLE_APPLICATION_CREDENTIALS</var>
to the file path of the JSON file that contains your service account key.
This variable only applies to your current shell session, so if you open
a new session, set the variable again.

### Linux or macOS

    export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/service-account-file.json"

### Windows

With PowerShell:

    $env:GOOGLE_APPLICATION_CREDENTIALS="C:\Users\username\Downloads\service-account-file.json"

After you've completed the above steps, Application Default Credentials (ADC)
is able to implicitly determine your credentials, allowing you to use service
account credentials when testing or running in non-Google environments.

Initialize the SDK as shown:

### Node.js

    initializeApp({
        credential: applicationDefault(),
        databaseURL: 'https://<DATABASE_NAME>.firebaseio.com'
    });

### Java

    FirebaseOptions options = FirebaseOptions.builder()
        .setCredentials(GoogleCredentials.getApplicationDefault())
        .setDatabaseUrl("https://<DATABASE_NAME>.firebaseio.com/")
        .build();

    FirebaseApp.initializeApp(options);

### Python

    default_app = firebase_admin.initialize_app()

### Go

    app, err := firebase.NewApp(context.Background(), nil)
    if err != nil {
    	log.Fatalf("error initializing app: %v\n", err)
    }https://github.com/firebase/firebase-admin-go/blob/4f7026f0837678ceb33ab2d2c145a0d18d9952fd/snippets/init.go#L60-L63

### C#

    FirebaseApp.Create(new AppOptions()
    {
        Credential = GoogleCredential.GetApplicationDefault(),
        ProjectId = "my-project-id",
    });
    https://github.com/firebase/firebase-admin-dotnet/blob/9d71ceb37ed2deaf22aed643d1dcfed759df9f9d/FirebaseAdmin/FirebaseAdmin.Snippets/FirebaseAppSnippets.cs#L48-L52

> [!NOTE]
> **Note:** Initialization options such as `databaseURL` shown in the code examples on this page are not strictly required to initialize the SDK. Depending on your deployment environment and the target use case, you can choose to specify only the options you need.

## Initialize multiple apps

In most cases, you only have to initialize a single, default app. You can
access services off of that app in two equivalent ways:

### Node.js

    // Initialize the default app
    const defaultApp = initializeApp(defaultAppConfig);

    console.log(defaultApp.name);  // '[DEFAULT]'

    // Retrieve services via the defaultApp variable...
    let defaultAuth = getAuth(defaultApp);
    let defaultDatabase = getDatabase(defaultApp);

    // ... or use the equivalent shorthand notation
    defaultAuth = getAuth();
    defaultDatabase = getDatabase();

### Java

    // Initialize the default app
    FirebaseApp defaultApp = FirebaseApp.initializeApp(defaultOptions);

    System.out.println(defaultApp.getName());  // "[DEFAULT]"

    // Retrieve services by passing the defaultApp variable...
    FirebaseAuth defaultAuth = FirebaseAuth.getInstance(defaultApp);
    FirebaseDatabase defaultDatabase = FirebaseDatabase.getInstance(defaultApp);

    // ... or use the equivalent shorthand notation
    defaultAuth = FirebaseAuth.getInstance();
    defaultDatabase = FirebaseDatabase.getInstance();

### Python

    # Import the Firebase service
    from firebase_admin import auth

    # Initialize the default app
    default_app = firebase_admin.initialize_app(cred)
    print(default_app.name)  # "[DEFAULT]"

    # Retrieve services via the auth package...
    # auth.create_custom_token(...)

### Go

    // Initialize default app
    app, err := firebase.NewApp(context.Background(), nil)
    if err != nil {
    	log.Fatalf("error initializing app: %v\n", err)
    }

    // Access auth service from the default app
    client, err := app.Auth(context.Background())
    if err != nil {
    	log.Fatalf("error getting Auth client: %v\n", err)
    }https://github.com/firebase/firebase-admin-go/blob/4f7026f0837678ceb33ab2d2c145a0d18d9952fd/snippets/init.go#L84-L94

### C#

    // Initialize the default app
    var defaultApp = FirebaseApp.Create(new AppOptions()
    {
        Credential = GoogleCredential.GetApplicationDefault(),
    });
    Console.WriteLine(defaultApp.Name); // "[DEFAULT]"

    // Retrieve services by passing the defaultApp variable...
    var defaultAuth = FirebaseAuth.GetAuth(defaultApp);

    // ... or use the equivalent shorthand notation
    defaultAuth = FirebaseAuth.DefaultInstance;

Some use cases require you to create multiple apps at the same time. For
example, you might want to read data from the Realtime Database of one Firebase
project and mint custom tokens for another project. Or you might want to
authenticate two apps with separate credentials. The Firebase SDK allows you
create multiple apps at the same time, each with their own configuration
information.

### Node.js

    // Initialize the default app
    initializeApp(defaultAppConfig);

    // Initialize another app with a different config
    var otherApp = initializeApp(otherAppConfig, 'other');

    console.log(getApp().name);  // '[DEFAULT]'
    console.log(otherApp.name);     // 'other'

    // Use the shorthand notation to retrieve the default app's services
    const defaultAuth = getAuth();
    const defaultDatabase = getDatabase();

    // Use the otherApp variable to retrieve the other app's services
    const otherAuth = getAuth(otherApp);
    const otherDatabase = getDatabase(otherApp);

### Java

    // Initialize the default app
    FirebaseApp defaultApp = FirebaseApp.initializeApp(defaultOptions);

    // Initialize another app with a different config
    FirebaseApp otherApp = FirebaseApp.initializeApp(otherAppConfig, "other");

    System.out.println(defaultApp.getName());  // "[DEFAULT]"
    System.out.println(otherApp.getName());    // "other"

    // Use the shorthand notation to retrieve the default app's services
    FirebaseAuth defaultAuth = FirebaseAuth.getInstance();
    FirebaseDatabase defaultDatabase = FirebaseDatabase.getInstance();

    // Use the otherApp variable to retrieve the other app's services
    FirebaseAuth otherAuth = FirebaseAuth.getInstance(otherApp);
    FirebaseDatabase otherDatabase = FirebaseDatabase.getInstance(otherApp);

### Python

    # Initialize the default app
    default_app = firebase_admin.initialize_app(cred)

    #  Initialize another app with a different config
    other_app = firebase_admin.initialize_app(cred, name='other')

    print(default_app.name)    # "[DEFAULT]"
    print(other_app.name)      # "other"

    # Retrieve default services via the auth package...
    # auth.create_custom_token(...)

    # Use the `app` argument to retrieve the other app's services
    # auth.create_custom_token(..., app=other_app)

### Go

    // Initialize the default app
    defaultApp, err := firebase.NewApp(context.Background(), nil)
    if err != nil {
    	log.Fatalf("error initializing app: %v\n", err)
    }

    // Initialize another app with a different config
    opt := option.WithCredentialsFile("service-account-other.json")
    otherApp, err := firebase.NewApp(context.Background(), nil, opt)
    if err != nil {
    	log.Fatalf("error initializing app: %v\n", err)
    }

    // Access Auth service from default app
    defaultClient, err := defaultApp.Auth(context.Background())
    if err != nil {
    	log.Fatalf("error getting Auth client: %v\n", err)
    }

    // Access auth service from other app
    otherClient, err := otherApp.Auth(context.Background())
    if err != nil {
    	log.Fatalf("error getting Auth client: %v\n", err)
    }https://github.com/firebase/firebase-admin-go/blob/4f7026f0837678ceb33ab2d2c145a0d18d9952fd/snippets/init.go#L102-L125

### C#

    // Initialize the default app
    var defaultApp = FirebaseApp.Create(defaultOptions);

    // Initialize another app with a different config
    var otherApp = FirebaseApp.Create(otherAppConfig, "other");

    Console.WriteLine(defaultApp.Name); // "[DEFAULT]"
    Console.WriteLine(otherApp.Name); // "other"

    // Use the shorthand notation to retrieve the default app's services
    var defaultAuth = FirebaseAuth.DefaultInstance;

    // Use the otherApp variable to retrieve the other app's services
    var otherAuth = FirebaseAuth.GetAuth(otherApp);

> [!NOTE]
> **Note:** Each app instance has its own configuration options and authentication state.

## Set scopes for Realtime Database and Authentication

If you're using a Google Compute Engine VM with [Google Application Default Credentials](https://cloud.google.com/docs/authentication/application-default-credentials)
for Realtime Database or Authentication, make sure to also set the right
[access scopes](https://cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#changeserviceaccountandscopes).
For Realtime Database and Authentication, you need scopes ending in `userinfo.email` and
either `cloud-platform` or `firebase.database`. To check the existing access
scopes and change them, run the following commands using
[gcloud](https://cloud.google.com/sdk/gcloud/).

### gcloud

    # Check the existing access scopes
    gcloud compute instances describe [INSTANCE_NAME] --format json

    # The above command returns the service account information. For example:
      "serviceAccounts": [
       {
        "email": "your.gserviceaccount.com",
        "scopes": [
         "https://www.googleapis.com/auth/cloud-platform",
         "https://www.googleapis.com/auth/userinfo.email"
         ]
        }
      ],

    # Stop the VM, then run the following command, using the service account
    # that gcloud returned when you checked the scopes.

    gcloud compute instances set-service-account [INSTANCE_NAME] --service-account "your.gserviceaccount.com" --scopes "https://www.googleapis.com/auth/firebase.database,https://www.googleapis.com/auth/userinfo.email"

## Testing with gcloud end user credentials

When testing the Admin SDK locally with
[Google Application Default Credentials](https://developers.google.com/identity/protocols/application-default-credentials)
obtained by running `gcloud auth application-default login`, additional
changes are needed to use Firebase Authentication due to the following:

- Firebase Authentication does not accept gcloud end user credentials generated using the gcloud OAuth client ID.
- Firebase Authentication requires the project ID to be provided on initialization for these type of end user credentials.

As a workaround, you can generate Google Application Default Credentials in
[gcloud](https://cloud.google.com/sdk/gcloud/) using your own
[OAuth 2.0 client ID](https://support.google.com/cloud/answer/6158849).
The OAuth client ID has to be a **Desktop app** application type.

### gcloud

    gcloud auth application-default login --client-id-file=[/path/to/client/id/file]

You can specify the project ID explicitly on app initialization or just use the
`GOOGLE_CLOUD_PROJECT` environment variable. The latter avoids the need to make
any additional changes to test your code.

To explicitly specify the project ID:

### Node.js

    import { initializeApp, applicationDefault } from 'firebase-admin/app';

    initializeApp({
      credential: applicationDefault(),
      projectId: '<FIREBASE_PROJECT_ID>',
    });

### Java

    FirebaseOptions options = FirebaseOptions.builder()
        .setCredentials(GoogleCredentials.getApplicationDefault())
        .setProjectId("<FIREBASE_PROJECT_ID>")
        .build();

    FirebaseApp.initializeApp(options);

### Python

    app_options = {'projectId': '<FIREBASE_PROJECT_ID>'}
    default_app = firebase_admin.initialize_app(options=app_options)

### Go

    config := &firebase.Config{ProjectID: "<FIREBASE_PROJECT_ID>"}
    app, err := firebase.NewApp(context.Background(), config)
    if err != nil {
            log.Fatalf("error initializing app: %v\n", err)
    }

### C#

    FirebaseApp.Create(new AppOptions()
    {
        Credential = GoogleCredential.GetApplicationDefault(),
        ProjectId = "<FIREBASE_PROJECT_ID>",
    });

## Next steps

Learn about Firebase:

- Explore [sample Firebase apps](https://firebase.google.com/docs/samples).

- Explore the open source code in GitHub for
  [Node.js](https://github.com/firebase/firebase-admin-node),
  [Java](https://github.com/firebase/firebase-admin-java),
  and [Python](https://github.com/firebase/firebase-admin-python).

- Read [Admin SDK-related blog posts](https://medium.com/@hiranya911) by one of
  the creators of the Admin SDK. For example:
  [Accessing Firestore and Firebase through a proxy server](https://medium.com/faun/firebase-accessing-firestore-and-firebase-through-a-proxy-server-c6c6029cddb1).

Add Firebase features to your app:

- Write a serverless backend with [Cloud Functions](https://firebase.google.com/docs/functions).
- Store info with [Realtime Database](https://firebase.google.com/docs/database) or blob data with [Cloud Storage](https://firebase.google.com/docs/storage).
- Receive notifications with [Cloud Messaging](https://firebase.google.com/docs/cloud-messaging).