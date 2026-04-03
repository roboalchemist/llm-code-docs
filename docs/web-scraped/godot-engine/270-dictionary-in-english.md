# Dictionary in English

# Dictionary
A built-in data structure that holds key-value pairs.

## Description
Dictionaries are associative containers that contain values referenced by unique keys. Dictionaries will preserve the insertion order when adding new entries. In other programming languages, this data structure is often referred to as a hash map or an associative array.
You can define a dictionary by placing a comma-separated list ofkey:valuepairs inside curly braces{}.
Creating a dictionary:
```
var my_dict = {} # Creates an empty dictionary.

var dict_variable_key = "Another key name"
var dict_variable_value = "value2"
var another_dict = {
    "Some key name": "value1",
    dict_variable_key: dict_variable_value,
}

var points_dict = { "White": 50, "Yellow": 75, "Orange": 100 }

# Alternative Lua-style syntax.
# Doesn't require quotes around keys, but only string constants can be used as key names.
# Additionally, key names must start with a letter or an underscore.
# Here, `some_key` is a string literal, not a variable!
another_dict = {
    some_key = 42,
}
```
```
var myDict = new Godot.Collections.Dictionary(); // Creates an empty dictionary.
var pointsDict = new Godot.Collections.Dictionary
{
    { "White", 50 },
    { "Yellow", 75 },
    { "Orange", 100 },
};
```
You can access a dictionary's value by referencing its corresponding key. In the above example,points_dict["White"]will return50. You can also writepoints_dict.White, which is equivalent. However, you'll have to use the bracket syntax if the key you're accessing the dictionary with isn't a fixed string (such as a number or variable).
```
@export_enum("White", "Yellow", "Orange") var my_color: String
var points_dict = { "White": 50, "Yellow": 75, "Orange": 100 }
func _ready():
    # We can't use dot syntax here as `my_color` is a variable.
    var points = points_dict[my_color]
```
```
[Export(PropertyHint.Enum, "White,Yellow,Orange")]
public string MyColor { get; set; }
private Godot.Collections.Dictionary _pointsDict = new Godot.Collections.Dictionary
{
    { "White", 50 },
    { "Yellow", 75 },
    { "Orange", 100 },
};

public override void _Ready()
{
    int points = (int)_pointsDict[MyColor];
}
```
In the above code,pointswill be assigned the value that is paired with the appropriate color selected inmy_color.
Dictionaries can contain more complex data:
```
var my_dict = {
    "First Array": [1, 2, 3, 4] # Assigns an Array to a String key.
}
```
```
var myDict = new Godot.Collections.Dictionary
{
    { "First Array", new Godot.Collections.Array { 1, 2, 3, 4 } }
};
```
To add a key to an existing dictionary, access it like an existing key and assign to it:
```
var points_dict = { "White": 50, "Yellow": 75, "Orange": 100 }
points_dict["Blue"] = 150 # Add "Blue" as a key and assign 150 as its value.
```
```
var pointsDict = new Godot.Collections.Dictionary
{
    { "White", 50 },
    { "Yellow", 75 },
    { "Orange", 100 },
};
pointsDict["Blue"] = 150; // Add "Blue" as a key and assign 150 as its value.
```
Finally, untyped dictionaries can contain different types of keys and values in the same dictionary:
```
# This is a valid dictionary.
# To access the string "Nested value" below, use `my_dict.sub_dict.sub_key` or `my_dict["sub_dict"]["sub_key"]`.
# Indexing styles can be mixed and matched depending on your needs.
var my_dict = {
    "String Key": 5,
    4: [1, 2, 3],
    7: "Hello",
    "sub_dict": { "sub_key": "Nested value" },
}
```
```
// This is a valid dictionary.
// To access the string "Nested value" below, use `((Godot.Collections.Dictionary)myDict["sub_dict"])["sub_key"]`.
var myDict = new Godot.Collections.Dictionary {
    { "String Key", 5 },
    { 4, new Godot.Collections.Array { 1, 2, 3 } },
    { 7, "Hello" },
    { "sub_dict", new Godot.Collections.Dictionary { { "sub_key", "Nested value" } } },
};
```
The keys of a dictionary can be iterated with theforkeyword:
```
var groceries = { "Orange": 20, "Apple": 2, "Banana": 4 }
for fruit in groceries:
    var amount = groceries[fruit]
```
```
var groceries = new Godot.Collections.Dictionary { { "Orange", 20 }, { "Apple", 2 }, { "Banana", 4 } };
foreach (var (fruit, amount) in groceries)
{
    // `fruit` is the key, `amount` is the value.
}
```
To enforce a certain type for keys and values, you can create atyped dictionary. Typed dictionaries can only contain keys and values of the given types, or that inherit from the given classes:
```
# Creates a typed dictionary with String keys and int values.
# Attempting to use any other type for keys or values will result in an error.
var typed_dict: Dictionary[String, int] = {
    "some_key": 1,
    "some_other_key": 2,
}

# Creates a typed dictionary with String keys and values of any type.
# Attempting to use any other type for keys will result in an error.
var typed_dict_key_only: Dictionary[String, Variant] = {
    "some_key": 12.34,
    "some_other_key": "string",
}
```
```
// Creates a typed dictionary with String keys and int values.
// Attempting to use any other type for keys or values will result in an error.
var typedDict = new Godot.Collections.Dictionary<String, int> {
    {"some_key", 1},
    {"some_other_key", 2},
};

// Creates a typed dictionary with String keys and values of any type.
// Attempting to use any other type for keys will result in an error.
var typedDictKeyOnly = new Godot.Collections.Dictionary<String, Variant> {
    {"some_key", 12.34},
    {"some_other_key", "string"},
};
```
Note:Dictionaries are always passed by reference. To get a copy of a dictionary which can be modified independently of the original dictionary, useduplicate().
Note:Erasing elements while iterating over dictionaries isnotsupported and will result in unpredictable behavior.
Note
There are notable differences when using this API with C#. SeeC# API differences to GDScriptfor more information.

