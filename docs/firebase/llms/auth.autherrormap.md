# Source: https://firebase.google.com/docs/reference/js/auth.autherrormap.md.txt

# AuthErrorMap interface

A mapping of error codes to error messages.

While error messages are useful for debugging (providing verbose textual context around what went wrong), these strings take up a lot of space in the compiled code. When deploying code in production, using [prodErrorMap](https://firebase.google.com/docs/reference/js/auth.md#proderrormap) will save you roughly 10k compressed/gzipped over [debugErrorMap](https://firebase.google.com/docs/reference/js/auth.md#debugerrormap). You can select the error map during initialization:  

    initializeAuth(app, {errorMap: debugErrorMap})

When initializing Auth, [prodErrorMap](https://firebase.google.com/docs/reference/js/auth.md#proderrormap) is default.

**Signature:**  

    export interface AuthErrorMap