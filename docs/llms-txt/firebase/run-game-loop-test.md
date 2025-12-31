# Source: https://firebase.google.com/docs/test-lab/ios/run-game-loop-test.md.txt

<br />

It can be hard to automate game testing when gaming apps are built on different UI frameworks. Game Loop tests allow you to integrate your native tests withTest Laband easily run them on devices you select. This guide describes how to prepare a Game Loop test to run usingFirebase Test Lab.

## About Game Loop tests

#### What is a Game Loop test?

A Game Loop test simulates the actions of a real player to verify that your game performs well for your users in a fast and scalable way. A loop is a full or partial run-through of your test on your gaming app. You can run a Game Loop test locally on a simulator or on a set of devices inTest Lab. Game Loop tests can be used to:

- Run through your game as an end user would play it. You can either script the input of the user, let the user be idle, or replace the user with an AI (for example, if you implemented AI in a car racing game, you can put an AI driver in charge of the user's input).
- Run your game at the highest quality setting to find out which devices can support it.
- Run a technical test, such as compiling multiple shaders, executing them, and checking that the output is as expected.

<br />

## **Step 1** : RegisterTest Lab's custom URL scheme

1. In Xcode, select a project target.

2. Click the**Info** tab, then add a new**URL type**.

3. In the**URL Schemes** field, enter`firebase-game-loop`. You can also register the custom URL scheme by adding it to your project's`Info.plist`configuration file anywhere within the`<dict>`tag:

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

Your app is now configured to run a test usingTest Lab.

## **Step 2**: Optionally configure your app

### **Run multiple loops**

If you plan to run multiple loops (aka scenarios) in your test, you must specify which loops you want to run in your app at launch time.

In your app delegate, override the`application(_:open:options:)`method:  

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

When you run multiple loops in your test, the current loop is passed as a parameter to the URL used to launch the app. You can also obtain the current loop number by parsing the`URLComponents`object used to fetch the custom URL scheme:  

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

### **End a test early**

By default, a Game Loop test continues running until it reaches a timeout of five minutes, even when all the loops have been executed. When the timeout is reached, the test ends and cancels any pending loops. You can speed up your test or end it early by callingTest Lab's custom URL scheme`firebase-game-loop-complete`in your app's AppDelegate. For example:  

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

Your Game Loop test terminates the current loop and executes the next loop. When there are no more loops to run, the test ends.

### **Write custom test results**

You can configure your Game Loop test to write custom test results to your device's file system. This way, when the test starts running,Test Labstores the result files in a`GameLoopsResults`directory on your testing device (which you must create yourself). When the test ends,Test Labmoves all files from the`GameLoopResults`directory to your project's bucket. Keep the following in mind when setting up your test:

- All result files are uploaded regardless of file type, size, or quantity.

- Test Labdoesn't process your test results until all the loops in your test have finished running, so if your test includes multiple loops that write output, make sure you append them to a unique result file or create a result file for each loop. This way, you can avoid overwriting results from a previous loop.

To set up your test to write custom test results:

1. In your app's`Documents`directory, create a directory named`GameLoopResults`.

2. From anywhere in your app's code (e.g., your app delegate), add the following:

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

## **Step 3**: Sign your app

1. Make sure that all artifacts in the app are signed. For example, you can do this through Xcode by specifying signing settings like provisioning profile and identity. For more information, see:[Apple Codesigning](https://developer.apple.com/support/code-signing/)

   | **Note** :Test Labre-signs your app with its own provisioning profile and certificate.

## **Step 4**: Package your app for uploading

Generate an IPA file for your app (you'll need to locate it later).

1. From the drop-down menu that appears, click**Product \> Archive** . Select the most recent archive, then click**Distribute App**.

2. In the window that appears, click**Development \> Next**.

3. Click**Export**, then enter a directory in which you want to download your app's IPA file.

## **Step 5**: Verify app signature

1. Verify the app signature by unzipping the .ipa file and then running`codesign --verify --deep --verbose /path/to/MyApp.app`where "MyApp" is the name of the app inside the unzipped folder (varies for each project). Expected output is`MyApp.app: valid on disk`.

## **Step 6**: Run your test locally

You can run your test locally to check its behavior before running it withTest Lab. To test locally, load your gaming app in a simulator and run:  

```
xcrun simctl openurl SIMULATOR_UDID firebase-game-loop://
```

- You can find your simulator's UDID by running the`instruments -s devices`command.

- If there is only one simulator running, enter the special string`"booted"`in place of<var translate="no">SIMULATOR_UDID</var>.

If your test contains multiple loops, you can specify which loop you want to run by passing the loop number to the`scenario`flag. Note that you can only run one loop at a time when running your test locally. For example, if you want to run loops 1, 2, and 5, you must run a separate command for each loop:  

    xcrun simctl openurl <var translate="no">SIMULATOR_UDID</var> firebase-game-loop://?scenario=1
    xcrun simctl openurl <var translate="no">SIMULATOR_UDID</var> firebase-game-loop://?scenario=2
    xcrun simctl openurl <var translate="no">SIMULATOR_UDID</var> firebase-game-loop://?scenario=5

## Next steps

Run your test using the[Firebaseconsole](https://firebase.google.com/docs/test-lab/ios/firebase-console)or the[gcloud CLI](https://firebase.google.com/docs/test-lab/ios/command-line).