## Tutorials
- GDScript basics: Dictionary
GDScript basics: Dictionary
- 3D Voxel Demo
3D Voxel Demo
- Operating System Testing Demo
Operating System Testing Demo

## Constructors

| Dictionary | Dictionary() |
|---|---|
| Dictionary | Dictionary(base:Dictionary, key_type:int, key_class_name:StringName, key_script:Variant, value_type:int, value_class_name:StringName, value_script:Variant) |
| Dictionary | Dictionary(from:Dictionary) |

Dictionary
Dictionary()
Dictionary
Dictionary(base:Dictionary, key_type:int, key_class_name:StringName, key_script:Variant, value_type:int, value_class_name:StringName, value_script:Variant)
Dictionary
Dictionary(from:Dictionary)

## Methods

| void | assign(dictionary:Dictionary) |
|---|---|
| void | clear() |
| Dictionary | duplicate(deep:bool= false)const |
| Dictionary | duplicate_deep(deep_subresources_mode:int= 1)const |
| bool | erase(key:Variant) |
| Variant | find_key(value:Variant)const |
| Variant | get(key:Variant, default:Variant= null)const |
| Variant | get_or_add(key:Variant, default:Variant= null) |
| int | get_typed_key_builtin()const |
| StringName | get_typed_key_class_name()const |
| Variant | get_typed_key_script()const |
| int | get_typed_value_builtin()const |
| StringName | get_typed_value_class_name()const |
| Variant | get_typed_value_script()const |
| bool | has(key:Variant)const |
| bool | has_all(keys:Array)const |
| int | hash()const |
| bool | is_empty()const |
| bool | is_read_only()const |
| bool | is_same_typed(dictionary:Dictionary)const |
| bool | is_same_typed_key(dictionary:Dictionary)const |
| bool | is_same_typed_value(dictionary:Dictionary)const |
| bool | is_typed()const |
| bool | is_typed_key()const |
| bool | is_typed_value()const |
| Array | keys()const |
| void | make_read_only() |
| void | merge(dictionary:Dictionary, overwrite:bool= false) |
| Dictionary | merged(dictionary:Dictionary, overwrite:bool= false)const |
| bool | recursive_equal(dictionary:Dictionary, recursion_count:int)const |
| bool | set(key:Variant, value:Variant) |
| int | size()const |
| void | sort() |
| Array | values()const |

