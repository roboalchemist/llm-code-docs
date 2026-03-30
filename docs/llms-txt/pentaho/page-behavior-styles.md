# Source: https://docs.pentaho.com/pba-report-designer/style-properties-reference/page-behavior-styles.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/style-properties-reference/page-behavior-styles.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/style-properties-reference/page-behavior-styles.md

# Page Behavior styles

**Page Behavior** styles control page display and rendering properties of the selected element when publishing to a page-aware file format.

| Property Name             | Data Type | Purpose                                                                                                                                 |
| ------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **display-on-first-page** | Boolean   | (Band elements only) If `true`, only displays this band on the first page                                                               |
| **display-on-last-page**  | Boolean   | (Band elements only) If `true`, only displays this band on the last page                                                                |
| **repeat-header**         | Boolean   | (Header and footer elements only) If `true`, repeats this header or footer on every printed page                                        |
| **page-break-after**      | Boolean   | If `true`, a page break will occur after this element                                                                                   |
| **page-break-before**     | Boolean   | If `true`, a page break will occur before this element                                                                                  |
| **sticky**                | Boolean   | If `true`, imports page-header/footer and the repeated group-header/footer from the master report into sub-reports                      |
| **avoid-page-break**      | Boolean   | If `true`, cancels a predefined (through a formula or function) page break                                                              |
| **orphan**                | Integer   | Defines the minimum number of elements or lines at end of the page before a page break can occur within the band or paragraph           |
| **widows**                | Integer   | Defines the minimum number of elements or lines at the beginning of the page before a page break can occur within the band or paragraph |
