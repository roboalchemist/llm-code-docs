# Source: https://docs-containers.back4app.com/docs/ios/xcode-user-register-and-login-tutorial.md

---
title: Sign-up/Sign-in - ObjC
slug: docs/ios/xcode-user-register-and-login-tutorial
description: In this guide you learn how to add user registration and login to your XCode app project.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-11T18:53:50.580Z
updatedAt: 2025-01-17T14:24:09.305Z
---

## Login and User registration tutorial using XCode and Back4App

### Introduction

This section explains how you can create an app with a simple user registration using [**Parse Server core features**](https://www.back4app.com/product/parse-server) through Back4App.

This is how it will look like:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/-oR4uTmXHkc1iW15BS3Kq_image.png" signedSrc size="30" width="974" height="1602" position="flex-start" caption}

:::hint{type="success"}
At any time, you can access the complete Project built with this tutorial at our [**GitHub repository**](https://github.com/templates-back4app/iOS-install-SDK).
:::

:::hint{type="info"}
**To complete this quickstart, you need:**

- [**Xcode**](https://developer.apple.com/xcode/).
- An app created at Back4App.
  - Follow the [**New Parse App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create a Parse app at Back4App.
- An iOS app connected to Back4App.
  - **Note:&#x20;**&#x46;ollow the [**Install Parse SDK (ObjC) Tutorial**](https://www.back4app.com/docs/ios/parse-objc-sdk) to create an Xcode Project connected to Back4App.
- A paid Apple Developer Account.
:::

## 1 - Set up

1. Add another view controller called LoggedInViewController. In the main storyboard drag a view controller on to the canvas and set the class to LoggedInViewController and set the Storyboard ID to LoggedInViewController
2. In both ViewController.m and LoggedInViewController.m make sure to include the Parse module by including it at the top of the file.

:::BlockQuote
\#import \<Parse/Parse.h>
:::

## 2 - Create your Sign Up and Login UI

Logging in creates a Session object, which points to the User logged in. If login is successful, *ParseUser.CurrentUser()* returns a User object, and a Session object is created in the Dashboard. Otherwise, if the target username does not exist, or the password is wrong, it returns null.

The method used to perform the login action is *ParseUser.logInWithUsername()*, which requires as many arguments as the strings of username and password, and may call a callback function.

:::hint{type="info"}
**Note:&#x20;**&#x41;fter signing up, login is performed automatically.
:::



1. Drag four UITextFields onto the ViewController in the main storyboard. Center the textfield and put two at the top and two at the bottom of the view controller. Drag two more UIButtons on to the view and place them below the textfields. Set the top button text to say Sign In. Set the bottom bottom to say Sign Up. Set the text fields to say username and password. It should look like this.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/cgQDT44MUapwapprPY2KA_image.png" signedSrc size="30" width="974" height="1602" position="flex-start" caption}

1. 2\. Next we are going to connect your UITextFields in your storyboard to properties in your view controller. Add the following properties to the top of ViewController.m. Next go to your storyboard and right click on each UITextField and click on the reference outlet then drag a line back to the ViewController icon and set it to the appropriate field. signInUsernameField connects to the sign In Username Field, etc… Finally we will add a UIActivityIndicatorView for later.

:::BlockQuote
@interface ViewController ()\{
&#x20;IBOutlet UITextField \* signInUserNameTextField;
&#x20;IBOutlet UITextField \* signInPasswordTextField;
&#x20;IBOutlet UITextField \* signUpUserNameTextField;
&#x20;IBOutlet UITextField \* signUpPasswordTextField;
&#x20;UIActivityIndicatorView \*activityIndicatorView;
}
:::

&#x20;    2\. Then in the viewDidLoad method set the UIActivityIndicatorView to be attached to the middle of the screen.

:::BlockQuote
\- (void)viewDidLoad \{
&#x20;\[super viewDidLoad];
&#x20;CGRect frame = CGRectMake (120.0, 185.0, 80, 80);
&#x20;activityIndicatorView = \[\[UIActivityIndicatorView alloc] initWithFrame\:frame];
&#x20;activityIndicatorView\.color = \[UIColor blueColor];
&#x20;\[self.view addSubview\:activityIndicatorView];
}
:::

&#x20;    3\. Then in the viewDidAppear method check to see if you are already logged in. If you are logged in you will redirect the user to the LoggedInViewController.

:::BlockQuote
\- (void)viewDidAppear:(BOOL)animated \{
&#x20;if (\[PFUser currentUser]) \{
&#x20;    \[self goToMainPage];
&#x20;}
}
:::

&#x20;    4\. Next lets add the goToMainPage method. It will redirec the user to the LoggedInViewController. Make sure the that the LoggedInViewController in the storyboard has its class and Storyboard ID set to LoggedInViewController.

:::BlockQuote
&#x20;\- (void)goToMainPage \{
&#x20;NSString \* storyboardName = @"Main";
&#x20;UIStoryboard \*storyboard = \[UIStoryboard storyboardWithName\:storyboardName bundle: nil];
&#x20;LoggedInViewController \* vc = \[storyboard instantiateViewControllerWithIdentifier:@"LoggedInViewController"];
&#x20;\[self presentViewController\:vc animated\:YES completion\:nil];
}
:::

&#x20;     5\. Now lets set up the IBAction that will connect to the SignUp button on the ViewController in the main storyboard.

:::BlockQuote
\- (IBAction)signUp:(id)sender \{
&#x20;PFUser \*user = \[PFUser user];
&#x20;user.username = signUpUserNameTextField.text;
&#x20;user.password = signUpPasswordTextField.text;
&#x20;\[activityIndicatorView startAnimating];
&#x20;\[user signUpInBackgroundWithBlock:^(BOOL succeeded, NSError \*error) \{
&#x20;    \[self->activityIndicatorView stopAnimating];
&#x20;    if (!error) \{
&#x20;        \[self goToMainPage];
&#x20;    } else \{
&#x20;        \[self displayMessageToUser\:error.localizedDescription];
&#x20;    }
&#x20;}];
}
:::

&#x20;     6\. We need to add the displayErrorMessage function to show any error messages from the server. We will use this method anytime we communicate with our parse app.

:::BlockQuote
\- (void)displayMessageToUser:(NSString\*)message \{
&#x20;UIAlertController\* alert = \[UIAlertController alertControllerWithTitle:@"Message"
&#x20;                                                               message\:message
&#x20;                                                        preferredStyle\:UIAlertControllerStyleAlert];
&#x20;UIPopoverPresentationController \*popPresenter = \[alert popoverPresentationController];
&#x20;popPresenter.sourceView = self.view;
&#x20;UIAlertAction \*Okbutton = \[UIAlertAction actionWithTitle:@"Ok" style\:UIAlertActionStyleDefault handler:^(UIAlertAction \*action) \{

&#x20;}];
&#x20;\[alert addAction\:Okbutton];
&#x20;popPresenter.sourceRect = self.view\.frame;
&#x20;alert.modalPresentationStyle = UIModalPresentationPopover;
&#x20;\[self presentViewController\:alert animated\:YES completion\:nil];
}
:::

&#x20;      7\. Now that we can handle network activity and network errors lets set up the IBAction that will connect to the SignIn button on the ViewController in the main storyboard.

:::BlockQuote
\- (IBAction)signUp:(id)sender \{
&#x20;PFUser \*user = \[PFUser user];
&#x20;user.username = signUpUserNameTextField.text;
&#x20;user.password = signUpPasswordTextField.text;
&#x20;\[activityIndicatorView startAnimating];
&#x20;\[user signUpInBackgroundWithBlock:^(BOOL succeeded, NSError \*error) \{
&#x20;    \[self->activityIndicatorView stopAnimating];
&#x20;    if (!error) \{
&#x20;        \[self goToMainPage];
&#x20;    } else \{
&#x20;        \[self displayMessageToUser\:error.localizedDescription];
&#x20;    }
&#x20;}];
}
:::

## 3 - Log Out

Logging out deletes the active Session object for the logged User. The method used to perform log out is *ParseUser.logOutInBackgroundWithBlock()*.

1. Drag a UIButton on to LoggedInViewController in the main storyboard. Set the button title to ‘Logout’. It should look like this.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/S0ZDJ3xgypXJ7bzVazxRm_image.png" signedSrc size="30" width="974" height="1602" position="flex-start" caption}

1. Lets add the displayErrorMessage function again to show any error messages from the server. We will use this method anytime we communicate with our parse app.

:::BlockQuote
\- (void)displayMessageToUser:(NSString\*)message \{
&#x20;UIAlertController\* alert = \[UIAlertController alertControllerWithTitle:@"Message"
&#x20;                                                               message\:message
&#x20;                                                        preferredStyle\:UIAlertControllerStyleAlert];
&#x20;UIPopoverPresentationController \*popPresenter = \[alert popoverPresentationController];
&#x20;popPresenter.sourceView = self.view;
&#x20;UIAlertAction \*Okbutton = \[UIAlertAction actionWithTitle:@"Ok" style\:UIAlertActionStyleDefault handler:^(UIAlertAction \*action) \{

&#x20;}];
&#x20;\[alert addAction\:Okbutton];
&#x20;popPresenter.sourceRect = self.view\.frame;
&#x20;alert.modalPresentationStyle = UIModalPresentationPopover;
&#x20;\[self presentViewController\:alert animated\:YES completion\:nil];
}
:::

&#x20;    2\. Lets add the goToStartPage function to take us back to the login/signup screen after we logout.

:::BlockQuote
\- (void)goToStartPage \{
&#x20;NSString \* storyboardName = @"Main";
&#x20;UIStoryboard \*storyboard = \[UIStoryboard storyboardWithName\:storyboardName bundle: nil];
&#x20;ViewController \* vc = \[storyboard instantiateViewControllerWithIdentifier:@"ViewController"];
&#x20;\[self presentViewController\:vc animated\:YES completion\:nil];
}
:::

&#x20;   3\. Finally lets add the IBAction to execute the logout call and take us back to ViewController.m signup/login page. This method logs out the PFUser and takes you back to the signup page. Connect this IBAction to the logout button on LoggedInViewController.

:::BlockQuote
&#x20;\- (IBAction)logout:(id)sender \{
&#x20;\[activityIndicatorView startAnimating];
&#x20;\[PFUser logOutInBackgroundWithBlock:^(NSError \* \_Nullable error) \{
&#x20;    \[self->activityIndicatorView stopAnimating];
&#x20;    if(error == nil)\{
&#x20;        \[self goToStartPage];
&#x20;    }else\{
&#x20;        \[self displayMessageToUser\:error.debugDescription];
&#x20;    }
&#x20;}];
}
:::

## 4 - Test your app

1. Run your app and create a couple of users, also try logging in again after registering them.
2. Login at [**Back4App Website**](https://www.back4app.com/)
3. Find your app and click on Dashboard>Core>Browser>User.
4. Try logging in and out with the same user and signing back in.

At this point, you should see your users as displayed below:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/tCMf5EqkqlpQbFhoyL5XT_image.png)

:::hint{type="info"}
**Note**: Using the codes displayed above, every time you log in with a user, a Session is opened in your Dashboard, but when the user logs out that particular Session ends. Also, whenever an unsuccessful login or sign up attempt occurs, the Session opened in Parse Server Dashboard is deleted.
:::

## It’s done!

At this stage, you can log in, register or log out of your app using Parse Server core features through Back4App!
