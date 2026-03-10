# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-result.md.txt

# firebase::functions::HttpsCallableResult Class Reference

# firebase::functions::HttpsCallableResult


`#include <callable_result.h>`

An [HttpsCallableResult](https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-result#classfirebase_1_1functions_1_1_https_callable_result) contains the result of calling an HttpsCallable.

## Summary

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-result#classfirebase_1_1functions_1_1_https_callable_result_1a0fbf93c5f6ec274c4142f8d2e1116381()` Creates an [HttpsCallableResult](https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-result#classfirebase_1_1functions_1_1_https_callable_result) with null data. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-result#classfirebase_1_1functions_1_1_https_callable_result_1a9ab85238a48112f42f1a2e00dde475de(const https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-result#classfirebase_1_1functions_1_1_https_callable_result & other)` Copy constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-result#classfirebase_1_1functions_1_1_https_callable_result_1acdd1894445007238d1bb13ae97acf601(https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-result#classfirebase_1_1functions_1_1_https_callable_result && other)` Move constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-result#classfirebase_1_1functions_1_1_https_callable_result_1a24d1fcb3d5e5407c2abaaf8c6e25e15c()` ||

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-result#classfirebase_1_1functions_1_1_https_callable_result_1a326f9b28241a62384c3895ce098c468b() const ` | `const https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant &` Returns the data that is the result of a Call. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-result#classfirebase_1_1functions_1_1_https_callable_result_1abadb88bb2ee2f1904747c67fe7fc5cfc(const https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-result#classfirebase_1_1functions_1_1_https_callable_result & other)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-result#classfirebase_1_1functions_1_1_https_callable_result &` Assignment operator. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-result#classfirebase_1_1functions_1_1_https_callable_result_1a716b900c4587f730a175b59492a008e8(https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-result#classfirebase_1_1functions_1_1_https_callable_result && other)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-result#classfirebase_1_1functions_1_1_https_callable_result &` Move assignment operator. |

## Public functions

### HttpsCallableResult

```c++
 HttpsCallableResult()
```
Creates an [HttpsCallableResult](https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-result#classfirebase_1_1functions_1_1_https_callable_result) with null data.

### HttpsCallableResult

```c++
 HttpsCallableResult(
  const HttpsCallableResult & other
)
```
Copy constructor.

Copying is as efficient as copying a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant).

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | [HttpsCallableResult](https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-result#classfirebase_1_1functions_1_1_https_callable_result) to copy data from. | |

### HttpsCallableResult

```c++
 HttpsCallableResult(
  HttpsCallableResult && other
)
```
Move constructor.

Moving is an efficient operation for [HttpsCallableResult](https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-result#classfirebase_1_1functions_1_1_https_callable_result) instances.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | [HttpsCallableResult](https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-result#classfirebase_1_1functions_1_1_https_callable_result) to move data from. | |

### data

```c++
const Variant & data() const 
```
Returns the data that is the result of a Call.

<br />

| Details ||
|---|---|
| **Returns** | The variant containing the data. |

### operator=

```c++
HttpsCallableResult & operator=(
  const HttpsCallableResult & other
)
```
Assignment operator.

Copying is as efficient as copying a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant).

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | [HttpsCallableResult](https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-result#classfirebase_1_1functions_1_1_https_callable_result) to copy data from. | |
| **Returns** | Reference to the destination [HttpsCallableResult](https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-result#classfirebase_1_1functions_1_1_https_callable_result). |

### operator=

```c++
HttpsCallableResult & operator=(
  HttpsCallableResult && other
)
```
Move assignment operator.

Moving is an efficient operation for [HttpsCallableResult](https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-result#classfirebase_1_1functions_1_1_https_callable_result) instances.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | [HttpsCallableResult](https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-result#classfirebase_1_1functions_1_1_https_callable_result) to move data from. | |
| **Returns** | Reference to the destination [HttpsCallableResult](https://firebase.google.com/docs/reference/cpp/class/firebase/functions/https-callable-result#classfirebase_1_1functions_1_1_https_callable_result). |

### \~HttpsCallableResult

```c++
 ~HttpsCallableResult()
```