# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/r-t-l.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/r-t-l.md

# R t l in JavaScript (ES5) Document editor control

Document Editor provides RTL (right-to-left) support. This can be enabled using the âenableRtlâ property.

{% tabs %}
{% highlight js tabtitle="index.js" %}
ej.base.L10n.load({
    'ar-AE': {
        'documenteditor': {
            'Table': 'ÙØ¬Ø¯ÙÙ',
            'Row': 'ÙØµÙ',
            'Cell': 'Ø§ÙØ®ÙÙÙ',
            'Ok': 'ÙÙØ§ÙÙ',
            'Cancel': 'Ø¥ÙØºØ§Ø¡ Ø§ÙØ£ÙØ±',
            'Size': 'Ø­Ø¬Ù',
            'Preferred Width': 'Ø§ÙØ¹Ø±Ø¶ Ø§ÙÙÙØ¶Ù',
            'Points': 'ÙÙØ§Ø·',
            'Percent': 'Ø§ÙÙØ§Ø¦Ù',
            'Measure in': 'Ø§ÙÙÙØ§Ø³ ÙÙ',
            'Alignment': 'ÙØ­Ø§Ø°Ø§Ù',
            'Left': 'ÙÙØ³Ø§Ø±',
            'Center': 'ÙØ±ÙØ²',
            'Right': 'Ø§ÙØ­Ù',
            'Justify': 'ØªØ¨Ø±ÙØ±',
            'Indent from left': 'ÙØ³Ø§ÙØ© Ø¨Ø§Ø¯Ø¦Ù ÙÙ Ø§ÙÙØ³Ø§Ø±',
            'Borders and Shading': 'Ø§ÙØ­Ø¯ÙØ¯ ÙØ§ÙØªØ¸ÙÙÙ',
            'Options': 'Ø®ÙØ§Ø±Ø§Øª',
            'Specify height': 'ØªØ­Ø¯ÙØ¯ Ø§ÙØ§Ø±ØªÙØ§Ø¹',
            'At least': 'Ø§ÙØ§ÙÙ',
            'Exactly': 'ØªÙØ§ÙØ§',
            'Row height is': 'Ø§Ø±ØªÙØ§Ø¹ Ø§ÙØµÙ ÙÙ',
            'Allow row to break across pages': 'Ø§ÙØ³ÙØ§Ø­ Ø¨ÙØµÙ Ø§ÙØµÙ Ø¹Ø¨Ø± Ø§ÙØµÙØ­Ø§Øª',
            'Repeat as header row at the top of each page': 'ØªÙØ±Ø§Ø± ÙØµÙ Ø±Ø§Ø³ ÙÙ Ø§Ø¹ÙÙ ÙÙ ØµÙØ­Ù',
            'Vertical alignment': 'ÙØ­Ø§Ø°Ø§Ø© Ø¹ÙÙØ¯Ù',
            'Top': 'Ø£Ø¹ÙÙ',
            'Bottom': 'Ø§Ø³ÙÙ',
            'Default cell margins': 'ÙÙØ§ÙØ´ Ø§ÙØ®ÙÙØ© Ø§ÙØ§ÙØªØ±Ø§Ø¶ÙØ©',
            'Default cell spacing': 'ØªØ¨Ø§Ø¹Ø¯ Ø§ÙØ®ÙØ§ÙØ§ Ø§ÙØ§ÙØªØ±Ø§Ø¶Ù',
            'Allow spacing between cells': 'Ø§ÙØ³ÙØ§Ø­ Ø¨Ø§ÙØªØ¨Ø§Ø¹Ø¯ Ø¨ÙÙ Ø§ÙØ®ÙØ§ÙØ§',
            'Cell margins': 'ÙÙØ§ÙØ´ Ø§ÙØ®ÙÙØ©',
            'Same as the whole table': 'ÙÙØ³ Ø§ÙØ¬Ø¯ÙÙ Ø¨Ø£ÙÙÙÙ',
            'Borders': 'Ø§ÙØ­Ø¯ÙØ¯',
            'None': 'Ø§Ù',
            'Single': 'ÙØ§Ø­Ø¯',
            'Dot': 'ÙÙØ·Ù',
            'DashSmallGap': 'Ø¯Ø§Ø´Ø³ÙØ¬Ø§Ø¨',
            'DashLargeGap': 'Ø§ÙØ§ØªØ­Ø§Ø¯ Ø§ÙØ®Ø§Øµ',
            'DashDot': 'Ø¯Ø§Ø´Ø¯ÙØª',
            'DashDotDot': 'Ø¯Ø¯ÙØ¯ÙØ¯ÙØª',
            'Double': 'Ø§ÙÙØ± ÙÙØ±Ø§ ÙØ²Ø¯ÙØ¬Ø§',
            'Triple': 'Ø§ÙØ«ÙØ§Ø«Ù',
            'ThinThickSmallGap': 'ÙØ¬ÙÙ ØµØºÙØ±Ù Ø³ÙÙÙÙ Ø±ÙÙÙ',
            'ThickThinSmallGap': 'Ø§ÙÙØ¬ÙØ© Ø§ÙØµØºÙØ±Ø© Ø±ÙÙÙÙ Ø³ÙÙÙÙ',
            'ThinThickThinSmallGap': 'ØµØºÙØ±Ù Ø³ÙÙÙÙ Ø±ÙÙÙÙ Ø§ÙÙØ¬ÙØ© Ø§ÙØµØºÙØ±Ø©',
            'ThinThickMediumGap': 'ÙØ¬ÙÙ ÙØªÙØ³Ø·Ù Ø³ÙÙÙ',
            'ThickThinMediumGap': 'Ø³ÙÙÙÙ Ø§ÙÙØ¬ÙØ© ÙØªÙØ³Ø·Ù Ø±ÙÙÙÙ',
            'ThinThickThinMediumGap': 'Ø±ÙÙÙÙ Ø³ÙÙÙÙ ÙØªÙØ³Ø·Ù Ø§ÙÙØ¬ÙØ©',
            'ThinThickLargeGap': 'Ø§ÙÙØ¬ÙØ© Ø§ÙÙØ¨ÙØ±Ø© Ø±ÙÙÙÙ Ø³ÙÙÙÙ',
            'ThickThinLargeGap': 'ÙØ¬ÙÙ ÙØ¨ÙØ±Ù Ø±ÙÙÙÙ Ø³ÙÙÙ',
            'ThinThickThinLargeGap': 'Ø±ÙÙÙÙ Ø³ÙÙÙÙ Ø§ÙÙØ¬ÙØ© Ø§ÙÙØ¨ÙØ±Ø©',
            'SingleWavy': 'ÙØ§Ø­Ø¯ ÙØ§Ø¦Ø¬',
            'DoubleWavy': 'ÙØ²Ø¯ÙØ¬ ÙØ§Ø¦Ø¬',
            'DashDotStroked': 'Ø§ÙØ¯ÙØ§Ø¹Ù ÙÙØ·Ù Ø§ÙÙÙÙØ©',
            'Emboss3D': 'D3ÙØ²Ø®Ø±Ù',
            'Engrave3D': 'D3ÙÙØ´',
            'Outset': 'Ø§ÙØ¨Ø¯Ø§ÙÙ',
            'Inset': 'Ø§ÙØ¯Ø§Ø®ÙÙ',
            'Thick': 'Ø³ÙÙÙÙ',
            'Style': 'ÙÙØ·',
            'Width': 'Ø¹Ø±Ø¶',
            'Height': 'Ø§Ø±ØªÙØ§Ø¹',
            'Letter': 'Ø±Ø³Ø§ÙÙ',
            'Tabloid': 'Ø§ÙØªØ§Ø¨ÙÙÙØ¯',
            'Legal': 'Ø§ÙÙØ§ÙÙÙÙÙ',
            'Statement': 'Ø¨ÙØ§Ù',
            'Executive': 'Ø§ÙØªÙÙÙØ°Ù',
            'A3': 'A3',
            'A4': 'A4',
            'A5': 'A5',
            'B4': 'B4',
            'B5': 'B5',
            'Custom Size': 'Ø­Ø¬Ù ÙØ®ØµØµ',
            'Different odd and even': 'ÙØ®ØªÙÙÙ ØºØ±ÙØ¨Ù ÙØ­ØªÙ',
            'Different first page': 'Ø§ÙØµÙØ­Ø© Ø§ÙØ§ÙÙÙ ÙØ®ØªÙÙÙ',
            'From edge': 'ÙÙ Ø§ÙØ­Ø§ÙØ©',
            'Header': 'Ø±Ø§Ø³',
            'Footer': 'ØªØ°ÙÙÙ Ø§ÙØµÙØ­Ù',
            'Margin': 'Ø§ÙÙÙØ§ÙØ´',
            'Paper': 'Ø§ÙÙØ±Ù',
            'Layout': 'ØªØ®Ø·ÙØ·',
            'Orientation': 'Ø§ÙØªÙØ¬Ù',
            'Landscape': 'Ø§ÙÙÙØ§Ø¸Ø± Ø§ÙØ·Ø¨ÙØ¹ÙÙ',
            'Portrait': 'ØµÙØ±Ù',
            'Table Of Contents': 'Ø¬Ø¯ÙÙ Ø§ÙÙØ­ØªÙÙØ§Øª',
            'Show page numbers': 'Ø¥Ø¸ÙØ§Ø± Ø£Ø±ÙØ§Ù Ø§ÙØµÙØ­Ø§Øª',
            'Right align page numbers': 'ÙØ­Ø§Ø°Ø§Ø© Ø£Ø±ÙØ§Ù Ø§ÙØµÙØ­Ø§Øª Ø¥ÙÙ Ø§ÙÙÙÙÙ',
            'Nothing': 'Ø´ÙØ¡',
            'Tab leader': 'ÙØ§Ø¦Ø¯ Ø¹ÙØ§ÙØ© Ø§ÙØªØ¨ÙÙØ¨',
            'Show levels': 'Ø¥Ø¸ÙØ§Ø± Ø§ÙÙØ³ØªÙÙØ§Øª',
            'Use hyperlinks instead of page numbers': 'Ø§Ø³ØªØ®Ø¯Ø§Ù Ø§ÙØ§Ø±ØªØ¨Ø§Ø·Ø§Øª Ø§ÙØªØ´Ø¹Ø¨ÙØ© Ø¨Ø¯ÙØ§ ÙÙ Ø£Ø±ÙØ§Ù Ø§ÙØµÙØ­Ø§Øª',
            'Build table of contents from': 'Ø¨ÙØ§Ø¡ Ø¬Ø¯ÙÙ ÙØ­ØªÙÙØ§Øª ÙÙ',
            'Styles': 'Ø§ÙÙØ§Ø·',
            'Available styles': 'Ø§ÙØ£ÙÙØ§Ø· Ø§ÙÙØªÙÙØ±Ø©',
            'TOC level': 'ÙØ³ØªÙÙ Ø¬Ø¯ÙÙ Ø§ÙÙØ­ØªÙÙØ§Øª',
            'Heading': 'Ø¹ÙÙØ§Ù',
            'Heading 1': 'Ø¹ÙÙØ§Ù 1',
            'Heading 2': 'Ø¹ÙÙØ§Ù 2',
            'Heading 3': 'Ø¹ÙÙØ§Ù 3',
            'Heading 4': 'Ø¹ÙÙØ§Ù 4',
            'Heading 5': 'Ø¹ÙÙØ§Ù 5',
            'Heading 6': 'Ø¹ÙÙØ§Ù 6',
            'List Paragraph': 'ÙÙØ±Ù Ø§ÙÙØ§Ø¦ÙØ©',
            'Normal': 'Ø§ÙØ¹Ø§Ø¯ÙÙ',
            'Outline levels': 'ÙØ³ØªÙÙØ§Øª Ø§ÙÙØ®Ø·Ø· Ø§ÙØªÙØµÙÙÙ',
            'Table entry fields': 'Ø­ÙÙÙ Ø¥Ø¯Ø®Ø§Ù Ø§ÙØ¬Ø¯ÙÙ',
            'Modify': 'ØªØ¹Ø¯ÙÙ',
            'Color': 'ÙÙÙ',
            'Setting': 'Ø§Ø¹Ø¯Ø§Ø¯',
            'Box': 'ÙØ±Ø¨Ø¹',
            'All': 'Ø¬ÙÙØ¹',
            'Custom': 'Ø§ÙÙØ®ØµØµÙ',
            'Preview': 'ÙØ¹Ø§ÙÙÙ',
            'Shading': 'Ø§ÙØªØ¸ÙÙÙ',
            'Fill': 'ÙÙØ¡',
            'Apply To': 'ØªÙØ·Ø¨Ù Ø¹ÙÙ',
            'Table Properties': 'Ø®ØµØ§Ø¦Øµ Ø§ÙØ¬Ø¯ÙÙ',
            'Cell Options': 'Ø®ÙØ§Ø±Ø§Øª Ø§ÙØ®ÙÙØ©',
            'Table Options': 'Ø®ÙØ§Ø±Ø§Øª Ø§ÙØ¬Ø¯ÙÙ',
            'Insert Table': 'Ø§Ø¯Ø±Ø§Ø¬ Ø¬Ø¯ÙÙ',
            'Number of columns': 'Ø¹Ø¯Ø¯ Ø§ÙØ§Ø¹ÙØ¯Ù',
            'Number of rows': 'Ø¹Ø¯Ø¯ Ø§ÙØµÙÙÙ',
            'Text to display': 'Ø§ÙÙØµ Ø§ÙØ°Ù Ø³ÙØªÙ Ø¹Ø±Ø¶Ù',
            'Address': 'Ø¹ÙÙØ§Ù',
            'Insert Hyperlink': 'Ø§Ø¯Ø±Ø§Ø¬ Ø§Ø±ØªØ¨Ø§Ø· ØªØ´Ø¹Ø¨Ù',
            'Edit Hyperlink': 'ØªØ­Ø±ÙØ± Ø§Ø±ØªØ¨Ø§Ø· ØªØ´Ø¹Ø¨Ù',
            'Insert': 'Ø§Ø¯Ø±Ø§Ø¬',
            'General': 'Ø§ÙØ¹Ø§ÙÙ',
            'Indentation': 'Ø§ÙÙØ³Ø§ÙÙ Ø§ÙØ¨Ø§Ø¯Ø¦Ù',
            'Before text': 'ÙØ¨Ù Ø§ÙÙØµ',
            'Special': 'Ø§ÙØ®Ø§ØµÙ',
            'First line': 'Ø§ÙØ³Ø·Ø± Ø§ÙØ£ÙÙ',
            'Hanging': 'ÙØ¹ÙÙÙ',
            'After text': 'Ø¨Ø¹Ø¯ Ø§ÙÙØµ',
            'By': 'ÙÙ',
            'Before': 'ÙØ¨Ù',
            'Line Spacing': 'ØªØ¨Ø§Ø¹Ø¯ Ø§ÙØ£Ø³Ø·Ø±',
            'After': 'Ø¨Ø¹Ø¯',
            'At': 'ÙÙ',
            'Multiple': 'ÙØªØ¹Ø¯Ø¯Ù',
            'Spacing': 'ØªØ¨Ø§Ø¹Ø¯',
            'Define new Multilevel list': 'ØªØ­Ø¯ÙØ¯ ÙØ§Ø¦ÙÙ ÙØªØ¹Ø¯Ø¯Ø© Ø§ÙØ§ØµØ¹Ø¯Ù Ø¬Ø¯ÙØ¯Ù',
            'List level': 'ÙØ³ØªÙÙ Ø§ÙÙØ§Ø¦ÙØ©',
            'Choose level to modify': 'Ø§Ø®ØªØ± Ø§ÙÙØ³ØªÙÙ Ø§ÙØ°Ù ØªØ±ÙØ¯ ØªØ¹Ø¯ÙÙÙ',
            'Level': 'ÙØ³ØªÙÙ',
            'Number format': 'ØªÙØ³ÙÙ Ø§ÙØ£Ø±ÙØ§Ù',
            'Number style for this level': 'ÙÙØ· Ø§ÙØ±ÙÙ ÙÙØ°Ø§ Ø§ÙÙØ³ØªÙÙ',
            'Enter formatting for number': 'Ø¥Ø¯Ø®Ø§Ù ØªÙØ³ÙÙ ÙØ±ÙÙ',
            'Start at': 'Ø¨Ø¯Ø§ÙØ© ÙÙ',
            'Restart list after': 'Ø£Ø¹Ø§Ø¯Ù ØªØ´ØºÙÙ ÙØ§Ø¦ÙÙ Ø¨Ø¹Ø¯',
            'Position': 'ÙÙÙÙ',
            'Text indent at': 'Ø§ÙÙØ³Ø§ÙØ© Ø§ÙØ¨Ø§Ø¯Ø¦Ø© ÙÙÙØµ ÙÙ',
            'Aligned at': 'ÙØ­Ø§Ø°Ø§Ø© ÙÙ',
            'Follow number with': 'Ø§ØªØ¨Ø¹ Ø§ÙØ±ÙÙ ÙØ¹',
            'Tab character': 'Ø­Ø±Ù Ø¹ÙØ§ÙØ© Ø§ÙØªØ¨ÙÙØ¨',
            'Space': 'Ø§ÙÙØ¶Ø§Ø¡',
            'Arabic': 'Ø§ÙØ¹Ø±Ø¨ÙØ©',
            'UpRoman': 'Ø­ØªÙ Ø§ÙØ±ÙÙØ§ÙÙ',
            'LowRoman': 'Ø§ÙØ±ÙÙØ§ÙÙØ© ÙÙØ®ÙØ¶Ù',
            'UpLetter': '',
            'LowLetter': '',
            'Number': 'Ø¹Ø¯Ø¯',
            'Leading zero': 'ÙØ¤Ø¯Ù ØµÙØ±',
            'Bullet': 'Ø±ØµØ§ØµÙ',
            'Ordinal': 'Ø§ÙØªØ±ØªÙØ¨ÙÙ',
            'Ordinal Text': 'Ø§ÙÙØµ Ø§ÙØªØ±ØªÙØ¨Ù',
            'For East': 'ÙÙØ´Ø±Ù',
            'No Restart': 'ÙØ§ Ø£Ø¹Ø§Ø¯Ù ØªØ´ØºÙÙ',
            'Font': 'Ø§ÙØ®Ø·',
            'Font style': 'ÙÙØ· Ø§ÙØ®Ø·',
            'Underline style': 'ÙÙØ· Ø§ÙØªØ³Ø·ÙØ±',
            'Font color': 'ÙÙÙ Ø§ÙØ®Ø·',
            'Effects': 'Ø§ÙØ§Ø«Ø§Ø±',
            'Strikethrough': 'ÙØªÙØ³Ø·Ù',
            'Superscript': 'ÙØ±ØªÙØ¹',
            'Subscript': 'ÙÙØ®ÙØ¶',
            'Double strikethrough': 'Ø®Ø· ÙØ²Ø¯ÙØ¬ ÙØªÙØ³Ø·Ù Ø®Ø·',
            'Regular': 'Ø§ÙØ¹Ø§Ø¯ÙÙ',
            'Bold': 'Ø¬Ø±ÙØ¦Ù',
            'Italic': 'ÙØ§Ø¦Ù',
            'Cut': 'ÙØ·Ø¹',
            'Copy': 'ÙØ³Ø®',
            'Paste': 'ÙØµÙ',
            'Hyperlink': 'Ø§ÙØ§Ø±ØªØ¨Ø§Ø· Ø§ÙØªØ´Ø¹Ø¨Ù',
            'Open Hyperlink': 'ÙØªØ­ Ø§Ø±ØªØ¨Ø§Ø· ØªØ´Ø¹Ø¨Ù',
            'Copy Hyperlink': 'ÙØ³Ø® Ø§Ø±ØªØ¨Ø§Ø· ØªØ´Ø¹Ø¨Ù',
            'Remove Hyperlink': 'Ø£Ø²Ø§ÙÙ Ø§Ø±ØªØ¨Ø§Ø· ØªØ´Ø¹Ø¨Ù',
            'Paragraph': 'Ø§ÙÙÙØ±Ù',
            'Linked(Paragraph and Character)': 'ÙØ±ØªØ¨Ø· (ÙÙØ±Ù ÙØ­Ø±Ù)',
            'Character': 'Ø­Ø±Ù',
            'Merge Cells': 'Ø¯ÙØ¬ Ø§ÙØ®ÙØ§ÙØ§',
            'Insert Above': 'Ø§Ø¯Ø±Ø§Ø¬ Ø£Ø¹ÙØ§Ù',
            'Insert Below': 'Ø§Ø¯Ø±Ø§Ø¬ Ø£Ø¯ÙØ§Ù',
            'Insert Left': 'Ø§Ø¯Ø±Ø§Ø¬ Ø¥ÙÙ Ø§ÙÙØ³Ø§Ø±',
            'Insert Right': 'Ø§Ø¯Ø±Ø§Ø¬ Ø§ÙÙÙÙÙ',
            'Delete': 'Ø­Ø°Ù',
            'Delete Table': 'Ø­Ø°Ù Ø¬Ø¯ÙÙ',
            'Delete Row': 'Ø­Ø°Ù ØµÙ',
            'Delete Column': 'Ø­Ø°Ù Ø¹ÙÙØ¯',
            'File Name': 'Ø§Ø³Ù Ø§ÙÙÙÙ',
            'Format Type': 'ÙÙØ¹ Ø§ÙØªÙØ³ÙÙ',
            'Save': 'Ø­ÙØ¸',
            'Navigation': 'Ø§ÙØªÙÙÙ',
            'Results': 'ÙØªØ§Ø¦Ø¬',
            'Replace': 'Ø§Ø³ØªØ¨Ø¯Ø§Ù',
            'Replace All': 'Ø§Ø³ØªØ¨Ø¯Ø§Ù Ø§ÙÙÙ',
            'We replaced all': 'Ø§Ø³ØªØ¨Ø¯ÙÙØ§ Ø¬ÙÙØ¹',
            'Find': 'Ø§ÙØ¹Ø«ÙØ±',
            'No matches': 'ÙØ§ ØªÙØ¬Ø¯ ØªØ·Ø§Ø¨ÙØ§Øª',
            'All Done': 'ÙÙ Ø§ÙÙÙØ§Ù Ø¨Ù',
            'Result': 'ÙØªÙØ¬Ù',
            'of': 'ÙÙ',
            'instances': 'Ø§ÙØ­Ø§ÙØ§Øª',
            'with': 'ÙØ¹',
            'Click to follow link': 'Ø§ÙÙØ± ÙÙØªØ§Ø¨Ø¹Ù Ø§ÙØ§Ø±ØªØ¨Ø§Ø·',
            'Continue Numbering': 'ÙØªØ§Ø¨Ø¹Ù Ø§ÙØªØ±ÙÙÙ',
            'Bookmark name': 'Ø§Ø³Ù Ø§ÙØ¥Ø´Ø§Ø±Ø© Ø§ÙÙØ±Ø¬Ø¹ÙØ©',
            'Close': 'Ø§ØºÙØ§Ù',
            'Restart At': 'Ø£Ø¹Ø§Ø¯Ù Ø§ÙØªØ´ØºÙÙ Ø¹ÙØ¯',
            'Properties': 'Ø®ØµØ§Ø¦Øµ',
            'Name': 'Ø§Ø³Ù',
            'Style type': 'ÙÙØ¹ Ø§ÙÙÙØ·',
            'Style based on': 'ÙÙØ· Ø§Ø³ØªÙØ§Ø¯Ø§ Ø¥ÙÙ',
            'Style for following paragraph': 'ÙÙØ· ÙÙÙÙØ±Ø© Ø§ÙØªØ§ÙÙØ©',
            'Formatting': 'Ø§ÙØªÙØ³ÙÙ',
            'Numbering and Bullets': 'Ø§ÙØªØ±ÙÙÙ ÙØ§ÙØªØ¹Ø¯Ø§Ø¯ Ø§ÙÙÙØ·Ù',
            'Numbering': 'ØªØ±ÙÙÙ',
            'Update Field': 'ØªØ­Ø¯ÙØ« Ø§ÙØ­ÙÙ',
            'Edit Field': 'ØªØ­Ø±ÙØ± Ø§ÙØ­ÙÙ',
            'Bookmark': 'Ø§ÙØ¥Ø´Ø§Ø±Ø© Ø§ÙÙØ±Ø¬Ø¹ÙØ©',
            'Page Setup': 'Ø§Ø¹Ø¯Ø§Ø¯ Ø§ÙØµÙØ­Ø©',
            'No bookmarks found': 'ÙÙ ÙØªÙ Ø§ÙØ¹Ø«ÙØ± Ø¹ÙÙ Ø¥Ø´Ø§Ø±Ø§Øª ÙØ±Ø¬Ø¹ÙÙ',
            'Number format tooltip information': 'ØªÙØ³ÙÙ Ø±ÙÙ Ø£Ø­Ø§Ø¯Ù Ø§ÙÙØ³ØªÙÙ:' + '</br>' + '[Ø¨Ø§Ø¯Ø¦Ù]% [ÙØ³ØªÙÙ Ø§ÙØ§Ø¹Ø¯Ø§Ø¯] [ÙØ§Ø­ÙÙ]' + '</br>'
                // tslint:disable-next-line:max-line-length
                + 'Ø¹ÙÙ Ø³Ø¨ÙÙ Ø§Ø§ÙÙØ«Ø§Ù Ø "Ø§ÙÙØµÙ% 1." Ø³ÙØªÙ Ø¹Ø±Ø¶ Ø§ÙØªØ±ÙÙÙ ÙØ«Ù' + '</br>' + 'Ø§ÙÙØµÙ Ø§ÙØ£ÙÙ- Ø§ÙØ¨ÙØ¯' + '</br>' + 'Ø§ÙÙØµÙ Ø§ÙØ«Ø§ÙÙ- Ø§ÙØ¨ÙØ¯' + '</br>...'
                + '</br>' + 'Ø§ÙÙØµÙ ÙÙÙ-Ø§ÙØ¨ÙØ¯' + '</br>'
                // tslint:disable-next-line:max-line-length
                + '</br>' + 'ØªÙØ³ÙÙ Ø±ÙÙ ÙØªØ¹Ø¯Ø¯ Ø§ÙØ¥Ø¹Ø¯Ø§Ø¯Ø§Øª:' + '</br>' + '[Ø¨Ø§Ø¯Ø¦Ù]% [ÙØ³ØªÙÙ Ø§ÙÙØ³ØªÙÙ]' + '</br>' + '[ÙØ§Ø­ÙÙ] + [Ø¨Ø§Ø¯Ø¦Ù]%' + '</br>' + '[Ø§ÙÙØ³ØªÙÙ] [ÙØ§Ø­ÙÙ]'
                + '</br>' + 'Ø¹ÙÙ Ø³Ø¨ÙÙ Ø§ÙÙØ«Ø§Ù Ø "% 1.% 2." Ø³ÙØªÙ Ø¹Ø±Ø¶ Ø§ÙØªØ±ÙÙÙ ÙØ«Ù' + '</br>' + '1.1 Ø§ÙØ¨ÙØ¯' + '</br>' + '1.2 Ø§ÙØ¨ÙØ¯' + '</br>...' + '</br>' + '1. ÙÙÙ-Ø§ÙØ¨ÙØ¯',
            'Format': 'ØªÙØ³ÙÙ',
            'Create New Style': 'Ø¥ÙØ´Ø§Ø¡ ÙÙØ· Ø¬Ø¯ÙØ¯',
            'Modify Style': 'ØªØ¹Ø¯ÙÙ Ø§ÙÙÙØ·',
            'New': 'Ø§ÙØ¬Ø¯ÙØ¯',
            'Bullets': 'Ø§ÙØ±ØµØ§Øµ',
            'Use bookmarks': 'Ø§Ø³ØªØ®Ø¯Ø§Ù Ø§ÙØ¥Ø´Ø§Ø±Ø§Øª Ø§ÙÙØ±Ø¬Ø¹ÙØ©',
            'Table of Contents': 'Ø¬Ø¯ÙÙ Ø§ÙÙØ­ØªÙÙØ§Øª',
            'AutoFit': 'Ø§ÙØ§Ø­ØªÙØ§Ø¡',
            'AutoFit to Contents': 'Ø§Ø­ØªÙØ§Ø¡ ØªÙÙØ§Ø¦Ù ÙÙÙØ­ØªÙÙØ§Øª',
            'AutoFit to Window': 'Ø§Ø­ØªÙØ§Ø¡ ØªÙÙØ§Ø¦Ù ÙÙØ¥Ø·Ø§Ø±',
            'Fixed Column Width': 'Ø¹Ø±Ø¶ Ø§ÙØ¹ÙÙØ¯ Ø§ÙØ«Ø§Ø¨Øª',
            'Reset': 'Ø§Ø¹Ø§Ø¯Ù ØªØ¹ÙÙÙ',
            'Match case': 'Ø­Ø§ÙÙ Ø§ÙÙØ¨Ø§Ø±Ø§Ø©',
            'Whole words': 'ÙÙÙØ§Øª ÙØ§ÙÙ',
            'Add': 'Ø§Ø¶Ø§ÙÙ',
            'Go To': 'Ø§ÙØ§ÙØªÙØ§Ù Ø¥ÙÙ',
            'Search for': 'Ø§ÙØ¨Ø­Ø« Ø¹Ù',
            'Replace with': 'Ø§Ø³ØªØ¨Ø¯Ø§Ù',
            'TOC 1': 'Ø¬Ø¯ÙÙ Ø§ÙÙØ­ØªÙÙØ§Øª 1',
            'TOC 2': 'Ø¬Ø¯ÙÙ Ø§ÙÙØ­ØªÙÙØ§Øª 2',
            'TOC 3': 'Ø¬Ø¯ÙÙ Ø§ÙÙØ­ØªÙÙØ§Øª 3',
            'TOC 4': 'Ø¬Ø¯ÙÙ Ø§ÙÙØ­ØªÙÙØ§Øª 4',
            'TOC 5': 'Ø¬Ø¯ÙÙ Ø§ÙÙØ­ØªÙÙØ§Øª 5',
            'TOC 6': 'Ø¬Ø¯ÙÙ Ø§ÙÙØ­ØªÙÙØ§Øª 6',
            'TOC 7': 'Ø¬Ø¯ÙÙ Ø§ÙÙØ­ØªÙÙØ§Øª 7',
            'TOC 8': 'Ø¬Ø¯ÙÙ Ø§ÙÙØ­ØªÙÙØ§Øª 8',
            'TOC 9': 'Ø¬Ø¯ÙÙ Ø§ÙÙØ­ØªÙÙØ§Øª 9',
            'Right-to-left': 'ÙÙ Ø§ÙÙÙÙÙ Ø¥ÙÙ Ø§ÙÙØ³Ø§Ø±',
            'Left-to-right': 'ÙÙ Ø§ÙÙØ³Ø§Ø± Ø¥ÙÙ Ø§ÙÙÙÙÙ',
            'Direction': 'Ø§ÙØ§ØªØ¬Ø§Ù',
            'Table direction': 'Ø§ØªØ¬Ø§Ù Ø§ÙØ¬Ø¯ÙÙ',
            'Indent from right': 'ÙØ³Ø§ÙØ© Ø¨Ø§Ø¯Ø¦Ù ÙÙ Ø§ÙÙÙÙÙ',
            'Page': 'ØµÙØ­Ù',
            'Fit one page': 'Ø§Ø­ØªÙØ§Ø¡ ØµÙØ­Ù ÙØ§Ø­Ø¯',
            'Fit page width': 'Ø§Ø­ØªÙØ§Ø¡ Ø¹Ø±Ø¶ Ø§ÙØµÙØ­Ø©',
            // tslint:disable-next-line:max-line-length
            'The current page number in the document. Click or tap to navigate specific page.': 'Ø±ÙÙ Ø§ÙØµÙØ­Ø© Ø§ÙØ­Ø§ÙÙØ© ÙÙ Ø§ÙÙØ³ØªÙØ¯. Ø§ÙÙØ± Ø£Ø£Ù Ø§Ø¶ØºØ· ÙÙØªÙÙÙ ÙÙ ØµÙØ­Ù ÙØ¹ÙÙÙ'
        },
        'colorpicker': {
            'Apply': 'ØªØ·Ø¨ÙÙ',
            'Cancel': 'Ø¥ÙØºØ§Ø¡ Ø§ÙØ£ÙØ±',
            'ModeSwitcher': 'ÙÙØªØ§Ø­ ÙÙØ±Ø¨Ø§Ø¦Ù Ø§ÙÙØ¶Ø¹'
        }
    }
});
var documenteditor = new ej.documenteditor.DocumentEditor({isReadOnly: false,enableRtl: true,locale: 'ar-AE', serviceUrl: 'https://document.syncfusion.com/web-services/docx-editor/api/documenteditor/'});
documenteditor.enableAllModules();
var containerPanel = document.getElementById('container');
function updateContainerSize() {
  this.containerPanel.style.height = window.innerHeight + 'px';
}

