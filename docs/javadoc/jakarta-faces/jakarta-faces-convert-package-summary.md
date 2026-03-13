# Package jakarta.faces.convert

---

package jakarta.faces.convert

-

Related Packages

Package
Description
jakarta.faces

-

Class
Description
BigDecimalConverter

 `Converter` implementation for `java.math.BigDecimal` values.

BigIntegerConverter

 `Converter` implementation for `java.math.BigInteger` values.

BooleanConverter

 `Converter` implementation for `java.lang.Boolean` (and boolean primitive) values.

ByteConverter

 `Converter` implementation for `java.lang.Byte` (and byte primitive) values.

CharacterConverter

 `Converter` implementation for `java.lang.Character` (and char primitive) values.

Converter<T>

 **Converter** is an interface
 describing a Java class that can perform Object-to-String and String-to-Object conversions between model data objects
 and a String representation of those objects that is suitable for rendering.

ConverterException

 **ConverterException** is an exception thrown by the `getAsObject()` or
 `getAsText()` method of a `Converter`, to indicate that the requested conversion cannot be
 performed.

DateTimeConverter

 `Converter` implementation for
 `java.util.Date` values.

DoubleConverter

 `Converter` implementation for `java.lang.Double` (and double primitive) values.

EnumConverter

 `Converter` implementation for
 `java.lang.Enum` (and enum primitive) values.

FacesConverter

 The presence of this annotation on a class automatically registers the
 class with the runtime as a `Converter`.

FacesConverter.Literal

 Supports inline instantiation of the `FacesConverter` qualifier.

FloatConverter

 `Converter` implementation for `java.lang.Float` (and float primitive) values.

IntegerConverter

 `Converter` implementation for `java.lang.Integer` (and int primitive) values.

LongConverter

 `Converter` implementation for `java.lang.Long` (and long primitive) values.

NumberConverter

 `Converter` implementation for `java.lang.Number`
 values.

ShortConverter

 `Converter` implementation for `java.lang.Short` (and short primitive) values.

UUIDConverter

 `Converter` implementation for `java.util.UUID` values.
