# Source: https://redocly.com/docs/realm/config/color-mode.md

# Source: https://redocly.com/docs/realm/branding/color-mode.md

# Color mode

Color mode is an interactive feature that allows users to change the visual theme of the documentation to tailor their reading experience.
But there's more to color mode than user convenience; it can have implications on health, accessibility, productivity, and more.

## Types of color mode

By clicking the color mode button in the top right of the navbar, users can switch between pre-defined color schemes according to their needs.
Every Redocly project includes light and dark mode out-of-the-box.
It's also possible to add [new, custom color modes](/docs/realm/branding/customize-color-modes#add-new-color-modes) using React code.

### Light mode ![light icon](/assets/theme-light.fe48fe5ad7e966171bd7a280fbf86cd6b5662ce86ba327600a347eefbc266ceb.7dee107e.svg)

Light mode displays dark text on a light background.
In well-lit environments, the increased contrast between the text and background can reduce glare and make reading more comfortable.

### Dark mode ![dark icon](/assets/theme-dark.89eefb6e6573f6936fac823e6a2499a92b8dd15928ce104a57d136f793a81c6e.7dee107e.svg)

Dark mode reverses the traditional "light-background, dark-text" configuration.
Instead, it dark mode presents lighter colors against a dark background.
It's favored in low-light conditions or by users that find bright screens uncomfortable.

## Color mode implementation

The navbar of your documentation contains an icon representing the color mode, such as light ( ![light icon](/assets/theme-light.fe48fe5ad7e966171bd7a280fbf86cd6b5662ce86ba327600a347eefbc266ceb.7dee107e.svg) ) or dark ( ![dark icon](/assets/theme-dark.89eefb6e6573f6936fac823e6a2499a92b8dd15928ce104a57d136f793a81c6e.7dee107e.svg) ).
When a user switches the color mode, the documentation's CSS dynamically changes to the corresponding color scheme throughout all content.
Additionally, the user's color mode is set in their local storage so their preferred color mode is applied when they return to your documentation.

### How color mode works

The color mode feature uses [CSS variables](/docs/realm/branding/css-variables) and color-mode-specific styling rules, allowing users to instantly transition between color schemes without reloading the page.

#### CSS variables as building blocks

The core theme defines a set of foundational CSS variables for things like colors and fonts.
These foundational variables are then used to define more specific CSS variables tailored for individual elements.
This approach helps maintain a cohesive look and feel while offering powerful customization.

#### Separate sets of styling rules

Each color mode draws from its own distinct set of styling rules.
The documentation switches between them when the user changes the color mode.
You can add your own, color-mode-specific styling rules by overriding the CSS variables, which you can learn about using the resources listed below.

## Resources

- **[Custom styles guide](/docs/realm/branding/customize-styles)** - Learn to customize your documentation's appearance using CSS variables and custom stylesheets
- **[Color mode customization](/docs/realm/branding/customize-color-modes)** - Create custom styling for light and dark modes with mode-specific color schemes and CSS rules
- **[Custom color modes](/docs/realm/branding/customize-color-modes#add-new-color-modes)** - Expand beyond the default light and dark modes by adding completely new color modes with custom icons and styling
- **[CSS variables reference](/docs/realm/branding/css-variables)** - Complete dictionary of CSS variables used by the color mode system for advanced customization