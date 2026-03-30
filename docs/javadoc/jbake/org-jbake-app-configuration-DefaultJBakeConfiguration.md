Package org.jbake.app.configuration

# Class DefaultJBakeConfiguration

java.lang.Object
org.jbake.app.configuration.DefaultJBakeConfiguration

All Implemented Interfaces:
`JBakeConfiguration`

---

public class DefaultJBakeConfiguration
extends Object
implements JBakeConfiguration
The default implementation of a `JBakeConfiguration`

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`static final String`
`DEFAULT_TYHMELEAF_TEMPLATE_MODE`
 

- 

## Constructor Summary

Constructors

Constructor
Description
`DefaultJBakeConfiguration(File sourceFolder,
 org.apache.commons.configuration2.CompositeConfiguration configuration)`
 
`DefaultJBakeConfiguration(org.apache.commons.configuration2.CompositeConfiguration configuration)`

Deprecated.
use `DefaultJBakeConfiguration(File, CompositeConfiguration)` instead

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
 
`List<String>`
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
 
`org.apache.commons.configuration2.CompositeConfiguration`
`getCompositeConfiguration()`
 
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
`getTemplateByDocType(String docType)`
 
`String`
`getTemplateEncoding()`
 
`File`
`getTemplateFileByDocType(String docType)`
 
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
`setAssetFolder(File assetFolder)`
 
`void`
`setAssetIgnoreHidden(boolean assetIgnoreHidden)`
 
`void`
`setClearCache(boolean clearCache)`
 
`void`
`setCompositeConfiguration(org.apache.commons.configuration2.CompositeConfiguration configuration)`
 
`void`
`setContentFolder(File contentFolder)`
 
`void`
`setDatabasePath(String path)`
 
`void`
`setDatabaseStore(String storeType)`
 
`void`
`setDataFileDocType(String dataFileDocType)`
 
`void`
`setDataFolder(File dataFolder)`
 
`void`
`setDefaultStatus(String status)`
 
`void`
`setDefaultType(String type)`
 
`void`
`setDestinationFolder(File destinationFolder)`
 
`void`
`setDestinationFolderName(String folderName)`
 
`void`
`setExampleProject(String type,
 String fileName)`
 
`void`
`setHeaderSeparator(String headerSeparator)`
 
`void`
`setImgPathPrependHost(boolean imgPathPrependHost)`
 
`void`
`setImgPathUPdate(boolean imgPathUpdate)`
 
`void`
`setMarkdownExtensions(String... extensions)`
 
`void`
`setOutputExtension(String outputExtension)`
 
`void`
`setPaginateIndex(boolean paginateIndex)`
 
`void`
`setPostsPerPage(int postsPerPage)`
 
`void`
`setPrefixForUriWithoutExtension(String prefix)`
 
`void`
`setProperty(String key,
 Object value)`

Set a property value for the given key

`void`
`setRenderTagsIndex(boolean enable)`
 
`void`
`setServerPort(int port)`
 
`void`
`setSiteHost(String siteHost)`
 
`void`
`setSourceFolder(File sourceFolder)`
 
`void`
`setTemplateExtensionForDocType(String docType,
 String extension)`
 
`void`
`setTemplateFileNameForDocType(String docType,
 String fileName)`
 
`void`
`setTemplateFolder(File templateFolder)`
 
`void`
`setUriWithoutExtension(boolean withoutExtension)`
 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Field Details

  - 

### DEFAULT_TYHMELEAF_TEMPLATE_MODE

public static final String DEFAULT_TYHMELEAF_TEMPLATE_MODE

See Also:

    - Constant Field Values

- 

## Constructor Details

  - 

### DefaultJBakeConfiguration

@Deprecated
public DefaultJBakeConfiguration(org.apache.commons.configuration2.CompositeConfiguration configuration)
Deprecated.
use `DefaultJBakeConfiguration(File, CompositeConfiguration)` instead

Some deprecated implementations just need access to the configuration without access to the source folder

Parameters:
`configuration` - The project configuration

  - 

### DefaultJBakeConfiguration

public DefaultJBakeConfiguration(File sourceFolder,
 org.apache.commons.configuration2.CompositeConfiguration configuration)

- 

## Method Details

  - 

### get

public Object get(String key)
Description copied from interface: `JBakeConfiguration`
Get property value by a given key from the configuration

Specified by:
`get` in interface `JBakeConfiguration`
Parameters:
`key` - a key for the property like site.host
Returns:
the value of the property

  - 

### getArchiveFileName

