# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenPersonFilterLevel.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ImagenPersonFilterLevel.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenPersonFilterLevel.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenPersonFilterLevel.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenPersonFilterLevel.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenPersonFilterLevel.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenPersonFilterLevel.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenPersonFilterLevel.md.txt

# ImagenPersonFilterLevel


```
class ImagenPersonFilterLevel
```

<br />

*** ** * ** ***

A filter used to prevent images from containing depictions of children or people.

## Summary

|                                                 ### Public companion properties                                                  |
|----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ImagenPersonFilterLevel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenPersonFilterLevel) | [ALLOW_ADULT](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenPersonFilterLevel.Companion#ALLOW_ADULT()) Allow generation of images containing adults only; images of children are filtered out.  |
| [ImagenPersonFilterLevel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenPersonFilterLevel) | [ALLOW_ALL](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenPersonFilterLevel.Companion#ALLOW_ALL()) Allow generation of images containing people of all ages.                                    |
| [ImagenPersonFilterLevel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenPersonFilterLevel) | [BLOCK_ALL](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenPersonFilterLevel.Companion#BLOCK_ALL()) Disallow generation of images containing people or faces; images of people are filtered out. |

## Public companion properties

### ALLOW_ADULT

```
valÂ ALLOW_ADULT:Â ImagenPersonFilterLevel
```

Allow generation of images containing adults only; images of children are filtered out.
Important: Generation of images containing people or faces may require your use case to be reviewed and approved by Cloud support; see the [Responsible AI and usage guidelines](https://cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen#person-face-gen) for more details.  

### ALLOW_ALL

```
valÂ ALLOW_ALL:Â ImagenPersonFilterLevel
```

Allow generation of images containing people of all ages.
Important: Generation of images containing people or faces may require your use case to be reviewed and approved by Cloud support; see the [Responsible AI and usage guidelines](https://cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen#person-face-gen) for more details.  

### BLOCK_ALL

```
valÂ BLOCK_ALL:Â ImagenPersonFilterLevel
```

Disallow generation of images containing people or faces; images of people are filtered out.