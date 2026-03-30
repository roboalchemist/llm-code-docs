# Source: https://docs-containers.back4app.com/docs/ios/parse-swift-sdk/users/user-registration.md

---
title: User Registration
slug: docs/ios/parse-swift-sdk/users/user-registration
description: In this guide, you'll learn how to perform queries involving constraints on ParseGeoPoint data types
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-11T15:40:08.878Z
updatedAt: 2025-01-17T14:23:08.365Z
---

# User Registration

## Introduction

Most real-world applications often utilize user-based features to provide a more personalized service to clients. These functionalities require the client to sign up on the app. With the **Back4App** platform and the ParseSwift SDK, you will be able to implement those features in your apps simply and quickly.

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- An App [**created on Back4App**](https://www.back4app.com/docs/get-started/new-parse-app).
- A basic iOS App to test queries
:::

## Goal

To implement a user registration feature on an iOS App using the ParseSwift SDK.

## 1 - Understanding the user registration flow

In order to integrate a signup option on an iOS app, it is necessary to create an object that conforms to the ParseUser protocol. This protocol implements the main required properties so that **Back4App** is able to store and manage login information. The following snippet shows how a user object can be implemented:

```swift
1   import Foundation
2   import ParseSwift
3
4   struct User: ParseUser {
5     // Additional properties required by the ParseUser protocol
6     var authData: [String : [String : String]?]?
7     var originalData: Data?
8     var objectId: String?
9     var createdAt: Date?
10    var updatedAt: Date?
11    var ACL: ParseACL?
12  
13    // Main properties linked to the user's information
14    var username: String?
15    var email: String?
16    var emailVerified: Bool?
17    var password: String?
18
19    // A custom property
20    var age: Int?
21  }
```

As it can be seen in the above snippet, ParseSwift allows us to have a very flexible implementation for a user object. Similar to the age field, we can add as many additional fields as needed.

Once we have the User object ready, the ParseUser protocol gives this object a set of methods to handle all the necessary user operations such as **sign up**, **log in**, **log out**, etc.

In the following step, we first take a look at how to implement a signup request.

## 2 - Creating a signup request

We start by adding the corresponding form where the user enters their account information. Let ViewController (a subclass of UIViewController) be the class where we implement the form. In the snippet below, we remark the key elements a basic signup form should have:

```swift
1   import UIKit
2   import ParseSwift
3
4   class ViewController: UIViewController {
5     // User inputs
6     @IBOutlet weak var usernameTextField: UITextField!
7     @IBOutlet weak var emailTextField: UITextField!
8     @IBOutlet weak var passwordTextField: UITextField!
9  
10    // Sign up button
11   @IBOutlet weak var signUpButton: UIButton!
12     
13    override func viewDidLoad() {
14      super.viewDidLoad()
15        
16      // Add additional code if needed
17    }
18
19    // Called when the user taps on the signUpButton
20    @IBAction func handleSignUp(_ sender: Any) {
21      guard let username = usernameTextField.text, let password = passwordTextField.text else {
22        return showMessage(title: "Error", message: "The credentials are not valid.")
23      }
24        
25      signUp(username: username, email: emailTextField.text, password: password)
26    }
27    
28    // This method prepares and registers the new user
29    private func signUp(username: String, email: String?, password: String) {
30      // TODO: Here we will implement the signup action
31    }
32    
33    // Presents an alert with a title, a message and a back button
34    func showMessage(title: String, message: String) {
35      let alertController = UIAlertController(title: title, message: message, preferredStyle: .alert)
36          
37      alertController.addAction(UIAlertAction(title: "Back", style: .cancel))
38        
39      present(alertController, animated: true)
40    }
41  }
```

We leave the layout part to the developer. You can integrate and set up the visual components according to your needs.

Next, in the following step, we implement the signUp(username\:email\:password:) method.

## 3 - Implementing the signup function

The first step for signing up a user is to have an instance of a User object with its corresponding credentials. The username and the password fields are mandatory to register a new user, the remaining fields are optional. Therefore, a typical way to instantiate a User object would be:

```swift
1   var newUser = User(username: "aCoolUsername", email: "myEmail@domain.net", password: "mySecurePassword")
2   newUser.age = 25
```

Additionally, we should also provide the initial values for the custom fields, like the age field in our case.

The next step is to perform the signup action. The ParseUser protocol implements the method signup(...) that will allow us to send the signup request to the **Back4App** application. There are three types of implementations for signup(...). Depending on the use case, one should pick the appropriate one.
Now, we can complete the signUp(username\:email\:password:) in ViewController:

```swift
1   class ViewController: UIViewController {
2     ...
3
4     private func signUp(username: String, email: String?, password: String) {
5       var newUser = User(username: username, email: email, password: password)
6       newUser.age = 25 // WARNING: This should be entered by the user, not hardcoded
7
8      //WARNING: ONLY USE ONE OF THE FOLLOWING CASES, THE SYNCHRONOUS OR THE ASYNCHRONOUS CASE  
9
10     // The below registers the user synchronously and returns the updated User object (stored on your Back4App application)
11    do {
12        let signedUpUser = try newUser.signup()
13        showMessage(title: "Signup succeeded", message: "\(user)")
14        usernameTextField.text = nil
15        emailTextField.text = nil
16        passwordTextField.text = nil
17      } catch let error as ParseError {
18        showMessage(title: "Error", message: error.message)
19      } catch {
20        showMessage(title: "Error", message: error.localizedDescription)
21      }
22  
23      // The below registers the user asynchronously and returns the updated User object (stored on your Back4App application) wrapped in a Result<User, ParseError> object
24      newUser.signup { [weak self] result in
25        switch result {
26          case .success(let signedUpUser):
27            self?.showMessage(title: "Signup succeeded", message: "\(signedUpUser)")
28            self?.usernameTextField.text = nil
29            self?.emailTextField.text = nil
30            self?.passwordTextField.text = nil
31          case .failure(let error):
32            self?.showMessage(title: "Error", message: error.message)
33        }
34      }
35    }
36  }
```

:::hint{type="info"}
**Note:**&#x52;egistering a new user using thesignup(...)method automatically logs in the user, so there is no need for the user to log in again to continue using your app.
:::

At any time during your app’s lifecycle, you can have access to the currently logged-in user from a **static** property implemented in the ParseUser protocol

```swift
1   let loggedInUser: User? = User.current
```

In [**this repository**](https://github.com/templates-back4app/ios-user-registration-app) you can find a simple user registration app that follows the steps we detailed above.

## Conclusion

The **Back4App** platform together with the ParseSwift SDK offers a quick and staightforward way to integrate a signup flow onto your iOS apps. Furthermore, in the following guides, we will explore the remaining procedures like log in, log out, etc.
