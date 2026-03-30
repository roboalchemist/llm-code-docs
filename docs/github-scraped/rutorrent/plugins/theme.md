# Theme Plugin Documentation

The Theme plugin enables custom theming and visual customization of ruTorrent.

## Features

- Multiple built-in themes
- Custom CSS support
- Theme-specific icons and graphics
- Persistent user theme preferences

## Built-in Themes

| Theme | Description |
|-------|-------------|
| Default | Standard ruTorrent appearance |
| Dark | Dark theme variant |
| Light | Light theme variant |

## Usage

1. Go to Settings > General
2. Select Theme from dropdown
3. Theme changes apply immediately

## Custom Themes

### Creating a Custom Theme

1. Create theme directory:

   ```bash
   mkdir -p plugins/theme/themes/mytheme
   ```

2. Create CSS file:

   ```css
   /* plugins/theme/themes/mytheme/style.css */
   body {
       background: #1a1a2e;
       color: #eee;
   }

   .torrent {
       border-color: #16213e;
   }
   ```

3. Register theme in init.php:

   ```php
   $themeList['mytheme'] = 'My Custom Theme';
   ```

### Theme Variables

Common CSS variables to customize:

```css
:root {
    --bg-primary: #1a1a2e;
    --bg-secondary: #16213e;
    --text-primary: #eee;
    --text-secondary: #aaa;
    --accent: #0f3460;
    --border: #e94560;
}
```

## Configuration

Edit `plugins/theme/conf.php`:

```php
<?php
// Default theme for new users
$defaultTheme = 'default';

// Allow users to change theme
$allowUserTheme = true;
?>
```

## Icons

Custom icons can be placed in:

```text
plugins/theme/themes/mytheme/images/
```

### Icon Naming

- `favicon.ico` - Favicon
- `logo.png` - Header logo