updateContainerSize();
documenteditor.appendTo('#DocumentEditor');

var sfdt=`{
    "sections": [
        {
            "blocks": [
                {
                    "characterFormat": {
                        "fontSize": 18.0,
                        "fontFamily": "Calibri",
                        "fontFamilyBidi": "Calibri"
                    },
                    "paragraphFormat": {
                        "beforeSpacing": 18.0,
                        "afterSpacing": 30.0,
                        "styleName": "Heading 1",
                        "bidi": true
                    },
                    "inlines": [
                        {
                            "text": "Ø§Ø¹ÙØ§Ù Ø§ÙÙØºØ§ÙØ±Ø© Ø¯ÙØ±Ø§Øª",
                            "characterFormat": {
                                "fontSize": 18.0,
                                "bidi": true,
                                "fontSizeBidi": 18.0
                            }
                        }
                    ]
                }
            ]
        }
    ]
}`;

documenteditor.open(sfdt);


{% endhighlight %}
{% highlight html tabtitle="index.html" %}
<!DOCTYPE html><html lang="en"><head>
    <title>EJ2 Animation</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Typescript UI Controls">
    <meta name="author" content="Syncfusion">
    <link href="index.css" rel="stylesheet">
    <link href="https://cdn.syncfusion.com/ej2/20.3.56/ej2-documenteditor/styles/fabric.css" rel="stylesheet">
    <link href="https://cdn.syncfusion.com/ej2/20.3.56/ej2-buttons/styles/fabric.css" rel="stylesheet">
    <link href="https://cdn.syncfusion.com/ej2/20.3.56/ej2-base/styles/fabric.css" rel="stylesheet">
    <link href="https://cdn.syncfusion.com/ej2/20.3.56/ej2-dropdowns/styles/fabric.css" rel="stylesheet">
    <link href="https://cdn.syncfusion.com/ej2/20.3.56/ej2-inputs/styles/fabric.css" rel="stylesheet">
    <link href="https://cdn.syncfusion.com/ej2/20.3.56/ej2-lists/styles/fabric.css" rel="stylesheet">
    <link href="https://cdn.syncfusion.com/ej2/20.3.56/ej2-navigations/styles/fabric.css" rel="stylesheet">
    <link href="https://cdn.syncfusion.com/ej2/20.3.56/ej2-popups/styles/fabric.css" rel="stylesheet">
    <link href="https://cdn.syncfusion.com/ej2/20.3.56/ej2-splitbuttons/styles/fabric.css" rel="stylesheet"> 
    
    
<script src="https://cdn.syncfusion.com/ej2/20.4.38/dist/ej2.min.js" type="text/javascript"></script>
</head>

<body>
    
    <div id="container">
        <div id="toolbar">            
        </div>
        <div style="width:100%;height: 100%">
            <!--Element which will render as DocumentEditor -->
            <div id="DocumentEditor"></div>
        </div>
    </div>


<script>
var ele = document.getElementById('container');
if(ele) {
  ele.style.visibility = "visible";
}   
      </script>
<script src="index.js" type="text/javascript"></script>
</body></html>
{% endhighlight %}
{% endtabs %}

