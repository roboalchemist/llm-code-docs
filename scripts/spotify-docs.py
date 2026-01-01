#!/usr/bin/env python3
"""
Optimized scraper for Spotify Web API documentation.
Focuses on key documentation sections without scraping all 100+ endpoint pages.
Output: docs/web-scraped/spotify/
"""
import requests
from pathlib import Path
from urllib.parse import urljoin
import re
from typing import Dict, List

OUTPUT_DIR = Path(__file__).parent / "docs" / "web-scraped" / "spotify"
BASE_URL = "https://developer.spotify.com"

# Key documentation pages to scrape
KEY_PAGES = {
    'index': f"{BASE_URL}/documentation/web-api",
    'getting-started': f"{BASE_URL}/documentation/web-api/getting-started",
    'access-token': f"{BASE_URL}/documentation/web-api/concepts/access-token",
    'api-calls': f"{BASE_URL}/documentation/web-api/concepts/api-calls",
    'apps': f"{BASE_URL}/documentation/web-api/concepts/apps",
    'playlists': f"{BASE_URL}/documentation/web-api/concepts/playlists",
    'quota-modes': f"{BASE_URL}/documentation/web-api/concepts/quota-modes",
    'rate-limits': f"{BASE_URL}/documentation/web-api/concepts/rate-limits",
    'scopes': f"{BASE_URL}/documentation/web-api/concepts/scopes",
    'spotify-uris-ids': f"{BASE_URL}/documentation/web-api/concepts/spotify-uris-ids",
    'track-relinking': f"{BASE_URL}/documentation/web-api/concepts/track-relinking",
    'redirect-uri': f"{BASE_URL}/documentation/web-api/concepts/redirect_uri",
}

