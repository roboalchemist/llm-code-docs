# Source: https://developer.spotify.com/documentation/web-api

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
