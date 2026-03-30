# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction-options.md.txt

# firebase::firestore::TransactionOptions Class Reference

# firebase::firestore::TransactionOptions


`#include <transaction_options.h>`

Options to customize transaction behavior for `Firestore.runTransaction()`.

## Summary

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction-options#classfirebase_1_1firestore_1_1_transaction_options_1ae4b651df1c4dbc7fe7ff7a7a55532226()` Creates the default `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction-options#classfirebase_1_1firestore_1_1_transaction_options`. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction-options#classfirebase_1_1firestore_1_1_transaction_options_1a2fb2e09c62b6d377281fac239bfc3f13(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction-options#classfirebase_1_1firestore_1_1_transaction_options & other)` Copy constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction-options#classfirebase_1_1firestore_1_1_transaction_options_1a6760dab372ee10caa17b9d01749633d5(https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction-options#classfirebase_1_1firestore_1_1_transaction_options && other)` Move constructor. ||

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction-options#classfirebase_1_1firestore_1_1_transaction_options_1adca299bf70f83802b66148b70ccba18c() const ` | `std::string` Returns a string representation of this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction-options#classfirebase_1_1firestore_1_1_transaction_options` object for logging/debugging purposes. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction-options#classfirebase_1_1firestore_1_1_transaction_options_1a9b6afb002d655bfacf80240549a26e33() const ` | `int32_t` Gets the maximum number of attempts to commit, after which the transaction fails. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction-options#classfirebase_1_1firestore_1_1_transaction_options_1a70032ad1285f82e4ff546b5073e5eb92(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction-options#classfirebase_1_1firestore_1_1_transaction_options & other)=default` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction-options#classfirebase_1_1firestore_1_1_transaction_options &` Copy assignment operator. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction-options#classfirebase_1_1firestore_1_1_transaction_options_1a030bc3d8b14dbf7074644fc0f739c044(https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction-options#classfirebase_1_1firestore_1_1_transaction_options && other)=default` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction-options#classfirebase_1_1firestore_1_1_transaction_options &` Move assignment operator. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction-options#classfirebase_1_1firestore_1_1_transaction_options_1ad38cd17206e39a9752d56644ade12c77(int32_t max_attempts)` | `void` Sets the maximum number of attempts to commit, after which the transaction fails. |

| ### Friend classes ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction-options#classfirebase_1_1firestore_1_1_transaction_options_1a5c5ac9778aa15d8b88e4181ff9db82b0` | `friend std::ostream &` Outputs the string representation of this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction-options#classfirebase_1_1firestore_1_1_transaction_options` object to the given stream. |

## Public functions

### ToString

```c++
std::string ToString() const 
```
Returns a string representation of this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction-options#classfirebase_1_1firestore_1_1_transaction_options` object for logging/debugging purposes.


> [!NOTE]
> **Note:** the exact string representation is unspecified and subject to change; don't rely on the format of the string.

<br />

### TransactionOptions

```c++
 TransactionOptions()=default
```
Creates the default `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction-options#classfirebase_1_1firestore_1_1_transaction_options`.

### TransactionOptions

```c++
 TransactionOptions(
  const TransactionOptions & other
)=default
```
Copy constructor.

This performs a deep copy, creating an independent instance.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction-options#classfirebase_1_1firestore_1_1_transaction_options` to copy from. | |

### TransactionOptions

```c++
 TransactionOptions(
  TransactionOptions && other
)=default
```
Move constructor.

Moving is not any more efficient than copying for `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction-options#classfirebase_1_1firestore_1_1_transaction_options` because this class is trivially copyable; however, future additions to this class may make it not trivially copyable, at which point moving would be more efficient than copying. After being moved from, `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction-options#classfirebase_1_1firestore_1_1_transaction_options` is in a valid but unspecified state.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction-options#classfirebase_1_1firestore_1_1_transaction_options` to move data from. | |

### max_attempts

```c++
int32_t max_attempts() const 
```
Gets the maximum number of attempts to commit, after which the transaction fails.

The default value is 5.

### operator=

```c++
TransactionOptions & operator=(
  const TransactionOptions & other
)=default
```
Copy assignment operator.

This performs a deep copy, creating an independent instance.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction-options#classfirebase_1_1firestore_1_1_transaction_options` to copy from. | |
| **Returns** | Reference to the destination `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction-options#classfirebase_1_1firestore_1_1_transaction_options`. |

### operator=

```c++
TransactionOptions & operator=(
  TransactionOptions && other
)=default
```
Move assignment operator.

Moving is not any more efficient than copying for `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction-options#classfirebase_1_1firestore_1_1_transaction_options` because this class is trivially copyable; however, future additions to this class may make it not trivially copyable, at which point moving would be more efficient than copying. After being moved from, `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction-options#classfirebase_1_1firestore_1_1_transaction_options` is in a valid but unspecified state.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction-options#classfirebase_1_1firestore_1_1_transaction_options` to move data from. | |
| **Returns** | Reference to the destination `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction-options#classfirebase_1_1firestore_1_1_transaction_options`. |

### set_max_attempts

```c++
void set_max_attempts(
  int32_t max_attempts
)
```
Sets the maximum number of attempts to commit, after which the transaction fails.

The default value is 5.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `max_attempts` | The maximum number of attempts; must be greater than zero. | |

## Friend classes

### operator\<\<

```c++
friend std::ostream & operator<<(std::ostream &, const TransactionOptions &)
```
Outputs the string representation of this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction-options#classfirebase_1_1firestore_1_1_transaction_options` object to the given stream.

**See also:** `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction-options#classfirebase_1_1firestore_1_1_transaction_options_1adca299bf70f83802b66148b70ccba18c` for comments on the representation format.