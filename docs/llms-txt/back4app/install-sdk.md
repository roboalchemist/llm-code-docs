# Source: https://docs-containers.back4app.com/docs/ios/parse-swift-sdk/install-sdk.md

---
title: Quickstart
slug: docs/ios/parse-swift-sdk/install-sdk
description: Learn how to install Parse iOS SDK into your Xcode project for Swift
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-11T10:30:04.297Z
updatedAt: 2025-01-17T14:22:28.197Z
---

# Install Parse SDK on your iOS Swift Project

## Introduction

In this section you will learn how to install Parse Swift iOS SDK into your Xcode project.

In this tutorial we will use a basic app created in Swift with Xcode 12 and **iOS 14**.

:::hint{type="success"}
At any time, you can access the complete Project built with this tutorial at our [**GitHub repository**](https://github.com/templates-back4app/iOS-install-SDK).
:::

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you need:**

- An app created at Back4App.
  - **Note:&#x20;**&#x46;ollow the [**New Parse App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create an app at Back4App.
- Xcode.
- Basic iOS app.
  - **Note:**&#x49;f you don’t have a basic app created you can open Xcode and hit **File-> New-> Project -> iOS**. Then select **App**. After you create your basic app you are ready to follow this guide.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/-iwt8golf8-OjxlZ5Y29W_image.png)



![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/x2hO0A18Ip_NBwkTbH_qd_image.png)
:::

## 1 - Choose your Installation Method

::::ExpandableHeading
### Swift Package Manager

**1.1 - Add the Parse Swift SDK Package - Swift Package Manager**

:::hint{type="info"}
Follow this step if you haven’t yet installed Parse iOS SDK.
:::

Newer versions of [**XCode**](https://developer.apple.com/xcode/) have the Swift Package Manager built in. This is the easiest and best way to install the Parse Swift SDK on your project and keep it updated.

Currently we only recommend using this method for installing the Parse Swift SDK.

Under the (File) menu, select (Swift Packages) and then (Add Package Dependency)

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/WNWUx2DQRnHc7zWOMZhG7_image.png)

On the (Choose Package Repository) window, paste the URL for the Parse Swift SDK github website ( https\://github.com/parse-community/Parse-Swift ) and click Next

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/dE6e5umL8vdVK48XjFdGx_image.png)

On the (Repository) window, you can select a Version, Branch or specific Commit. Choose the method you prefer and click Next

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Ga6Swwt7LymSKKbJiVFlL_image.png)

Wait for XCode to resolve all Parse-Swift dependencies and then click Next

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/-LhzW14lQHBbbD0w9EAsJ_image.png)

Check if ht package product ParseSwift is checked and your target is correctly selected on Add to Target, then click Next

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/5yvU_zsCXMc0r5bi0BKB1_image.png)

The Swift package should appear on the Dependencies tree right under your project, showing its version on the right side:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/L5Qvl3TXUkLwszlCu_qEu_image.png" signedSrc size="60" width="528" height="992" position="center" caption}

If you need to update the ParseSwift package, right click it under the Dependencies tree and choose Update Package. The process will automatically update everything for you.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Iht_rEnp6CCr3m2U_X3tT_image.png" signedSrc size="60" width="666" height="1232" position="center" caption}

Congratulations! You have now installed the Parse Swift iOS SDK
::::

::::ExpandableHeading
### Cocoapods

**1.1 - Install the Parse Swift iOS SDK**

:::hint{type="info"}
Follow this step if you haven’t yet installed Parse Swift iOS SDK.
:::

