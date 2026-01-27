# Source: https://clickwrap-developer.ironcladapp.com/docs/add-a-snapshot-location-to-an-agreed-event.md

# Add a Snapshot Location to an Agreed Event

## Overview

Snapshots enable legal teams to manage and automatically capture visual evidence for clickwrap agreements at scale.

This guide will cover how to add location keys to your Clickwrap implementation to automatically tie visual evidence to tracked acceptances.

## Requirements

To get started, you'll need to ensure that you have the following:

* Create a Location under Ironclad Snapshot Locations
* Location key from a **published** Ironclad Location that contains the URL of the embedded agreement.

## Adding a Snapshot Location

Replace 'location-key' with your location key. Then, place the following code after the JS snippet and `_ps('load')`.

```javascript
_ps('set', 'snapshot_location', 'location-key');
```

Afterward, the location will display the date of last acceptance.