# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/variant.md.txt

# firebase::Variant Class Reference

# firebase::Variant


`#include <variant.h>`

[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) data type used by Firebase libraries.

## Summary

| ### Constructors and Destructors ||
|---|---|
| [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1ad4417ed5a59b99ad370d6baab2850fc4)`()` Construct a null [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant). ||
| [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1afb30b564129107050ee61c5612a870a5)`(T value)` Construct a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) with the given templated type. ||
| [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1aaf440f3716ed46fdcba18c1f4a2f8109)`(const std::string & value)` Construct a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing the given string value (makes a copy). ||
| [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1af4ff4674a4ea140eb74c66d2f1dc4893)`(const std::vector< `[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)` > & value)` Construct a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing the given std::vector of [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant). ||
| [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1aa361ad6b25c70323cc18a19ae1d9e472)`(const std::vector< T > & value)` Construct a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing the given std::vector of something that can be constructed into a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant). ||
| [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a4c5da9332000eb578cec61b27775ef8a)`(const T array_of_values[], size_t array_size)` Construct a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) from an array of supported types into a Vector. ||
| [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1aa01c7173ed132bbbc700b4494e21dc70)`(const std::map< `[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)`, `[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)` > & value)` Construct a Variatn containing the given std::map of [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) to [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant). ||
| [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a6ce0f6bb2468d7390c8dd16d9da41cf6)`(const std::map< K, V > & value)` Construct a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing the given std::map of something that can be constructed into a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant), to something that can be constructed into a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant). ||
| [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a6cc3131bf93a5d95ffbe338b26674f5e)`(const `[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)` & other)` Copy constructor. ||
| [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a530f91afb6bd667bda817a5341058755)`(`[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)` && other)` Move constructor. ||
| [~Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1aabf383eed0a7edbce2e3398659a51f76)`()` Destructor. Frees the memory that this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) owns. ||

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ### Public types                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| [Type](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a186a23e71959f678215d2c6cece6ddf1)`{` ` `[kTypeNull](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a186a23e71959f678215d2c6cece6ddf1abb3f2d9832b554399ebf0fd5d790896c)`,` ` `[kTypeInt64](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a186a23e71959f678215d2c6cece6ddf1a0c672e4d4ff759325e8955e160b85436)`,` ` `[kTypeDouble](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a186a23e71959f678215d2c6cece6ddf1a5a3ab8ceabb9b532863bb8ff7483fc3e)`,` ` `[kTypeBool](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a186a23e71959f678215d2c6cece6ddf1accbb445d18e2ecc5ba6244aeb9f488dd)`,` ` `[kTypeStaticString](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a186a23e71959f678215d2c6cece6ddf1aa2fe144a4817d080e5a840b8f62657e6)`,` ` `[kTypeMutableString](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a186a23e71959f678215d2c6cece6ddf1ab8eb50d9186ffa1d7bebd9ddab6171ce)`,` ` `[kTypeVector](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a186a23e71959f678215d2c6cece6ddf1add868c1404fbab8712d41754960de9f8)`,` ` `[kTypeMap](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a186a23e71959f678215d2c6cece6ddf1a95df4995cd6c837a6a21e5576b1a06c0)`,` ` `[kTypeStaticBlob](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a186a23e71959f678215d2c6cece6ddf1ad3dcaa73712ffe0c42fd69f4d2dd0caa)`,` ` `[kTypeMutableBlob](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a186a23e71959f678215d2c6cece6ddf1ab5e5a04b7e5bf27ec8346db471cfc7a1) `}` | enum Type of data that this variant object contains. |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                          ### Public functions                                                                                                                                                                                                                                                                                                                                                                                                                                                           ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AsBool](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1ab43a4b15db7bddf49a98ee822e7b8dc6)`() const `                                                                                                                                                                                                                                               | [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) Get the current [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) converted into a boolean.                                                                                                                                                                                                                                                                  |
| [AsDouble](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a7829a18339c00c03f3690079f9684d6c)`() const `                                                                                                                                                                                                                                             | [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) Get the current [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) converted into a floating-point number.                                                                                                                                                                                                                                                    |
| [AsInt64](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a66e9612eef63064df0f61d13b1d24bfd)`() const `                                                                                                                                                                                                                                              | [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) Get the current [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) converted into an integer.                                                                                                                                                                                                                                                                 |
| [AsString](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a32c5fa03ab6c2c7a70423283b09bd93e)`() const `                                                                                                                                                                                                                                             | [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) Get the current [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) converted into a string.                                                                                                                                                                                                                                                                   |
| [AssignMap](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a83457c7fbf0cb6f2a94fd7fcabb67039)`(std::map< `[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)`, `[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)` > **map)`       | `void` Assigns an existing map which was allocated on the heap into the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) without performing a copy.                                                                                                                                                                                                                                                                                                                    |
| [AssignMutableString](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1ad5b601bec15b37a57584f44e48538bfa)`(std::string **str)`                                                                                                                                                                                                                        | `void` Assigns an existing string which was allocated on the heap into the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) without performing a copy.                                                                                                                                                                                                                                                                                                                 |
| [AssignVector](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a92b0dcdefe620f70bac5101fa6d0ad9c)`(std::vector< `[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)` > **vect)`                                                                                                              | `void` Assigns an existing vector which was allocated on the heap into the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) without performing a copy.                                                                                                                                                                                                                                                                                                                 |
| [Clear](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a4a33654e5d89b323457efdc190f331dd)`(`[Type](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a186a23e71959f678215d2c6cece6ddf1)` new_type)`                                                                                                  | `void` Clear the given [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) data, optionally into a new type.                                                                                                                                                                                                                                                                                                                                                              |
| [blob_data](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a080ff7ce9125a6456f38942793b201d1)`() const `                                                                                                                                                                                                                                            | `const uint8_t *` Get the pointer to the binary data contained in a blob.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [blob_size](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a16c3aa5f37c719bf8040cbbecea71f8b)`() const `                                                                                                                                                                                                                                            | `size_t` Get the size of a blob.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [bool_value](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a247b188170dc9b41203f92e9d072c122)`() const `                                                                                                                                                                                                                                           | `const bool &` Const accessor for a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing a bool.                                                                                                                                                                                                                                                                                                                                                                |
| [double_value](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a090daa70019bf3846b8fa95a080660bb)`() const `                                                                                                                                                                                                                                         | `double` Const accessor for a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing a double.                                                                                                                                                                                                                                                                                                                                                                    |
| [int64_value](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1aad5c6263c017fc21029cbff453efbb48)`() const `                                                                                                                                                                                                                                          | `int64_t` Const accessor for a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing an integer.                                                                                                                                                                                                                                                                                                                                                                 |
| [is_blob](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a303a1a32e6d802f9ed858ae7d6adfd6d)`() const `                                                                                                                                                                                                                                              | `bool` Get whether this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) contains a blob.                                                                                                                                                                                                                                                                                                                                                                              |
| [is_bool](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a6cf87a68eed5d0f855ff8af6a8ad536e)`() const `                                                                                                                                                                                                                                              | `bool` Get whether this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) contains a bool.                                                                                                                                                                                                                                                                                                                                                                              |
| [is_container_type](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a98d7af8d0e6cdb922ffb2786337c338e)`() const `                                                                                                                                                                                                                                    | `bool` Get whether this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) contains a container type: Vector or Map.                                                                                                                                                                                                                                                                                                                                                     |
| [is_double](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a61013eaaabab3bf4821539ffe20998e2)`() const `                                                                                                                                                                                                                                            | `bool` Get whether this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) contains a double.                                                                                                                                                                                                                                                                                                                                                                            |
| [is_fundamental_type](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1acf65d0584e7c5c822200549221ab7987)`() const `                                                                                                                                                                                                                                  | `bool` Get whether this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) contains a fundamental type: Null, Int64, Double, Bool, or one of the two String types.                                                                                                                                                                                                                                                                                                       |
| [is_int64](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1ae027517ef79b3378b02cb0a75b0466a3)`() const `                                                                                                                                                                                                                                             | `bool` Get whether this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) contains an integer.                                                                                                                                                                                                                                                                                                                                                                          |
| [is_map](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a553149fda8694447f508b46161bccd76)`() const `                                                                                                                                                                                                                                               | `bool` Get whether this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) contains a map.                                                                                                                                                                                                                                                                                                                                                                               |
| [is_mutable_blob](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1af453263bb747cb4a23ff46c0727df00b)`() const `                                                                                                                                                                                                                                      | `bool` Get whether this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) contains a mutable blob.                                                                                                                                                                                                                                                                                                                                                                      |
| [is_mutable_string](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a19eae453c73f9f123874b43b8ffa4ca4)`() const `                                                                                                                                                                                                                                    | `bool` Get whether this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) contains a mutable string.                                                                                                                                                                                                                                                                                                                                                                    |
| [is_null](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1acc4b107bbc4e5dc7a7a55ee7fca3adb0)`() const `                                                                                                                                                                                                                                              | `bool` Get whether this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) is currently null.                                                                                                                                                                                                                                                                                                                                                                            |
| [is_numeric](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a6109b9ac50c3a45e2155886d31de0ab4)`() const `                                                                                                                                                                                                                                           | `bool` Get whether this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) contains a numeric type, Int64 or Double.                                                                                                                                                                                                                                                                                                                                                     |
| [is_static_blob](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a8fb7c12d75c6f19213b1f25a69e51caa)`() const `                                                                                                                                                                                                                                       | `bool` Get whether this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) contains a static blob.                                                                                                                                                                                                                                                                                                                                                                       |
| [is_static_string](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1aef3ac8abec97242c888e4c726597bd8e)`() const `                                                                                                                                                                                                                                     | `bool` Get whether this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) contains a static string.                                                                                                                                                                                                                                                                                                                                                                     |
| [is_string](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a00e2e0475680c273bf7de5e782b7023c)`() const `                                                                                                                                                                                                                                            | `bool` Get whether this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) contains a string.                                                                                                                                                                                                                                                                                                                                                                            |
| [is_vector](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1ae924a40af357f53db329425e1bc9d248)`() const `                                                                                                                                                                                                                                            | `bool` Get whether this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) contains a vector.                                                                                                                                                                                                                                                                                                                                                                            |
| [map](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a14c106a7c035ea56e0eb630c338820b0)`()`                                                                                                                                                                                                                                                         | `std::map< `[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)`, `[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)` > &` Mutable accessor for a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing a map of [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) data.                |
| [map](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a292c22fa5de2baa46578644906eb51ab)`() const `                                                                                                                                                                                                                                                  | `const std::map< `[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)`, `[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)` > &` Const accessor for a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing a map of strings to [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) data. |
| [mutable_blob_data](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a900e8bb1fb61260cb19c2de34d1af1aa)`()`                                                                                                                                                                                                                                           | `uint8_t *` Get a mutable pointer to the binary data contained in a blob.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [mutable_blob_data](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1abb6f7958c7a9734198d34d5637cf7dbf)`() const `                                                                                                                                                                                                                                    | `uint8_t *` Const accessor for a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) contianing mutable blob data.                                                                                                                                                                                                                                                                                                                                                        |
| [mutable_string](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a9251c28af47fcd13757f0d5fd4e4ffc9)`()`                                                                                                                                                                                                                                              | `std::string &` Mutable accessor for a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing a string.                                                                                                                                                                                                                                                                                                                                                           |
| [mutable_string](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a09a9cd3ad8179952153b369e02769591)`() const `                                                                                                                                                                                                                                       | `std::string` Const accessor for a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing a string.                                                                                                                                                                                                                                                                                                                                                               |
| [operator!=](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1aeea5b8b8b6f0b30885c6d9747c20dc14)`(const `[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)` & other) const `                                                                                                                 | `bool` Inequality operator: x != y is evaluated as !(x == y).                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [operator<](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a89ca6c319fd531879d2def0d54f46625)`(const `[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)` & other) const `                                                                                                                  | `bool` Inequality operator, only meant for internal use.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [operator<=](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a955dbeb0054c0f6de3484fa18cdecbcc)`(const `[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)` & other) const `                                                                                                                 | `bool` Inequality operator: x \<= y is evaluated as !(x \> y)                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [operator=](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a683825ec8163a263337120fb364ddbef)`(const `[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)` & other)`                                                                                                                         | [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)` &` Copy assignment operator.                                                                                                                                                                                                                                                                                                                                                                                         |
| [operator=](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1ac957298bd798dbbe8a31c706044d016e)`(`[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)` && other) noexcept`                                                                                                                     | [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)` &` Move assignment operator.                                                                                                                                                                                                                                                                                                                                                                                         |
| [operator==](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a4c4a7024e4694aa8588fe23fa054d670)`(const `[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)` & other) const `                                                                                                                 | `bool` Equality operator.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [operator>](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1ad0380f8b0ce86368efebf54d7823dab4)`(const `[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)` & other) const `                                                                                                                  | `bool` Inequality operator: x \> y is evaluated as y \< x.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [operator>=](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1add2aafc0a65882e034cc41743bb7889b)`(const `[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)` & other) const `                                                                                                                 | `bool` Inequality operator: x \>= y is evaluated as !(x \< y)                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [set_bool_value](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1ab5a6fbd7aee5c5fcf5b9f1e96ddc0c47)`(bool value)`                                                                                                                                                                                                                                    | `void` Sets the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) to the given boolean value.                                                                                                                                                                                                                                                                                                                                                                           |
| [set_double_value](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a1c4d1c3179ee486cd8cb81420f8ed02c)`(double value)`                                                                                                                                                                                                                                | `void` Sets the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) to an double-precision floating point value.                                                                                                                                                                                                                                                                                                                                                          |
| [set_int64_value](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a9e99b6f5dadca2973218774b095c27ae)`(int64_t value)`                                                                                                                                                                                                                                | `void` Sets the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) to an 64-bit integer value.                                                                                                                                                                                                                                                                                                                                                                           |
| [set_map](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a4fbd1be786e58d3e8a62df09008eacaa)`(const std::map< `[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)`, `[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)` > & value)` | `void` Sets the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) to a copy of the given map.                                                                                                                                                                                                                                                                                                                                                                           |
| [set_mutable_blob](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a0d4d14a8b3fb05978ad7ec499576d4b4)`(const void *src_data, size_t size_bytes)`                                                                                                                                                                                                     | `void` Sets the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) to a copy of the given binary data.                                                                                                                                                                                                                                                                                                                                                                   |
| [set_mutable_string](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a4e1b5e81df10fe31b8cf700bb8bc6653)`(const std::string & value, bool use_small_string)`                                                                                                                                                                                          | `void` Sets the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) to a copy of the given string.                                                                                                                                                                                                                                                                                                                                                                        |
| [set_null](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a5ff60ccab8f984622e31be7fae87ade3)`()`                                                                                                                                                                                                                                                    | `void` Sets the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) value to null.                                                                                                                                                                                                                                                                                                                                                                                        |
| [set_static_blob](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1acf89af59b693d087b8b57d08ed4e62e8)`(const void *static_data, size_t size_bytes)`                                                                                                                                                                                                   | `void` Sets the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) to point to static binary data.                                                                                                                                                                                                                                                                                                                                                                       |
| [set_string_value](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a2e5ff0117468094b0eb27e5908d0e527)`(const char *value)`                                                                                                                                                                                                                           | `void` Sets the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) to point to a static string buffer.                                                                                                                                                                                                                                                                                                                                                                   |
| [set_string_value](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a6fd0f849abfb67fc28b0e91b713416c3)`(char *value)`                                                                                                                                                                                                                                 | `void` Sets the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) to a mutable string.                                                                                                                                                                                                                                                                                                                                                                                  |
| [set_string_value](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1ae7386879d8caf9f4e7bfbc743e8a88bf)`(const std::string & value)`                                                                                                                                                                                                                   | `void` Sets the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) to a mutable string.                                                                                                                                                                                                                                                                                                                                                                                  |
| [set_vector](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a276a1ed8855a9a63a6632bd9b5956864)`(const std::vector< `[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)` > & value)`                                                                                                         | `void` Sets the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) to a copy of the given vector.                                                                                                                                                                                                                                                                                                                                                                        |
| [string_value](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1af93cb329bff0357e5435223089c3d375)`() const `                                                                                                                                                                                                                                         | `const char *` Const accessor for a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing a string.                                                                                                                                                                                                                                                                                                                                                              |
| [type](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a60a7e500025e93547684a96a979ee413)`() const `                                                                                                                                                                                                                                                 | [Type](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a186a23e71959f678215d2c6cece6ddf1) Get the current type contained in this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant).                                                                                                                                                                                                                                    |
| [vector](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a24f62801e317339dec02c242d6bd57c2)`()`                                                                                                                                                                                                                                                      | `std::vector< `[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)` > &` Mutable accessor for a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing a vector of [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) data.                                                                                                                        |
| [vector](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1ad5e5ed5a03181eb0053390ca045aa295)`() const `                                                                                                                                                                                                                                               | `const std::vector< `[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)` > &` Const accessor for a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing a vector of [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) data.                                                                                                                    |

