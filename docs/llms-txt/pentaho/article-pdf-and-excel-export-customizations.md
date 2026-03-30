# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/customize-pentaho-products-cp/customize-pentaho-analyzer/article-pdf-and-excel-export-customizations.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/customize-pentaho-products-cp/customize-pentaho-analyzer/article-pdf-and-excel-export-customizations.md

# PDF and Excel export customizations

Analyzer allows you to customize the appearance and content of your PDF and Excel outputs.

The complete list of properties that you can change are in the file comments. You can find the file here at `server/pentaho-server/pentaho-solutions/system/analyzer/analyzer.properties`.

You can test your customizations to `analyzer.properties` in real time by refreshing the cache for the Analyzer report you are modifying using the **More actions and options** > **Administration** > **Clear Cache** menu action.

You can customize the appearance of your company's PDF and Excel exports from Analyzer in a number of ways. For example, Analyzer PDF exports can be personalized with a company logo and a cover page, and you can change the default font used to generate PDFs.

## Customizing the PDF cover page

You can customize the PDF cover page with the following `analyzer.properties`.

| Property                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **renderer.pdf.cover.hide**  | Generates the PDF export without a cover page. (Default value: `false`)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **renderer.pdf.cover.image** | <p>Generates the PDF export with a custom cover image. The gray boxes in the title background of the report’s cover page can be hidden by setting <strong>renderer.pdf.cover.hideTitleBackground</strong><code>=true</code>. When the background is hidden, the title font color is black instead of white.</p><p>The cover image is anchored in the bottom left corner of the page. The image is not scaled based on the export page size. Specify the file name of the image and type, no path, and place the image file in the <code>/pentaho-solutions/system/analyzer/resources</code> directory.</p><p>If you want to design a cover page with a specific page size and image orientation, then you can override the default <strong>renderer.pdf.cover.image</strong>. For each page size and orientation (see below), the provided image width and height completely fill the cover page. When setting the property to use for the size and orientation, you should replace the “width x height” value in the property with the file name and type of the image, for example <strong>renderer.pdf.cover.image.letter.landscape</strong><code>= my\_favorite\_image.jpg</code>.</p><ul><li><strong>renderer.pdf.cover.image.letter.landscape=792x612</strong></li><li><strong>renderer.pdf.cover.image.letter.portrait=612x792</strong></li><li><strong>renderer.pdf.cover.image.legal.landscape=1008x612</strong></li><li><strong>renderer.pdf.cover.image.legal.portrait=612x1008</strong></li><li><strong>renderer.pdf.cover.image.note.landscape=720x540</strong></li><li><strong>renderer.pdf.cover.image.note.portrait=540x720</strong></li><li><strong>renderer.pdf.cover.image.tabloid.landscape=1224x792</strong></li><li><strong>renderer.pdf.cover.image.tabloid.portrait=792x1224</strong></li><li><strong>renderer.pdf.cover.image.ledger.landscape=792x1224</strong></li><li><strong>renderer.pdf.cover.image.ledger.portrait=1224x792</strong></li><li><strong>renderer.pdf.cover.image.postcard.landscape=416x283</strong></li><li><strong>renderer.pdf.cover.image.postcard.portrait=283x416</strong></li><li><strong>renderer.pdf.cover.image.executive.landscape=756x283</strong></li><li><strong>renderer.pdf.cover.image.executive.portrait=522x756</strong></li><li><strong>renderer.pdf.cover.image.a3.landscape=1191x842</strong></li><li><strong>renderer.pdf.cover.image.a3.portrait=842x1191</strong></li><li><strong>renderer.pdf.cover.image.a4.landscape=842x595</strong></li><li><strong>renderer.pdf.cover.image.a4.portrait=595x842</strong></li><li><strong>renderer.pdf.cover.image.a5.landscape=595x420</strong></li><li><strong>renderer.pdf.cover.image.a5.portrait=420x595</strong></li><li><strong>renderer.pdf.cover.image.b4.landscape=1000x708</strong></li><li><strong>renderer.pdf.cover.image.b4.portrait=708x1000</strong></li><li><strong>renderer.pdf.cover.image.b5.landscape=708x498</strong></li><li><strong>renderer.pdf.cover.image.b5.portrait=498x708</strong></li></ul> |

## Customizing the PDF logo

You can customize the PDF logo with the following `analyzer.properties`.

