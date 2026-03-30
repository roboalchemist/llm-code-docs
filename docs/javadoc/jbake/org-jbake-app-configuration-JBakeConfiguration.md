Package org.jbake.app.configuration

# Interface JBakeConfiguration

All Known Implementing Classes:
`DefaultJBakeConfiguration`

---

public interface JBakeConfiguration
JBakeConfiguration gives you access to the project configuration. Typically located in a file called jbake.properties.

 Use one of `JBakeConfigurationFactory` methods to create an instance.

- 

## Method Summary

Modifier and Type
Method
Description
`void`
`addConfiguration(Properties properties)`
 
`Map<String,Object>`
`asHashMap()`
 
`Object`
`get(String key)`

Get property value by a given key from the configuration

`String`
`getAbbreviatedGitHash()`
 
`String`
`getArchiveFileName()`
 
`List<String>`
`getAsciidoctorAttributes()`
 
`Object`
`getAsciidoctorOption(String optionKey)`

Get an asciidoctor option by it's key

`List<String>`
`getAsciidoctorOptionKeys()`

Get a list of asciidoctor options

`File`
`getAssetFolder()`
 
`String`
`getAssetFolderName()`
 
`boolean`
`getAssetIgnoreHidden()`
 
`String`
`getAttributesExportPrefixForAsciidoctor()`
 
`String`
`getBuildTimeStamp()`
 
`boolean`
`getClearCache()`
 
`File`
`getContentFolder()`
 
`String`
`getContentFolderName()`
 
`String`
`getDatabasePath()`
 
`String`
`getDatabaseStore()`
 
`String`
`getDataFileDocType()`
 
`File`
`getDataFolder()`
 
`String`
`getDataFolderName()`
 
`String`
`getDateFormat()`
 
`String`
`getDefaultStatus()`
 
`String`
`getDefaultType()`
 
`File`
`getDestinationFolder()`
 
`List<String>`
`getDocumentTypes()`
 
`String`
`getDraftSuffix()`
 
`String`
`getError404FileName()`
 
`String`
`getExampleProjectByType(String templateType)`

Get name for example project name by given template type

`boolean`
`getExportAsciidoctorAttributes()`
 
`String`
`getFeedFileName()`
 
`TimeZone`
`getFreemarkerTimeZone()`
 
`String`
`getHeaderSeparator()`
 
`String`
`getIgnoreFileName()`
 
`boolean`
`getImgPathPrependHost()`
 
`boolean`
`getImgPathUpdate()`
 
`String`
`getIndexFileName()`
 
`List<Property>`
`getJbakeProperties()`
 
`String`
`getJvmLocale()`
 
`Iterator<String>`
`getKeys()`

Get an iterator of available configuration keys

`List<String>`
`getMarkdownExtensions()`

A list of markdown extensions

`String`
`getOutputEncoding()`
 
`String`
`getOutputExtension()`
 
`String`
`getOutputExtensionByDocType(String docType)`
 
`boolean`
`getPaginateIndex()`
 
`int`
`getPostsPerPage()`
 
`String`
`getPrefixForUriWithoutExtension()`
 
`boolean`
`getRenderArchive()`
 
`String`
`getRenderEncoding()`
 
`boolean`
`getRenderError404()`
 
`boolean`
`getRenderFeed()`
 
`boolean`
`getRenderIndex()`
 
`boolean`
`getRenderSiteMap()`
 
`boolean`
`getRenderTags()`
 
`boolean`
`getRenderTagsIndex()`
 
`boolean`
`getSanitizeTag()`
 
`String`
`getServerContextPath()`
 
`String`
`getServerHostname()`
 
`int`
`getServerPort()`
 
`String`
`getSiteHost()`
 
`String`
`getSiteMapFileName()`
 
`File`
`getSourceFolder()`
 
`String`
`getTagPathName()`
 
`String`
`getTemplateByDocType(String doctype)`
 
`String`
`getTemplateEncoding()`
 
`File`
`getTemplateFileByDocType(String doctype)`
 
`File`
`getTemplateFolder()`
 
`String`
`getTemplateFolderName()`
 
`String`
`getThymeleafLocale()`
 
`String`
`getThymeleafModeByType(String type)`
 
`boolean`
`getUriWithoutExtension()`
 
`String`
`getVersion()`
 
`void`
`setDestinationFolder(File destination)`
 
`void`
`setProperty(String key,
 Object value)`

Set a property value for the given key

- 

## Method Details

  - 

### get

Object get(String key)
Get property value by a given key from the configuration

