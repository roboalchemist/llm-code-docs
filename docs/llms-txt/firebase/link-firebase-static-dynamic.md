# Source: https://firebase.google.com/docs/ios/link-firebase-static-dynamic.md.txt

<br />

Beginning with CocoaPods 1.9.0 and Firebase 7, you can choose whether your Firebase dependencies are built as static or dynamic frameworks. We recommend using static frameworks unless you require certain dynamic library behaviors.

Note that libraries developed outside of GitHub can only be linked statically even with CocoaPods 1.9.0 and later. Currently, this library list includesAdMob,Analytics,Firebase ML, andPerformance Monitoring. All other distribution channels, including the zip file, Swift Package Manager, and Carthage provide statically linked libraries only.

This document assumes a working knowledge of dynamic and static linking on Apple platforms. If you're unfamiliar with these concepts, take a look at the following documentation:

- [Mach-O Programming Topics](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/MachOTopics/0-Introduction/introduction.html#//apple_ref/doc/uid/TP40001827-SW1)
- [Dynamic Library Programming Topics](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/DynamicLibraries/000-Introduction/Introduction.html)
- [Using Firebase in libraries](https://github.com/firebase/firebase-ios-sdk/blob/master/docs/firebase_in_libraries.md)

Since this document is concerned with the types of library linkage and not the loading of non-executable resource bundles, the terms*library* and*framework*are used interchangeably.

## Static linking

Statically linked libraries are bundled into your application executable at build time. As a result, the object files in the static library will be present in your app when it launches and do not need to be resolved at app-launch time by the dynamic linker. Consequently, apps using static linking will launch faster. This comes at the expense of a slightly larger binary / app executable, although it should be noted that the larger executable size will be offset by the lack of bundled dynamic libraries.

You can force static linking of Firebase dependencies by explicitly specifying the linkage in your Podfile:  

    # cocoapods >= 1.9.0
    use_frameworks! :linkage => :static

| **Note:** Swift Package Manager, Carthage, and the zip file provide statically linked libraries only.

## Dynamic linking

Dynamically linked libraries are stored in your app bundle separately from your app's main executable, and they must be loaded at app-launch time by the dynamic linker. Apple's frameworks are all linked dynamically to enable code-sharing between processes; similarly, you can use dynamic frameworks to share code between your app and extension targets. You cannot share dynamic frameworks between separate applications, even if they are both signed by the same developer.

If you want to use Firebase as a dependency of a dynamic framework target, you also need to link Firebase dynamically; otherwise you'll run into[duplicate class definitions](https://github.com/firebase/firebase-ios-sdk/blob/master/docs/firebase_in_libraries.md)in your app's runtime. Dynamic linking is the default behavior with`use_frameworks!`, but you can still explicitly specify dynamic linkage in your Podfile:  

    # cocoapods >= 1.9.0
    use_frameworks! :linkage => :dynamic

Note that dynamic linking may increase your app's launch time, especially if your app has a lot of dependencies.
| **Note:** Swift Package Manager, Carthage, and the zip file provide statically linked libraries only.