|                                                                                                                                                                                                                                                                                           ### Public static functions                                                                                                                                                                                                                                                                                            ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [EmptyMap](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a50c570355384a10db088b0b9684a18f8)`()`                                                                                                                                                  | [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) Get a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing an empty map.                                                        |
| [EmptyMutableBlob](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1ac827a26897029a574be33df7c5559b96)`(size_t size_bytes)`                                                                                                                         | [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) Return a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing an empty mutable blob of the requested size, filled with 0-bytes. |
| [EmptyMutableString](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a9d85a432eba25a009a2e7b508bdb8f6a)`()`                                                                                                                                        | [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) Get a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing an empty mutable string.                                             |
| [EmptyString](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a7e493fd37616ce5913d48d9d35bf192d)`()`                                                                                                                                               | [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) Get an empty string variant.                                                                                                                                                                     |
| [EmptyVector](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a52395f2c31da28050d29d3e02e8b06af)`()`                                                                                                                                               | [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) Get a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing an empty vector.                                                     |
| [False](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a58fc0f239239e033fbf754fe7c20ddf2)`()`                                                                                                                                                     | [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) Get a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) of bool value false.                                                            |
| [FromBool](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a3ac269783b0cd633b175b82da624e2b3)`(bool value)`                                                                                                                                        | [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) Return a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) from a boolean.                                                              |
| [FromDouble](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a8bd830b41aca84815c2c1af5d200a002)`(double value)`                                                                                                                                    | [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) Return a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) from a double-precision floating point number.                               |
| [FromInt64](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1ab7b37f77dc471d923b8cf1d791c6b8a2)`(int64_t value)`                                                                                                                                    | [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) Return a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) from a 64-bit integer.                                                       |
| [FromMutableBlob](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a162e582ad6645546f1c53ebe9fb08ddd)`(const void *src_data, size_t size_bytes)`                                                                                                    | [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) Return a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing a copy of binary data.                                            |
| [FromMutableString](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a56561fd23a61fe794d7d4b5d4f320494)`(const std::string & value)`                                                                                                                | [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) Return a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) from a string.                                                               |
| [FromStaticBlob](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a15a255dcadfe55adf1c49bdcb5505aff)`(const void *static_data, size_t size_bytes)`                                                                                                  | [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) Return a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) that points to static binary data.                                           |
| [FromStaticString](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1ab3a9257e58b904e86c40cf20f11d0472)`(const char *value)`                                                                                                                         | [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) Return a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) from a static string.                                                        |
| [MutableStringFromStaticString](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a64d1e49f84515a8a56a93ecd6021b02d)`(const char *value)`                                                                                                            | [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) Return a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) from a string, but make it mutable.                                          |
| [Null](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a44ad99ff82979b9cd8d483504b4877b7)`()`                                                                                                                                                      | [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) Get a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) of type Null.                                                                   |
| [One](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1ae273dbb9a86a640e1eb29e6cc5ce64a3)`()`                                                                                                                                                       | [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) Get a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) of integer value 1.                                                             |
| [OnePointZero](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1ae1a2589bcb3615ee0b5ecf272430e1fd)`()`                                                                                                                                              | [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) Get a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) of double value 1.0.                                                            |
| [True](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a71f7d0e2ef52fece8eedec032a2520f1)`()`                                                                                                                                                      | [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) Get a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) of bool value true.                                                             |
| [TypeName](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a0ec7da68774493364ec071477bf19b1c)`(`[Type](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a186a23e71959f678215d2c6cece6ddf1)` type)` | `const char *` Get the human-readable type name of a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) type.                                                                                                                                       |
| [Zero](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a22e651a96c4de89af4e68132d747d639)`()`                                                                                                                                                      | [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) Get a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) of integer value 0.                                                             |
| [ZeroPointZero](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a7ab8ad27db32a5969e8c3d998a96c7ea)`()`                                                                                                                                             | [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) Get a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) of double value 0.0.                                                            |

