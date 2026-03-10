# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/package-summary.md.txt

# com.google.firebase.ai

# com.google.firebase.ai

## Classes

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/Chat` | Representation of a multi-turn interaction with a model. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI` | Entry point for all *Firebase AI* functionality. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel` | Represents a multimodal model (like Gemini), capable of generating content based on various input types. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ImagenModel` | Represents a generative model (like Imagen), capable of generating images based on various input types. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/InferenceMode` | Specifies how the SDK should choose between on-device and in-cloud inference. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/InferenceSource` | Indicates the source of the model inference. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/LiveGenerativeModel` | Represents a multimodal model (like Gemini) capable of real-time content generation based on various input types, supporting bidirectional streaming. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/OnDeviceConfig` | Configuration for on-device AI model inference. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/TemplateGenerativeModel` | Represents a multimodal model (like Gemini), capable of generating content based on various templated input types. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/TemplateImagenModel` | Represents a generative model (like Imagen), capable of generating images based a template. |

## Extension functions summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/package-summary#(com.google.firebase.Firebase).ai(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend,kotlin.Boolean)( app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp, backend: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerativeBackend, useLimitedUseAppCheckTokens: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html )` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI` instance for the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/package-summary#(com.google.firebase.Firebase).ai(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend,kotlin.Boolean)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/package-summary#(com.google.firebase.Firebase).ai(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend)(app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp, backend: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerativeBackend)` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI` instance for the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/package-summary#(com.google.firebase.Firebase).ai(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend)`. |

## Extension properties summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/package-summary#(com.google.firebase.Firebase).ai()` The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI` instance for the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` using the Google AI Backend. |

## Extension functions

### ai

```
fun Firebase.ai(
    app: FirebaseApp = Firebase.app,
    backend: GenerativeBackend = GenerativeBackend.googleAI(),
    useLimitedUseAppCheckTokens: Boolean
): FirebaseAI
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI` instance for the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/package-summary#(com.google.firebase.Firebase).ai(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend,kotlin.Boolean)`.

| Parameters |
|---|---|
| `backend: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerativeBackend = GenerativeBackend.googleAI()` | the backend reference to make generative AI requests to. |
| `useLimitedUseAppCheckTokens: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | use App Check's limited-use tokens when sending requests to the backend. Learn more about [limited-use tokens](https://firebase.google.com/docs/ai-logic/app-check), including their nuances, when to use them, and best practices for integrating them into your app. |

### ai

```
fun Firebase.ai(
    app: FirebaseApp = Firebase.app,
    backend: GenerativeBackend = GenerativeBackend.googleAI()
): FirebaseAI
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI` instance for the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/package-summary#(com.google.firebase.Firebase).ai(com.google.firebase.FirebaseApp,com.google.firebase.ai.type.GenerativeBackend)`.

| Parameters |
|---|---|
| `backend: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerativeBackend = GenerativeBackend.googleAI()` | the backend reference to make generative AI requests to. |

## Extension properties

### ai

```
val Firebase.ai: FirebaseAI
```

The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI` instance for the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` using the Google AI Backend.