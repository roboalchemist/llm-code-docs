# Source: https://docs-containers.back4app.com/docs/ios/graphql/swift-graphql.md

---
title: Using GraphQL Apollo iOS Client in a Swift Project
slug: docs/ios/graphql/swift-graphql
description: Learn how to use the GraphQL Apollo iOS Client into your Swift project
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-12T14:02:29.968Z
updatedAt: 2025-01-17T18:51:50.319Z
---

## Introduction

In this section you will learn how to install the Apollo iOS Client on your Swift project and query data from Back4app using it.

## Prerequisites

:::hint{type="info"}
**To complete this quickstart, you need:**

- Xcode.
- An app created at Back4App.
  - Follow the [**New Parse App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create a Parse app at Back4App.
:::

- A Class with some data stored (so you can retrieve it).

## 1 - Getting Apollo Client into your XCode Project

The easiest way to integrate the Apollo iOS Client is by using [**CocoaPods**](https://cocoapods.org/). In order to integrate it, follow these steps:

1. Create your XCode project and in the same folder of your .xcodeproj file, create a new file named Podfile

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/PEUfa1YovxMtVmHjTMbSx_image.png)

1. Edit the Podfile file and add the following code, changing the string YourProjectNameHere to your project’s name:

```ruby
# Uncomment the next line to define a global platform for your project
 platform :ios, '12.0'

 target 'YourProjectNameHere' do
 # Comment the next line if you're not using Swift and don't want to use dynamic frameworks
 use_frameworks!

 # Pods for ConferencePlanner
 pod 'Apollo'

 end
```

1. Save the file and open a terminal. Go to that folder and type:

:::BlockQuote
pod install
:::

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/ZZl780kGZg-WYcpBiKM-5_image.png)

1. When the installation finishes, you should have a new file with the format .xcworkspace. Open that file with Xcode.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/QfRd01OyKsYTkJg_1Ukjj_image.png)

## 2 - Retrieve your Schemas

You need a file name schema.json containing the Schemas for your GraphQL endpoint. There are two ways for you to retrieve your full Schema:

1. Using the Back4app GraphQL Console
2. Using Apollo

We will discuss both. Choose the one you like the best.

### 2.1 - Retrieve your Schemas with the Back4app GraphQL Console

Go to your GraphQL Console for the App you want to retrieve the schema from and on, the right hand under the Schema tab, click the Download button.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/9xb-cnkV0mslqAG6-jcq5_image.png)

### 2.2 - Retrieve your Schemas with Apollo

If you prefer to use Apollo, first you have to install the Desktop version by typing:

:::BlockQuote
npm install -g apollo
:::

Then, run the following command replacing the values for the headers with your AppId and Masterkey:

:::BlockQuote
apollo client --endpoint=[**https://parseapi.back4app.com/graphql**](https://parseapi.back4app.com/graphql) --header="X-Parse-Application-Id: YourAppIdHere" --header="X-Parse-Master-Key: YourMasterKeyHere"
:::

This will generate aschema.json file as output

## 3 - Add your Schema.json file to the project

Add the schema.json file that you downloaded or retrieved to your project in the root directory. This is the same folder where your AppDelegate.swift file is located.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/v9dpqhKpw7IaDvEF7ssNE_image.png)

## 4 - Create your GraphQL files

You now can create your GraphQL files with your files and mutations.
Those file must have the .graphql extension and cointain at least one query or mutation in order for Apollo to crate the Swift code from.

A useful convention is to colocate queries, mutations or fragments with the Swift code that uses them by creating \<name>.graphql next to \<name>.swift.

If you don’t have pre-existing .graphql files in your file tree, create a very simple query and add it to a .graphql file in your file tree so that when you run the code generation build step, it actually finds something. If you don’t, you’ll get the error No operations or fragments found to generate code for.

Here is a simple query that as an example, that returns Parse users:

```graphql
1   query findAllUsers{
2     objects{
3       find_User{
4         count
5         results{
6           username
7         }
8       }
9     }
10  }
```

Add that file to your Target directory at the same level your schema.json file is:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/uWcuy8aTL1cGATaqNejYM_image.png)

## 5 - Add a code generation build step

You can invoke apollo as part of the Xcode build process, which will retrieve and update the schema.json file automatically so your classes will always reflect any changes you make by calling the check-and-run-apollo-cli.sh wrapper script.

