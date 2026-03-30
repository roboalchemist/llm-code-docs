# Mediainfo Plugin Documentation

The Mediainfo plugin displays detailed media file information for video and audio files.

## Features

- Display detailed codec information
- Show resolution, bitrate, framerate
- Audio track details (channels, language, codec)
- Subtitle track information
- File duration and container format

## Requirements

- mediainfo command-line tool
- PHP exec() function enabled

## Installation

### Install Mediainfo

```bash
# Debian/Ubuntu
apt-get install mediainfo

# macOS
brew install mediainfo

# Or download from https://mediaarea.net/en/MediaInfo
```

### Verify Installation

```bash
mediainfo --version
```

## Configuration

Edit `plugins/mediainfo/conf.php`:

```php
<?php
// Path to mediainfo binary
$pathToCreatetorrent = '';  // Empty = search PATH

// Or specify full path:
$pathToCreatetorrent = '/usr/bin/mediainfo';
?>
```

## Usage

1. Select a torrent with media files
2. Go to Files tab
3. Click on a video or audio file
4. View detailed mediainfo output

## Output Example

```
General
Format: Matroska
Duration: 00:45:32
File size: 1.46 GiB

Video
Codec: V_MPEGH/ISO/HEVC
Resolution: 3840x2160
Aspect ratio: 16:9
Frame rate: 23.976 fps
Bit rate: 7 500 kb/s

Audio
Codec: A_EAC3
Channels: 6
Language: English
Bit rate: 256 kb/s

Subtitle
Format: UTF-8
Language: English
```

## Troubleshooting

### "Mediainfo not found"

1. Install mediainfo package
2. Set path in configuration
3. Verify web server can execute mediainfo

### Empty Output

- Check file permissions
- Verify mediainfo can read the file
- Look for encoding issues
