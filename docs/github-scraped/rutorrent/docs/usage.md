# ruTorrent Usage Guide

## Interface Overview

### Top Menu Bar

Quick action buttons for:

- Adding torrents
- Removing torrents
- Starting/stopping/pausing
- Accessing settings
- Plugin features (Create, RSS, etc.)

### Left Side Menu

Organize torrents by:

| Category | Description |
|----------|-------------|
| All | View all torrents |
| Download | Active downloads |
| Finished | Completed downloads |
| Active | Currently uploading/downloading |
| Inactive | Paused or stopped |
| Error | Torrents with errors |
| Labels | Custom category labels |
| Tracker | Grouped by tracker |
| Search | Filter current view |
| Feeds | RSS feed items |

### Main Tabs

| Tab | Description |
|-----|-------------|
| General | Torrent details and status |
| Info | Detailed torrent information |
| Files | File list within torrent |
| Trackers | Tracker status and peers |
| Peers | Connected peers |
| Speed | Upload/download graphs |
| Plugins | Plugin-specific content |
| Traffic | Traffic statistics |
| Chunks | Chunk visualization |
| Logger | Activity log |

### Bottom Status Bar

- Total upload/download speed
- Server throttle controls
- Remaining disk space

## Adding Torrents

### Method 1: Upload .torrent File

1. Click the **Add** button in the toolbar
2. Select **Browse** to upload a .torrent file
3. Optionally set download directory
4. Click **OK**

### Method 2: URL Download

1. Click the **Add** button
2. Select **URL** tab
3. Enter the torrent URL (`.torrent` file URL)
4. Optionally set download directory
5. Click **OK**

### Method 3: Drag and Drop

1. Drag a `.torrent` file onto the main window
2. Optionally set download directory
3. Click **OK**

## Torrent Controls

### Individual Torrent Actions

Right-click on a torrent for context menu:

| Action | Description |
|--------|-------------|
| Start | Begin downloading/seeding |
| Pause | Pause activity |
| Stop | Stop and retain data |
| Remove | Delete torrent and optionally data |
| Force Start | Start ignoring seed limits |
| Force Recheck | Verify torrent data |
| Execute Command | Run custom command |

### Batch Operations

Select multiple torrents (Ctrl+click or Shift+click) to:

- Start/Stop/Pause all selected
- Set labels
- Set download priority
- Remove selected

## Torrent Properties

Right-click -> Properties for:

| Property | Description |
|----------|-------------|
| Maximum peers | Max connected peers |
| Upload slots | Upload slot limit |
| Seed ratio | Target seed ratio |
| Priority | Download priority |
| Trackers | Add/edit tracker list |

## Labels

Labels help organize torrents by category, tracker, or any custom grouping.

### Creating Labels

1. Right-click in the label area
2. Select **Add Label**
3. Enter label name
4. Assign torrents by dragging or context menu

### Label-based Filtering

Click a label in the sidebar to filter the torrent list.

## Search and Filter

### Local Search

Use the search box in the toolbar to filter the current torrent list.

### Persistent Searches

Create saved searches in the sidebar:

1. Right-click **Search** in sidebar
2. Select **Add Search**
3. Enter search criteria
4. Search appears as sidebar item

## RSS Feeds

See [RSS Plugin Documentation](../plugins/rss.md) for detailed RSS usage.

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| Enter | Open selected torrent |
| Delete | Remove selected torrent |
| Space | Toggle selection |
| Ctrl+A | Select all |
| Escape | Deselect all |

## Managing Disk Space

### Setting Download Directories

Configure in Settings -> Directories:

- **Download to**: Default download location
- **Move completed to**: Archive completed downloads

### Cleanup Options

Right-click -> Erase Data to:

- Remove data files
- Keep torrent entry for re-download