Parameters:
`key` - a key for the property like site.host
Returns:
the value of the property

  - 

### getArchiveFileName

String getArchiveFileName()

Returns:
Output filename for archive file, is only used when `getRenderArchive()` is true

  - 

### getAsciidoctorAttributes

List<String> getAsciidoctorAttributes()

Returns:
attributes to be set when processing input

  - 

### getAsciidoctorOption

Object getAsciidoctorOption(String optionKey)
Get an asciidoctor option by it's key

Parameters:
`optionKey` - an option key
Returns:
the value of the option key

  - 

### getAsciidoctorOptionKeys

List<String> getAsciidoctorOptionKeys()
Get a list of asciidoctor options

Returns:
list of asciidoctor options

  - 

### getAssetFolder

File getAssetFolder()

Returns:
the folder where assets are stored, they are copied directly in output folder and not processed

  - 

### getAssetFolderName

String getAssetFolderName()

Returns:
name of folder for assets

  - 

### getAssetIgnoreHidden

boolean getAssetIgnoreHidden()

Returns:
Flag indicating if hidden asset resources should be ignored

  - 

### getAttributesExportPrefixForAsciidoctor

String getAttributesExportPrefixForAsciidoctor()

Returns:
Prefix to be used when exporting JBake properties to Asciidoctor

  - 

### getBuildTimeStamp

String getBuildTimeStamp()

Returns:
Timestamp that records when JBake build was made

  - 

### getClearCache

boolean getClearCache()

Returns:
Flag indicating to flash the database cache

  - 

### getContentFolder

File getContentFolder()

Returns:
the content folder

  - 

### getContentFolderName

String getContentFolderName()