## Public types

### Type

```c++
 Type
```  
Type of data that this variant object contains.

|                                                                                                                                                                                                                                                                      Properties                                                                                                                                                                                                                                                                       ||
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `kTypeBool`          | A boolean value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `kTypeDouble`        | A double-precision floating point number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `kTypeInt64`         | A 64-bit integer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `kTypeMap`           | A std::map, mapping [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) to [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant).                                                                                                                                                                                                                                                                                   |
| `kTypeMutableBlob`   | A blob of data that the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) holds. Never constructed by default. Use [Variant::FromMutableBlob()](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a162e582ad6645546f1c53ebe9fb08ddd) to create a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) of this type, and copy binary data from an existing source. |
| `kTypeMutableString` | A std::string.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `kTypeNull`          | Null, or no data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `kTypeStaticBlob`    | An statically-allocated blob of data that we point to. Never constructed by default. Use [Variant::FromStaticBlob()](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a15a255dcadfe55adf1c49bdcb5505aff) to create a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) of this type.                                                                                                                                   |
| `kTypeStaticString`  | A statically-allocated string we point to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `kTypeVector`        | A std::vector of [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant).                                                                                                                                                                                                                                                                                                                                                                                                    |

## Public functions

### AsBool

```c++
Variant AsBool() const 
```  
Get the current [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) converted into a boolean.

