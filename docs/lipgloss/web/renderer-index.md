lipgloss
# Module renderer 
Source 
## Structs§
OutputOutput configuration for terminal capabilities.RendererRenderer stores environment-specific rendering options such as
the detected color profile and whether the terminal background is dark.
## Enums§
ColorProfileKindColor profiles supported by the renderer. Mirrors termenv’s profiles.
## Functions§
color_profileGet the current color profile from the default renderer.default_rendererGet a reference to the default renderer.has_dark_backgroundQuery whether the default renderer assumes a dark background.set_color_profileSet the color profile on the default renderer.set_default_rendererReplace the global default renderer.set_has_dark_backgroundSet dark background flag on the default renderer.