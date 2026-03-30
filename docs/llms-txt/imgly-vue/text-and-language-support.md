# Text and Language Support

Support right-to-left text, complex scripts, and multilingual typography in your designs using CE.SDK’s comprehensive text rendering capabilities.

![Text and Language Support example showing multilingual text in different scripts](/docs/cesdk/_astro/browser.hero.DwyccKcU_2l173g.webp)

15 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-text-language-support-browser)[

GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-text-language-support-browser)

CE.SDK provides built-in support for creating designs that work seamlessly across different languages and writing systems. The engine automatically handles text shaping, bidirectional layout, and script-specific rendering - supporting all Unicode characters, complex script ligatures, and mixed LTR/RTL content without additional configuration.

```
import type { EditorPlugin, EditorPluginContext, CreativeEngine } from '@cesdk/cesdk-js';import packageJson from './package.json';
// Typeface definitionsconst ROBOTO_BOLD = {  name: 'Roboto',  fonts: [    {      uri: 'https://fonts.gstatic.com/s/roboto/v30/KFOlCnqEu92Fr1MmEU9vAw.ttf',      subFamily: 'Bold',      weight: 'bold' as const,      style: 'normal' as const    }  ]};
const NOTO_NASKH_ARABIC = {  name: 'Noto Naskh Arabic',  fonts: [    {      uri: `${window.location.origin}${import.meta.env.BASE_URL}NotoNaskhArabic-Regular.ttf`,      subFamily: 'Regular',      weight: 'normal' as const,      style: 'normal' as const    }  ]};
const NOTO_SANS_KR = {  name: 'Noto Sans KR',  fonts: [    {      uri: `${window.location.origin}${import.meta.env.BASE_URL}NotoSansKR-VariableFont_wght.ttf`,      subFamily: 'Regular',      weight: 'normal' as const,      style: 'normal' as const    }  ]};
// Layout configurationconst LAYOUT = {  PAGE: { width: 800, height: 1200 },  TEXT: { x: 50, width: 700, defaultHeight: 140, fontSize: 20 },  SPACING: { gap: 16, startY: 50 }};
// Typeface interfaceinterface Typeface {  name: string;  fonts: Array<{    uri: string;    subFamily: string;    weight: 'normal' | 'bold';    style: 'normal' | 'italic';  }>;}
function createTextBlock(  engine: CreativeEngine,  page: number,  text: string,  typeface: Typeface,  yPosition: number,  height: number = LAYOUT.TEXT.defaultHeight,  alignment: 'Left' | 'Center' | 'Right' = 'Left'): void {  const textBlock = engine.block.create('text');  engine.block.setString(textBlock, 'text/text', text);  engine.block.setPositionX(textBlock, LAYOUT.TEXT.x);  engine.block.setPositionY(textBlock, yPosition);  engine.block.setWidth(textBlock, LAYOUT.TEXT.width);  engine.block.setHeight(textBlock, height);  engine.block.setFloat(textBlock, 'text/fontSize', LAYOUT.TEXT.fontSize);  engine.block.setTypeface(textBlock, typeface);  if (alignment !== 'Left') {    engine.block.setEnum(textBlock, 'text/horizontalAlignment', alignment);  }  engine.block.appendChild(page, textBlock);}
/** * CE.SDK Plugin: Text Language Support Guide * * Demonstrates multilingual text support: * - RTL text rendering (Arabic) * - Complex script support (Korean) * - Custom font loading for Unicode coverage * - Text alignment for different writing directions */class Example implements EditorPlugin {  name = packageJson.name;
  version = packageJson.version;
  async initialize({ cesdk }: EditorPluginContext): Promise<void> {    if (!cesdk) {      throw new Error('CE.SDK instance is required for this plugin');    }
    await cesdk.addDefaultAssetSources();    await cesdk.addDemoAssetSources({ sceneMode: 'Design' });
    // Add custom multilingual fonts to asset library    cesdk.engine.asset.addLocalSource('multilingual-typefaces');
    cesdk.engine.asset.addAssetToSource('multilingual-typefaces', {      id: 'noto-naskh-arabic',      label: { en: 'Noto Naskh Arabic' },      payload: {        typeface: {          name: 'Noto Naskh Arabic',          fonts: [            {              uri: `${window.location.origin}${import.meta.env.BASE_URL}NotoNaskhArabic-Regular.ttf`,              subFamily: 'Regular',              weight: 'normal',              style: 'normal'            }          ]        }      }    });
    cesdk.engine.asset.addAssetToSource('multilingual-typefaces', {      id: 'noto-sans-kr',      label: { en: 'Noto Sans KR' },      payload: {        typeface: {          name: 'Noto Sans KR',          fonts: [            {              uri: `${window.location.origin}${import.meta.env.BASE_URL}NotoSansKR-VariableFont_wght.ttf`,              subFamily: 'Regular',              weight: 'normal',              style: 'normal'            }          ]        }      }    });
    cesdk.ui.updateAssetLibraryEntry('ly.img.typefaces', {      sourceIds: ['ly.img.typeface', 'multilingual-typefaces']    });
    const engine = cesdk.engine;
    // Create a blank scene with a white canvas    const scene = engine.scene.create();    const page = engine.block.create('page');    engine.block.setWidth(page, LAYOUT.PAGE.width);    engine.block.setHeight(page, LAYOUT.PAGE.height);    engine.block.appendChild(scene, page);    engine.scene.zoomToBlock(page);
    // Create four text elements demonstrating multilingual font support    const textElements = [      { text: 'RTL Arabic', typeface: ROBOTO_BOLD, height: 140 },      {        text: 'هذا مثال.',        typeface: NOTO_NASKH_ARABIC,        height: 160,        alignment: 'Right' as const      },      { text: 'Korean', typeface: ROBOTO_BOLD, height: 140 },      { text: '이는 한 예입니다.', typeface: NOTO_SANS_KR, height: 140 }    ];
    let currentY = LAYOUT.SPACING.startY;    for (const element of textElements) {      createTextBlock(        engine,        page,        element.text,        element.typeface,        currentY,        element.height,        element.alignment      );      currentY += element.height + LAYOUT.SPACING.gap;    }  }}
export default Example;
```

