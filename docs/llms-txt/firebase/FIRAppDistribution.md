# Source: https://firebase.google.com/docs/reference/ios/firebaseappdistribution/api/reference/Classes/FIRAppDistribution.md.txt

# FirebaseAppDistribution Framework Reference

# FIRAppDistribution


    @interface FIRAppDistribution : NSObject

The Firebase App Distribution API provides methods to check for update to
the app and returns information that enables updating the app.

By default, Firebase App Distribution is initialized with `FirebaseApp.configure()`.

Note: The App Distribution class cannot be subclassed. If this makes testing difficult,
we suggest using a wrapper class or a protocol extension.
- `
  ``
  ``
  `

  ### [isTesterSignedIn](https://firebase.google.com/docs/reference/ios/firebaseappdistribution/api/reference/Classes/FIRAppDistribution#/c:objc(cs)FIRAppDistribution(py)isTesterSignedIn)

  `
  `  
  Returns true if the App Distribution tester is signed in.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) BOOL isTesterSignedIn;

- `
  ``
  ``
  `

  ### [-signInTesterWithCompletion:](https://firebase.google.com/docs/reference/ios/firebaseappdistribution/api/reference/Classes/FIRAppDistribution#/c:objc(cs)FIRAppDistribution(im)signInTesterWithCompletion:)

  `
  `  
  Sign-in the App Distribution tester  

  #### Declaration

  Objective-C  

      - (void)signInTesterWithCompletion:
          (nonnull void (^)(NSError *_Nullable))completion;

- `
  ``
  ``
  `

  ### [-checkForUpdateWithCompletion:](https://firebase.google.com/docs/reference/ios/firebaseappdistribution/api/reference/Classes/FIRAppDistribution#/c:objc(cs)FIRAppDistribution(im)checkForUpdateWithCompletion:)

  `
  `  
  Check to see whether a new distribution is available  

  #### Declaration

  Objective-C  

      - (void)checkForUpdateWithCompletion:
          (nonnull void (^)(https://firebase.google.com/docs/reference/ios/firebaseappdistribution/api/reference/Classes/FIRAppDistributionRelease.html *_Nullable_result,
                            NSError *_Nullable))completion;

- `
  ``
  ``
  `

  ### [-signOutTester](https://firebase.google.com/docs/reference/ios/firebaseappdistribution/api/reference/Classes/FIRAppDistribution#/c:objc(cs)FIRAppDistribution(im)signOutTester)

  `
  `  
  Sign out App Distribution tester  

  #### Declaration

  Objective-C  

      - (void)signOutTester;

- `
  ``
  ``
  `

  ### [-application:openURL:options:](https://firebase.google.com/docs/reference/ios/firebaseappdistribution/api/reference/Classes/FIRAppDistribution#/c:objc(cs)FIRAppDistribution(im)application:openURL:options:)

  `
  `  
  Handle an App Distribution URL, for example a link to download a new pre-release version.
  Call this method in your app delegate's `openURL` implementation if swizzling is disabled.  

  #### Declaration

  Objective-C  

      - (BOOL)application:(nonnull UIApplication *)application
                  openURL:(nonnull NSURL *)url
                  options:(nonnull NSDictionary<NSString *, id> *)options;

- `
  ``
  ``
  `

  ### [+appDistribution](https://firebase.google.com/docs/reference/ios/firebaseappdistribution/api/reference/Classes/FIRAppDistribution#/c:objc(cs)FIRAppDistribution(cm)appDistribution)

  `
  `  
  Accesses the singleton App Distribution instance.  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)appDistribution;

  #### Return Value

  The singleton App Distribution instance.