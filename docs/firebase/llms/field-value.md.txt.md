# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value.md.txt

# firebase::firestore::FieldValue Class Reference

# firebase::firestore::FieldValue


`#include <field_value.h>`

A field value represents variant datatypes as stored by [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore).

## Summary

[FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) can be used when reading a particular field with [DocumentSnapshot::Get()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot_1a75ca512289bd37032c0d30e222e07bcf) or fields with [DocumentSnapshot::GetData()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot_1a575b4e055541ecfb98f0621aa53c5f01). When writing document fields with [DocumentReference::Set()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference_1ace49a9db5c4c1f68ab85a36b1738eebc) or [DocumentReference::Update()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference_1a3aa6aef66a13b5601737a2cea610b179), it can also represent sentinel values in addition to real data values.

For a non-sentinel instance, you can check whether it is of a particular type with is_foo() and get the value with foo_value(), where foo can be one of null, boolean, integer, double, timestamp, string, blob, reference, geo_point, array or map. If the instance is not of type foo, the call to foo_value() will fail (and cause a crash).

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1a45c923f91d56627b75c06ee70daa67c3()` Creates an invalid [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) that has to be reassigned before it can be used. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1a8cb79b35bf5d2c16c6f2f6b209153787(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value & other)` Copy constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1a6c6a0cf49e220307e0eedbd9a19fd16d(https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value && other)` Move constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1add063d811662629e5d70292021d23940()` ||

| ### Public types ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1aae7d666fe5704aa8ec3aeee221bca661` | enumThe enumeration of all valid runtime types of [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value). |

| ### Friend classes ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1ae2bb68878c97ca2e82b6e4164f17d531` | `friend std::ostream &` Outputs the string representation of this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` to the given stream. |

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1ad7abc6ff8a8018cdbc400843c8761584() const ` | `std::string` Returns a string representation of this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` for logging/debugging purposes. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1ae65e5f3e14b8b7b90f2b46e110c98316() const ` | `std::vector< https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value >` Gets the vector of FieldValues contained in this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1a71763dada290752612b78d0b3737d6d2() const ` | `size_t` Gets the blob size contained in this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1a251978c77491d4df0ee457e1985c5408() const ` | `const uint8_t *` Gets the blob value contained in this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1a74de7ac104d1689e34f2bbd2743fdad5() const ` | `bool` Gets the boolean value contained in this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1aeb89fbe0174d9d51a243bd7455d8ed5b() const ` | `double` Gets the double value contained in this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1a250c214edff2b60c31114ca593dec53e() const ` | `class https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point` Gets the [GeoPoint](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point) value contained in this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1a01fd906083f9f7ff80c2ad7bae930bc7() const ` | `int64_t` Gets the integer value contained in this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1ad4fd21353140082f10d5b74372f450b7() const ` | `bool` Gets whether this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) contains an array of FieldValues. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1ae011ce9dd566dfbca1018ab6cea7fb50() const ` | `bool` Gets whether this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) contains a blob. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1a31c6d5c94aae79c27d4d4d0a24d20471() const ` | `bool` Gets whether this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) contains a boolean value. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1a5fe0773582a42d5bab2d7c416dbeb3f1() const ` | `bool` Gets whether this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) contains a double value. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1a2bcf64edd089284107d96419292a3c18() const ` | `bool` Gets whether this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) contains a [GeoPoint](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1aa265e47c362699f6d699ce3020c48050() const ` | `bool` Gets whether this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) contains an integer value. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1afd8e01b83b1253bd147cb4aa6ddd3a7e() const ` | `bool` Gets whether this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) contains a map of std::string to [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1ab3ae3019524e9d34f1de15a9bf1e550c() const ` | `bool` Gets whether this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) is currently null. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1a354a6e5405e52cdf67af1db68f204ee9() const ` | `bool` Gets whether this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) contains a reference to a document in the same [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1a1c2716d5fde409a2581baaa5a7cfad1e() const ` | `bool` Gets whether this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) contains a string. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1adfc49f1f651986265789855634185059() const ` | `bool` Gets whether this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) contains a timestamp. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1a7624885957a9aa6570e28d23d497d9da() const ` | `bool` Returns `true` if this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` is valid, `false` if it is not valid. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1a61f465732b6e05e77e06d933d8ca7dfe() const ` | `https://firebase.google.com/docs/reference/cpp/namespace/firebase/firestore#namespacefirebase_1_1firestore_1a8c836c76e7e87d8021bf3b33c8a71c7c` Gets the map of string to [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) contained in this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1aac09e35208f0f821b3c6d6ef8ab6c0e6(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value & other)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value &` Copy assignment operator. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1a21b1e01d7a803b4d7117566136f8d2d3(https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value && other) noexcept` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value &` Move assignment operator. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1a4538a3db08e0a567b5c875b727a8fa18() const ` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference` Gets the [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) contained in this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1a0d55f89753998395f4eff3fcc85f4f60() const ` | `std::string` Gets the string value contained in this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1aeb893841f48e3e4f63deadcffd5ab664() const ` | `class https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp` Gets the timestamp value contained in this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1a1f6868f0163616234680f9ab76344f21() const ` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1aae7d666fe5704aa8ec3aeee221bca661` Gets the current type contained in this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value). |

