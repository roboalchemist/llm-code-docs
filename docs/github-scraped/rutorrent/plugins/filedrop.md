# FileDrop Plugin Documentation

The FileDrop plugin enables drag-and-drop file upload for adding torrents.

## Features

- Drag and drop .torrent files directly into the browser
- Multi-file support
- Works with modern browsers (Chrome, Firefox, Safari, Edge)
- File validation before upload

## Requirements

- Modern browser with HTML5 File API
- Flash plugin NOT required (uses native HTML5)

## Usage

1. Drag one or more .torrent files from your computer
2. Drop onto the ruTorrent window
3. Configure download settings if prompted
4. Click Upload or OK

## Configuration

Edit `plugins/filedrop/conf.php`:

```php
<?php
// Enable/disable
$enabled = true;

// Maximum file size (bytes)
$max_file_size = 1024 * 1024;  // 1 MB

// Allowed extensions
$allowed_extensions = ['torrent'];
?>
```

## Browser Compatibility

| Browser | Support |
|---------|---------|
| Chrome 7+ | Full |
| Firefox 4+ | Full |
| Safari 6+ | Full |
| Edge 12+ | Full |
| IE 10+ | Limited |

## Troubleshooting

### Drop Zone Not Appearing

1. Ensure plugin is enabled
2. Check browser console for errors
3. Verify JavaScript is enabled

### Files Not Uploading

- Check PHP upload limits (post_max_size, upload_max_filesize)
- Verify temp directory is writable
- Check file permissions
