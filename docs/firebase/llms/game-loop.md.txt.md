# Source: https://firebase.google.com/docs/test-lab/game-loop.md.txt

# Get started with Game Loop tests for iOS

With Game Loop tests, you can write tests native to your game engine and then run
them in Test Lab on devices you choose. This way, you don't need to worry
about writing for different UI or testing frameworks. A Game Loop test
simulates the actions of a real player, and when you run it on Test Lab, it
provides a fast and scalable way to verify that your game performs well
for your users.

This page shows you how to run a Game Loop test, then view and manage your test
results in the Test Lab page of the Firebase console. You can also further
customize your tests with optional features, such as
[writing custom test results](https://firebase.google.com/docs/test-lab/game-loop#write-results)
or [ending your test early](https://firebase.google.com/docs/test-lab/game-loop#end-early).

> [!NOTE]
> **Note:** You can use Test Lab at no charge with the Spark pricing plan, which comes with a limited daily quota. For more information about other pricing plans and usage limits, see [Firebase Pricing Plans](https://firebase.google.com/pricing).

## What is a Game Loop Test?

A loop is a full or partial run-through of your test on your gaming app. You can
run a Game Loop test locally on a simulator or on a set of devices in
Test Lab. Game Loop tests can be used to:

- Run through your game as an end user would play it. You can
  either script the input of the user, let the user be idle, or replace the user
  with an AI (for example, if you implemented AI in a car
  racing game, you can put an AI driver in charge of the user's input).

- Run your game at the highest quality setting to find out which devices
  can support it.

- Run a technical test, such as compiling multiple shaders, executing them,
  and checking that the output is as expected.

## Step 1: Register Test Lab's custom URL scheme

First, you must register Firebase Test Lab's
custom URL scheme in your app:

1. In Xcode, select a project target.

2. Click the **Info** tab, then add a new **URL type**.

3. In the **URL Schemes** field, enter `firebase-game-loop`.
   You can also register the custom URL scheme by adding it to your project's
   `Info.plist` configuration file anywhere within the `<dict>` tag:

       <key>CFBundleURLTypes</key>
        <array>
            <dict>
                <key>CFBundleURLName</key>
                <string></string>
                <key>CFBundleTypeRole</key>
                <string>Editor</string>
                <key>CFBundleURLSchemes</key>
                <array>
                    <string>firebase-game-loop</string>
                </array>
            </dict>
        </array>

Your app is now configured to run a test using Test Lab.

## Step 2 (optional): Configure your app to run multiple loops

If your app has multiple custom URL schemes registered and you plan to run
multiple loops (aka scenarios) in your test, you must specify which loops you
want to run in your app at launch time.

In your app delegate, override the `application(_:open:options:)` method:

### Swift

    func application(_app: UIApplication,
                     open url: URL
                     options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
        let components = URLComponents(url: url, resolvingAgainstBaseURL: true)!
        if components.scheme == "firebase-game-loop" {
            // ...Enter Game Loop Test logic to override application(_:open:options:).
        }
        return true
    }

### Objective-C

    - (BOOL)application:(UIApplication *)app
                openURL:(NSURL *)url
                options:(NSDictionary &lt;UIApplicationOpenURLOptionsKey, id&gt; *)options {
      if ([url.scheme isEqualToString:(@"firebase-game-loop")]) {
          // ...Enter Game Loop Test logic to override application(_:open:options:).
      }
    }

When you run multiple loops in your test, the current loop is passed as a
parameter to the URL used to launch the app. You can also obtain the current
loop number by parsing the
`URLComponents` object used to fetch the custom URL scheme:

### Swift

    if components.scheme == "firebase-game-loop" {
        // Iterate over all parameters and find the one with the key "scenario".
        let scenarioNum = Int(components.queryItems!.first(where: { $0.name == "scenario" })!.value!)!
        // ...Write logic specific to the current loop (scenarioNum).
    }

### Objective-C

    if ([url.scheme isEqualToString:(@"firebase-game-loop")]) {
        // Launch the app as part of a game loop.
        NSURLComponents *components = [NSURLComponents componentsWithURL:url
                                                 resolvingAgainstBaseURL:YES];
        for (NSURLQueryItem *item in [components queryItems]) {
            if ([item.name isEqualToString:@"scenario"]) {
                NSInteger scenarioNum = [item.value integerValue];
                // ...Write logic specific to the current loop (scenarioNum).
            }
        }
    }

## Step 3: Create and run a test

After you register Test Lab's custom URL scheme, you can run your test
in the [Firebase console](https://firebase.google.com/docs/test-lab/game-loop#run-console) or with the [gcloud beta CLI](https://firebase.google.com/docs/test-lab/game-loop#run-gcloud).
If you haven't already, generate an IPA file for your app (you'll need
to locate it later).

> [!NOTE]
> **Tip:** Before using Test Lab, you can first make sure your game loops work as intended by running your test [locally on a simulator.](https://firebase.google.com/docs/test-lab/game-loop#run-local)

#### Generate an IPA for your app


1. In Xcode, select a provisioning profile for the target app.

   > [!NOTE]
   > **Note** : Test Lab re-signs your app with its own provisioning profile and certificate.

2. From the drop-down menu that appears, click **Product \> Archive** . Select the most recent archive, then click **Distribute App**.
3. In the window that appears, click **Development \> Next**.
4. *Optional:* To get a faster build, deselect the **Rebuild from Bitcode** option, then click **Next** . Test Lab doesn't require thinning or rebuilding your app to run a test so you can safely disable this option.
5. Click **Export**, then enter a directory in which you want to download your app's IPA file.

### Run a test in the Firebase console

1. If you haven't already, open the [Firebase console](https://console.firebase.google.com/)
   and create a project.

2. On the Test Lab page of the Firebase console, click **Run Your First
   Test \> Run an iOS Game Loop**.

3. In the **Upload App** section, click **Browse** , then select your app's
   IPA file (if you haven't already, [generate an IPA file](https://firebase.google.com/docs/test-lab/ios/run-game-loop-test#package-app)
   for your app).

4. *Optional* : If you want to run multiple loops (aka scenarios) at a time or
   select specific loops to run, enter the loop numbers in the **Scenarios**
   field.

   For example, when you enter "1-3, 5", Test Lab runs loops 1, 2, 3, and 5.
   By default (if you don't enter anything in the **Scenarios** field),
   Test Lab only runs loop 1.
5. In the **Devices** section, select one or more physical devices you want to
   test your app on, then click **Start Tests**.

### Run a test with the gcloud beta CLI

**Note:** The gcloud beta CLI command for iOS Game Loop tests is a **beta release**. This means that the functionality might change in backward-incompatible ways. A beta release is not subject to any SLA or deprecation policy and may receive limited or no support.

1. If you haven't already, configure your local gcloud SDK environment,
   then make sure to install the
   [gcloud beta component](https://cloud.google.com/sdk/docs/components#alpha_and_beta_components).

2. Run the `gcloud beta firebase test ios run` command and use the following
   flags to configure the run:

| Flags for Game Loop tests ||
|---|---|
| `--type` | **Required** : Specifies the type of iOS test you want to run. You can enter test types `xctest` (default) or `game-loop`. |
| `--app` | **Required** : Absolute path (Google Cloud Storage or filesystem) to your app's IPA file. This flag is only valid when running Game Loop tests. |
| `--scenario-numbers` | The loops (aka scenarios) you want to run in your app. You can enter one loop, a list or loops, or a range of loops. The default loop is 1. For example, `--scenario-numbers=1-3,5` runs loops 1, 2, 3, and 5. |
| `--device-model` | The physical device you want to run your test on (find out which [available devices](https://firebase.google.com/docs/test-lab/ios/available-testing-devices) you can use). |
| `--timeout` | The maximum duration you want your test to run. You can enter an integer to represent the duration in seconds, or an integer and enumeration to represent the duration as a longer unit of time. For example: - `--timeout=200` forces your test to terminate when it runs up to 200 seconds. - `--timeout=1h` forces your test to terminate when it runs up to an hour. |

For example, the following command runs a Game Loop test that executes loops
1, 4, 6, 7, and 8 on an iPhone 8 Plus:

```
gcloud beta firebase test ios run
 --type game-loop --app path/to/my/App.ipa --scenario-numbers 1,4,6-8
 --device-model=iphone8plus
```

For more information on the gcloud CLI, see the
[reference documentation](https://cloud.google.com/sdk/gcloud/reference/beta/).

### Run a test locally

To run your test locally, load your gaming app in a simulator and run:

```
xcrun simctl openurl SIMULATOR_UDID firebase-game-loop://
```

- You can find your simulator's UDID by running the
  `instruments -s devices` command.

- If there is only one simulator running, enter the special string
  `"booted"` in place of <var translate="no">SIMULATOR_UDID</var>.

If your test contains multiple loops, you can specify which loop you want to run
by passing the loop number to the `scenario` flag. Note that you can
only run one loop at a time when running your test locally. For example, if you
want to run loops 1, 2, and 5, you must run a separate command for each loop:

    xcrun simctl openurl SIMULATOR_UDID firebase-game-loop://?scenario=1
    xcrun simctl openurl SIMULATOR_UDID firebase-game-loop://?scenario=2
    xcrun simctl openurl SIMULATOR_UDID firebase-game-loop://?scenario=5

## End a test early

By default, a Game Loop test continues running until it reaches a timeout
of five minutes, even when all the loops have been executed. When the
timeout is reached, the test ends and cancels any pending loops. You can speed
up your test or end it early by calling Test Lab's custom URL scheme
`firebase-game-loop-complete` in your app's AppDelegate. For example:

### Swift

    /// End the loop by calling our custom url scheme.
    func finishLoop() {
        let url = URL(string: "firebase-game-loop-complete://")!
        UIApplication.shared.open(url)
    }

### Objective-C

    - (void)finishLoop {
      UIApplication *app = [UIApplication sharedApplication];
      [app openURL:[NSURL URLWithString:@"firebase-game-loop-complete://"]
          options:@{}
    completionHandler:^(BOOL success) {}];
    }

Your Game Loop test terminates the current loop and executes the next loop.
When there are no more loops to run, the test ends.

## Write custom test results

You can configure your Game Loop test to write custom test results to your
device's file system. This way, when the test starts running, Test Lab
stores the result files in a `GameLoopsResults` directory on your testing
device (which you must create yourself). When the test ends, Test Lab moves
all files from the `GameLoopResults` directory to your project's bucket. Keep
the following in mind when setting up your test:

- All result files are uploaded regardless of file type, size, or quantity.

- Test Lab doesn't process your test results until all the loops in your
  test have finished running, so if your test includes multiple loops that write
  output, make sure you append them to a unique result file or create a result
  file for each loop. This way, you can avoid overwriting results from a
  previous loop.

To set up your test to write custom test results:

1. In your app's `Documents` directory, create a directory named
   `GameLoopResults`.

2. From anywhere in your app's code (e.g., your app delegate), add the
   following:

   ### Swift

       /// Write to a results file.
       func writeResults() {
         let text = "Greetings from game loops!"
         let fileName = "results.txt"
         let fileManager = FileManager.default
         do {

         let docs = try fileManager.url(for: .documentDirectory,
                                        in: .userDomainMask,
                                        appropriateFor: nil,
                                        create: true)
         let resultsDir = docs.appendingPathComponent("GameLoopResults")
         try fileManager.createDirectory(
             at: resultsDir,
             withIntermediateDirectories: true,
             attributes: nil)
         let fileURL = resultsDir.appendingPathComponent(fileName)
         try text.write(to: fileURL, atomically: false, encoding: .utf8)
         } catch {
           // ...Handle error writing to file.
         }
       }

   ### Objective-C

       /// Write to a results file.
       - (void)writeResults:(NSString *)message {
           // Locate and create the results directory (if it doesn't exist already).
           NSFileManager *manager = [NSFileManager defaultManager];
           NSURL* url = [[manager URLsForDirectory:NSDocumentDirectory
                                         inDomains:NSUserDomainMask] lastObject];
           NSURL* resultsDir = [url URLByAppendingPathComponent:@"GameLoopResults"
                                                    isDirectory:YES];
           [manager createDirectoryAtURL:resultsDir
             withIntermediateDirectories:NO
                              attributes:nil
                                   error:nil];

           // Write the result message to a text file.
           NSURL* resultFile = [resultsDir URLByAppendingPathComponent:@"result.txt"];
           if ([manager fileExistsAtPath:[resultFile path]]) {
               // Append to the existing file
               NSFileHandle *handle = [NSFileHandle fileHandleForWritingToURL:resultFile
                                                                        error:nil];
               [handle seekToEndOfFile];
               [handle writeData:[message dataUsingEncoding:NSUTF8StringEncoding]];
               [handle closeFile];
           } else {
               // Create and write to the file.
               [message writeToURL:resultFile
                        atomically:NO
                          encoding:NSUTF8StringEncoding error:nil];
           }
       }