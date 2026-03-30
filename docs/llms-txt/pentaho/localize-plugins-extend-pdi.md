# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/embed-and-extend-pentaho-functionality-cp/embed-and-extend-pdi-functionality/extend-pentaho-data-integration/localize-plugins-extend-pdi.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/embed-and-extend-pentaho-functionality-cp/embed-and-extend-pdi-functionality/extend-pentaho-data-integration/localize-plugins-extend-pdi.md

# Localize plugins

#### Message bundles

PDI uses property files for internationalization. Property files reside in the `messages` sub-package in the plugin JAR file. Each property file is specific to a locale. Property files contain translations for message keys that are used in the source code. A `messages` sub-package containing locale-specific translations is called a message bundle.

Consider the package layout of the sample job entry plugin project. It contains its main Java class in the `org.pentaho.di.sdk.samples.jobentries.demo` package, and there is a message bundle containing the localized strings for the en\_US locale.

![Message bundle](https://3256662623-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTSPdUdWBWVGi0uurnXBG%2Fuploads%2Fgit-blob-650148459068e1497643228bed93b351a32ba526%2FExtend_Pentaho_Data_Integration_Message_bundle.png?alt=media)

Additional property files can be added using the naming pattern `messages_*&lt;locale&gt;*.properties`. PDI core steps and job entries usually come with several localizations. See the shell job entry messages package for an example of more complete `i18n`: [https://github.com/pentaho/pentaho-k...shell/messages](https://github.com/pentaho/pentaho-kettle/tree/master/engine/src/main/resources/org/pentaho/di/job/entries/shell/messages).

#### Resolving localized strings

The key to resolving localized strings is to use the `getString()` methods of [org.pentaho.di.i18n.BaseMessages](https://github.com/pentaho/pentaho-kettle/blob/master/core/src/main/java/org/pentaho/di/i18n/BaseMessages.java). PDI follows conventions when using this class, which enables easy integration with the [PDI translator tool](http://wiki.pentaho.com/display/EAI/Kettle+4+and+the+art+of+internationalization).

All PDI plugin classes that use localization declare a private static `Class<?> PKG` field, and assign a class that lives one package-level above the message bundle package. This is often the main class of the plugin.

With the `PKG` field defined, the plugin then resolves its localized strings with a call to `BaseMessages.getString(PKG, “localization key”, ... optional_parameters)`. The first argument helps PDI find the correct message bundle, the second argument is the key to localize, and the optional parameters are injected into the localized string following the Java [Message Format](http://docs.oracle.com/javase/6/docs/api/java/text/MessageFormat.html) conventions.

#### Common localization strings

Some strings are commonly used, and have been pulled together into a common message bundle in [org.pentaho.di.i18n.messages](https://github.com/pentaho/pentaho-kettle/tree/master/core/src/org/pentaho/di/i18n). Whenever `BaseMessages` cannot find the key in the specified message bundle, PDI looks for the key in the common message bundle.

#### Example

For an example, check the sample [Job Entry plugin project](https://docs.pentaho.com/pdia-admin/10.2-admin/embed-and-extend-pentaho-functionality-cp/embed-and-extend-pdi-functionality/extend-pentaho-data-integration/create-different-types-of-plugins/create-job-entry-plugins), which uses this technique for localized string resolution in its dialog class.
