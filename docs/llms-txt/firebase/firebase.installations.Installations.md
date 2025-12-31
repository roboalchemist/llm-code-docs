# Source: https://firebase.google.com/docs/reference/js/v8/firebase.installations.Installations.md.txt

# Installations | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [installations](https://firebase.google.com/docs/reference/js/v8/firebase.installations).
- Installations

The Firebase Installations service interface.

Do not call this constructor directly. Instead, use
[`firebase.installations()`](https://firebase.google.com/docs/reference/js/v8/firebase.installations).

## Index

### Properties

- [app](https://firebase.google.com/docs/reference/js/v8/firebase.installations.Installations#app)

### Methods

- [delete](https://firebase.google.com/docs/reference/js/v8/firebase.installations.Installations#delete)
- [getId](https://firebase.google.com/docs/reference/js/v8/firebase.installations.Installations#getid)
- [getToken](https://firebase.google.com/docs/reference/js/v8/firebase.installations.Installations#gettoken)
- [onIdChange](https://firebase.google.com/docs/reference/js/v8/firebase.installations.Installations#onidchange)

## Properties

### app

app: [App](https://firebase.google.com/docs/reference/js/v8/firebase.app.App)  
The [app](https://firebase.google.com/docs/reference/js/v8/firebase.app.App) associated with the `Installations` service
instance.

example
:

        var app = analytics.app;


## Methods

### delete

- delete ( ) : Promise \< void \>
- Deletes the Firebase Installation and all associated data.

  #### Returns Promise\<void\>

### getId

- getId ( ) : Promise \< string \>
- Creates a Firebase Installation if there isn't one for the app and
  returns the Installation ID.

  #### Returns Promise\<string\>

  Firebase Installation ID

### getToken

- getToken ( forceRefresh ? : boolean ) : Promise \< string \>
- Returns an Authentication Token for the current Firebase Installation.

  #### Parameters

  -

    ##### Optional forceRefresh: boolean

  #### Returns Promise\<string\>

  Firebase Installation Authentication Token

### onIdChange

- onIdChange ( callback : ( installationId : string ) =\> void ) : ( ) =\> void
- Sets a new callback that will get called when Installlation ID changes.
  Returns an unsubscribe function that will remove the callback when called.

  #### Parameters

  -

    ##### callback: (installationId: string) =\> void

    -
      - (installationId: string): void

      <!-- -->

      -

        #### Parameters

        -

          ##### installationId: string

        #### Returns void

  #### Returns () =\> void

  -
    - (): void

    <!-- -->

    -

      #### Returns void