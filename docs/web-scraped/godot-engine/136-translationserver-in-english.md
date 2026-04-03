# TranslationServer in English

# TranslationServer
Inherits:Object
The server responsible for language translations.

## Description
The translation server is the API backend that manages all language translations.
Translations are stored inTranslationDomains, which can be accessed by name. The most commonly used translation domain is the main translation domain. It always exists and can be accessed using an emptyStringName. The translation server provides wrapper methods for accessing the main translation domain directly, without having to fetch the translation domain first. Custom translation domains are mainly for advanced usages like editor plugins. Names starting withgodot.are reserved for engine internals.

## Tutorials
- Internationalizing games
Internationalizing games
- Locales
Locales

## Properties

| bool | pseudolocalization_enabled | false |

bool
pseudolocalization_enabled
false

## Methods

| void | add_translation(translation:Translation) |
|---|---|
| void | clear() |
| int | compare_locales(locale_a:String, locale_b:String)const |
| Array[Translation] | find_translations(locale:String, exact:bool)const |
| String | format_number(number:String, locale:String)const |
| PackedStringArray | get_all_countries()const |
| PackedStringArray | get_all_languages()const |
| PackedStringArray | get_all_scripts()const |
| String | get_country_name(country:String)const |
| String | get_language_name(language:String)const |
| PackedStringArray | get_loaded_locales()const |
| String | get_locale()const |
| String | get_locale_name(locale:String)const |
| TranslationDomain | get_or_add_domain(domain:StringName) |
| String | get_percent_sign(locale:String)const |
| String | get_plural_rules(locale:String)const |
| String | get_script_name(script:String)const |
| String | get_tool_locale() |
| Translation | get_translation_object(locale:String) |
| Array[Translation] | get_translations()const |
| bool | has_domain(domain:StringName)const |
| bool | has_translation(translation:Translation)const |
| bool | has_translation_for_locale(locale:String, exact:bool)const |
| String | parse_number(number:String, locale:String)const |
| StringName | pseudolocalize(message:StringName)const |
| void | reload_pseudolocalization() |
| void | remove_domain(domain:StringName) |
| void | remove_translation(translation:Translation) |
| void | set_locale(locale:String) |
| String | standardize_locale(locale:String, add_defaults:bool= false)const |
| StringName | translate(message:StringName, context:StringName= &"")const |
| StringName | translate_plural(message:StringName, plural_message:StringName, n:int, context:StringName= &"")const |

void
add_translation(translation:Translation)
void
clear()
compare_locales(locale_a:String, locale_b:String)const
Array[Translation]
find_translations(locale:String, exact:bool)const
String
format_number(number:String, locale:String)const
PackedStringArray
get_all_countries()const
PackedStringArray
get_all_languages()const
PackedStringArray
get_all_scripts()const
String
get_country_name(country:String)const
String
get_language_name(language:String)const
PackedStringArray
get_loaded_locales()const
String
get_locale()const
String
get_locale_name(locale:String)const
TranslationDomain
get_or_add_domain(domain:StringName)
String
get_percent_sign(locale:String)const
String
get_plural_rules(locale:String)const
String
get_script_name(script:String)const
String
get_tool_locale()
Translation
get_translation_object(locale:String)
Array[Translation]
get_translations()const
bool
has_domain(domain:StringName)const
bool
has_translation(translation:Translation)const
bool
has_translation_for_locale(locale:String, exact:bool)const
String
parse_number(number:String, locale:String)const
StringName
pseudolocalize(message:StringName)const
void
reload_pseudolocalization()
void
remove_domain(domain:StringName)
void
remove_translation(translation:Translation)
void
set_locale(locale:String)
String
standardize_locale(locale:String, add_defaults:bool= false)const
StringName
translate(message:StringName, context:StringName= &"")const
StringName
translate_plural(message:StringName, plural_message:StringName, n:int, context:StringName= &"")const

## Property Descriptions
boolpseudolocalization_enabled=false🔗
- voidset_pseudolocalization_enabled(value:bool)
voidset_pseudolocalization_enabled(value:bool)
- boolis_pseudolocalization_enabled()
boolis_pseudolocalization_enabled()
Iftrue, enables the use of pseudolocalization on the main translation domain. SeeProjectSettings.internationalization/pseudolocalization/use_pseudolocalizationfor details.