void
assign(dictionary:Dictionary)
void
clear()
Dictionary
duplicate(deep:bool= false)const
Dictionary
duplicate_deep(deep_subresources_mode:int= 1)const
bool
erase(key:Variant)
Variant
find_key(value:Variant)const
Variant
get(key:Variant, default:Variant= null)const
Variant
get_or_add(key:Variant, default:Variant= null)
get_typed_key_builtin()const
StringName
get_typed_key_class_name()const
Variant
get_typed_key_script()const
get_typed_value_builtin()const
StringName
get_typed_value_class_name()const
Variant
get_typed_value_script()const
bool
has(key:Variant)const
bool
has_all(keys:Array)const
hash()const
bool
is_empty()const
bool
is_read_only()const
bool
is_same_typed(dictionary:Dictionary)const
bool
is_same_typed_key(dictionary:Dictionary)const
bool
is_same_typed_value(dictionary:Dictionary)const
bool
is_typed()const
bool
is_typed_key()const
bool
is_typed_value()const
Array
keys()const
void
make_read_only()
void
merge(dictionary:Dictionary, overwrite:bool= false)
Dictionary
merged(dictionary:Dictionary, overwrite:bool= false)const
bool
recursive_equal(dictionary:Dictionary, recursion_count:int)const
bool
set(key:Variant, value:Variant)
size()const
void
sort()
Array
values()const

## Operators

| bool | operator !=(right:Dictionary) |
|---|---|
| bool | operator ==(right:Dictionary) |
| Variant | operator [](key:Variant) |

bool
operator !=(right:Dictionary)
bool
operator ==(right:Dictionary)
Variant
operator [](key:Variant)

## Constructor Descriptions
DictionaryDictionary()🔗
Constructs an emptyDictionary.
DictionaryDictionary(base:Dictionary, key_type:int, key_class_name:StringName, key_script:Variant, value_type:int, value_class_name:StringName, value_script:Variant)
Creates a typed dictionary from thebasedictionary. A typed dictionary can only contain keys and values of the given types, or that inherit from the given classes, as described by this constructor's parameters.
DictionaryDictionary(from:Dictionary)
Returns the same dictionary asfrom. If you need a copy of the dictionary, useduplicate().

