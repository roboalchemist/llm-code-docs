# SABnzbd Documentation Index

SABnzbd is an open-source Usenet binary newsreader and automation tool that automates downloading NZBs from newsgroups.

## Quick Links

- **Official Website**: https://sabnzbd.org
- **GitHub Repository**: https://github.com/sabnzbd/sabnzbd
- **Forum**: https://forums.sabnzbd.org

## Documentation Structure

### API Documentation

1. **API Reference** - Complete REST API endpoints, authentication, and response formats
   - Queue functions (pause, resume, add, delete, priority management)
   - History functions (retrieve completed jobs, retry, statistics)
   - Status monitoring (CPU, disk space, server stats)
   - Configuration management and utilities

### Configuration

1. **General Settings** - Basic SABnzbd configuration
2. **Folder Configuration** - Directory paths for downloads and temporary files
3. **Server Configuration** - Usenet server setup and credentials
4. **Categories** - Job categorization and routing
5. **Sorting** - Post-processing job sorting rules
6. **Switches** - Feature toggles and performance settings

### Installation & Setup

1. **Windows Installation** - Windows-specific installation instructions
2. **macOS Installation** - macOS-specific installation instructions
3. **Linux Installation** - Linux distribution installation guides
4. **Quick Start Guide** - Getting started with SABnzbd

### Scripting & Automation

1. **Post-Processing Scripts** - Scripts that run after downloads complete
2. **Pre-Queue Scripts** - Scripts that filter/modify NZBs before queueing

### Advanced Topics

1. **HTTPS/SSL Setup** - Secure web interface configuration
2. **Command Line Options** - CLI parameters and startup configuration
3. **High-Speed Tweaks** - Performance optimization settings

## Common Use Cases

### Integration with Sonarr/Radarr

SABnzbd serves as the download engine for Sonarr (TV) and Radarr (Movies):

- Configure API key in SABnzbd settings
- Use API endpoint: `http://host:port/api`
- Support for job categories, post-processing scripts, and priority control

### Automation & Monitoring

- Use the REST API to programmatically manage downloads
- Monitor queue status and history
- Implement custom post-processing workflows with scripts
- Setup RSS feeds for automatic NZB discovery

## Version Information

This documentation is for SABnzbd 4.5 (latest stable version at time of scraping).
