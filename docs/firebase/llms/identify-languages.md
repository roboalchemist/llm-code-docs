# Source: https://firebase.google.com/docs/ml-kit/ios/identify-languages.md.txt

# Source: https://firebase.google.com/docs/ml-kit/identify-languages.md.txt

# Source: https://firebase.google.com/docs/ml-kit/android/identify-languages.md.txt

| This page describes an old version of the Language Identification API, which was part of ML Kit for Firebase. Development of this API has been moved to the standalone ML Kit SDK, which you can use with or without Firebase.[Learn more](https://developers.google.com/ml-kit/migration).
|
| See[Identify the language of text with ML Kit on Android](https://developers.google.com/ml-kit/language/identification/android)for the latest documentation.

<br />

You can use ML Kit to identify the language of a string of text. You can get the string's most likely language or get confidence scores for all of the string's possible languages.

ML Kit recognizes text in 103 different languages in their native scripts. In addition, romanized text can be recognized for Arabic, Bulgarian, Chinese, Greek, Hindi, Japanese, and Russian.

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
     implementation 'com.google.firebase:firebase-ml-natural-language-language-id-model:20.0.7'
   }
   ```

## Identify the language of a string

To identify the language of a string, get an instance of`FirebaseLanguageIdentification`, and then pass the string to the`identifyLanguage()`method.

For example:  

    FirebaseLanguageIdentification languageIdentifier =
            FirebaseNaturalLanguage.getInstance().getLanguageIdentification();
    languageIdentifier.identifyLanguage(text)
          .addOnSuccessListener(
              new OnSuccessListener<String>() {
                @Override
                public void onSuccess(@Nullable String languageCode) {
                  if (languageCode != "und") {
                    Log.i(TAG, "Language: " + languageCode);
                  } else {
                    Log.i(TAG, "Can't identify language.");
                  }
                }
              })
          .addOnFailureListener(
              new OnFailureListener() {
                @Override
                public void onFailure(@NonNull Exception e) {
                  // Model couldn't be loaded or other internal error.
                  // ...
                }
              });

If the call succeeds, a[BCP-47 language code](https://en.wikipedia.org/wiki/IETF_language_tag)is passed to the success listener, indicating the language of the text. See the[complete list of supported languages](https://firebase.google.com/docs/ml-kit/langid-support). If no language could be confidently detected, the code`und`(undetermined) is passed.

By default, ML Kit returns a value other than`und`only when it identifies the language with a confidence value of at least 0.5. You can change this threshold by passing a`FirebaseLanguageIdentificationOptions`object to`getLanguageIdentification()`:  

    FirebaseLanguageIdentification languageIdentifier = FirebaseNaturalLanguage
            .getInstance()
            .getLanguageIdentification(
                    new FirebaseLanguageIdentificationOptions.Builder()
                            .setIdentifyLanguageConfidenceThreshold(0.34f)
                            .build());

## Get the possible languages of a string

To get the confidence values of a string's most likely languages, get an instance of`FirebaseLanguageIdentification`, and then pass the string to the`identifyAllLanguages()`method.

For example:  

    FirebaseLanguageIdentification languageIdentifier =
            FirebaseNaturalLanguage.getInstance().getLanguageIdentification();
    languageIdentifier.identifyAllLanguages(text)
          .addOnSuccessListener(
              new OnSuccessListener<String>() {
                @Override
                public void onSuccess(List<IdentifiedLanguage> identifiedLanguages) {
                  for (IdentifiedLanguage identifiedLanguage : identifiedLanguages) {
                    String language = identifiedLanguage.getLanguageCode();
                    float confidence = identifiedLanguage.getConfidence();
                    Log.i(TAG, language + " (" + confidence + ")");
                  }
                }
              })
          .addOnFailureListener(
              new OnFailureListener() {
                @Override
                public void onFailure(@NonNull Exception e) {
                  // Model couldn't be loaded or other internal error.
                  // ...
                }
              });

If the call succeeds, a list of`IdentifiedLanguage`objects is passed to the success listener. From each object, you can get the language's BCP-47 code and the confidence that the string is in that language. See the[complete list of supported languages](https://firebase.google.com/docs/ml-kit/langid-support). Note that these values indicate the confidence that the entire string is in the given language; ML Kit doesn't identify multiple languages in a single string.

By default, ML Kit returns only languages with confidence values of at least 0.01. You can change this threshold by passing a`FirebaseLanguageIdentificationOptions`object to`getLanguageIdentification()`:  

    FirebaseLanguageIdentification languageIdentifier = FirebaseNaturalLanguage
            .getInstance()
            .getLanguageIdentification(
                    new FirebaseLanguageIdentificationOptions.Builder()
                            .setIdentifyAllLanguagesConfidenceThreshold(0.5f)
                            .build());

If no language meets this threshold, the list will have one item, with the value`und`.