## Method Descriptions
voidassign(dictionary:Dictionary)🔗
Assigns elements of anotherdictionaryinto the dictionary. Resizes the dictionary to matchdictionary. Performs type conversions if the dictionary is typed.
voidclear()🔗
Clears the dictionary, removing all entries from it.
Dictionaryduplicate(deep:bool= false)const🔗
Returns a new copy of the dictionary.
By default, ashallowcopy is returned: all nestedArray,Dictionary, andResourcekeys and values are shared with the original dictionary. Modifying any of those in one dictionary will also affect them in the other.
Ifdeepistrue, adeepcopy is returned: all nested arrays and dictionaries are also duplicated (recursively). AnyResourceis still shared with the original dictionary, though.
Dictionaryduplicate_deep(deep_subresources_mode:int= 1)const🔗
Duplicates this dictionary, deeply, likeduplicate()when passingtrue, with extra control over how subresources are handled.
deep_subresources_modemust be one of the values fromDeepDuplicateMode. By default, only internal resources will be duplicated (recursively).
boolerase(key:Variant)🔗
Removes the dictionary entry by key, if it exists. Returnstrueif the givenkeyexisted in the dictionary, otherwisefalse.
Note:Do not erase entries while iterating over the dictionary. You can iterate over thekeys()array instead.
Variantfind_key(value:Variant)const🔗
Finds and returns the first key whose associated value is equal tovalue, ornullif it is not found.
Note:nullis also a valid key. If inside the dictionary,find_key()may give misleading results.
Variantget(key:Variant, default:Variant= null)const🔗
Returns the corresponding value for the givenkeyin the dictionary. If thekeydoes not exist, returnsdefault, ornullif the parameter is omitted.
Variantget_or_add(key:Variant, default:Variant= null)🔗
Gets a value and ensures the key is set. If thekeyexists in the dictionary, this behaves likeget(). Otherwise, thedefaultvalue is inserted into the dictionary and returned.
intget_typed_key_builtin()const🔗
Returns the built-inVarianttype of the typed dictionary's keys as aVariant.Typeconstant. If the keys are not typed, returns@GlobalScope.TYPE_NIL. See alsois_typed_key().
StringNameget_typed_key_class_name()const🔗
Returns thebuilt-inclass name of the typed dictionary's keys, if the built-inVarianttype is@GlobalScope.TYPE_OBJECT. Otherwise, returns an emptyStringName. See alsois_typed_key()andObject.get_class().
Variantget_typed_key_script()const🔗
Returns theScriptinstance associated with this typed dictionary's keys, ornullif it does not exist. See alsois_typed_key().
intget_typed_value_builtin()const🔗
Returns the built-inVarianttype of the typed dictionary's values as aVariant.Typeconstant. If the values are not typed, returns@GlobalScope.TYPE_NIL. See alsois_typed_value().
StringNameget_typed_value_class_name()const🔗
Returns thebuilt-inclass name of the typed dictionary's values, if the built-inVarianttype is@GlobalScope.TYPE_OBJECT. Otherwise, returns an emptyStringName. See alsois_typed_value()andObject.get_class().
Variantget_typed_value_script()const🔗
Returns theScriptinstance associated with this typed dictionary's values, ornullif it does not exist. See alsois_typed_value().
boolhas(key:Variant)const🔗
Returnstrueif the dictionary contains an entry with the givenkey.
```
var my_dict = {
    "Godot" : 4,
    210 : null,
}

print(my_dict.has("Godot")) # Prints true
print(my_dict.has(210))     # Prints true
print(my_dict.has(4))       # Prints false
```
```
var myDict = new Godot.Collections.Dictionary
{
    { "Godot", 4 },
    { 210, default },
};

GD.Print(myDict.ContainsKey("Godot")); // Prints True
GD.Print(myDict.ContainsKey(210));     // Prints True
GD.Print(myDict.ContainsKey(4));       // Prints False
```
In GDScript, this is equivalent to theinoperator:
```
if "Godot" in { "Godot": 4 }:
    print("The key is here!") # Will be printed.
```
Note:This method returnstrueas long as thekeyexists, even if its corresponding value isnull.
boolhas_all(keys:Array)const🔗
Returnstrueif the dictionary contains all keys in the givenkeysarray.
```
var data = { "width": 10, "height": 20 }
data.has_all(["height", "width"]) # Returns true
```
inthash()const🔗
Returns a hashed 32-bit integer value representing the dictionary contents.
```
var dict1 = { "A": 10, "B": 2 }
var dict2 = { "A": 10, "B": 2 }

print(dict1.hash() == dict2.hash()) # Prints true
```
```
var dict1 = new Godot.Collections.Dictionary { { "A", 10 }, { "B", 2 } };
var dict2 = new Godot.Collections.Dictionary { { "A", 10 }, { "B", 2 } };

// Godot.Collections.Dictionary has no Hash() method. Use GD.Hash() instead.
GD.Print(GD.Hash(dict1) == GD.Hash(dict2)); // Prints True
```
Note:Dictionaries with the same entries but in a different order will not have the same hash.
Note:Dictionaries with equal hash values arenotguaranteed to be the same, because of hash collisions. On the contrary, dictionaries with different hash values are guaranteed to be different.
boolis_empty()const🔗
Returnstrueif the dictionary is empty (its size is0). See alsosize().
boolis_read_only()const🔗
Returnstrueif the dictionary is read-only. Seemake_read_only(). Dictionaries are automatically read-only if declared withconstkeyword.
boolis_same_typed(dictionary:Dictionary)const🔗
Returnstrueif the dictionary is typed the same asdictionary.
boolis_same_typed_key(dictionary:Dictionary)const🔗
Returnstrueif the dictionary's keys are typed the same asdictionary's keys.
boolis_same_typed_value(dictionary:Dictionary)const🔗
Returnstrueif the dictionary's values are typed the same asdictionary's values.
boolis_typed()const🔗
Returnstrueif the dictionary is typed. Typed dictionaries can only store keys/values of their associated type and provide type safety for the[]operator. Methods of typed dictionary still returnVariant.
boolis_typed_key()const🔗
Returnstrueif the dictionary's keys are typed.
boolis_typed_value()const🔗
Returnstrueif the dictionary's values are typed.
Arraykeys()const🔗
Returns the list of keys in the dictionary.
voidmake_read_only()🔗
Makes the dictionary read-only, i.e. disables modification of the dictionary's contents. Does not apply to nested content, e.g. content of nested dictionaries.
voidmerge(dictionary:Dictionary, overwrite:bool= false)🔗
Adds entries fromdictionaryto this dictionary. By default, duplicate keys are not copied over, unlessoverwriteistrue.
```
var dict = { "item": "sword", "quantity": 2 }
var other_dict = { "quantity": 15, "color": "silver" }

# Overwriting of existing keys is disabled by default.
dict.merge(other_dict)
print(dict)  # { "item": "sword", "quantity": 2, "color": "silver" }

# With overwriting of existing keys enabled.
dict.merge(other_dict, true)
print(dict)  # { "item": "sword", "quantity": 15, "color": "silver" }
```
```
var dict = new Godot.Collections.Dictionary
{
    ["item"] = "sword",
    ["quantity"] = 2,
};

var otherDict = new Godot.Collections.Dictionary
{
    ["quantity"] = 15,
    ["color"] = "silver",
};

// Overwriting of existing keys is disabled by default.
dict.Merge(otherDict);
GD.Print(dict); // { "item": "sword", "quantity": 2, "color": "silver" }

// With overwriting of existing keys enabled.
dict.Merge(otherDict, true);
GD.Print(dict); // { "item": "sword", "quantity": 15, "color": "silver" }
```
Note:merge()isnotrecursive. Nested dictionaries are considered as keys that can be overwritten or not depending on the value ofoverwrite, but they will never be merged together.
Dictionarymerged(dictionary:Dictionary, overwrite:bool= false)const🔗
Returns a copy of this dictionary merged with the otherdictionary. By default, duplicate keys are not copied over, unlessoverwriteistrue. See alsomerge().
This method is useful for quickly making dictionaries with default values:
```
var base = { "fruit": "apple", "vegetable": "potato" }
var extra = { "fruit": "orange", "dressing": "vinegar" }
# Prints { "fruit": "orange", "vegetable": "potato", "dressing": "vinegar" }
print(extra.merged(base))
# Prints { "fruit": "apple", "vegetable": "potato", "dressing": "vinegar" }
print(extra.merged(base, true))
```
boolrecursive_equal(dictionary:Dictionary, recursion_count:int)const🔗
Returnstrueif the two dictionaries contain the same keys and values, innerDictionaryandArraykeys and values are compared recursively.
boolset(key:Variant, value:Variant)🔗
Sets the value of the element at the givenkeyto the givenvalue. Returnstrueif the value is set successfully. Fails and returnsfalseif the dictionary is read-only, or ifkeyandvaluedon't match the dictionary's types. This is the same as using the[]operator (dict[key]=value).
intsize()const🔗
Returns the number of entries in the dictionary. Empty dictionaries ({}) always return0. See alsois_empty().
voidsort()🔗
Sorts the dictionary in ascending order, by key. The final order is dependent on the "less than" (<) comparison between keys.
```
var numbers = { "c": 2, "a": 0, "b": 1 }
numbers.sort()
print(numbers) # Prints { "a": 0, "b": 1, "c": 2 }
```
This method ensures that the dictionary's entries are ordered consistently whenkeys()orvalues()are called, or when the dictionary needs to be converted to a string through@GlobalScope.str()orJSON.stringify().
Arrayvalues()const🔗
Returns the list of values in this dictionary.

## Operator Descriptions
booloperator !=(right:Dictionary)🔗
Returnstrueif the two dictionaries do not contain the same keys and values.
booloperator ==(right:Dictionary)🔗
Returnstrueif the two dictionaries contain the same keys and values. The order of the entries does not matter.
Note:In C#, by convention, this operator compares byreference. If you need to compare by value, iterate over both dictionaries.
Variantoperator [](key:Variant)🔗
Returns the corresponding value for the givenkeyin the dictionary. If the entry does not exist, fails and returnsnull. For safe access, useget()orhas().

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.