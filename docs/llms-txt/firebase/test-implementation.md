# Source: https://firebase.google.com/docs/crashlytics/test-implementation.md.txt

<br />

iOS+AndroidFlutterUnity  

<br />

## Force a crash to test your implementation

| **Note:** Before forcing a crash, make sure that your app is configured to[automatically upload dSYM files](https://firebase.google.com/docs/crashlytics/get-started?platform=ios#set-up-dsym-uploading).

1. Add code to your app that you can use to force a test crash.

   You can use the following code to add a button to your app that, when pressed, causes a crash. The button is labeled "Test Crash".

   <br />

   ### SwiftUI

   ```swift
   Button("Crash") {
     fatalError("Crash was triggered")
   }
   ```

   ### UIKit

   ### Swift

   ```python
   import UIKit

   class ViewController: UIViewController {
     override func viewDidLoad() {
         super.viewDidLoad()

         // Do any additional setup after loading the view, typically from a nib.

         let button = UIButton(type: .roundedRect)
         button.frame = CGRect(x: 20, y: 50, width: 100, height: 30)
         button.setTitle("Test Crash", for: [])
         button.addTarget(self, action: #selector(self.crashButtonTapped(_:)), for: .touchUpInside)
         view.addSubview(button)
     }

     @IBAction func crashButtonTapped(_ sender: AnyObject) {
         let numbers = [0]
         let _ = numbers[1]
     }
   }
   ```

   ### Objective-C

   ```objective-c
   #import "ViewController.h"

   @implementation ViewController
   â (void)viewDidLoad {
       [super viewDidLoad];

       // Do any additional setup after loading the view, typically from a nib.

       UIButton* button = [UIButton buttonWithType:UIButtonTypeRoundedRect];
       button.frame = CGRectMake(20, 50, 100, 30);
       [button setTitle:@"Test Crash" forState:UIControlStateNormal];
       [button addTarget:self action:@selector(crashButtonTapped:)
           forControlEvents:UIControlEventTouchUpInside];
       [self.view addSubview:button];
   }

   â (IBAction)crashButtonTapped:(id)sender {
       @[][1];
   }

   @end
   ```
2. Build and run your app in Xcode with the Xcode debugger disconnected.

   | **The Xcode debugger prevents crash reports from being sent toCrashlytics.** Complete the following steps to disconnect your test device or simulator from the Xcode debugger***before***forcing a crash.
   1. Clickplay_arrow**Build and then run the current scheme**to build your app on a test device or simulator.

   2. Wait until your app is running, then clickstop**Stop running the scheme or action** to close the initial instance of your app. This initial instance included the debugger that interferes withCrashlytics.

3. Force the test crash in order to send your app's first crash report:

   1. Open your app from the home screen of your test device or simulator.

   2. In your app, press the "Test Crash" button that you added using the code above.

   3. After your app crashes, run it again from Xcode so that your app can send the crash report to Firebase.

4. Go to the[Crashlyticsdashboard](https://console.firebase.google.com/project/_/crashlytics)of theFirebaseconsole to see your test crash.

If you've refreshed the console and you're still not seeing the test crash after five minutes, try enabling debug logging (next section).

## Enable debug logging forCrashlytics

If you don't see your test crash in theCrashlyticsdashboard, you can use debug logging forCrashlyticsto help track down the problem.

1. Enable debug logging:

   1. In Xcode, select**Product \> Scheme \> Edit scheme**.

   2. Select**Run** from the left menu, then select the**Arguments**tab.

   3. In the*Arguments Passed on Launch* section, add`-FIRDebugEnabled`.

2. Force a test crash. The first section on this page describes how to do this.

3. Within your logs, search for a log message fromCrashlyticsthat contains the following string, which verifies that your app is sending crashes to Firebase.

   ```
   Completed report submission
   ```
   | After confirming that your app is sending crashes, you can optionally disable debug logging by removing the`-FIRDebugEnabled`from the arguments passed on launch.

If you don't see this log or your test crash in theCrashlyticsdashboard of theFirebaseconsole after five minutes, reach out to[Firebase Support](https://firebase.google.com/support/troubleshooter/crashlytics/missing)with a copy of your log output so that we can help you troubleshoot further.

## Next steps

- [Customize your crash report setup](https://firebase.google.com/docs/crashlytics/customize-crash-reports)by adding opt-in reporting, logs, keys, and tracking of non-fatal errors.