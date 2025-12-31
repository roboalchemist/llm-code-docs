# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/safety-setting.md.txt

# Firebase.AI.SafetySetting Struct Reference

# Firebase.AI.SafetySetting

A type used to specify a threshold for harmful content, beyond which the model will return a fallback response instead of generated content.

## Summary

| ### Constructors and Destructors ||
|---|---|
| [SafetySetting](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/safety-setting#struct_firebase_1_1_a_i_1_1_safety_setting_1aa814818e842cf7c9223e515dc4f88abb)`(`[HarmCategory](https://firebase.google.com/docs/reference/unity/namespace/firebase/a-i#namespace_firebase_1_1_a_i_1ae7e954295da056c823c0963d6b457382)` category, `[HarmBlockThreshold](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/safety-setting#struct_firebase_1_1_a_i_1_1_safety_setting_1a85fe9bacee67c2a14b20c0b12493a488)` threshold, `[HarmBlockMethod](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/safety-setting#struct_firebase_1_1_a_i_1_1_safety_setting_1a236d10d84d894ee3cd989a39ceca83fc)`? method)` Initializes a new safety setting with the given category and threshold. ||

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              ### Public types                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| [HarmBlockMethod](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/safety-setting#struct_firebase_1_1_a_i_1_1_safety_setting_1a236d10d84d894ee3cd989a39ceca83fc)`{` ` `[Probability](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/safety-setting#struct_firebase_1_1_a_i_1_1_safety_setting_1a236d10d84d894ee3cd989a39ceca83fca0d2765b30694ee9f4fb7be2ae3b676dc)`,` ` `[Severity](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/safety-setting#struct_firebase_1_1_a_i_1_1_safety_setting_1a236d10d84d894ee3cd989a39ceca83fca007cc9547ae8884ad597cd92ba505422) `}`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | enum The method of computing whether the threshold has been exceeded. |
| [HarmBlockThreshold](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/safety-setting#struct_firebase_1_1_a_i_1_1_safety_setting_1a85fe9bacee67c2a14b20c0b12493a488)`{` ` `[LowAndAbove](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/safety-setting#struct_firebase_1_1_a_i_1_1_safety_setting_1a85fe9bacee67c2a14b20c0b12493a488ab38533abc7d7d3bf2661d78df74e0ba7)`,` ` `[MediumAndAbove](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/safety-setting#struct_firebase_1_1_a_i_1_1_safety_setting_1a85fe9bacee67c2a14b20c0b12493a488a4115c8b233f3f48c8716473bf12f7ceb)`,` ` `[OnlyHigh](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/safety-setting#struct_firebase_1_1_a_i_1_1_safety_setting_1a85fe9bacee67c2a14b20c0b12493a488a0ffb341e3112a1c2b1b07867af5d09bb)`,` ` `[None](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/safety-setting#struct_firebase_1_1_a_i_1_1_safety_setting_1a85fe9bacee67c2a14b20c0b12493a488a6adf97f83acf6453d4a6a4b1070f3754)`,` ` `[Off](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/safety-setting#struct_firebase_1_1_a_i_1_1_safety_setting_1a85fe9bacee67c2a14b20c0b12493a488ad15305d7a4e34e02489c74a5ef542f36) `}` | enum Block at and beyond a specified threshold.                       |

## Public types

### HarmBlockMethod

```c#
 Firebase::AI::SafetySetting::HarmBlockMethod
```  
The method of computing whether the threshold has been exceeded.

|                        Properties                        ||
|---------------|-------------------------------------------|
| `Probability` | Use only the probability score.           |
| `Severity`    | Use both probability and severity scores. |

### HarmBlockThreshold

```c#
 Firebase::AI::SafetySetting::HarmBlockThreshold
```  
Block at and beyond a specified threshold.

|                                                   Properties                                                    ||
|------------------|-----------------------------------------------------------------------------------------------|
| `LowAndAbove`    | Content with negligible harm is allowed.                                                      |
| `MediumAndAbove` | Content with negligible to low harm is allowed.                                               |
| `None`           | All content is allowed regardless of harm.                                                    |
| `Off`            | All content is allowed regardless of harm, and metadata will not be included in the response. |
| `OnlyHigh`       | Content with negligible to medium harm is allowed.                                            |

## Public functions

### SafetySetting

```c#
 Firebase::AI::SafetySetting::SafetySetting(
  HarmCategory category,
  HarmBlockThreshold threshold,
  HarmBlockMethod? method
)
```  
Initializes a new safety setting with the given category and threshold.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                     Details                                                                                                                                                                                                                                                                                                                                                                                                                     ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `category`  | The category this safety setting should be applied to.                                                                                                                                 | | `threshold` | The threshold describing what content should be blocked.                                                                                                                               | | `method`    | The method of computing whether the threshold has been exceeded; if not specified, the default method is `Severity` for most models. This parameter is unused in the GoogleAI backend. | |