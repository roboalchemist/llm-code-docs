# Source: https://docs.pentaho.com/pdia-admin/administer/manage-the-pentaho-system/localize-folders-and-reports.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/manage-the-pentaho-system/localize-folders-and-reports.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/manage-the-pentaho-system/localize-folders-and-reports.md

# Localize Folders and Reports

You can localize the names and descriptions for reports and folders that appear in the User Console. Localization is helpful if your co-workers work in different countries and speak different languages, but use the console to access the same reports and folders. For example, localization allows German speakers to view report names in German and Americans to view the same report names in English.

**Note:** Localization language packs have been created through a community initiative that uses an installer built by Webdetails, a Pentaho company. The language packs apply to both EE and CE, and are maintained by community members. The packs are not officially supported by Pentaho.

Localization information is stored in the Pentaho Repository, along with other report and folder information. Typically, to localize names and descriptions of reports and folders you do three things:

1. Download the report or folder from the Pentaho Repository. Localization information is stored in one or more text files that have the `.locale` extension.
2. Add or edit the localization files downloaded with the reports or folders.
3. Re-upload the report or folder, along with the localization files, into the Pentaho Repository.

## Localization file structure

When you download a report or folder from the Pentaho Repository, localization information is stored in a text file that has a `.locale` extension. You add or edit localization files, but must upload them to the Pentaho Repository for the changes to appear in the User Console.

Each report and folder that appears in the console should have a default localization file associated with it. The default localization file should indicate the name that appears when you view the name of the report or folder in the console. Optionally, the localization file can contain the report description. The report description appears when you hover the mouse pointer over the report or folder name in the console.

If multiple localization files are present, the User Console displays the localization information contained in them if you set the language indicated in the localization file as the default in the console or in your web browser. Otherwise, the information in the default localization file is displayed instead.

Localization information appears in two places in a localization file: in the file name and in variables inside the file.

### Localization file names

Localization file names consist of several parts that are joined by underscores. This is an example of a localization file name for a folder: `index_es_PA.locale`

In folder localization, file names the word `index` appears first, as in the previous example. If the localization file is for a report, the name of the report appears instead of index, like this: `Inventory Report_es_PA.prpt.locale`

The second and third parts of the file name indicate the two-letter language code and the two-letter country code. Language codes adhere to ISO 639-1; country codes can be found in ISO-3166. In the previous example, `es` is the language code for Spanish and `PA` is the country code for Panama. A list of often-used language and country codes appears here.

Although rarely used, the dialect code can appear after the country code.

File extensions, which appear after the period, indicate the report type and end with: `.locale` In the previous example `prpt` indicates the report type.

Language, country, and dialect codes are optional parts of file names. The report type extension should not be included in folder localization file names. Only the report name (or the word index for folders) is required as is the `.locale` extension. But, if a country code is present, the language code must also be present, and if a dialect code is present, both the language and country codes must be present.

If a localization file name contains no language, country, or dialect code, the console assumes that the file is the default for a report or folder. A default localization file name for a folder looks like this: `index.locale`

### Localization variables

Localization files have at least two variables that contain localization information.

* *file.title* holds the name of the report or folder that appears in the User Console.
* *file.description* holds the text for the Tool Tip that appears when you hover the mouse pointer over the report or folder name in the User Console.

Here is an example of a localization file for a report.

```
#Locale = es
#Wed Apr 17 13:55:53 EDT 2013
file.title=Inventario Region 23
file.description=Lista del inventario de la región 23
```

**Note:** In localization `.properties` files, *file.name* and *file.url-name* are sometimes used instead of *file.title* and *url-description* is sometimes used instead of the *file.description* variable.

Before variable values set in the localization file can be displayed, you must adjust either the User Console or your web browser’s language so that it matches the localization file’s language. You must also upload the localization file into the Pentaho Repository along with the other report files.

Using the previous example, the User Console displays the value of **file.title** (`Inventario Region 23`) when you open it. If you hover the mouse pointer over the report name in the console, a Tool Tip appears that displays the value of **file.description** (`Lista del inventario de la region 23`).

**Note:** Unicode can be used to display non-Latin languages, such as Chinese or Japanese.

### Popularly used country and location codes

Language and country codes that are used to construct localization file names appear in standards ISO 639-1 and ISO 3166. Here is a list of popularly used language and country codes.

| Lanuage    | Language Code | Country           | Country Code |
| ---------- | ------------- | ----------------- | ------------ |
| Chinese    | zh            | China             | CN           |
| Dutch      | nl            | Netherlands       | NL           |
| French     | fr            | France            | FR           |
| German     | de            | Germany           | DE           |
| Italian    | it            | Italy             | IT           |
| Japanese   | ja            | Japan             | JP           |
| Korean     | ko            | Republic of Korea | KR           |
| Portuguese | pt            | Brazil            | BR           |
| Portuguese | pt            | Portugal          | PT           |
| Spanish    | es            | Argentina         | AR           |
| Spanish    | es            | Spain             | ES           |

## Set default localization for reports and folders

Complete these steps if you want to set up default localization information.

