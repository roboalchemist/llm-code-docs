# Source: https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Categories.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Categories.md.txt

# FirebaseAnalytics Framework Reference

# Categories

The following categories are available globally.
- `
  ``
  ``
  `

  ### [FIRAnalytics(AppDelegate)](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Categories/FIRAnalytics%28AppDelegate%29)

  `
  `  
  Provides App Delegate handlers to be used in your App Delegate.

  To save time integrating Firebase Analytics in an application, Firebase Analytics does not
  require delegation implementation from the AppDelegate if neither SwiftUI nor UIScene lifecycle
  is adopted. Instead this is automatically done by Firebase Analytics. Should you choose instead
  to delegate manually, you can turn off the App Delegate Proxy by adding
  FirebaseAppDelegateProxyEnabled into your app's Info.plist and setting it to boolean `NO`, and
  adding the methods in this category to corresponding delegation handlers.

  To handle Universal Links, you must return `true` in
  `UIApplicationDelegate.application(_:didFinishLaunchingWithOptions:)`.
- `
  ``
  ``
  `

  ### [FIRAnalytics(Consent)](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Categories/FIRAnalytics%28Consent%29)

  `
  `  
  Sets the applicable end user consent state.
- `
  ``
  ``
  `

  ### [FIRAnalytics(OnDevice)](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Categories/FIRAnalytics%28OnDevice%29)

  `
  `  
  Undocumented