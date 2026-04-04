# Source: https://uat.rive.app/docs/runtimes/fonts.md

# Source: https://uat.rive.app/docs/editor/text/fonts.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Fonts

Select a font in the inspector as part of a Text Style. The default list is populated via Google Fonts, however you can also upload your own fonts to the Assets Panel.

## Font Options

Font variables and OpenType features can be found in the options fly-out of the Text Styles subsection. If supported by the font, you can find it alongside the font weight dropdown.

<Info>
  Font variables can be animated. Open the options fly-out in animate mode to add keys.
</Info>

<Info>
  Not all fonts support variable axes and OpenType features. The options menu will only surface for supported fonts.
</Info>

<img src="https://mintcdn.com/rive/7FKuJTeC-EIGSybi/images/editor/text/text-runs-fonts-overview.gif?s=30b44fbaf5f74318fc1ba65844ca9095" alt="Configure variables and features for compatible fonts" width="1000" height="347" data-path="images/editor/text/text-runs-fonts-overview.gif" />

***

## Font Sources

### Google Fonts

The default font list is populated via Google Fonts. These fonts are available to use on all plans. After selecting a font it'll appear in the Assets Panel under the 'Fonts' category. This is true for both custom *and* Google fonts. The latter will update automatically based on the fonts you're using within the Rive file.

<Info>
  Fonts provided by Google Fonts are marked with a G icon.
</Info>

### Custom Fonts

Upload custom fonts by drag-and-dropping your font file into the editor or via the `+` action in the Assets Panel. Uploaded fonts will show at the top of the font selection drop down in the text inspector.

<Info>
  Select a font in the Assets Panel to view available metadata and licenses in the Inspector.
</Info>

***

## Export Options

Your Rive file will need to reference a font file if you're looking to dynamically update text at runtime. Configure the available options to suit your needs and optimise your `.riv` files. Select a font in the Assets Panel to reveal its export options in the Inspector.

### Export Type

Select the font in the **Assets** panel and change the **Type** option to define where you'd like the font to export to.

<img src="https://mintcdn.com/rive/7FKuJTeC-EIGSybi/images/editor/text/text-runs-fonts-detail.png?fit=max&auto=format&n=7FKuJTeC-EIGSybi&q=85&s=1c552fe379f358a2c635f9ec97a58c02" alt="Export Options" width="529" height="465" data-path="images/editor/text/text-runs-fonts-detail.png" />

* **Embedded:** Embed the font file inside the `.riv`. Embedding the font inside the Rive file is the simplest option, however will increase the size of the file. Use this option if the font is unique to your animation, and isn't already available inside your app, website, or game.
* **Referenced:** Export the font file alongside the `.riv`. This option is ideal if you have multiple Rive files using the same font, or if you're implementing a Rive file into an app, game, or website that already has the font file available. Using a referenced font file will reduce the size of your Rive files.
* **Hosted:** Hosted fonts are uploaded to Rive's CDN for a runtime to download from on demand. Similar to a referenced font file, choosing to host the font on Rive's CDN will omit it from the `.riv`, thus reducing the `.riv` file size. The Rive runtimes will fetch the font when your animation plays in your app, game, or website.

<Info>
  Assets hosted on Rive's CDN can be accessed by anyone with the link.
</Info>

<Note>
  Hosted fonts are available on Voyager and Enterprise plans. [Learn more about our plans and pricing](https://rive.app/pricing).
</Note>

***

### Glyph / Script Selection

Alongside the font location, you can configure the glyphs you wish to be included. Removing unnecessary glyphs and scripts will reduce the size of the font file (referenced/hosted) or Rive file (embedded). Deciding which scripts to include will depend on whether you want to dynamically update text at runtime, and the languages you want to support.

<Info>
  Use the 'View Glyphs' feature to browse what glyphs / scripts are available for your chosen font. You can find it in the Inspector after selecting a font in the Assets Panel.
</Info>

<img src="https://mintcdn.com/rive/7FKuJTeC-EIGSybi/images/editor/text/text-runs-fonts-gliphs.gif?s=6036fb584cdeb96d44da54bcc7c9d815" alt="Use the viewer to browse a font's available glyphs and scripts" width="1000" height="513" data-path="images/editor/text/text-runs-fonts-gliphs.gif" />

**Choose from three options**

* **All Glyphs:** Export the entire font file. All the glyphs will be available to use at runtime.
* **Glyphs Used:** Only exports glyphs used within the file. For example, if your text says "Hello World!", only the `H`,`e`,`l`,`o`,`W`,`r`,`d`, and `!` glyphs would be exported. Use this option if you don't intend to change the text at runtime.

<Tip>
  If you want to include a specific set of glyphs (ex: numbers only), you can include these glyphs in a separate artboard and they will be compiled for runtime.
</Tip>

* **Custom:** Export chosen scripts. Use the script options fly-out to toggle scripts on and off. Use this option if you want to dynamically update text at runtime, but don't need to support certain languages or alphabets. This will help reduce file size by removing scripts you don't plan to use.

<img src="https://mintcdn.com/rive/7FKuJTeC-EIGSybi/images/editor/text/text-runs-fonts-custom.gif?s=04b87a7f0dcc43257fb115b673704690" alt="Remove unwanted scripts to optimize font exports" width="1200" height="541" data-path="images/editor/text/text-runs-fonts-custom.gif" />
