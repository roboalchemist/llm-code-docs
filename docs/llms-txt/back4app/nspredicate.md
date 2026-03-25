# Source: https://docs-containers.back4app.com/docs/ios/nspredicate.md

---
title: Querying with NSPredicate
slug: docs/ios/nspredicate
description: Learn how to use NSPredicate to execute queries
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-11T18:29:18.025Z
updatedAt: 2025-01-16T21:00:02.467Z
---

# Querying with NSPredicate

## Introduction

In this section you will learn how to use NSPredicate to define your queries in Objective-C.

:::hint{type="success"}
At any time, you can access the complete Project built with this tutorial at our [**GitHub repository**](https://github.com/templates-back4app/iOS-install-SDK).
:::

## Prerequisites

In this tutorial we will use a basic app created in Objective-C with Xcode 9.1 and **iOS 11**.

:::hint{type="info"}
**To complete this tutorial, you need:**

- An app created at Back4App.
  - **Note:&#x20;**&#x46;ollow the [**New Parse App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create an app at Back4App.
- Xcode.
- Basic iOS app.
  - **Note:**&#x49;f you don’t have a basic app created you can open Xcode and hit **File-> New-> Project -> iOS**. Then select **App**. After you create your basic app you are ready to follow this guide.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/cNLdHv0CpMyIVzG3ZJa_v_image.png)



![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/BVaGv4xYWoLZlA-aWy8Q6_image.png)
:::

:::hint{type="danger"}
**Note:&#x20;**&#x50;arse iOS SDK works with iOS 7.0 or higher.
:::

## 1 - Get the template

Download the template at
[**Back4App’s GitHub repository**](https://github.com/back4app/ios-objective-c-quickstart-example/archive/master.zip), and unzip files in your project folder.

You can do that using the following command line:

:::BlockQuote
&#x20; $ curl -LOk https\://github.com/back4app/ios-objective-c-quickstart-example/archive/master.zip && unzip master.zip
:::

## 2 - Open the project template

1. Open Xcode.
2. Click on File->Open.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/o-vrZ2axir-Tgc_SQbLGU_image.png)

3\. Navigate to the project folder and double click on QuickStartObjcExampleApp.xcworkspace.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/N7i40E8hUhNvNYZxNtBSI_image.png)

&#x20;   4\. Wait for Xcode to open the project.

## 3 - Understandig the Difference

Usually for Objective-C you have two options for building queries: using the ‘PFQuery’ or the ‘NSPredicate’. Both work similarly but depending on how many constraints you want to use, it might make more sense using one instead of the other.

For instance, a simple query using PFQuery would be:

:::BlockQuote
1   \[query whereKey:@"playerName" notEqualTo:@"Michael Yabuti"];
2   \[query whereKey:@"playerAge" greaterThan:@18];
:::

But a more complex query could become

:::BlockQuote
1   \[query whereKey:@"playerName" notEqualTo:@"Michael Yabuti"];
2   \[query whereKey:@"playerAge" greaterThan:@18];
3   \[query whereKey:@"playerHeight" greaterThan:@180];
4   \[query whereKey:@"playerWeight" greaterThan:@80];
5   \[query whereKey:@"playerFavoriteColour" notEqualTo:@"blue"];
6   \[query whereKey:@"playerIsLeftHanded" equalTo:@true];
7   \[query whereKey:@"playerShoeSize" notEqualTo:@42];
8   \[query whereKey:@"playerLivingState" equalTo:@"Arizona"];
9   \[query whereKey:@"playerLivingCity" notEqualTo:@"Springfield"];
10  \[query whereKey:@"playerMothersName" equalTo:@"Jane"];
:::

So, depending on each case, you can choose to use ‘NSPredicate’ instead.
A simple query using ‘NSPredicate’ would be:

:::BlockQuote
1   NSPredicate \*predicate = \[NSPredicate predicateWithFormat:
@"playerName != 'Michael Yabuti' AND playerAge > 18"];
2   PFQuery \*query = \[PFQuery queryWithClassName:@"GameScore" predicate\:predicate];
:::

While a more complex query could become:

:::BlockQuote
1   NSPredicate \*predicate = \[NSPredicate predicateWithFormat:   @"playerName != 'Michael Yabuti' AND playerAge > 18 AND playerHeight > 180 AND playerWeight > 80 AND playerFavoriteColour != 'blue' AND playerIsLeftHanded = true AND playerShoeSize != 42 AND playerLivingState = 'Arizona' AND playerLivingCity != 'Springfield' AND playerMothersName = 'Jane'"];
2   PFQuery \*query = \[PFQuery queryWithClassName:@"GameScore" predicate\:predicate];
:::

## 4 - Executing your Query

You can, then, execute your query:

:::BlockQuote
1   \[query findObjectsInBackgroundWithBlock:^(NSArray \*objects, NSError \*error) \{
2     if (!error) \{
3       // Request succeeded
4     }
5   }];
:::

## Next Steps

At this point, you have learned how to get started with iOS apps.

:::hint{type="info"}
Learn more by walking around our[**&#x20;iOS Tutorials**](https://www.back4app.com/docs/ios/ios-app-template) or check [**Parse open source documentation for iOS SDK**](https://docs.parseplatform.org/ios/guide/).
:::

