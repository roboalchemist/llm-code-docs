# Source: https://firebase.google.com/docs/reference/unity/class/firebase/auth/user-info-interface.md.txt

# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user-info-interface.md.txt

# firebase::auth::UserInfoInterface Class Reference

# firebase::auth::UserInfoInterface


`#include <user.h>`

Interface implemented by each identity provider.

## Summary

### Inheritance

Direct Known Subclasses:[firebase::auth::User](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user)

| ### Constructors and Destructors ||
|---|---|
| [~UserInfoInterface](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user-info-interface#classfirebase_1_1auth_1_1_user_info_interface_1a23a4a5102ccfe856e85ca50ed491791e)`()` ||

|                                                                                                                                  ### Public functions                                                                                                                                  ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [display_name](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user-info-interface#classfirebase_1_1auth_1_1_user_info_interface_1a85295cc56bbbe4e2e05bcb7d6b745249)`() const ` | `virtual std::string` Gets the display name associated with the user, if any.      |
| [email](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user-info-interface#classfirebase_1_1auth_1_1_user_info_interface_1a12774ad23efe5a62853ef8a0deb87708)`() const `        | `virtual std::string` Gets email associated with the user, if any.                 |
| [phone_number](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user-info-interface#classfirebase_1_1auth_1_1_user_info_interface_1aea3186ad14aeb53fd8521eb75d58816d)`() const ` | `virtual std::string` Gets the phone number for the user, in E.164 format.         |
| [photo_url](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user-info-interface#classfirebase_1_1auth_1_1_user_info_interface_1a9abadeb204d12fd0d0a5a962d8349d28)`() const `    | `virtual std::string` Gets the photo url associated with the user, if any.         |
| [provider_id](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user-info-interface#classfirebase_1_1auth_1_1_user_info_interface_1acbdf133555e0bccf794c1584db62b958)`() const `  | `virtual std::string` Gets the provider ID for the user (For example, "Facebook"). |
| [uid](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user-info-interface#classfirebase_1_1auth_1_1_user_info_interface_1a39644e30a79b0cbc6841ebee691cc74c)`() const `          | `virtual std::string` Gets the unique Firebase user ID for the user.               |

## Public functions

### display_name

```c++
virtual std::string display_name() const 
```  
Gets the display name associated with the user, if any.  

### email

```c++
virtual std::string email() const 
```  
Gets email associated with the user, if any.  

### phone_number

```c++
virtual std::string phone_number() const 
```  
Gets the phone number for the user, in E.164 format.  

### photo_url

```c++
virtual std::string photo_url() const 
```  
Gets the photo url associated with the user, if any.  

### provider_id

```c++
virtual std::string provider_id() const 
```  
Gets the provider ID for the user (For example, "Facebook").  

### uid

```c++
virtual std::string uid() const 
```  
Gets the unique Firebase user ID for the user.


| **Note:** The user's ID, unique to the Firebase project. Do NOT use this value to authenticate with your backend server, if you have one. Use [User::GetToken()](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1a2214a2f314fd251bad6f318ec9eab22d) instead.

<br />

### \~UserInfoInterface

```c++
virtual  ~UserInfoInterface()
```