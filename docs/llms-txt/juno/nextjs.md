# Source: https://juno.build/docs/guides/nextjs.md

# Source: https://juno.build/docs/examples/frontend/nextjs.md

# Next.js Example

This project is a note-taking app template built with **Next.js**, **TypeScript**, and **Tailwind CSS**, designed to demonstrate integration with Juno for app development. It showcases authentication, data storage, and file storage using Juno's Satellite container.

You can scaffold it using the following command, or browse the source code:

```
npm create juno@latest -- --template nextjs-example
```

Source: [github.com/junobuild/create-juno/templates/nextjs-example](https://github.com/junobuild/create-juno/tree/main/templates/nextjs-example)

---

## Folder Structure

```
nextjs-example/âââ public/                # Static assetsâââ src/â   âââ app/               # Next.js app directory (routing, layout, etc.)â   âââ components/        # React UI components (auth, table, modal, banner, etc.)â   âââ types/             # TypeScript types (e.g., note.ts)âââ juno.config.mjs        # Juno Satellite configurationâââ package.json           # Project dependencies and scriptsâââ next.config.mjs        # Next.js configurationâââ README.md              # User-facing documentationâââ ...                    # Other config and build files
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

*   **src/app/**: Next.js app directory, handles routing and layout.
*   **components/**: Contains UI and logic for authentication, notes table, modal, banner, etc.
*   **types/note.ts**: TypeScript interface for notes.

---

## Data Structure

*   **NoteData** (`src/types/note.ts`):

```
export interface NoteData {  text: string;  url?: string;}export type Note = Doc<NoteData>;
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
*   Update `juno.config.mjs` with your Satellite ID.

4.  **Create required collections**:

*   `notes` in Datastore: [http://localhost:5866/datastore](http://localhost:5866/datastore)
*   `images` in Storage: [http://localhost:5866/storage](http://localhost:5866/storage)

5.  **Start the frontend dev server** (in a separate terminal):

```
npm run dev
```

---

## Juno-Specific Configuration

*   `juno.config.mjs`: Defines Satellite IDs for development/production, build source, and predeploy steps. See the [Configuration reference](/docs/reference/configuration.md) for details.
*   `next.config.mjs`: Uses the `withJuno` plugin to load environment variables and inject config automatically at build time. See the [Next.js Plugin reference](/docs/reference/plugins.md#nextjs-plugin) for more information.

---

## Production Deployment

*   Create a Satellite on the [Juno Console](https://console.juno.build) for mainnet.
*   Update `juno.config.mjs` with the production Satellite ID.
*   Build and deploy:

```
npm run buildjuno hosting deploy
```

---

## Notes

*   The app is intended as a starting point for Juno-based projects.
*   All logic is in TypeScript and React function components.
*   The app is fully client-side (Server Side Rendering is not supported yet) and interacts with Juno via the Satellite container.

---

## Juno SDK Used

The following functions from `@junobuild/core` are used in this example:

| Function | Purpose/Description | Where Used (File/Component) | Juno Docs/Source Reference |
| --- | --- | --- | --- |
| `initSatellite` | Initialize Juno Satellite container | [`src/app/page.tsx`](https://github.com/junobuild/create-juno/blob/main/templates/nextjs-example/src/app/page.tsx) | [Initialization](/docs/setup-the-sdk.md#initialization) |
| `onAuthStateChange` | Subscribe to auth state changes | [`src/components/auth.tsx`](https://github.com/junobuild/create-juno/blob/main/templates/nextjs-example/src/components/auth.tsx) | [Listening to Auth Changes](/docs/build/authentication/utilities.md#listening-to-auth-changes) |
| `signIn` | Sign in user | [`src/components/login.tsx`](https://github.com/junobuild/create-juno/blob/main/templates/nextjs-example/src/components/login.tsx) | [Sign-in](/docs/build/authentication/internet-identity.md#sign-in) |
| `signOut` | Sign out user | [`src/components/logout.tsx`](https://github.com/junobuild/create-juno/blob/main/templates/nextjs-example/src/components/logout.tsx) | [Sign-out](/docs/build/authentication/utilities.md#sign-out) |
| `listDocs` | List documents in a collection | [`src/components/table.tsx`](https://github.com/junobuild/create-juno/blob/main/templates/nextjs-example/src/components/table.tsx) | [List documents](/docs/build/datastore/development.md#list-documents) |
| `setDoc` | Create or update a document | [`src/components/modal.tsx`](https://github.com/junobuild/create-juno/blob/main/templates/nextjs-example/src/components/modal.tsx) | [Add a document](/docs/build/datastore/development.md#add-a-document) |
| `deleteDoc` | Delete a document | [`src/components/delete.tsx`](https://github.com/junobuild/create-juno/blob/main/templates/nextjs-example/src/components/delete.tsx) | [Delete a document](/docs/build/datastore/development.md#delete-a-document) |
| `uploadFile` | Upload a file to storage | [`src/components/modal.tsx`](https://github.com/junobuild/create-juno/blob/main/templates/nextjs-example/src/components/modal.tsx) | [Upload file](/docs/build/storage/development.md#upload-file) |
| `deleteAsset` | Delete a file from storage | [`src/components/delete.tsx`](https://github.com/junobuild/create-juno/blob/main/templates/nextjs-example/src/components/delete.tsx) | [Delete asset](/docs/build/storage/development.md#delete-asset) |