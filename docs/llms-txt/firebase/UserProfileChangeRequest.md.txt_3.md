# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/UserProfileChangeRequest.md.txt

# FirebaseAuth Framework Reference

# UserProfileChangeRequest

    @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
    @objc(FIRUserProfileChangeRequest)
    open class UserProfileChangeRequest : NSObject

Represents an object capable of updating a user's profile data.

Properties are marked as being part of a profile update when they are set. Setting a
property value to nil is not the same as leaving the property unassigned.
- `


  ### [displayName](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/UserProfileChangeRequest#/c:@M@FirebaseAuth@objc(cs)FIRUserProfileChangeRequest(py)displayName)


  ` The name of the user.

  #### Declaration

  Swift

      @objc
      open var displayName: String? { get set }

- `


  ### [photoURL](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/UserProfileChangeRequest#/c:@M@FirebaseAuth@objc(cs)FIRUserProfileChangeRequest(py)photoURL)


  ` The URL of the user's profile photo.

  #### Declaration

  Swift

      @objc
      open var photoURL: URL? { get set }

- `


  ### [commitChanges(completion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/UserProfileChangeRequest#/c:@M@FirebaseAuth@objc(cs)FIRUserProfileChangeRequest(im)commitChangesWithCompletion:)


  ` Commits any pending changes.

  Invoked asynchronously on the main thread in the future.

  This method should only be called once.Once called, property values should not be changed.

  #### Declaration

  Swift

      @objc
      open func commitChanges(completion: ((Error?) -> Void)? = nil)

  #### Parameters

  |---|---|
  | ` completion ` | Optionally; the block invoked when the user profile change has been applied. |

- `


  ### [commitChanges()](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/UserProfileChangeRequest#/s:12FirebaseAuth24UserProfileChangeRequestC13commitChangesyyYaKF)


  ` Commits any pending changes.

  This method should only be called once. Once called, property values should not be changed.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      open func commitChanges() async throws