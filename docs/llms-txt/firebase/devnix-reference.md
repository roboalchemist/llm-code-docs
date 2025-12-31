# Source: https://firebase.google.com/docs/studio/devnix-reference.md.txt

This page includes details on the schema for your workspace environment configuration file, which should always be located at`.idx/dev.nix`.

To learn about the Nix language, see the[official Nix language tutorial](https://nix.dev/tutorials/nix-language).

## packages

Packages to install in the environment.

You can use the`pkgs`argument to select packages to install, for example`pkgs.python3`. Note that the contents of`pkgs`depends on the selected`channel`channel option.

Example:  

    {pkgs, ...}: {
      channel = "stable-23.11";
      packages = [pkgs.vim];
    }

You can search for available packages here:[stable-23.11](https://search.nixos.org/packages?channel=23.11)or[unstable](https://search.nixos.org/packages?channel=unstable).

*Type:*list of package

*Default:* `[ ]`

## channel

nixpkgs channel to use.

This channel defines the contents of the`pkgs`argument.

*Type:*one of "stable-23.05", "stable-23.11", "stable-24.05", "stable-24.11", "unstable"

*Default:* `"stable-23.11"`

## env

Environment variables that are set inside the developer environment.

These are propagated to all of your shells and the preview server. Environment variables can be especially useful if your application requires a specific set of variables.

The value of each variable can be either a string or a list of strings. The latter is concatenated, interspersed with colon characters.

`PATH`must be a list, as it's always extended and never replaced completely.

Example:  

    {pkgs, ...}: {
      env = {
        HELLO = "world";
        # append an entry to PATH
        PATH = ["/some/path/bin"];
      };
    }

*Type:*attribute set of ((list of string) or anything)

*Default:* `{ }`

## idx.extensions

Code extensions you want to install in your IDX workspace.

This is a list of fully qualified extension ids, for example`${publisherId}.${extensionId}`.

You can find a list of available extensions on the[Open VSX Registry](https://open-vsx.org/)and enter them in your`dev.nix`file by`${publisherId}.${extensionId}`.

*Type:*list of (non-empty string or path)

*Default:* `[ ]`

## idx.previews.enable

Set this to`true`to enable IDX Previews.

This feature provides a way to run and reload your apps automatically as you are developing them.

*Type:*boolean

*Default:* `true`

*Example:* `true`

## idx.previews.previews

Preview configurations.

Define the commands IDX executes in your developer environment.

Example:  

    {pkgs, ...}: {
      idx.previews = {
        enable = true;
        previews = {
          web = {
            command = ["yes"];
            cwd = "subfolder";
            manager = "web";
            env = {
              HELLO = "world";
            };
          };
        };
      };
    }

*Type:*attribute set of (submodule)

*Default:* `{ }`

## idx.previews.previews.\<name\>.activity

Android Launch Activity

*Type:*string

*Default:* `""`

## idx.previews.previews.\<name\>.command

Command to execute

*Type:*list of string

*Default:* `[ ]`

## idx.previews.previews.\<name\>.cwd

Working directory

*Type:*string

*Default:* `""`

## idx.previews.previews.\<name\>.env

Environment variables to set.

*Type:*attribute set of string

*Default:* `{ }`

## idx.previews.previews.\<name\>.manager

Manager

*Type:*one of "web", "flutter", "android", "gradle"

## idx.workspace.onCreate

Commands to execute when the workspace is created and opened for the first time.

This can be useful to setup the development environment. For example, here we are specifying`npm install`to run:  

    {pkgs, ...}: {
      idx.workspace.onCreate = {
        npm-install = "npm install";
        # files to open when the workspace is first opened.
        default.openFiles = [ "src/index.ts" ];
      };
    }

*Type:*attribute set of (path or string or ({ openFiles = \[ string \];}))

*Default:* `{ }`

## idx.workspace.onStart

Commands to execute whenever the workspace is opened.

This can be useful to start build watchers. For example, here we are specifying 2 commands to run:  

    {pkgs, ...}: {
      idx.workspace.onStart = {
        npm-watch-fe = "npm run watch:frontend";
        npm-watch-be = "npm run watch:backend";
        # files to open when the workspace is (re)opened.
        default.openFiles = [ "src/index.ts" ];
      };
    }

*Type:*attribute set of (path or string or ({ openFiles = \[ string \];}))

*Default:* `{ }`

## imports

You can extend your dev.nix file with an imported file.  

    # dev.nix
    { pkgs, ... }: {
      imports = [
        ./some-file.nix
      ];
      # ...
    }
    # some-file.nix
    { pkgs, ... }: {
      packages = [
        pkgs.python3
      ];
      # ...
    }

There are multiple reasons you may want to import a custom`.nix`file in`dev.nix`:

1. Your`dev.nix`file is large and you want to modularize it to improve maintainability.

       { pkgs, ... }: {
         channel = "stable-24.11";
         # ...
         imports = [
           ./env-cfg.nix
           ./preview-config.nix
         ];
       }

2. You want to configure options specific to your local environment and add the file to your`.gitignore`list.

       # dev.nix
       { pkgs, lib, ... }: {
         # ...

         imports = lib.optionals (builtins.pathExists ./dev.local.nix ) [ ./dev.local.nix ];
       }

       #.gitignore
       .idx/dev.local.nix

*Type:*list of path

*Default:* `[ ]`

## services

Common services to enable when the workspace opens.

For example, to enable Postgres and use the`pgvector`extension, add the following to`dev.nix`:  

        services.postgres = {
          extensions = ["pgvector"];
          enable = true;
        };

The following sections list all supported services and their configurable options.

### services.docker.enable

Whether to enable Rootless docker.

*Type:*boolean

*Default:* `false`

*Example:* `true`

### services.mongodb.enable

Whether to enable MongoDB server.

*Type:*boolean

*Default:* `false`

*Example:* `true`

### services.mongodb.package

MongoDB package to use.

*Type:*package

*Default:* `<derivation mongodb-6.0.11>`

### services.mongodb.port

Configures the port Mongod will listen on.

By default tcp is disabled and Mongod only listens on /tmp/mongodb/mongodb.sock.

To connect, use the connection string`mongodb://%2Ftmp%2Fmongodb%2Fmongodb.sock`.

*Type:*16 bit unsigned integer; between 0 and 65535 (both inclusive)

*Default:* `0`

### services.mysql.enable

Whether to enable MySQL server.

The server is initialized with a passwordless user root. So to create additional users and create databases use`mysql -u root`.

*Type:*boolean

*Default:* `false`

*Example:* `true`

### services.mysql.package

MySQL package to use.

*Type:*package

*Default:* `pkgs.mysql`

*Example:* `pkgs.mysql80`

### services.postgres.enable

Whether to enable PostgreSQL server.

*Type:*boolean

*Default:* `false`

*Example:* `true`

### services.postgres.enableTcp

Whether to enable Postgres to listen on TCP.

*Type:*boolean

*Default:* `true`

*Example:* `true`

### services.postgres.package

PostgreSQL package to use.

*Type:*package

*Default:* `pkgs.postgresql`

*Example:* `pkgs.postgresql_15`

### services.postgres.extensions

Postgres extensions to install.

*Type:*list of (one of "age", "apache_datasketches", "cstore_fdw", "hypopg", "jsonb_deep_sum", "periods", "pg_auto_failover", "pg_bigm", "pg_cron", "pg_ed25519", "pg_embedding", "pg_hint_plan", "pg_hll", "pg_ivm", "pg_net", "pg_partman", "pg_rational", "pg_relusage", "pg_repack", "pg_safeupdate", "pg_similarity", "pg_topn", "pg_uuidv7", "pgaudit", "pgjwt", "pgroonga", "pgrouting", "pgsql-http", "pgtap", "pgvector", "plpgsql_check", "plr", "plv8", "postgis", "promscale_extension", "repmgr", "rum", "smlar", "tds_fdw", "temporal_tables", "timescaledb", "timescaledb-apache", "timescaledb_toolkit", "tsearch_extras", "tsja", "wal2json")

*Default:* `[ ]`

*Example:* `[ "pgvector" "postgis" ];`

### services.pubsub.enable

Whether to enable Google Pub/Sub emulator.

More documentation on using the emulator can be found here: https://cloud.google.com/pubsub/docs/emulator#using_the_emulator .

*Type:*boolean

*Default:* `false`

*Example:* `true`

### services.pubsub.port

Configures the port Pub/Sub will listen on.

*Type:*16 bit unsigned integer; between 0 and 65535 (both inclusive)

*Default:* `8085`

### services.pubsub.project-id

Project ID to use to run the Pub/Sub emulator. This project is for testing only, it does not have to exist and is only used locally.

*Type:*string matching the pattern \[a-z\]\[a-z0-9-\]{5,29}

*Default:* `"idx-pubsub-emulator"`

### services.redis.enable

Whether to enable Redis server.

*Type:*boolean

*Default:* `false`

*Example:* `true`

### services.redis.port

Configures the port Redis will listen on.

By default tcp is disabled and redis only listens on /tmp/redis/redis.sock.

*Type:*16 bit unsigned integer; between 0 and 65535 (both inclusive)

*Default:* `0`

### services.spanner.enable

Whether to enable Google Cloud Spanner Emulator.

*Type:*boolean

*Default:* `false`

*Example:* `true`

### services.spanner.fault-injection

Whether to enable random fault injection into transactions.

*Type:*boolean

*Default:* `false`

*Example:* `true`

### services.spanner.grpc-port

The TCP port to which the emulator should be bound.

*Type:*16 bit unsigned integer; between 0 and 65535 (both inclusive)

*Default:* `9010`

### services.spanner.rest-port

The port at which REST requests are served

*Type:*16 bit unsigned integer; between 0 and 65535 (both inclusive)

*Default:* `9020`