Xcode can use [**CocoaPods**](https://cocoapods.org/) as dependency manager for Swift and Objective-C Cocoa projects.

You can refer to [**CocoaPods Getting Started Guide**](https://guides.cocoapods.org/using/getting-started.html) for additional details.

To install CocoaPods, open your terminal, copy the following code snippet and paste it in to your terminal and hit return:

:::BlockQuote
$ sudo gem install cocoapods
:::

CocoaPods should install automatically after you enter your password. If there’s a problem you may need to upgrade your local version of Ruby.

Next open up the Xcode Project folder and open a terminal window in that folder.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/mq-QnkfRF0Cc0sjbgN6BC_image.png)

Now you are going to create a Podfile. Copy the following code snippet and paste it in to your terminal and hit return:

:::BlockQuote
$ pod init
:::

If your folder now shows your Podfile you did it correctly.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/6ErZwMqR9QICzyzgedlRT_image.png)

:::hint{type="danger"}
**Be careful,&#x20;**&#x49;f you don’t see the podfile make sure your terminal is actually inside the project folder..
:::

Next open your Podfile with Xcode or any text editor and under each target add “pod ‘Parse’”.

:::BlockQuote
pod 'ParseSwift'
:::

Your Podfile will look similar to this:

:::BlockQuote
platform \:ios, '14.0'

target 'Cocoapods\_ParseSwift' do
&#x20; \# Comment the next line if you don't want to use dynamic frameworks
&#x20; use\_frameworks!

&#x20; \# Pods for Cocoapods\_ParseSwift
&#x20; pod 'ParseSwift'

end
:::

Now you are going to add Parse Swift to your project. Make sure your terminal is opened to your project folder. Copy the following code snippet and paste it in to your terminal and hit return:

:::BlockQuote
$ pod install
:::

CocoaPods will rebuild the project as a workspace and your project will now look like this.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/79GE-ZlmH8y-zEPjEKJ9e_image.png)

If you have already opened your Xcode project close it. From now on you’ll open the workspace file instead of the project file. Double click on the workspace file to open it.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/xJMQtHVYYc370i3-v-yRz_image.png)

Congratulations! You have now installed the Parse iOS SDK
::::

## 2 - Connect your Parse App

1. Open your project’s AppDelegate.swift file to set up the app’s credentials.
2. Parse Swift iOS SDK uses these settings to connect to the Back4App servers.
3. At the top of the file you should see a function called ‘didFinishLaunchingWithOptions’.
4. Paste the following code snippet inside this function, and make sure it is above the line that says ‘return true’.

:::CodeblockTabs
AppDelegate.swift

```swift
1   ParseSwift.initialize(applicationId: "PASTE_YOUR_APPLICATION_ID_HERE", clientKey: "PASTE_YOUR_CLIENT_ID_HERE", serverURL: URL(string: "https://parseapi.back4app.com")!)
```
:::

At the top of your AppDelegate.swift file make sure to include Parse as a module by including the follwing code snippet right below ‘import UIKit’.

:::CodeblockTabs
AppDelegate.swift

```swift
1   import ParseSwift
```
:::

Your AppDelegate.swift file should now look like this:

:::CodeblockTabs
AppDelegate.swift

```swift
1   import UIKit
2   import ParseSwift
3
4   @main
5   class AppDelegate: UIResponder, UIApplicationDelegate {
6
7
8
9       func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
10          // Override point for customization after application launch.
11          ParseSwift.initialize(applicationId: "PASTE_YOUR_APPLICATION_ID_HERE", clientKey: "PASTE_YOUR_CLIENT_ID_HERE", serverURL: URL(string: "https://parseapi.back4app.com")!)
12          return true
13      }
14
15      // MARK: UISceneSession Lifecycle
16
17      func application(_ application: UIApplication, configurationForConnecting connectingSceneSession: UISceneSession, options: UIScene.ConnectionOptions) -> UISceneConfiguration {
18          // Called when a new scene session is being created.
19          // Use this method to select a configuration to create the new scene with.
20          return UISceneConfiguration(name: "Default Configuration", sessionRole: connectingSceneSession.role)
21      }
22
23      func application(_ application: UIApplication, didDiscardSceneSessions sceneSessions: Set<UISceneSession>) {
24          // Called when the user discards a scene session.
25          // If any sessions were discarded while the application was not running, this will be called shortly after application:didFinishLaunchingWithOptions.
26          // Use this method to release any resources that were specific to the discarded scenes, as they will not return.
27      }
28
29
30  }
```
:::