def html_to_markdown(html_content: str) -> str:
    """Convert HTML content to basic Markdown"""
    # Remove script and style tags
    content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)

    # Convert headers
    content = re.sub(r'<h1[^>]*>(.*?)</h1>', r'# \1\n', content, flags=re.IGNORECASE)
    content = re.sub(r'<h2[^>]*>(.*?)</h2>', r'## \1\n', content, flags=re.IGNORECASE)
    content = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1\n', content, flags=re.IGNORECASE)
    content = re.sub(r'<h4[^>]*>(.*?)</h4>', r'#### \1\n', content, flags=re.IGNORECASE)
    content = re.sub(r'<h5[^>]*>(.*?)</h5>', r'##### \1\n', content, flags=re.IGNORECASE)
    content = re.sub(r'<h6[^>]*>(.*?)</h6>', r'###### \1\n', content, flags=re.IGNORECASE)

    # Convert code blocks
    content = re.sub(r'<pre[^>]*>(.*?)</pre>', r'```\n\1\n```\n', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', content, flags=re.IGNORECASE)

    # Convert bold and italic
    content = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', content, flags=re.IGNORECASE)
    content = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', content, flags=re.IGNORECASE)
    content = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', content, flags=re.IGNORECASE)
    content = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', content, flags=re.IGNORECASE)

    # Convert line breaks and paragraphs
    content = re.sub(r'<br\s*/?>', '\n', content, flags=re.IGNORECASE)
    content = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', content, flags=re.DOTALL | re.IGNORECASE)

    # Convert lists
    content = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<ul[^>]*>|</ul>|<ol[^>]*>|</ol>', '', content, flags=re.IGNORECASE)

    # Convert links
    content = re.sub(r'<a[^>]*href=["\'](.*?)["\']*[^>]*>(.*?)</a>', r'[\2](\1)', content, flags=re.IGNORECASE)

    # Remove remaining HTML tags
    content = re.sub(r'<[^>]+>', '', content)

    # Decode HTML entities
    entities = {
        '&nbsp;': ' ', '&lt;': '<', '&gt;': '>', '&amp;': '&',
        '&quot;': '"', '&#39;': "'", '&apos;': "'", '&#x27;': "'"
    }
    for entity, char in entities.items():
        content = content.replace(entity, char)

    # Clean up excessive whitespace
    content = re.sub(r'\n{3,}', '\n\n', content)
    content = content.strip()

    return content

def fetch_url(url: str) -> str:
    """Fetch URL content"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""

def scrape_page(url: str, title: str) -> Dict:
    """Scrape a single page"""
    print(f"Scraping {title}...")
    html = fetch_url(url)
    if not html:
        return None

    markdown = html_to_markdown(html)
    full_content = f"# Source: {url}\n\n# {title}\n\n{markdown}"

    return {
        'title': title,
        'url': url,
        'content': full_content
    }

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Starting Spotify Web API documentation scrape...")
    print(f"Output directory: {OUTPUT_DIR}")
    print(f"Scraping {len(KEY_PAGES)} key pages\n")

    # Scrape key pages
    scraped = []
    for name, url in KEY_PAGES.items():
        page = scrape_page(url, name.replace('-', ' ').title())
        if page:
            scraped.append((name, page))

    # Write main index
    index_content = """# Source: https://developer.spotify.com/documentation/web-api

# Spotify Web API Documentation

Official documentation for the Spotify Web API, which enables apps to retrieve metadata (artists, albums, tracks), search content, manage playlists, control playback, and more.

## Overview

The Spotify Web API is a RESTful API that provides access to music metadata and user information from Spotify. It allows developers to:

- Search for artists, albums, and tracks
- Get metadata about music content
- Access user profile information and listening history
- Create and modify playlists
- Control playback on Spotify devices
- Get audio analysis and features for tracks
- Access user's saved tracks and playlists
- Manage user library and preferences

## Key Concepts

### Authentication

The Spotify Web API uses OAuth 2.0 for authentication. Several authorization flows are available:

- **Authorization Code Flow** - For user-authenticated applications
- **Client Credentials Flow** - For server-to-server authentication
- **Implicit Flow** - For browser-based applications
- **PKCE Flow** - For mobile and desktop applications

### Rate Limiting

The Web API enforces rate limiting on a per-application basis. Rate limits are specified in terms of requests per second. If the rate limit is exceeded, the API will return a 429 (Too Many Requests) response.

### Quota Modes

Quota modes determine how many minutes of streaming content a user can listen to in a given period. The API provides information about the user's current quota.

### Spotify URIs and IDs

Each Spotify resource (artist, album, track, etc.) has a unique Spotify URI and ID. These identifiers are used to reference resources in the API.

## Getting Started

To get started with the Spotify Web API:

1. Register your application at the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Accept the developer agreement
3. Create an app and select "Web API"
4. Obtain your Client ID and Client Secret
5. Choose an authorization flow appropriate for your use case
6. Make your first API request

## Quick Links

- Official Documentation: https://developer.spotify.com/documentation/web-api
- Developer Dashboard: https://developer.spotify.com/dashboard
- Community Forum: https://community.spotify.com/t5/Spotify-for-Developers/ct-p/spotify-developers
- OpenAPI Schema: https://developer.spotify.com/_data/documentation/web-api/reference/open-api-schema.yml

## Common Use Cases

### Search

Search for artists, albums, tracks, playlists, shows, and episodes.

**Endpoint:** `GET /v1/search`

### User Data

Get information about the authenticated user's profile and listening history.

**Key Endpoints:**
- `GET /v1/me` - Get current user's profile
- `GET /v1/me/player` - Get user's currently playing track
- `GET /v1/me/top/tracks` - Get user's top tracks
- `GET /v1/me/top/artists` - Get user's top artists

### Playlists

Create, modify, and manage playlists.

**Key Endpoints:**
- `GET /v1/playlists/{playlist_id}` - Get playlist details
- `POST /v1/users/{user_id}/playlists` - Create playlist
- `POST /v1/playlists/{playlist_id}/tracks` - Add tracks to playlist

### Playback Control

Control playback on Spotify devices.

**Key Endpoints:**
- `PUT /v1/me/player/play` - Start playback
- `PUT /v1/me/player/pause` - Pause playback
- `POST /v1/me/player/next` - Skip to next track
- `POST /v1/me/player/previous` - Skip to previous track

### Audio Analysis

Get detailed audio features and analysis for tracks.

**Key Endpoints:**
- `GET /v1/audio-features/{track_id}` - Get audio features
- `GET /v1/audio-analysis/{track_id}` - Get detailed audio analysis

## Documentation Structure

This documentation is organized into the following sections:

- **Concepts** - Foundational topics like authentication, rate limiting, and resource identifiers
- **Tutorials** - Step-by-step guides for implementing common features
- **How-Tos** - Practical guides for specific tasks
- **API Reference** - Complete endpoint documentation with request/response examples

## Community & Support

- **Community Forum:** https://community.spotify.com/t5/Spotify-for-Developers/ct-p/spotify-developers
- **Documentation:** https://developer.spotify.com/documentation
- **GitHub Examples:** https://github.com/spotify/web-api-examples
- **Status Page:** https://developer.spotify.com/status

## Libraries & SDKs

Several third-party libraries provide convenient interfaces to the Spotify Web API:

- **Spotipy** (Python) - Lightweight Python library with full Web API access
- **spotify-web-api-ts-sdk** (TypeScript) - TypeScript SDK with types
- **SpotifyAPI** (Swift) - Swift library for iOS development
- **Web Playback SDK** - JavaScript SDK for browser-based playback control

## License & Terms

Use of the Spotify Web API is subject to the [Spotify Developer Terms of Service](https://developer.spotify.com/terms).
"""

    # Write pages
    written_count = 0
    for name, page in scraped:
        filename = f"{name}.md"
        filepath = OUTPUT_DIR / filename
        filepath.write_text(page['content'], encoding='utf-8')
        print(f"Written: {filename}")
        written_count += 1

    # Write main index
    (OUTPUT_DIR / 'index.md').write_text(index_content, encoding='utf-8')
    print(f"Written: index.md")

    print(f"\nScraping complete!")
    print(f"Total files written: {written_count + 1}")

    # Verify
    md_files = list(OUTPUT_DIR.glob('*.md'))
    total_size = sum(f.stat().st_size for f in md_files)
    print(f"Verification: {len(md_files)} markdown files, {total_size / 1024:.1f} KB total")

if __name__ == '__main__':
    main()