1. Download the report or folder to which you want to add localization information.

   Instructions for how to do this appear in [Download folders and files](https://docs.pentaho.com/pdia-admin/10.2-admin/manage-the-pentaho-repository/upload-and-download-from-the-pentaho-repository#download-folders-and-files).
2. Unzip the downloaded report or folder, then determine whether a default localization file already exists.

   Localization files have a `.local` extension and are named either `index.locale` (for folders) or `<report name>.<report type>.locale` for reports. If a default localization file exists you do not need to continue with these steps.
3. To add new localization information, you must create a default localization file. Localization file names follow very specific naming conventions. To determine the name of the new localization file, do this.
   1. For folders, the default localization file name convention is: `index.locale`
   2. For reports, the default localization file name convention is: `<report name>.<report type>.locale`

      An example of a valid file name is: `Inventory Report.prpt.locale`
4. Use a text editor to create a blank localization file that has the file name you constructed in the previous step, then save the file in the directory of the folder or report.
5. Type the following in the blank file:

   ```
   #Localization File 
   file.title= 
   file.description=
   ```
6. Type the name of the report or folder that you want to appear in the User Console after the *file.title=* variable.

   Type the name of the report or folder exactly as you want it to appear.

   *file.title=*`Inventario`
7. Type the description for the report or folder after the *file.description* variable.

   The value of the *file.description=* appears when you hover the mouse pointer over the report or folder name in the User Console. Type the description exactly as you want it to appear.

   *file.description=*`Inventario para El Rey`
8. Save and close the file.
9. Upload the localization file along with other report or folder files into the Pentaho Repository.

   Instructions for how to do this appear in [Upload folders and files](https://docs.pentaho.com/pdia-admin/10.2-admin/manage-the-pentaho-repository/upload-and-download-from-the-pentaho-repository#upload-folders-and-files).

## Localize for additional languages

Complete these steps if you want to display report and folder names and descriptions in a language other than the default. If you want to change the default language displayed only, we recommend that you edit the default locale file.

1. Download the report or folder to which you want to add localization information.

   Instructions for how to do this appear in [Download folders and files](https://docs.pentaho.com/pdia-admin/10.2-admin/manage-the-pentaho-repository/upload-and-download-from-the-pentaho-repository#download-folders-and-files).
2. Unzip the downloaded report or folder.
3. To add new localization information, you must create a new localization file.

   Localization file names follow very specific naming conventions. You can optionally specify country and language codes, as well as the report type. To determine the name of the new localization file, do this.

   1. For folders, the localization file name convention is: `index_<language code>_<country code>.locale`

      An example of a valid file name is: `index_es_PA.locale`

      **Note:** Language and country codes are optional.
   2. For reports, the localization file name convention is: `<report name>_<language code>_<country code>.<report type>.locale`

      An example of a valid file name is: `Inventory Report_es_PA.prpt.locale`

      **Note:** Language and country codes are optional.
4. Use a text editor to create a blank localization file that has the file name you constructed in the previous step, then save the file in the directory of the folder or report.
5. Type the following in the blank file.

   ```
   #Localization File 
   file.title= 
   file.description=
   ```
6. Type the name of the report or folder that you want to appear in the User Console after the *file.title=* variable.

   Type the name of the report or folder exactly as you want it to appear.

   *file.title=*`Inventario`
7. Type the description for the report or folder after the *file.description* variable.

   The value of the *file.description=* appears when you hover the mouse pointer over the report or folder name in the User Console. Type the description exactly as you want it to appear.

   *file.description=*`Inventario para El Rey`
8. Save and close the file.
9. Upload the localization file along with other report or folder files into the Pentaho Repository.

   Instructions for how to do this appear in [Upload folders and files](https://docs.pentaho.com/pdia-admin/10.2-admin/manage-the-pentaho-repository/upload-and-download-from-the-pentaho-repository#upload-folders-and-files).

## Edit existing localization information

Complete these steps if you want to edit localization information for report and folder names and descriptions that appear in the User Console.

1. Download the report or folder for which you want to edit localization information.

   Instructions for how to do this appear in [Download folders and files](https://docs.pentaho.com/pdia-admin/10.2-admin/manage-the-pentaho-repository/upload-and-download-from-the-pentaho-repository#download-folders-and-files).
2. Unzip the downloaded report or folder.
3. Use a text editor to open the localization file you want to modify.

   Localization files have the `.local` extension. Localization files for folders begin with the word: `index` Localization files for reports begin with the report name.
4. To change the report or folder name that appears in the User Console, edit the *file.title=* variable.

   *file.title=*`Inventario`
5. To change the report or folder description Tool Tip that appears when you hover the mouse pointer over the report or folder name in the User Console, edit the value of the *file.description=* variable.

   *file.description=*`Inventario para El Rey`
6. Save and close the file.
7. Re-upload the localization file, along with the other report or folder files, into the Pentaho Repository.

   Instructions for how to do this appear in [Upload folders and files](https://docs.pentaho.com/pdia-admin/10.2-admin/manage-the-pentaho-repository/upload-and-download-from-the-pentaho-repository#upload-folders-and-files).
