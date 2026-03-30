# Source: https://docs.jit.io/docs/drata-api-integration.md

# Drata API Integration

## Overview

Integrating with Drata API enables you to sync compliance metadata from Drata into Jit for enhanced visibility and control. This integration allows you to:

* Sync Workspaces, Frameworks, Requirements, Controls, and Policies from Drata into Jit
* Centralize your compliance context within Jit's platform
* Maintain up-to-date compliance information across both platforms
* Analyze relationships between policies, controls, and requirements

## Integration steps

* Step 1: Create an API token in your Drata account
* Step 2: Configure the integration in Jit's UI

### Step 1: Create an API Token in Your Drata Account

1. Log in to <https://app.drata.com> > Click on your profile name > `Settings`
2. Click `API Keys`
3. Click `Create API Key`
4. Fill out the Create API Key Form using the guidance below and be sure to save it:
   * **Expiration Date**: We recommend a long expiration date so that your integration does not unexpectedly stop working
   * The following scopes must be enabled:
     * *Controls: Control List - R*
     * *Workspaces: List workspaces - R*
     * *Frameworks: List frameworks - R*
     * *Requirements: List requirements - R*
     * *Policies: List policies - R, Download policies - R, View policy content - R*
5. Copy the API Key and save it somewhere secure!

### Step 2: Configure the Integration in Jit's UI

1. From the Jit platform, navigate to **Settings** > **Integrations**
2. Find the **Drata API** integration card
3. Click **Connect**
4. In the integration modal:
   * The token will be stored as `DRATA_API_TOKEN`
   * Paste your Drata API Token in the token field
5. Click **Save** to complete the integration

Once configured, Jit will begin syncing your compliance metadata from Drata automatically.

## Data Access and Relationships

The integration will sync the following data from Drata:

1. **Workspaces** - Basic workspace information and configuration
2. **Frameworks** - Available compliance frameworks (e.g., SOC 2)
3. **Requirements** - Framework-specific requirements and their descriptions
4. **Controls** - Specific controls and their implementation status
5. **Policies** - Policy metadata and content

### Relationship Analysis

The integration establishes relationships between different compliance components:

1. **Explicit Relationships**:
   * Controls → Requirements
   * Requirements → Frameworks
   * Frameworks → Workspaces

2. **Analyzed Relationships**:
   * Policies → Controls (through content analysis)
   * Policies → Requirements (through content analysis)

These relationships help create a comprehensive view of your compliance landscape within Jit.