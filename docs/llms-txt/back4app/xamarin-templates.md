# Source: https://docs-containers.back4app.com/docs/xamarin/xamarin-templates.md

---
title: Start from template
slug: docs/xamarin/xamarin-templates
description: In this guide you learn how to download and start using a complete(frontend and backend) Xamarin app template on Visual Studio.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-02-27T14:19:53.850Z
updatedAt: 2024-03-28T22:02:28.051Z
---

# Start your Xamarin project using a pre built template

## Introduction

In this section you learn how to get started with a Visual Studio template and get ready to use Back4App in 5 easy steps.

## Prerequisites

:::hint{type="info"}
**To complete this quickstart, you need:**

- [**Visual Studio**](https://visualstudio.microsoft.com/pt-br/) and [**Xamarin Dependency**](https://dotnet.microsoft.com/pt-br/apps/xamarin).
- An app created at Back4App. See more on [**New Parse App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app).
:::

## 1 - Get the template

Download the template at [**Back4App’s GitHub repository**](https://github.com/back4app/xamarin-quickstart-example).

You can do that using the following command line:

:::BlockQuote
&#x20;$ curl -LOk https\://github.com/back4app/xamarin-quickstart-example/archive/master.zip && unzip master.zip
:::

## 2 - Open the project template

1. Open Visual Studio.
2. Click on Open Project / Solution

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/so-iCN0G6PN0X9fptkLwd_image.png)

&#x20;    3\. Navigate to the project folder and click on Open.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/ZjUdMLg52SFaMIchsINc1_image.png)

## 3 - Install Required NuGet Packages

We need some additional libraries for this example. We will get them through Nuget Packages.

1. Right click on App’s name in the Solution Explorer and click on Manage NuGet Packages....

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/xEdKcXEhcPA4BaJeMmpMr_image.png)

&#x20;    2\. Press on Browse, search and install the packages parse by Parse and Xamarin.Android.Support.v7.AppCompat by Xamarin Inc..

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/q9KsmkOqBA37bCbY_7tkd_image.png)

&#x20;    3\. Wait for the installations to complete.

## 4 - Setup app’s credentials

Update your strings values to set up the app’s credentials. Parse Xamarin SDK uses these settings to connect to the Back4App servers.

1. Open your strings file: .../App1/Resources/values/strings.xml&#x20;

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/FQxsAoO4h5vUvcQ7g2lzP_image.png)

&#x20;    2\. Go to your App Dashboard at Back4App website.

&#x20;    3\. Navigate to app’s settings: Click on Features > Core Settings and press Settings.

&#x20;    4\. Return to your strings.xml file and paste your applicationId and dotNetKey.

:::hint{type="info"}
&#x20;See more at our [**Back4App’s Creating New App guide**](https://www.back4app.com/docs/get-started/new-parse-app).
:::



## 5 - Testing your connection

1. Build your app in a device or virtual device ( Shift + F10).

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/T6hqZuL1cps6rAtgNCpEG_image.png)

&#x20;       2\. Wait until the Hello World! screen appears as below.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/n0SHe6T2l7E_KiwP2mQ8d_image.png" signedSrc size="50" width="720" height="1280" position="center" caption}

&#x20;       3\. Login at [**Back4App**](https://www.back4app.com/).

&#x20;       4\. Find your app and click on Dashboard.

&#x20;       5\. Click on Core.

&#x20;       6\. Go to Browser.

If everything works properly, you should find a class named Installation as follows:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/ZLsk-nIXi_Kx43i0IjbXc_image.png)

## Next Steps

At this point, you have learned how to get started with Android apps. You are now ready to explore [**Parse Server core features**](https://www.back4app.com/product/parse-server) and [**Back4App add-ons**](https://www.back4app.com/product/addons).

Learn more by walking around [**Parse open source documentation for .NET SDK**](http://docs.parseplatform.org/dotnet/guide/).

