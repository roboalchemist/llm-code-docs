# Source: https://juno.build/docs/guides/sveltekit.md

# Source: https://juno.build/docs/examples/frontend/sveltekit.md

# SvelteKit Example

This project is a note-taking app template built with **SvelteKit**, **TypeScript**, and **Tailwind CSS**, designed to demonstrate integration with Juno for app development. It showcases authentication, data storage, and file storage using Juno's Satellite container.

You can scaffold it using the following command, or browse the source code:

```
npm create juno@latest -- --template sveltekit-example
```

Source: [github.com/junobuild/create-juno/templates/sveltekit-example](https://github.com/junobuild/create-juno/tree/main/templates/sveltekit-example)

---

## Folder Structure

```
sveltekit-example/âââ static/                # Static assetsâââ src/â   âââ lib/               # SvelteKit components, stores, types, etc.â   âââ routes/            # SvelteKit routes and layoutsâ   âââ app.css            # Tailwind CSS stylesâ   âââ app.html           # SvelteKit HTML templateâââ juno.config.ts         # Juno Satellite configurationâââ package.json           # Project dependencies and scriptsâââ vite.config.ts         # Vite build configurationâââ README.md              # User-facing documentationâââ ...                    # Other config and build files
```

---

## Key Features

*   **Juno Integration**: Uses Juno's Satellite for authentication, Datastore, and Storage.
*   **Authentication**: Login/logout flow.
*   **Notes Collection**: Users can create, view, and delete notes (text, with optional file URL).
*   **Images Collection**: Supports file storage for images.
*   **Responsive UI**: Built with Tailwind CSS for modern styling.
*   **Banner**: Warns if the Satellite is not configured for local development.

---

## Main Components

*   **src/routes/+layout.svelte**: Main layout, initializes Juno Satellite, wraps content in authentication.
*   **lib/components/**: Contains UI and logic for authentication, notes table, modal, banner, etc.
*   **lib/types/note.ts**: TypeScript interface for notes.
*   **lib/types/user.ts**: TypeScript interface for user.

---

## Data Structure

*   **Note** (`src/lib/types/note.ts`):

```
export interface Note {  text: string;  url?: string;}
```

---

## How to Run

. **Install dependencies**:

```
npm install
```

NaN. **Start Juno local emulator**:

**Important:**

Requires the Juno CLI to be available `npm i -g @junobuild/cli`

```
juno emulator start
```

3. **Create a Satellite** for local dev:

*   Visit [http://localhost:5866](http://localhost:5866) and follow the instructions.
*   Update `juno.config.ts` with your Satellite ID.

4.  **Create required collections**:

*   `notes` in Datastore: [http://localhost:5866/datastore](http://localhost:5866/datastore)
*   `images` in Storage: [http://localhost:5866/storage](http://localhost:5866/storage)

5.  **Start the frontend dev server** (in a separate terminal):

```
npm run dev
```

---

## Juno-Specific Configuration

*   **juno.config.ts**: Defines Satellite IDs for development/production, build source, and predeploy steps. See the [Configuration reference](/docs/reference/configuration.md) for details.
*   **vite.config.ts**: Registers the `juno` plugin to inject environment variables automatically. See the [Vite Plugin reference](/docs/reference/plugins.md#vite-plugin) for more information.

---

## Production Deployment

*   Create a Satellite on the [Juno Console](https://console.juno.build) for mainnet.
*   Update with the production Satellite ID.
*   Build and deploy:

```
npm run buildjuno hosting deploy
```

---

## Notes

*   The app is intended as a starting point for Juno-based projects.
*   All logic is in TypeScript and SvelteKit components/stores.
*   The app is fully client-side (Server Side Rendering is not supported yet) and interacts with Juno via the Satellite container.

---

## Juno SDK Used

The following functions from `@junobuild/core` are used in this example:

| Function | Purpose/Description | Where Used (File/Component) | Juno Docs/Source Reference |
| --- | --- | --- | --- |
| `initSatellite` | Initialize Juno Satellite container | [`src/routes/+layout.svelte`](https://github.com/junobuild/create-juno/blob/main/templates/sveltekit-example/src/routes/+layout.svelte) | [Initialization](/docs/setup-the-sdk.md#initialization) |
| `onAuthStateChange` | Subscribe to auth state changes | [`src/lib/components/Auth.svelte`](https://github.com/junobuild/create-juno/blob/main/templates/sveltekit-example/src/lib/components/Auth.svelte) | [Listening to Auth Changes](/docs/build/authentication/utilities.md#listening-to-auth-changes) |
| `signIn` | Sign in user | [`src/lib/components/Login.svelte`](https://github.com/junobuild/create-juno/blob/main/templates/sveltekit-example/src/lib/components/Login.svelte) | [Sign-in](/docs/build/authentication/internet-identity.md#sign-in) |
| `signOut` | Sign out user | [`src/lib/components/Logout.svelte`](https://github.com/junobuild/create-juno/blob/main/templates/sveltekit-example/src/lib/components/Logout.svelte) | [Sign-out](/docs/build/authentication/utilities.md#sign-out) |
| `listDocs` | List documents in a collection | [`src/lib/components/Table.svelte`](https://github.com/junobuild/create-juno/blob/main/templates/sveltekit-example/src/lib/components/Table.svelte) | [List documents](/docs/build/datastore/development.md#list-documents) |
| `setDoc` | Create or update a document | [`src/lib/components/Modal.svelte`](https://github.com/junobuild/create-juno/blob/main/templates/sveltekit-example/src/lib/components/Modal.svelte) | [Add a document](/docs/build/datastore/development.md#add-a-document) |
| `deleteDoc` | Delete a document | [`src/lib/components/Delete.svelte`](https://github.com/junobuild/create-juno/blob/main/templates/sveltekit-example/src/lib/components/Delete.svelte) | [Delete a document](/docs/build/datastore/development.md#delete-a-document) |
| `uploadFile` | Upload a file to storage | [`src/lib/components/Modal.svelte`](https://github.com/junobuild/create-juno/blob/main/templates/sveltekit-example/src/lib/components/Modal.svelte) | [Upload file](/docs/build/storage/development.md#upload-file) |
| `deleteAsset` | Delete a file from storage | [`src/lib/components/Delete.svelte`](https://github.com/junobuild/create-juno/blob/main/templates/sveltekit-example/src/lib/components/Delete.svelte) | [Delete asset](/docs/build/storage/development.md#delete-asset) |