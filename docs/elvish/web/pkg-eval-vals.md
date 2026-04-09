### Overview ¶

Package vals contains basic facilities for manipulating values used in the
Elvish runtime.

### Index ¶

- Constants

- Variables

-
        func Assoc(a, k, v interface{}) (interface{}, error)

-
        func Bool(v interface{}) bool

-
        func CanIterate(v interface{}) bool

-
        func CheckDeprecatedIndex(a, k interface{}) string

-
        func Collect(it interface{}) ([]interface{}, error)

-
        func Concat(lhs, rhs interface{}) (interface{}, error)

-
        func Dissoc(a, k interface{}) interface{}

-
        func Eq(r interface{}) tt.Matcher

-
        func Equal(x, y interface{}) bool

-
        func Feed(f func(interface{}) bool, values ...interface{})

-
        func FromGo(a interface{}) interface{}

-
        func HasKey(container, key interface{}) bool

-
        func Hash(v interface{}) uint32

-
        func Index(a, k interface{}) (interface{}, error)

-
        func Iterate(v interface{}, f func(interface{}) bool) error

-
        func IterateKeys(v interface{}, f func(interface{}) bool) error

-
        func Kind(v interface{}) string

-
        func Len(v interface{}) int

-
        func MakeList(vs ...interface{}) vector.Vector

-
        func MakeMap(a ...interface{}) hashmap.Map

-
        func NoSuchKey(k interface{}) error

-
        func Repr(v interface{}, indent int) string

-
        func ScanToGo(src interface{}, ptr interface{}) error

-
        func ToString(v interface{}) string

-
        func TypeOf(i interface{}) reflect.Type

-
        func ValueOf(i interface{}) reflect.Value

-
          type Assocer

-
          type Booler

-
          type Concatter

-
          type Dissocer

-
          type Equaler

-
          type ErrIndexer

-
          type File

-
          type HasKeyer

-
          type Hasher

-
          type Indexer

-
          type Iterator

-
          type KeysIterator

-
          type Kinder

-
          type Lener

-
          type List

-
          type ListIndex

-

-
            func ConvertListIndex(rawIndex interface{}, n int) (*ListIndex, error)

-
          type ListReprBuilder

-

-
            func NewListReprBuilder(indent int) *ListReprBuilder

-

-
            func (b *ListReprBuilder) String() string

-
            func (b *ListReprBuilder) WriteElem(v string)

-
          type Map

-
          type MapReprBuilder

-

-
            func NewMapReprBuilder(indent int) *MapReprBuilder

-

-
            func (b *MapReprBuilder) String() string

-
            func (b *MapReprBuilder) WritePair(k string, indent int, v string)

-
          type Pipe

-

-
            func NewPipe(r, w *os.File) Pipe

-

-
            func (p Pipe) Equal(rhs interface{}) bool

-
            func (p Pipe) Hash() uint32

-
            func (Pipe) Kind() string

-
            func (p Pipe) Repr(int) string

-
          type PseudoStructMap

-
          type RConcatter

-
          type Reprer

-
          type Scanner

-
          type Stringer

-
          type StructMap

-
          type ValueTester

-

-
            func TestValue(t *testing.T, v interface{}) ValueTester

-

-
            func (vt ValueTester) AllKeys(wantKeys ...interface{}) ValueTester

-
            func (vt ValueTester) Assoc(key, val, wantNew interface{}) ValueTester

-
            func (vt ValueTester) AssocError(key, val interface{}, wantErr error) ValueTester

-
            func (vt ValueTester) Bool(wantBool bool) ValueTester

-
            func (vt ValueTester) Equal(others ...interface{}) ValueTester

-
            func (vt ValueTester) HasKey(keys ...interface{}) ValueTester

-
            func (vt ValueTester) HasNoKey(keys ...interface{}) ValueTester

-
            func (vt ValueTester) Hash(wantHash uint32) ValueTester

-
            func (vt ValueTester) Index(key, wantVal interface{}) ValueTester

-
            func (vt ValueTester) IndexError(key interface{}, wantErr error) ValueTester

-
            func (vt ValueTester) Kind(wantKind string) ValueTester

-
            func (vt ValueTester) Len(wantLen int) ValueTester

-
            func (vt ValueTester) NotEqual(others ...interface{}) ValueTester

