# Style Editor

## Overview

The Style Editor enables developers to allow users to customize design elements through an intuitive interface without requiring CSS knowledge. Customizations are managed through "tweaks"—LESS variables paired with JSON configuration objects.

## Basic Syntax

Tweaks are defined in CSS/LESS files using comments with a specific format:

```css
// tweak: { "type" : "value", "title" : "Page Width", "min" : 500, "max" : 1400 }
@pageWidth: 600px;
```

**Critical requirement:** Comments must begin with exactly two forward slashes and a space before the tweak definition.

## Tweak Types

### Value

Range sliders that return measurement units with configurable min/max values, step increments, and sensitivity settings.

Example:

```css
// tweak: { "type": "value", "title": "Font Size", "min": 12, "max": 48, "step": 1 }
@baseFontSize: 16px;
```

### Color

Color picker returning colors in the original CSS format (hex, rgba, etc.).

Example:

```css
// tweak: { "type": "color", "title": "Primary Color" }
@primaryColor: #3498db;
```

### Typography

Provides font customization options matching CSS properties:

- Font family
- Font weight
- Font size
- Letter spacing
- Line height
- Text transform

Example:

```css
// tweak: { "type": "typography", "title": "Heading Font" }
@headingFont: Georgia, serif;
```

### Checkbox

Toggles a CSS class on the body element when activated, enabling conditional styling.

Example:

```css
// tweak: { "type": "checkbox", "title": "Dark Mode" }
@darkModeEnabled: false;
```

### Dropdown

Applies selected class to body element based on user choice from defined options.

Example:

```css
// tweak: { "type": "dropdown", "title": "Layout", "options": ["wide", "narrow", "fluid"] }
@layoutType: wide;
```

### Image

Upload field for presentational images, particularly useful for background images in CSS.

Example:

```css
// tweak: { "type": "image", "title": "Background Image" }
@bgImage: "";
```

## Organization Features

### Categories

Group related tweaks by adding a `"category"` key/value pair; matching values group tweaks under shared headings.

Example:

```css
// tweak: { "type": "value", "title": "Page Width", "category": "Layout", "min": 500, "max": 1400 }
@pageWidth: 600px;

// tweak: { "type": "value", "title": "Sidebar Width", "category": "Layout", "min": 200, "max": 400 }
@sidebarWidth: 300px;
```

### Targets

Allow users to click elements and view associated style options using the `"target"` property with CSS selectors.

Example:

```css
// tweak: { "type": "color", "title": "Button Color", "target": "button" }
@buttonColor: #3498db;
```

### showOnlyWhenPresent

Display tweaks conditionally based on HTML element presence (comma-separated selectors).

Example:

```css
// tweak: { "type": "color", "title": "Sidebar Color", "showOnlyWhenPresent": ".sidebar, aside" }
@sidebarColor: #ecf0f1;
```

## JavaScript Integration

Developers can access tweak values and listen for changes in custom JavaScript.

### Retrieve Tweak Values

```javascript
Y.Squarespace.Template.getTweakValue('variableName')
```

### Listen for Tweak Changes

```javascript
Y.Global.on('tweak:change', function(f) {
  // Handle tweak change
  var newValue = Y.Squarespace.Template.getTweakValue('variableName');
  console.log('Tweak changed to:', newValue);
});
```

### Listen for Tweak Resets

```javascript
Y.Global.on('tweak:reset', function(f) {
  // Handle tweak reset to default
});
```

### Enable JavaScript Access

Add `"js" : true` to the tweak definition to enable JavaScript integration:

```css
// tweak: { "type": "value", "title": "Page Width", "min": 500, "max": 1400, "js": true }
@pageWidth: 600px;
```

Once enabled, retrieve the value in your custom script:

```javascript
var pageWidth = Y.Squarespace.Template.getTweakValue('pageWidth');
```

## Complete Example

```css
// tweak: { "type": "color", "title": "Link Color", "category": "Typography", "js": true }
@linkColor: #0088cc;

// tweak: { "type": "typography", "title": "Body Font", "category": "Typography" }
@bodyFont: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;

// tweak: { "type": "value", "title": "Padding", "category": "Spacing", "min": 0, "max": 100, "step": 5 }
@basePadding: 20px;

// tweak: { "type": "checkbox", "title": "Show Sidebar", "category": "Layout" }
@showSidebar: true;
```

## User Experience

When tweaks are properly configured, users access style customization through the Style Editor in Squarespace's design interface without needing to know CSS or edit code directly.
