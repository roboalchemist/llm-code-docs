spdx::lexer
# Struct ParseMode 
Source 

```
pub struct ParseMode {
    pub allow_slash_as_or_operator: bool,
    pub allow_imprecise_license_names: bool,
    pub allow_postfix_plus_on_gpl: bool,
    pub allow_deprecated: bool,
    pub allow_unknown: bool,
}
```

## Fields§
§`allow_slash_as_or_operator: bool`

Allows the use of `/` as a synonym for the `OR` operator.

This also allows for not having whitespace between the `/` and the terms
on either side
§`allow_imprecise_license_names: bool`

Allows some invalid/imprecise identifiers as synonyms for an actual
license identifier.

See `IMPRECISE_NAMES` for a list
of the current synonyms. Note that this list is not comprehensive but
can be expanded upon when invalid identifiers are found in the wild.
§`allow_postfix_plus_on_gpl: bool`

The various GPL licenses diverge from every other license in the SPDX
license list by having an `-or-later` variant that is used as a suffix
on a base license (eg. `GPL-3.0-or-later`) rather than the canonical
`GPL-3.0+`.

This option just allows GPL licenses to be treated similarly to all of
the other SPDX licenses.
§`allow_deprecated: bool`

Whether deprecated license or exception identifiers are allowed
§`allow_unknown: bool`

Whether unknown license or exception identifiers are allowed

## Implementations§