# Source: https://firebase.google.com/docs/ml-kit/ios/identify-languages.md.txt

> [!CAUTION]
> This page describes an old version of the Language Identification API, which was part
> of ML Kit for Firebase. Development of this API has been moved to the
> standalone ML Kit SDK, which you can use with or without Firebase.
> [Learn more](https://developers.google.com/ml-kit/migration).
>
> See
> [Identify the language of text with ML Kit on iOS](https://developers.google.com/ml-kit/language/identification/ios)
> for the latest documentation.


You can use ML Kit to identify the language of a string of text. You can
get the string's most likely language or get confidence scores for all of the
string's possible languages.

ML Kit recognizes text in 103 different languages in their native scripts.
In addition, romanized text can be recognized for Arabic, Bulgarian, Chinese,
Greek, Hindi, Japanese, and Russian.

<br />

## Before you begin

1. If you have not already added Firebase to your app, do so by following the steps in the [getting started guide](https://firebase.google.com/docs/ios/setup).
2. Include the ML Kit libraries in your Podfile:

   ```
   pod 'Firebase/MLNaturalLanguage', '6.25.0'
   pod 'Firebase/MLNLLanguageID', '6.25.0'
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

## Identify the language of a string

To identify the language of a string, get an instance of
`LanguageIdentification`, and then pass the string to the
`identifyLanguage(for:)` method.

For example:

### Swift

    let languageId = NaturalLanguage.naturalLanguage().languageIdentification()

    languageId.identifyLanguage(for: text) { (languageCode, error) in
      if let error = error {
        print("Failed with error: \(error)")
        return
      }
      if let languageCode = languageCode, languageCode != "und" {
        print("Identified Language: \(languageCode)")
      } else {
        print("No language was identified")
      }
    }

### Objective-C

    FIRNaturalLanguage *naturalLanguage = [FIRNaturalLanguage naturalLanguage];
    FIRLanguageIdentification *languageId = [naturalLanguage languageIdentification];

    [languageId identifyLanguageForText:text
                             completion:^(NSString * _Nullable languageCode,
                                          NSError * _Nullable error) {
                               if (error != nil) {
                                 NSLog(@"Failed with error: %@", error.localizedDescription);
                                 return;
                               }
                               if (languageCode != nil
                                   && ![languageCode isEqualToString:@"und"] ) {
                                 NSLog(@"Identified Language: %@", languageCode);
                               } else {
                                 NSLog(@"No language was identified");
                               }
                             }];

If the call succeeds, a
[BCP-47 language code](https://en.wikipedia.org/wiki/IETF_language_tag) is
passed to the completion handler, indicating the language of the text. See the
[complete list of supported languages](https://firebase.google.com/docs/ml-kit/langid-support). If no
language could be confidently detected, the code `und` (undetermined) is passed.

By default, ML Kit returns a non-`und` value only when it identifies the
language with a confidence value of at least 0.5. You can change this threshold
by passing a `LanguageIdentificationOptions` object to
`languageIdentification(options:)`:

### Swift

    let options = LanguageIdentificationOptions(confidenceThreshold: 0.4)
    let languageId = NaturalLanguage.naturalLanguage().languageIdentification(options: options)

### Objective-C

    FIRNaturalLanguage *naturalLanguage = [FIRNaturalLanguage naturalLanguage];
    FIRLanguageIdentificationOptions *options =
        [[FIRLanguageIdentificationOptions alloc] initWithConfidenceThreshold:0.4];
    FIRLanguageIdentification *languageId =
        [naturalLanguage languageIdentificationWithOptions:options];

## Get the possible languages of a string

To get the confidence values of a string's most likely languages, get an
instance of `LanguageIdentification`, and then pass the string to the
`identifyPossibleLanguages(for:)` method.

For example:

### Swift

    let languageId = NaturalLanguage.naturalLanguage().languageIdentification()

    languageId.identifyPossibleLanguages(for: text) { (identifiedLanguages, error) in
      if let error = error {
        print("Failed with error: \(error)")
        return
      }
      guard let identifiedLanguages = identifiedLanguages,
        !identifiedLanguages.isEmpty,
        identifiedLanguages[0].languageCode != "und"
      else {
        print("No language was identified")
        return
      }

      print("Identified Languages:\n" +
        identifiedLanguages.map {
          String(format: "(%@, %.2f)", $0.languageCode, $0.confidence)
          }.joined(separator: "\n"))
    }

### Objective-C

    FIRNaturalLanguage *naturalLanguage = [FIRNaturalLanguage naturalLanguage];
    FIRLanguageIdentification *languageId = [naturalLanguage languageIdentification];

    [languageId identifyPossibleLanguagesForText:text
                                      completion:^(NSArray<FIRIdentifiedLanguage *> * _Nonnull identifiedLanguages,
                                                   NSError * _Nullable error) {
      if (error != nil) {
        NSLog(@"Failed with error: %@", error.localizedDescription);
        return;
      }
      if (identifiedLanguages.count == 1
          && [identifiedLanguages[0].languageCode isEqualToString:@"und"] ) {
        NSLog(@"No language was identified");
        return;
      }
      NSMutableString *outputText = [NSMutableString stringWithFormat:@"Identified Languages:"];
      for (FIRIdentifiedLanguage *language in identifiedLanguages) {
        [outputText appendFormat:@"\n(%@, %.2f)", language.languageCode, language.confidence];
      }
      NSLog(outputText);
    }];

If the call succeeds, a list of `IdentifiedLanguage` objects is passed to the
continuation handler. From each object, you can get the language's BCP-47 code
and the confidence that the string is in that language. See the
[complete list of supported languages](https://firebase.google.com/docs/ml-kit/langid-support). Note that
these values indicate the confidence that the entire string is in the given
language; ML Kit doesn't identify multiple languages in a single string.

By default, ML Kit returns only languages with confidence values of at least
0.01. You can change this threshold by passing a
`LanguageIdentificationOptions` object to `languageIdentification(options:)`:

### Swift

    let options = LanguageIdentificationOptions(confidenceThreshold: 0.4)
    let languageId = NaturalLanguage.naturalLanguage().languageIdentification(options: options)

### Objective-C

    FIRNaturalLanguage *naturalLanguage = [FIRNaturalLanguage naturalLanguage];
    FIRLanguageIdentificationOptions *options =
        [[FIRLanguageIdentificationOptions alloc] initWithConfidenceThreshold:0.4];
    FIRLanguageIdentification *languageId =
        [naturalLanguage languageIdentificationWithOptions:options];

If no language meets this threshold, the list will have one item, with the value
`und`.