lopdf
# Struct FontData 
Source 

```
pub struct FontData {
    pub font_name: String,
    pub flags: i64,
    pub font_bbox: (i64, i64, i64, i64),
    pub italic_angle: i64,
    pub ascent: i64,
    pub descent: i64,
    pub cap_height: i64,
    pub stem_v: i64,
    pub encoding: String,
    /* private fields */
}
```

## Fields§
§`font_name: String`

(Required) The PostScript name of the font. This should be the same as the value of BaseFont in the font or CIDFont dictionary that refers to this font descriptor.
§`flags: i64`

(Required) A collection of flags defining various characteristics of the font.
§`font_bbox: (i64, i64, i64, i64)`

(Required, except for Type 3 fonts) A rectangle (see Section 3.8.4, “Rectangles”), expressed in the glyph coordinate system, specifying the font bounding box. This is the smallest rectangle enclosing the shape that would result if all of the glyphs of the font were placed with their origins coincident and then filled.
Format as: (x_min, y_min, x_max, y_max).
§`italic_angle: i64`

(Required) The angle, expressed in degrees counterclockwise from the vertical, of the dominant vertical strokes of the font. (For example, the 9-o’clock position is 90 degrees, and the 3-o’clock position is –90 degrees.) The value is negative for fonts that slope to the right, as almost all italic fonts do.
§`ascent: i64`

(Required, except for Type 3 fonts) The maximum height above the baseline reached by glyphs in this font, excluding the height of glyphs for accentedc haracters.
§`descent: i64`

(Required, except for Type 3 fonts) The maximum depth below the baseline reached by glyphs in this font. The value is a negative number.
§`cap_height: i64`

(Required for fonts that have Latin characters, except for Type 3 fonts) The vertical coordinate of the top of flat capital letters, measured from the baseline.
§`stem_v: i64`

(Required, except for Type 3 fonts) The thickness, measured horizontally, of the dominant vertical stems of glyphs in the font.
§`encoding: String`

(Required) The name of a predefined CMap, or a stream containing a CMap program, that maps character codes to font numbers and CIDs. If the descendant is a Type 2 CIDFont whose associated TrueType font program is not embedded in the PDF file, the Encoding entry must be a predefined CMap name
Read more (page 422): https://opensource.adobe.com/dc-acrobat-sdk-docs/pdfstandards/pdfreference1.5_v6.pdf

## Implementations§