# Source: https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/auth/fetch-providers-result.md.txt

# firebase::auth::Auth::FetchProvidersResult Struct Reference

# firebase::auth::Auth::FetchProvidersResult


`#include <auth.h>`

Results of calls FetchProvidersForEmail.

## Summary

|                                                                                                                                        ### Public attributes                                                                                                                                         ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| [providers](https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/auth/fetch-providers-result#structfirebase_1_1auth_1_1_auth_1_1_fetch_providers_result_1a70b448bcf4056aa857d366fc365975f7) | `std::vector< std::string >` The IDPs (identity providers) that can be used for `email`. |

## Public attributes

### providers

```c++
std::vector< std::string > firebase::auth::Auth::FetchProvidersResult::providers
```  
The IDPs (identity providers) that can be used for `email`.

An array of length `num_providers` of null-terminated strings.