# Radarr Documentation Index

Radarr is a movie collection manager and automation tool (PVR for movies).

**Official Website:** https://radarr.video/
**GitHub Repository:** https://github.com/Radarr/Radarr
**Wiki:** https://wiki.servarr.com/radarr/
**API Documentation:** https://radarr.video/docs/api/

## Contents

### Getting Started

- **00-README.md** - Official project README
- **01-CONTRIBUTING.md** - Contributing guidelines

### API Documentation

- **02-API-V3.md** - Radarr API v3 reference

### Wiki Pages

- **03-Wiki-Installation.md** - Installation guide
- **03-Wiki-Settings.md** - Settings and configuration
- **03-Wiki-Workflow.md** - Workflow and initial setup
- **03-Wiki-Library.md** - Library management
- **03-Wiki-Wanted.md** - Wanted/missing movies

### Configuration

- **03-Wiki-Profiles.md** - Quality and release profiles
- **03-Wiki-Quality.md** - Quality settings
- **03-Wiki-CustomFormats.md** - Custom format configuration

### Advanced

- **03-Wiki-AppData.md** - AppData folder reference
- **03-Wiki-PostgreSQL.md** - PostgreSQL database setup

## API Quick Reference

Radarr provides a comprehensive REST API (v3) for automation and integration.

Access the interactive API documentation at: https://radarr.video/docs/api/

### Common API Endpoints

- `GET /api/v3/movie` - List all movies
- `GET /api/v3/movie/{id}` - Get movie details
- `POST /api/v3/movie` - Add a new movie
- `GET /api/v3/calendar` - Get calendar
- `GET /api/v3/wanted/missing` - Get wanted/missing movies
- `GET /api/v3/profile` - List quality profiles
- `GET /api/v3/customformat` - List custom formats

Requires API key authentication via `X-Api-Key` header or `apikey` query parameter.

## Key Features

- Automatic movie discovery and download
- Full integration with torrent and usenet clients
- Quality profiles and custom formats
- Multiple language support
- Calendar integration
- Wanted/missing movie tracking
- REST API for automation
- Docker support

## Related Projects

The Servarr project includes several related services:

- **Sonarr** - TV series automation (PVR for TV)
- **Lidarr** - Music library management
- **Prowlarr** - Indexer management
- **Bazarr** - Subtitle management

All share similar architecture and API patterns.
