# Editor icons in English

# Editor icons

When a new class is created and exposed to scripting, the editor's interface
will display it with a default icon representing the base class it inherits
from. In most cases, it's still recommended to create icons for new classes to
improve the user experience.

## Creating icons

To create new icons, you first need a vector graphics editor installed.
For instance, you can use the open sourceInkscapeeditor.
Clone thegodotrepository containing all the editor icons:

```
git clone https://github.com/godotengine/godot.git
```

The icons must be created in a vector graphics editor in SVG format. There are
three main requirements to follow:

- Icons must be 16×16. In Inkscape, you can configure the document size inFile > Document Properties.
Icons must be 16×16. In Inkscape, you can configure the document size inFile > Document Properties.
- Lines should be snapped to pixels whenever possible to remain crisp at lower DPI.
You can create a 16×16 grid in Inkscape to make this easier.
Lines should be snapped to pixels whenever possible to remain crisp at lower DPI.
You can create a 16×16 grid in Inkscape to make this easier.
- If the user has configured their editor to use a light theme, Godot will
convert the icon's colors based on aset of predefined color mappings.
This is to ensure the icon always displays with a sufficient contrast rate.
Try to restrict your icon's color palette to colors found in the list above.
Otherwise, your icon may become difficult to read on a light background.
If the user has configured their editor to use a light theme, Godot will
convert the icon's colors based on aset of predefined color mappings.
This is to ensure the icon always displays with a sufficient contrast rate.
Try to restrict your icon's color palette to colors found in the list above.
Otherwise, your icon may become difficult to read on a light background.
Once you're satisfied with the icon's design, save the icon in the cloned
repository'seditor/iconsfolder. The icon name should match the intended
name in a case-sensitive manner. For example, to create an icon for
CPUParticles2D, name the fileCPUParticles2D.svg.
You can also browse all existing icons on theGodot editor iconswebsite.

## Import options for custom icons

For custom icons that are present in projects (as opposed to the engine source code),
there are two import options you should enable:

### Scaling for hiDPI displays

Icons need to be scaled properly on hiDPI displays to ensure they remain
crisp and large enough to be readable.
To ensure the icon is rendered at a correct scale on hiDPI displays, select the
SVG file in the FileSystem dock, enable theEditor > Scale with Editor Scaleoption in the Import dock and clickReimport. Note that this option is
only available for icons in SVG format, as it requires the use of a vector
format to work.

### Color conversion for light editor themes

To ensure the icon has its colors converted when the user is using a light
theme, select the SVG file in the FileSystem dock, enable theEditor > Convert
Colors with Editor Themeoption in the Import dock and clickReimport. Note that this option is only available for icons in SVG
format, as it requires the use of a vector format to work.

## Icon optimization

Because the editor renders SVGs once at load time, they need to be small
in size so they can be efficiently parsed. When thepre-commit hookruns, it automatically optimizes
the SVG usingsvgo.
Note
While this optimization step won't impact the icon's quality noticeably, it
will still remove editor-only information such as guides. Therefore, it's
recommended to keep the source SVG around if you need to make further
changes.

## Integrating and sharing the icons

If you're contributing to the engine itself, you should make a pull request to
add optimized icons toeditor/iconsin the main repository. Recompile the
engine to make it pick up new icons for classes.
It's also possible to create custom icons within a module. If you're creating
your own module and don't plan to integrate it with Godot, you don't need to
make a separate pull request for your icons to be available within the editor
as they can be self-contained.
For specific instructions on how to create module icons, refer toCreating custom module icons.

## Troubleshooting

If icons don't appear in the editor, make sure that:

- Each icon's filename matches the naming requirement as described previously.
Each icon's filename matches the naming requirement as described previously.
- Thesvgmodule is enabled at compile-time (it is enabled by default).
Without this module, icons won't appear in the editor at all.
Thesvgmodule is enabled at compile-time (it is enabled by default).
Without this module, icons won't appear in the editor at all.

## References

- editor/icons
editor/icons

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
