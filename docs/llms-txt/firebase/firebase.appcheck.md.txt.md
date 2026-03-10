# Source: https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.md.txt

# appCheck | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- appCheck

Firebase App Check does not work in a Node.js environment using `ReCaptchaV3Provider` or
`ReCaptchaEnterpriseProvider`, but can be used in Node.js if you use
`CustomProvider` and write your own attestation method.

### Callable

- appCheck ( app ? : [App](https://firebase.google.com/docs/reference/js/v8/firebase.app.App) ) : [AppCheck](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.AppCheck)
- Firebase App Check does not work in a Node.js environment using `ReCaptchaV3Provider` or
  `ReCaptchaEnterpriseProvider`, but can be used in Node.js if you use
  `CustomProvider` and write your own attestation method.

  #### Parameters

  -

    ##### Optional app: [App](https://firebase.google.com/docs/reference/js/v8/firebase.app.App)

  #### Returns [AppCheck](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.AppCheck)

## Index

### Classes

- [CustomProvider](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.CustomProvider)
- [ReCaptchaEnterpriseProvider](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.ReCaptchaEnterpriseProvider)
- [ReCaptchaV3Provider](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.ReCaptchaV3Provider)

### Interfaces

- [AppCheck](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.AppCheck)
- [AppCheckProvider](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.AppCheckProvider)
- [AppCheckToken](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.AppCheckToken)
- [AppCheckTokenResult](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.AppCheckTokenResult)
- [CustomProviderOptions](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.CustomProviderOptions)