| Property                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **renderer.logo.image**             | <p>Adds a custom logo image to a PDF export. The logo image is placed on the bottom left corner of every page. This image should have no padding and a white background. If the PDF includes a cover page, the logo is placed bottom center on that page. You need to specify the image file name and type, no path, and place the image file in the <code>/pentaho-solutions/system/analyzer/resources/</code> directory.If you want to set a logo image specific to a page size, then you can override the <strong>default renderer.logo.image</strong> property with the desired size value:</p><ul><li><strong>renderer.logo.image.letter</strong></li><li><strong>renderer.logo.image.legal</strong></li><li><strong>renderer.logo.image.note</strong></li><li><strong>renderer.logo.image.tabloid</strong></li><li><strong>renderer.logo.image.ledger</strong></li><li><strong>renderer.logo.image.postcard</strong></li><li><strong>renderer.logo.image.executive</strong></li><li><strong>renderer.logo.image.a3</strong></li><li><strong>renderer.logo.image.a4</strong></li><li><strong>renderer.logo.image.a5</strong></li><li><strong>renderer.logo.image.b4</strong></li><li><strong>renderer.logo.image.b5</strong></li></ul> |
| **renderer.logo.image.hideOnCover** | Hides the logo on the cover page when set to `true`. Useful when the cover page already includes a custom background image. (Default value: `false`)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

## Set default fonts for PDF export

When displaying data in Analyzer, your reports will use the default browser fonts. However, the PDF export function may not have the same fonts available to it when creating a PDF from your Analyzer report, resulting in output that doesn't look the same way in PDF format as it does in the browser. The default font for PDFs is Helvetica, but you can specify any TrueType font or collection to replace it. Follow the instructions below to specify a different font for PDF exports.

**Note:** If you have localized your schema in a language that uses a multi-byte character set (most Asian languages fit into this category), this process is required to make PDF output appear without errors.

1. Stop the Pentaho User Console and Pentaho Server.
2. Navigate to the `pentaho/server/pentaho-server/pentaho-solutions/system/analyzer/` directory and open the `analyzer.properties` file with any text editor.
3. Uncomment the **renderer.pdf.font.path** line.

   ```
   renderer.pdf.font.path=C:/WINDOWS/Fonts/MSGOTHIC.TTC,1
   ```
4. Replace the value of this line with the `TrueType` font or collection that you want to use as the default. If you are specifying a collection, you must put a `,1` after the font name, as shown in the above example. This does not apply to individual fonts (TTF files).

   ```
   renderer.pdf.font.path=/usr/share/fonts/truetype/freefont/FreeSans.ttf
   ```
5. Save and close the file, and restart the Pentaho Server.

Your PDF exports from Analyzer should have the font you specified.

## Removing report attributes

PDF and Excel exports from Analyzer, by default, include information such as the report creator, report name, folder location, filters used, and fields used. As shown in the table below, you can exclude some or all of this information from an export by setting the value of its property to `true` in `analyzer.properties`.

| Property                                   | Description                                                        |
| ------------------------------------------ | ------------------------------------------------------------------ |
| **renderer.metadata.hide.aboutThisReport** | Removes the “About this report” section. (Default value = `false`) |
| **renderer.metadata.hide.filterSummary**   | Removes the “Filter summary” section. (Default value = `false`)    |
| **renderer.metadata.hide.fieldsUsed**      | Removes the “Fields used” section. (Default value = `false`)       |

You can retain the "About This Report" section and customize the items it contains by setting the value for the associated property, as described in the following table.

