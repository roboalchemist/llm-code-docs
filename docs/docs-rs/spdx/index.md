# Crate spdx 
Source 
## Re-exports§
`pub use error::ParseError;``pub use expression::Expression;``pub use lexer::ParseMode;`
## Modules§
detection`detection`Allows analysis of text to determine if it resembles a license
This module is basically an inling of askalonoerrorError typesexpressionTypes used in SPDX expressions, notably `Expression`flagsFlags that can apply to licenses and/or license exceptionsidentifiersAuto-generated lists of license identifiers and exception identifierslexerContains types for lexing an SPDX license expressiontext`text`Auto-generated full canonical text of each license
## Structs§
AdditionRefA user supplied `AddtionRef-<user string>` to specify additional text to
associate with a license that falls outside the SPDX license listExceptionAn SPDX exceptionExceptionIdUnique identifier for a particular exceptionLicenseAn SPDX licenseLicenseIdUnique identifier for a particular licenseLicenseRefSPDX allows the use of `LicenseRef-<user supplied string>` to provide
arbitrary licenses that aren’t a part of the official SPDX license listLicenseReqRepresents a single license requirement.LicenseeA convenience wrapper for a license and optional additional text that can be
checked against a license requirement to see if it satisfies the requirement
placed by a license holder
## Enums§
AdditionItemA single addition term in a addition expression, according to the SPDX spec.LicenseItemA single license term in a license expression, according to the SPDX spec.
## Functions§
exception_idAttempts to find an `ExceptionId` for the stringgnu_license_idAttempts to find a GNU license from its base name.imprecise_license_idFind license partially matching the name, e.g. “apache” => “Apache-2.0”license_idAttempts to find a `LicenseId` given a short id.license_versionReturns the version number of the SPDX list from which
the license and exception identifiers are sourced from