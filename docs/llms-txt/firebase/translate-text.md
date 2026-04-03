# Source: https://firebase.google.com/docs/ml-kit/ios/translate-text.md.txt

# Source: https://firebase.google.com/docs/ml-kit/android/translate-text.md.txt

| This page describes an old version of the Translation API, which was part of ML Kit for Firebase. Development of this API has been moved to the standalone ML Kit SDK, which you can use with or without Firebase.[Learn more](https://developers.google.com/ml-kit/migration).
|
| See[Translate text with ML Kit on Android](https://developers.google.com/ml-kit/language/translation/android)for the latest documentation.

<br />

You can use ML Kit to translate text between languages. ML Kit currently supports translation between[59 languages](https://firebase.google.com/docs/ml-kit/translation-language-support).

<br />

## Before you begin

1. If you haven't already,[add Firebase to your Android project](https://firebase.google.com/docs/android/setup).
2. Add the dependencies for the ML Kit Android libraries to your module (app-level) Gradle file (usually`app/build.gradle`):  

   ```carbon
   apply plugin: 'com.android.application'
   apply plugin: 'com.google.gms.google-services'

   dependencies {
     // ...

     implementation 'com.google.firebase:firebase-ml-natural-language:22.0.0'
     implementation 'com.google.firebase:firebase-ml-natural-language-translate-model:20.0.8'
   }
   ```

## Translate a string of text

To translate a string between two languages:

1. Create a`FirebaseTranslator`object, configuring it with the source and target languages:

   ### Java

       // Create an English-German translator:
       FirebaseTranslatorOptions options =
               new FirebaseTranslatorOptions.Builder()
                       .setSourceLanguage(FirebaseTranslateLanguage.EN)
                       .setTargetLanguage(FirebaseTranslateLanguage.DE)
                       .build();
       final FirebaseTranslator englishGermanTranslator =
               FirebaseNaturalLanguage.getInstance().getTranslator(options);

   ### Kotlin

       // Create an English-German translator:
       val options = FirebaseTranslatorOptions.Builder()
               .setSourceLanguage(FirebaseTranslateLanguage.EN)
               .setTargetLanguage(FirebaseTranslateLanguage.DE)
               .build()
       val englishGermanTranslator = FirebaseNaturalLanguage.getInstance().getTranslator(options)

   If you don't know the language of the input text, you can use the[language identification API](https://firebase.google.com/docs/ml-kit/identify-languages)first. (But be sure you don't keep too many language models on the device at once.)
2. Make sure the required translation model has been downloaded to the device. Don't call`translate()`until you know the model is available.

   ### Java

       FirebaseModelDownloadConditions conditions = new FirebaseModelDownloadConditions.Builder()
           .requireWifi()
           .build();
       englishGermanTranslator.downloadModelIfNeeded(conditions)
             .addOnSuccessListener(
                 new OnSuccessListener<Void>() {
                   @Override
                   public void onSuccess(Void v) {
                     // Model downloaded successfully. Okay to start translating.
                     // (Set a flag, unhide the translation UI, etc.)
                   }
                 })
             .addOnFailureListener(
                 new OnFailureListener() {
                   @Override
                   public void onFailure(@NonNull Exception e) {
                     // Model couldn't be downloaded or other internal error.
                     // ...
                   }
                 });

   ### Kotlin

       englishGermanTranslator.downloadModelIfNeeded()
               .addOnSuccessListener {
                   // Model downloaded successfully. Okay to start translating.
                   // (Set a flag, unhide the translation UI, etc.)
               }
               .addOnFailureListener { exception ->
                   // Model couldn't be downloaded or other internal error.
                   // ...
               }

   Language models are around 30MB, so don't download them unnecessarily, and only download them using WiFi, unless the user has specified otherwise. You should also delete unneeded models. See[Explicitly manage translation models](https://firebase.google.com/docs/ml-kit/android/translate-text#manage_models).
3. After you confirm the model has been downloaded, pass a string of text in the source language to`translate()`:

   ### Java

       englishGermanTranslator.translate(text)
             .addOnSuccessListener(
                 new OnSuccessListener<String>() {
                   @Override
                   public void onSuccess(@NonNull String translatedText) {
                     // Translation successful.
                   }
                 })
             .addOnFailureListener(
                 new OnFailureListener() {
                   @Override
                   public void onFailure(@NonNull Exception e) {
                     // Error.
                     // ...
                   }
                 });

   ### Kotlin

       englishGermanTranslator.translate(text)
               .addOnSuccessListener { translatedText ->
                   // Translation successful.
               }
               .addOnFailureListener { exception ->
                    // Error.
                    // ...
               }

   The translated text, in the target language you configured, is passed to the success listener.

## Explicitly manage translation models

<br />

When you use the translation API as described above, ML Kit automatically downloads language-specific translation models to the device as required. You can also explicitly manage the translation models you want available on the device by using ML Kit's translation model management API. This can be useful if you want to download models ahead of time, or delete unneeded models from the device.

<br />

### Java

    FirebaseModelManager modelManager = FirebaseModelManager.getInstance();

    // Get translation models stored on the device.
    modelManager.getDownloadedModels(FirebaseTranslateRemoteModel.class)
            .addOnSuccessListener(new OnSuccessListener<Set<FirebaseTranslateRemoteModel>>() {
                @Override
                public void onSuccess(Set<FirebaseTranslateRemoteModel> models) {
                    // ...
                }
            })
            .addOnFailureListener(new OnFailureListener() {
                @Override
                public void onFailure(@NonNull Exception e) {
                    // Error.
                }
            });

    // Delete the German model if it's on the device.
    FirebaseTranslateRemoteModel deModel =
            new FirebaseTranslateRemoteModel.Builder(FirebaseTranslateLanguage.DE).build();
    modelManager.deleteDownloadedModel(deModel)
            .addOnSuccessListener(new OnSuccessListener<Void>() {
                @Override
                public void onSuccess(Void v) {
                    // Model deleted.
                }
            })
            .addOnFailureListener(new OnFailureListener() {
                @Override
                public void onFailure(@NonNull Exception e) {
                    // Error.
                }
            });

    // Download the French model.
    FirebaseTranslateRemoteModel frModel =
            new FirebaseTranslateRemoteModel.Builder(FirebaseTranslateLanguage.FR).build();
    FirebaseModelDownloadConditions conditions = new FirebaseModelDownloadConditions.Builder()
            .requireWifi()
            .build();
    modelManager.download(frModel, conditions)
            .addOnSuccessListener(new OnSuccessListener<Void>() {
                @Override
                public void onSuccess(Void v) {
                    // Model downloaded.
                }
            })
            .addOnFailureListener(new OnFailureListener() {
                @Override
                public void onFailure(@NonNull Exception e) {
                    // Error.
                }
            });

### Kotlin

    val modelManager = FirebaseModelManager.getInstance()

    // Get translation models stored on the device.
    modelManager.getDownloadedModels(FirebaseTranslateRemoteModel::class.java)
        .addOnSuccessListener { models ->
            // ...
        }
        .addOnFailureListener {
            // Error.
        }

    // Delete the German model if it's on the device.
    val deModel = FirebaseTranslateRemoteModel.Builder(FirebaseTranslateLanguage.DE).build()
    modelManager.deleteDownloadedModel(deModel)
        .addOnSuccessListener {
            // Model deleted.
        }
        .addOnFailureListener {
            // Error.
        }

    // Download the French model.
    val frModel = FirebaseTranslateRemoteModel.Builder(FirebaseTranslateLanguage.FR).build()
    val conditions = FirebaseModelDownloadConditions.Builder()
        .requireWifi()
        .build()
    modelManager.download(frModel, conditions)
        .addOnSuccessListener {
            // Model downloaded.
        }
        .addOnFailureListener {
            // Error.
        }