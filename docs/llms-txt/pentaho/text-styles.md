# Source: https://docs.pentaho.com/pba-report-designer/style-properties-reference/text-styles.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/style-properties-reference/text-styles.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/style-properties-reference/text-styles.md

# Text styles

**Text** styles control the font and font properties pertaining to the text of the selected element.

**Note:** For elements that control colors, possible values are standard HTML color names (red, blue, green, black, etc.) or hexadecimal color values (#000000, #FFFFFF, #CCFF00, etc.)

| Property Name       | Data Type | Purpose                                                                                                         |
| ------------------- | --------- | --------------------------------------------------------------------------------------------------------------- |
| **h-align**         | Selection | Horizontally aligns the selected content within this element                                                    |
| **v-align**         | Selection | Vertically aligns the selected content within this element                                                      |
| **v-align-in-band** | Selection | An extended text-alignment that allows fine control on how **inline-text** is aligned within a line             |
| **text-wrap**       | Boolean   | A flag indicating whether text will automatically wrap at the end of the line                                   |
| **text-color**      | Selection | The text (foreground) color.                                                                                    |
| **bg-color**        | Selection | The element's background color.                                                                                 |
| **line-height**     | Integer   | Defines the height of a single text line. Is always greater or equal to the font size                           |
| **overflow-text**   | String    | A text quote that is printed if the given text does not fully fit into the element bound                        |
| **trim**            | Boolean   | A flag indicating whether leading and trailing white spaces will be removed                                     |
| **trim-whitespace** | Selection | Controls how the renderer treats white spaces                                                                   |
| **bg-ext**          | String    | An extended foreground paint **property. Expert** option                                                        |
| **encoding**        | Boolean   | Specifies the target **text-encoding** for the given field, in case the output supports **per-field** encodings |
