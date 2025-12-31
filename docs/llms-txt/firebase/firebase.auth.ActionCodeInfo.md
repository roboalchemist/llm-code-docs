# Source: https://firebase.google.com/docs/reference/node/firebase.auth.ActionCodeInfo.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.auth.ActionCodeInfo.md.txt

# ActionCodeInfo | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [auth](https://firebase.google.com/docs/reference/js/v8/firebase.auth).
- ActionCodeInfo

A response from [firebase.auth.Auth.checkActionCode](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#checkactioncode).

## Index

### Type aliases

- [Operation](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ActionCodeInfo#operation)

### Properties

- [data](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ActionCodeInfo#data)
- [operation](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ActionCodeInfo#operation-1)

### Variables

- [Operation](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ActionCodeInfo#operation-2)

## Type aliases

### Operation

Operation: string

## Properties

### data

data: { email?: string \| null; fromEmail?: string \| null; multiFactorInfo?: [MultiFactorInfo](https://firebase.google.com/docs/reference/js/v8/firebase.auth.MultiFactorInfo) \| null; previousEmail?: string \| null }  
The data associated with the action code.

For the `PASSWORD_RESET`, `VERIFY_EMAIL`, and `RECOVER_EMAIL` actions, this object
contains an `email` field with the address the email was sent to.

For the RECOVER_EMAIL action, which allows a user to undo an email address
change, this object also contains a `previousEmail` field with the user account's
current email address. After the action completes, the user's email address will
revert to the value in the `email` field from the value in `previousEmail` field.

For the VERIFY_AND_CHANGE_EMAIL action, which allows a user to verify the email
before updating it, this object contains a `previousEmail` field with the user
account's email address before updating. After the action completes, the user's
email address will be updated to the value in the `email` field from the value
in `previousEmail` field.

For the REVERT_SECOND_FACTOR_ADDITION action, which allows a user to unenroll
a newly added second factor, this object contains a `multiFactorInfo` field with
the information about the second factor. For phone second factor, the
`multiFactorInfo` is a [firebase.auth.PhoneMultiFactorInfo](https://firebase.google.com/docs/reference/js/v8/firebase.auth.PhoneMultiFactorInfo) object,
which contains the phone number.  

#### Type declaration

-

  ##### Optional email?: string \| null

-

  ##### Optional fromEmail?: string \| null

  deprecated

  :   This field is deprecated in favor of previousEmail.

-

  ##### Optional multiFactorInfo?: [MultiFactorInfo](https://firebase.google.com/docs/reference/js/v8/firebase.auth.MultiFactorInfo) \| null

-

  ##### Optional previousEmail?: string \| null

### operation

operation: string  
The type of operation that generated the action code. This could be:

- \`EMAIL_SIGNIN\`: email sign in code generated via [firebase.auth.Auth.sendSignInLinkToEmail](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#sendsigninlinktoemail).
- \`PASSWORD_RESET\`: password reset code generated via [firebase.auth.Auth.sendPasswordResetEmail](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#sendpasswordresetemail).
- \`RECOVER_EMAIL\`: email change revocation code generated via [firebase.User.updateEmail](https://firebase.google.com/docs/reference/js/v8/firebase.User#updateemail).
- \`REVERT_SECOND_FACTOR_ADDITION\`: revert second factor addition code generated via [firebase.User.MultiFactorUser.enroll](https://firebase.google.com/docs/reference/js/v8/firebase.user.MultiFactorUser#enroll).
- \`VERIFY_AND_CHANGE_EMAIL\`: verify and change email code generated via [firebase.User.verifyBeforeUpdateEmail](https://firebase.google.com/docs/reference/js/v8/firebase.User#verifybeforeupdateemail).
- \`VERIFY_EMAIL\`: email verification code generated via [firebase.User.sendEmailVerification](https://firebase.google.com/docs/reference/js/v8/firebase.User#sendemailverification).

## Variables

### Operation

Operation: { EMAIL_SIGNIN: [Operation](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ActionCodeInfo#operation); PASSWORD_RESET: [Operation](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ActionCodeInfo#operation); RECOVER_EMAIL: [Operation](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ActionCodeInfo#operation); REVERT_SECOND_FACTOR_ADDITION: [Operation](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ActionCodeInfo#operation); VERIFY_AND_CHANGE_EMAIL: [Operation](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ActionCodeInfo#operation); VERIFY_EMAIL: [Operation](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ActionCodeInfo#operation) }  
An enumeration of the possible email action types.  

#### Type declaration

-

  ##### EMAIL_SIGNIN: [Operation](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ActionCodeInfo#operation)

  The email link sign-in action.
-

  ##### PASSWORD_RESET: [Operation](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ActionCodeInfo#operation)

  The password reset action.
-

  ##### RECOVER_EMAIL: [Operation](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ActionCodeInfo#operation)

  The email revocation action.
-

  ##### REVERT_SECOND_FACTOR_ADDITION: [Operation](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ActionCodeInfo#operation)

  The revert second factor addition email action.
-

  ##### VERIFY_AND_CHANGE_EMAIL: [Operation](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ActionCodeInfo#operation)

  The verify and update email action.
-

  ##### VERIFY_EMAIL: [Operation](https://firebase.google.com/docs/reference/js/v8/firebase.auth.ActionCodeInfo#operation)

The email verification action.