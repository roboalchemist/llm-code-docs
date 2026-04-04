# Source: https://firebase.google.com/docs/ml-kit/ios/translate-text.md.txt

> [!CAUTION]
> This page describes an old version of the Translation API, which was part
> of ML Kit for Firebase. Development of this API has been moved to the
> standalone ML Kit SDK, which you can use with or without Firebase.
> [Learn more](https://developers.google.com/ml-kit/migration).
>
> See
> [Translate text with ML Kit on iOS](https://developers.google.com/ml-kit/language/translation/ios)
> for the latest documentation.


You can use ML Kit to translate text between languages. ML Kit
currently supports translation between
[59 languages](https://firebase.google.com/docs/ml-kit/translation-language-support).

<br />

## Before you begin

<br />

1. If you have not already added Firebase to your app, do so by following the steps in the [getting started guide](https://firebase.google.com/docs/ios/setup).
2. Include the ML Kit libraries in your Podfile:

   ```
   pod 'Firebase/MLNLTranslate', '6.25.0'
   ```
   After you install or update your project's Pods, be sure to open your Xcode project using its `.xcworkspace`.
3. In your app, import Firebase:

   #### Swift

   ```swift
   import Firebase
   ```

   #### Objective-C

   ```objective-c
   @import Firebase;
   ```

## Translate a string of text

To translate a string between two languages:

1. Create a `Translator` object, configuring it with the source and target
   languages:

   ### Swift

       // Create an English-German translator:
       let options = TranslatorOptions(sourceLanguage: .en, targetLanguage: .de)
       let englishGermanTranslator = NaturalLanguage.naturalLanguage().translator(options: options)

   ### Objective-C

       // Create an English-German translator:
       FIRTranslatorOptions *options =
           [[FIRTranslatorOptions alloc] initWithSourceLanguage:FIRTranslateLanguageEN
                                                 targetLanguage:FIRTranslateLanguageDE];
       FIRTranslator *englishGermanTranslator =
           [[FIRNaturalLanguage naturalLanguage] translatorWithOptions:options];

   If you don't know the language of the input text, you can use the [language
   identification API](https://firebase.google.com/docs/ml-kit/identify-languages) first. (But be sure you
   don't keep too many language models on the device at once.)
2. Make sure the required translation model has been downloaded to the device.
   Don't call `translate(_:completion:)` until you know the model is available.

   ### Swift

       let conditions = ModelDownloadConditions(
           allowsCellularAccess: false,
           allowsBackgroundDownloading: true
       )
       englishGermanTranslator.downloadModelIfNeeded(with: conditions) { error in
           guard error == nil else { return }

           // Model downloaded successfully. Okay to start translating.
       }

   ### Objective-C

       FIRModelDownloadConditions *conditions =
           [[FIRModelDownloadConditions alloc] initWithAllowsCellularAccess:NO
                                                allowsBackgroundDownloading:YES];
       [englishGermanTranslator downloadModelIfNeededWithConditions:conditions
                                                         completion:^(NSError *_Nullable error) {
         if (error != nil) {
           return;
         }
         // Model downloaded successfully. Okay to start translating.
       }];

   Language models are around 30MB, so don't download them unnecessarily, and
   only download them using WiFi, unless the user has specified otherwise. You
   should also delete unneeded models.
   See [Explicitly manage translation models](https://firebase.google.com/docs/ml-kit/ios/translate-text#manage_models).
3. After you confirm the model has been downloaded, pass a string of text in
   the source language to `translate(_:completion:)`:

   ### Swift

       englishGermanTranslator.translate(text) { translatedText, error in
           guard error == nil, let translatedText = translatedText else { return }

           // Translation succeeded.
       }

   ### Objective-C

       [englishGermanTranslator translateText:text
                                   completion:^(NSString *_Nullable translatedText,
                                                NSError *_Nullable error) {
         if (error != nil || translatedText == nil) {
           return;
         }

         // Translation succeeded.
       }];

   ML Kit translates the text to the target language you configured and
   passes the translated text to the completion handler.

## Explicitly manage translation models


When you use the translation API as described above, ML Kit automatically
downloads language-specific translation models to the device as required. You
can also explicitly manage the translation models you want available on the
device by using ML Kit's translation model management API. This can be
useful if you want to download models ahead of time, or delete unneeded models
from the device.

<br />

To get the translation models stored on the device:

### Swift

    let localModels = ModelManager.modelManager().downloadedTranslateModels

### Objective-C

    NSSet<FIRTranslateRemoteModel *> *localModels =
        [FIRModelManager modelManager].downloadedTranslateModels;

To delete a model:

### Swift

    // Delete the German model if it's on the device.
    let deModel = TranslateRemoteModel.translateRemoteModel(language: .de)
    ModelManager.modelManager().deleteDownloadedModel(deModel) { error in
        guard error == nil else { return }
        // Model deleted.
    }

### Objective-C

    // Delete the German model if it's on the device.
    FIRTranslateRemoteModel *deModel =
        [FIRTranslateRemoteModel translateRemoteModelWithLanguage:FIRTranslateLanguageDE];
    [[FIRModelManager modelManager] deleteDownloadedModel:deModel
                                               completion:^(NSError * _Nullable error) {
                                                   if (error != nil) {
                                                       return;
                                                   }
                                                   // Model deleted.
                                               }];

To download a model:

### Swift

    // Download the French model.
    let frModel = TranslateRemoteModel.translateRemoteModel(language: .fr)

    // Keep a reference to the download progress so you can check that the model
    // is available before you use it.
    progress = ModelManager.modelManager().download(
        frModel,
        conditions: ModelDownloadConditions(
            allowsCellularAccess: false,
            allowsBackgroundDownloading: true
        )
    )

If you want to get the download status with `NotificationCenter`, register
observers for `firebaseMLModelDownloadDidSucceed` and
`firebaseMLModelDownloadDidFail`. Be sure to use a weak reference to `self`
in the observer block, since downloads can take some time, and the originating
object can be freed by the time the download finishes. For example:

    NotificationCenter.default.addObserver(
        forName: .firebaseMLModelDownloadDidSucceed,
        object: nil,
        queue: nil
    ) { [weak self] notification in
        guard let strongSelf = self,
            let userInfo = notification.userInfo,
            let model = userInfo[ModelDownloadUserInfoKey.remoteModel.rawValue]
                as? TranslateRemoteModel,
            model == frModel
            else { return }
        // The model was downloaded and is available on the device
    }

    NotificationCenter.default.addObserver(
        forName: .firebaseMLModelDownloadDidFail,
        object: nil,
        queue: nil
    ) { [weak self] notification in
        guard let strongSelf = self,
            let userInfo = notification.userInfo,
            let model = userInfo[ModelDownloadUserInfoKey.remoteModel.rawValue]
                as? TranslateRemoteModel
            else { return }
        let error = userInfo[ModelDownloadUserInfoKey.error.rawValue]
        // ...
    }

### Objective-C

    // Download the French model.
    FIRModelDownloadConditions *conditions =
        [[FIRModelDownloadConditions alloc] initWithAllowsCellularAccess:NO
                                             allowsBackgroundDownloading:YES];
    FIRTranslateRemoteModel *frModel =
        [FIRTranslateRemoteModel translateRemoteModelWithLanguage:FIRTranslateLanguageFR];

    // Keep a reference to the download progress so you can check that the model
    // is available before you use it.
    self.downloadProgress = [[FIRModelManager modelManager] downloadModel:frModel
                                                               conditions:conditions];

If you want to get the download status with `NSNotificationCenter`, register
observers for `FIRModelDownloadDidSucceedNotification` and
`FIRModelDownloadDidFailNotification`. Be sure to use a weak reference to
`self` in the observer block, since downloads can take some time, and the
originating object can be freed by the time the download finishes.

    __block MyViewController *weakSelf = self;

    [NSNotificationCenter.defaultCenter
     addObserverForName:FIRModelDownloadDidSucceedNotification
     object:nil
     queue:nil
     usingBlock:^(NSNotification * _Nonnull note) {
         if (weakSelf == nil | note.userInfo == nil) {
             return;
         }

         FIRTranslateRemoteModel *model = note.userInfo[FIRModelDownloadUserInfoKeyRemoteModel];
         if ([model isKindOfClass:[FIRTranslateRemoteModel class]]
             && model == frModel) {
             // The model was downloaded and is available on the device
         }
     }];

    [NSNotificationCenter.defaultCenter
     addObserverForName:FIRModelDownloadDidFailNotification
     object:nil
     queue:nil
     usingBlock:^(NSNotification * _Nonnull note) {
         if (weakSelf == nil | note.userInfo == nil) {
             return;
         }

         NSError *error = note.userInfo[FIRModelDownloadUserInfoKeyError];
     }];