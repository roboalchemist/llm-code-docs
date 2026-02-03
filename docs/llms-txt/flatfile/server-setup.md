# Source: https://flatfile.com/docs/embedding/server-setup.md

> ## Documentation Index
> Fetch the complete documentation index at: https://flatfile.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Server Setup for Space Reuse

> Server-side implementation guide for reusing existing spaces

To reuse existing spaces with embedded Flatfile, you need a server-side component that retrieves space access tokens using your secret key. This guide shows you how to set up the server-side pattern correctly.

## Why Server-Side Setup is Required

When reusing an existing space, you cannot use your publishable key directly. Instead, you must:

1. **Server-side**: Use your secret key to retrieve the space and its access token
2. **Client-side**: Use the access token (not publishable key) to launch the space

This pattern ensures security by keeping your secret key on the server while providing the necessary access token to the client.

## Server-Side Implementation

### Environment Setup

Create a `.env` file with your credentials:

```bash  theme={null}
# .env
FLATFILE_API_KEY=sk_1234567890abcdef  # Your secret key
SPACE_ID=us_sp_abc123def456           # Space ID to reuse
BASE_URL=http://localhost:3000        # Your application URL
```

### Basic Server Example

Here's a Node.js/Express server that retrieves space access tokens:

```javascript  theme={null}
// server.js
import express from "express";
import cors from "cors";
import { FlatfileClient } from "@flatfile/api";
import dotenv from "dotenv";

dotenv.config();

const app = express();
const PORT = process.env.PORT || 3001;

// Initialize Flatfile API with secret key
const flatfile = new FlatfileClient({
  token: process.env.FLATFILE_API_KEY, // Secret key
});

// Enable CORS for your frontend
app.use(
  cors({
    origin: process.env.BASE_URL || "http://localhost:3000",
  })
);

app.use(express.json());

// Endpoint to retrieve space with access token
app.get("/api/spaces/:spaceId", async (req, res) => {
  try {
    const { spaceId } = req.params;

    // Retrieve space using secret key
    const space = await flatfile.spaces.get(spaceId);

    // Return space data including access token
    res.json({
      success: true,
      data: space.data, // Contains both id and accessToken
    });
  } catch (error) {
    console.error("Error retrieving space:", error);
    res.status(500).json({
      success: false,
      error: "Failed to retrieve space",
    });
  }
});

// Health check endpoint
app.get("/health", (req, res) => {
  res.json({ status: "OK" });
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

### Enhanced Server with Multiple Spaces

For applications that need to handle multiple spaces:

```javascript  theme={null}
// enhanced-server.js
import express from "express";
import cors from "cors";
import { FlatfileClient } from "@flatfile/api";
import dotenv from "dotenv";

dotenv.config();

const app = express();
const flatfile = new FlatfileClient({
  token: process.env.FLATFILE_API_KEY,
});

app.use(
  cors({
    origin: process.env.BASE_URL || "http://localhost:3000",
  })
);

app.use(express.json());

// Get space by ID
app.get("/api/spaces/:spaceId", async (req, res) => {
  try {
    const { spaceId } = req.params;
    const space = await flatfile.spaces.get(spaceId);

    res.json({
      success: true,
      data: {
        id: space.data.id,
        name: space.data.name,
        accessToken: space.data.accessToken,
      },
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: "Failed to retrieve space",
    });
  }
});

// List available spaces
app.get("/api/spaces", async (req, res) => {
  try {
    const spaces = await flatfile.spaces.list();

    res.json({
      success: true,
      data: spaces.data.map((space) => ({
        id: space.id,
        name: space.name,
        createdAt: space.createdAt,
      })),
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: "Failed to list spaces",
    });
  }
});

// Create new space (optional)
app.post("/api/spaces", async (req, res) => {
  try {
    const { name, environmentId } = req.body;

    const space = await flatfile.spaces.create({
      name,
      environmentId,
      // Additional space configuration
    });

    res.json({
      success: true,
      data: {
        id: space.data.id,
        name: space.data.name,
        accessToken: space.data.accessToken,
      },
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: "Failed to create space",
    });
  }
});

const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

## Client-Side Implementation

### Fetching Space Data

Your client application should fetch the space data from your server:

```javascript  theme={null}
// client.js
async function getSpaceData(spaceId) {
  try {
    const response = await fetch(`/api/spaces/${spaceId}`);
    const result = await response.json();

    if (!result.success) {
      throw new Error(result.error);
    }

    return result.data; // Contains id and accessToken
  } catch (error) {
    console.error("Failed to fetch space data:", error);
    throw error;
  }
}
```

### Using the Space Data

Once you have the space data, use it to initialize Flatfile:

```javascript  theme={null}
window.openFlatfile = () => {
  fetch(server_url + "/space") // Make a request to the server endpoint
    .then((response) => response.json())
    .then((space) => {
      const flatfileOptions = {
        space: {
          id: space && space.data && space.data.id,
          accessToken: space && space.data && space.data.accessToken,
        },
        sidebarConfig: {
          showSidebar: false,
        },
        // Additional props...
      };
      initializeFlatfile(flatfileOptions);
    })
    .catch((error) => {
      console.error("Error retrieving space in client:", error);
    });
};
```

## Complete Workflow Example

Here's how the complete workflow works:

### 1. Server Setup

```javascript  theme={null}
// server.js
app.get("/api/spaces/:spaceId", async (req, res) => {
  const space = await flatfile.spaces.get(req.params.spaceId);
  res.json({ data: space.data });
});
```

### 2. Client Request

```javascript  theme={null}
// client.js
const response = await fetch("/api/spaces/us_sp_abc123def456");
const { data } = await response.json();
```

### 3. Client Usage

```javascript  theme={null}
const flatfileOptions = {
  space: {
    id: space && space.data && space.data.id,
    accessToken: space && space.data && space.data.accessToken,
  },
  sidebarConfig: {
    showSidebar: false,
  },
  // Additional props...
};
initializeFlatfile(flatfileOptions);
```

## Security Considerations

### Environment Variables

Never expose your secret key in client-side code:

```javascript  theme={null}
// ✅ Good - server-side only
const flatfile = new FlatfileClient({
  token: process.env.FLATFILE_API_KEY, // Secret key on server
});

// ❌ Bad - never do this in client code
const flatfile = new FlatfileClient({
  token: "sk_1234567890abcdef", // Secret key exposed
});
```

### CORS Configuration

Configure CORS to only allow your frontend domain:

```javascript  theme={null}
app.use(
  cors({
    origin: process.env.BASE_URL, // Only your frontend
    credentials: true,
  })
);
```

### Access Token Handling

* Access tokens are temporary and space-specific
* They should be fetched fresh for each session
* Store them securely in your client application

## Error Handling

### Server-Side Errors

```javascript  theme={null}
app.get("/api/spaces/:spaceId", async (req, res) => {
  try {
    const space = await flatfile.spaces.get(req.params.spaceId);
    res.json({ success: true, data: space.data });
  } catch (error) {
    if (error.status === 404) {
      res.status(404).json({
        success: false,
        error: "Space not found",
      });
    } else if (error.status === 403) {
      res.status(403).json({
        success: false,
        error: "Access denied",
      });
    } else {
      res.status(500).json({
        success: false,
        error: "Server error",
      });
    }
  }
});
```

### Client-Side Errors

```javascript  theme={null}
async function getSpaceData(spaceId) {
  try {
    const response = await fetch(`/api/spaces/${spaceId}`);

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }

    const result = await response.json();

    if (!result.success) {
      throw new Error(result.error);
    }

    return result.data;
  } catch (error) {
    console.error("Failed to fetch space data:", error);
    throw error;
  }
}
```

## Testing

### Local Development

1. Start your server: `node server.js`
2. Test the endpoint: `curl http://localhost:3001/api/spaces/us_sp_abc123def456`
3. Verify the response includes `id` and `accessToken`

### Production Deployment

1. Set environment variables on your server
2. Deploy your server application
3. Update your client to use the production server URL
4. Test the complete workflow

## Next Steps

Once your server is set up:

* Update your client applications to use the server endpoint
* Test the space reuse functionality
* Monitor server logs for any issues
* Consider adding authentication for your server endpoints

For client-side SDK implementation, see the framework-specific guides:

* [JavaScript SDK](./javascript)
* [React SDK](./react)
* [Vue SDK](./vue)
* [Angular SDK](./angular)