| ### Public static functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1a6391cfa0350e6c6cdeebbbd926075818(std::vector< https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value > value)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` Constructs a [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) containing the given [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) vector value. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1ab5d91fc8b4806a0d4168b372e83442c8(std::vector< https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value > elements)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` Returns a special value that can be used with Set() or Update() that tells the server to remove the given elements from any array value that already exists on the server. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1ac1afec9c75b7c89e00db18dab4568e94(std::vector< https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value > elements)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` Returns a special value that can be used with Set() or Update() that tells the server to union the given elements with any array value that already exists on the server. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1a017e2836fc39ff7f48ef3c36391d7165(const uint8_t *value, size_t size)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` Constructs a [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) containing the given blob value of given size. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1a700e66e7c0cf68e30c88d0b9963e2677(bool value)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` Constructs a [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) containing the given boolean value. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1ac3e445cdf6a56f62f4d7dd4f6015e81e()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` Returns a sentinel for use with Update() to mark a field for deletion. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1a21924bbac448cc58f740d6b27a83ee22(double value)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` Constructs a [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) containing the given double-precision floating point value. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1aa5701ea46e0fd192ca96b219e7df819e(https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point value)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` Constructs a [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) containing the given [GeoPoint](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point) value. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1aca49a435cad7ff4d2cbe20c17eef83b0(T by_value)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` Returns a special value that can be used with `Set()` or `Update()` that tells the server to increment the field's current value by the given integer value. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1aca49a435cad7ff4d2cbe20c17eef83b0(T by_value)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` Returns a special value that can be used with `Set()` or `Update()` that tells the server to increment the field's current value by the given floating point value. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1acb7fafdc0cdf464ff2c753f97a250f1f(int64_t value)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` Constructs a [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) containing the given 64-bit integer value. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1ade4029b4af459e6e2fad000f39b5916f(https://firebase.google.com/docs/reference/cpp/namespace/firebase/firestore#namespacefirebase_1_1firestore_1a8c836c76e7e87d8021bf3b33c8a71c7c value)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` Constructs a [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) containing the given [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) map value. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1a2f53ca0c77dfabd8ed8bd313721f960c()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` Constructs a null. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1ae23cfcd7eeaae6933aa20a37e0c487f5(https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference value)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` Constructs a [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) containing the given reference value. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1a3b819352e7dd45e30d427cee8ca78ee1()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` Returns a sentinel that can be used with Set() or Update() to include a server-generated timestamp in the written data. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1a30002edad4bb1ce74adecd3c9c539b34(std::string value)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` Constructs a [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) containing the given std::string value. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1a3d70b6af389b8de1db8c46a42fb55e14(https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp value)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` Constructs a [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) containing the given [Timestamp](https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp) value. |

## Public types

### Type

```c++
 Type
```
The enumeration of all valid runtime types of [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value).

## Friend classes

### operator\<\<

```c++
friend std::ostream & operator<<(std::ostream &out, const FieldValue &value)
```
Outputs the string representation of this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` to the given stream.

**See also:** `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1ad7abc6ff8a8018cdbc400843c8761584` for comments on the representation format.

## Public functions

### FieldValue

```c++
 FieldValue()