## Method Descriptions
voidadd_translation(translation:Translation)🔗
Adds a translation to the main translation domain.
voidclear()🔗
Removes all translations from the main translation domain.
intcompare_locales(locale_a:String, locale_b:String)const🔗
Compares two locales and returns a similarity score between0(no match) and10(full match).
Array[Translation]find_translations(locale:String, exact:bool)const🔗
Returns theTranslationinstances in the main translation domain that matchlocale(seecompare_locales()). Ifexactistrue, only instances whose locale exactly equalslocalewill be returned.
Stringformat_number(number:String, locale:String)const🔗
Converts a number from Western Arabic (0..9) to the numeral system used in the givenlocale.
PackedStringArrayget_all_countries()const🔗
Returns an array of known country codes.
PackedStringArrayget_all_languages()const🔗
Returns array of known language codes.
PackedStringArrayget_all_scripts()const🔗
Returns an array of known script codes.
Stringget_country_name(country:String)const🔗
Returns a readable country name for thecountrycode.
Stringget_language_name(language:String)const🔗
Returns a readable language name for thelanguagecode.
PackedStringArrayget_loaded_locales()const🔗
Returns an array of all loaded locales of the project.
Stringget_locale()const🔗
Returns the current locale of the project.
See alsoOS.get_locale()andOS.get_locale_language()to query the locale of the user system.
Stringget_locale_name(locale:String)const🔗
Returns a locale's language and its variant (e.g."en_US"would return"English(UnitedStates)").
TranslationDomainget_or_add_domain(domain:StringName)🔗
Returns the translation domain with the specified name. An empty translation domain will be created and added if it does not exist.
Stringget_percent_sign(locale:String)const🔗
Returns the percent sign used in the givenlocale.
Stringget_plural_rules(locale:String)const🔗
Returns the default plural rules for thelocale.
Stringget_script_name(script:String)const🔗
Returns a readable script name for thescriptcode.
Stringget_tool_locale()🔗
Returns the current locale of the editor.
Note:When called from an exported project returns the same value asget_locale().
Translationget_translation_object(locale:String)🔗
Deprecated:Usefind_translations()instead.
Returns theTranslationinstance that best matcheslocalein the main translation domain. Returnsnullif there are no matches.
Array[Translation]get_translations()const🔗
Returns all availableTranslationinstances in the main translation domain as added byadd_translation().
boolhas_domain(domain:StringName)const🔗
Returnstrueif a translation domain with the specified name exists.
boolhas_translation(translation:Translation)const🔗
Returnstrueif the main translation domain contains the giventranslation.
boolhas_translation_for_locale(locale:String, exact:bool)const🔗
Returnstrueif there are anyTranslationinstances in the main translation domain that matchlocale(seecompare_locales()). Ifexactistrue, only instances whose locale exactly equalslocaleare considered.
Stringparse_number(number:String, locale:String)const🔗
Convertsnumberfrom the numeral system used in the givenlocaleto Western Arabic (0..9).
StringNamepseudolocalize(message:StringName)const🔗
Returns the pseudolocalized string based on themessagepassed in.
Note:This method always uses the main translation domain.
voidreload_pseudolocalization()🔗
Reparses the pseudolocalization options and reloads the translation for the main translation domain.
voidremove_domain(domain:StringName)🔗
Removes the translation domain with the specified name.
Note:Trying to remove the main translation domain is an error.
voidremove_translation(translation:Translation)🔗
Removes the given translation from the main translation domain.
voidset_locale(locale:String)🔗
Sets the locale of the project. Thelocalestring will be standardized to match known locales (e.g.en-USwould be matched toen_US).
If translations have been loaded beforehand for the new locale, they will be applied.
Stringstandardize_locale(locale:String, add_defaults:bool= false)const🔗
Returns alocalestring standardized to match known locales (e.g.en-USwould be matched toen_US). Ifadd_defaultsistrue, the locale may have a default script or country added.
StringNametranslate(message:StringName, context:StringName= &"")const🔗
Returns the current locale's translation for the given message and context.
Note:This method always uses the main translation domain.
StringNametranslate_plural(message:StringName, plural_message:StringName, n:int, context:StringName= &"")const🔗
Returns the current locale's translation for the given message, plural message and context.
The numbernis the number or quantity of the plural object. It will be used to guide the translation system to fetch the correct plural form for the selected language.
Note:This method always uses the main translation domain.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.