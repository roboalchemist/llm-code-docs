# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/safety-rating.md.txt

# Firebase.AI.SafetyRating Struct Reference

# Firebase.AI.SafetyRating

A type defining potentially harmful media categories and their model-assigned ratings.

## Summary

A value of this type may be assigned to a category for every model-generated response, not just responses that exceed a certain threshold.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ### Public types                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| [HarmProbability](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/safety-rating#struct_firebase_1_1_a_i_1_1_safety_rating_1a7009d3f51cf801d6d5583861e6372077)`{` ` `[Unknown](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/safety-rating#struct_firebase_1_1_a_i_1_1_safety_rating_1a7009d3f51cf801d6d5583861e6372077a88183b946cc5f0e8c96b2e66e1c74a7e)` = 0,` ` `[Negligible](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/safety-rating#struct_firebase_1_1_a_i_1_1_safety_rating_1a7009d3f51cf801d6d5583861e6372077aa295493d972709c15ec5098fb718e14a)`,` ` `[Low](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/safety-rating#struct_firebase_1_1_a_i_1_1_safety_rating_1a7009d3f51cf801d6d5583861e6372077a28d0edd045e05cf5af64e35ae0c4c6ef)`,` ` `[Medium](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/safety-rating#struct_firebase_1_1_a_i_1_1_safety_rating_1a7009d3f51cf801d6d5583861e6372077a87f8a6ab85c9ced3702b4ea641ad4bb5)`,` ` `[High](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/safety-rating#struct_firebase_1_1_a_i_1_1_safety_rating_1a7009d3f51cf801d6d5583861e6372077a655d20c1ca69519ca647684edbb2db35) `}` | enum The probability that a given model output falls under a harmful content category.         |
| [HarmSeverity](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/safety-rating#struct_firebase_1_1_a_i_1_1_safety_rating_1a7c7ecae6e74ad269bf7b05a87550b2ff)`{` ` `[Unknown](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/safety-rating#struct_firebase_1_1_a_i_1_1_safety_rating_1a7c7ecae6e74ad269bf7b05a87550b2ffa88183b946cc5f0e8c96b2e66e1c74a7e)` = 0,` ` `[Negligible](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/safety-rating#struct_firebase_1_1_a_i_1_1_safety_rating_1a7c7ecae6e74ad269bf7b05a87550b2ffaa295493d972709c15ec5098fb718e14a)`,` ` `[Low](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/safety-rating#struct_firebase_1_1_a_i_1_1_safety_rating_1a7c7ecae6e74ad269bf7b05a87550b2ffa28d0edd045e05cf5af64e35ae0c4c6ef)`,` ` `[Medium](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/safety-rating#struct_firebase_1_1_a_i_1_1_safety_rating_1a7c7ecae6e74ad269bf7b05a87550b2ffa87f8a6ab85c9ced3702b4ea641ad4bb5)`,` ` `[High](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/safety-rating#struct_firebase_1_1_a_i_1_1_safety_rating_1a7c7ecae6e74ad269bf7b05a87550b2ffa655d20c1ca69519ca647684edbb2db35) `}`    | enum The magnitude of how harmful a model response might be for the respective `HarmCategory`. |

|                                                                                                                                                                                                                          ### Properties                                                                                                                                                                                                                          ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Blocked](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/safety-rating#struct_firebase_1_1_a_i_1_1_safety_rating_1a2eeae1247af80cd9082f86f7ecd017ab)          | `bool` If true, the response was blocked.                                                                                                                                                                                                                                   |
| [Category](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/safety-rating#struct_firebase_1_1_a_i_1_1_safety_rating_1af5d9ba812add4273b483e1fb88c8098a)         | [HarmCategory](https://firebase.google.com/docs/reference/unity/namespace/firebase/a-i#namespace_firebase_1_1_a_i_1ae7e954295da056c823c0963d6b457382) The category describing the potential harm a piece of content may pose.                                               |
| [Probability](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/safety-rating#struct_firebase_1_1_a_i_1_1_safety_rating_1a0b57f1f35a10fc04947fd449d8d1587a)      | [HarmProbability](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/safety-rating#struct_firebase_1_1_a_i_1_1_safety_rating_1a7009d3f51cf801d6d5583861e6372077) The model-generated probability that the content falls under the specified HarmCategory. |
| [ProbabilityScore](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/safety-rating#struct_firebase_1_1_a_i_1_1_safety_rating_1a20bc48bd1d9195dba550a403bc85c690) | `float` The confidence score that the response is associated with the corresponding HarmCategory.                                                                                                                                                                           |
| [Severity](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/safety-rating#struct_firebase_1_1_a_i_1_1_safety_rating_1a4008745b0dfd8f099b991312b10e57f4)         | [HarmSeverity](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/safety-rating#struct_firebase_1_1_a_i_1_1_safety_rating_1a7c7ecae6e74ad269bf7b05a87550b2ff) The severity reflects the magnitude of how harmful a model response might be.               |
| [SeverityScore](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/safety-rating#struct_firebase_1_1_a_i_1_1_safety_rating_1af000607be76146adb3e5458696adf19e)    | `float` The severity score is the magnitude of how harmful a model response might be.                                                                                                                                                                                       |

## Public types

### HarmProbability

```c#
 Firebase::AI::SafetyRating::HarmProbability
```  
The probability that a given model output falls under a harmful content category.

Note: This does not indicate the severity of harm for a piece of content.

|                                                              Properties                                                               ||
|--------------|-------------------------------------------------------------------------------------------------------------------------|
| `High`       | The probability is high. The content described is very likely harmful.                                                  |
| `Low`        | The probability is small but non-zero.                                                                                  |
| `Medium`     | The probability is moderate.                                                                                            |
| `Negligible` | The probability is zero or close to zero. For benign content, the probability across all categories will be this value. |
| `Unknown`    | A new and not yet supported value.                                                                                      |

### HarmSeverity

```c#
 Firebase::AI::SafetyRating::HarmSeverity
```  
The magnitude of how harmful a model response might be for the respective `HarmCategory`.

|                    Properties                    ||
|--------------|------------------------------------|
| `High`       | High level of harm severity.       |
| `Low`        | Low level of harm severity.        |
| `Medium`     | Medium level of harm severity.     |
| `Negligible` | Negligible level of harm severity. |
| `Unknown`    | A new and not yet supported value. |

## Properties

### Blocked

```c#
bool Firebase::AI::SafetyRating::Blocked
```  
If true, the response was blocked.  

### Category

```c#
HarmCategory Firebase::AI::SafetyRating::Category
```  
The category describing the potential harm a piece of content may pose.  

### Probability

```c#
HarmProbability Firebase::AI::SafetyRating::Probability
```  
The model-generated probability that the content falls under the specified HarmCategory.

This is a discretized representation of the `ProbabilityScore`.

Important: This does not indicate the severity of harm for a piece of content.  

### ProbabilityScore

```c#
float Firebase::AI::SafetyRating::ProbabilityScore
```  
The confidence score that the response is associated with the corresponding HarmCategory.

The probability safety score is a confidence score between 0.0 and 1.0, rounded to one decimal place; it is discretized into a `HarmProbability` in `Probability`. See [probability scores](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/configure-safety-filters#comparison_of_probability_scores_and_severity_scores) in the Google Cloud documentation for more details.  

### Severity

```c#
HarmSeverity Firebase::AI::SafetyRating::Severity
```  
The severity reflects the magnitude of how harmful a model response might be.

This is a discretized representation of the `SeverityScore`.  

### SeverityScore

```c#
float Firebase::AI::SafetyRating::SeverityScore
```  
The severity score is the magnitude of how harmful a model response might be.

The severity score ranges from 0.0 to 1.0, rounded to one decimal place; it is discretized into a `HarmSeverity` in `Severity`. See [severity scores](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/configure-safety-filters#comparison_of_probability_scores_and_severity_scores) in the Google Cloud documentation for more details.