Null, 0, 0.0, empty strings, empty vectors, empty maps, blobs of size 0, and "false" (case-sensitive) are all considered false. All other values are true.

<br />

|                                                                                                                                             Details                                                                                                                                              ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) of type Bool containing the original [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) interpreted as a Bool. |

### AsDouble

```c++
Variant AsDouble() const 
```  
Get the current [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) converted into a floating-point number.

Only valid for fundamental types.

Special cases: If a Bool is true, this will return 1. All other cases will return 0.

<br />

|                                                                                                                                               Details                                                                                                                                                ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing a Double that represents the value of this original [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant). |

### AsInt64

```c++
Variant AsInt64() const 
```  
Get the current [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) converted into an integer.

Only valid for fundamental types.

Special cases: If a String can be parsed as a number via strtol(), it will be. If a Bool is true, this will return 1. All other cases (including non-fundamental types) will return 0.

<br />

|                                                                                                                                               Details                                                                                                                                                ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing an Int64 that represents the value of this original [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant). |

### AsString

```c++
Variant AsString() const 
```  
Get the current [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) converted into a string.

Only valid for fundamental types.

Special cases: Booleans will be returned as "true" or "false". Null will be returned as an empty string. The returned string may be either mutable or static, depending on the source type. All other cases will return an empty string.

<br />

|                                                                                                                                               Details                                                                                                                                                ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing a String that represents the value of this original [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant). |

### AssignMap

```c++
void AssignMap(
  std::map< Variant, Variant > **map
)
```  
Assigns an existing map which was allocated on the heap into the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) without performing a copy.

This object will take over ownership of the map, and will set the std::map\*\* you pass in to NULL.

The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)'s type will be set to Map.

<br />

|                                                                                                                                                                                                                                                                 Details                                                                                                                                                                                                                                                                 ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `map` | Pointer to a pointer to an STL map. The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) will take over ownership of the pointer to the map, and set the pointer you passed in to NULL. | |

### AssignMutableString

```c++
void AssignMutableString(
  std::string **str
)
```  
Assigns an existing string which was allocated on the heap into the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) without performing a copy.

This object will take over ownership of the pointer, and will set the std::string\* you pass in to NULL.

The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)'s type will be set to MutableString.

<br />

|                                                                                                                                                                                                                                                                       Details                                                                                                                                                                                                                                                                       ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `str` | Pointer to a pointer to an STL string. The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) will take over ownership of the pointer to the string, and set the pointer you passed in to NULL. | |

### AssignVector

```c++
void AssignVector(
  std::vector< Variant > **vect
)
```  
Assigns an existing vector which was allocated on the heap into the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) without performing a copy.

This object will take over ownership of the pointer, and will set the std::vector\* you pass in to NULL.

The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)'s type will be set to Vector.

<br />

|                                                                                                                                                                                                                                                                        Details                                                                                                                                                                                                                                                                        ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `vect` | Pointer to a pointer to an STL vector. The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) will take over ownership of the pointer to the vector, and set the pointer you passed in to NULL. | |

### Clear

```c++
void Clear(
  Type new_type
)
```  
Clear the given [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) data, optionally into a new type.

Frees up any memory that might have been allocated. After calling this, you can access the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) as the new type.

<br />

|                                                                                                                                                                                                                                                                                                                                   Details                                                                                                                                                                                                                                                                                                                                   ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `new_type` | Optional new type to clear the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) to. You may immediately begin using the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) as that new type. | |

### Variant

```c++
 Variant()
```  
Construct a null [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant).

The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) constructed will be of type Null.  

### Variant

```c++
 Variant(
  T value
)
```  
Construct a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) with the given templated type.


Valid types for this constructor are `int`, `int64_t`, `float`, `double`, `bool`, `const char*`, and `char*` (but see below for additional [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) types).

|                                                     Details                                                     ||
|------------|-----------------------------------------------------------------------------------------------------|
| Parameters | |---------|-------------------------------------| | `value` | The value to construct the variant. | |

Type `int` or `int64_t`:

- The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) constructed will be of type Int64.

<br />

Type `double` or `float`:

- The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) constructed will be of type Double.

<br />

Type `bool`:

- The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) constructed will be of type Bool.

<br />

Type `const char*`:

- The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) constructed will be of type StaticString, and [is_string()](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a00e2e0475680c273bf7de5e782b7023c) will return true. **Note:** If you use this constructor, you must ensure that the memory pointed to stays valid for the life of the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant), otherwise call [mutable_string()](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a9251c28af47fcd13757f0d5fd4e4ffc9) or [set_mutable_string()](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a4e1b5e81df10fe31b8cf700bb8bc6653), which will copy the string to an internal buffer.

<br />

Type `char*`:

- The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) constructed will be of type MutableString, and [is_string()](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a00e2e0475680c273bf7de5e782b7023c) will return true.

<br />

Other types will result in compiler error unless using the following constructor overloads:

- `std::string`
- `std::vector<`[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)`>`
- `std::vector` where T is convertible to variant type
- `T*`, `size_t` where T is convertible to variant type
- `std::map<`[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)`, `[Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)`>`
- `std::map` where K and V is convertible to variant type

<br />

### Variant

```c++
 Variant(
  const std::string & value
)
```  
Construct a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing the given string value (makes a copy).

