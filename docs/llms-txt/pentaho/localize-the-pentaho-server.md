# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/customize-pentaho-products-cp/customize-the-pentaho-user-console/localize-the-pentaho-server.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/customize-pentaho-products-cp/customize-the-pentaho-user-console/localize-the-pentaho-server.md

# Localize the Pentaho Server

You can localize the Pentaho User Console, Pentaho Analyzer, and Dashboard Designer by creating locale- and language-specific message bundles within the Pentaho web application. Message bundles are dynamically adjusted according to browser locale, so you can create localized message bundles for every language you want to support, and let each individual user's system language settings determine which one is loaded.

Stop the Pentaho Server before editing anything inside of the Pentaho WAR file.

For brevity's sake, only the default Pentaho User Console files will be explained in detail. The file naming convention is identical among all message bundles in Pentaho Business Analytics. The following files are located in the `mantle/messages/` directory:

* **`mantleMessages.properties`**

  The default message bundle for the Pentaho User Console. In its initial condition, it is a copy of `mantleMessages_en.properties`. If you want to change the default language and dialect, copy your preferred message bundle file over this one.
* **mantleMessages\_en.properties**

  The English-language version of the standard message bundle. This is an identical copy of `mantleMessages.properties`.
* **mantleMessages\_fr.properties**

  The French-language version of the standard message bundle.
* **mantleMessages\_de.properties**

  The German-language version of the standard message bundle.
* **mantleMessages\_supported\_languages.properties**

  Contains a list of localized message bundles and the native language names they correspond to; this relieves the Pentaho Server of the burden of having to discover them on its own. A `supported_languages.properties` file should be created for every message bundle that you intend to localize.

The following code is an example of the content found in the `mantleMessages_supported_languages.properties` file:

```
en=English
de=Deutsch
fr=Français
```

New files are created in the following format: `mantleMessages_*xx*_*YY*.properties` where *xx* represents a lowercase two-letter language code, and *YY* represents a two-letter locale code, where applicable. So, for instance, U.S. and British English could have two separate message bundles if you wanted to draw a distinction between the two dialects:

* `mantleMessages_en_US.properties`
* `mantleMessages_en_GB.properties`

The language and country codes must be in standard ISO format. You can look up both sets of codes on these pages:

* <http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes>
* <https://www.iso.org/iso-3166-country-codes.html>

You can edit the default message bundle directly if you need to make surgical changes to the content inside of it. If you plan to translate it into another language, it makes more sense to copy the file and change the name appropriately, then translate it line by line. Be sure to update `supported_languages.properties` with the new country and dialect code and the native language name that it corresponds to.

**Note:** All message bundles must be UTF-8 encoded.
