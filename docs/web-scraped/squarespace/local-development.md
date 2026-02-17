# Local Development

## Overview

The Squarespace Local Development Server is a command-line tool that enables template development on your local machine. It "sets up a test server on your computer, allowing you to see changes to your template before making them live."

## Prerequisites

- A website configured with developer mode enabled
- Your site cloned locally via Git

## Installation

### Step 1: Install Node Package Manager (NPM)

If Node Package Manager isn't already installed, follow the [NPM installation guide](https://docs.npmjs.com/getting-started/installing-node). Ensure proper permissions are configured as documented in [NPM's permission guide](https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally).

### Step 2: Install the Development Server

Run this command to install globally:

```bash
npm install -g @squarespace/server
```

This installs the Squarespace development server as a global command-line tool.

## Getting Started

### Basic Setup

Navigate to your cloned repository and launch the development environment:

```bash
git clone https://github.com/{{ your_org }}/{{ your_repo }}.git
cd {{ your_repo }}
squarespace-server https://site-name.squarespace.com
```

The server runs on port 9000 by default. Access your site at `http://localhost:9000` and template modifications will appear on page refresh.

### Standard Workflow

1. Clone your site repository to your local machine
2. Start the development server with your site URL
3. Open the site in your browser at localhost:9000
4. Edit template files locally
5. Refresh browser to see changes immediately
6. Commit changes to Git and push to deploy

## Important Notes

### Trial Sites
Trial sites require the `--auth` flag during startup:
```bash
squarespace-server https://site-name.squarespace.com --auth
```

### CMS Structure Requirements
Custom collections, post types, and static pages must be committed and pushed to Squarespace before local preview. Once pushed, these items can be edited locally after creating them in the CMS.

### Preview Limitations
The local development server previews template changes but cannot create new content types—those must be defined in the CMS interface.

## Advanced Options

### View All Commands
```bash
squarespace-server --help
```

### Common Options

#### Directory
Specify template source location:
```bash
squarespace-server https://site-name.squarespace.com -d, --directory=/path/to/template
```

#### Port
Change server port:
```bash
squarespace-server https://site-name.squarespace.com -p, --port=8080
```

#### Authentication
Authenticate for password-protected or trial sites:
```bash
squarespace-server https://site-name.squarespace.com --auth
```

#### Verbose Logging
Enable detailed logging:
```bash
squarespace-server https://site-name.squarespace.com --verbose
```

## Accessing Assets

### Site CSS
For local development, access compiled CSS at:

```
http://localhost:9000/local-assets/site.css
```

This endpoint is exclusive to the local development server and allows inspection of LESS compilation results.

## Development Best Practices

### Live Reloading
The local development server automatically reflects changes when you refresh your browser. No need to restart the server for template modifications.

### CSS and JavaScript
Changes to stylesheets and scripts in `/styles/` and `/scripts/` directories are reflected immediately on refresh.

### Collection Changes
If you modify collection configurations or add new collections:
1. Commit and push changes to the repository
2. Verify they're visible in the CMS
3. Refresh the local development server

### Performance Testing
Use the local development environment to test:
- Template rendering performance
- JavaScript execution and event handling
- CSS rendering and layout responsiveness
- Asset loading and optimization

## Troubleshooting

### Server Won't Start
- Verify NPM is installed: `npm --version`
- Ensure port 9000 is not in use
- Check that your site URL is correct
- Verify you have developer mode enabled

### Changes Not Appearing
- Ensure you're accessing http://localhost:9000 (not localhost:8000 or another port)
- Clear browser cache (Ctrl+Shift+Delete or Cmd+Shift+Delete)
- Verify files are saved locally
- Check terminal for error messages with `--verbose` flag

### Port Already in Use
Use the `-p` flag to specify a different port:
```bash
squarespace-server https://site-name.squarespace.com -p 8080
```

## Support

Questions or feedback should be directed to [Squarespace support](https://support.squarespace.com/hc/requests/new?ticket_form_id=64347&subtopic_value=top::design:code-developerplatform), mentioning the Local Development Server specifically.