:::hint{type="danger"}
**Be careful,&#x20;**&#x49;f Xcode tells you there is **No Such Module ‘Parse’&#x20;**&#x74;here’s an easy solution. In Xcode open ‘Target > Build Settings > Search Paths > Framework Search Paths’ and then add two values: ‘$(PROJECT\_DIR)’ and ‘$(inherited)’. Xcode will now be able to find your Parse module.
:::

1. Go to your App Dashboard at Back4App website.
2. Navigate to app’s settings: Click on Features > Core Settingsblock> Server.
3. Return to your AppDelegate.swift file and paste your applicationId and clientKey.

:::hint{type="info"}
See more at our [**New Parse App guide**](https://www.back4app.com/docs/get-started/new-parse-app).
:::

## 3 - Test your connection

Open your ViewController.swift file.

At the top of the file make sure to include Parse as a module by including the follwing code snippet right below ‘import UIKit’.

:::CodeblockTabs
ViewController.swift

```swift
1   import ParseSwift
```
:::

Inside the function called ‘viewDidLoad’ add a snippet of code below the code that configures parse.

:::CodeblockTabs
ViewController.swift

```swift
1   testParseConnection()
```
:::

Then add a function below viewDidLoad() method.

:::CodeblockTabs
ViewController.swift

```swift
1	    struct GameScore: ParseObject {
2	        //: Those are required for Object
3	        var objectId: String?
4	        var createdAt: Date?
5	        var updatedAt: Date?
6	        var ACL: ParseACL?
7	
8	        //: Your own properties.
9	        var score: Int = 0
10	
11	        //: Custom initializer.
12	        init(score: Int) {
13	            self.score = score
14	        }
15	
16	        init(objectId: String?) {
17	            self.objectId = objectId
18	        }
19	    }
20	
21	    func testParseConnection(){
22	        let score = GameScore(score: 10)
23	        let score2 = GameScore(score: 3)
24	        score.save { result in
25	            switch result {
26	            case .success(let savedScore):
27	                assert(savedScore.objectId != nil)
28	                assert(savedScore.createdAt != nil)
29	                assert(savedScore.updatedAt != nil)
30	                assert(savedScore.ACL == nil)
31	                assert(savedScore.score == 10)
32	
33	                /*: To modify, need to make it a var as the value type
34	                    was initialized as immutable.
35	                */
36	                var changedScore = savedScore
37	                changedScore.score = 200
38	                changedScore.save { result in
39	                    switch result {
40	                    case .success(var savedChangedScore):
41	                        assert(savedChangedScore.score == 200)
42	                        assert(savedScore.objectId == savedChangedScore.objectId)
43	
44	                        /*: Note that savedChangedScore is mutable since it's
45	                            a var after success.
46	                        */
47	                        savedChangedScore.score = 500
48	
49	                    case .failure(let error):
50	                        assertionFailure("Error saving: \(error)")
51	                    }
52	                }
53	            case .failure(let error):
54	                assertionFailure("Error saving: \(error)")
55	            }
56	        }
57	    }
58	}
```
:::

1. Build your app in a device or simulator (Command+R).
2. Wait until the main screen appears.
3. Login at [**Back4App Website**](https://www.back4app.com/)
4. Find your app and click on Dashboard
5. Click on Core.
6. Go to Browser.

If everything works properly, you should find a class named GameScore and the saved objects in it.

## Next Steps

At this point, you have learned how to get started with iOS apps. You are now ready to explore [**Parse Server core features**](https://www.back4app.com/product/parse-server) and [**Back4App add-ons**](https://www.back4app.com/product/addons).&#x20;

:::hint{type="success"}
Learn more by walking around our[**&#x20;iOS Tutorials**](https://www.back4app.com/docs/ios/ios-app-template) or check [**Parse open source documentation for iOS SDK**](https://docs.parseplatform.org/ios/guide/).
:::