| Property                                               | Description                                                       |
| ------------------------------------------------------ | ----------------------------------------------------------------- |
| **renderer.metadata.hide.aboutThisReport.name**\`\`    | Removes the “report name” field. (Default value = `false`)        |
| **renderer.metadata.hide.aboutThisReport.description** | Removes the “report description” field. (Default value = `false`) |
| **renderer.metadata.hide.aboutThisReport.creator**     | Removes the “report creator” field. (Default value = `false`)     |
| **renderer.metadata.hide.aboutThisReport.location**    | Removes the “report location” field. (Default value = `false`)    |
| **renderer.metadata.hide.aboutThisReport.createdOn**   | Removes the “creation date” field. (Default value = `false`)      |
| **renderer.metadata.hide.aboutThisReport.cube**        | Removes the “cube annotation” field. (Default value = `false`)    |

## Removing a data table and report worksheet

PDF and Excel exports of an Analyzer chart report, by default, also include a data table and report worksheet. You can exclude the data table and / or the report worksheet from PDF and Excel exports of a chart report by setting the value of the associated property to `true`, as described in the following table.

| Property                          | Description                                                                                                   |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **renderer.pdf.dataTable.hide**   | Excludes the data table from a chart report exported to PDF. (Default value = `false`)                        |
| **renderer.excel.dataTable.hide** | Excludes the data table and report worksheet from a chart report exported to Excel. (Default value = `false`) |

## Creating custom headers and footers

Headers and footers can be customized to include static text such as disclaimers and copyright information, or dynamic text such as the current user and date. These header and footer templates, defined in Analyzer's resource message files, can be localized into different languages. Analyzer's resource message files are in the `pentaho-solutions/system/analyzer/resources` directory. The base resources file is `messages.properties`. The table below describes each message file.

**Note:** For testing custom headers and footers, you can set `localizationService.cache.resource.bundle=false` in the `analyzer.properties` file for immediate pickup by Analyzer of changes to the `message*.properties` files. For performance reasons, this setting should only be performed in development environments.

| Message file                    | Description                                                                                                       |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **RendererPDFHeaderTemplate**   | Header template that appears in top-left corner of a PDF. (Default value = `%report`)                             |
| **RendererPDFFooterTemplate**   | Footer template that appears in bottom-right corner of a PDF. (Default value = `Page %pageCurrent of %pageTotal`) |
| **RendererExcelHeaderTemplate** | Header template that appears on the first line of each Excel worksheet.                                           |
| **RendererExcelFooterTemplate** | Footer template that appears after the content on each Excel worksheet.                                           |

When a PDF and Excel export is generated, the tokens described in the table below are replaced in the template text.

| Token          | Description                               |
| -------------- | ----------------------------------------- |
| `%report`      | Current report name.                      |
| `%user`        | Username of session exporting the report. |
| `%date`        | Date and time when report was exported.   |
| `%pageCurrent` | Current page number (PDF only).           |
| `%pageTotal`   | Total page number (PDF only).             |

## Theming a pivot table

If you modify the system theme or add a new theme that changes the styles on the HTML pivot table, the PDF and Excel pivot tables can inherit the same background and font colors. To enable this feature, `renderer.dataTable.inheritTheme` must be set to `true` in `analyzer.properties`.

The following pivot table items can be themed in PDF and Excel exports.

![Pivot table items](https://3256662623-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTSPdUdWBWVGi0uurnXBG%2Fuploads%2Fgit-blob-1948c5aac68f36ce3b8e0a11618c45041dd4e00f%2FPDI_Analyzer_Pivot_Table_example.png?alt=media)

When generating the PDF or Excel export, the following CSS rule sets are used by the theme-specific CSS file to customize the pivot table.

| Number                                                                                                                       | Pivot table item              | CSS selector                                                     | CSS declarations A                  | Example                                                |
| ---------------------------------------------------------------------------------------------------------------------------- | ----------------------------- | ---------------------------------------------------------------- | ----------------------------------- | ------------------------------------------------------ |
| 1                                                                                                                            | Level headers                 | <p>.pivotTable</p><p>.columnHeaders</p><p>.columnheading</p>     | <p>background-color</p><p>color</p> | <p>Education Level</p><p>Name</p><p>Product Family</p> |
| 2                                                                                                                            | Level member property headers | <p>.pivotTable</p><p>.columnHeaders</p><p>.columnPropHeading</p> | <p>background-color</p><p>color</p> | Yearly Income                                          |
| 3                                                                                                                            | Measure headers               | <p>.pivotTable</p><p>.columnHeaders</p><p>.metric</p>            | <p>background-color</p><p>color</p> | Unit Sales                                             |
| 4                                                                                                                            | Level members                 | <p>.pivotTable</p><p>.columnHeaders</p><p>.member</p>            | background-color                    | <p>Graduate Degree</p><p>Food</p><p>1997</p>           |
| 5                                                                                                                            | Total members and cells       | <p>.pivotTable</p><p>.cells</p><p>.colSubTotal</p>               | background-color                    | Cells under Graduate Degree Total and Food Total       |
| 6                                                                                                                            | Grand total cells             | <p>.pivotTable</p><p>.cells</p><p>.colGrandTotal</p>             | background-color                    | Cells under Grand Total                                |
| A CSS declarations for background-color and color must be specified using hex notation, such as `#FF0000` for the color red. |                               |                                                                  |                                     |                                                        |

