# Source: https://flatfile.com/docs/embedding/advanced-configuration.md

# Advanced Configuration

> Complete configuration reference for embedded Flatfile

This reference covers all configuration options for embedded Flatfile, from basic setup to advanced customization.

## Authentication & Security

### publishableKey

Your publishable key authenticates your application with Flatfile. This key is safe to include in client-side code.

**Where to find it:**

1. Log into [Platform Dashboard](https://platform.flatfile.com)
2. Navigate to **Developer Settings** → **API Keys**
3. Copy your **Publishable Key** (starts with `pk_`)

```javascript
// Example usage
const config = {
  publishableKey: "pk_1234567890abcdef", // Your actual key
};
```

### Security Best Practices

#### Environment Variables

Store your publishable key in environment variables rather than hardcoding:

```javascript
// ✅ Good - using environment variable
const config = {
  publishableKey: process.env.REACT_APP_FLATFILE_KEY,
};

// ❌ Avoid - hardcoded keys
const config = {
  publishableKey: "pk_1234567890abcdef",
};
```

## Common Configuration Options

These options are shared across all SDK implementations:

### Authentication

| Option           | Type   | Required | Description                                  |
| ---------------- | ------ | -------- | -------------------------------------------- |
| `publishableKey` | string | ✅        | Your publishable key from Platform Dashboard |

### User Identity

| Option                 | Type   | Required | Description                                                                     |
| ---------------------- | ------ | -------- | ------------------------------------------------------------------------------- |
| `userInfo`             | object | ❌        | User metadata for space creation                                                |
| `userInfo.userId`      | string | ❌        | Unique user identifier                                                          |
| `userInfo.name`        | string | ❌        | User's display name - this is displayed in the dashboard as the associated user |
| `userInfo.companyId`   | string | ❌        | Company identifier                                                              |
| `userInfo.companyName` | string | ❌        | Company display name                                                            |
| `externalActorId`      | string | ❌        | Unique identifier for embedded users                                            |

### Space Setup

| Option          | Type     | Required | Description                               |
| --------------- | -------- | -------- | ----------------------------------------- |
| `name`          | string   | ✅        | Name of the space                         |
| `environmentId` | string   | ✅        | Environment identifier                    |
| `spaceId`       | string   | ❌        | ID of existing space to reuse             |
| `workbook`      | object   | ❌        | Workbook configuration for dynamic spaces |
| `listener`      | Listener | ❌        | Event listener for responding to events   |

### Look & Feel

| Option                            | Type    | Required | Description                                                          |
| --------------------------------- | ------- | -------- | -------------------------------------------------------------------- |
| `themeConfig`                     | object  | ❌        | Theme values for Space, sidebar and data table                       |
| `spaceBody`                       | object  | ❌        | Space options for creating new Space; used with Angular and Vue SDKs |
| `sidebarConfig`                   | object  | ❌        | Sidebar UI configuration                                             |
| `sidebarConfig.defaultPage`       | object  | ❌        | Landing page configuration                                           |
| `sidebarConfig.showDataChecklist` | boolean | ❌        | Toggle data config, defaults to false                                |
| `sidebarConfig.showSidebar`       | boolean | ❌        | Show/hide sidebar                                                    |
| `document`                        | object  | ❌        | Document content for space                                           |
| `document.title`                  | string  | ❌        | Document title                                                       |
| `document.body`                   | string  | ❌        | Document body content (markdown)                                     |

### CSS Customization

You can customize the embedded Flatfile iframe and its container elements using CSS variables and class selectors. This allows you to control colors, sizing, borders, and other visual aspects of the iframe wrapper to match your application's design.

#### CSS Variables

Define these CSS variables in your application's stylesheet to control the appearance of Flatfile's embedded components:

```css
:root {
  --ff-primary-color: #4c48ef;
  --ff-secondary-color: #616a7d;
  --ff-text-color: #090b2b;
  --ff-dialog-border-radius: 4px;
  --ff-border-radius: 5px;
  --ff-bg-fade: rgba(0, 0, 0, 0.2);
}
```

#### Container Elements

Target these elements to customize the iframe container:

```css
/* The default mount element */
#flatfile_iFrameContainer {
  /* Your custom styles */
}

/* A div around the iframe that contains Flatfile */
.flatfile_iframe-wrapper {
  /* Your custom styles */
}

/* The actual iframe that contains Flatfile */
#flatfile_iframe {
  /* Your custom styles */
}
```

#### Modal Display Customization

When `displayAsModal` is set to `true`, customize the modal appearance:

```css
/* Container styles when displayed as modal */
.flatfile_displayAsModal {
  padding: 50px !important;
  width: calc(100% - 100px) !important;
  height: calc(100vh - 100px) !important;
}

.flatfile_iframe-wrapper.flatfile_displayAsModal {
  background: var(--ff-bg-fade);
}

/* Close button styles */
.flatfile_displayAsModal .flatfile-close-button {
  /* Your custom styles */
}

.flatfile_displayAsModal .flatfile-close-button svg {
  fill: var(--ff-secondary-color);
}

/* Iframe border radius when displayed as modal */
.flatfile_displayAsModal #flatfile_iframe {
  border-radius: var(--ff-border-radius);
}
```

#### Exit Confirmation Dialog

Customize the confirmation dialog that appears when closing Flatfile:

```css
/* Modal backdrop */
.flatfile_outer-shell {
  background-color: var(--ff-bg-fade);
  border-radius: var(--ff-border-radius);
}

/* Inner container */
.flatfile_inner-shell {
  /* Your custom styles */
}

/* Dialog box */
.flatfile_modal {
  border-radius: var(--ff-dialog-border-radius);
}

/* Button container */
.flatfile_button-group {
  /* Your custom styles */
}

/* All buttons */
.flatfile_button {
  /* Your custom styles */
}

/* Primary "Yes, cancel" button */
.flatfile_primary {
  border: 1px solid var(--ff-primary-color);
  background-color: var(--ff-primary-color);
  color: #fff;
}

/* Secondary "No, stay" button */
.flatfile_secondary {
  color: var(--ff-secondary-color);
}

/* Dialog heading */
.flatfile_modal-heading {
  color: var(--ff-text-color);
}

/* Dialog description text */
.flatfile_modal-text {
  color: var(--ff-secondary-color);
}
```

#### Error Component

Customize the error display component:

```css
/* Error container */
.ff_error_container {
  /* Your custom styles */
}

/* Error heading */
.ff_error_heading {
  /* Your custom styles */
}

/* Error description */
.ff_error_text {
  /* Your custom styles */
}
```

### Basic Behavior

| Option                 | Type     | Required | Description                                |
| ---------------------- | -------- | -------- | ------------------------------------------ |
| `closeSpace`           | object   | ❌        | Options for closing iframe                 |
| `closeSpace.operation` | string   | ❌        | Operation type                             |
| `closeSpace.onClose`   | function | ❌        | Callback when space closes                 |
| `displayAsModal`       | boolean  | ❌        | Display as modal or inline (default: true) |

## Advanced Configuration Options

These options provide specialized functionality for custom implementations:

### Space Reuse

| Option        | Type   | Required | Description                                   |
| ------------- | ------ | -------- | --------------------------------------------- |
| `id`          | string | ✅        | Space ID                                      |
| `accessToken` | string | ✅        | Access token for space (obtained server-side) |

**Important:** To reuse an existing space, you must retrieve the spaceId and access token server-side using your secret key, then pass the `accessToken` to the client. See [Server Setup Guide](./server-setup) for details.

### UI Overrides

| Option                    | Type         | Required | Description                                                      |
| ------------------------- | ------------ | -------- | ---------------------------------------------------------------- |
| `mountElement`            | string       | ❌        | Element to mount Flatfile (default: "flatfile\_iFrameContainer") |
| `loading`                 | ReactElement | ❌        | Custom loading component                                         |
| `exitTitle`               | string       | ❌        | Exit dialog title (default: "Close Window")                      |
| `exitText`                | string       | ❌        | Exit dialog text (default: "See below")                          |
| `exitPrimaryButtonText`   | string       | ❌        | Primary button text (default: "Yes, exit")                       |
| `exitSecondaryButtonText` | string       | ❌        | Secondary button text (default: "No, stay")                      |
| `errorTitle`              | string       | ❌        | Error dialog title (default: "Something went wrong")             |

### On-Premises Configuration

| Option     | Type   | Required | Description                                                                                      |
| ---------- | ------ | -------- | ------------------------------------------------------------------------------------------------ |
| `apiUrl`   | string | ❌        | API endpoint (default: "[https://platform.flatfile.com/api](https://platform.flatfile.com/api)") |
| `spaceUrl` | string | ❌        | Spaces API URL (default: "[https://platform.flatfile.com/s](https://platform.flatfile.com/s)")   |

URLs for other regions can be found [here](../reference/cli#regional-servers).

## Configuration Examples

### Basic Space Creation

```javascript
const config = {
  publishableKey: "pk_1234567890abcdef",
  name: "Customer Data Import",
  environmentId: "us_env_abc123",
  workbook: {
    // your workbook configuration
  },
  userInfo: {
    userId: "user_123",
    name: "John Doe",
  },
};
```

### Space Reuse with Access Token

```javascript
// Client-side: Use space with access token from server
const config = {
  space: {
    id: "us_sp_abc123def456",
    accessToken: "at_1234567890abcdef", // Retrieved server-side
  },
};
```

### Advanced UI Customization

```javascript
const config = {
  publishableKey: "pk_1234567890abcdef",
  mountElement: "custom-flatfile-container",
  exitTitle: "Are you sure you want to leave?",
  exitText: "Your progress will be saved.",
  themeConfig: {
    // custom theme configuration
  },
};
```

## Troubleshooting

### Invalid publishableKey

**Error:** `"Invalid publishable key"`

**Solution:**

* Verify key starts with `pk_`
* Check for typos or extra spaces
* Ensure key is from correct environment

### Space Not Found

**Error:** `"Space not found"` or `403 Forbidden`

**Solution:**

* Verify Space ID format (`us_sp_` prefix)
* Ensure Space exists and is active
* Check Space permissions in dashboard

### CORS Issues

**Error:** `"CORS policy blocked"`

**Solution:**

* Add your domain to allowed origins in Platform Dashboard
* Ensure you're using publishable key (not secret key)
* Check browser network tab for specific CORS errors

### Access Token Issues

**Error:** `"Invalid access token"` when using space reuse

**Solution:**

* Ensure access token is retrieved server-side using secret key
* Check that token hasn't expired
* Verify space ID matches the token

## Testing Setup

For development and testing:

```javascript
// Development configuration
const config = {
  publishableKey: "pk_test_1234567890abcdef", // publishable key from development environment
};
```

Create separate test Spaces for development to avoid affecting production data.

## Next Steps

Once configured:

* Deploy your event listener to Flatfile
* Configure data validation and transformation rules
* Test the embedding in your application
* Deploy to production with production keys

For server-side space reuse patterns, see our [Server Setup Guide](./server-setup).
