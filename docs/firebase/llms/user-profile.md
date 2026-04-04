# Source: https://firebase.google.com/docs/reference/unity/class/firebase/auth/user-profile.md.txt

# Source: https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/user/user-profile.md.txt

# firebase::auth::User::UserProfile Struct Reference

# firebase::auth::User::UserProfile


`#include <user.h>`

Parameters to the [UpdateUserProfile()](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1a28ff1771991dbcee97a6d99e84ba0f6d) function.

## Summary

For fields you don't want to update, pass NULL. For fields you want to reset, pass "".

| ### Constructors and Destructors ||
|---|---|
| [UserProfile](https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/user/user-profile#structfirebase_1_1auth_1_1_user_1_1_user_profile_1a50360daabe722379af60b0f216856c93)`()` Construct a [UserProfile](https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/user/user-profile#structfirebase_1_1auth_1_1_user_1_1_user_profile) with no display name or photo URL. ||

|                                                                                                                                                         ### Public attributes                                                                                                                                                          ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| [display_name](https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/user/user-profile#structfirebase_1_1auth_1_1_user_1_1_user_profile_1a4bae837a5fcf0863fe2228fd4b151f8b) | `const char *` [User](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user) display name. |
| [photo_url](https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/user/user-profile#structfirebase_1_1auth_1_1_user_1_1_user_profile_1ab7fcca5f69159d73fcf3b64d3ef73fe5)    | `const char *` [User](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user) photo URI.    |

## Public attributes

### display_name

```c++
const char * firebase::auth::User::UserProfile::display_name
```  
[User](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user) display name.  

### photo_url

```c++
const char * firebase::auth::User::UserProfile::photo_url
```  
[User](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user) photo URI.

## Public functions

### UserProfile

```c++
 firebase::auth::User::UserProfile::UserProfile()
```  
Construct a [UserProfile](https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/user/user-profile#structfirebase_1_1auth_1_1_user_1_1_user_profile) with no display name or photo URL.