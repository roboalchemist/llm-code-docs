# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-reference.md.txt

# firebase::functions::HttpsCallableReference Class Reference

# firebase::functions::HttpsCallableReference


`#include <callable_reference.h>`

Represents a reference to a Cloud [Functions](https://firebase.google.com/docs/reference/cpp/class/firebase/functions/functions#classfirebase_1_1functions_1_1_functions) object.

## Summary

Developers can call HTTPS Callable [Functions](https://firebase.google.com/docs/reference/cpp/class/firebase/functions/functions#classfirebase_1_1functions_1_1_functions).

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-reference#classfirebase_1_1functions_1_1_https_callable_reference_1a9f3499a8610b0f6710c9762bdfd4a159()` Default constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-reference#classfirebase_1_1functions_1_1_https_callable_reference_1a6d561aa41b05bbb9eba078675bf87bd5(const https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-reference#classfirebase_1_1functions_1_1_https_callable_reference & reference)` Copy constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-reference#classfirebase_1_1functions_1_1_https_callable_reference_1a8cc5a68d24b86182bd13545a8936a94b(https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-reference#classfirebase_1_1functions_1_1_https_callable_reference && other)` Move constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-reference#classfirebase_1_1functions_1_1_https_callable_reference_1a467be1eb6576b4f4aea37b5a80192ded()` ||

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-reference#classfirebase_1_1functions_1_1_https_callable_reference_1ae2e740b7f794a20da1982dc8ffe0f5b9()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-result#classfirebase_1_1functions_1_1_https_callable_result >` Calls the function. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-reference#classfirebase_1_1functions_1_1_https_callable_reference_1a083095c77fec3c4dbeace8f9ba343c1e(const https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant & data)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-result#classfirebase_1_1functions_1_1_https_callable_result >` Calls the function. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-reference#classfirebase_1_1functions_1_1_https_callable_reference_1ac3192392c78e52be537224f50b61fb90()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/functions/functions#classfirebase_1_1functions_1_1_functions *` Gets the [firebase::functions::Functions](https://firebase.google.com/docs/reference/cpp/class/firebase/functions/functions#classfirebase_1_1functions_1_1_functions) instance to which we refer. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-reference#classfirebase_1_1functions_1_1_https_callable_reference_1a39d3f2a4e6d81d19cb55b349c5408402() const ` | `bool` Returns true if this [HttpsCallableReference](https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-reference#classfirebase_1_1functions_1_1_https_callable_reference) is valid, false if it is not valid. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-reference#classfirebase_1_1functions_1_1_https_callable_reference_1a1b64ac83a9489f9fdb10d522cc91afd5(const https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-reference#classfirebase_1_1functions_1_1_https_callable_reference & reference)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-reference#classfirebase_1_1functions_1_1_https_callable_reference &` Copy assignment operator. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-reference#classfirebase_1_1functions_1_1_https_callable_reference_1ab9b2cfa408f32ffa704bba2852920315(https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-reference#classfirebase_1_1functions_1_1_https_callable_reference && other)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-reference#classfirebase_1_1functions_1_1_https_callable_reference &` Move assignment operator. |

## Public functions

### Call

```c++
Future< HttpsCallableResult > Call()
```
Calls the function.

<br />

| Details ||
|---|---|
| **Returns** | The result of the call; |

### Call

```c++
Future< HttpsCallableResult > Call(
  const Variant & data
)
```
Calls the function.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `data` | The params to pass to the function. | |
| **Returns** | The result of the call; |

### HttpsCallableReference

```c++
 HttpsCallableReference()
```
Default constructor.

This creates an invalid [HttpsCallableReference](https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-reference#classfirebase_1_1functions_1_1_https_callable_reference). Attempting to perform any operations on this reference will fail unless a valid [HttpsCallableReference](https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-reference#classfirebase_1_1functions_1_1_https_callable_reference) has been assigned to it.

### HttpsCallableReference

```c++
 HttpsCallableReference(
  const HttpsCallableReference & reference
)
```
Copy constructor.

It's totally okay (and efficient) to copy [HttpsCallableReference](https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-reference#classfirebase_1_1functions_1_1_https_callable_reference) instances, as they simply point to the same location.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `reference` | [HttpsCallableReference](https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-reference#classfirebase_1_1functions_1_1_https_callable_reference) to copy from. | |

### HttpsCallableReference

```c++
 HttpsCallableReference(
  HttpsCallableReference && other
)
```
Move constructor.

Moving is an efficient operation for [HttpsCallableReference](https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-reference#classfirebase_1_1functions_1_1_https_callable_reference) instances.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | [HttpsCallableReference](https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-reference#classfirebase_1_1functions_1_1_https_callable_reference) to move data from. | |

### functions

```c++
Functions * functions()
```
Gets the [firebase::functions::Functions](https://firebase.google.com/docs/reference/cpp/class/firebase/functions/functions#classfirebase_1_1functions_1_1_functions) instance to which we refer.

The pointer will remain valid indefinitely.

<br />

| Details ||
|---|---|
| **Returns** | The [firebase::functions::Functions](https://firebase.google.com/docs/reference/cpp/class/firebase/functions/functions#classfirebase_1_1functions_1_1_functions) instance that this [HttpsCallableReference](https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-reference#classfirebase_1_1functions_1_1_https_callable_reference) refers to. |

### is_valid

```c++
bool is_valid() const 
```
Returns true if this [HttpsCallableReference](https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-reference#classfirebase_1_1functions_1_1_https_callable_reference) is valid, false if it is not valid.

An invalid [HttpsCallableReference](https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-reference#classfirebase_1_1functions_1_1_https_callable_reference) indicates that the reference is uninitialized (created with the default constructor) or that there was an error retrieving the reference.

<br />

| Details ||
|---|---|
| **Returns** | true if this [HttpsCallableReference](https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-reference#classfirebase_1_1functions_1_1_https_callable_reference) is valid, false if this [HttpsCallableReference](https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-reference#classfirebase_1_1functions_1_1_https_callable_reference) is invalid. |

### operator=

```c++
HttpsCallableReference & operator=(
  const HttpsCallableReference & reference
)
```
Copy assignment operator.

It's totally okay (and efficient) to copy [HttpsCallableReference](https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-reference#classfirebase_1_1functions_1_1_https_callable_reference) instances, as they simply point to the same location.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `reference` | [HttpsCallableReference](https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-reference#classfirebase_1_1functions_1_1_https_callable_reference) to copy from. | |
| **Returns** | Reference to the destination [HttpsCallableReference](https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-reference#classfirebase_1_1functions_1_1_https_callable_reference). |

### operator=

```c++
HttpsCallableReference & operator=(
  HttpsCallableReference && other
)
```
Move assignment operator.

Moving is an efficient operation for [HttpsCallableReference](https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-reference#classfirebase_1_1functions_1_1_https_callable_reference) instances.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | [HttpsCallableReference](https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-reference#classfirebase_1_1functions_1_1_https_callable_reference) to move data from. | |
| **Returns** | Reference to the destination [HttpsCallableReference](https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-reference#classfirebase_1_1functions_1_1_https_callable_reference). |

### \~HttpsCallableReference

```c++
 ~HttpsCallableReference()
```