The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) constructed will be of type MutableString, and [is_string()](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a00e2e0475680c273bf7de5e782b7023c) will return true.

<br />

|                                                                                                                                                       Details                                                                                                                                                       ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------|---------------------------------------------------------------------------------------------------------------------------------------| | `value` | The string to use for the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant). | |

### Variant

```c++
 Variant(
  const std::vector< Variant > & value
)
```  
Construct a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing the given std::vector of [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant).

The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) constructed will be of type Vector.

<br />

|                                                                                                                                                             Details                                                                                                                                                             ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------|---------------------------------------------------------------------------------------------------------------------------------------------| | `value` | The STL vector to copy into the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant). | |

### Variant

```c++
 Variant(
  const std::vector< T > & value
)
```  
Construct a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing the given std::vector of something that can be constructed into a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant).

The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) constructed will be of type Vector.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `value` | An STL vector containing elements that can be converted to [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) (such as ints, strings, vectors). A [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) will be created for each element, and copied into the Vector [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) constructed here. | |

### Variant

```c++
 Variant(
  const T array_of_values[],
  size_t array_size
)
```  
Construct a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) from an array of supported types into a Vector.

The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) constructed will be of type Vector.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `array_of_values` | A C array containing elements that can be converted to [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) (such as ints, strings, vectors). A [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) will be created for each element, and copied into the Vector [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) constructed here. | | `array_size`      | Number of elements of the array.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | |

### Variant

```c++
 Variant(
  const std::map< Variant, Variant > & value
)
```  
Construct a Variatn containing the given std::map of [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) to [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant).

The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) constructed will be of type Map.

<br />

|                                                                                                                                                          Details                                                                                                                                                          ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------|------------------------------------------------------------------------------------------------------------------------------------------| | `value` | The STL map to copy into the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant). | |

### Variant

```c++
 Variant(
  const std::map< K, V > & value
)
```  
Construct a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing the given std::map of something that can be constructed into a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant), to something that can be constructed into a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant).

The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) constructed will be of type Map.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `value` | An STL map containing keys and values that can be converted to [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) (such as ints, strings, vectors). A [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) will be created for each key and for each value, and copied by pairs into the Map [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) constructed here. | |

### Variant

```c++
 Variant(
  const Variant & other
)
```  
Copy constructor.

Performs a deep copy.

<br />

|                                                                                                                                                 Details                                                                                                                                                 ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------|---------------------------------------------------------------------------------------------------------------------------------| | `other` | Source [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) to copy from. | |

### Variant

```c++
 Variant(
  Variant && other
) noexcept
```  
Move constructor.

Efficiently moves the more complex data types by simply reassigning pointer ownership.

<br />

|                                                                                                                                                 Details                                                                                                                                                 ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------|---------------------------------------------------------------------------------------------------------------------------------| | `other` | Source [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) to move from. | |

### blob_data

```c++
const uint8_t * blob_data() const 
```  
Get the pointer to the binary data contained in a blob.

This method works with both static and mutable blob.

<br />

|                                                                                                          Details                                                                                                           ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | Pointer to the binary data. Use [blob_size()](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a16c3aa5f37c719bf8040cbbecea71f8b) to get the number of bytes. |

### blob_size

```c++
size_t blob_size() const 
```  
Get the size of a blob.

This method works with both static and mutable blobs.

<br />

|                              Details                               ||
|-------------|-------------------------------------------------------|
| **Returns** | Number of bytes of binary data contained in the blob. |

### bool_value

```c++
const bool & bool_value() const 
```  
Const accessor for a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing a bool.


| **Note:** If the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) is not of Bool type, this will assert.

<br />

|                                                                       Details                                                                       ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | The bool contained in this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant). |

### double_value

```c++
double double_value() const 
```  
Const accessor for a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing a double.


| **Note:** If the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) is not of Double type, this will assert.

<br />

|                                                                        Details                                                                        ||
|-------------|------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | The double contained in this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant). |

### int64_value

```c++
int64_t int64_value() const 
```  
Const accessor for a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing an integer.


| **Note:** If the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) is not of Int64 type, this will assert.

<br />

|                                                                        Details                                                                         ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | The integer contained in this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant). |

### is_blob

```c++
bool is_blob() const 
```  
Get whether this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) contains a blob.


| **Note:** No matter which type of blob the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) contains, you can read its data via [blob_data()](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a080ff7ce9125a6456f38942793b201d1) and get its size via [blob_size()](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a16c3aa5f37c719bf8040cbbecea71f8b).

<br />

|                                                                                             Details                                                                                              ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | True if the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)'s type is either StaticBlob or MutableBlob; false otherwise. |

### is_bool

```c++
bool is_bool() const 
```  
Get whether this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) contains a bool.

<br />

|                                                                               Details                                                                                ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | True if the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)'s type is Bool, false otherwise. |

### is_container_type

```c++
bool is_container_type() const 
```  
Get whether this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) contains a container type: Vector or Map.

<br />

|                                                                                    Details                                                                                    ||
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | True if the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)'s type is Vector or Map; false otherwise. |

### is_double

```c++
bool is_double() const 
```  
Get whether this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) contains a double.

<br />

|                                                                                Details                                                                                 ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | True if the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)'s type is Double, false otherwise. |

### is_fundamental_type

```c++
bool is_fundamental_type() const 
```  
Get whether this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) contains a fundamental type: Null, Int64, Double, Bool, or one of the two String types.

Essentially !is_containerType().

<br />

|                                                                                           Details                                                                                            ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | True if the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)'s type is Int64, Double, Bool, or Null; false otherwise. |

### is_int64

```c++
bool is_int64() const 
```  
Get whether this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) contains an integer.

<br />

|                                                                                Details                                                                                ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | True if the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)'s type is Int64, false otherwise. |

### is_map

```c++
bool is_map() const 
```  
Get whether this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) contains a map.

<br />

|                                                                               Details                                                                               ||
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | True if the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)'s type is Map, false otherwise. |

### is_mutable_blob

```c++
bool is_mutable_blob() const 
```  
Get whether this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) contains a mutable blob.

<br />

|                                                                                   Details                                                                                   ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | True if the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)'s type is MutableBlob, false otherwise. |

### is_mutable_string

```c++
bool is_mutable_string() const 
```  
Get whether this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) contains a mutable string.

<br />

|                                                                                    Details                                                                                    ||
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | True if the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)'s type is MutableString, false otherwise. |

### is_null

```c++
bool is_null() const 
```  
Get whether this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) is currently null.

<br />

|                                                                            Details                                                                            ||
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | True if the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) is Null, false otherwise. |

### is_numeric

```c++
bool is_numeric() const 
```  
Get whether this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) contains a numeric type, Int64 or Double.

<br />

|                                                                                        Details                                                                                         ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | True if the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)'s type is either Int64 or Double; false otherwise. |

### is_static_blob

```c++
bool is_static_blob() const 
```  
Get whether this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) contains a static blob.

<br />