The example below shows a pivot table that was themed by modifying the ruby theme in the \`pentaho-solutions/system/analyzer/styles/themes/ruby/anaRuby.css\` file.

![Pivot table Ruby theme](https://3256662623-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTSPdUdWBWVGi0uurnXBG%2Fuploads%2Fgit-blob-8bb4f3d10a94a860baeaf17650c00142b16cf87a%2FPDI_Analyzer_Pivot_Table_Ruby.png?alt=media)

If you are customizing the HTML pivot table, use the following reference which lists the corresponding CSS selectors for each pivot table item. Many of these items also support `:hover` selection style changes. The CSS rule sets used to style the PDF and Excel pivot tables are a subset of the CSS selectors listed below.

**Note:** When styling the HTML pivot table, static resources such as CSS files are cached in the Pentaho Server. You can temporarily disable this caching by setting `<cache>` to `false` in the `pentaho-solutions\system\analyzer\settings.xml` file.

| Number | Pivot table item              | CSS selectors                                                                                                                                                                                                         |
| ------ | ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1      | Level headers                 | <p>.pivotTable</p><p>.columnHeaders</p><p>.columnheading</p><p>.pivotTable</p><p>.rowLabelHeaders TD</p>                                                                                                              |
| 2      | Level member property headers | <p>.pivotTable</p><p>.columnHeaders</p><p>.columnPropHeading</p><p>.pivotTable</p><p>.rowLabelHeaders</p><p>.rowPropHeader</p>                                                                                        |
| 3      | Measure headers               | <p>.pivotTable</p><p>.columnHeaders</p><p>.metric</p>                                                                                                                                                                 |
| 4      | Level members                 | <p>.pivotTable</p><p>.columnHeaders</p><p>.member</p><p>.pivotTable</p><p>.rowHeaders</p><p>.inner</p><p>.pivotTable</p><p>.rowHeaders</p><p>.outer</p>                                                               |
| 5      | Total members and cells       | <p>.pivotTable</p><p>.columnHeaders</p><p>.memberSubTotal</p><p>.pivotTable</p><p>.rowHeaders</p><p>.subTotal</p><p>.pivotTable</p><p>.cells</p><p>.colSubTotal</p><p>.pivotTable</p><p>.cells</p><p>.rowSubTotal</p> |
| 6      | Grand total cells             | <p>.pivotTable</p><p>.cells</p><p>.colGrandTotal</p>                                                                                                                                                                  |

### Set pivot table minimum font size

When rendering the pivot table for PDF export, Analyzer attempts to fit the complete width of the table onto a single page using a size 9 font. If the table cannot fit the page using the size 9 font, then progressively smaller font sizes fonts are automatically attempted, down to a lower default limit of 3. To set a higher minimum font size and avoid the need to use PDF zoom functions to read the table, you can override this property.

1. Navigate to the `pentaho/server/pentaho-server/pentaho-solutions/system/analyzer/` directory and open the `analyzer.properties` file with any text editor.
2. Locate **renderer.pdf.font.table.min**.

   `renderer.pdf.font.table.minSize=3`
3. Replace the value with the smallest font size that you want used for exported pivot tables.
4. Save and close the file.
5. Test your changes by refreshing the cache or by restarting the Pentaho Server.

Your pivot tables exported to PDF from Analyzer will use text with the minimum font size.

## Customize the logo on Excel exports

You can add a custom logo to your Excel exports from Analyzer. The image is placed after the content on each worksheet.

To add a custom logo, follow the steps below.

1. Navigate to the `pentaho/server/pentaho-server/pentaho-solutions/system/analyzer/` directory and open the `analyzer.properties` file with any text editor.
2. Locate **renderer.excel.logo.image**

   `renderer.excel.logo.image=`
3. Specify the image file name and type, with no path.

   For example, `my_favorite_logo.jpg`
4. Place the image file in the `/pentaho-solutions/system/analyzer/resources/` directory.
5. Save and close the file.
6. Test your changes by refreshing the cache or by restarting the Pentaho Server.

Your Excel exports from Analyzer will now contain the logo.

## Customize the font on Excel exports

You can set the font used for your Excel exports from Analyzer.

To change the font, follow the steps below.

**Note:** The font used with Excel reports must be accessible by the Java virtual machine or operating system.

1. Navigate to the `pentaho/server/pentaho-server/pentaho-solutions/system/analyzer/` directory and open the `analyzer.properties` file with any text editor.
2. Locate **renderer.excel.font.name**.

   `renderer.excel.font.name=Verdana`
3. Specify the name of the font.

   (Default `= Verdana`
4. Save and close the file.
5. Test your changes by refreshing the cache or by restarting the Pentaho Server.

Your Excel exports from Analyzer will now use the font.
