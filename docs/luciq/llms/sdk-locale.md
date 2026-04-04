# Source: https://docs.luciq.ai/kmp/setup-luciq-for-kmp/custom-settings/sdk-customization/sdk-locale.md

# Source: https://docs.luciq.ai/flutter/setup-luciq-for-flutter/custom-settings/sdk-customization/sdk-locale.md

# Source: https://docs.luciq.ai/react-native/setup-luciq-for-react-native/custom-settings/sdk-customization/sdk-locale.md

# Source: https://docs.luciq.ai/android/set-up-luciq-for-android/sdk-customizations/sdk-locale.md

# Source: https://docs.luciq.ai/ios/setup-luciq-for-ios/custom-settings/sdk-customization/sdk-locale.md

# SDK Locale

### Setting the locale

The SDK will automatically use the current locale of your user's device, however, you can override it with the following method.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
Luciq.setLocale(.french)
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
[Luciq setLocale:LCQLocaleFrench];
```

{% endcode %}
{% endtab %}
{% endtabs %}

Here are the possible locale values:

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
.arabic
.azerbaijani
.catalan
.catalanSpain
.chineseSimplified
.chineseTaiwan
.chineseTraditional
.czech
.danish
.dutch
.english
.french
.german
.italian
.japanese
.korean
.norwegian
.polish
.portuguese
.portugueseBrazil
.russian
.slovak
.spanish
.swedish
.turkish
.hungarian
.finnish
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
LCQLocaleArabic    
LCQLocaleChineseSimplified    
LCQLocaleChineseTaiwan
LCQLocaleChineseTraditional
LCQLocaleCzech
LCQLocaleDanish
LCQLocaleDutch
LCQLocaleEnglish
LCQLocaleFrench
LCQLocaleGerman
LCQLocaleItalian
LCQLocaleJapanese
LCQLocaleKorean
LCQLocaleNorwegian
LCQLocalePolish
LCQLocalePortugese
LCQLocalePortugueseBrazil
LCQLocaleRussian
LCQLocaleSlovak
LCQLocaleSpanish
LCQLocaleSwedish
LCQLocaleTurkish
```

{% endcode %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}

### Dashboard Language

At the moment, the Luciq dashboard only supports English. Changing the SDK locale will not change the language of your dashboard.
{% endhint %}

#### Overriding String Values