public String getArchiveFileName()

Specified by:
`getArchiveFileName` in interface `JBakeConfiguration`
Returns:
Output filename for archive file, is only used when `JBakeConfiguration.getRenderArchive()` is true

  - 

### getAsciidoctorAttributes

public List<String> getAsciidoctorAttributes()

Specified by:
`getAsciidoctorAttributes` in interface `JBakeConfiguration`
Returns:
attributes to be set when processing input

  - 

### getAsciidoctorOption

public List<String> getAsciidoctorOption(String optionKey)
Description copied from interface: `JBakeConfiguration`
Get an asciidoctor option by it's key

Specified by:
`getAsciidoctorOption` in interface `JBakeConfiguration`
Parameters:
`optionKey` - an option key
Returns:
the value of the option key

  - 

### getAsciidoctorOptionKeys

public List<String> getAsciidoctorOptionKeys()
Description copied from interface: `JBakeConfiguration`
Get a list of asciidoctor options

Specified by:
`getAsciidoctorOptionKeys` in interface `JBakeConfiguration`
Returns:
list of asciidoctor options

  - 

### getAssetFolder

public File getAssetFolder()

Specified by:
`getAssetFolder` in interface `JBakeConfiguration`
Returns:
the folder where assets are stored, they are copied directly in output folder and not processed

  - 

### setAssetFolder

public void setAssetFolder(File assetFolder)

  - 

### getAssetFolderName

public String getAssetFolderName()

Specified by:
`getAssetFolderName` in interface `JBakeConfiguration`
Returns:
name of folder for assets

  - 

### getAssetIgnoreHidden

public boolean getAssetIgnoreHidden()

Specified by:
`getAssetIgnoreHidden` in interface `JBakeConfiguration`
Returns:
Flag indicating if hidden asset resources should be ignored

  - 

### setAssetIgnoreHidden

public void setAssetIgnoreHidden(boolean assetIgnoreHidden)

  - 

### getAttributesExportPrefixForAsciidoctor

public String getAttributesExportPrefixForAsciidoctor()

Specified by:
`getAttributesExportPrefixForAsciidoctor` in interface `JBakeConfiguration`
Returns:
Prefix to be used when exporting JBake properties to Asciidoctor

  - 

### getBuildTimeStamp

public String getBuildTimeStamp()

Specified by:
`getBuildTimeStamp` in interface `JBakeConfiguration`
Returns:
Timestamp that records when JBake build was made

  - 

### getClearCache

public boolean getClearCache()

Specified by:
`getClearCache` in interface `JBakeConfiguration`
Returns:
Flag indicating to flash the database cache

  - 

### setClearCache

public void setClearCache(boolean clearCache)

  - 

### getCompositeConfiguration

public org.apache.commons.configuration2.CompositeConfiguration getCompositeConfiguration()

  - 

### setCompositeConfiguration

public void setCompositeConfiguration(org.apache.commons.configuration2.CompositeConfiguration configuration)

  - 

### getContentFolder

public File getContentFolder()

Specified by:
`getContentFolder` in interface `JBakeConfiguration`
Returns:
the content folder

  - 

### setContentFolder

public void setContentFolder(File contentFolder)

  - 

### getContentFolderName

public String getContentFolderName()

