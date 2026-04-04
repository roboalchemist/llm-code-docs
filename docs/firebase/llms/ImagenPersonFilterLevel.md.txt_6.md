# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenPersonFilterLevel.md.txt

# ImagenPersonFilterLevel

# ImagenPersonFilterLevel


```
class ImagenPersonFilterLevel
```

<br />

*** ** * ** ***

A filter used to prevent images from containing depictions of children or people.

## Summary

| ### Public companion properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenPersonFilterLevel` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenPersonFilterLevel.Companion#ALLOW_ADULT()` Allow generation of images containing adults only; images of children are filtered out. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenPersonFilterLevel` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenPersonFilterLevel.Companion#ALLOW_ALL()` Allow generation of images containing people of all ages. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenPersonFilterLevel` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenPersonFilterLevel.Companion#BLOCK_ALL()` Disallow generation of images containing people or faces; images of people are filtered out. |

## Public companion properties

### ALLOW_ADULT

```
val ALLOW_ADULT: ImagenPersonFilterLevel
```

Allow generation of images containing adults only; images of children are filtered out.
> Important: Generation of images containing people or faces may require your use case to be reviewed and approved by Cloud support; see the [Responsible AI and usage guidelines](https://cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen#person-face-gen) for more details.

### ALLOW_ALL

```
val ALLOW_ALL: ImagenPersonFilterLevel
```

Allow generation of images containing people of all ages.
> Important: Generation of images containing people or faces may require your use case to be reviewed and approved by Cloud support; see the [Responsible AI and usage guidelines](https://cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen#person-face-gen) for more details.

### BLOCK_ALL

```
val BLOCK_ALL: ImagenPersonFilterLevel
```

Disallow generation of images containing people or faces; images of people are filtered out.