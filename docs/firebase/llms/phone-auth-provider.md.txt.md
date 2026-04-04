# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider.md.txt

# firebase::auth::PhoneAuthProvider Class Reference

# firebase::auth::PhoneAuthProvider


`#include <credential.h>`

Use phone number text messages to authenticate.

## Summary

Allows developers to use the phone number and SMS verification codes to authenticate a user on a mobile device.

This class is not supported on tvOS and Desktop platforms.

The verification flow results in a [Credential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential) that can be used to,

- Sign in to an existing phone number account/sign up with a new phone number
- Link a phone number to a current user. This provider will be added to the user.
- Update a phone number on an existing user.
- Re-authenticate an existing user. This may be needed when a sensitive operation requires the user to be recently logged in.

<br />

Possible verification flows: (1) [User](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user) manually enters verification code.

- [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) calls [VerifyPhoneNumber](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider#classfirebase_1_1auth_1_1_phone_auth_provider_1ad8b24001f507a420a3915d0f29865d84).
- Web verification page is displayed to user where they may need to solve a CAPTCHA. \[iOS only\].
- [Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth) server sends the verification code via SMS to the provided phone number. [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) receives verification id via [Listener::OnCodeSent()](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider/listener#classfirebase_1_1auth_1_1_phone_auth_provider_1_1_listener_1a65f3a2abf007af3dfb1f8d2136bf4c29).
- [User](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user) receives SMS and enters verification code in app's GUI.
- [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) uses user's verification code to call [PhoneAuthProvider::GetCredential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider#classfirebase_1_1auth_1_1_phone_auth_provider_1a149b7a3daa4161cd754cdeeff2779437).

<br />

(2) SMS is automatically retrieved (Android only).

- [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) calls [VerifyPhoneNumber](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider#classfirebase_1_1auth_1_1_phone_auth_provider_1ad8b24001f507a420a3915d0f29865d84) with `timeout_ms` \> 0.
- [Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth) server sends the verification code via SMS to the provided phone number.
- SMS arrives and is automatically retrieved by the operating system. [Credential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential) is automatically created and passed to the app via [Listener::OnVerificationCompleted()](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider/listener#classfirebase_1_1auth_1_1_phone_auth_provider_1_1_listener_1a85770051624295e82b97a424bfe2efea).

<br />

(3) Phone number is instantly verified (Android only).

- [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) calls [VerifyPhoneNumber](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider#classfirebase_1_1auth_1_1_phone_auth_provider_1ad8b24001f507a420a3915d0f29865d84).
- The operating system validates the phone number without having to send an SMS. [Credential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential) is automatically created and passed to the app via [Listener::OnVerificationCompleted()](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider/listener#classfirebase_1_1auth_1_1_phone_auth_provider_1_1_listener_1a85770051624295e82b97a424bfe2efea).

<br />

All three flows can be handled with the example code below. The flow is complete when PhoneVerifier::credential() returns non-NULL.


```c++
class PhoneVerifier : public PhoneAuthProvider::Listener {
 public:
  PhoneVerifier(const char* phone_number,
                PhoneAuthProvider* phone_auth_provider)
    : display_message_("Sending SMS with verification code"),
      display_verification_code_input_box_(false),
      display_resend_sms_button_(false),
      phone_auth_provider_(phone_auth_provider),
      phone_number_(phone_number) {
    SendSms();
  }

  ~PhoneVerifier() override {}

  void OnVerificationCompleted(Credential credential) override {
    // Grab `mutex_` for the scope of `lock`. Callbacks can be called on
    // other threads, so this mutex ensures data access is atomic.
    MutexLock lock(mutex_);
    credential_ = credential;
  }

  void OnVerificationFailed(const std::string& error) override {
    MutexLock lock(mutex_);
    display_message_ = "Verification failed with error: " + error;
  }

  void OnCodeSent(const std::string& verification_id,
                  const PhoneAuthProvider::ForceResendingToken&
                      force_resending_token) override {
    MutexLock lock(mutex_);
    verification_id_ = verification_id;
    force_resending_token_ = force_resending_token;

    display_verification_code_input_box_ = true;
    display_message_ = "Waiting for SMS";
  }

  void OnCodeAutoRetrievalTimeOut(
      const std::string& verification_id) override {
    MutexLock lock(mutex_);
    display_resend_sms_button_ = true;
  }

  // Draw the verification GUI on screen and process input events.
  void Draw() {
    MutexLock lock(mutex_);

    // Draw an informative message describing what's currently happening.
    ShowTextBox(display_message_.c_str());

    // Once the time out expires, display a button to resend the SMS.
    // If the button is pressed, call VerifyPhoneNumber again using the
    // force_resending_token_.
    if (display_resend_sms_button_ && !verification_id_.empty()) {
      const bool resend_sms = ShowTextButton("Resend SMS");
      if (resend_sms) {
        SendSms();
      }
    }

    // Once the SMS has been sent, allow the user to enter the SMS
    // verification code into a text box. When the user has completed
    // entering it, call GetCredential() to complete the flow.
    if (display_verification_code_input_box_) {
      const std::string verification_code =
        ShowInputBox("Verification code");
      if (!verification_code.empty()) {
        credential_ = phone_auth_provider_->GetCredential(
            verification_id_.c_str(), verification_code.c_str());
      }
    }
  }

  // The phone number verification flow is complete when this returns
  // non-NULL.
  Credential* credential() {
    MutexLock lock(mutex_);
    return credential_.is_valid() ? &credential_ : nullptr;
  }

 private:
  void SendSms() {
    static const uint32_t kAutoVerifyTimeOut = 2000;
    MutexLock lock(mutex_);
    phone_auth_provider_->VerifyPhoneNumber(
        phone_number_.c_str(), kAutoVerifyTimeOut, &force_resending_token_,
        this);
    display_resend_sms_button_ = false;
  }

  // GUI-related variables.
  std::string display_message_;
  bool display_verification_code_input_box_;
  bool display_resend_sms_button_;

  // Phone flow related variables.
  PhoneAuthProvider* phone_auth_provider_;
  std::string phone_number_;
  std::string verification_id_;
  PhoneAuthProvider::ForceResendingToken force_resending_token_;
  Credential credential_;

  // Callbacks can be called on other threads, so guard them with a mutex.
  Mutex mutex_;
};
```

<br />

| ### Public static attributes ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider#classfirebase_1_1auth_1_1_phone_auth_provider_1a76386856f415f1802c47a4ddcfea9996` | `const char *const` The string used to identify this provider. |

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider#classfirebase_1_1auth_1_1_phone_auth_provider_1a149b7a3daa4161cd754cdeeff2779437(const char *verification_id, const char *verification_code)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-credential#classfirebase_1_1auth_1_1_phone_auth_credential` Generate a credential for the given phone number. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider#classfirebase_1_1auth_1_1_phone_auth_provider_1ad8b24001f507a420a3915d0f29865d84(const https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/phone-auth-options#structfirebase_1_1auth_1_1_phone_auth_options & options, https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider/listener#classfirebase_1_1auth_1_1_phone_auth_provider_1_1_listener *listener)` | `void` Start the phone number authentication operation. |

| ### Public static functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider#classfirebase_1_1auth_1_1_phone_auth_provider_1a5f68dc44352eb0cae46e8a62e6cf2b43(https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth *auth)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider#classfirebase_1_1auth_1_1_phone_auth_provider &` Return the [PhoneAuthProvider](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider#classfirebase_1_1auth_1_1_phone_auth_provider) for the specified `auth`. |

| ### Classes ||
|---|---|
| [firebase::auth::PhoneAuthProvider::ForceResendingToken](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider/force-resending-token) | Token to maintain current phone number verification session. |
| [firebase::auth::PhoneAuthProvider::Listener](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider/listener) | Receive callbacks from [VerifyPhoneNumber](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider#classfirebase_1_1auth_1_1_phone_auth_provider_1ad8b24001f507a420a3915d0f29865d84) events. |

## Public static attributes

### kProviderId

```c++
const char *const kProviderId
```
The string used to identify this provider.

## Public functions

### GetCredential

```c++
PhoneAuthCredential GetCredential(
  const char *verification_id,
  const char *verification_code
)
```
Generate a credential for the given phone number.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `verification_id` | The id returned when sending the verification code. Sent to the caller via [Listener::OnCodeSent](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider/listener#classfirebase_1_1auth_1_1_phone_auth_provider_1_1_listener_1a65f3a2abf007af3dfb1f8d2136bf4c29). | | `verification_code` | The verification code supplied by the user, most likely by a GUI where the user manually enters the code received in the SMS sent by [VerifyPhoneNumber](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider#classfirebase_1_1auth_1_1_phone_auth_provider_1ad8b24001f507a420a3915d0f29865d84). | |
| **Returns** | New [Credential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential). |

### VerifyPhoneNumber

```c++
void VerifyPhoneNumber(
  const PhoneAuthOptions & options,
  PhoneAuthProvider::Listener *listener
)
```
Start the phone number authentication operation.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `options` | The [PhoneAuthOptions](https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/phone-auth-options#structfirebase_1_1auth_1_1_phone_auth_options) struct with a verification configuration. | | `listener` | Class that receives notification whenever an SMS verification event occurs. | |

## Public static functions

### GetInstance

```c++
PhoneAuthProvider & GetInstance(
  Auth *auth
)
```
Return the [PhoneAuthProvider](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider#classfirebase_1_1auth_1_1_phone_auth_provider) for the specified `auth`.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `auth` | The [Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth) session for which we want to get a [PhoneAuthProvider](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider#classfirebase_1_1auth_1_1_phone_auth_provider). | |