# Source: https://docs-containers.back4app.com/docs/ios/swift-login-tutorial.md

---
title: Sign-up/Sign-in - Swift
slug: docs/ios/swift-login-tutorial
description: In this guide you learn how to add user registration and login to your Swift App.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-11T18:39:43.812Z
updatedAt: 2025-01-16T21:00:06.426Z
---

# Login and User registration tutorial using Swift

## Introduction

This section explains how you can create an app with a simple user registration using [**Parse Server core features**](https://www.back4app.com/product/parse-server) through Back4App.

:::hint{type="success"}
At any time, you can access the complete Project built with this tutorial at our [**GitHub repository**](https://github.com/templates-back4app/iOS-install-SDK).
:::

:::hint{type="info"}
**To complete this quickstart, you need:**

- [**Xcode**](https://developer.apple.com/xcode/).
- An app created at Back4App.
  - Follow the [**New Parse App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create a Parse app at Back4App.
- An iOS app connected to Back4App.
  - **Note:&#x20;**&#x46;ollow the [**Install Parse SDK (Swift) Tutorial**](https://www.back4app.com/docs/ios/parse-swift-sdk) to create an Xcode Project connected to Back4App.
- A paid Apple Developer Account.
:::

## Let’s get started!

Following the next steps you will be able to build an App that will Sign-in, Sign-up and Logout at Back4App Database.

## 1 - Set up and Create your Sign Up and Login UI

1. Go to Xcode, access the main folder from the Project and then open the ViewController.swift file to edit it.
2. In ViewController.swift make sure to include the Parse module by including it at the top of the file.

```swift
1   import Parse
```

&#x20;    3\. Go to Main.storyboard, drag four UITextFields onto the ViewController in the main storyboard. Center the textfield and put two at the top and two at the bottom of the view controller. Drag two more UIButtons on to the view and place them below the textfields. Drag one more Loader Indicators on each Button.
Set the top button text to say Sign In. Set the bottom bottom to say Sign Up. Set the text fields to say username and password.

&#x20;    4\. Next we are going to connect your UITextFields in your storyboard to properties in your view controller. Add the following properties to the top of ViewController.swift. Next go to your storyboard and right click on each UITextField and click on the reference outlet then drag a line back to the ViewController icon and set it to the appropriate field. signInUsernameField connects to the sign In Username Field, etc…

It should look like this:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/uVLBHeYZQQZcbGLyiyb38_image.png)

```swift
1   import UIKit
2   import Parse
3
4   class ViewController: UIViewController {
5
6       @IBOutlet weak var txtUsernameSignin: UITextField!
7       @IBOutlet weak var txtPasswordSignin: UITextField!
8       @IBOutlet weak var indicatorLogin: UIActivityIndicatorView!
9    
10      @IBOutlet weak var txtUsernameSignup: UITextField!
11      @IBOutlet weak var txtPasswordSignup: UITextField!
12      @IBOutlet weak var indicatorSignup: UIActivityIndicatorView!
13    
14      override func viewDidLoad() {
15          super.viewDidLoad()
16          // Do any additional setup after loading the view.
17      }
18    
19      @IBAction func signin(_ sender: Any) {
20          //todo
21      }
22    
23      @IBAction func signup(_ sender: Any) {
24          //todo
25      }
26  
27  }
```

## 2 - Create a Sign-in function

Add the following code inside the sign-in function:

```swift
1          @IBAction func signin(_ sender: Any) {
2           PFUser.logInWithUsername(inBackground: self.txtUsernameSignin.text!, password: self.txtPasswordSignin.text!) {
3             (user: PFUser?, error: Error?) -> Void in
4             if user != nil {
5               self.displayAlert(withTitle: "Login Successful", message: "")
6             } else {
7               self.displayAlert(withTitle: "Error", message: error!.localizedDescription)
8             }
9           }
10      }
```

## 3 - Create a Sign-up function

Add the following code inside the sign-up function:

```swift
1       @IBAction func signup(_ sender: Any) {
2           let user = PFUser()
3           user.username = self.txtUsernameSignup.text
4           user.password = self.txtPasswordSignup.text
5        
6           self.indicatorSignup.startAnimating()
7           user.signUpInBackground {(succeeded: Bool, error: Error?) -> Void in
8               self.indicatorSignup.stopAnimating()
9               if let error = error {
10                  self.displayAlert(withTitle: "Error", message: error.localizedDescription)
11              } else {
12                  self.displayAlert(withTitle: "Success", message: "Account has been successfully created")
13              }
14          }
15      }
```

## 4 - Log Out

When logging, it creates a Session object, which points to the User logged in. If login is successful, ParseUser.CurrentUser() returns a User object, and a Session object is created in the Dashboard. Otherwise, if the target username does not exist, or the password is wrong, it returns null.

To do Logout follow the steps below:

1. Go to Main.storyboard, drag one UIButton called “Logout”, and add a action between this UIbutton and the ViewController.swift.
2. Add the following code in this function:

```swift
1    @IBAction func logout(_ sender: Any) {
2        PFUser.logOut()
3    }
```

## 5 - Application Code

```swift
1   import UIKit
2   import Parse
3
4   class ViewController: UIViewController {
5    
6       @IBOutlet weak var txtUsernameSignin: UITextField!
7       @IBOutlet weak var txtPasswordSignin: UITextField!
8       @IBOutlet weak var indicatorSignin: UIActivityIndicatorView!
9    
10      @IBOutlet weak var txtUsernameSignup: UITextField!
11      @IBOutlet weak var txtPasswordSignup: UITextField!
12      @IBOutlet weak var indicatorSignup: UIActivityIndicatorView!
13    
14      @IBOutlet weak var btnLogout: UIButton!
15    
16      override func viewDidLoad() {
17          super.viewDidLoad()
18      }
19
20      @IBAction func signin(_ sender: Any) {
21          PFUser.logInWithUsername(inBackground: self.txtUsernameSignin.text!, password: self.txtPasswordSignin.text!) {
22            (user: PFUser?, error: Error?) -> Void in
23            if user != nil {
24              self.displayAlert(withTitle: "Login Successful", message: "")
25            } else {
26              self.displayAlert(withTitle: "Error", message: error!.localizedDescription)
27            }
28          }
29      }
30   
31      @IBAction func signup(_ sender: Any) {
32          let user = PFUser()
33          user.username = self.txtUsernameSignup.text
34          user.password = self.txtPasswordSignup.text
35          
36          self.indicatorSignup.startAnimating()
37          user.signUpInBackground {(succeeded: Bool, error: Error?) -> Void in
38              self.indicatorSignup.stopAnimating()
39              if let error = error {
40                  self.displayAlert(withTitle: "Error", message: error.localizedDescription)
41              } else {
42                  self.displayAlert(withTitle: "Success", message: "Account has been successfully created")
43              }
44          }
45      }
46    
47      @IBAction func logout(_ sender: Any) {
48          PFUser.logOut()
49      }
50      
51      func displayAlert(withTitle title: String, message: String) {
52          let alert = UIAlertController(title: title, message: message, preferredStyle: .alert)
53          let okAction = UIAlertAction(title: "Ok", style: .default)
54          alert.addAction(okAction)
55          self.present(alert, animated: true)
56      }
57    
58  }
```

The application UI will be similar to this:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Hb0Hy0l7KmiL8nM7sUG2M_image.png" signedSrc size="40" width="640" height="1136" position="center" caption}

## 6 - Test your app

1. Run your app and create a couple of users, also try logging in again after registering them.
2. Login at [**Back4App Website**](https://www.back4app.com/)
3. Find your app and click on Dashboard>Core>Browser>User.
4. Try logging in and out with the same user and signing back in.

At this point, you should see your users as displayed below:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/bd-AZQhcoldg7wXvBK28B_image.png)

:::hint{type="info"}
**Note**: Using the codes displayed above, every time you log in with a user, a Session is opened in your Dashboard, but when the user logs out that particular Session ends. Also, whenever an unsuccessful login or sign up attempt occurs, the Session opened in Parse Server Dashboard is deleted.
:::

## It’s done!

At this stage, you can log in, register or log out of your app using Parse Server core features through Back4App!
