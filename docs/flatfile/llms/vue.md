# Source: https://flatfile.com/docs/embedding/vue.md

> ## Documentation Index
> Fetch the complete documentation index at: https://flatfile.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Vue Embedding

> Embed Flatfile in Vue.js applications

Embed Flatfile in your Vue.js application using our Vue SDK. This provides Vue components and composables for seamless integration.

## Installation

```bash  theme={null}
npm install @flatfile/vue
```

## Basic Implementation

### 1. Initialize Flatfile

Use the `initializeFlatfile` composable in your Vue component:

```vue  theme={null}
<script setup>
import { ref } from "vue";
import { initializeFlatfile } from "@flatfile/vue";

const showSpace = ref(false);

const spaceProps = {
  publishableKey: "pk_your_publishable_key",
};

const { Space, OpenEmbed } = initializeFlatfile(spaceProps);

const openImport = () => {
  showSpace.value = true;
  OpenEmbed();
};
</script>

<template>
  <div>
    <h1>Welcome to our app</h1>
    <button @click="openImport">Import Data</button>

    <div v-if="showSpace">
      <Space />
    </div>
  </div>
</template>
```

### 2. Get Your Credentials

**publishableKey**: Get from [Platform Dashboard](https://platform.flatfile.com) → Developer Settings

For authentication and security guidance, see [Advanced Configuration](./advanced-configuration).

## Complete Example

<Note>
  The example below will open an empty space. To create the sheet your users
  should land on, you'll want to create a workbook as shown further down this
  page.
</Note>

```vue  theme={null}
<script setup>
import { ref } from "vue";
import { initializeFlatfile } from "@flatfile/vue";

const showSpace = ref(false);

const spaceProps = {
  publishableKey: "pk_your_publishable_key",
  closeSpace: {
    onClose: () => {
      showSpace.value = false;
    },
  },
};

const { Space, OpenEmbed } = initializeFlatfile(spaceProps);

const toggleImport = () => {
  showSpace.value = !showSpace.value;
  if (showSpace.value) {
    OpenEmbed();
  }
};
</script>

<template>
  <div>
    <h1>My Application</h1>
    <button @click="toggleImport">
      {{ showSpace ? "Close" : "Open" }} Import
    </button>

    <div v-if="showSpace" class="space-wrapper">
      <Space />
    </div>
  </div>
</template>

<style>
.space-wrapper {
  margin-top: 20px;
}
</style>
```

## Options API Syntax

If you prefer the Options API:

```vue  theme={null}
<script>
import { initializeFlatfile } from "@flatfile/vue";

export default {
  data() {
    return {
      showSpace: false,
    };
  },
  setup() {
    const spaceProps = {
      publishableKey: "pk_your_publishable_key",
      spaceId: "us_sp_your_space_id",
    };

    const { Space, OpenEmbed } = initializeFlatfile(spaceProps);

    return {
      Space,
      OpenEmbed,
    };
  },
  methods: {
    openImport() {
      this.showSpace = true;
      this.OpenEmbed();
    },
  },
};
</script>

<template>
  <div>
    <button @click="openImport">Import Data</button>
    <div v-if="showSpace">
      <Space />
    </div>
  </div>
</template>
```

## Creating New Spaces

To create a new Space each time:

1. Add a `workbook` configuration object. Read more about workbooks [here](../core-concepts/workbooks).
2. Optionally [deploy](../core-concepts/listeners) a `listener` for custom data processing. Your listener will contain your validations and transformations

```vue  theme={null}
<script setup>
import { initializeFlatfile } from "@flatfile/vue";

const spaceProps = {
  publishableKey: "pk_your_publishable_key",
  workbook: {
    name: "Contacts Import",
    sheets: [
      {
        name: "Contacts",
        slug: "contacts",
        fields: [
          { key: "name", type: "string", label: "Name" },
          { key: "email", type: "string", label: "Email" },
        ],
      },
    ],
  },
};

const { Space, OpenEmbed } = initializeFlatfile(spaceProps);
</script>
```

For detailed workbook configuration, see the [Workbook API Reference](https://reference.flatfile.com/api-reference/workbooks).

## Reusing Existing Spaces

When reusing existing Spaces, the proper pattern is to let your server handle Space creation and management:

```vue  theme={null}
<script setup>
import { ref } from "vue";
import { initializeFlatfile } from "@flatfile/vue";

const showSpace = ref(false);

// Client-side initialization with existing Space
const spaceProps = {
  space: {
    spaceId: "us_sp_yourSpaceId",
    token: "accessToken",
  },
};

const { Space, OpenEmbed } = initializeFlatfile(spaceProps);

const openImport = () => {
  showSpace.value = true;
  OpenEmbed();
};
</script>
```

For server-side Space creation and management patterns, see [Server Setup](/embedding/server-setup).

## TypeScript Support

The Vue SDK supports TypeScript:

```vue  theme={null}
<script setup lang="ts">
import { ref, Ref } from "vue";
import { initializeFlatfile } from "@flatfile/vue";

interface SpaceConfig {
  publishableKey: string;
}

const showSpace: Ref<boolean> = ref(false);

const spaceProps: SpaceConfig = {
  publishableKey: "pk_your_publishable_key",
};

const { Space, OpenEmbed } = initializeFlatfile(spaceProps);
</script>
```

## Styling

Add custom styles to integrate with your Vue application:

```vue  theme={null}
<style scoped>
.import-button {
  background-color: #4c48ef;
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 6px;
  cursor: pointer;
}

.import-button:hover {
  background-color: #3f3ccc;
}

.space-container {
  margin-top: 20px;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  overflow: hidden;
}
</style>
```

## Configuration Options

For complete configuration options including authentication, theming, and advanced settings, see [Advanced Configuration](./advanced-configuration).

## Next Steps

* **Authentication**: Set up secure authentication with [Advanced Configuration](./advanced-configuration)
* **Server Setup**: Configure backend data processing with [Server Setup](./server-setup)
* **Styling**: Customize the embedded experience in your Platform Dashboard Space settings
* **API Integration**: Use [Flatfile API](https://reference.flatfile.com) to retrieve processed data

## Quick Links

<CardGroup cols={2}>
  <Card title="Advanced Configuration" icon="gear" href="/embedding/advanced-configuration">
    Authentication, theming, and advanced options
  </Card>

  <Card title="Server Setup" icon="server" href="/embedding/server-setup">
    Backend integration and data processing
  </Card>
</CardGroup>

## Example Projects

<CardGroup cols={2}>
  <Card title="Vue Example" icon="vuejs" href="https://github.com/FlatFilers/create-flatfile-vuejs">
    Complete Vue.js application with Flatfile embedding
  </Card>
</CardGroup>
