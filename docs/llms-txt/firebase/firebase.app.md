# Source: https://firebase.google.com/docs/reference/node/firebase.app.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.app.md.txt

# app | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- app

### Callable

- app ( name ? : string ) : [App](https://firebase.google.com/docs/reference/js/v8/firebase.app.App)
- Retrieves a Firebase [app](https://firebase.google.com/docs/reference/js/v8/firebase.app.App) instance.

  When called with no arguments, the default app is returned. When an app name
  is provided, the app corresponding to that name is returned.

  An exception is thrown if the app being retrieved has not yet been
  initialized.

  example
  :

          // Return the default app
          var app = firebase.app();


  example
  :

          // Return a named app
          var otherApp = firebase.app("otherApp");


  #### Parameters

  -

    ##### Optional name: string

    Optional name of the app to return. If no name is
    provided, the default is `"[DEFAULT]"`.

  #### Returns [App](https://firebase.google.com/docs/reference/js/v8/firebase.app.App)

  The app corresponding to the provided app name.
  If no app name is provided, the default app is returned.

## Index

### Interfaces

- [App](https://firebase.google.com/docs/reference/js/v8/firebase.app.App)