This guide covers how to work with multilingual text using both the built-in text UI and programmatic APIs for font configuration, text direction, and dynamic language content.

## Programmatic Font and Typeface Management[#](#programmatic-font-and-typeface-management)

### Initialize CE.SDK[#](#initialize-cesdk)

For applications that need to manage multilingual text programmatically, we start by setting up CE.SDK and creating a scene.

```
// Create a blank scene with a white canvasconst scene = engine.scene.create();const page = engine.block.create('page');engine.block.setWidth(page, LAYOUT.PAGE.width);engine.block.setHeight(page, LAYOUT.PAGE.height);engine.block.appendChild(scene, page);engine.scene.zoomToBlock(page);
```

This creates a blank 800×1200px canvas that we’ll use for demonstrating multilingual text features.

### Configuring Typefaces for Language Support[#](#configuring-typefaces-for-language-support)

To support specific languages and scripts, we define typefaces as constants with appropriate Unicode coverage. This example uses a constants-based approach for reusable typeface definitions that can be referenced throughout the code.

```
// Typeface definitionsconst ROBOTO_BOLD = {  name: 'Roboto',  fonts: [    {      uri: 'https://fonts.gstatic.com/s/roboto/v30/KFOlCnqEu92Fr1MmEU9vAw.ttf',      subFamily: 'Bold',      weight: 'bold' as const,      style: 'normal' as const    }  ]};
const NOTO_NASKH_ARABIC = {  name: 'Noto Naskh Arabic',  fonts: [    {      uri: `${window.location.origin}${import.meta.env.BASE_URL}NotoNaskhArabic-Regular.ttf`,      subFamily: 'Regular',      weight: 'normal' as const,      style: 'normal' as const    }  ]};
const NOTO_SANS_KR = {  name: 'Noto Sans KR',  fonts: [    {      uri: `${window.location.origin}${import.meta.env.BASE_URL}NotoSansKR-VariableFont_wght.ttf`,      subFamily: 'Regular',      weight: 'normal' as const,      style: 'normal' as const    }  ]};
```