|                                                                                  Details                                                                                   ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | True if the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)'s type is StaticBlob, false otherwise. |

### is_static_string

```c++
bool is_static_string() const 
```  
Get whether this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) contains a static string.

<br />

|                                                                                   Details                                                                                    ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | True if the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)'s type is StaticString, false otherwise. |

### is_string

```c++
bool is_string() const 
```  
Get whether this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) contains a string.


| **Note:** No matter which type of string the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) contains, you can read its value via [string_value()](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1af93cb329bff0357e5435223089c3d375).

<br />

|                                                                                                       Details                                                                                                       ||
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | True if the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)'s type is either StaticString or MutableString or SmallString; false otherwise. |

### is_vector

```c++
bool is_vector() const 
```  
Get whether this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) contains a vector.

<br />

|                                                                                Details                                                                                 ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | True if the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)'s type is Vector, false otherwise. |

### map

```c++
std::map< Variant, Variant > & map()
```  
Mutable accessor for a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing a map of [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) data.


| **Note:** If the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) is not of Map type, this will assert.

<br />

|                                                                             Details                                                                             ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | Reference to the map contained in this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant). |

### map

```c++
const std::map< Variant, Variant > & map() const 
```  
Const accessor for a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing a map of strings to [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) data.


| **Note:** If the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) is not of Map type, this will assert.

<br />

|                                                                             Details                                                                             ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | Reference to the map contained in this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant). |

### mutable_blob_data

```c++
uint8_t * mutable_blob_data()
```  
Get a mutable pointer to the binary data contained in a blob.

If the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) contains a static blob, it will be converted into a mutable blob, which copies the binary data into the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)'s buffer.

<br />

|                                                             Details                                                              ||
|-------------|---------------------------------------------------------------------------------------------------------------------|
| **Returns** | Pointer to a mutable buffer of binary data. The size of the buffer cannot be changed, but the contents are mutable. |

### mutable_blob_data

```c++
uint8_t * mutable_blob_data() const 
```  
Const accessor for a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) contianing mutable blob data.


| **Note:** Unlike the non-const accessor, this accessor cannot "promote" a static blob to mutable, and thus will assert if the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) you pass in is not of MutableBlob type.

<br />

|                                                             Details                                                              ||
|-------------|---------------------------------------------------------------------------------------------------------------------|
| **Returns** | Pointer to a mutable buffer of binary data. The size of the buffer cannot be changed, but the contents are mutable. |

### mutable_string

```c++
std::string & mutable_string()
```  
Mutable accessor for a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing a string.

If the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) contains a static string, it will be converted into a mutable string, which copies the const char\*'s data into a std::string.


| **Note:** If the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) is not one of the two String types, this will assert.

<br />

|                                                                              Details                                                                               ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | Reference to the string contained in this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant). |

### mutable_string

```c++
std::string mutable_string() const 
```  
Const accessor for a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing a string.


| **Note:** Unlike the non-const accessor, this accessor cannot "promote" a static string to mutable, and thus returns a std::string copy instead of a const reference to a std::string

<br />

|                                                                                     Details                                                                                     ||
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | std::string with the string contents contained in this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant). |

### operator!=

```c++
bool operator!=(
  const Variant & other
) const 
```  
Inequality operator: x != y is evaluated as !(x == y).

<br />

|                                                                                                                                           Details                                                                                                                                            ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|---------------------------------------------------------------------------------------------------------------------------| | `other` | [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) to compare to. | |
| **Returns** | Results of the comparison.                                                                                                                                                                                                                                                      |

### operator\<

```c++
bool operator<(
  const Variant & other
) const 
```  
Inequality operator, only meant for internal use.

Explanation: In order to use [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) as a key for std::map, we must provide a comparison function. This comparison function is ONLY for std::map to be able to use a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) as a map key.

We define v1 \< v2 IFF:

- If different types, compare type as int: v1.type() \< v2.type() (note: this means that Variant(1) \< [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)(0.0) - be careful!)
- If both are int64: v1.int64_value() \< v2.int64_value();
- If both are double: v1.double_value() \< v2.double_value()
- If both are bool: v1.bool_value() \< v2.bool_value();
- If both are either static or mutable strings: strcmp(v1, v2) \< 0
- If both are vectors:
  - If v1\[0\] \< v2\[0\], that means v1 \< v2 == true. Otherwise:
  - If v1\[0\] \> v2\[0\], that means v1 \< v2 == false. Otherwise:
  - Continue to the next element of both vectors and compare again.
  - If you reach the end of one vector first, that vector is considered to be lesser.
- If both are maps, iterate similar to vectors (since maps are ordered), but for each element, first compare the key, then the value.
- If both are blobs, the smaller-sized blob is considered lesser. If both blobs are the same size, use memcmp to compare the bytes.

<br />

We have defined this operation such that if !(v1 \< v2) \&\& !(v2 \< v1), it must follow that v1 == v2.


| **Note:** This will not give you the results you expect if you compare Variants of different types! For example, [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)(0.0) \< Variant(1).

<br />

|                                                                                                                                           Details                                                                                                                                            ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|---------------------------------------------------------------------------------------------------------------------------| | `other` | [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) to compare to. | |
| **Returns** | Results of the comparison, as described in this documentation.                                                                                                                                                                                                                  |

### operator\<=

```c++
bool operator<=(
  const Variant & other
) const 
```  
Inequality operator: x \<= y is evaluated as !(x \> y)

<br />

|                                                                                                                                           Details                                                                                                                                            ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|---------------------------------------------------------------------------------------------------------------------------| | `other` | [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) to compare to. | |
| **Returns** | Results of the comparison.                                                                                                                                                                                                                                                      |

### operator=

```c++
Variant & operator=(
  const Variant & other
)
```  
Copy assignment operator.

Performs a deep copy.

<br />

|                                                                                                                                                 Details                                                                                                                                                 ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------|---------------------------------------------------------------------------------------------------------------------------------| | `other` | Source [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) to copy from. | |

### operator=

```c++
Variant & operator=(
  Variant && other
) noexcept
```  
Move assignment operator.

Efficiently moves the more complex data types by simply reassigning pointer ownership.

<br />

|                                                                                                                                                 Details                                                                                                                                                 ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------|---------------------------------------------------------------------------------------------------------------------------------| | `other` | Source [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) to move from. | |

### operator==

```c++
bool operator==(
  const Variant & other
) const 
```  
Equality operator.

Both the type and the value must be equal (except that static strings CAN be == to mutable strings). For container types, element-by-element comparison is performed. For strings, string comparison is performed.

<br />

|                                                                                                                                           Details                                                                                                                                            ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|---------------------------------------------------------------------------------------------------------------------------| | `other` | [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) to compare to. | |
| **Returns** | True if the Variants are of identical types and values, false otherwise.                                                                                                                                                                                                        |

### operator\>

```c++
bool operator>(
  const Variant & other
) const 
```  
Inequality operator: x \> y is evaluated as y \< x.

<br />