The wrapper checks if the version of Apollo installed on your system is compatible with the framework version in your project.
If you don’t check that, you could potentially generate code that is incompatible with the runtime code in the framework.

The steps are:

1. On your application target’s Build Phases settings tab, click the + icon and choose New Run Script Phase.
2. In the created Run Script, change its name to Generate Apollo GraphQL API.
3. Drag this new run script just above Compile Sources in your list of Build Phases so that it executes before your code is compiled.
4. Add the following to the Run Script:

:::BlockQuote
SCRIPT\_PATH="$\{PODS\_ROOT}/Apollo/scripts"
cd "$\{SRCROOT}/$\{TARGET\_NAME}"
"$\{SCRIPT\_PATH}"/check-and-run-apollo-cli.sh codegen --target=swift --includes=./\*\*/\*.graphql --localSchemaFile="schema.json" API.swift
:::

If you are using XCode 11 Beta, add this script instead:

:::BlockQuote
\# Go to the build root and go back up to where SPM keeps the apollo iOS framework checked out.
cd "$\{BUILD\_ROOT}"
cd "../../SourcePackages/checkouts/apollo-ios/scripts"APOLLO\_SCRIPT\_PATH="$(pwd)"if \[ -z "$\{APOLLO\_SCRIPT\_PATH}" ]; then
echo "error: Couldn't find the CLI script in your checked out SPM packages; make sure to add the framework to your project."
exit 1
ficd "$\{SRCROOT}/$\{TARGET\_NAME}"
"$\{APOLLO\_SCRIPT\_PATH}"/check-and-run-apollo-cli.sh codegen --target=swift --includes=./\*\*/\*.graphql --localSchemaFile="schema.json" API.swift
:::

## 6 - Build and add your API file to the target

Build your project and a file named API.swift should be created on your Target’s directory:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/thnYgBrzLVGMa9km99xEM_image.png)

Drag the generated API.swift file to your target and make sure to uncheck the “Copy Files If Needed” checkbox:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/VyC5uBcLau99P9-M6EPvg_image.png)

Make sure you checked all the Targets the API file needs to be included in.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/xaX63Ky-ADCvHITAbPCC2_image.png" signedSrc size="60" width="266" height="394" position="center" caption alt}

## 7 - Configure the Client

Now on your ViewController.swift, create your Apollo configuration and change your AppId and ClientKey values:

```swift
1   let apollo: ApolloClient = {
2       let configuration = URLSessionConfiguration.default
3       configuration.httpAdditionalHeaders = [
4           "X-Parse-Application-Id": "YourAppIdHere",
5           "X-Parse-Client-Key": "YourClientKeyHere"
6       ]
7
8       let url = URL(string: "https://parseapi.back4app.com/graphql")!
9   
10      return ApolloClient(
11          networkTransport: HTTPNetworkTransport(
12              url: url,
13              configuration: configuration
14          )
15      )
16  }()
```

## 8 - Configure the Client

On your viewDidLoad, call your GraphQL query from the Apollo client:

```swift
1   apollo.fetch(query: FindAllUsersQuery()) { result in
2       guard let data = try? result.get().data else { return }
3       print(data.objects?.findUser.results[0].username)
4   }
```

If you have any users in your User class, the first one (index 0) should be retrieved:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/8QfZCn__MDZsnj1VrTftc_image.png)

## Optional Step - Get syntax highlighting

You can have GraphQL syntax highlighting on XCode if you wish. To achieve that:

1. Clone the [**xcode-apollo repository**](https://github.com/apollostack/xcode-apollo) to your computer.
2. Close Xcode if it is currently running.
3. You may need to create these folders inside of \~/Library/Developer/Xcode:

:::BlockQuote
mkdir \~/Library/Developer/Xcode/Plug-ins \~/Library/Developer/Xcode/Specifications
:::

&#x20;   4\. Copy GraphQL.ideplugin to \~/Library/Developer/Xcode/Plug-ins.

:::BlockQuote
cp -R GraphQL.ideplugin \~/Library/Developer/Xcode/Plug-ins
:::

&#x20;    5\. Copy GraphQL.xclangspec to \~/Library/Developer/Xcode/Specifications.

:::BlockQuote
cp -R GraphQL.xclangspec \~/Library/Developer/Xcode/Specifications
:::

You may receive a warning the first time you start up Xcode after installing these add-ons. Once you agree to load the plugin, you will no longer see this warning.