-
            func (vt ValueTester) Repr(wantRepr string) ValueTester

### Constants ¶

      View Source
      

```
const NoPretty = math.MinInt32
```

NoPretty can be passed to Repr to suppress pretty-printing.

### Variables ¶

      View Source
      

```
var EmptyList = vector.Empty
```

EmptyList is an empty list.

      View Source
      

```
var EmptyMap = hashmap.New(Equal, Hash)
```

EmptyMap is an empty map.

      View Source
      

```
var ErrConcatNotImplemented = errors.New("concat not implemented")
```

ErrConcatNotImplemented is a special error value used to signal that
concatenation is not implemented. See Concat for how it is used.

### Functions ¶

####

      func Assoc ¶
  
    
  

    
    
      

```
func Assoc(a, k, v interface{}) (interface{}, error)
```

Assoc takes a container, a key and value, and returns a modified version of
the container, in which the key associated with the value. It is implemented
for the builtin type string, List and Map types, StructMap types, and types
satisfying the Assocer interface. For other types, it returns an error.

####

      func Bool ¶
  
    
  

    
    
      

```
func Bool(v interface{}) bool
```

Bool converts a value to bool. It is implemented for nil, the builtin bool
type, and types implementing the Booler interface. For all other values, it
returns true.

####

      func CanIterate ¶
  
    
  

    
    
      

```
func CanIterate(v interface{}) bool
```

CanIterate returns whether the value can be iterated. If CanIterate(v) is
true, calling Iterate(v, f) will not result in an error.

####

      func CheckDeprecatedIndex ¶
  
    
      added in
      v0.15.0
    
  

    
    
      

```
func CheckDeprecatedIndex(a, k interface{}) string
```

CheckDeprecatedIndex checks if the given indexing operation is using any
deprecated syntax, and returns a non-empty message if it is.

####

      func Collect ¶
  
    
  

    
    
      

```
func Collect(it interface{}) ([]interface{}, error)
```

Collect collects all elements of an iterable value into a slice.

####

      func Concat ¶
  
    
  

    
    
      

```
func Concat(lhs, rhs interface{}) (interface{}, error)
```

Concat concatenates two values. If both operands are strings, it returns lhs
- rhs, nil. If the left operand implements Concatter, it calls
lhs.Concat(rhs). If lhs doesn't implement the interface or returned
ErrConcatNotImplemented, it then calls rhs.RConcat(lhs). If all attempts
fail, it returns nil and an error.

####

      func Dissoc ¶
  
    
  

    
    
      

```
func Dissoc(a, k interface{}) interface{}
```

Dissoc takes a container and a key, and returns a modified version of the
container, with the given key dissociated with any value. It is implemented
for the Map type and types satisfying the Dissocer interface. For other
types, it returns nil.

####

      func Eq ¶
  
    
      added in
      v0.14.0
    
  

    
    
      

```
func Eq(r interface{}) tt.Matcher
```

Eq returns a tt.Matcher that matches using the Equal function.

####

      func Equal ¶
  
    
  

    
    
      

```
func Equal(x, y interface{}) bool
```

Equal returns whether two values are equal. It is implemented for the builtin
types bool and string, the File, List, Map types, StructMap types, and types
satisfying the Equaler interface. For other types, it uses reflect.DeepEqual
to compare the two values.

####

      func Feed ¶
  
    
      added in
      v0.15.0
    
  

    
    
      

```
func Feed(f func(interface{}) bool, values ...interface{})
```

Feed calls the function with given values, breaking earlier if the function
returns false.

####

      func FromGo ¶
  
    
  

    
    
      

```
func FromGo(a interface{}) interface{}
```

FromGo converts a Go value to an Elvish value. Conversion happens when the
argument is int, float64 or rune (this is consistent with ScanToGo). In other
cases, this function just returns the argument.

####

      func HasKey ¶
  
    
  

    
    
      

```
func HasKey(container, key interface{}) bool
```

HasKey returns whether a container has a key. It is implemented for the Map
type, StructMap types, and types satisfying the HasKeyer interface. It falls
back to iterating keys using IterateKeys, and if that fails, it falls back to
calling Len and checking if key is a valid numeric or slice index. Otherwise
it returns false.

####

      func Hash ¶
  
    
  

    
    
      

```
func Hash(v interface{}) uint32
```