|                                                                                                                                           Details                                                                                                                                            ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|---------------------------------------------------------------------------------------------------------------------------| | `other` | [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) to compare to. | |
| **Returns** | Results of the comparison.                                                                                                                                                                                                                                                      |

### operator\>=

```c++
bool operator>=(
  const Variant & other
) const 
```  
Inequality operator: x \>= y is evaluated as !(x \< y)

<br />

|                                                                                                                                           Details                                                                                                                                            ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|---------------------------------------------------------------------------------------------------------------------------| | `other` | [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) to compare to. | |
| **Returns** | Results of the comparison.                                                                                                                                                                                                                                                      |

### set_bool_value

```c++
void set_bool_value(
  bool value
)
```  
Sets the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) to the given boolean value.

The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)'s type will be set to Bool.

<br />

|                                                                                                                                                       Details                                                                                                                                                       ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------|---------------------------------------------------------------------------------------------------------------------------------------| | `value` | The boolean value for the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant). | |

### set_double_value

```c++
void set_double_value(
  double value
)
```  
Sets the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) to an double-precision floating point value.

The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)'s type will be set to Double.

<br />

|                                                                                                                                                                               Details                                                                                                                                                                               ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------| | `value` | The double-precision floating point value for the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant). | |

### set_int64_value

```c++
void set_int64_value(
  int64_t value
)
```  
Sets the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) to an 64-bit integer value.

The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)'s type will be set to Int64.

<br />

|                                                                                                                                                              Details                                                                                                                                                              ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------|----------------------------------------------------------------------------------------------------------------------------------------------| | `value` | The 64-bit integer value for the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant). | |

### set_map

```c++
void set_map(
  const std::map< Variant, Variant > & value
)
```  
Sets the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) to a copy of the given map.

The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)'s type will be set to Map.

<br />

|                                                                                                                                                          Details                                                                                                                                                          ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------|------------------------------------------------------------------------------------------------------------------------------------------| | `value` | The STL map to copy into the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant). | |

### set_mutable_blob

```c++
void set_mutable_blob(
  const void *src_data,
  size_t size_bytes
)
```  
Sets the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) to a copy of the given binary data.

The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)'s type will be set to MutableBlob.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                              Details                                                                                                                                                                                                                                                                                                                                                                                               ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `src_data`   | The data to use for the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant). If you pass in nullptr, no data will be copied, but a buffer of the requested size will be allocated. | | `size_bytes` | The size of the data, in bytes.                                                                                                                                                                                                           | |

### set_mutable_string

```c++
void set_mutable_string(
  const std::string & value,
  bool use_small_string
)
```  
Sets the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) to a copy of the given string.

The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)'s type will be set to SmallString if the size of the string is less than kMaxSmallStringSize (8 bytes on x86, 16 bytes on x64) or otherwise set to MutableString.

<br />

|                                                                                                                                                                                                                                                 Details                                                                                                                                                                                                                                                  ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |--------------------|---------------------------------------------------------------------------------------------------------------------------------------| | `value`            | The string to use for the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant). | | `use_small_string` | Check to see if the input string should be treated as a small string or left as a mutable string                                      | |

### set_null

```c++
void set_null()
```  
Sets the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) value to null.

The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)'s type will be Null.  

### set_static_blob

```c++
void set_static_blob(
  const void *static_data,
  size_t size_bytes
)
```  
Sets the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) to point to static binary data.

The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)'s type will be set to kTypeStaticBlob.


| **Note:** If you use this method, you must ensure that the memory pointer to stays valid for the life of the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant), or otherwise call [mutable_blob_data()](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a900e8bb1fb61260cb19c2de34d1af1aa) or [set_mutable_blob()](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a0d4d14a8b3fb05978ad7ec499576d4b4), which will copy the data into an internal buffer.

<br />

|                                                                                                                                                                                                                                                                                                                                  Details                                                                                                                                                                                                                                                                                                                                   ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `static_data` | Pointer to statically-allocated binary data. The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) will point to the data, not copy it. | | `size_bytes`  | Size of the data, in bytes.                                                                                                                                                                      | |

### set_string_value

```c++
void set_string_value(
  const char *value
)
```  
Sets the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) to point to a static string buffer.

The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)'s type will be set to StaticString.


| **Note:** If you use this method, you must ensure that the memory pointed to stays valid for the life of the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant), or otherwise call [mutable_string()](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a9251c28af47fcd13757f0d5fd4e4ffc9) or [set_mutable_string()](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a4e1b5e81df10fe31b8cf700bb8bc6653), which will copy the string to an internal buffer.

<br />

|                                                                                                                                                                                    Details                                                                                                                                                                                    ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `value` | A pointer to the static null-terminated string for the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant). | |

### set_string_value

```c++
void set_string_value(
  char *value
)
```  
Sets the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) to a mutable string.

The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)'s type will be set to MutableString.

<br />

|                                                                                                                                                                                                     Details                                                                                                                                                                                                     ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `value` | A pointer to a null-terminated string, which will be copied into to the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant). | |

### set_string_value

```c++
void set_string_value(
  const std::string & value
)
```  
Sets the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) to a mutable string.

The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)'s type will be set to MutableString.

<br />

|                                                                                                                                                       Details                                                                                                                                                       ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------|---------------------------------------------------------------------------------------------------------------------------------------| | `value` | The string to use for the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant). | |

### set_vector

```c++
void set_vector(
  const std::vector< Variant > & value
)
```  
Sets the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) to a copy of the given vector.

The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)'s type will be set to Vector.

<br />

|                                                                                                                                                             Details                                                                                                                                                             ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------|---------------------------------------------------------------------------------------------------------------------------------------------| | `value` | The STL vector to copy into the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant). | |

### string_value

```c++
const char * string_value() const 
```  
Const accessor for a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing a string.

This can return both static and mutable strings. The pointer is only guaranteed to persist if this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)'s type is StaticString.


| **Note:** If the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) is not of StaticString or MutableString type, this will assert.

<br />

|                                                                        Details                                                                        ||
|-------------|------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | The string contained in this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant). |

### type

```c++
Type type() const 
```  
Get the current type contained in this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant).

<br />

|                                                               Details                                                               ||
|-------------|------------------------------------------------------------------------------------------------------------------------|
| **Returns** | The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant)'s type. |

### vector

```c++
std::vector< Variant > & vector()
```  
Mutable accessor for a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing a vector of [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) data.


| **Note:** If the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) is not of Vector type, this will assert.

<br />

|                                                                              Details                                                                               ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | Reference to the vector contained in this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant). |

### vector

```c++
const std::vector< Variant > & vector() const 
```  
Const accessor for a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing a vector of [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) data.


| **Note:** If the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) is not of Vector type, this will assert.

<br />

|                                                                              Details                                                                               ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | Reference to the vector contained in this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant). |

### \~Variant

```c++
 ~Variant()
```  
Destructor. Frees the memory that this [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) owns.

## Public static functions

### EmptyMap

```c++
Variant EmptyMap()
```  
Get a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing an empty map.