The example defines three typefaces as named constants:

*   **ROBOTO\_BOLD** - A web font for Latin script labels
*   **NOTO\_NASKH\_ARABIC** - Optimized for Arabic script with proper contextual forms
*   **NOTO\_SANS\_KR** - Variable font supporting Korean (Hangul) characters

Each typeface includes:

*   **name** - The typeface family name
*   **fonts** - Array of font objects with URIs and styles
*   **uri** - Path to font file (TTF, OTF, WOFF2 formats supported)
*   **weight** - Font weight (normal, bold, or numeric values)
*   **style** - Font style (normal or italic)

CE.SDK uses system fonts with Unicode support by default. Custom typefaces are useful when you need specific brand fonts or enhanced coverage for particular scripts.

### Applying Fonts with a Helper Function[#](#applying-fonts-with-a-helper-function)

The `createTextBlock()` function encapsulates all text block setup logic, reducing code duplication. Text elements are defined as an array and processed in a loop:

```
function createTextBlock(  engine: CreativeEngine,  page: number,  text: string,  typeface: Typeface,  yPosition: number,  height: number = LAYOUT.TEXT.defaultHeight,  alignment: 'Left' | 'Center' | 'Right' = 'Left'): void {  const textBlock = engine.block.create('text');  engine.block.setString(textBlock, 'text/text', text);  engine.block.setPositionX(textBlock, LAYOUT.TEXT.x);  engine.block.setPositionY(textBlock, yPosition);  engine.block.setWidth(textBlock, LAYOUT.TEXT.width);  engine.block.setHeight(textBlock, height);  engine.block.setFloat(textBlock, 'text/fontSize', LAYOUT.TEXT.fontSize);  engine.block.setTypeface(textBlock, typeface);  if (alignment !== 'Left') {    engine.block.setEnum(textBlock, 'text/horizontalAlignment', alignment);  }  engine.block.appendChild(page, textBlock);}
```

```
// Create four text elements demonstrating multilingual font supportconst textElements = [  { text: 'RTL Arabic', typeface: ROBOTO_BOLD, height: 140 },  {    text: 'هذا مثال.',    typeface: NOTO_NASKH_ARABIC,    height: 160,    alignment: 'Right' as const  },  { text: 'Korean', typeface: ROBOTO_BOLD, height: 140 },  { text: '이는 한 예입니다.', typeface: NOTO_SANS_KR, height: 140 }];
let currentY = LAYOUT.SPACING.startY;for (const element of textElements) {  createTextBlock(    engine,    page,    element.text,    element.typeface,    currentY,    element.height,    element.alignment  );  currentY += element.height + LAYOUT.SPACING.gap;}
```

This approach provides several benefits:

*   **DRY Principle** - Eliminates repetitive block setup code
*   **Easy to Extend** - Add new languages by appending to the configuration array
*   **Maintainable** - Change layout spacing or dimensions in one place

The `engine.block.setTypeface()` method applies fonts at the block level. CE.SDK automatically uses the configured fonts to render text with proper glyph coverage for the languages in your content.

## Working with Right-to-Left (RTL) Text[#](#working-with-right-to-left-rtl-text)

### Understanding Automatic RTL Detection[#](#understanding-automatic-rtl-detection)

CE.SDK automatically detects text direction based on Unicode character properties. When you create a text block with RTL content like Arabic or Hebrew, the engine analyzes the text and applies right-to-left rendering automatically.

