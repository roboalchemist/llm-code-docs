Package org.apache.commons.validator.routines

# Class DomainValidator

java.lang.Object
org.apache.commons.validator.routines.DomainValidator

All Implemented Interfaces:
`Serializable`

---

public class DomainValidator
extends Object
implements Serializable

**Domain name** validation routines.

 

 This validator provides methods for validating Internet domain names
 and top-level domains.
 

 

Domain names are evaluated according
 to the standards RFC1034,
 section 3, and RFC1123,
 section 2.1. No accommodation is provided for the specialized needs of
 other applications; if the domain name has been URL-encoded, for example,
 validation will fail even though the equivalent plaintext version of the
 same name would have passed.
 

 

 Validation is also provided for top-level domains (TLDs) as defined and
 maintained by the Internet Assigned Numbers Authority (IANA):
 

   

     
- `isValidInfrastructureTld(java.lang.String)` - validates infrastructure TLDs
         (`.arpa`, etc.)
     
- `isValidGenericTld(java.lang.String)` - validates generic TLDs
         (`.com, .org`, etc.)
     
- `isValidCountryCodeTld(java.lang.String)` - validates country code TLDs
         (`.us, .uk, .cn`, etc.)
   

 

 (**NOTE**: This class does not provide IP address lookup for domain names or
 methods to ensure that a given domain name matches a specific IP; see
 `InetAddress` for that functionality.)
 

Since:
1.4
See Also:

- Serialized Form

