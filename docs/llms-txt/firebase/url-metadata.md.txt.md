# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/url-metadata.md.txt

# Firebase.AI.UrlMetadata Struct Reference

# Firebase.AI.UrlMetadata

Metadata for a single URL retrieved by the [UrlContext](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/url-context#struct_firebase_1_1_a_i_1_1_url_context) tool.

## Summary

| ### Public types ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/url-metadata#struct_firebase_1_1_a_i_1_1_url_metadata_1a9f243163691b14b49ad0478a568ed1db{ https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/url-metadata#struct_firebase_1_1_a_i_1_1_url_metadata_1a9f243163691b14b49ad0478a568ed1dba6fcdc090caeade09d0efd6253932b6f5 = 0, https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/url-metadata#struct_firebase_1_1_a_i_1_1_url_metadata_1a9f243163691b14b49ad0478a568ed1dba505a83f220c02df2f85c3810cd9ceb38, https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/url-metadata#struct_firebase_1_1_a_i_1_1_url_metadata_1a9f243163691b14b49ad0478a568ed1dba902b0d55fddef6f8d651fe1035b7d4bd, https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/url-metadata#struct_firebase_1_1_a_i_1_1_url_metadata_1a9f243163691b14b49ad0478a568ed1dba68ce487660ad97b9df6f32551405ef58, https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/url-metadata#struct_firebase_1_1_a_i_1_1_url_metadata_1a9f243163691b14b49ad0478a568ed1dbad3d57868b6ff9839eff631d2cc8acbce }` | enumStatus of the URL retrieval. |

| ### Properties ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/url-metadata#struct_firebase_1_1_a_i_1_1_url_metadata_1afdfdb51640619b6044a6cb3db4481a92` | `https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/url-metadata#struct_firebase_1_1_a_i_1_1_url_metadata_1a9f243163691b14b49ad0478a568ed1db` The status of the URL retrieval. |
| `https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/url-metadata#struct_firebase_1_1_a_i_1_1_url_metadata_1a69eff6c2d3953d3928199d186b461db1` | `System.Uri` The retrieved URL. |

## Public types

### UrlRetrievalStatus

```c#
 Firebase::AI::UrlMetadata::UrlRetrievalStatus
```
Status of the URL retrieval.

| Properties ||
|---|---|
| `Error` | The URL retrieval failed. |
| `Paywall` | The URL retrieval failed because the content is behind a paywall. |
| `Success` | The URL retrieval was successful. |
| `Unsafe` | The URL retrieval failed because the content is unsafe. |
| `Unspecified` | Unspecified retrieval status |

## Properties

### RetrievalStatus

```c#
UrlRetrievalStatus Firebase::AI::UrlMetadata::RetrievalStatus
```
The status of the URL retrieval.

### Url

```c#
System.Uri Firebase::AI::UrlMetadata::Url
```
The retrieved URL.