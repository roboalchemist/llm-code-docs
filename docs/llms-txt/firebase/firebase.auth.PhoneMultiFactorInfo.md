# Source: https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneMultiFactorInfo.md.txt

# PhoneMultiFactorInfo | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [auth](https://firebase.google.com/docs/reference/js/v8/firebase.auth).
- PhoneMultiFactorInfo

The subclass of the MultiFactorInfo interface for phone number second factors.
The factorId of this second factor is
[firebase.auth.PhoneMultiFactorGenerator.FACTOR_ID](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneMultiFactorGenerator#factor_id).

## Index

### Properties

- [displayName](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneMultiFactorInfo#displayname)
- [enrollmentTime](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneMultiFactorInfo#enrollmenttime)
- [factorId](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneMultiFactorInfo#factorid)
- [phoneNumber](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneMultiFactorInfo#phonenumber)
- [uid](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneMultiFactorInfo#uid)

## Properties

### Optional displayName

displayName: string \| null
Inherited from [MultiFactorInfo](https://firebase.google.com/docs/reference/js/v8/firebase.auth.MultiFactorInfo).[displayName](https://firebase.google.com/docs/reference/js/v8/firebase.auth.MultiFactorInfo#displayname)  
The user friendly name of the current second factor.

### enrollmentTime

enrollmentTime: string
Inherited from [MultiFactorInfo](https://firebase.google.com/docs/reference/js/v8/firebase.auth.MultiFactorInfo).[enrollmentTime](https://firebase.google.com/docs/reference/js/v8/firebase.auth.MultiFactorInfo#enrollmenttime)  
The enrollment date of the second factor formatted as a UTC string.

### factorId

factorId: string
Inherited from [MultiFactorInfo](https://firebase.google.com/docs/reference/js/v8/firebase.auth.MultiFactorInfo).[factorId](https://firebase.google.com/docs/reference/js/v8/firebase.auth.MultiFactorInfo#factorid)  
The identifier of the second factor.

### phoneNumber

phoneNumber: string  
The phone number associated with the current second factor.

### uid

uid: string
Inherited from [MultiFactorInfo](https://firebase.google.com/docs/reference/js/v8/firebase.auth.MultiFactorInfo).[uid](https://firebase.google.com/docs/reference/js/v8/firebase.auth.MultiFactorInfo#uid)  
The multi-factor enrollment ID.