# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/storage/listener.md.txt

# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/messaging/listener.md.txt

# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider/listener.md.txt

# firebase::auth::PhoneAuthProvider::Listener Class Reference

# firebase::auth::PhoneAuthProvider::Listener


**This is an abstract class.**


`#include <credential.h>`

Receive callbacks from [VerifyPhoneNumber](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider#classfirebase_1_1auth_1_1_phone_auth_provider_1ad8b24001f507a420a3915d0f29865d84) events.

## Summary

Please see [PhoneAuthProvider](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider#classfirebase_1_1auth_1_1_phone_auth_provider) for a sample implementation.

| ### Constructors and Destructors ||
|---|---|
| [Listener](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider/listener#classfirebase_1_1auth_1_1_phone_auth_provider_1_1_listener_1a3ffb98653144cafdff110f49991e2e62)`()` ||
| [~Listener](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider/listener#classfirebase_1_1auth_1_1_phone_auth_provider_1_1_listener_1ae3b9285d442c8ec92849532ef835677f)`()` ||

|                                                                                                                                                                                                                                                                                                                                                                ### Public functions                                                                                                                                                                                                                                                                                                                                                                ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [OnCodeAutoRetrievalTimeOut](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider/listener#classfirebase_1_1auth_1_1_phone_auth_provider_1_1_listener_1a3ea7ebac04e74de3ff76996ce4090193)`(const std::string & verification_id)`                                                                                                                                                                                                                              | `virtual void` The timeout specified in [VerifyPhoneNumber](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider#classfirebase_1_1auth_1_1_phone_auth_provider_1ad8b24001f507a420a3915d0f29865d84) has expired. |
| [OnCodeSent](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider/listener#classfirebase_1_1auth_1_1_phone_auth_provider_1_1_listener_1a65f3a2abf007af3dfb1f8d2136bf4c29)`(const std::string & verification_id, const `[ForceResendingToken](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider/force-resending-token#classfirebase_1_1auth_1_1_phone_auth_provider_1_1_force_resending_token)` & force_resending_token)` | `virtual void` SMS message with verification code sent to phone number.                                                                                                                                                                           |
| [OnVerificationCompleted](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider/listener#classfirebase_1_1auth_1_1_phone_auth_provider_1_1_listener_1a85770051624295e82b97a424bfe2efea)`(`[PhoneAuthCredential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-credential#classfirebase_1_1auth_1_1_phone_auth_credential)` credential)=0`                                                                                      | `virtual void` Phone number auto-verification succeeded.                                                                                                                                                                                          |
| [OnVerificationFailed](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider/listener#classfirebase_1_1auth_1_1_phone_auth_provider_1_1_listener_1ae94577c2b30cbd9518145d13769301a7)`(const std::string & error)=0`                                                                                                                                                                                                                                            | `virtual void` Phone number verification failed with an error.                                                                                                                                                                                    |

## Public functions

### Listener

```c++
 Listener()
```  

### OnCodeAutoRetrievalTimeOut

```c++
virtual void OnCodeAutoRetrievalTimeOut(
  const std::string & verification_id
)
```  
The timeout specified in [VerifyPhoneNumber](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider#classfirebase_1_1auth_1_1_phone_auth_provider_1ad8b24001f507a420a3915d0f29865d84) has expired.

Called once `auto_verify_time_out_ms` has passed. If using auto SMS retrieval, you can choose to block the UI (do not allow manual input of the verification code) until timeout is hit.


| **Note:** This callback is called immediately on iOS, since iOS does not have auto-validation.

<br />

|                                                                        Details                                                                        ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-------------------|----------------------------------------------| | `verification_id` | Identify the transaction that has timed out. | |

### OnCodeSent

```c++
virtual void OnCodeSent(
  const std::string & verification_id,
  const ForceResendingToken & force_resending_token
)
```  
SMS message with verification code sent to phone number.

Called immediately after [Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth) server sends a verification SMS. Once receiving this, you can allow users to manually input the verification code (even if you're also performing auto-verification). For user manual input case, get the SMS verification code from the user and then call [GetCredential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider#classfirebase_1_1auth_1_1_phone_auth_provider_1a149b7a3daa4161cd754cdeeff2779437) with the user's code.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `verification_id`       | Pass to [GetCredential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider#classfirebase_1_1auth_1_1_phone_auth_provider_1a149b7a3daa4161cd754cdeeff2779437) along with the user-input verification code to complete the phone number verification flow. | | `force_resending_token` | If the user requests that another SMS message be sent, use this when you recall [VerifyPhoneNumber](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider#classfirebase_1_1auth_1_1_phone_auth_provider_1ad8b24001f507a420a3915d0f29865d84).                | |

### OnVerificationCompleted

```c++
virtual void OnVerificationCompleted(
  PhoneAuthCredential credential
)=0
```  
Phone number auto-verification succeeded.

Called when,

- auto-sms-retrieval has succeededflow (2) in [PhoneAuthProvider](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider#classfirebase_1_1auth_1_1_phone_auth_provider)
- instant validation has succeededflow (3) in [PhoneAuthProvider](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider#classfirebase_1_1auth_1_1_phone_auth_provider)

<br />


| **Note:** This callback is never called on iOS, since iOS does not have auto-validation. It is always called immediately in the stub desktop implementation, however, since it fakes immediate success.

<br />

|                                                                                        Details                                                                                        ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |--------------|-------------------------------------------------------------------| | `credential` | The completed credential from the phone number verification flow. | |

### OnVerificationFailed

```c++
virtual void OnVerificationFailed(
  const std::string & error
)=0
```  
Phone number verification failed with an error.

Called when and error occurred doing phone number authentication. For example,

- quota exceeded
- unknown phone number format

<br />

<br />

|                                               Details                                               ||
|------------|-----------------------------------------------------------------------------------------|
| Parameters | |---------|-------------------------------| | `error` | A description of the failure. | |

### \~Listener

```c++
virtual  ~Listener()
```