```
// Create four text elements demonstrating multilingual font supportconst textElements = [  { text: 'RTL Arabic', typeface: ROBOTO_BOLD, height: 140 },  {    text: 'هذا مثال.',    typeface: NOTO_NASKH_ARABIC,    height: 160,    alignment: 'Right' as const  },  { text: 'Korean', typeface: ROBOTO_BOLD, height: 140 },  { text: '이는 한 예입니다.', typeface: NOTO_SANS_KR, height: 140 }];
let currentY = LAYOUT.SPACING.startY;for (const element of textElements) {  createTextBlock(    engine,    page,    element.text,    element.typeface,    currentY,    element.height,    element.alignment  );  currentY += element.height + LAYOUT.SPACING.gap;}
```

The engine implements the Unicode Bidirectional Algorithm (UAX #9), which:

*   **Detects strong directional characters** - Characters like Arabic or Hebrew letters establish RTL flow
*   **Handles neutral characters** - Spaces, punctuation, and numbers display correctly in context
*   **Manages embedding** - LTR words (like English brand names) embed correctly within RTL text

This automatic detection works for:

*   **Arabic** - Including Persian and Urdu variants
*   **Hebrew** - Modern and Biblical Hebrew
*   **Mixed content** - English or other LTR text within RTL paragraphs

### Text Alignment for RTL Languages[#](#text-alignment-for-rtl-languages)

While text direction is detected automatically, you may want to control horizontal alignment to match language conventions. The `createTextBlock()` helper function includes an optional `alignment` parameter that defaults to ‘Left’ for standard LTR text.

```
if (alignment !== 'Left') {  engine.block.setEnum(textBlock, 'text/horizontalAlignment', alignment);}
```

The alignment logic:

*   **Conditional Application** - The helper only calls `setEnum()` when alignment differs from the default ‘Left’
*   **Optional Parameter** - Elements without an `alignment` property in the configuration array use the default
*   **Type Safety** - TypeScript ensures only valid values (‘Left’, ‘Center’, ‘Right’) are used

In the example configuration array, the Arabic text specifies `alignment: 'Right'` which triggers the alignment logic:

```
{  text: 'هذا مثال.',  typeface: NOTO_NASKH_ARABIC,  height: 160,  alignment: 'Right' as const  // Explicitly set for RTL text}
```

Common alignment patterns:

*   **Right alignment** - Standard for Arabic, Hebrew, Persian, Urdu
*   **Left alignment** - Standard for English, European languages, CJK (default)
*   **Center alignment** - Language-neutral for titles and headings

This approach provides flexibility while keeping common cases simple - most text uses default left alignment without extra configuration.

## Complex Script Support[#](#complex-script-support)

CE.SDK automatically handles complex script features without requiring additional configuration. The text engine provides:

### Arabic Script Features[#](#arabic-script-features)

When rendering Arabic text, the engine automatically applies:

*   **Contextual letter forms** - Letters change shape based on position (initial, medial, final, isolated)
*   **Required ligatures** - Mandatory character combinations render as single glyphs
*   **Diacritical marks** - Tashkeel marks position correctly above and below letters
*   **Kashida** - Text justification through letter elongation

These features work automatically when you use fonts that include the necessary OpenType tables.

### Other Complex Scripts[#](#other-complex-scripts)

The text engine similarly supports other writing systems:

*   **Devanagari** (Hindi, Sanskrit) - Conjunct formations and half-forms
*   **Thai** - Vowel and tone mark positioning above and below base characters
*   **Japanese** - Kanji, hiragana, and katakana rendering
*   **Southeast Asian scripts** - Khmer subscripts, Myanmar ligatures

All complex script features are applied automatically based on Unicode properties and font capabilities.

## Creating Multilingual Design Templates[#](#creating-multilingual-design-templates)

### Using Variables for Multilingual Content[#](#using-variables-for-multilingual-content)

For designs that need to display different language content dynamically, use variable bindings. Variables enable you to switch languages while maintaining proper text rendering for each script.

Benefits of using variables:

*   **Dynamic language switching** - Update variable values to change content language
*   **Consistent formatting** - Text styling and layout remain stable across languages
*   **Template reusability** - One template works for multiple language markets

Variables are particularly useful for:

*   **Localized marketing materials** - Same design, different language content
*   **A/B testing** - Test messaging across languages
*   **Regional campaigns** - Deploy region-specific content from a single template

### Template Design Considerations[#](#template-design-considerations)

When designing multilingual templates, account for:

*   **Text expansion** - Some languages require 30-50% more space than English
*   **Direction changes** - RTL layouts may need mirrored designs
*   **Font availability** - Ensure typefaces cover all target scripts
*   **Line height** - Scripts with diacritics may need additional vertical space

Test templates with representative content in all target languages to verify layout works correctly.

## Font Fallback and Character Coverage[#](#font-fallback-and-character-coverage)

### Font Selection Priority[#](#font-selection-priority)

When rendering text, CE.SDK follows a fallback chain to ensure all characters display correctly:

1.  **Primary typeface** - The explicitly assigned font
2.  **System fonts** - Fonts available on the user’s system
3.  **Fallback glyphs** - Generic replacement characters when no font contains the glyph

This fallback system ensures text always renders, even when fonts lack specific characters.

### Ensuring Complete Character Coverage[#](#ensuring-complete-character-coverage)

To avoid missing glyph issues:

*   **Use comprehensive typefaces** - Noto fonts family provides extensive Unicode coverage
*   **Test with target languages** - Verify fonts include required scripts before deployment
*   **Configure fallback stacks** - Define multiple typefaces for comprehensive coverage
*   **Check font formats** - Ensure fonts include OpenType layout tables for complex scripts

Testing with representative text samples in all target languages helps identify coverage gaps before production.

## Troubleshooting[#](#troubleshooting)

### Text Displays as Squares or Question Marks[#](#text-displays-as-squares-or-question-marks)

**Issue**: Characters render as replacement glyphs (□ or ?) instead of the intended script.

**Solution**: The selected font lacks glyphs for the text content. Use fonts with appropriate Unicode coverage:

*   Verify font supports required Unicode blocks
*   Test with Noto fonts family for comprehensive coverage
*   Check font file format compatibility (TTF, OTF, WOFF2)
*   Ensure font files are accessible with correct URIs

### RTL Text Renders Left-to-Right[#](#rtl-text-renders-left-to-right)

**Issue**: Arabic or Hebrew text flows left-to-right instead of right-to-left.

**Solution**: Set horizontal alignment to match RTL conventions:

*   Use `engine.block.setEnum(block, 'text/horizontalAlignment', 'Right')`
*   Verify font includes bidirectional layout features
*   Check that font supports RTL scripts
*   Test with known RTL-compatible fonts (Noto Sans Arabic, Noto Sans Hebrew)

### Ligatures or Diacritics Display Incorrectly[#](#ligatures-or-diacritics-display-incorrectly)

**Issue**: Complex script features like ligatures or diacritical marks appear disconnected or mispositioned.

**Solution**: Use fonts specifically designed for the target script:

*   Verify font includes GSUB/GPOS OpenType tables
*   Use script-specific Noto fonts
*   Check font includes required OpenType layout features
*   Test with fonts known to support the script

### Mixed-Direction Text Layout Issues[#](#mixed-direction-text-layout-issues)

**Issue**: Text with both LTR and RTL content displays incorrectly.

**Solution**: The engine’s automatic bidirectional handling should resolve most cases. If issues persist:

*   Test with different fonts to verify bidirectional support
*   Use Unicode directional formatting characters sparingly (RLM U+200F, LRM U+200E)
*   Verify text editor preserves directional markers
*   Check that text content includes proper strong directional characters

---



[Source](https:/img.ly/docs/cesdk/vue/text/font-combinations-a1b2c3)