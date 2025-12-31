# Source: https://juno.build/docs/guides/angular.md

# Source: https://juno.build/docs/examples/frontend/angular.md

# Angular Example

This project is a note-taking app template built with **Angular**, **TypeScript**, and **Tailwind CSS**, designed to demonstrate integration with Juno for app development. It showcases authentication, data storage, and file storage using Juno's Satellite container.

You can scaffold it using the following command, or browse the source code:

```
npm create juno@latest -- --template angular-example
```

Source: [github.com/junobuild/create-juno/templates/angular-example](https://github.com/junobuild/create-juno/tree/main/templates/angular-example)

---

## Folder Structure

```
angular-example/âââ public/                # Static assetsâââ src/â   âââ app/               # Angular modules, components, services, and typesâ   âââ environments/      # Environment configuration filesâ   âââ styles.css         # Tailwind CSS stylesâ   âââ main.ts            # Angular entry pointâââ juno.config.mjs        # Juno Satellite configurationâââ package.json           # Project dependencies and scriptsâââ angular.json           # Angular CLI configurationâââ README.md              # User-facing documentationâââ ...                    # Other config and build files
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

*   **app.component.ts**: Main Angular component, bootstraps the app and layout.
*   **components/**: Contains UI and logic for authentication, notes table, modal, banner, etc.
*   **services/**: Angular services for interacting with Juno and managing app state.
*   **types/note.ts**: TypeScript interface for notes.

---

## Data Structure

*   **Note** (`src/app/types/note.ts`):
    
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

3.  **Create a Satellite** for local dev:
    *   Visit [http://localhost:5866](http://localhost:5866) and follow the instructions.
    *   Update `src/environments/environment.ts` with your Satellite ID.

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
*   **src/environments/environment.ts**: Contains the Satellite ID for local development.
*   **src/environments/environment.prod.ts**: Contains the Satellite ID for production.

---

## Production Deployment

*   Create a Satellite on the [Juno Console](https://console.juno.build) for mainnet.
*   Update `src/environments/environment.prod.ts` and `juno.config.mjs` with the production Satellite ID.
*   Build and deploy:

```
npm run buildjuno hosting deploy
```

---

## Notes

*   The app is intended as a starting point for Juno-based projects.
*   All logic is in TypeScript and Angular components/services.
*   The app is fully client-side (Server Side Rendering is not supported yet) and interacts with Juno via the Satellite container.

---

## Juno SDK Used

The following functions from `@junobuild/core` are used in this example:

| Function | Purpose/Description | Where Used (File/Component) | Juno Docs/Source Reference |
| --- | --- | --- | --- |
| `initSatellite` | Initialize Juno Satellite container | [`src/app/app.component.ts`](https://github.com/junobuild/create-juno/blob/main/templates/angular-example/src/app/app.component.ts) | [Initialization](/docs/setup-the-sdk.md#initialization) |
| `onAuthStateChange` | Subscribe to auth state changes | [`src/app/services/auth.service.ts`](https://github.com/junobuild/create-juno/blob/main/templates/angular-example/src/app/services/auth.service.ts) | [Listening to Auth Changes](/docs/build/authentication/utilities.md#listening-to-auth-changes) |
| `signIn` | Sign in user | [`src/app/components/login/login.component.ts`](https://github.com/junobuild/create-juno/blob/main/templates/angular-example/src/app/components/login/login.component.ts) | [Sign-in](/docs/build/authentication/internet-identity.md#sign-in) |
| `signOut` | Sign out user | [`src/app/components/logout/logout.component.ts`](https://github.com/junobuild/create-juno/blob/main/templates/angular-example/src/app/components/logout/logout.component.ts) | [Sign-out](/docs/build/authentication/utilities.md#sign-out) |
| `listDocs` | List documents in a collection | [`src/app/services/docs.service.ts`](https://github.com/junobuild/create-juno/blob/main/templates/angular-example/src/app/services/docs.service.ts) | [List documents](/docs/build/datastore/development.md#list-documents) |
| `setDoc` | Create or update a document | [`src/app/components/modal/modal.component.ts`](https://github.com/junobuild/create-juno/blob/main/templates/angular-example/src/app/components/modal/modal.component.ts) | [Add a document](/docs/build/datastore/development.md#add-a-document) |
| `deleteDoc` | Delete a document | [`src/app/components/delete/delete.component.ts`](https://github.com/junobuild/create-juno/blob/main/templates/angular-example/src/app/components/delete/delete.component.ts) | [Delete a document](/docs/build/datastore/development.md#delete-a-document) |
| `uploadFile` | Upload a file to storage | [`src/app/components/modal/modal.component.ts`](https://github.com/junobuild/create-juno/blob/main/templates/angular-example/src/app/components/modal/modal.component.ts) | [Upload file](/docs/build/storage/development.md#upload-file) |
| `deleteAsset` | Delete a file from storage | [`src/app/components/delete/delete.component.ts`](https://github.com/junobuild/create-juno/blob/main/templates/angular-example/src/app/components/delete/delete.component.ts) | [Delete asset](/docs/build/storage/development.md#delete-asset) |