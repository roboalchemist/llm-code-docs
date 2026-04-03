# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.auth.userbuilder.md.txt

# auth.UserBuilder class

Builder used to create functions for Firebase Auth user lifecycle events.

**Signature:**  

    export declare class UserBuilder 

## Methods

|                                                                      Method                                                                      | Modifiers |                    Description                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------|-----------|---------------------------------------------------|
| [beforeCreate(handler)](https://firebase.google.com/docs/reference/functions/firebase-functions.auth.userbuilder.md#authuserbuilderbeforecreate) |           | Blocks request to create a Firebase Auth user.    |
| [beforeEmail(handler)](https://firebase.google.com/docs/reference/functions/firebase-functions.auth.userbuilder.md#authuserbuilderbeforeemail)   |           |                                                   |
| [beforeSignIn(handler)](https://firebase.google.com/docs/reference/functions/firebase-functions.auth.userbuilder.md#authuserbuilderbeforesignin) |           | Blocks request to sign-in a Firebase Auth user.   |
| [beforeSms(handler)](https://firebase.google.com/docs/reference/functions/firebase-functions.auth.userbuilder.md#authuserbuilderbeforesms)       |           |                                                   |
| [onCreate(handler)](https://firebase.google.com/docs/reference/functions/firebase-functions.auth.userbuilder.md#authuserbuilderoncreate)         |           | Responds to the creation of a Firebase Auth user. |
| [onDelete(handler)](https://firebase.google.com/docs/reference/functions/firebase-functions.auth.userbuilder.md#authuserbuilderondelete)         |           | Responds to the deletion of a Firebase Auth user. |

## auth.UserBuilder.beforeCreate()

Blocks request to create a Firebase Auth user.

**Signature:**  

    beforeCreate(handler: (user: AuthUserRecord, context: AuthEventContext) => MaybeAsync<BeforeCreateResponse | void>): BlockingFunction;

### Parameters

| Parameter |                                               Type                                               |                         Description                         |
|-----------|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| handler   | (user: AuthUserRecord, context: AuthEventContext) =\> MaybeAsync\<BeforeCreateResponse \| void\> | Event handler that blocks creation of a Firebase Auth user. |

**Returns:**

[BlockingFunction](https://firebase.google.com/docs/reference/functions/firebase-functions.blockingfunction.md#blockingfunction_interface)

## auth.UserBuilder.beforeEmail()

**Signature:**  

    beforeEmail(handler: (context: AuthEventContext) => MaybeAsync<BeforeEmailResponse | void>): BlockingFunction;

### Parameters

| Parameter |                                   Type                                    | Description |
|-----------|---------------------------------------------------------------------------|-------------|
| handler   | (context: AuthEventContext) =\> MaybeAsync\<BeforeEmailResponse \| void\> |             |

**Returns:**

[BlockingFunction](https://firebase.google.com/docs/reference/functions/firebase-functions.blockingfunction.md#blockingfunction_interface)

## auth.UserBuilder.beforeSignIn()

Blocks request to sign-in a Firebase Auth user.

**Signature:**  

    beforeSignIn(handler: (user: AuthUserRecord, context: AuthEventContext) => MaybeAsync<BeforeSignInResponse | void>): BlockingFunction;

### Parameters

| Parameter |                                               Type                                               |                        Description                         |
|-----------|--------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| handler   | (user: AuthUserRecord, context: AuthEventContext) =\> MaybeAsync\<BeforeSignInResponse \| void\> | Event handler that blocks sign-in of a Firebase Auth user. |

**Returns:**

[BlockingFunction](https://firebase.google.com/docs/reference/functions/firebase-functions.blockingfunction.md#blockingfunction_interface)

## auth.UserBuilder.beforeSms()

**Signature:**  

    beforeSms(handler: (context: AuthEventContext) => MaybeAsync<BeforeSmsResponse | void>): BlockingFunction;

### Parameters

| Parameter |                                  Type                                   | Description |
|-----------|-------------------------------------------------------------------------|-------------|
| handler   | (context: AuthEventContext) =\> MaybeAsync\<BeforeSmsResponse \| void\> |             |

**Returns:**

[BlockingFunction](https://firebase.google.com/docs/reference/functions/firebase-functions.blockingfunction.md#blockingfunction_interface)

## auth.UserBuilder.onCreate()

Responds to the creation of a Firebase Auth user.

**Signature:**  

    onCreate(handler: (user: UserRecord, context: EventContext) => PromiseLike<any> | any): CloudFunction<UserRecord>;

### Parameters

| Parameter |                                                                                                                                            Type                                                                                                                                             |                             Description                              |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| handler   | (user: [UserRecord](https://firebase.google.com/docs/reference/functions/firebase-functions.auth.md#authuserrecord), context: [EventContext](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontext.md#eventcontext_interface)) =\> PromiseLike\<any\> \| any | Event handler that responds to the creation of a Firebase Auth user. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[UserRecord](https://firebase.google.com/docs/reference/functions/firebase-functions.auth.md#authuserrecord)\>

## auth.UserBuilder.onDelete()

Responds to the deletion of a Firebase Auth user.

**Signature:**  

    onDelete(handler: (user: UserRecord, context: EventContext) => PromiseLike<any> | any): CloudFunction<UserRecord>;

### Parameters

| Parameter |                                                                                                                                            Type                                                                                                                                             |                             Description                              |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| handler   | (user: [UserRecord](https://firebase.google.com/docs/reference/functions/firebase-functions.auth.md#authuserrecord), context: [EventContext](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontext.md#eventcontext_interface)) =\> PromiseLike\<any\> \| any | Event handler that responds to the deletion of a Firebase Auth user. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[UserRecord](https://firebase.google.com/docs/reference/functions/firebase-functions.auth.md#authuserrecord)\>