```
Creates an invalid [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) that has to be reassigned before it can be used.

Calling any member function on an invalid [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) will be a no-op. If the function returns a value, it will return a zero, empty, or invalid value, depending on the type of the value.

### FieldValue

```c++
 FieldValue(
  const FieldValue & other
)
```
Copy constructor.

`https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` is immutable and can be efficiently copied (no deep copy is performed).

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` to copy from. | |

### FieldValue

```c++
 FieldValue(
  FieldValue && other
) noexcept
```
Move constructor.

Moving is more efficient than copying for a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value`. After being moved from, a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` is equivalent to its default-constructed state.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` to move data from. | |

### ToString

```c++
std::string ToString() const 
```
Returns a string representation of this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` for logging/debugging purposes.


> [!NOTE]
> **Note:** the exact string representation is unspecified and subject to change; don't rely on the format of the string.

<br />

### array_value

```c++
std::vector< FieldValue > array_value() const 
```
Gets the vector of FieldValues contained in this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value).

### blob_size

```c++
size_t blob_size() const 
```
Gets the blob size contained in this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value).

### blob_value

```c++
const uint8_t * blob_value() const 
```
Gets the blob value contained in this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value).

### boolean_value

```c++
bool boolean_value() const 
```
Gets the boolean value contained in this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value).

### double_value

```c++
double double_value() const 
```
Gets the double value contained in this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value).

### geo_point_value

```c++
class GeoPoint geo_point_value() const 
```
Gets the [GeoPoint](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point) value contained in this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value).

### integer_value

```c++
int64_t integer_value() const 
```
Gets the integer value contained in this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value).

### is_array

```c++
bool is_array() const 
```
Gets whether this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) contains an array of FieldValues.

### is_blob

```c++
bool is_blob() const 
```
Gets whether this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) contains a blob.

### is_boolean

```c++
bool is_boolean() const 
```
Gets whether this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) contains a boolean value.

### is_double

```c++
bool is_double() const 
```
Gets whether this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) contains a double value.

### is_geo_point

```c++
bool is_geo_point() const 
```
Gets whether this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) contains a [GeoPoint](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point).

### is_integer

```c++
bool is_integer() const 
```
Gets whether this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) contains an integer value.

### is_map

```c++
bool is_map() const 
```
Gets whether this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) contains a map of std::string to [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value).

### is_null

```c++
bool is_null() const 
```
Gets whether this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) is currently null.

### is_reference

```c++
bool is_reference() const 
```
Gets whether this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) contains a reference to a document in the same [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore).

### is_string

```c++
bool is_string() const 
```
Gets whether this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) contains a string.

### is_timestamp

```c++
bool is_timestamp() const 
```
Gets whether this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) contains a timestamp.

### is_valid

```c++
bool is_valid() const 
```
Returns `true` if this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` is valid, `false` if it is not valid.

An invalid `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` could be the result of:

- Creating a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` using the default constructor.
- Moving from the `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value`.
- Calling `DocumentSnapshot::Get(field)` for a field that does not exist in the document.

<br />

<br />

| Details ||
|---|---|
| **Returns** | `true` if this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` is valid, `false` if this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` is invalid. |

### map_value

```c++
MapFieldValue map_value() const 
```
Gets the map of string to [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) contained in this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value).

### operator=

```c++
FieldValue & operator=(
  const FieldValue & other
)
```
Copy assignment operator.

`https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` is immutable and can be efficiently copied (no deep copy is performed).

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` to copy from. | |
| **Returns** | Reference to the destination `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value`. |

### operator=

```c++
FieldValue & operator=(
  FieldValue && other
) noexcept
```
Move assignment operator.

Moving is more efficient than copying for a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value`. After being moved from, a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` is equivalent to its default-constructed state.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` to move data from. | |
| **Returns** | Reference to the destination `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value`. |

### reference_value

```c++
DocumentReference reference_value() const 
```
Gets the [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) contained in this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value).

### string_value

```c++
std::string string_value() const 
```
Gets the string value contained in this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value).

### timestamp_value

```c++
class Timestamp timestamp_value() const 
```
Gets the timestamp value contained in this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value).

