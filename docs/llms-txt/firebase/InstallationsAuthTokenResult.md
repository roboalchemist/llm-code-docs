# Source: https://firebase.google.com/docs/reference/swift/firebaseinstallations/api/reference/Classes/InstallationsAuthTokenResult.md.txt

# FirebaseInstallations Framework Reference

# InstallationsAuthTokenResult

    class InstallationsAuthTokenResult : NSObject

The class represents a result of the installation auth token request.
- `
  ``
  ``
  `

  ### [authToken](https://firebase.google.com/docs/reference/swift/firebaseinstallations/api/reference/Classes/InstallationsAuthTokenResult#/c:objc(cs)FIRInstallationsAuthTokenResult(py)authToken)

  `
  `  
  The installation auth token string.  

  #### Declaration

  Swift  

      var authToken: String { get }

- `
  ``
  ``
  `

  ### [expirationDate](https://firebase.google.com/docs/reference/swift/firebaseinstallations/api/reference/Classes/InstallationsAuthTokenResult#/c:objc(cs)FIRInstallationsAuthTokenResult(py)expirationDate)

  `
  `  
  The installation auth token expiration date.  

  #### Declaration

  Swift  

      var expirationDate: Date { get }