# Source: https://firebase.google.com/docs/reference/swift/firebaseappdistribution/api/reference/Classes/AppDistribution.md.txt

# FirebaseAppDistribution Framework Reference

# AppDistribution

    class AppDistribution : NSObject

The Firebase App Distribution API provides methods to check for update to
the app and returns information that enables updating the app.

By default, Firebase App Distribution is initialized with `FirebaseApp.configure()`.

Note: The App Distribution class cannot be subclassed. If this makes testing difficult,
we suggest using a wrapper class or a protocol extension.
- `
  ``
  ``
  `

  ### [isTesterSignedIn](https://firebase.google.com/docs/reference/swift/firebaseappdistribution/api/reference/Classes/AppDistribution#/c:objc(cs)FIRAppDistribution(py)isTesterSignedIn)

  `
  `  
  Returns true if the App Distribution tester is signed in.  

  #### Declaration

  Swift  

      var isTesterSignedIn: Bool { get }

- `
  ``
  ``
  `

  ### [signInTester()](https://firebase.google.com/docs/reference/swift/firebaseappdistribution/api/reference/Classes/AppDistribution#/c:objc(cs)FIRAppDistribution(im)signInTesterWithCompletion:)

  `
  `  
  Sign-in the App Distribution tester  

  #### Declaration

  Swift  

      func signInTester() async throws

- `
  ``
  ``
  `

  ### [checkForUpdate()](https://firebase.google.com/docs/reference/swift/firebaseappdistribution/api/reference/Classes/AppDistribution#/c:objc(cs)FIRAppDistribution(im)checkForUpdateWithCompletion:)

  `
  `  
  Check to see whether a new distribution is available  

  #### Declaration

  Swift  

      func checkForUpdate() async throws -> FIRAppDistributionRelease?

- `
  ``
  ``
  `

  ### [signOutTester()](https://firebase.google.com/docs/reference/swift/firebaseappdistribution/api/reference/Classes/AppDistribution#/c:objc(cs)FIRAppDistribution(im)signOutTester)

  `
  `  
  Sign out App Distribution tester  

  #### Declaration

  Swift  

      func signOutTester()

- `
  ``
  ``
  `

  ### [application(_:open:options:)](https://firebase.google.com/docs/reference/swift/firebaseappdistribution/api/reference/Classes/AppDistribution#/c:objc(cs)FIRAppDistribution(im)application:openURL:options:)

  `
  `  
  Handle an App Distribution URL, for example a link to download a new pre-release version.
  Call this method in your app delegate's `openURL` implementation if swizzling is disabled.  

  #### Declaration

  Swift  

      func application(_ application: UIApplication, open url: URL, options: [String : Any] = [:]) -> Bool

- `
  ``
  ``
  `

  ### [appDistribution()](https://firebase.google.com/docs/reference/swift/firebaseappdistribution/api/reference/Classes/AppDistribution#/c:objc(cs)FIRAppDistribution(cm)appDistribution)

  `
  `  
  Accesses the singleton App Distribution instance.  

  #### Declaration

  Swift  

      class func appDistribution() -> Self

  #### Return Value

  The singleton App Distribution instance.