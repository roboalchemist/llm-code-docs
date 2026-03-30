# Source: https://render.com/docs/monorepo-support.md

# Monorepo Support — Deploy from a repo that contains the source for multiple apps.

A *monorepo* is a single Git repository that contains the source code for multiple related applications:

```bash
# A monorepo containing a Python backend and a JavaScript frontend

📁 my-monorepo
|
├── README.md
├── 📁 backend
│   ├── app.py
│   ├── README.md
│   ├── requirements.txt
│   └── 📁 tests
│       └── test_app.py
└── 📁 frontend
    ├── 📁 components
    │   └── login.js
    ├── index.js
    ├── package.json
    ├── README.md
    └── 📁 src
        └── auth.js
```

You can deploy the individual apps in a monorepo as separate Render services. You can also configure each service to redeploy only if you make changes to its corresponding files:

- *Set a service's [root directory](#setting-a-root-directory)* to ignore file changes _outside_ that directory.
- *Set [build filters](#setting-build-filters)* to ignore file changes that match specific [path patterns](#filter-syntax).

Specify any combination of a root directory and build filters to customize your service's autodeploy behavior.

## Setting a root directory

By default, Render [automatically deploys](/deploys#automatic-deploys) your service whenever you push _any_ changes to its linked Git branch. If you set a *root directory* for your service, Render only triggers an autodeploy if your changes affect files anywhere under that directory. This helps you avoid unnecessary deploys when working in a monorepo.

> Files outside your service's root directory are not available to the service at build time or at runtime.

Set your service's root directory in any of the following ways:

**Dashboard**

1. In the [Render Dashboard](https://dashboard.render.com), open the *Settings* page for the service you want to configure.

2. Scroll down to the *Build & Deploy* section and find the *Root Directory* setting:

   [image: Setting a root directory in the Render Dashboard]

3. Click *Edit*.

4. Specify the root directory to use and click *Save Changes*.

5. In the dialog that appears, verify your service's build and start commands (which will now run relative to the new root directory).

6. Click *Update Fields*.

**API**

Set the `rootDir` field in a request to the Render API's [Update Service](https://api-docs.render.com/reference/update-service) endpoint.

In the same request, update values for the following fields as needed to be relative to the new root directory:

- `buildCommand`
- `startCommand`
- `preDeployCommand`
- `dockerfilePath`
- `dockerContext`
- `staticPublishPath`

**Blueprints (render.yaml)**

> *Use this method only if you manage your services with [Blueprints](infrastructure-as-code).*

1. In your Blueprint's `render.yaml` file, add the `rootDir` key to the definition of each applicable service:

   ```yaml:render.yaml
   services:
     - type: web
       name: app-backend
       runtime: python
       rootDir: backend # highlight-line
       buildCommand: pip install -r requirements.txt
       startCommand: python app.py
     - type: web
       name: app-frontend
       runtime: node
       rootDir: frontend # highlight-line
       buildCommand: npm install
       startCommand: npm start
   ```

2. For each of the following fields that your service uses, update the values as needed to be relative to the new root directory:

   - `buildCommand`
   - `startCommand`
   - `preDeployCommand`
   - `dockerfilePath`
   - `dockerContext`
   - `staticPublishPath`

3. Save and deploy your changes.

If you don't set a root directory, Render uses the repository root as the default.

### Root-relative settings

Render runs commands and interacts with files relative to your service's root directory. All of the following settings operate relative to the root directory:

- Build command
- Start command
- Pre-deploy command
- Publish directory
- Dockerfile path
- Docker build context directory

If you _don't_ set a root directory for a monorepo-backed service, the service's build command might look like this:

```shell
cd backend && go build -o app . # Starts at repository root
```

Setting the service's root directory to the `backend` directory simplifies the build command to this:

```shell
go build -o app . # Starts in backend directory
```

## Setting build filters

Set *build filters* for your service to specify which files in your repo do (or don't) trigger an autodeploy when you push changes to them:

[image: Setting build filters in the Render Dashboard]

Configure your service's build filters in any of the following ways:

**Dashboard**

1. In the [Render Dashboard](https://dashboard.render.com), open the *Settings* page for the service you want to configure.
2. Scroll down to the *Build & Deploy* section and find the *Build Filters* setting.
3. Click *Edit*.
4. Click *+ Add Included Path* and/or *+ Add Ignored Path* as needed.
5. Enter the [path patterns](#filter-syntax) for all paths you want to include and ignore.
6. Click *Save Changes*.

**API**

Set the `buildFilter` field in a request to the Render API's [Update Service](https://api-docs.render.com/reference/update-service) endpoint.

Here's an example payload:

```json
{
  "buildFilter": {
    "paths": ["frontend/**"],
    "ignoredPaths": ["docs/**", "README.md"]
  }
}
```

Note that the property name for included paths is `paths` (not `includedPaths`).

**Blueprints (render.yaml)**

> *Use this method only if you manage your services with [Blueprints](infrastructure-as-code).*

Add the `buildFilter` key to the definition of each applicable service in your Blueprint's `render.yaml` file:

```yaml:render.yaml{8-13}
services:
  - type: web
    name: app-frontend
    runtime: node
    rootDir: frontend
    buildCommand: npm install
    startCommand: npm start
    buildFilter:
      paths:
        - frontend/**
      ignoredPaths:
        - docs/**
        - README.md
```

### Filter rules

Build filters can define rules for included paths, ignored paths, or both:

------

###### Path type

*Included paths*

###### Description

Changes that match an included path *will* trigger an autodeploy, *unless* those files also match an ignored path.

- If you specify at least one included path, all non-matching paths are automatically ignored (you don't need to specify them as ignored paths).
- If you don't specify any included paths, _all_ file changes trigger an autodeploy unless they match an ignored path.

---

###### Path type

*Ignored paths*

###### Description

Changes that match an ignored path *will not* trigger an autodeploy, *even if* those files also match an included path. In other words, ignoring a path takes precedence over including it.

------

Build filter paths are always relative to your _repository_ root, even if you’ve set a different [root directory](#setting-a-root-directory). This means your build filters _can_ include paths from other directories in your repo.

### Filter syntax

Build filters use *glob syntax* to define the patterns for included and ignored file paths. See supported wildcards and example usage below:

------

###### Syntax & Description

*`?`* Matches any single character except the file path separator `/`

###### Example

`frontend/sample.?s` Matches:

- frontend/sample.*t*s

Does not match:

- frontend/index.js
- frontend/components/login.jsx

---

###### Syntax & Description

*`*`* Matches zero or more characters except the file path separator `/`

###### Example

`backend/util/*.go` Matches:

- backend/util/*util*.go
- backend/util/*util_test*.go

Does not match:

- backend/main.go
- backend/util/readme.md

---

###### Syntax & Description

*`**`* Matches zero or more directories or sub-directories

###### Example

`**/readme.md` Matches:

- readme.md
- *backend*/readme.md
- *frontend/src*/readme.md

Does not match:

- backend/main.go
- frontend/index.js

---

###### Syntax & Description

*`[abc]`* Matches one character specified in the bracket

###### Example

`frontend/src/auth[nz].js` Matches:

- frontend/auth*n*.js
- frontend/auth*z*.js

Does not match:

- frontend/src/auth.js

---

###### Syntax & Description

*`[^abc]`* Matches one character that is NOT specified in the bracket

###### Example

`backend/build/[^ax]*.sh` Matches:

- backend/build/*q*uemu.sh

Does not match:

- backend/build/x86.sh
- backend/build/amd64.sh

---

###### Syntax & Description

*`[lo-hi]`* Matches one character (c) within the range lo <= c <= hi

###### Example

`backend/**/*[0-9].sh` Matches:

- backend/build/x8*6*.sh
- backend/build/amd6*4*.sh

Does not match:

- backend/build/quemu.sh

---

###### Syntax & Description

*`[^lo-hi]`* Matches one character (c) that is NOT within the range lo <= c <= hi

###### Example

`backend/build/*[^0-9].sh` Matches:

- backend/build/quem*u*.sh

Does not match:

- backend/build/x86.sh
- backend/build/amd64.sh

------

## Using with service previews

Your service's root directory and build filters also affect the creation of [pull request previews](service-previews#pull-request-previews-git-backed) (if you've enabled them). If you open a pull request that only modifies ignored files for a service, Render skips creating a preview instance for that pull request.

A file might be ignored because it's outside your service's [root directory](#setting-a-root-directory), or because it matches one of your build filter's [ignored paths](#filter-rules).

## FAQ

###### Can I ignore changes to my repo's Blueprint files?

*No.* Changes to a [Blueprint's](infrastructure-as-code) YAML file (usually `render.yaml`) are always processed regardless of your build filters. Blueprint syncs are also unaffected by build filters.

###### Do build filters affect any deploys besides autodeploys?

*No.* If you trigger a [manual deploy](/deploys#manual-deploys) or update your service's configuration (such as its build command or start command), Render always proceeds with the deploy regardless of your build filters.

###### Do build filters do anything if I've disabled autodeploys?

*Yes.* Although build filters don't affect your service's deploys in this case, they can still affect the creation of [pull request previews](#using-with-service-previews).

###### Do build filters and root directory work with preview environments?

*Yes.* If you define the root directory or specify build filters for each service in your Blueprint file, Render only creates a [preview environment](preview-environments) if the files changed in a pull request match the root directory or build filter paths for at least one service.
