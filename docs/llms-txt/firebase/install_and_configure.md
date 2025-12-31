# Source: https://firebase.google.com/docs/emulator-suite/install_and_configure.md.txt

<br />

The Firebase Local Emulator Suite can be installed and configured for different prototype and test environments, anything from one-off prototyping sessions to production-scale continuous integration workflows.

## Install the Local Emulator Suite

Before installing the Emulator Suite you will need:

- [Node.js](https://nodejs.org/en/download)version 16.0 or higher.
- [Java](https://jdk.java.net)JDK version 11 or higher.

To install the Emulator Suite:

1. Install the[FirebaseCLI](https://firebase.google.com/docs/cli). If you don't already have the Firebase CLI installed,[install it now](https://firebase.google.com/docs/cli#install_the_firebase_cli). You will need CLI version 8.14.0 or higher to use the Emulator Suite. You can check which version you have installed using the following command:  

   ```
   firebase --version
   ```
2. If you haven't already done so, initialize the current working directory as a Firebase project, following the onscreen prompts to specify which products to use:  

   ```
   firebase init
   ```
3. Set up the Emulator Suite. This command starts a configuration wizard that lets you select emulators of interest, download the corresponding emulator binary files, and set emulator ports if the defaults are not appropriate.  

   ```
   firebase init emulators
   ```

Once an emulator is installed, no update checks are performed and no additional automatic downloads will occur until you update your Firebase CLI version.

## Configure Emulator Suite

You can optionally configure the emulators' network ports and path to Security Rules definitions in the`firebase.json`file:

- Change emulator ports by running`firebase init emulators`or by editing`firebase.json`manually.
- Change the path to Security Rules definitions by editing`firebase.json`manually.

If you don't configure these settings, the emulators will listen on their default ports, and theCloud Firestore,Realtime DatabaseandCloud Storage for Firebaseemulators will run with open data security.

|      Command       |                                                                                                            Description                                                                                                             |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **init emulators** | Start an emulator initialization wizard. Identify emulators to be installed and optionally specify emulator port settings.`init emulators`is non-destructive; accepting defaults will preserve the current emulator configuration. |

### Port configuration

Each emulator binds to a different port on your machine with a preferred default value.

|        **Emulator**        | **Default Port** |
|----------------------------|------------------|
| Authentication             | 9099             |
| App Hosting                | 5002             |
| Emulator Suite UI          | 4000             |
| Cloud Functions            | 5001             |
| Eventarc                   | 9299             |
| Realtime Database          | 9000             |
| Cloud Firestore            | 8080             |
| Cloud Storage for Firebase | 9199             |
| Firebase Hosting           | 5000             |
| Pub/Sub                    | 8085             |

### Project ID configuration

Depending on how you invoke emulators, you may run multiple instances of an emulator using different Firebase project IDs or multiple emulator instances for a given project ID. In such cases, emulator instances are running in a separate environment.

It's generally a good practice to set one project ID for all emulator invocations, so theEmulator Suite UI, different product emulators, and all running instances of a particular emulator can communicate correctly in all cases.

Local Emulator Suiteissues warnings when it detects multiple project IDs in the environment, though you can override this behavior by setting the`singleProjectMode`key to`false`in your`firebase.json`.

You can check project ID declaration(s) for mismatches in:

- **The default project in the command line.** By default, the project ID will be taken on startup from the project selected with`firebase init`or`firebase use`. To view the list of projects (and see which one is selected) use`firebase projects:list`.
- **Rules unit tests.** The project ID is often specified in calls to the Rules Unit Testing library methods`initializeTestEnvironment`or`initializeTestApp`.
- **The command line`--project`flag.** Passing theFirebaseCLI`--project`flag overrides the default project. You'll need to ensure the value of the flag matches the project ID in unit tests and app initialization.

Also check platform-specific project ID configurations you've set while configuring your[Apple platforms](https://firebase.google.com/docs/ios/setup#add-config-file),[Android](https://firebase.google.com/docs/android/setup#add-config-file), and[web](https://firebase.google.com/docs/web/setup#add-sdks-initialize)projects.

### Security Rules configuration

The emulators will take Security Rules configuration from the`database`,`firestore`and`storage`configuration keys in`firebase.json`.  

    {
      // Existing firebase configuration ...
      "database": {
        "rules": "database.rules.json"
      },
      "firestore": {
        "rules": "firestore.rules"
      },
      "storage": {
        "rules": "storage.rules"
      }

      // ...

      // Optional emulator configuration. Default
      // values are used if absent.
      "emulators": {
        "singleProjectMode": false, // do not warn on detection of multiple project IDs
        "firestore": {
          "port": "8080"
        },
        "ui": {
          "enabled": true,      // Default is `true`
          "port": 4000          // If unspecified, see CLI log for selected port
        },
        "auth": {
          "port": "9099"
        },
        "pubsub": {
          "port": "8085"
        }
      }
    }

### Specifying Java options

TheRealtime Databaseemulator,Cloud Firestoreemulator, and part ofCloud Storage for Firebaseemulator are based on Java, which can be customized with JVM flags via the environment variable`JAVA_TOOL_OPTIONS`.

For example, if you experience Java heap space related errors, you may increase the maximum Java heap size to 4GB:  

    export JAVA_TOOL_OPTIONS="-Xmx4g"
    firebase emulators:start

Multiple flags can be specified in quotes separated by spaces, like`JAVA_TOOL_OPTIONS="-Xms2g -Xmx4g"`. The flags only affect the Java-based components of the emulators and have no effect on other parts of theFirebaseCLI, such asEmulator Suite UI.

## Start up emulators

You can start emulators to run until manually terminated, or to run for the duration of a designated test script then automatically shut down.

|                        Command                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|--------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **emulators:start**                                    | Start emulators for the Firebase products configured in`firebase.json`. Emulator processes will continue running until explicitly stopped. Calling`emulators:start`will download the emulators to \~/.cache/firebase/emulators/ if they are not already installed. |                            Flag                            |                                                                                                                                                                                                                                                                                           Description                                                                                                                                                                                                                                                                                            | |------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `--only`                                                   | *Optional.*Limit which emulators start. Supply a comma-separated list of emulator names, specifying one or more of 'auth', 'database', 'firestore', 'functions', 'hosting', or 'pubsub'.                                                                                                                                                                                                                                                                                                                                                                                                         | | `--inspect-functions `<var translate="no">debug_port</var> | *Optional.* Use with theCloud Functionsemulator to enable breakpoint debugging of functions at the specified port (or the default port 9229 if argument omitted). Note that when this flag is supplied, theCloud Functionsemulator switches to a special serialized execution mode in which functions are executed in a single process, in sequential (FIFO) order; this simplifies function debugging, though the behavior differs from multi-process, parallel execution of functions in the cloud.                                                                                            | | `--export-on-exit=`                                        | *Optional.* Use with theAuthentication,Cloud Firestore,Realtime DatabaseorCloud Storage for Firebaseemulator. Instruct the emulator(s) to export data to a directory when shutdown occurs, as described for the`emulators:export`command. The export directory can be specified with this flag:`firebase emulators:start --export-on-exit=./saved-data`. If`--import`is used, the export path defaults to the same; for example:`firebase emulators:start --import=./data-path --export-on-exit`. Lastly, if desired, pass different directory paths to the`--import`and`--export-on-exit`flags. | | `--import=`<var translate="no">import_directory</var>      | *Optional.* Use with theAuthentication,Cloud Firestore,Realtime DatabaseorCloud Storage for Firebaseemulator. Import data saved using the`--export-on-exit`startup option or the`emulators:export`command to a runningAuthentication,Cloud Firestore,Realtime DatabaseorCloud Storage for Firebaseemulator instance. Any data currently in emulator memory will be overwitten.                                                                                                                                                                                                                   | | `--log-verbosity=`<var translate="no">verbosity</var>      | *Optional.*Reduces the amount of logging output from the emulators to reduce noise in the console and in log files. Valid values are DEBUG, INFO, QUIET, SILENT.                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **emulators:exec<var translate="no">scriptpath</var>** | Run the script at`scriptpath`after starting emulators for the Firebase products configured in`firebase.json`. Emulator processes will automatically stop when the script has finished running. |                            Flag                            |                                                                                                                                                                                                                                                                                           Description                                                                                                                                                                                                                                                                                            | |------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `--only`                                                   | *Optional.*Limit which emulators start. Supply a comma-separated list of emulator names, specifying one or more of 'firestore', 'database', 'functions', 'hosting', or 'pubsub'.                                                                                                                                                                                                                                                                                                                                                                                                                 | | `--inspect-functions `<var translate="no">debug_port</var> | *Optional.* Use with theCloud Functionsemulator to enable breakpoint debugging of functions at the specified port (or the default port 9229 if argument omitted). Note that when this flag is supplied, theCloud Functionsemulator switches to a special serialized execution mode in which functions are executed in a single process, in sequential (FIFO) order; this simplifies function debugging, though the behavior differs from multi-process, parallel execution of functions in the cloud.                                                                                            | | `--export-on-exit=`                                        | *Optional.* Use with theAuthentication,Cloud Firestore,Realtime DatabaseorCloud Storage for Firebaseemulator. Instruct the emulator(s) to export data to a directory when shutdown occurs, as described for the`emulators:export`command. The export directory can be specified with this flag:`firebase emulators:start --export-on-exit=./saved-data`. If`--import`is used, the export path defaults to the same; for example:`firebase emulators:start --import=./data-path --export-on-exit`. Lastly, if desired, pass different directory paths to the`--import`and`--export-on-exit`flags. | | `--import=`<var translate="no">import_directory</var>      | *Optional.* Use with theAuthentication,Cloud Firestore,Realtime DatabaseorCloud Storage for Firebaseemulator. Import data saved using the`--export-on-exit`startup option or the`emulators:export`command to a runningAuthentication,Cloud Firestore,Realtime DatabaseorCloud Storage for Firebaseemulator instance. Any data currently in emulator memory will be overwritten.                                                                                                                                                                                                                  | | `--ui`                                                     | *Optional.*Run the Emulator UI during execution.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | | `--log-verbosity=`<var translate="no">verbosity</var>      | *Optional.*Reduces the amount of logging output from the emulators to reduce noise in the console and in log files. Valid values are DEBUG, INFO, QUIET, SILENT.                                                                                                                                                                                                                                                                                                                                                                                                                                 | |

The`firebase emulators:exec`method is generally more appropriate for continuous integration workflows.

## Export and import emulator data

You can export data from theAuthentication,Cloud Firestore,Realtime DatabaseandCloud Storage for Firebaseemulators to use as a shareable, common baseline data set. These data sets can be imported using the`--import`flag, as described above.

|----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **emulators:export<var translate="no">export_directory</var>** | *Authentication,Cloud Firestore,Realtime DatabaseorCloud Storage for Firebaseemulator* . Export data from a runningCloud Firestore,Realtime DatabaseorCloud Storage for Firebaseemulator instance. The specified`export_directory`will be created if it does not already exist. If the specified directory exists, you will be prompted to confirm that the previous export data should be overwritten. You can skip this prompt using the**--force** flag. The export directory contains a data manifest file,`firebase-export-metadata.json`. You can instruct the emulators to export data automatically when they shutdown using the`--export-on-exit`flags described above. |

## Integrate with your CI system

### Running containerized Emulator Suite images

Installation and configuration of the Emulator Suite with containers in a typical CI setup is straightforward.

There are a few issues to note:

- JAR files are installed and cached at`~/.cache/firebase/emulators/`.

  - You may want to add this path to your CI cache configuration to avoid repeated downloads.
- If you do not have a`firebase.json`file in your repository, you must add a command line argument to the`emulators:start`or`emulators:exec`command to specify which emulators should be started. For example,  
  `--only functions,firestore`.

### Generate an auth token (Hosting emulator only)

If your continuous integration workflows rely onFirebase Hosting, then you will need to log in using a token in order to run`firebase emulators:exec`. The other emulators do not require login.
| **Note:** If you have configured hosting in`firebase.json`but do not need it in CI test setups, use the`--only`flag to`emulators:start`or`emulators:exec`to include only the emulators that you need.

To generate a token, run`firebase login:ci`on your local environment; this should not be performed from a CI system. Follow instructions to authenticate. You should only need to perform this step once per project, since the token will be valid across builds. The token should be treated like a password; make sure it is kept secret.

If your CI environment allows you to specify environment variables that can be used in the build scripts, simply create an environment variable called`FIREBASE_TOKEN`, with the value being the access token string. The Firebase CLI will automatically pick up the`FIREBASE_TOKEN`environment variable and the emulators will start properly.

As a last resort, you can simply include the token in your build script, but make sure that untrusted parties do not have access. For this hard-coded approach, you can add`--token "YOUR_TOKEN_STRING_HERE"`to the`firebase emulators:exec`command.

## Use the Emulator Hub REST API

### List running emulators

To list the currently running emulators, send a`GET`request to the`/emulators`endpoint of the Emulator Hub.  

    curl localhost:4400/emulators

The result will be a JSON object listing all running emulators and their host/port configuration, for example:  

    {
      "hub":{
        "name": "hub",
        "host": "localhost",
        "port": 4400
      },
      "functions": {
        "name": "functions",
        "host": "localhost",
        "port": 5001
      }
      "firestore": {
        "name": "firestore",
        "host": "localhost",
        "port": 8080
      }
    }

### Enable / Disable Background Function Triggers

In some situations you will need to temporarily disable local function and extension triggers. For example you may want to delete all of the data in theCloud Firestoreemulator without triggering any`onDelete`functions that are running in theCloud FunctionsorExtensionsemulators.

To temporarily disable local function triggers, send a`PUT`request to the`/functions/disableBackgroundTriggers`endpoint of the Emulator Hub.  

    curl -X PUT localhost:4400/functions/disableBackgroundTriggers

The result will be a JSON object detailing the current state.  

    {
      "enabled": false
    }

To enable local function triggers after they have been disabled, send a`PUT`request to the`/functions/enableBackgroundTriggers`endpoint of the Emulator Hub.  

    curl -X PUT localhost:4400/functions/enableBackgroundTriggers

The result will be a JSON object detailing the current state.  

    {
      "enabled": true
    }

## Emulator SDK integrations

The tables in this section indicate which emulators are supported by client and Admin SDKs.*Future*means emulator support is planned but not yet available.

### Client SDK availability

|                            | **Android** | **Apple platforms** | **Web** | **Firebase UI Android** | **Firebase UI iOS** | **Firebase UI Web** |
|----------------------------|-------------|---------------------|---------|-------------------------|---------------------|---------------------|
| Realtime Database          | 19.4.0      | 7.2.0               | 8.0.0   | 6.4.0                   | Future              | N/A                 |
| Cloud Firestore            | 21.6.0      | 7.2.0               | 8.0.0   | 6.4.0                   | Future              | N/A                 |
| Authentication             | 20.0.0      | 7.0.0               | 8.0.0   | 7.0.0                   | Future              | 4.7.2               |
| Cloud Storage for Firebase | 20.0.0      | 8.0.0               | 8.4.0   | 7.0.0                   | 11.0.0              | N/A                 |
| Cloud Functions            | 19.1.0      | 7.2.0               | 8.0.0   | N/A                     | N/A                 | N/A                 |
| Hosting                    | N/A         | N/A                 | N/A     | N/A                     | N/A                 | N/A                 |
| Extensions                 | N/A         | N/A                 | N/A     | N/A                     | N/A                 | N/A                 |

### Admin SDK availability

|                            | **Node** | **Java** | **Python** | **Go** |
|----------------------------|----------|----------|------------|--------|
| Realtime Database          | 8.6.0    | 6.10.0   | 2.18.0     | Future |
| Cloud Firestore            | 8.0.0    | 6.10.0   | 3.0.0      | 1.0.0  |
| Authentication             | 9.3.0    | 7.2.0    | 5.0.0      | 4.2.0  |
| Cloud Storage for Firebase | 9.8.0    | Future   | Future     | Future |
| Cloud Functions            | N/A      | N/A      | N/A        | N/A    |
| Hosting                    | N/A      | N/A      | N/A        | N/A    |
| Extensions                 | N/A      | N/A      | N/A        | N/A    |