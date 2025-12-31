# Source: https://juno.build/docs/examples/frontend/react-javascript.md

# React JavaScript Example

This project is a note-taking app template built with **React**, **JavaScript**, and **Tailwind CSS**, designed to demonstrate integration with Juno for app development. It showcases authentication, data storage, and file storage using Juno's Satellite container.

You can scaffold it using the following command, or browse the source code:

```
npm create juno@latest -- --template react-example
```

Source: [github.com/junobuild/create-juno/templates/react-example](https://github.com/junobuild/create-juno/tree/main/templates/react-example)

---

## Folder Structure

```
react-example/âââ public/                # Static assetsâââ src/â   âââ components/        # React UI components (Auth, Table, Modal, Banner, etc.)â   âââ App.jsx            # Main app componentâ   âââ main.jsx           # React entry pointâ   âââ index.css          # Tailwind CSS stylesâââ juno.config.mjs        # Juno Satellite configurationâââ package.json           # Project dependencies and scriptsâââ vite.config.js         # Vite build configurationâââ README.md              # User-facing documentationâââ ...                    # Other config and build files
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

*   **App.jsx**: Initializes Juno Satellite, renders the main layout, and wraps content in authentication.
*   **Banner.jsx**: Shows a warning if the Satellite ID is missing in local dev.
*   **Auth.jsx**: Provides authentication context and login/logout UI.
*   **Table.jsx**: Displays the list of notes from the Datastore.
*   **Modal.jsx**: Handles note creation and editing.
*   **Delete.jsx**: Handles note deletion.
*   **Footer.jsx, Background.jsx, Button.jsx, etc.**: UI and utility components.

---

## Data Structure

*   **Note** (used in Table.jsx):

```
// Example note object{  key: string,  data: {    text: string,    url?: string  }}
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

*   **juno.config.mjs**: Defines Satellite IDs for development/production, build source, and predeploy steps. See the [Configuration reference](/docs/reference/configuration.md) for details.
*   **vite.config.js**: Registers the `juno` plugin to inject environment variables automatically. See the [Vite Plugin reference](/docs/reference/plugins.md#vite-plugin) for more information.

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
*   All logic is in JavaScript and React function components.
*   The app is fully client-side (Server Side Rendering is not supported yet) and interacts with Juno via the Satellite container.

---

## Juno SDK Used

The following functions from `@junobuild/core` are used in this example:

| Function | Purpose/Description | Where Used (File/Component) | Juno Docs/Source Reference |
| --- | --- | --- | --- |
| `initSatellite` | Initialize Juno Satellite container | [`src/App.jsx`](https://github.com/junobuild/create-juno/blob/main/templates/react-example/src/App.jsx) | [Initialization](/docs/setup-the-sdk.md#initialization) |
| `onAuthStateChange` | Subscribe to auth state changes | [`src/components/Auth.jsx`](https://github.com/junobuild/create-juno/blob/main/templates/react-example/src/components/Auth.jsx) | [Listening to Auth Changes](/docs/build/authentication/utilities.md#listening-to-auth-changes) |
| `signIn` | Sign in user | [`src/components/Login.jsx`](https://github.com/junobuild/create-juno/blob/main/templates/react-example/src/components/Login.jsx) | [Sign-in](/docs/build/authentication/internet-identity.md#sign-in) |
| `signOut` | Sign out user | [`src/components/Logout.jsx`](https://github.com/junobuild/create-juno/blob/main/templates/react-example/src/components/Logout.jsx) | [Sign-out](/docs/build/authentication/utilities.md#sign-out) |
| `listDocs` | List documents in a collection | [`src/components/Table.jsx`](https://github.com/junobuild/create-juno/blob/main/templates/react-example/src/components/Table.jsx) | [List documents](/docs/build/datastore/development.md#list-documents) |
| `setDoc` | Create or update a document | [`src/components/Modal.jsx`](https://github.com/junobuild/create-juno/blob/main/templates/react-example/src/components/Modal.jsx) | [Add a document](/docs/build/datastore/development.md#add-a-document) |
| `deleteDoc` | Delete a document | [`src/components/Delete.jsx`](https://github.com/junobuild/create-juno/blob/main/templates/react-example/src/components/Delete.jsx) | [Delete a document](/docs/build/datastore/development.md#delete-a-document) |
| `uploadFile` | Upload a file to storage | [`src/components/Modal.jsx`](https://github.com/junobuild/create-juno/blob/main/templates/react-example/src/components/Modal.jsx) | [Upload file](/docs/build/storage/development.md#upload-file) |
| `deleteAsset` | Delete a file from storage | [`src/components/Delete.jsx`](https://github.com/junobuild/create-juno/blob/main/templates/react-example/src/components/Delete.jsx) | [Delete asset](/docs/build/storage/development.md#delete-asset) |