- 

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static enum `
`DomainValidator.ArrayType`

Enum used by `updateTLDOverride(ArrayType, String[])`
 to determine which override array to update / fetch

`static class `
`DomainValidator.Item`

Specifies overrides when creating a new class.

- 

## Method Summary

Modifier and Type
Method
Description
`static DomainValidator`
`getInstance()`

Gets the singleton instance of this validator.

`static DomainValidator`
`getInstance(boolean allowLocal)`

Gets the singleton instance of this validator, with local validation as required.

`static DomainValidator`
`getInstance(boolean allowLocal,
 List<DomainValidator.Item> items)`

Gets a new instance of this validator.

`String[]`
`getOverrides(DomainValidator.ArrayType table)`

Gets a copy of an instance level internal array.

`static String[]`
`getTLDEntries(DomainValidator.ArrayType table)`

Gets a copy of a class level internal array.

`boolean`
`isAllowLocal()`

Tests whether this instance allow local addresses.

`boolean`
`isValid(String domain)`

Tests whether the specified `String` parses as a valid domain name with a recognized top-level domain.

`boolean`
`isValidCountryCodeTld(String ccTld)`

Tests whether the specified `String` matches any IANA-defined country code top-level domain.

`boolean`
`isValidGenericTld(String gTld)`

Tests whether the specified `String` matches any IANA-defined generic top-level domain.

`boolean`
`isValidInfrastructureTld(String iTld)`

Tests whether the specified `String` matches any IANA-defined infrastructure top-level domain.

`boolean`
`isValidLocalTld(String lTld)`

Tests whether the specified `String` matches any widely used "local" domains (localhost or localdomain).

`boolean`
`isValidTld(String tld)`

Returns true if the specified `String` matches any IANA-defined top-level domain.

`static void`
`updateTLDOverride(DomainValidator.ArrayType table,
 String... tlds)`

Updates one of the TLD override arrays.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Method Details

  - 

### getInstance

public static DomainValidator getInstance()
Gets the singleton instance of this validator. It will not consider local addresses as valid.

Returns:
the singleton instance of this validator.

  - 

### getInstance

public static DomainValidator getInstance(boolean allowLocal)
Gets the singleton instance of this validator, with local validation as required.

Parameters:
`allowLocal` - Whether local addresses are considered valid.
Returns:
the singleton instance of this validator.

  - 

### getInstance

public static DomainValidator getInstance(boolean allowLocal,
 List<DomainValidator.Item> items)
Gets a new instance of this validator. The user can provide a list of `DomainValidator.Item` entries which can be used to override the generic and country code
 lists. Note that any such entries override values provided by the `updateTLDOverride(ArrayType, String[])` method If an entry for a particular
 type is not provided, then the class override (if any) is retained.

Parameters:
`allowLocal` - Whether local addresses are considered valid.
`items` - array of `DomainValidator.Item` entries.
Returns:
an instance of this validator.
Since:
1.7

  - 

### getTLDEntries

public static String[] getTLDEntries(DomainValidator.ArrayType table)
Gets a copy of a class level internal array.

Parameters:
`table` - the array type (any of the enum values).
Returns:
a copy of the array.
Throws:
`IllegalArgumentException` - if the table type is unexpected (should not happen).
Since:
1.5.1

  - 

### updateTLDOverride

public static void updateTLDOverride(DomainValidator.ArrayType table,
 String... tlds)
Updates one of the TLD override arrays. This must only be done at program startup, before any instances are accessed using getInstance.
 

 For example:
 
 

 `DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, "apache")`
 
 

 To clear an override array, provide an empty array.
 

Parameters:
`table` - the table to update, see `DomainValidator.ArrayType` Must be one of the following
              

              
    - COUNTRY_CODE_MINUS
              
    - COUNTRY_CODE_PLUS
              
    - GENERIC_MINUS
              
    - GENERIC_PLUS
              
    - LOCAL_MINUS
              
    - LOCAL_PLUS
              

`tlds` - the array of TLDs, must not be null.
Throws:
`IllegalStateException` - if the method is called after getInstance.
`IllegalArgumentException` - if one of the read-only tables is requested.
Since:
1.5.0

  - 

### getOverrides

public String[] getOverrides(DomainValidator.ArrayType table)
Gets a copy of an instance level internal array.

Parameters:
`table` - the array type (any of the enum values).
Returns:
a copy of the array.
Throws:
`IllegalArgumentException` - if the table type is unexpected, for example, GENERIC_RO.
Since:
1.7

  - 

### isAllowLocal

public boolean isAllowLocal()
Tests whether this instance allow local addresses.

Returns:
true if local addresses are allowed.
Since:
1.7

  - 

### isValid

public boolean isValid(String domain)
Tests whether the specified `String` parses as a valid domain name with a recognized top-level domain. The parsing is case-insensitive.

Parameters:
`domain` - the parameter to check for domain name syntax.
Returns:
true if the parameter is a valid domain name.

  - 

### isValidCountryCodeTld

public boolean isValidCountryCodeTld(String ccTld)
Tests whether the specified `String` matches any IANA-defined country code top-level domain. Leading dots are ignored if present. The search is
 case-insensitive.

Parameters:
`ccTld` - the parameter to check for country code TLD status, not null.
Returns:
true if the parameter is a country code TLD.

  - 

### isValidGenericTld

public boolean isValidGenericTld(String gTld)
Tests whether the specified `String` matches any IANA-defined generic top-level domain. Leading dots are ignored if present. The search is
 case-insensitive.

Parameters:
`gTld` - the parameter to check for generic TLD status, not null.
Returns:
true if the parameter is a generic TLD.

  - 

### isValidInfrastructureTld

public boolean isValidInfrastructureTld(String iTld)
Tests whether the specified `String` matches any IANA-defined infrastructure top-level domain. Leading dots are ignored if present. The search is
 case-insensitive.

Parameters:
`iTld` - the parameter to check for infrastructure TLD status, not null.
Returns:
true if the parameter is an infrastructure TLD.

  - 

### isValidLocalTld

public boolean isValidLocalTld(String lTld)
Tests whether the specified `String` matches any widely used "local" domains (localhost or localdomain). Leading dots are ignored if present. The
 search is case-insensitive.

Parameters:
`lTld` - the parameter to check for local TLD status, not null.
Returns:
true if the parameter is a local TLD.

  - 

### isValidTld

public boolean isValidTld(String tld)
Returns true if the specified `String` matches any IANA-defined top-level domain. Leading dots are ignored if present. The search is
 case-insensitive.
 

 If allowLocal is true, the TLD is checked using `isValidLocalTld(String)`. The TLD is then checked against
 `isValidInfrastructureTld(String)`, `isValidGenericTld(String)` and `isValidCountryCodeTld(String)`.
 

Parameters:
`tld` - the parameter to check for TLD status, not null.
Returns:
true if the parameter is a TLD.