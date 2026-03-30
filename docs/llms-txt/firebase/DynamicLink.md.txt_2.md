# Source: https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLink.md.txt

# FirebaseDynamicLinks Framework Reference

# DynamicLink

    class DynamicLink : NSObject

A received Dynamic Link.
- `


  ### [url](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLink#/c:objc(cs)FIRDynamicLink(py)url)


  ` The URL that was passed to the app.

  #### Declaration

  Swift

      var url: URL? { get }

- `


  ### [matchType](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLink#/c:objc(cs)FIRDynamicLink(py)matchType)


  ` The match type of the received Dynamic Link.

  #### Declaration

  Swift

      var matchType: https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Enums/DLMatchType.html { get }

- `


  ### [utmParametersDictionary](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLink#/c:objc(cs)FIRDynamicLink(py)utmParametersDictionary)


  ` UTM parameters associated with a Firebase Dynamic Link.

  #### Declaration

  Swift

      var utmParametersDictionary: [String : Any] { get }

- `


  ### [minimumAppVersion](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLink#/c:objc(cs)FIRDynamicLink(py)minimumAppVersion)


  ` The minimum iOS application version that supports the Dynamic Link. This is retrieved
  from the imv= parameter of the Dynamic Link URL. Note: This is not the minimum iOS system
  version, but the minimum app version. If app version of the opening app is less than the
  value of this property, then app expected to open AppStore to allow user to download most
  recent version. App can notify or ask user before opening AppStore.

  #### Declaration

  Swift

      var minimumAppVersion: String? { get }

- `


  ### [-init](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLink#/c:objc(cs)FIRDynamicLink(im)init)


  ` Unavailable
  Undocumented