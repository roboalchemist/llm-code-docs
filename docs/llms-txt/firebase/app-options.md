# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/app-options.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/app-options.md.txt

# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/app-options.md.txt

# firebase::AppOptions Class Reference

# firebase::AppOptions


`#include <app.h>`

Options that control the creation of a Firebase [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app).

## Summary


**See also:**
[firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app)

| ### Constructors and Destructors ||
|---|---|
| [AppOptions](https://firebase.google.com/docs/reference/cpp/class/firebase/app-options#classfirebase_1_1_app_options_1a5e50b35c610e27f7f2b4f0318055dd47)`()` Create [AppOptions](https://firebase.google.com/docs/reference/cpp/class/firebase/app-options#classfirebase_1_1_app_options). ||

|                                                                                                                              ### Public functions                                                                                                                               ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| [api_key](https://firebase.google.com/docs/reference/cpp/class/firebase/app-options#classfirebase_1_1_app_options_1af27ddadf6ddfe379fb821d0fd7954d22)`() const `                               | `const char *` Get the API key.                                                 |
| [app_id](https://firebase.google.com/docs/reference/cpp/class/firebase/app-options#classfirebase_1_1_app_options_1a16d96ca57e90a5bc30a0a6fb94f79459)`() const `                                | `const char *` Retrieves the app ID.                                            |
| [database_url](https://firebase.google.com/docs/reference/cpp/class/firebase/app-options#classfirebase_1_1_app_options_1ad0261ff25346f8a4d82da2915ec58646)`() const `                          | `const char *` Get database root URL, e.g.                                      |
| [messaging_sender_id](https://firebase.google.com/docs/reference/cpp/class/firebase/app-options#classfirebase_1_1_app_options_1a0248e9f0fdb164d3d33383c0f4756183)`() const `                   | `const char *` Get the Firebase Cloud Messaging sender ID.                      |
| [project_id](https://firebase.google.com/docs/reference/cpp/class/firebase/app-options#classfirebase_1_1_app_options_1a5831a8c77eec92e30813f16a7655b853)`() const `                            | `const char *` Get the Google Cloud project ID.                                 |
| [set_api_key](https://firebase.google.com/docs/reference/cpp/class/firebase/app-options#classfirebase_1_1_app_options_1ac8ed231504a8c11838ed53f9b2ebf253)`(const char *key)`                   | `void` API key used to authenticate requests from your app.                     |
| [set_app_id](https://firebase.google.com/docs/reference/cpp/class/firebase/app-options#classfirebase_1_1_app_options_1a67573953fe43ce9b8cff6b0602409140)`(const char *id)`                     | `void` Set the Firebase app ID used to uniquely identify an instance of an app. |
| [set_database_url](https://firebase.google.com/docs/reference/cpp/class/firebase/app-options#classfirebase_1_1_app_options_1a171ef782c65c4deb5d8a109f985cef09)`(const char *url)`              | `void` Set the database root URL, e.g. "<http://abc-xyz-123.firebaseio.com>".   |
| [set_messaging_sender_id](https://firebase.google.com/docs/reference/cpp/class/firebase/app-options#classfirebase_1_1_app_options_1a6f0824a31d908b059316af8b3c595506)`(const char *sender_id)` | `void` Set the Firebase Cloud Messaging sender ID.                              |
| [set_project_id](https://firebase.google.com/docs/reference/cpp/class/firebase/app-options#classfirebase_1_1_app_options_1af2f9f576035e5eb289817cf2c0dd525c)`(const char *project)`            | `void` Set the Google Cloud project ID.                                         |
| [set_storage_bucket](https://firebase.google.com/docs/reference/cpp/class/firebase/app-options#classfirebase_1_1_app_options_1a9c651c380ee603d7028c5c03ee5c5307)`(const char *bucket)`         | `void` Set the Google Cloud Storage bucket name, e.g.                           |
| [storage_bucket](https://firebase.google.com/docs/reference/cpp/class/firebase/app-options#classfirebase_1_1_app_options_1a41bdfb8021440feac759d944ea6f5d34)`() const `                        | `const char *` Get the Google Cloud Storage bucket name,.                       |

|                                                                                                                                                                                                                              ### Public static functions                                                                                                                                                                                                                               ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [LoadFromJsonConfig](https://firebase.google.com/docs/reference/cpp/class/firebase/app-options#classfirebase_1_1_app_options_1a54f8d0909118ba7937362f36a259d91c)`(const char *config, `[AppOptions](https://firebase.google.com/docs/reference/cpp/class/firebase/app-options#classfirebase_1_1_app_options)` *options)` | [AppOptions](https://firebase.google.com/docs/reference/cpp/class/firebase/app-options#classfirebase_1_1_app_options)` *` Load options from a config string. |

## Public functions

### AppOptions

```c++
 AppOptions()
```  
Create [AppOptions](https://firebase.google.com/docs/reference/cpp/class/firebase/app-options#classfirebase_1_1_app_options).

To create a [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) object, the Firebase application identifier and API key should be set using [set_app_id()](https://firebase.google.com/docs/reference/cpp/class/firebase/app-options#classfirebase_1_1_app_options_1a67573953fe43ce9b8cff6b0602409140) and [set_api_key()](https://firebase.google.com/docs/reference/cpp/class/firebase/app-options#classfirebase_1_1_app_options_1ac8ed231504a8c11838ed53f9b2ebf253) respectively.

**See also:** [firebase::App::Create()](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app_1a5161747a9bbed350214cb5e1c0a23503).  

### api_key

```c++
const char * api_key() const 
```  
Get the API key.

**See also:** [set_api_key()](https://firebase.google.com/docs/reference/cpp/class/firebase/app-options#classfirebase_1_1_app_options_1ac8ed231504a8c11838ed53f9b2ebf253).  

### app_id

```c++
const char * app_id() const 
```  
Retrieves the app ID.

**See also:** [set_app_id()](https://firebase.google.com/docs/reference/cpp/class/firebase/app-options#classfirebase_1_1_app_options_1a67573953fe43ce9b8cff6b0602409140).  

### database_url

```c++
const char * database_url() const 
```  
Get database root URL, e.g.

"<http://abc-xyz-123.firebaseio.com>".  

### messaging_sender_id

```c++
const char * messaging_sender_id() const 
```  
Get the Firebase Cloud Messaging sender ID.

**See also:** [set_messaging_sender_id()](https://firebase.google.com/docs/reference/cpp/class/firebase/app-options#classfirebase_1_1_app_options_1a6f0824a31d908b059316af8b3c595506).  

### project_id

```c++
const char * project_id() const 
```  
Get the Google Cloud project ID.

This is the project_id in the Android google-services.json config file or PROJECT_ID in the GoogleService-Info.plist.  

### set_api_key

```c++
void set_api_key(
  const char *key
)
```  
API key used to authenticate requests from your app.

For example, "AIzaSyDdVgKwhZl0sTTTLZ7iTmt1r3N2cJLnaDk" used to identify your app to Google servers.

This only needs to be specified if your application does not include google-services.json or GoogleService-Info.plist in its resources.  

### set_app_id

```c++
void set_app_id(
  const char *id
)
```  
Set the Firebase app ID used to uniquely identify an instance of an app.

This is the mobilesdk_app_id in the Android google-services.json config file or GOOGLE_APP_ID in the GoogleService-Info.plist.

This only needs to be specified if your application does not include google-services.json or GoogleService-Info.plist in its resources.  

### set_database_url

```c++
void set_database_url(
  const char *url
)
```  
Set the database root URL, e.g. "<http://abc-xyz-123.firebaseio.com>".  

### set_messaging_sender_id

```c++
void set_messaging_sender_id(
  const char *sender_id
)
```  
Set the Firebase Cloud Messaging sender ID.

For example "012345678901", used to configure Firebase Cloud Messaging.

This only needs to be specified if your application does not include google-services.json or GoogleService-Info.plist in its resources.  

### set_project_id

```c++
void set_project_id(
  const char *project
)
```  
Set the Google Cloud project ID.  

### set_storage_bucket

```c++
void set_storage_bucket(
  const char *bucket
)
```  
Set the Google Cloud Storage bucket name, e.g.

\\"abc-xyz-123.storage.firebase.com\\".  

### storage_bucket

```c++
const char * storage_bucket() const 
```  
Get the Google Cloud Storage bucket name,.

**See also:** [set_storage_bucket()](https://firebase.google.com/docs/reference/cpp/class/firebase/app-options#classfirebase_1_1_app_options_1a9c651c380ee603d7028c5c03ee5c5307).

## Public static functions

### LoadFromJsonConfig

```c++
AppOptions * LoadFromJsonConfig(
  const char *config,
  AppOptions *options
)
```  
Load options from a config string.

<br />

|                                                                                                                                                                                                     Details                                                                                                                                                                                                     ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-----------|------------------------------------------------------------------------------------------------------------------| | `config`  | A JSON string that contains Firebase configuration i.e. the content of the downloaded google-services.json file. | | `options` | Optional: If provided, load options into it.                                                                     | |
| **Returns** | An instance containing the loaded options if successful. If the options argument to this function is null, this method returns an [AppOptions](https://firebase.google.com/docs/reference/cpp/class/firebase/app-options#classfirebase_1_1_app_options) instance allocated from the heap.                                                                                                          |