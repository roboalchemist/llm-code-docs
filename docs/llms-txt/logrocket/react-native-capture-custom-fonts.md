# Source: https://docs.logrocket.com/reference/react-native-capture-custom-fonts.md

# Capture Custom Fonts

Capture React Native application Custom Fonts

If you use custom fonts or icons and notice missing icons or incorrectly sized text in Session Replay, you may want to follow these instructions to upload your fonts on release builds. This will enable custom fonts to display in Session Replay. Custom font replay requires a minimum SDK version of 1.33.8.

Each platform, iOS and Android, has its own steps to configure custom font upload and capture. Font upload must be configured within the app's native Android and iOS build steps.

* [Android Custom Font configuration](https://docs.logrocket.com/reference/android-capture-custom-fonts#/)
* [iOS Custom Font configuration](https://docs.logrocket.com/reference/ios-capture-custom-fonts#/)

> 📘 Icons and fonts accessed through packages
>
> If your app utilizes any icons or fonts from third party packages you will need to add a copy of those font files to the correct directory so that the font files can be uploaded for replay. In iOS, this directory is defined by the `LOGROCKET_ASSET_DIR` build setting value. For Android, only files located at `android/app/src/main/assets/fonts` will be uploaded by default, though custom `assetDir` paths can be specified through the build.gradle config (see details [here](https://docs.logrocket.com/reference/android-capture-custom-fonts#font-resource-location)).