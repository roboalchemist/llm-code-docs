# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/hierarchical-data/hdt-path-specification.md

# Hierarchical data path specifications

The Hierarchical data path (HDT) path specification for extractions is different than the specification for modifications. Each specification is described below.

## HDT path specification for extractions

The HDT path specifications for extractions are:

* You must always start with the dollar sign (`$`) for the root.
* Simple alphanumeric key values are separated by periods (`.`).
* Numeric indices are designated like arrays with square brackets `[ n ]`.
* Complex string identifiers are designated with single quotation marks in square brackets `[‘Complex string identifier’]`.
* If your identifier has a special characters like a single quote mark, you must escape that character with a backslash (`\`). For example `['\‘Complex string identifier\’']`.
* You can use the asterisk (\*) wildcard for string or numeric keys.

For example: `$['l am a perfectly'].normal[0].example`

## HDT path specification for modifications

The HDT path specifications for modifications are:

* There is an additional array push operator of square brackets `[ ]` when added to the end of an array that will create an index.
* There are four special reference quote marks that you can use:
  * `$[?string_field?]` - Takes the string value of a field from an incoming PDI row and uses that value as the map key fragment.
  * `$[#numeric_field#]` - Takes the numeric value of an incoming PDI field and uses the value for array or list access with a resolved numeric index.
  * `$[$string_backreference$]` – Matches the string key fragment from a previous paths segment.
  * `$[@numeric_backreference@]` - Matches the numeric array or list index from a previous paths segment.

**Note:** The backreference numbering is based on the index in the path. In the code example: `$.first[ 4 ][‘hello’]`, the `$1$ = ‘first`’, `@2@ = 4, $3$ = ‘hello’`. The backreference is a 1-based index, and the surrounding `$` or `@` specifies if a string or numeric value was used.
