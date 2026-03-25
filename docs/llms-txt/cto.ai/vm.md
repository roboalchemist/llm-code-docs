# Source: https://docs.cto.new/settings-config/vm.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.cto.new/llms.txt
> Use this file to discover all available pages before exploring further.

# Task Runner (VM)

> cto.new's development environment

For connected repos, cto.new works in a cloud virtual machine that we call a **'task runner'**.

Properly configuring the task runner with system setup, project dependencies, and code checks will significantly improve the agent's work.

<Check>
  cto.new can attempt to configure its own task runner using the setup agent
</Check>

cto.new will automatically resize your VM's memory to meet the needs of your project.

### System Setup

Install and configure software, tools, and packages required at the system level.

For example, this system setup configuration installs Node 18 and configures a database to run tests:

```[expandable]  theme={null}
# Downgrade to Node v18
sudo apt-get remove -y nodejs && curl -fsSL https://deb.nodesource.com/setup_18.x | sudo bash - && sudo apt-get install -y nodejs

# Create test database
export PGPASSWORD=postgres && psql -U postgres -c "CREATE DATABASE test_db;"

# Run database migrations
npm run migrate
```

Every VM has the following base system specification by default.

<Accordion icon="notes" title="VM base specifications">
  ```
  ## Base Operating System

  - **Image**: `ubuntu:24.04` (default, configurable via `config.image`)
  - **Architecture**: follows `dpkg --print-architecture` (typically amd64)
  - **Environment variables at build**:
    - `DEBIAN_FRONTEND=noninteractive`
    - `CI=true`

  ## APT Packages

  Installed via `apt-get install -y` (from `config.ts`):

  | Package | Purpose |
  |---------|---------|
  | apt-utils | APT utilities |
  | bash-completion | Shell completion |
  | build-essential | gcc, g++, make |
  | ca-certificates | TLS certificates |
  | cmake | Build system |
  | curl | HTTP client |
  | dnsutils | dig, nslookup |
  | expect | Scripted interaction |
  | file | File type detection |
  | git | Version control |
  | gnupg | GPG for package verification |
  | htop | Process viewer |
  | iputils-ping | ping |
  | jq | JSON processor |
  | less | Pager |
  | libblas-dev | BLAS (linear algebra) |
  | libhdf5-dev | HDF5 scientific data |
  | liblapack-dev | LAPACK (linear algebra) |
  | libopenblas-dev | OpenBLAS |
  | libsqlite3-dev | SQLite development |
  | libssl-dev | OpenSSL development |
  | lsb-release | LSB release info |
  | lsof | List open files |
  | netcat-openbsd | netcat |
  | openssh-client | ssh, scp, sftp |
  | pkg-config | Package config |
  | procps | ps, top, etc. |
  | python3 | Python runtime |
  | python3-dev | Python headers |
  | python3-pip | pip |
  | python3-venv | venv |
  | ripgrep | rg |
  | rsync | File sync |
  | software-properties-common | add-apt-repository |
  | sqlite3 | SQLite CLI |
  | strace | System call tracer |
  | sudo | Privilege elevation |
  | tmux | Terminal multiplexer |
  | tree | Directory tree |
  | unzip | Unzip archives |
  | wget | HTTP downloader |

  ## Symlinks

  - `/usr/bin/python` → `/usr/bin/python3`

  ## Third-Party Software

  ### GitHub CLI (gh)

  - Source: https://cli.github.com/packages (official apt repo)
  - Installed via apt after adding keyring and sources.list entry

  ### Docker

  - Source: https://get.docker.com (official convenience script)
  - Includes: Docker Engine, CLI, containerd, Docker Compose plugin
  - `engine` user is in the `docker` group

  ### Node.js (via NVM)

  - Source: nvm-sh/nvm v0.40.2
  - Install: `nvm install --lts` (Node.js LTS)
  - Aliases: `default` → `lts/*`
  - Corepack: enabled with `yarn@stable` prepared

  ### Bun

  - Source: https://bun.sh/install
  - Install path: `/home/engine/.bun`

  ### UV (Python)

  - Source: https://astral.sh/uv/install.sh
  - Python package manager from Astral

  ### Playwright

  - CLI: `@playwright/cli@latest` (global npm)
  - Browser: Chromium
  - System deps: installed via `playwright install-deps chromium`
  - Skills: installed via `playwright-cli install --skills` in `/home/engine`

  ## User and Environment

  ### User

  - **Username**: `engine`
  - **Home**: `/home/engine`
  - **Shell**: `/bin/bash`
  - **Sudo**: passwordless (`NOPASSWD:ALL` in `/etc/sudoers.d/engine`)
  - **Groups**: `engine`, `docker`

  ### Environment Variables (engine user)

  | Variable | Value |
  |----------|-------|
  | HOME | /home/engine |
  | USER | engine |
  | SHELL | /bin/bash |
  | NVM_DIR | /home/engine/.nvm |
  | BUN_INSTALL | /home/engine/.bun |
  | PATH | /home/engine/.local/bin:/home/engine/.bun/bin:... |
  | PLAYWRIGHT_MCP_BROWSER | chromium |
  | WORKDIR | /home/engine |

  ## Directories

  | Path | Purpose |
  |------|---------|
  | /home/engine | User home, default WORKDIR |
  | /home/engine/project | Project directory |
  | /home/engine/.claude/skills | System skills (Playwright, Convex for vibe) |
  ```
</Accordion>

### Project Dependencies

Install repo specific dependencies like libraries, frameworks and packages.

For example, use npm to install project dependencies:

```[expandable]  theme={null}
# Install deps
npm install
```

### Code Checks

Code checks are commands cto.new runs before committing your code, to ensure it passes and pre commit or pipeline steps.

Use code checks to lint, test and build your code, for example:

```[expandable]  theme={null}
# Run lint
npm run lint

# Run build
npm run build

# Run tests
npm run test
```

### Task Runner Test

Run a test to verify your task runner is configured properly and cto.new can successfully make commits.

Running a test can take several minutes but can be manually stopped.

If your pipeline changes or you make any changes to cto.new's VM you should re-run the tests to ensure cto.new can work effectively.


Built with [Mintlify](https://mintlify.com).