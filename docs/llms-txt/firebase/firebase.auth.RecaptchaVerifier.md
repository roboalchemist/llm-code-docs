# Source: https://firebase.google.com/docs/reference/js/v8/firebase.auth.RecaptchaVerifier.md.txt

# RecaptchaVerifier | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [auth](https://firebase.google.com/docs/reference/js/v8/firebase.auth).
- RecaptchaVerifier

An [reCAPTCHA](https://www.google.com/recaptcha/)-based application
verifier.

This class does not work in a Node.js environment.

param

:   The reCAPTCHA container parameter. This
    has different meaning depending on whether the reCAPTCHA is hidden or
    visible. For a visible reCAPTCHA the container must be empty. If a string
    is used, it has to correspond to an element ID. The corresponding element
    must also must be in the DOM at the time of initialization.

param

:   The optional reCAPTCHA parameters. Check the
    reCAPTCHA docs for a comprehensive list. All parameters are accepted
    except for the sitekey. Firebase Auth backend provisions a reCAPTCHA for
    each project and will configure this upon rendering. For an invisible
    reCAPTCHA, a size key must have the value 'invisible'.

param

:   The corresponding Firebase app. If none is
    provided, the default Firebase App instance is used. A Firebase App
    instance must be initialized with an API key, otherwise an error will be
    thrown.

### Implements

- [ApplicationVerifier](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ApplicationVerifier)

## Index

### Constructors

- [constructor](https://firebase.google.com/docs/reference/js/v8/firebase.auth.RecaptchaVerifier#constructor)

### Properties

- [type](https://firebase.google.com/docs/reference/js/v8/firebase.auth.RecaptchaVerifier#type)

### Methods

- [clear](https://firebase.google.com/docs/reference/js/v8/firebase.auth.RecaptchaVerifier#clear)
- [render](https://firebase.google.com/docs/reference/js/v8/firebase.auth.RecaptchaVerifier#render)
- [verify](https://firebase.google.com/docs/reference/js/v8/firebase.auth.RecaptchaVerifier#verify)

## Constructors

### constructor

- new RecaptchaVerifier ( container : any \| string , parameters ? : Object \| null , app ? : [App](https://firebase.google.com/docs/reference/js/v8/firebase.app.App) \| null ) : [RecaptchaVerifier](https://firebase.google.com/docs/reference/js/v8/firebase.auth.RecaptchaVerifier)
-
  | Inherited from [RecaptchaVerifier](https://firebase.google.com/docs/reference/js/v8/firebase.auth.RecaptchaVerifier).[constructor](https://firebase.google.com/docs/reference/js/v8/firebase.auth.RecaptchaVerifier#constructor)

  #### Parameters

  -

    ##### container: any \| string

  -

    ##### Optional parameters: Object \| null

  -

    ##### Optional app: [App](https://firebase.google.com/docs/reference/js/v8/firebase.app.App) \| null

  #### Returns [RecaptchaVerifier](https://firebase.google.com/docs/reference/js/v8/firebase.auth.RecaptchaVerifier)

## Properties

### type

type: string
| Implementation of [ApplicationVerifier](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ApplicationVerifier).[type](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ApplicationVerifier#type)
Inherited from [RecaptchaVerifier](https://firebase.google.com/docs/reference/js/v8/firebase.auth.RecaptchaVerifier).[type](https://firebase.google.com/docs/reference/js/v8/firebase.auth.RecaptchaVerifier#type)  
The application verifier type. For a reCAPTCHA verifier, this is 'recaptcha'.

## Methods

### clear

- clear ( ) : void
-
  Inherited from [RecaptchaVerifier](https://firebase.google.com/docs/reference/js/v8/firebase.auth.RecaptchaVerifier).[clear](https://firebase.google.com/docs/reference/js/v8/firebase.auth.RecaptchaVerifier#clear)  
  Clears the reCAPTCHA widget from the page and destroys the current instance.

  #### Returns void

### render

- render ( ) : Promise \< number \>
-
  Inherited from [RecaptchaVerifier](https://firebase.google.com/docs/reference/js/v8/firebase.auth.RecaptchaVerifier).[render](https://firebase.google.com/docs/reference/js/v8/firebase.auth.RecaptchaVerifier#render)  
  Renders the reCAPTCHA widget on the page.

  #### Returns Promise\<number\>

  A Promise that resolves with the
  reCAPTCHA widget ID.

### verify

- verify ( ) : Promise \< string \>
-
  | Implementation of [ApplicationVerifier](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ApplicationVerifier).[verify](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ApplicationVerifier#verify)
  Inherited from [RecaptchaVerifier](https://firebase.google.com/docs/reference/js/v8/firebase.auth.RecaptchaVerifier).[verify](https://firebase.google.com/docs/reference/js/v8/firebase.auth.RecaptchaVerifier#verify)  
  Waits for the user to solve the reCAPTCHA and resolves with the reCAPTCHA
  token.

  #### Returns Promise\<string\>

A Promise for the reCAPTCHA token.