You can immediately call [map()](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a14c106a7c035ea56e0eb630c338820b0) on it to work with the map it contains.

<br />

|                                                                            Details                                                                             ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) of type Map, containing no elements. |

### EmptyMutableBlob

```c++
Variant EmptyMutableBlob(
  size_t size_bytes
)
```  
Return a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing an empty mutable blob of the requested size, filled with 0-bytes.

<br />

|                                                                                             Details                                                                                             ||
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |--------------|----------------------------------------| | `size_bytes` | Size of the buffer you want, in bytes. |                                                                |
| **Returns** | A [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing a mutable blob of the requested size, filled with 0-bytes. |

### EmptyMutableString

```c++
Variant EmptyMutableString()
```  
Get a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing an empty mutable string.

<br />

|                                                                                   Details                                                                                    ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) of type MutableString, containing an empty string. |

### EmptyString

```c++
Variant EmptyString()
```  
Get an empty string variant.

<br />

|                                                                                    Details                                                                                    ||
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) of type StaticString, referring to an empty string. |

### EmptyVector

```c++
Variant EmptyVector()
```  
Get a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing an empty vector.

You can immediately call [vector()](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a24f62801e317339dec02c242d6bd57c2) on it to work with the vector it contains.

<br />

|                                                                              Details                                                                              ||
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) of type Vector, containing no elements. |

### False

```c++
Variant False()
```  
Get a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) of bool value false.

<br />

|                                                                          Details                                                                          ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) of type Bool, with value false. |

### FromBool

```c++
Variant FromBool(
  bool value
)
```  
Return a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) from a boolean.

<br />

|                                                                                                                                                           Details                                                                                                                                                            ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|-------------------------------------------------------------------------------------------------------------------------------------------| | `value` | Boolean value to put into the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant). | |
| **Returns** | A [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing the Boolean.                                                                                                                                                                            |

### FromDouble

```c++
Variant FromDouble(
  double value
)
```  
Return a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) from a double-precision floating point number.

<br />

|                                                                                                                                                                                   Details                                                                                                                                                                                    ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `value` | Double-precision floating point value to put into the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant); | |
| **Returns** | A [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing the double-precision floating point number.                                                                                                                                                                                             |

### FromInt64

```c++
Variant FromInt64(
  int64_t value
)
```  
Return a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) from a 64-bit integer.

<br />

|                                                                                                                                                                  Details                                                                                                                                                                   ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|--------------------------------------------------------------------------------------------------------------------------------------------------| | `value` | 64-bit integer value to put into the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant). | |
| **Returns** | A [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing the 64-bit integer.                                                                                                                                                                                   |

### FromMutableBlob

```c++
Variant FromMutableBlob(
  const void *src_data,
  size_t size_bytes
)
```  
Return a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing a copy of binary data.

<br />

|                                                                                                                                                                                                                                                                     Details                                                                                                                                                                                                                                                                      ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------| | `src_data`   | Pointer to binary data to be copied into the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant). | | `size_bytes` | Size of the data, in bytes.                                                                                                                              | |
| **Returns** | A [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing a copy of the binary data.                                                                                                                                                                                                                                                                                                                                                                                  |

### FromMutableString

```c++
Variant FromMutableString(
  const std::string & value
)
```  
Return a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) from a string.

This method makes a copy of the string.

<br />

|                                                                                                                                                           Details                                                                                                                                                            ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|-------------------------------------------------------------------------------------------------------------------------------------------| | `value` | String value to copy into the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant). | |
| **Returns** | A [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing a copy of the string.                                                                                                                                                                   |

### FromStaticBlob

```c++
Variant FromStaticBlob(
  const void *static_data,
  size_t size_bytes
)
```  
Return a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) that points to static binary data.


| **Note:** If you use this function, you must ensure that the memory pointed to stays valid for the life of the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant), otherwise call mutable_blob() or [set_mutable_blob()](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a0d4d14a8b3fb05978ad7ec499576d4b4), which will copy the data to an internal buffer.

<br />

|                                                                                                                                                                                                                                                                                                                                   Details                                                                                                                                                                                                                                                                                                                                   ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `static_data` | Pointer to statically-allocated binary data. The [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) will point to the data, not copy it. | | `size_bytes`  | Size of the data, in bytes.                                                                                                                                                                      | |
| **Returns** | A [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) pointing to the binary data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

### FromStaticString

```c++
Variant FromStaticString(
  const char *value
)
```  
Return a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) from a static string.


| **Note:** If you use this function, you must ensure that the memory pointed to stays valid for the life of the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant), otherwise call [mutable_string()](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a9251c28af47fcd13757f0d5fd4e4ffc9) or [set_mutable_string()](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant_1a4e1b5e81df10fe31b8cf700bb8bc6653), which will copy the string to an internal buffer.

<br />

|                                                                                 Details                                                                                  ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|---------------------------------------------------------| | `value` | Pointer to statically-allocated null-terminated string. |                 |
| **Returns** | A [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) referring to the string pointer you passed in. |

### MutableStringFromStaticString

```c++
Variant MutableStringFromStaticString(
  const char *value
)
```  
Return a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) from a string, but make it mutable.

Only copies the string once, unlike Variant(std::string(value)), which copies the string twice.

<br />

|                                                                                                                                                                            Details                                                                                                                                                                             ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|------------------------------------------------------------------------------------------------------------------------------------------------------------| | `value` | String value to copy into the [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) and make mutable. | |
| **Returns** | A [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) containing a mutable copy of the string.                                                                                                                                                                                             |

### Null

```c++
Variant Null()
```  
Get a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) of type Null.

<br />

|                                                                 Details                                                                 ||
|-------------|----------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) of type Null. |

### One

```c++
Variant One()
```  
Get a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) of integer value 1.

<br />

|                                                                        Details                                                                         ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) of type Int64, with value 1. |

### OnePointZero

```c++
Variant OnePointZero()
```  
Get a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) of double value 1.0.

<br />

|                                                                          Details                                                                          ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) of type Double, with value 1.0. |

### True

```c++
Variant True()
```  
Get a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) of bool value true.

<br />

|                                                                         Details                                                                          ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) of type Bool, with value true. |

### TypeName

```c++
const char * TypeName(
  Type type
)
```  
Get the human-readable type name of a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) type.

<br />

|                                                                                                                                             Details                                                                                                                                              ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |--------|------------------------------------------------------------------------------------------------------------------------------| | `type` | [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) type to describe. | |
| **Returns** | A string describing the type, suitable for error messages or debugging. For example "Int64" or "MutableString".                                                                                                                                                                     |

### Zero

```c++
Variant Zero()
```  
Get a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) of integer value 0.

<br />

|                                                                        Details                                                                         ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) of type Int64, with value 0. |

### ZeroPointZero

```c++
Variant ZeroPointZero()
```  
Get a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) of double value 0.0.

<br />

|                                                                          Details                                                                          ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) of type Double, with value 0.0. |