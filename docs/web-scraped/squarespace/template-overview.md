# Template Overview

## Core Concept

Squarespace templates follow a static website structure with predefined folders and files that work together to create dynamic sites.

## Languages & Technologies

### JSON Template

The primary templating language for Squarespace, described as "an easy to use, easy to read, minimalist template language" that produces HTML-compatible templates.

### LESS CSS

Template stylesheets use LESS processing, which "extends CSS with dynamic behavior such as variables, mixins, operations and functions."

## Directory Structure

The root folder organization includes:

### /assets/

- Template-specific design files (images, fonts, icons)
- Per-file limit of 10MB

### /blocks/

- Reusable component templates
- Configurations for navigation elements

### /collections/

- Content presentation templates for various post types
- Supports unlimited collection types per site

### /pages/

- Static HTML pages not editable by end users

### /scripts/

- JavaScript files for site functionality

### /styles/

- CSS/LESS stylesheets merged into site.css

### /site.region

- Global site wrapper template for headers, footers, sidebars

### /template.conf

- Core template configuration and settings

## Collections System

Collections define how different content types display. Each collection requires:

- **.list** files - Templates for collection list views
- **.item** files - Templates for individual item pages (permalinks)
- **.conf** files - Collection configuration settings

This system supports unlimited collection types per site, with options for chronological sorting (like a blog) or user-ordered arrangements (like a gallery).

### Blog Collections

Collections are commonly used for blogs. The system supports:

- List view templates for displaying multiple blog posts
- Item templates for individual post pages
- Chronological sorting by default
- Category and tag organization

### Gallery Collections

For gallery-like presentations:

- User-ordered arrangements
- Custom sorting and filtering
- Image presentation templates

## Template Configuration

All templates require a `template.conf` file written in JSON format containing:

- Template metadata (name, author)
- Layout definitions
- Navigation configuration
- Stylesheet listings