Returns:
name of Folder where content (that's to say files to be transformed) resides in

  - 

### getDataFolder

File getDataFolder()

Returns:
the data folder

  - 

### getDataFolderName

String getDataFolderName()

Returns:
name of Folder where data files reside in

  - 

### getDataFileDocType

String getDataFileDocType()

Returns:
docType for data files

  - 

### getDatabasePath

String getDatabasePath()

Returns:
Folder to store database files in

  - 

### getDatabaseStore

String getDatabaseStore()

Returns:
name to identify if database is kept in memory (memory) or persisted to disk (plocal)

  - 

### getDateFormat

String getDateFormat()

Returns:
How date is formated

  - 

### getDefaultStatus

String getDefaultStatus()

Returns:
Default status to use (in order to avoid putting it in all files)

  - 

### getDefaultType

String getDefaultType()

Returns:
Default type to use (in order to avoid putting it in all files)

  - 

### getDestinationFolder

File getDestinationFolder()

Returns:
The destination folder to render and copy files to

  - 

### setDestinationFolder

void setDestinationFolder(File destination)

  - 

### getDocumentTypes

List<String> getDocumentTypes()

  - 

### getDraftSuffix

String getDraftSuffix()

Returns:
Suffix used to identify draft files

  - 

### getError404FileName

String getError404FileName()

Returns:
Output filename for error404 file, is only used when `getRenderError404()` is true

  - 

### getExampleProjectByType

String getExampleProjectByType(String templateType)
Get name for example project name by given template type

Parameters:
`templateType` - a template type
Returns:
example project name

  - 

### getExportAsciidoctorAttributes

boolean getExportAsciidoctorAttributes()

Returns:
Flag indicating if JBake properties should be made available to Asciidoctor

  - 

### getFeedFileName

String getFeedFileName()

Returns:
Output filename for feed file, is only used when `getRenderFeed()` is true

  - 

### getHeaderSeparator

String getHeaderSeparator()

Returns:
String used to separate the header from the body

  - 

### getIgnoreFileName

String getIgnoreFileName()

Returns:
Filename to use to ignore a directory in addition to ".jbakeignore"

  - 

### getIndexFileName

String getIndexFileName()

Returns:
Output filename for index, is only used when `getRenderIndex()` is true

  - 

### getKeys

Iterator<String> getKeys()
Get an iterator of available configuration keys

Returns:
an iterator of configuration keys

  - 

### getMarkdownExtensions

List<String> getMarkdownExtensions()
A list of markdown extensions
 

 `markdown.extension=HARDWRAPS,AUTOLINKS,FENCED_CODE_BLOCKS,DEFINITIONS`

Returns:
list of markdown extensions as string

  - 

### getOutputExtension

String getOutputExtension()

Returns:
file extension to be used for all output files

  - 

### getOutputExtensionByDocType

String getOutputExtensionByDocType(String docType)

  - 

### getPaginateIndex

boolean getPaginateIndex()

Returns:
Flag indicating if there should be pagination when rendering index

  - 

### getPostsPerPage

int getPostsPerPage()

Returns:
How many posts per page on index

  - 

### getPrefixForUriWithoutExtension

String getPrefixForUriWithoutExtension()

Returns:
URI prefix for content that should be given extension-less output URI's

  - 

### getRenderArchive

boolean getRenderArchive()

Returns:
Flag indicating if archive file should be generated

  - 

### getRenderEncoding

String getRenderEncoding()

Returns:
Encoding used when rendering files

  - 

### getOutputEncoding

String getOutputEncoding()

Returns:
Output encoding for freemarker url escaping

  - 

### getRenderError404

boolean getRenderError404()

Returns:
Flag indicating if error404 file should be generated

  - 

### getRenderFeed

boolean getRenderFeed()

Returns:
Flag indicating if feed file should be generated

  - 

### getRenderIndex

boolean getRenderIndex()

Returns:
Flag indicating if index file should be generated

  - 

### getRenderSiteMap

boolean getRenderSiteMap()

Returns:
Flag indicating if sitemap file should be generated

  - 

### getRenderTags

boolean getRenderTags()

Returns:
Flag indicating if tag files should be generated

  - 

### getRenderTagsIndex

boolean getRenderTagsIndex()

Returns:
Flag indicating if tag index file should be generated

  - 

### getSanitizeTag

boolean getSanitizeTag()

Returns:
Flag indicating if the tag value should be sanitized

  - 

### getServerPort

int getServerPort()

Returns:
Port used when running Jetty server

  - 

### getSiteHost

String getSiteHost()

Returns:
the host url of the site e.g. http://jbake.org

  - 

### getSiteMapFileName

String getSiteMapFileName()

Returns:
Sitemap template file name. Used only when `getRenderSiteMap()` is set to true

  - 

### getSourceFolder

File getSourceFolder()

Returns:
the source folder of the project

  - 

### getTagPathName

String getTagPathName()

Returns:
Tags output path, used only when `getRenderTags()` is true

  - 

### getTemplateEncoding

String getTemplateEncoding()

Returns:
Encoding to be used for template files

  - 

### getTemplateByDocType

String getTemplateByDocType(String doctype)

  - 

### getTemplateFileByDocType

File getTemplateFileByDocType(String doctype)

  - 

### getTemplateFolder

File getTemplateFolder()

Returns:
the template folder

  - 

### getTemplateFolderName

String getTemplateFolderName()

Returns:
name of folder where template files are looked for

  - 

### getThymeleafLocale

String getThymeleafLocale()

Returns:
Locale used for Thymeleaf template rendering

  - 

### getUriWithoutExtension

boolean getUriWithoutExtension()

Returns:
Flag indicating if content matching prefix below should be given extension-less URI's

  - 

### getImgPathPrependHost

boolean getImgPathPrependHost()

Returns:
Flag indicating if image paths should be prepended with `getSiteHost()` value - only has an effect if
 `getImgPathUpdate()` is set to true

  - 

### getImgPathUpdate

boolean getImgPathUpdate()

Returns:
Flag indicating if image paths in content should be updated with absolute path (using URI value of content file),
 see `getImgPathUpdate()` which allows you to control the absolute path used

  - 

### getVersion

String getVersion()

Returns:
Version of JBake

  - 

### setProperty

void setProperty(String key,
 Object value)
Set a property value for the given key

Parameters:
`key` - the key for the property
`value` - the value of the property

  - 

### getThymeleafModeByType

String getThymeleafModeByType(String type)

Parameters:
`type` - the documents type
Returns:
the the thymeleaf render mode ( defaults to `DefaultJBakeConfiguration.DEFAULT_TYHMELEAF_TEMPLATE_MODE` )

  - 

### getServerContextPath

String getServerContextPath()

  - 

### getServerHostname

String getServerHostname()

  - 

### getAbbreviatedGitHash

String getAbbreviatedGitHash()

Returns:
Abbreviated hash of latest git commit

  - 

### getJvmLocale

String getJvmLocale()

Returns:
Locale to set in the JVM

  - 

### getFreemarkerTimeZone

TimeZone getFreemarkerTimeZone()

Returns:
TimeZone to use within Freemarker

  - 

### asHashMap

Map<String,Object> asHashMap()

  - 

### getJbakeProperties

List<Property> getJbakeProperties()

  - 

### addConfiguration

void addConfiguration(Properties properties)