# Source: https://firebase.google.com/docs/reference/node/firebase.auth.phonemultifactorinfo.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.auth.phonemultifactorinfo.md.txt

# PhoneMultiFactorInfo | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [auth](https://firebase.google.com/docs/reference/js/v8/firebase.auth).
- PhoneMultiFactorInfo

The subclass of the MultiFactorInfo interface for phone number second factors.
The factorId of this second factor is
[firebase.auth.PhoneMultiFactorGenerator.FACTOR_ID](https://firebase.google.com/docs/reference/js/v8/firebase.auth.phonemultifactorgenerator#factor_id).

## Index

### Properties

- [displayName](https://firebase.google.com/docs/reference/js/v8/firebase.auth.phonemultifactorinfo#displayname)
- [enrollmentTime](https://firebase.google.com/docs/reference/js/v8/firebase.auth.phonemultifactorinfo#enrollmenttime)
- [factorId](https://firebase.google.com/docs/reference/js/v8/firebase.auth.phonemultifactorinfo#factorid)
- [phoneNumber](https://firebase.google.com/docs/reference/js/v8/firebase.auth.phonemultifactorinfo#phonenumber)
- [uid](https://firebase.google.com/docs/reference/js/v8/firebase.auth.phonemultifactorinfo#uid)

## Properties

### Optional displayName

displayName: string \| null
Inherited from [MultiFactorInfo](https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorinfo).[displayName](https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorinfo#displayname)  
The user friendly name of the current second factor.

### enrollmentTime

enrollmentTime: string
Inherited from [MultiFactorInfo](https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorinfo).[enrollmentTime](https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorinfo#enrollmenttime)  
The enrollment date of the second factor formatted as a UTC string.

### factorId

factorId: string
Inherited from [MultiFactorInfo](https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorinfo).[factorId](https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorinfo#factorid)  
The identifier of the second factor.

### phoneNumber

phoneNumber: string  
The phone number associated with the current second factor.

### uid

uid: string
Inherited from [MultiFactorInfo](https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorinfo).[uid](https://firebase.google.com/docs/reference/js/v8/firebase.auth.multifactorinfo#uid)  
The multi-factor enrollment ID.