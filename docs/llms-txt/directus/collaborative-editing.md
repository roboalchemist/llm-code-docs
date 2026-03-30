# Source: https://directus.io/docs/raw/guides/content/collaborative-editing.md

# Collaborative Editing

> Directus Collaborative Editing enables real-time data synchronization and collaborative editing across collections, allowing multiple users to edit content simultaneously without conflicts.

![Collaborative editing thumbnail](/img/collaborative-post.png)

Collaborative Editing transforms your Directus project into a real-time collaborative platform where multiple users can edit content simultaneously. This feature provides conflict-free collaborative editing through smart field locking, user awareness indicators, and instant synchronization across all connected clients.

This documentation covers everything you need to know about configuring, using, and developing with collaborative editing in your Directus projects.

## Overview Video

<div style="padding:56.33% 0 0 0;position:relative;">
<iframe src="https://www.youtube.com/embed//R2Tx35sLm3I" frameBorder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Directus-Visual-Editor-Preview">



</iframe>
</div>

## Key Features

- **Real-time Collaboration** - Multiple users edit simultaneously with instant synchronization
- **Smart Field Locking** - Automatic conflict prevention through field-level locking
- **User Awareness** - Visual indicators show who's editing what in real-time
- **Universal Support** - Works across collections, file library, user directory, and relationships
- **Easy Configuration** - Deploy globally across your project

## How It Works

Collaborative Editing provides a sophisticated real-time collaboration experience:

<table>
<thead>
  <tr>
    <th>
      Feature
    </th>
    
    <th>
      Traditional Way
    </th>
    
    <th>
      Collaborative Editing
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <strong>
        User Awareness
      </strong>
    </td>
    
    <td>
      No visibility of other users
    </td>
    
    <td>
      Real-time avatars show who's editing
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Conflict Prevention
      </strong>
    </td>
    
    <td>
      Manual coordination required
    </td>
    
    <td>
      Automatic field locking prevents conflicts
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Real-time Updates
      </strong>
    </td>
    
    <td>
      Manual refresh needed
    </td>
    
    <td>
      Instant synchronization across all users
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Relationship Editing
      </strong>
    </td>
    
    <td>
      Limited to single users
    </td>
    
    <td>
      Multiple users can edit related content
    </td>
  </tr>
</tbody>
</table>

## Getting Started

Follow these guides to set up collaborative editing in your Directus project:

<callout color="primary" icon="material-symbols:settings-suggest-rounded" to="/guides/content/collaborative-editing/configuration">

**Configuration**
Configure settings and environment variables.

</callout>

<callout color="secondary" icon="material-symbols:menu-book-outline" to="/guides/content/collaborative-editing/usage">

**Usage Guide**
Learn the basics of collaborative editing.

</callout>

<callout color="green" icon="material-symbols:code-blocks-rounded" to="/guides/content/collaborative-editing/development">

**Development & Custom Extensions**
Integrate with custom interfaces.

</callout>

## Requirements

- **Directus 11.15.0 or higher**
- **WebSockets enabled** in your Directus configuration

## Technology Overview

The feature uses a custom WebSocket implementation for real-time synchronization and smart field locking to prevent conflicts. All collaborative actions respect Directus user permissions and access controls.

## Next Steps

<callout color="primary" icon="material-symbols:arrow-forward-rounded" to="/guides/content/collaborative-editing/configuration">

**Ready to get started?**
Start with the Configuration guide to get up and running.

</callout>

Transform your Directus project into a collaborative workspace where teams can work together seamlessly on content creation and management.