You can also override each string shown to your users individually using the following method.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
Luciq.setValue("Please enter a correct email address", forStringWithKey: kIBGInvalidEmailTitleStringName)
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
[Luciq setValue:@"Please enter a correct email address" forStringWithKey:kLCQInvalidEmailTitleStringName];
```

{% endcode %}
{% endtab %}
{% endtabs %}

Here are the possible keys:

{% tabs %}
{% tab title="Constants" %}
{% code overflow="wrap" %}

```swift
kLCQStartAlertTextStringName
kLCQShakeStartAlertTextStringName
kLCQTwoFingerSwipeStartAlertTextStringName
kLCQEdgeSwipeStartAlertTextStringName
kLCQScreenshotStartAlertTextStringName
kLCQInvalidEmailMessageStringName
kLCQInvalidEmailTitleStringName
kLCQInsufficientContentTitleStringName
kLCQInsufficientContentMessageStringName
kLCQInvocationTitleStringName
kLCQAskAQuestionStringName
kLCQReportBugStringName
kLCQReportFeedbackStringName
kLCQReportBugDescriptionStringName
kLCQReportFeedbackDescriptionStringName
kLCQReportQuestionDescriptionStringName
kLCQRequestFeatureDescriptionStringName
kLCQEmailFieldPlaceholderStringName
kLCQCommentFieldPlaceholderForBugReportStringName
kLCQCommentFieldPlaceholderForFeedbackStringName
kLCQCommentFieldPlaceholderForQuestionStringName
kLCQChatReplyFieldPlaceholderStringName
kLCQAddScreenRecordingMessageStringName
kLCQAddVoiceMessageStringName
kLCQAddImageFromGalleryStringName
kLCQAddExtraScreenshotStringName
kLCQAudioRecordingPermissionDeniedTitleStringName
kLCQAudioRecordingPermissionDeniedMessageStringName
kLCQScreenRecordingPermissionDeniedMessageStringName
kLCQMicrophonePermissionAlertSettingsButtonTitleStringName
kLCQMicrophonePermissionAlertLaterButtonTitleStringName
kLCQChatsTitleStringName
kLCQTeamStringName
kLCQRecordingMessageToHoldTextStringName
kLCQRecordingMessageToReleaseTextStringName
kLCQMessagesNotificationTitleSingleMessageStringName
kLCQMessagesNotificationTitleMultipleMessagesStringName
kLCQScreenshotTitleStringName
kLCQOkButtonTitleStringName
kLCQSendButtonTitleStringName
kLCQCancelButtonTitleStringName
kLCQThankYouAlertTitleStringName
kLCQThankYouAlertMessageStringName
kLCQAudioStringName
kLCQScreenRecordingStringName
kLCQImageStringName
kLCQReachedMaximimNumberOfAttachmentsTitleStringName
kLCQReachedMaximimNumberOfAttachmentsMessageStringName
kLCQVideoRecordingFailureMessageStringName
kLCQSurveyEnterYourAnswerTextPlaceholder
kLCQVideoPressRecordTitle
kLCQCollectingDataText
kLCQLowDiskStorageTitle
kLCQLowDiskStorageMessage
kLCQInboundByLineMessage
kLCQExtraFieldIsRequiredText
kLCQExtraFieldMissingDataText
kLCQSurveyIntroTitleText
kLCQSurveyIntroDescriptionText
kLCQSurveyIntroTakeSurveyButtonText
kLCQStoreRatingThankYouTitleText
kLCQStoreRatingThankYouDescriptionText
kLCQCustomSurveyThankYouTitleText
kLCQCustomSurveyThankYouDescriptionText
kLCQSurveysNPSLeastLikelyStringName
kLCQSurveysNPSMostLikelyStringName
kLCQSurveyNextButtonTitle
kLCQSurveySubmitButtonTitle
kLCQSurveyAppStoreThankYouTitle
kLCQSurveyAppStoreButtonTitle
kLCQExpectedResultsStringName
kLCQActualResultsStringName
kLCQStepsToReproduceStringName
kLCQReplyButtonTitleStringName
kLCQFeatureRequestsTitle 
kLCQFeatureDetailsTitle 
kLCQStringFeatureRequestsRefreshText 
kLCQFeatureRequestSortingByRecentlyUpdatedText 
kLCQFeatureRequestSortingByTopVotesText 
kLCQFeatureRequestErrorStateTitleLabel 
kLCQFeatureRequestErrorStateDescriptionLabel 
kLCQBetaWelcomeMessageWelcomeStepTitle;
kLCQBetaWelcomeMessageWelcomeStepContent;
kLCQBetaWelcomeMessageHowToReportStepTitle;
kLCQBetaWelcomeMessageHowToReportStepContent;
kLCQBetaWelcomeMessageFinishStepTitle;
kLCQBetaWelcomeMessageFinishStepContent;
kLCQBetaWelcomeDoneButtonTitle;
kLCQLiveWelcomeMessageTitle;
kLCQLiveWelcomeMessageContent;
kLCQReproStepsListHeader
kLCQReproStepsListEmptyStateLabel
kLCQReproStepsListTitle
kLCQReproStepsListItemName
kLCQReproStepsDisclaimerBody
kLCQReproStepsDisclaimerLink
kLCQDiscardAlertTitle
kLCQDiscardAlertMessage
kLCQFrustratingExperienceStringName
kLCQCommentFieldPlaceholderForFrustratingExperienceStringName
kLCQCommentFieldFrustratingExperienceAccessibilityStringHint
```

{% endcode %}
{% endtab %}
{% endtabs %}