Hash returns the 32-bit hash of a value. It is implemented for the builtin
types bool and string, the File, List, Map types, StructMap types, and types
satisfying the Hasher interface. For other values, it returns 0 (which is OK
in terms of correctness).

####

      func Index ¶
  
    
  

    
    
      

```
func Index(a, k interface{}) (interface{}, error)
```

Index indexes a value with the given key. It is implemented for the builtin
type string, the List type, StructMap types, and types satisfying the
ErrIndexer or Indexer interface (the Map type satisfies Indexer). For other
types, it returns a nil value and a non-nil error.

####

      func Iterate ¶
  
    
  

    
    
      

```
func Iterate(v interface{}, f func(interface{}) bool) error
```

Iterate iterates the supplied value, and calls the supplied function in each
of its elements. The function can return false to break the iteration. It is
implemented for the builtin type string, the List type, and types satisfying
the Iterator interface. For these types, it always returns a nil error. For
other types, it doesn't do anything and returns an error.

####

      func IterateKeys ¶
  
    
  

    
    
      

```
func IterateKeys(v interface{}, f func(interface{}) bool) error
```

IterateKeys iterates the keys of the supplied value, calling the supplied
function for each key. The function can return false to break the iteration.
It is implemented for the Map type, StructMap types, and types satisfying the
IterateKeyser interface. For these types, it always returns a nil error. For
other types, it doesn't do anything and returns an error.

####

      func Kind ¶
  
    
  

    
    
      

```
func Kind(v interface{}) string
```

Kind returns the "kind" of the value, a concept similar to type but not yet
very well defined. It is implemented for the builtin nil, bool and string,
the File, List, Map types, StructMap types, and types satisfying the Kinder
interface. For other types, it returns the Go type name of the argument
preceded by "!!".

TODO: Decide what `kind-of` should report for an external command object
and document the rationale for the choice in the doc string for `func
(ExternalCmd) Kind()` as well as user facing documentation. It's not
obvious why this returns "fn" rather than "external" for that case.

####

      func Len ¶
  
    
  

    
    
      

```
func Len(v interface{}) int
```

Len returns the length of the value, or -1 if the value does not have a
well-defined length. It is implemented for the builtin type string, StructMap
types, and types satisfying the Lener interface. For other types, it returns
-1.

####

      func MakeList ¶
  
    
  

    
    
      

```
func MakeList(vs ...interface{}) vector.Vector
```

MakeList creates a new List from values.

####

      func MakeMap ¶
  
    
  

    
    
      

```
func MakeMap(a ...interface{}) hashmap.Map
```

MakeMap creates a map from arguments that are alternately keys and values. It
panics if the number of arguments is odd.

####

      func NoSuchKey ¶
  
    
  

    
    
      

```
func NoSuchKey(k interface{}) error
```

NoSuchKey returns an error indicating that a key is not found in a map-like
value.

####

      func Repr ¶
  
    
  

    
    
      

```
func Repr(v interface{}, indent int) string
```

Repr returns the representation for a value, a string that is preferably (but
not necessarily) an Elvish expression that evaluates to the argument. If
indent >= 0, the representation is pretty-printed. It is implemented for the
builtin types nil, bool and string, the File, List and Map types, StructMap
types, and types satisfying the Reprer interface. For other types, it uses
fmt.Sprint with the format "<unknown %v>".

####

      func ScanToGo ¶
  
    
  

    
    
      

```
func ScanToGo(src interface{}, ptr interface{}) error
```

ScanToGo converts an Elvish value to a Go value. the pointer points to. It
uses the type of the pointer to determine the destination type, and puts the
converted value in the location the pointer points to. Conversion only
happens when the destination type is int, float64 or rune; in other cases,
this function just checks that the source value is already assignable to the
destination.

####

      func ToString ¶
  
    
  

    
    
      

```
func ToString(v interface{}) string
```

ToString converts a Value to string. It is implemented for the builtin
float64 and string types, and type satisfying the Stringer interface. It
falls back to Repr(v, NoPretty).

####

      func TypeOf ¶
  
    
  

    
    
      

```
func TypeOf(i interface{}) reflect.Type
```

TypeOf is like reflect.TypeOf, except that when given an argument of nil, it
does not return nil, but the Type for the empty interface.

