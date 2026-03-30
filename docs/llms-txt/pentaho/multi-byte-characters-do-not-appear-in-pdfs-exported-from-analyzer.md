# Source: https://docs.pentaho.com/pba/9.3-analytics/analysis-issues/multi-byte-characters-do-not-appear-in-pdfs-exported-from-analyzer.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/analysis-issues/multi-byte-characters-do-not-appear-in-pdfs-exported-from-analyzer.md

# Multi-byte characters do not appear in PDFs exported from Analyzer

If you are using a multi-byte character set, such as would be used for languages like Japanese or Chinese, and find that you have missing or corrupted output when exporting Analyzer reports to PDF, you will have to specify a default TrueType font for PDF rendering that supports multi-byte characters. The default PDF font in Analyzer is Helvetica, which does not support multi-byte character sets.

When displaying data in Analyzer, your reports will use the default browser fonts. However, the PDF export function may not have the same fonts available when creating a PDF from your Analyzer report. The resulting output will not look the same in PDF as it did in the browser. The default font for PDF is Helvetica, but you can specify any TrueType font or collection to replace it using the following instructions:

1. Stop the Pentaho Server and User Console.
2. Edit the `analyzer.properties` file in the `/pentaho/server/pentaho-server/pentaho-solutions/system/analyzer/` folder.
3. Uncomment the `renderer.pdf.font.path` line, as shown in the following sample line of code:

   ```
   renderer.pdf.font.path=C:/WINDOWS/Fonts/MSGOTHIC.TTC,1
   ```
4. Replace the value of this line with the TrueType font or collection that you want to use as the default. If you are specifying a collection, you must put a `,1` after the font name, as shown in the above example. This does not apply to individual fonts (TTF files).

   ```
   renderer.pdf.font.path=/usr/share/fonts/truetype/freefont/FreeSans.ttf
   ```
5. Save and close the file, and start the Pentaho Server.