Specified by:
`getContentFolderName` in interface `JBakeConfiguration`
Returns:
name of Folder where content (that's to say files to be transformed) resides in

  - 

### getDataFolder

public File getDataFolder()

Specified by:
`getDataFolder` in interface `JBakeConfiguration`
Returns:
the data folder

  - 

### setDataFolder

public void setDataFolder(File dataFolder)

  - 

### getDataFolderName

public String getDataFolderName()

Specified by:
`getDataFolderName` in interface `JBakeConfiguration`
Returns:
name of Folder where data files reside in

  - 

### getDataFileDocType

public String getDataFileDocType()

Specified by:
`getDataFileDocType` in interface `JBakeConfiguration`
Returns:
docType for data files

  - 

### setDataFileDocType

public void setDataFileDocType(String dataFileDocType)

  - 

### getDatabasePath

public String getDatabasePath()

Specified by:
`getDatabasePath` in interface `JBakeConfiguration`
Returns:
Folder to store database files in

  - 

### setDatabasePath

public void setDatabasePath(String path)

  - 

### getDatabaseStore

public String getDatabaseStore()

Specified by:
`getDatabaseStore` in interface `JBakeConfiguration`
Returns:
name to identify if database is kept in memory (memory) or persisted to disk (plocal)

  - 

### setDatabaseStore

public void setDatabaseStore(String storeType)

  - 

### getDateFormat

public String getDateFormat()

Specified by:
`getDateFormat` in interface `JBakeConfiguration`
Returns:
How date is formated

  - 

### getDefaultStatus

public String getDefaultStatus()

Specified by:
`getDefaultStatus` in interface `JBakeConfiguration`
Returns:
Default status to use (in order to avoid putting it in all files)

  - 

### setDefaultStatus

public void setDefaultStatus(String status)

  - 

### getDefaultType

public String getDefaultType()

Specified by:
`getDefaultType` in interface `JBakeConfiguration`
Returns:
Default type to use (in order to avoid putting it in all files)

  - 

### setDefaultType

public void setDefaultType(String type)

  - 

### getDestinationFolder

public File getDestinationFolder()

Specified by:
`getDestinationFolder` in interface `JBakeConfiguration`
Returns:
The destination folder to render and copy files to

  - 

### setDestinationFolder

public void setDestinationFolder(File destinationFolder)

Specified by:
`setDestinationFolder` in interface `JBakeConfiguration`

  - 

### getDocumentTypes

public List<String> getDocumentTypes()

Specified by:
`getDocumentTypes` in interface `JBakeConfiguration`

  - 

### getDraftSuffix

public String getDraftSuffix()

Specified by:
`getDraftSuffix` in interface `JBakeConfiguration`
Returns:
Suffix used to identify draft files

  - 

### getError404FileName

public String getError404FileName()

Specified by:
`getError404FileName` in interface `JBakeConfiguration`
Returns:
Output filename for error404 file, is only used when `JBakeConfiguration.getRenderError404()` is true

  - 

### getExampleProjectByType

public String getExampleProjectByType(String templateType)
Description copied from interface: `JBakeConfiguration`
Get name for example project name by given template type

Specified by:
`getExampleProjectByType` in interface `JBakeConfiguration`
Parameters:
`templateType` - a template type
Returns:
example project name

  - 

### getExportAsciidoctorAttributes

public boolean getExportAsciidoctorAttributes()

Specified by:
`getExportAsciidoctorAttributes` in interface `JBakeConfiguration`
Returns:
Flag indicating if JBake properties should be made available to Asciidoctor

  - 

### getFeedFileName

public String getFeedFileName()

Specified by:
`getFeedFileName` in interface `JBakeConfiguration`
Returns:
Output filename for feed file, is only used when `JBakeConfiguration.getRenderFeed()` is true

  - 

### getIgnoreFileName

public String getIgnoreFileName()

Specified by:
`getIgnoreFileName` in interface `JBakeConfiguration`
Returns:
Filename to use to ignore a directory in addition to ".jbakeignore"

  - 

### getIndexFileName

public String getIndexFileName()

Specified by:
`getIndexFileName` in interface `JBakeConfiguration`
Returns:
Output filename for index, is only used when `JBakeConfiguration.getRenderIndex()` is true

  - 

### getKeys

public Iterator<String> getKeys()
Description copied from interface: `JBakeConfiguration`
Get an iterator of available configuration keys

Specified by:
`getKeys` in interface `JBakeConfiguration`
Returns:
an iterator of configuration keys

  - 

### getMarkdownExtensions

public List<String> getMarkdownExtensions()
Description copied from interface: `JBakeConfiguration`
A list of markdown extensions
 

 `markdown.extension=HARDWRAPS,AUTOLINKS,FENCED_CODE_BLOCKS,DEFINITIONS`

Specified by:
`getMarkdownExtensions` in interface `JBakeConfiguration`
Returns:
list of markdown extensions as string

  - 

### setMarkdownExtensions

public void setMarkdownExtensions(String... extensions)

  - 

### getOutputExtension

public String getOutputExtension()

Specified by:
`getOutputExtension` in interface `JBakeConfiguration`
Returns:
file extension to be used for all output files

  - 

### setOutputExtension

public void setOutputExtension(String outputExtension)

  - 

### getOutputExtensionByDocType

public String getOutputExtensionByDocType(String docType)

Specified by:
`getOutputExtensionByDocType` in interface `JBakeConfiguration`

  - 

### getPaginateIndex

public boolean getPaginateIndex()

Specified by:
`getPaginateIndex` in interface `JBakeConfiguration`
Returns:
Flag indicating if there should be pagination when rendering index

  - 

### setPaginateIndex

public void setPaginateIndex(boolean paginateIndex)

  - 

### getPostsPerPage

public int getPostsPerPage()

Specified by:
`getPostsPerPage` in interface `JBakeConfiguration`
Returns:
How many posts per page on index

  - 

### setPostsPerPage

public void setPostsPerPage(int postsPerPage)

  - 

### getPrefixForUriWithoutExtension

public String getPrefixForUriWithoutExtension()

Specified by:
`getPrefixForUriWithoutExtension` in interface `JBakeConfiguration`
Returns:
URI prefix for content that should be given extension-less output URI's

  - 

### setPrefixForUriWithoutExtension

public void setPrefixForUriWithoutExtension(String prefix)

  - 

### getRenderArchive

public boolean getRenderArchive()

Specified by:
`getRenderArchive` in interface `JBakeConfiguration`
Returns:
Flag indicating if archive file should be generated

  - 

### getRenderEncoding

public String getRenderEncoding()

Specified by:
`getRenderEncoding` in interface `JBakeConfiguration`
Returns:
Encoding used when rendering files

  - 

### getOutputEncoding

public String getOutputEncoding()

Specified by:
`getOutputEncoding` in interface `JBakeConfiguration`
Returns:
Output encoding for freemarker url escaping

  - 

### getRenderError404

public boolean getRenderError404()

Specified by:
`getRenderError404` in interface `JBakeConfiguration`
Returns:
Flag indicating if error404 file should be generated

  - 

### getRenderFeed

public boolean getRenderFeed()

Specified by:
`getRenderFeed` in interface `JBakeConfiguration`
Returns:
Flag indicating if feed file should be generated

  - 

### getRenderIndex

public boolean getRenderIndex()

Specified by:
`getRenderIndex` in interface `JBakeConfiguration`
Returns:
Flag indicating if index file should be generated

  - 

### getRenderSiteMap

public boolean getRenderSiteMap()

Specified by:
`getRenderSiteMap` in interface `JBakeConfiguration`
Returns:
Flag indicating if sitemap file should be generated

  - 

### getRenderTags

public boolean getRenderTags()

Specified by:
`getRenderTags` in interface `JBakeConfiguration`
Returns:
Flag indicating if tag files should be generated

  - 

### getRenderTagsIndex

public boolean getRenderTagsIndex()

Specified by:
`getRenderTagsIndex` in interface `JBakeConfiguration`
Returns:
Flag indicating if tag index file should be generated

  - 

### setRenderTagsIndex

public void setRenderTagsIndex(boolean enable)

  - 

### getSanitizeTag

public boolean getSanitizeTag()

Specified by:
`getSanitizeTag` in interface `JBakeConfiguration`
Returns:
Flag indicating if the tag value should be sanitized

  - 

### getServerPort

public int getServerPort()

Specified by:
`getServerPort` in interface `JBakeConfiguration`
Returns:
Port used when running Jetty server

  - 

### setServerPort

public void setServerPort(int port)

  - 

### getSiteHost

public String getSiteHost()

Specified by:
`getSiteHost` in interface `JBakeConfiguration`
Returns:
the host url of the site e.g. http://jbake.org

  - 

### setSiteHost

public void setSiteHost(String siteHost)

  - 

### getSiteMapFileName

public String getSiteMapFileName()

Specified by:
`getSiteMapFileName` in interface `JBakeConfiguration`
Returns:
Sitemap template file name. Used only when `JBakeConfiguration.getRenderSiteMap()` is set to true

  - 

### getSourceFolder

public File getSourceFolder()

Specified by:
`getSourceFolder` in interface `JBakeConfiguration`
Returns:
the source folder of the project

  - 

### setSourceFolder

public void setSourceFolder(File sourceFolder)

  - 

### getTagPathName

public String getTagPathName()

Specified by:
`getTagPathName` in interface `JBakeConfiguration`
Returns:
Tags output path, used only when `JBakeConfiguration.getRenderTags()` is true

  - 

### getTemplateEncoding

public String getTemplateEncoding()

Specified by:
`getTemplateEncoding` in interface `JBakeConfiguration`
Returns:
Encoding to be used for template files

  - 

### getTemplateByDocType

public String getTemplateByDocType(String docType)

Specified by:
`getTemplateByDocType` in interface `JBakeConfiguration`

  - 

### getTemplateFileByDocType

public File getTemplateFileByDocType(String docType)

Specified by:
`getTemplateFileByDocType` in interface `JBakeConfiguration`

  - 

### getTemplateFolder

public File getTemplateFolder()

Specified by:
`getTemplateFolder` in interface `JBakeConfiguration`
Returns:
the template folder

  - 

### setTemplateFolder

public void setTemplateFolder(File templateFolder)

  - 

### getTemplateFolderName

public String getTemplateFolderName()

Specified by:
`getTemplateFolderName` in interface `JBakeConfiguration`
Returns:
name of folder where template files are looked for

  - 

### getThymeleafLocale

public String getThymeleafLocale()

Specified by:
`getThymeleafLocale` in interface `JBakeConfiguration`
Returns:
Locale used for Thymeleaf template rendering

  - 

### getUriWithoutExtension

public boolean getUriWithoutExtension()

Specified by:
`getUriWithoutExtension` in interface `JBakeConfiguration`
Returns:
Flag indicating if content matching prefix below should be given extension-less URI's

  - 

### setUriWithoutExtension

public void setUriWithoutExtension(boolean withoutExtension)

  - 

### getVersion

public String getVersion()

Specified by:
`getVersion` in interface `JBakeConfiguration`
Returns:
Version of JBake

  - 

### setDestinationFolderName

public void setDestinationFolderName(String folderName)

  - 

### setExampleProject

public void setExampleProject(String type,
 String fileName)

  - 

### setProperty

public void setProperty(String key,
 Object value)
Description copied from interface: `JBakeConfiguration`
Set a property value for the given key

Specified by:
`setProperty` in interface `JBakeConfiguration`
Parameters:
`key` - the key for the property
`value` - the value of the property

  - 

### getThymeleafModeByType

public String getThymeleafModeByType(String type)

Specified by:
`getThymeleafModeByType` in interface `JBakeConfiguration`
Parameters:
`type` - the documents type
Returns:
the the thymeleaf render mode ( defaults to `DEFAULT_TYHMELEAF_TEMPLATE_MODE` )

  - 

### getServerContextPath

public String getServerContextPath()

Specified by:
`getServerContextPath` in interface `JBakeConfiguration`

  - 

### getServerHostname

public String getServerHostname()

Specified by:
`getServerHostname` in interface `JBakeConfiguration`

  - 

### asHashMap

public Map<String,Object> asHashMap()

Specified by:
`asHashMap` in interface `JBakeConfiguration`

  - 

### setTemplateExtensionForDocType

public void setTemplateExtensionForDocType(String docType,
 String extension)

  - 

### setTemplateFileNameForDocType

public void setTemplateFileNameForDocType(String docType,
 String fileName)

  - 

### getHeaderSeparator

public String getHeaderSeparator()

Specified by:
`getHeaderSeparator` in interface `JBakeConfiguration`
Returns:
String used to separate the header from the body

  - 

### setHeaderSeparator

public void setHeaderSeparator(String headerSeparator)

  - 

### getImgPathPrependHost

public boolean getImgPathPrependHost()

Specified by:
`getImgPathPrependHost` in interface `JBakeConfiguration`
Returns:
Flag indicating if image paths should be prepended with `JBakeConfiguration.getSiteHost()` value - only has an effect if
 `JBakeConfiguration.getImgPathUpdate()` is set to true

  - 

### setImgPathPrependHost

public void setImgPathPrependHost(boolean imgPathPrependHost)

  - 

### getImgPathUpdate

public boolean getImgPathUpdate()

Specified by:
`getImgPathUpdate` in interface `JBakeConfiguration`
Returns:
Flag indicating if image paths in content should be updated with absolute path (using URI value of content file),
 see `JBakeConfiguration.getImgPathUpdate()` which allows you to control the absolute path used

  - 

### setImgPathUPdate

public void setImgPathUPdate(boolean imgPathUpdate)

  - 

### getJbakeProperties

public List<Property> getJbakeProperties()

Specified by:
`getJbakeProperties` in interface `JBakeConfiguration`

  - 

### addConfiguration

public void addConfiguration(Properties properties)

Specified by:
`addConfiguration` in interface `JBakeConfiguration`

  - 

### getAbbreviatedGitHash

public String getAbbreviatedGitHash()

Specified by:
`getAbbreviatedGitHash` in interface `JBakeConfiguration`
Returns:
Abbreviated hash of latest git commit

  - 

### getJvmLocale

public String getJvmLocale()

Specified by:
`getJvmLocale` in interface `JBakeConfiguration`
Returns:
Locale to set in the JVM

  - 

### getFreemarkerTimeZone

public TimeZone getFreemarkerTimeZone()

Specified by:
`getFreemarkerTimeZone` in interface `JBakeConfiguration`
Returns:
TimeZone to use within Freemarker