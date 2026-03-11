# Source: https://casdoor.github.io/docs/basic/server-installation

Title: Server installation | Casdoor · AI-Native Identity and Access Management (IAM) / SSO Platform with MCP Server

URL Source: https://casdoor.github.io/docs/basic/server-installation

Markdown Content:
Requirements[​](https://casdoor.github.io/docs/basic/server-installation#requirements "Direct link to Requirements")
--------------------------------------------------------------------------------------------------------------------

### Operating system[​](https://casdoor.github.io/docs/basic/server-installation#operating-system "Direct link to Operating system")

Windows, Linux, and macOS are supported.

### Build environment[​](https://casdoor.github.io/docs/basic/server-installation#build-environment "Direct link to Build environment")

*   [Go 1.21+](https://go.dev/dl/)
*   [Node.js LTS (20)](https://nodejs.org/)
*   [Yarn 1.x](https://classic.yarnpkg.com/en/docs/install)

info

Use **Yarn 1.x** for the frontend; NPM can cause UI styling issues ([casdoor#294](https://github.com/casdoor/casdoor/issues/294)).

caution

If Go dependencies fail to download, set **GOPROXY** (e.g. `https://goproxy.cn/`).

### Database[​](https://casdoor.github.io/docs/basic/server-installation#database "Direct link to Database")

Casdoor uses [XORM](https://xorm.io/) and supports these databases ([Xorm drivers](https://xorm.io/docs/chapter-01/readme/)):

*   `MySQL`
*   `MariaDB`
*   `PostgreSQL`
*   `CockroachDB`
*   `SQL Server`
*   `Oracle`
*   `SQLite 3`
*   `TiDB`

Download[​](https://casdoor.github.io/docs/basic/server-installation#download "Direct link to Download")
--------------------------------------------------------------------------------------------------------

### Pre-built binaries[​](https://casdoor.github.io/docs/basic/server-installation#pre-built-binaries "Direct link to Pre-built binaries")

[GitHub Releases](https://github.com/casdoor/casdoor/releases) provide binaries for Linux (x86_64, arm64), macOS (x86_64, arm64), and Windows (x86_64, arm64). Extract the archive and run the `casdoor` binary. It includes the web frontend and a sample `conf/app.conf`; set the database connection before first run (see [Configure database](https://casdoor.github.io/docs/basic/server-installation#configure-database)).

Quick start with binaries

`# Linux/macOS exampletar -xzf casdoor_Linux_x86_64.tar.gzcd casdoor_Linux_x86_64# Edit conf/app.conf with your database settings./casdoor`

### Build from source[​](https://casdoor.github.io/docs/basic/server-installation#build-from-source "Direct link to Build from source")

Repository: `https://github.com/casdoor/casdoor` (backend and frontend in one repo).

| Part | Description | Stack |
| --- | --- | --- |
| Frontend | Web UI | JavaScript + React |
| Backend | REST API | Go + Beego + XORM |

Clone the repo (Go Modules are used):

`cd path/to/foldergit clone https://github.com/casdoor/casdoor`

Configuration[​](https://casdoor.github.io/docs/basic/server-installation#configuration "Direct link to Configuration")
-----------------------------------------------------------------------------------------------------------------------

### Configure database[​](https://casdoor.github.io/docs/basic/server-installation#configure-database "Direct link to Configure database")

Casdoor supports MySQL, MariaDB, PostgreSQL, CockroachDB, SQL Server, Oracle, SQLite3, and TiDB. Default config uses MySQL.

#### MySQL[​](https://casdoor.github.io/docs/basic/server-installation#mysql "Direct link to MySQL")

Create a database named `casdoor` if it does not exist. Set the connection in `conf/app.conf` (see [app.conf](https://github.com/casdoor/casdoor/blob/master/conf/app.conf)):

`driverName = mysqldataSourceName = root:123456@tcp(localhost:3306)/dbName = casdoor`

#### PostgreSQL[​](https://casdoor.github.io/docs/basic/server-installation#postgresql "Direct link to PostgreSQL")

Create a database (e.g. `casdoor`) before running; xorm requires it in the connection string. Example `app.conf`:

`driverName = postgresdataSourceName = user=postgres password=postgres host=localhost port=5432 sslmode=disable dbname=casdoordbName = casdoor`

info

For PostgreSQL, ensure that `dataSourceName` has a non-empty `dbName` and also [duplicate](https://github.com/casdoor/casdoor/issues/2127) the database name for the `dbname` field as shown in the example above.

#### CockroachDB[​](https://casdoor.github.io/docs/basic/server-installation#cockroachdb "Direct link to CockroachDB")

CockroachDB can also be used with the PostgreSQL driver and has the same configuration as PostgreSQL.

`driverName = postgresdataSourceName = user=postgres password=postgres host=localhost port=5432 sslmode=disable dbname=casdoor serial_normalization=virtual_sequencedbName = casdoor`

info

For CockroachDB, remember to add `serial_normalization=virtual_sequence` to the `dataSourceName` as shown in the example above. Otherwise, you will get an error regarding an existing database whenever the service starts or restarts. Note that this must be added before the database is created.

#### SQLite3[​](https://casdoor.github.io/docs/basic/server-installation#sqlite3 "Direct link to SQLite3")

To configure SQLite3, you should specify `app.conf` like this:

`driverName = sqlitedataSourceName = file:casdoor.db?cache=shareddbName = casdoor`

### Config files[​](https://casdoor.github.io/docs/basic/server-installation#config-files "Direct link to Config files")

Backend and frontend options are documented in [Configuration](https://casdoor.org/docs/basic/configuration). For a minimal setup, set `driverName` and `dataSourceName` in [conf/app.conf](https://github.com/casdoor/casdoor/blob/master/conf/app.conf) (see [Configure database](https://casdoor.github.io/docs/basic/server-installation#configure-database)).

Run[​](https://casdoor.github.io/docs/basic/server-installation#run "Direct link to Run")
-----------------------------------------------------------------------------------------

### Development mode[​](https://casdoor.github.io/docs/basic/server-installation#development-mode "Direct link to Development mode")

#### Backend[​](https://casdoor.github.io/docs/basic/server-installation#backend "Direct link to Backend")

Start the Go backend (default port 8000):

`go run main.go`

Then start the frontend.

#### Frontend [​](https://casdoor.github.io/docs/basic/server-installation#frontend- "Direct link to frontend-")

The frontend is a [Create React App](https://create-react-app.dev/) project and runs on port 7001 by default:

`cd webyarn installyarn start`

Open [http://localhost:7001](http://localhost:7001/) and sign in as **built-in/admin** / **123**.

### Production mode [​](https://casdoor.github.io/docs/basic/server-installation#production-mode- "Direct link to production-mode-")

#### Backend[​](https://casdoor.github.io/docs/basic/server-installation#backend-1 "Direct link to Backend")

Build and run the binary:

For Linux:

`go build./casdoor`

For Windows:

`go buildcasdoor.exe`

#### Frontend[​](https://casdoor.github.io/docs/basic/server-installation#frontend "Direct link to Frontend")

Build static assets:

`cd webyarn installyarn build`

Open [http://localhost:8000](http://localhost:8000/) and sign in as **built-in/admin** / **123**.

tip

To use a different port, set `httpport` in `conf/app.conf` and restart the backend.

Ports and URLs

*   **Dev:** Frontend runs on port 7001 (`yarn start`). Point apps at **[http://localhost:7001](http://localhost:7001/)** for the Casdoor login page.
*   **Prod:** Frontend is built and served by the backend on port 8000. Use **[https://your-casdoor-domain](https://your-casdoor-domain/)** (or your reverse proxy URL).

**Example:**[Casnode](https://casnode.org/) uses Casdoor. In dev, set `serverUrl` to `http://localhost:7001`; in prod, set it to `https://door.casdoor.com`.

![Image 1: Casnode Example](https://casdoor.org/assets/images/casnodeexample-06892ab1a66c35c830aa85d51c8f75ed.png)
