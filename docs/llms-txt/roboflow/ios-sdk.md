# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/sdks/ios-sdk.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/depuroi/sdks/ios-sdk.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/sdks/ios-sdk.md

# Source: https://docs.roboflow.com/deploy/sdks/ios-sdk.md

# iOS SDK

The Roboflow Mobile iOS SDK is a great option if you are developing an iOS application where having a model running on the edge (iPad or iPhone) is needed for faster inference or to unlock a new suite of features, capabilities, and use cases (like augmented reality).

Native mobile applications with custom computer vision models embedded in them allows developers to give their apps the sense of sight.

## Task Support

The following task types are supported by the hosted API:

| Task Type             | Supported by iOS SDK Deployment |
| --------------------- | ------------------------------- |
| Object Detection      | ✅                               |
| Classification        |                                 |
| Instance Segmentation | ✅ (iOS 18 or higher)            |
| Semantic Segmentation |                                 |

## Deploy a Model to an iOS Device

### Supported Hardware and Software

All iOS devices support on-device inference, but those older than the iPhone 8 (A11 Bionic Processor) will fall back to the less energy efficient gpu engine.

Roboflow requires a minimum iOS version of 15.4 (18.0 for instance segmentation models).

## Prototyping

You can develop against the [Roboflow Hosted Inference API](https://docs.roboflow.com/deploy/serverless). It uses the same trained models as on-device inference.

## Installation&#x20;

* Install [CocoaPods](https://guides.cocoapods.org/using/getting-started.html) | [Troubleshooting Guide](https://guides.cocoapods.org/using/troubleshooting#installing-cocoapods)

"CocoaPods is built with Ruby and it will be installable with the default Ruby available on macOS. You can use a Ruby Version manager, however, we recommend that you use the standard Ruby available on macOS unless you know what you're doing. Using the default Ruby install will require you to use `sudo` when installing gems. (This is only an issue for the duration of the gem installation, though.)" - [CocoaPods](https://guides.cocoapods.org/using/getting-started.html)

The "Sudo-less" installation is an option, if you do not want to grant RubyGems admin privileges for this process. However, note that the `sudo` installation is more typical.

Check that CocoaPods is successfully installed by entering `pod --version` in your Terminal.

### Installing the Roboflow CocoaPod

First, run `pod init` in your project directory.

Make sure the `Podfile` specifies the `platform :ios, '15.4'`

Next, add `pod 'Roboflow'` to your `Podfile`.

If you do not have the XCode Command Line Tools installed, run `xcode-select --install` in your Terminal.

This will return: `xcode-select: error: command line tools are alreadyinstalled, use "Software Update" to install updates` if the Command Line Tools are already present on your system.&#x20;

Lastly, run `pod install` and open the generated `.xcworkspace` file in [XCode](https://developer.apple.com/xcode/).

![Terminal after successful installation of the Podfile](https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-742fddf172d5eea914ea63a42170583cbe748443%2Fimage.png?alt=media)

![The project directory after successful installation of the Podfile](https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-85737dbd1b9fcb80ea6674633012e85c908f5c30%2Fimage.png?alt=media)

* If it returns this error: "You may have encountered a bug in the Ruby interpreter or extension libraries," then first run `brew install cocoapods`, and then run `pod install` and open the generated `.xcworkspace` file in XCode.
  * Check that CocoaPods is successfully installed by entering `pod --version` in your Terminal.

### Using Roboflow in Swift

Navigate to the `.xcworkspace` file in XCode.

![](https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-845222e3655098babfff65dff3575a9886c12c24%2Fimage.png?alt=media)

Next, import Roboflow by adding `import Roboflow`. to the `.xcworkspace` file.

Then, create an instance of the Roboflow API with `let rf = Roboflow(apiKey: "API_KEY")`. For `modelVersion`, replace `YOUR-MODEL-VERSION-#` with the integer value of your model's version number.

#### [Locating Your Project Information](https://docs.roboflow.com/deploy/sdks/broken-reference)

**Completion Handler Usage:**

```swift
import Roboflow
...
//initalize with your API Key
let rf = RoboflowMobile(apiKey: "API_KEY")
var model: RFModel?
...

//model is your model's project name
rf.load(model: "YOUR-MODEL-ID", modelVersion: YOUR-MODEL-VERSION-#) { [self] model, error, modelName, modelType in
    if error != nil {
        print(error?.localizedDescription as Any)
    } else {
        model?.configure(threshold: threshold, overlap: overlap, maxObjects: maxObjects
                            processingMode: .performance or .balanced or .quality, // instance seg
                            maxNumberPoints: max number of mask processing points) // instance seg
        self.model = model
    }
    
}
...

//model?.detect takes a UIImage and runs inference on it
let img = UIImage(named: "example.jpeg") // or CVPixelBuffer
model?.detect(image: img!) { predictions, error in
    if error != nil {
        print(error)
    } else {
        print(predictions)
    }
}
```

**Asynchronous Usage:**

To use asynchronously, you must invoke your Roboflow model within an asynchronous block.

```swift
import Roboflow
...
//initalize with your API Key
let rf = RoboflowMobile(apiKey: "API_KEY")
...

//model is your model's project name
let (model, loadingError, modelName, modelType) = await rf.load(model: "YOUR-MODEL-ID", modelVersion: YOUR-MODEL-VERSION-#)
model!.configure(threshold: threshold, overlap: overlap, maxObjects: maxObjects)
...

//model?.detect takes a UIImage and runs inference on it
let img = UIImage(named: "example.jpeg")
let (predictions, predictionError) = await model!.detect(image: img!)
print(predictions)
```

**Predictions Format:**

```
x:Float //center of object x
y:Float //center of object y
width:Float
height:Float
className:String
confidence:Float
color:UIColor
box:CGRect
points:[CGPoint] // instance segmentation models only
```

[CGRect](https://developer.apple.com/documentation/corefoundation/cgrect)

### Native Swift Example

The [roboflow-ios-starter](https://github.com/roboflow/roboflow-ios-starter) app is a great starting point for creating a realtime iOS app with roboflow models. It includes camera setup, model loading and process, and output drawing code for both object-detection and instance segmentation models.

### React Native Expo App Example

We also provide an example of integrating this SDK into an expo app with React Native here. You may find this useful when considering the construction of your own downstream application.&#x20;

Be sure that you have both [Expo](https://docs.expo.dev/) and [CocoaPods](https://cocoapods.org/) installed.

* `expo-cli` supports the following Node.js versions: `>=12.13.0 <15.0.0` (Maintenance LTS) and `>=16.0.0 <17.0.0` (Active LTS)
* The yarn package must be installed for Node.js (`npm install -g yarn`)

{% embed url="<https://github.com/roboflow-ai/RoboflowExpoExample>" %}

### Example iOS application - CashCounter

Download [CashCounter](https://apps.apple.com/app/roboflow-cash-counter/id1633812788), our example iOS app that counts US coins and bills, as an example of how you could deploy a computer vision model to an iPhone. You'll see examples of visualizing bounding boxes, FPS, object counting, image upload, and more.