### type

```c++
Type type() const 
```
Gets the current type contained in this [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value).

### \~FieldValue

```c++
 ~FieldValue()
```

## Public static functions

### Array

```c++
FieldValue Array(
  std::vector< FieldValue > value
)
```
Constructs a [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) containing the given [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) vector value.

### ArrayRemove

```c++
FieldValue ArrayRemove(
  std::vector< FieldValue > elements
)
```
Returns a special value that can be used with Set() or Update() that tells the server to remove the given elements from any array value that already exists on the server.

All instances of each element specified will be removed from the array. If the field being modified is not already an array, it will be overwritten with an empty array.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `elements` | The elements to remove from the array. | |
| **Returns** | The [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) sentinel for use in a call to Set() or Update(). |

### ArrayUnion

```c++
FieldValue ArrayUnion(
  std::vector< FieldValue > elements
)
```
Returns a special value that can be used with Set() or Update() that tells the server to union the given elements with any array value that already exists on the server.

Each specified element that doesn't already exist in the array will be added to the end. If the field being modified is not already an array, it will be overwritten with an array containing exactly the specified elements.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `elements` | The elements to union into the array. | |
| **Returns** | The [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) sentinel for use in a call to Set() or Update(). |

### Blob

```c++
FieldValue Blob(
  const uint8_t *value,
  size_t size
)
```
Constructs a [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) containing the given blob value of given size.

`value` is copied into the returned [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value).

### Boolean

```c++
FieldValue Boolean(
  bool value
)
```
Constructs a [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) containing the given boolean value.

### Delete

```c++
FieldValue Delete()
```
Returns a sentinel for use with Update() to mark a field for deletion.

### Double

```c++
FieldValue Double(
  double value
)
```
Constructs a [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) containing the given double-precision floating point value.

### GeoPoint

```c++
FieldValue GeoPoint(
  GeoPoint value
)
```
Constructs a [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) containing the given [GeoPoint](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/geo-point#classfirebase_1_1firestore_1_1_geo_point) value.

### Increment

```c++
FieldValue Increment(
  T by_value
)
```
Returns a special value that can be used with `Set()` or `Update()` that tells the server to increment the field's current value by the given integer value.

If the current field value is an integer, possible integer overflows are resolved to `LONG_MAX` or `LONG_MIN`. If the current field value is a double, both values will be interpreted as doubles and the arithmetic will follow IEEE 754 semantics.

If field is not an integer or a double, or if the field does not yet exist, the transformation will set the field to the given value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `by_value` | The integer value to increment by. Should be an integer type not larger than `int64_t`. | |
| **Returns** | The [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) sentinel for use in a call to `Set()` or `Update().` |

### Increment

```c++
FieldValue Increment(
  T by_value
)
```
Returns a special value that can be used with `Set()` or `Update()` that tells the server to increment the field's current value by the given floating point value.

If the current field value is an integer, possible integer overflows are resolved to `LONG_MAX` or `LONG_MIN`. If the current field value is a double, both values will be interpreted as doubles and the arithmetic will follow IEEE 754 semantics.

If field is not an integer or a double, or if the field does not yet exist, the transformation will set the field to the given value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `by_value` | The double value to increment by. Should be a floating point type no larger than `double`. | |
| **Returns** | The [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) sentinel for use in a call to `Set()` or `Update().` |

### Integer

```c++
FieldValue Integer(
  int64_t value
)
```
Constructs a [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) containing the given 64-bit integer value.

### Map

```c++
FieldValue Map(
  MapFieldValue value
)
```
Constructs a [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) containing the given [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) map value.

### Null

```c++
FieldValue Null()
```
Constructs a null.

### Reference

```c++
FieldValue Reference(
  DocumentReference value
)
```
Constructs a [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) containing the given reference value.

### ServerTimestamp

```c++
FieldValue ServerTimestamp()
```
Returns a sentinel that can be used with Set() or Update() to include a server-generated timestamp in the written data.

### String

```c++
FieldValue String(
  std::string value
)
```
Constructs a [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) containing the given std::string value.

### Timestamp

```c++
FieldValue Timestamp(
  Timestamp value
)
```
Constructs a [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) containing the given [Timestamp](https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp) value.