# Source: https://docs-containers.back4app.com/docs/ios/parse-swift-sdk/users/sign-in-with-apple.md

# Source: https://docs-containers.back4app.com/docs/platform/sign-in-with-apple.md

---
title: Sign Up With Apple
slug: docs/platform/sign-in-with-apple
description: In this tutorial you will learn the steps to set up Sign In with Apple within your Apple account.
image: https://www.back4app.com/_public/img/back4app-og.png
createdAt: 2024-02-02T14:37:30.716Z
updatedAt: 2025-01-27T19:45:35.739Z
---

# Sign In with Apple Tutorial

## Introduction

Sign In with Apple enables users to sign in to Apps using their Apple ID.
This feature is available on iOS 13 and later, and Parse 3.5 and later.

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- An app created at Back4App
- See the [**Create New App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create an app at Back4App.
- Set up a Subdomain for your Back4app app
- See [**Activating your Web Hosting and Live Query**](https://www.back4app.com/docs/platform/activating-web-hosting) to learn how to create a subdomain in Back4App.
- An [**Apple Developer account**](https://developer.apple.com/).
:::

## 1 - Create a New Back4App App

First of all, it’s necessary to make sure that you have an existing app created at Back4App. However, if you are a new user, you can check [**this tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create one.

## 2 - Add the Sign In with Apple capability to your XCode project

In your XCode Project, click on the Target (1) and go to the Signing & Capabilities tab (2).
Click the + Capability button (3) and add the Sign In with Apple capability (4).
While there, choose your Bundle Identifier (5) and hold that information because we will need it later.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/OaqDtMwyMrhMjvpsgMqCP_image.png)

## 3 - Create a new Service ID

Log into your [**Apple Developer account**](https://developer.apple.com/) and go to the Identifiers section. Check if your created Bundle Identifier is there

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/SJ71g8F23N98KDnIgRlTS_image.png)

Click the Bundle Identifier and scroll down. Check if the Sign In with Apple is selected

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Of5puKJb4HSnxpf7_7laa_image.png)

Click Edit and make sure the Enable as a primary App ID is selected

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/aYO-XTOt-T54DIE3nGHtZ_image.png)

If everything is right, save and exit.

## 4 - Set up Parse Auth for Apple

Go to the Back4App website, log in, and then find your app. After that, click on Server Settings search for the Apple Login block, and select Settings.

The Apple Login section looks like this:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/g6VC7nVrqvf_yC3KBw5uJ_image.png" signedSrc size="40" width="255" height="314" position="center" caption}

Now, you just need to paste your Bundle ID in the field below and click on the button to save.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/tSyAtP9dJ7v4L_9pWfb9k_image.png" signedSrc size="70" width="599" height="454" position="center" caption}

In case you face any trouble while integrating Apple Login, please contact our team via chat!

## 5 - Option 1 - Download our Template

There is some coding involved in making Sign in With Apple work, so we created [**this template**](https://github.com/templates-back4app/ParseSignInWithApple) that you can download, and change the Bundle Identifier, the App Id, and Client Key.

The code is fully documented so it is a good starting point.

If you prefer to read through this doc, please go on to the next step.

## 6 - Option 2 - Manually write code

Inside your view, add the AuthenticationServices framework and create the AuthDelegate that will handle the PFUserAuthenticationDelegate:

```swift
1   import AuthenticationServices
2
3   class AuthDelegate:NSObject, PFUserAuthenticationDelegate {
4       func restoreAuthentication(withAuthData authData: [String : String]?) -> Bool {
5           return true
6       }
7    
8       func restoreAuthenticationWithAuthData(authData: [String : String]?) -> Bool {
9           return true
10      }
11  }
```

## 7 - Implement your Delegates for the ViewController

Implement the ASAuthorizationControllerDelegate and ASAuthorizationControllerPresentationContextProviding for the ViewController:

```swift
1   class ViewController: UIViewController, ASAuthorizationControllerDelegate, ASAuthorizationControllerPresentationContextProviding
```

## 8 - Add the Sign In with Apple button

The ViewDidAppear is a good place for it. If you choose other places, remember to call it just once:

```swift
1   override func viewDidAppear(_ animated: Bool) {
2           super.viewDidAppear(animated)
3        
4           // Sign In with Apple button
5           let signInWithAppleButton = ASAuthorizationAppleIDButton()
6
7           // set this so the button will use auto layout constraint
8           signInWithAppleButton.translatesAutoresizingMaskIntoConstraints = false
9
10          // add the button to the view controller root view
11          self.view.addSubview(signInWithAppleButton)
12
13          // set constraint
14          NSLayoutConstraint.activate([
15              signInWithAppleButton.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor, constant: 50.0),
16              signInWithAppleButton.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor, constant: -50.0),
17              signInWithAppleButton.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor, constant: -70.0),
18              signInWithAppleButton.heightAnchor.constraint(equalToConstant: 50.0)
19          ])
20
21          // the function that will be executed when user tap the button
22          signInWithAppleButton.addTarget(self, action: #selector(appleSignInTapped), for: .touchUpInside)
23      }
```

The appleSignInTapped in the last line must also be defined inside the ViewController class:

```swift
1  // This is the function that will be executed when user taps the button
2       @objc func appleSignInTapped() {
3           let provider = ASAuthorizationAppleIDProvider()
4           let request = provider.createRequest()
5           // request full name and email from the user's Apple ID
6           request.requestedScopes = [.fullName, .email]
7
8           // pass the request to the initializer of the controller
9           let authController = ASAuthorizationController(authorizationRequests: [request])
10        
11          // similar to delegate, this will ask the view controller
12          // which window to present the ASAuthorizationController
13          authController.presentationContextProvider = self
14        
15          // delegate functions will be called when user data is
16          // successfully retrieved or error occured
17          authController.delegate = self
18          
19          // show the Sign-in with Apple dialog
20          authController.performRequests()
21      }
```

## 9 - The presentationContextProvider

The presentationContextProvider (ASAuthorizationControllerPresentationContextProviding) will ask for which window should display the Authorization dialog. As we are going to display it in the same window, we must return self.view\.window:

```swift
1   func presentationAnchor(for controller: ASAuthorizationController) -> ASPresentationAnchor {
2           // return the current view window
3           return self.view.window!
4       }
```

## 10 - Handling the delegate ASAuthorizationControllerDelegate

There are a few options that we must handle when the delegate is called, so let’s add some code to handle those options distinctly:

```swift
1   func authorizationController(controller: ASAuthorizationController, didCompleteWithError error: Error) {
2           print("authorization error")
3           guard let error = error as? ASAuthorizationError else {
4               return
5           }
6
7           switch error.code {
8           case .canceled:
9               // user press "cancel" during the login prompt
10              print("Canceled")
11          case .unknown:
12              // user didn't login their Apple ID on the device
13             print("Unknown")
14          case .invalidResponse:
15              // invalid response received from the login
16              print("Invalid Respone")
17          case .notHandled:
18              // authorization request not handled, maybe internet failure during login
19              print("Not handled")
20          case .failed:
21              // authorization failed
22              print("Failed")
23          @unknown default:
24              print("Default")
25          }
26      }
```

## 11 - Handling the delegate for didCompleteWithAuthorization

When we successfully authenticate, we can retrieve the authorized information:

```swift
1      func authorizationController(controller: ASAuthorizationController, didCompleteWithAuthorization authorization: ASAuthorization) {
2        
3              if let appleIDCredential = authorization.credential as? ASAuthorizationAppleIDCredential {
4                  // unique ID for each user, this uniqueID will always be returned
5                  let userID = appleIDCredential.user
6                  print("UserID: " + userID)
7            
8                  // if needed, save it to user defaults by uncommenting the line below
9                  //UserDefaults.standard.set(appleIDCredential.user, forKey: "userID")
10            
11                 // optional, might be nil
12                 let email = appleIDCredential.email
13                 print("Email: " + (email ?? "no email") )
14            
15                 // optional, might be nil
16                 let givenName = appleIDCredential.fullName?.givenName
17                 print("Given Name: " + (givenName ?? "no given name") )
18            
19                 // optional, might be nil
20                 let familyName = appleIDCredential.fullName?.familyName
21                 print("Family Name: " + (familyName ?? "no family name") )
22            
23                 // optional, might be nil
24                 let nickName = appleIDCredential.fullName?.nickname
25                 print("Nick Name: " + (nickName ?? "no nick name") )
26                 /*
27                     useful for server side, the app can send identityToken and authorizationCode
28                     to the server for verification purpose
29                 */
30                 var identityToken : String?
31                 if let token = appleIDCredential.identityToken {
32                     identityToken = String(bytes: token, encoding: .utf8)
33                     print("Identity Token: " + (identityToken ?? "no identity token"))
34                 }
35
36                 var authorizationCode : String?
37                 if let code = appleIDCredential.authorizationCode {
38                     authorizationCode = String(bytes: code, encoding: .utf8)
39                     print("Authorization Code: " + (authorizationCode ?? "no auth code") )
40                 }
41
42                 // do what you want with the data here
43            
44           }    
45       }
```

That’s the place where we can also add code for logging in Parse. So right after the do what you want with the data here comment, let’s add:

```swift
1   PFUser.logInWithAuthType(inBackground: "apple", authData: ["token": String(identityToken!), "id": userID]).continueWith { task -> Any? in
2                   if ((task.error) != nil){
3                       //DispatchQueue.main.async {
4                           print("Could not login.\nPlease try again.")
5                           print("Error with parse login after SIWA: \(task.error!.localizedDescription)")
6                       //}
7                       return task
8                   }
9                   print("Successfuly signed in with Apple")
10                  return nil
11              }
```

And of course, add the Parse framework:

```swift
1   import Parse
```

