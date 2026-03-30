# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenPersonFilterLevel.md.txt

# ImagenPersonFilterLevel

# ImagenPersonFilterLevel


```
@PublicPreviewAPI
class ImagenPersonFilterLevel
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

A filter used to prevent images from containing depictions of children or people.

## Summary

| ### Public companion properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenPersonFilterLevel` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenPersonFilterLevel.Companion#ALLOW_ADULT()` Filters out any images containing depictions of children. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenPersonFilterLevel` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenPersonFilterLevel.Companion#ALLOW_ALL()` No filters applied. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenPersonFilterLevel` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenPersonFilterLevel.Companion#BLOCK_ALL()` Filters out any images containing depictions of people. |

## Public companion properties

### ALLOW_ADULT

```
val ALLOW_ADULT: ImagenPersonFilterLevel
```

Filters out any images containing depictions of children.

### ALLOW_ALL

```
val ALLOW_ALL: ImagenPersonFilterLevel
```

No filters applied.

### BLOCK_ALL

```
val BLOCK_ALL: ImagenPersonFilterLevel
```

Filters out any images containing depictions of people.