####

      func ValueOf ¶
  
    
  

    
    
      

```
func ValueOf(i interface{}) reflect.Value
```

ValueOf is like reflect.ValueOf, except that when given an argument of nil,
it does not return a zero Value, but the Value for the zero value of the
empty interface.

### Types ¶

####

      type Assocer ¶
  
    
  

    
    
      

```
type Assocer interface {
 // Assoc returns a slightly modified version of the receiver with key k
 // associated with value v.
 Assoc(k, v interface{}) (interface{}, error)
}
```

Assocer wraps the Assoc method.

####

      type Booler ¶
  
    
  

    
    
      

```
type Booler interface {
 // Bool computes the truth value of the receiver.
 Bool() bool
}
```

Booler wraps the Bool method.

####

      type Concatter ¶
  
    
  

    
    
      

```
type Concatter interface {
 // Concat concatenates the receiver with another value, the receiver being
 // the left operand. If concatenation is not supported for the given value,
 // the method can return the special error type ErrCatNotImplemented.
 Concat(v interface{}) (interface{}, error)
}
```

Concatter wraps the Concat method. See Concat for how it is used.

####

      type Dissocer ¶
  
    
  

    
    
      

```
type Dissocer interface {
 // Dissoc returns a slightly modified version of the receiver with key k
 // dissociated with any value.
 Dissoc(k interface{}) interface{}
}
```

Dissocer wraps the Dissoc method.

####

      type Equaler ¶
  
    
  

    
    
      

```
type Equaler interface {
 // Equal compares the receiver to another value. Two equal values must have
 // the same hash code.
 Equal(other interface{}) bool
}
```

Equaler wraps the Equal method.

####

      type ErrIndexer ¶
  
    
  

    
    
      

```
type ErrIndexer interface {
 // Index retrieves one value from the receiver at the specified index.
 Index(k interface{}) (interface{}, error)
}
```

ErrIndexer wraps the Index method.

####

      type File ¶
  
    
  

    
    
      

```
type File = *os.File
```

File is an alias for *os.File.

####

      type HasKeyer ¶
  
    
  

    
    
      

```
type HasKeyer interface {
 // HasKey returns whether the receiver has the given argument as a valid
 // key.
 HasKey(interface{}) bool
}
```

HasKeyer wraps the HasKey method.

####

      type Hasher ¶
  
    
  

    
    
      

```
type Hasher interface {
 // Hash computes the hash code of the receiver.
 Hash() uint32
}
```

Hasher wraps the Hash method.

####

      type Indexer ¶
  
    
  

    
    
      

```
type Indexer interface {
 // Index retrieves the value corresponding to the specified key in the
 // container. It returns the value (if any), and whether it actually exists.
 Index(k interface{}) (v interface{}, ok bool)
}
```

Indexer wraps the Index method.

####

      type Iterator ¶
  
    
  

    
    
      

```
type Iterator interface {
 // Iterate calls the passed function with each value within the receiver.
 // The iteration is aborted if the function returns false.
 Iterate(func(v interface{}) bool)
}
```

Iterator wraps the Iterate method.

####

      type KeysIterator ¶
  
    
  

    
    
      

```
type KeysIterator interface {
 // IterateKeys calls the passed function with each key within the receiver.
 // The iteration is aborted if the function returns false.
 IterateKeys(func(v interface{}) bool)
}
```

KeysIterator wraps the IterateKeys method.

####

      type Kinder ¶
  
    
  

    
    
      

```
type Kinder interface {
 Kind() string
}
```

Kinder wraps the Kind method.

####

      type Lener ¶
  
    
  

    
    
      

```
type Lener interface {
 // Len computes the length of the receiver.
 Len() int
}
```

Lener wraps the Len method.

####

      type List ¶
  
    
  

    
    
      

```
type List = vector.Vector
```

List is an alias for the underlying type used for lists in Elvish.

####

      type ListIndex ¶
  
    
  

    
    
      

```
type ListIndex struct {
 Slice bool
 Lower int
 Upper int
}
```

ListIndex represents a (converted) list index.

####

      func ConvertListIndex ¶
  
    
  

    
    
      

```
func ConvertListIndex(rawIndex interface{}, n int) (*ListIndex, error)
```

ConvertListIndex parses a list index, check whether it is valid, and returns
the converted structure.
