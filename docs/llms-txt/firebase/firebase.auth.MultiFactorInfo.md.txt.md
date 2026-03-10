# Source: https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorinfo.md.txt

# MultiFactorInfo | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [auth](https://firebase.google.com/docs/reference/js/v8/firebase.auth).
- MultiFactorInfo

A structure containing the information of a second factor entity.

## Index

### Properties

- [displayName](https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorinfo#displayname)
- [enrollmentTime](https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorinfo#enrollmenttime)
- [factorId](https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorinfo#factorid)
- [uid](https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorinfo#uid)

## Properties

### Optional displayName

displayName: string \| null The user friendly name of the current second factor.

### enrollmentTime

enrollmentTime: string The enrollment date of the second factor formatted as a UTC string.

### factorId

factorId: string The identifier of the second factor.

### uid

uid: string The multi-factor enrollment ID.