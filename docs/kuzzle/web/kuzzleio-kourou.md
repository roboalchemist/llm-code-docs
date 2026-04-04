# Source: https://github.com/kuzzleio/kourou

Title: GitHub - kuzzleio/kourou: The CLI that helps you manage your Kuzzle application

URL Source: https://github.com/kuzzleio/kourou

Markdown Content:
The CLI that helps you manage your Kuzzle instances.

[![Image 1: oclif](https://camo.githubusercontent.com/4cd9ba494681981e22760cc9c296c21d9ba9909e1177764ab17b8ced2c6a54a8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636c692d6f636c69662d627269676874677265656e2e737667)](https://oclif.io/)[![Image 2: Version](https://camo.githubusercontent.com/026cf92d558b64deff86e39769971135541146e6e3513afe2720977c211b335b/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f6b6f75726f752e737667)](https://npmjs.org/package/kourou)[![Image 3: Downloads/week](https://camo.githubusercontent.com/5681a9257cb0ad91197f451d5fe7a7ce35b56483481cc193d3181afe350a5dbc/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f64772f6b6f75726f752e737667)](https://npmjs.org/package/kourou)[![Image 4: License](https://camo.githubusercontent.com/e0dcd86f5ed1ef6a80c250484ea3b5955a75cb34957f912ab21519026027a6dd/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f6c2f6b6f75726f752e737667)](https://github.com/kuzzleio/kourou/blob/master/package.json)

*   [kourou](https://github.com/kuzzleio/kourou#kourou)
*   [Usage](https://github.com/kuzzleio/kourou#usage)
*   [Commands](https://github.com/kuzzleio/kourou#commands)
*   [Where does this weird name come from?](https://github.com/kuzzleio/kourou#where-does-this-weird-name-come-from)
*   [Have fun with a quine](https://github.com/kuzzleio/kourou#have-fun-with-a-quine)
*   [Telemetry](https://github.com/kuzzleio/kourou#telemetry)

⚠️ This project is currently in beta and breaking changes may occur until the 1.0.0

Usage
-----

[](https://github.com/kuzzleio/kourou#usage)

$ npm install -g kourou
$ kourou COMMAND
running command...
$ kourou (-v|--version|version)
kourou/1.2.0 linux-x64 node-v22.16.0
$ kourou --help [COMMAND]
USAGE
 $ kourou COMMAND
...

Connect and authenticate to Kuzzle API
--------------------------------------

[](https://github.com/kuzzleio/kourou#connect-and-authenticate-to-kuzzle-api)
Commands that needs to send requests to Kuzzle API can specify the Kuzzle server address and authentication informations.

By command line:

```
--host=host                    [default: localhost] Kuzzle server host
  --port=port                    [default: 7512] Kuzzle server port
  --username=username            [default: anonymous] Kuzzle user
  --password=password            Kuzzle user password
  --api-key=api-key              Kuzzle user api-key
  --ssl                          [default: true for port 443] Use SSL to connect to Kuzzle
  --protocol                     [default: ws] Protocol used to connect to Kuzzle ( `http` or `ws` )
```

By environment variables:

```
KUZZLE_HOST                [default: localhost] Kuzzle server host
  KUZZLE_PORT                [default: 7512] Kuzzle server port
  KUZZLE_USERNAME            [default: anonymous] Kuzzle user
  KUZZLE_PASSWORD            Kuzzle user password
  KUZZLE_API_KEY             Kuzzle user api-key
  KUZZLE_SSL                 Use SSL to connect to Kuzzle
  KUZZLE_PROTOCOL            Protocol used to connect to Kuzzle ( `http` or `ws` )
```

User impersonation
------------------

[](https://github.com/kuzzleio/kourou#user-impersonation)
You can impersonate a user before executing a command with the `--as` flag and a user `kuid` .

User impersonation require the following rights for the authenticated user: `security:createApiKey` , `security:deleteApiKey`

$ kourou sdk:query auth:getCurrentUser --as gordon --username admin --password admin

 🚀 Kourou - Executes an API query.

 [ℹ] Connecting to http://localhost:7512 ...
 [ℹ] Impersonate user "gordon"

[...]

Automatic command infering for API actions
------------------------------------------

[](https://github.com/kuzzleio/kourou#automatic-command-infering-for-api-actions)
When no command is found, Kourou will try to execute the given command with the `sdk:query` command.

The first argument has to be the name of the controller and the action separated by a semicolon (eg `document:create` )

Kourou will try to infer common arguments like `index` , `collection` , `_id` or `body` .

It will automatically infer and accept the following lists of arguments:

*   `<command> <index>`
    *   _eg: `kourou collection:list iot` _

.

*   `<command> <body>`
    *   _eg: `kourou security:createUser '{"content":{"profileIds":["default"]}}' --id yagmur` _

.

*   `<command> <index> <collection>`
    *   _eg: `kourou collection:truncate iot sensors` _

.

*   `<command> <index> <collection> <body>`
    *   _eg: `kourou bulk:import iot sensors '{bulkData: []}'` _

.

*   `<command> <index> <collection> <id>`
    *   _eg: `kourou document:delete iot sensors sigfox-123` _

.

*   `<command> <index> <collection> <id> <body>`
    *   _eg: `kourou document:create iot sensors sigfox-123 '{temperature: 42}'` _

All other arguments and options will be passed as-is to the `sdk:query` method.

> Note: you can pass arguments to the API actions with the `--arg` or `-a` option in your command, e.g. `kourou security:createFirstAdmin '{ ...credentials here... }' -a reset=true`

Commands
--------

[](https://github.com/kuzzleio/kourou#commands)
*   [`kourou api-key:check TOKEN`](https://github.com/kuzzleio/kourou#kourou-api-keycheck-token)
*   [`kourou api-key:create USER`](https://github.com/kuzzleio/kourou#kourou-api-keycreate-user)
*   [`kourou api-key:delete USER ID`](https://github.com/kuzzleio/kourou#kourou-api-keydelete-user-id)
*   [`kourou api-key:search USER`](https://github.com/kuzzleio/kourou#kourou-api-keysearch-user)
*   [`kourou app:debug-proxy`](https://github.com/kuzzleio/kourou#kourou-appdebug-proxy)
*   [`kourou app:doctor`](https://github.com/kuzzleio/kourou#kourou-appdoctor)
*   [`kourou app:scaffold DESTINATION`](https://github.com/kuzzleio/kourou#kourou-appscaffold-destination)
*   [`kourou app:start-services`](https://github.com/kuzzleio/kourou#kourou-appstart-services)
*   [`kourou autocomplete [SHELL]`](https://github.com/kuzzleio/kourou#kourou-autocomplete-shell)
*   [`kourou collection:create INDEX COLLECTION [BODY]`](https://github.com/kuzzleio/kourou#kourou-collectioncreate-index-collection-body)
*   [`kourou collection:export INDEX COLLECTION`](https://github.com/kuzzleio/kourou#kourou-collectionexport-index-collection)
*   [`kourou collection:import PATH`](https://github.com/kuzzleio/kourou#kourou-collectionimport-path)
*   [`kourou collection:migrate SCRIPT PATH`](https://github.com/kuzzleio/kourou#kourou-collectionmigrate-script-path)
*   [`kourou config:diff FIRST SECOND`](https://github.com/kuzzleio/kourou#kourou-configdiff-first-second)
*   [`kourou document:search INDEX COLLECTION [QUERY]`](https://github.com/kuzzleio/kourou#kourou-documentsearch-index-collection-query)
*   [`kourou es:aliases:cat`](https://github.com/kuzzleio/kourou#kourou-esaliasescat)
*   [`kourou es:indices:cat`](https://github.com/kuzzleio/kourou#kourou-esindicescat)
*   [`kourou es:indices:get INDEX ID`](https://github.com/kuzzleio/kourou#kourou-esindicesget-index-id)
*   [`kourou es:indices:insert INDEX`](https://github.com/kuzzleio/kourou#kourou-esindicesinsert-index)
*   [`kourou es:migrate`](https://github.com/kuzzleio/kourou#kourou-esmigrate)
*   [`kourou es:snapshot:create REPOSITORY NAME`](https://github.com/kuzzleio/kourou#kourou-essnapshotcreate-repository-name)
*   [`kourou es:snapshot:create-repository REPOSITORY LOCATION`](https://github.com/kuzzleio/kourou#kourou-essnapshotcreate-repository-repository-location)
*   [`kourou es:snapshot:list REPOSITORY`](https://github.com/kuzzleio/kourou#kourou-essnapshotlist-repository)
*   [`kourou es:snapshot:restore REPOSITORY NAME`](https://github.com/kuzzleio/kourou#kourou-essnapshotrestore-repository-name)
*   [`kourou file:decrypt FILE`](https://github.com/kuzzleio/kourou#kourou-filedecrypt-file)
*   [`kourou file:encrypt FILE`](https://github.com/kuzzleio/kourou#kourou-fileencrypt-file)
*   [`kourou file:test FILE`](https://github.com/kuzzleio/kourou#kourou-filetest-file)
*   [`kourou help [COMMAND]`](https://github.com/kuzzleio/kourou#kourou-help-command)
*   [`kourou import PATH`](https://github.com/kuzzleio/kourou#kourou-import-path)
*   [`kourou index:export INDEX`](https://github.com/kuzzleio/kourou#kourou-indexexport-index)
*   [`kourou index:import PATH`](https://github.com/kuzzleio/kourou#kourou-indeximport-path)
*   [`kourou instance:kill`](https://github.com/kuzzleio/kourou#kourou-instancekill)
*   [`kourou instance:list`](https://github.com/kuzzleio/kourou#kourou-instancelist)
*   [`kourou instance:logs`](https://github.com/kuzzleio/kourou#kourou-instancelogs)
*   [`kourou instance:spawn`](https://github.com/kuzzleio/kourou#kourou-instancespawn)
*   [`kourou paas:login`](https://github.com/kuzzleio/kourou#kourou-paaslogin)
*   [`kourou profile:export`](https://github.com/kuzzleio/kourou#kourou-profileexport)
*   [`kourou profile:import PATH`](https://github.com/kuzzleio/kourou#kourou-profileimport-path)
*   [`kourou realtime:subscribe INDEX COLLECTION [FILTERS]`](https://github.com/kuzzleio/kourou#kourou-realtimesubscribe-index-collection-filters)
*   [`kourou redis:list-keys [MATCH]`](https://github.com/kuzzleio/kourou#kourou-redislist-keys-match)
*   [`kourou role:export`](https://github.com/kuzzleio/kourou#kourou-roleexport)
*   [`kourou role:import PATH`](https://github.com/kuzzleio/kourou#kourou-roleimport-path)
*   [`kourou sdk:execute [CODE]`](https://github.com/kuzzleio/kourou#kourou-sdkexecute-code)
*   [`kourou sdk:query CONTROLLER:ACTION`](https://github.com/kuzzleio/kourou#kourou-sdkquery-controlleraction)
*   [`kourou user:export`](https://github.com/kuzzleio/kourou#kourou-userexport)
*   [`kourou user:export-mappings`](https://github.com/kuzzleio/kourou#kourou-userexport-mappings)
*   [`kourou user:import PATH`](https://github.com/kuzzleio/kourou#kourou-userimport-path)
*   [`kourou user:import-mappings PATH`](https://github.com/kuzzleio/kourou#kourou-userimport-mappings-path)
*   [`kourou vault:add SECRETS-FILE KEY VALUE`](https://github.com/kuzzleio/kourou#kourou-vaultadd-secrets-file-key-value)
*   [`kourou vault:decrypt FILE`](https://github.com/kuzzleio/kourou#kourou-vaultdecrypt-file)
*   [`kourou vault:encrypt FILE`](https://github.com/kuzzleio/kourou#kourou-vaultencrypt-file)
*   [`kourou vault:show SECRETS-FILE [KEY]`](https://github.com/kuzzleio/kourou#kourou-vaultshow-secrets-file-key)
*   [`kourou vault:test SECRETS-FILE`](https://github.com/kuzzleio/kourou#kourou-vaulttest-secrets-file)

`kourou api-key:check TOKEN`
----------------------------

[](https://github.com/kuzzleio/kourou#kourou-api-keycheck-token)
Checks an API key validity

```
USAGE
  $ kourou api-key:check TOKEN

ARGUMENTS
  TOKEN  API key token

OPTIONS
  --api-key=api-key    Kuzzle user api-key
  --as=as              Impersonate a user
  --help               show CLI help
  --host=host          [default: localhost] Kuzzle server host
  --password=password  Kuzzle user password
  --port=port          [default: 7512] Kuzzle server port
  --protocol=protocol  [default: ws] Kuzzle protocol (http or ws)
  --ssl                Use SSL to connect to Kuzzle
  --username=username  [default: anonymous] Kuzzle username (local strategy)

EXAMPLE
  kourou api-key:check eyJhbG...QxfQrc
```

_See code: [lib/commands/api-key/check.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/api-key/check.js)_

`kourou api-key:create USER`
----------------------------

[](https://github.com/kuzzleio/kourou#kourou-api-keycreate-user)
Creates a new API Key for a user

```
USAGE
  $ kourou api-key:create USER

ARGUMENTS
  USER  User kuid

OPTIONS
  -d, --description=description  (required) API Key description
  --api-key=api-key              Kuzzle user api-key
  --as=as                        Impersonate a user
  --expire=expire                [default: -1] API Key validity
  --help                         show CLI help
  --host=host                    [default: localhost] Kuzzle server host
  --id=id                        API Key unique ID
  --password=password            Kuzzle user password
  --port=port                    [default: 7512] Kuzzle server port
  --protocol=protocol            [default: ws] Kuzzle protocol (http or ws)
  --ssl                          Use SSL to connect to Kuzzle
  --username=username            [default: anonymous] Kuzzle username (local strategy)
```

_See code: [lib/commands/api-key/create.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/api-key/create.js)_

`kourou api-key:delete USER ID`
-------------------------------

[](https://github.com/kuzzleio/kourou#kourou-api-keydelete-user-id)
Deletes an API key.

```
USAGE
  $ kourou api-key:delete USER ID

ARGUMENTS
  USER  User kuid
  ID    API Key unique ID

OPTIONS
  --api-key=api-key    Kuzzle user api-key
  --as=as              Impersonate a user
  --help               show CLI help
  --host=host          [default: localhost] Kuzzle server host
  --password=password  Kuzzle user password
  --port=port          [default: 7512] Kuzzle server port
  --protocol=protocol  [default: ws] Kuzzle protocol (http or ws)
  --ssl                Use SSL to connect to Kuzzle
  --username=username  [default: anonymous] Kuzzle username (local strategy)

EXAMPLE
  kourou vault:delete sigfox-gateway 1k-BF3EBjsXdvA2PR8x
```

_See code: [lib/commands/api-key/delete.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/api-key/delete.js)_

`kourou api-key:search USER`
----------------------------

[](https://github.com/kuzzleio/kourou#kourou-api-keysearch-user)
Lists a user's API Keys.

```
USAGE
  $ kourou api-key:search USER

ARGUMENTS
  USER  User kuid

OPTIONS
  --api-key=api-key    Kuzzle user api-key
  --as=as              Impersonate a user
  --filter=filter      Filter to match the API Key descriptions
  --help               show CLI help
  --host=host          [default: localhost] Kuzzle server host
  --password=password  Kuzzle user password
  --port=port          [default: 7512] Kuzzle server port
  --protocol=protocol  [default: ws] Kuzzle protocol (http or ws)
  --ssl                Use SSL to connect to Kuzzle
  --username=username  [default: anonymous] Kuzzle username (local strategy)
```

_See code: [lib/commands/api-key/search.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/api-key/search.js)_

`kourou app:debug-proxy`
------------------------

[](https://github.com/kuzzleio/kourou#kourou-appdebug-proxy)
Create a Proxy Server that allows Chrome to debug Kuzzle remotely using the DebugController

```
USAGE
  $ kourou app:debug-proxy

OPTIONS
  --api-key=api-key          Kuzzle user api-key
  --as=as                    Impersonate a user
  --forwardPort=forwardPort  [default: 9222] Port of the forwarding server
  --help                     show CLI help
  --host=host                [default: localhost] Kuzzle server host
  --keepAuth                 Keep the user authenticated

  --noAutoEnableDebugger     True if Kourou should not enable and disable the Debugger automatically before and after
                             usage

  --password=password        Kuzzle user password

  --port=port                [default: 7512] Kuzzle server port

  --protocol=protocol        [default: ws] Kuzzle protocol (http or ws)

  --showDebuggerEvents       Verbose mode to display events sent to the Chrome Debugger

  --showDebuggerPayloads     Verbose mode to display payloads sent by and to the Chrome Debugger

  --ssl                      Use SSL to connect to Kuzzle

  --ttl=ttl                  [default: 1h] Kuzzle login TTL

  --username=username        [default: anonymous] Kuzzle username (local strategy)
```

_See code: [lib/commands/app/debug-proxy.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/app/debug-proxy.js)_

`kourou app:doctor`
-------------------

[](https://github.com/kuzzleio/kourou#kourou-appdoctor)
Analyze a Kuzzle application

```
USAGE
  $ kourou app:doctor

OPTIONS
  --api-key=api-key              Kuzzle user api-key
  --as=as                        Impersonate a user
  --elasticsearch=elasticsearch  [default: http://localhost:9200] Elasticsearch server URL
  --help                         show CLI help
  --host=host                    [default: localhost] Kuzzle server host
  --password=password            Kuzzle user password
  --port=port                    [default: 7512] Kuzzle server port
  --protocol=protocol            [default: ws] Kuzzle protocol (http or ws)
  --ssl                          Use SSL to connect to Kuzzle
  --username=username            [default: anonymous] Kuzzle username (local strategy)
```

_See code: [lib/commands/app/doctor.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/app/doctor.js)_

`kourou app:scaffold DESTINATION`
---------------------------------

[](https://github.com/kuzzleio/kourou#kourou-appscaffold-destination)
Scaffolds a new Kuzzle application

```
USAGE
  $ kourou app:scaffold DESTINATION

ARGUMENTS
  DESTINATION  Directory to scaffold the app

OPTIONS
  --flavor=flavor  [default: generic] Template flavor ("generic", "iot").
  --help           show CLI help
```

_See code: [lib/commands/app/scaffold.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/app/scaffold.js)_

`kourou app:start-services`
---------------------------

[](https://github.com/kuzzleio/kourou#kourou-appstart-services)
Starts Kuzzle services (Elasticsearch and Redis)

```
USAGE
  $ kourou app:start-services

OPTIONS
  --check  Check prerequisite before running services
  --help   show CLI help
```

_See code: [lib/commands/app/start-services.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/app/start-services.js)_

`kourou autocomplete [SHELL]`
-----------------------------

[](https://github.com/kuzzleio/kourou#kourou-autocomplete-shell)
display autocomplete installation instructions

```
USAGE
  $ kourou autocomplete [SHELL]

ARGUMENTS
  SHELL  shell type

OPTIONS
  -r, --refresh-cache  Refresh cache (ignores displaying instructions)

EXAMPLES
  $ kourou autocomplete
  $ kourou autocomplete bash
  $ kourou autocomplete zsh
  $ kourou autocomplete --refresh-cache
```

_See code: [@oclif/plugin-autocomplete](https://github.com/oclif/plugin-autocomplete/blob/v1.3.10/src/commands/autocomplete/index.ts)_

`kourou collection:create INDEX COLLECTION [BODY]`
--------------------------------------------------

[](https://github.com/kuzzleio/kourou#kourou-collectioncreate-index-collection-body)
Creates a collection

```
USAGE
  $ kourou collection:create INDEX COLLECTION [BODY]

ARGUMENTS
  INDEX       Index name
  COLLECTION  Collection name
  BODY        Collection mappings and settings in JS or JSON format. Will be read from STDIN if available

OPTIONS
  --api-key=api-key    Kuzzle user api-key
  --as=as              Impersonate a user
  --help               show CLI help
  --host=host          [default: localhost] Kuzzle server host
  --password=password  Kuzzle user password
  --port=port          [default: 7512] Kuzzle server port
  --protocol=protocol  [default: ws] Kuzzle protocol (http or ws)
  --ssl                Use SSL to connect to Kuzzle
  --username=username  [default: anonymous] Kuzzle username (local strategy)
```

_See code: [lib/commands/collection/create.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/collection/create.js)_

`kourou collection:export INDEX COLLECTION`
-------------------------------------------

[](https://github.com/kuzzleio/kourou#kourou-collectionexport-index-collection)
Exports a collection (JSONL format)

```
USAGE
  $ kourou collection:export INDEX COLLECTION

ARGUMENTS
  INDEX       Index name
  COLLECTION  Collection name

OPTIONS
  --api-key=api-key
      Kuzzle user api-key

  --as=as
      Impersonate a user

  --batch-size=batch-size
      [default: 2000] Maximum batch size (see limits.documentsFetchCount config)

  --editor
      Open an editor (EDITOR env variable) to edit the query before sending

  --fields=fields
      [CSV format only] The list of fields to be included in the CSV export in dot-path format.

      Example:
      --fields oneField,anotherField,yetAnotherOne.nested.moarNested

      Note that the '_id' field is always included in the CSV export. Leaving this option empty implies that all
      exportable fields in the mapping will be exported.

  --format=jsonl|kuzzle|csv
      [default: jsonl] "kuzzle" will export in Kuzzle format usable for internal fixtures,
      "jsonl" allows to import that data back with kourou,
      "csv" allows to import data into Excel (please, specify the fields to export using the --fields option).

  --help
      show CLI help

  --host=host
      [default: localhost] Kuzzle server host

  --password=password
      Kuzzle user password

  --path=path
      Dump root directory

  --port=port
      [default: 7512] Kuzzle server port

  --protocol=protocol
      [default: ws] Kuzzle protocol (http or websocket)

  --query=query
      [default: {}] Only dump documents matching the query (JS or JSON format)

  --scrollTTL=scrollTTL
      [default: 20s] The scroll TTL option to pass to the dump operation (which performs a document.search under the
      hood),
      expressed in ms format, e.g. '2s', '1m', '3h'.

  --ssl
      Use SSL to connect to Kuzzle

  --type=type
      [default: all] Type of the export: all, mappings, data

  --username=username
      [default: anonymous] Kuzzle username (local strategy)

EXAMPLES
  kourou collection:export nyc-open-data yellow-taxi
  kourou collection:export nyc-open-data yellow-taxi --query '{ term: { city: "Saigon" } }'
```

_See code: [lib/commands/collection/export.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/collection/export.js)_

`kourou collection:import PATH`
-------------------------------

[](https://github.com/kuzzleio/kourou#kourou-collectionimport-path)
Imports a collection

```
USAGE
  $ kourou collection:import PATH

ARGUMENTS
  PATH  Dump directory path

OPTIONS
  --api-key=api-key        Kuzzle user api-key
  --as=as                  Impersonate a user
  --batch-size=batch-size  [default: 200] Maximum batch size (see limits.documentsWriteCount config)
  --collection=collection  If set, override the collection destination name
  --help                   show CLI help
  --host=host              [default: localhost] Kuzzle server host
  --index=index            If set, override the index destination name
  --no-mappings            Skip collection mappings
  --password=password      Kuzzle user password
  --port=port              [default: 7512] Kuzzle server port
  --protocol=protocol      [default: ws] Kuzzle protocol (http or websocket)
  --ssl                    Use SSL to connect to Kuzzle
  --username=username      [default: anonymous] Kuzzle username (local strategy)
```

_See code: [lib/commands/collection/import.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/collection/import.js)_

`kourou collection:migrate SCRIPT PATH`
---------------------------------------

[](https://github.com/kuzzleio/kourou#kourou-collectionmigrate-script-path)
Migrate a collection by transforming documents from a dump file and importing them into Kuzzle

```
USAGE
  $ kourou collection:migrate SCRIPT PATH

ARGUMENTS
  SCRIPT  Migration script path
  PATH    Collection dump path

OPTIONS
  --api-key=api-key        Kuzzle user api-key
  --as=as                  Impersonate a user
  --batch-size=batch-size  [default: 200] Maximum batch size (see limits.documentsWriteCount config)
  --collection=collection  If set, override the collection destination name
  --help                   show CLI help
  --host=host              [default: localhost] Kuzzle server host
  --index=index            If set, override the index destination name
  --password=password      Kuzzle user password
  --port=port              [default: 7512] Kuzzle server port
  --protocol=protocol      [default: ws] Kuzzle protocol (http or websocket)
  --ssl                    Use SSL to connect to Kuzzle
  --username=username      [default: anonymous] Kuzzle username (local strategy)
```

_See code: [lib/commands/collection/migrate.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/collection/migrate.js)_

`kourou config:diff FIRST SECOND`
---------------------------------

[](https://github.com/kuzzleio/kourou#kourou-configdiff-first-second)
Returns differences between two Kuzzle configuration files (kuzzlerc)

```
USAGE
  $ kourou config:diff FIRST SECOND

ARGUMENTS
  FIRST   First configuration file
  SECOND  Second configuration file

OPTIONS
  --strict  Exit with an error if differences are found
  --values  Also displays value changes

EXAMPLE
  kourou config:diff config/local/kuzzlerc config/production/kuzzlerc
```

_See code: [lib/commands/config/diff.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/config/diff.js)_

`kourou document:search INDEX COLLECTION [QUERY]`
-------------------------------------------------

[](https://github.com/kuzzleio/kourou#kourou-documentsearch-index-collection-query)
Searches for documents

```
USAGE
  $ kourou document:search INDEX COLLECTION [QUERY]

ARGUMENTS
  INDEX       Index name
  COLLECTION  Collection name
  QUERY       Search query in JS or JSON format.

OPTIONS
  --api-key=api-key    Kuzzle user api-key
  --as=as              Impersonate a user
  --editor             Open an editor (EDITOR env variable) to edit the request before sending
  --from=from          Optional offset
  --help               show CLI help
  --host=host          [default: localhost] Kuzzle server host
  --lang=lang          [default: koncorde] Specify the query language to use
  --password=password  Kuzzle user password
  --port=port          [default: 7512] Kuzzle server port
  --protocol=protocol  [default: ws] Kuzzle protocol (http or ws)
  --scroll=scroll      Optional scroll TTL
  --size=size          Optional page size
  --sort=sort          [default: {}] Sort in JS or JSON format.
  --ssl                Use SSL to connect to Kuzzle
  --username=username  [default: anonymous] Kuzzle username (local strategy)

EXAMPLES
  kourou document:search iot sensors '{ equals: { name: "corona" } }'
  kourou document:search iot sensors '{ match: { name: "cOrOnna" } }' -a lang=elasticsearch
  kourou document:search iot sensors --editor
```

_See code: [lib/commands/document/search.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/document/search.js)_

`kourou es:aliases:cat`
-----------------------

[](https://github.com/kuzzleio/kourou#kourou-esaliasescat)
Lists available ES aliases

```
USAGE
  $ kourou es:aliases:cat

OPTIONS
  -g, --grep=grep  Match output with pattern
  -n, --node=node  [default: http://localhost:9200] Elasticsearch server URL
  --help           show CLI help
```

_See code: [lib/commands/es/aliases/cat.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/es/aliases/cat.js)_

`kourou es:indices:cat`
-----------------------

[](https://github.com/kuzzleio/kourou#kourou-esindicescat)
Lists available ES indexes

```
USAGE
  $ kourou es:indices:cat

OPTIONS
  -g, --grep=grep  Match output with pattern
  -n, --node=node  [default: http://localhost:9200] Elasticsearch server URL
  --help           show CLI help
```

_See code: [lib/commands/es/indices/cat.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/es/indices/cat.js)_

`kourou es:indices:get INDEX ID`
--------------------------------

[](https://github.com/kuzzleio/kourou#kourou-esindicesget-index-id)
Gets a document from ES

```
USAGE
  $ kourou es:indices:get INDEX ID

ARGUMENTS
  INDEX  ES Index name
  ID     Document ID

OPTIONS
  -n, --node=node  [default: http://localhost:9200] Elasticsearch server URL
  --help           show CLI help
```

_See code: [lib/commands/es/indices/get.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/es/indices/get.js)_

`kourou es:indices:insert INDEX`
--------------------------------

[](https://github.com/kuzzleio/kourou#kourou-esindicesinsert-index)
Inserts a document directly into ES (will replace if exists)

```
USAGE
  $ kourou es:indices:insert INDEX

ARGUMENTS
  INDEX  ES Index name

OPTIONS
  -n, --node=node  [default: http://localhost:9200] Elasticsearch server URL
  --body=body      [default: {}] Document body in JSON
  --help           show CLI help
  --id=id          Document ID
```

_See code: [lib/commands/es/indices/insert.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/es/indices/insert.js)_

`kourou es:migrate`
-------------------

[](https://github.com/kuzzleio/kourou#kourou-esmigrate)
Migrate all the index from an Elasticsearch (or a file) to another Elasticsearch

```
USAGE
  $ kourou es:migrate

OPTIONS
  --batch-size=batch-size  [default: 1000] How many documents to move in batch per operation
  --dest=dest              (required) Migration destination provider
  --dry-run                Print witch collections will be migrated
  --esVersion=7|8          [default: 7] Elasticsearch version to use for the migration
  --help                   show CLI help
  --no-interactive         Skip confirmation interactive prompts (perfect for scripting)
  --only-mappings          Only migrate mappings
  --pattern=pattern        Pattern to match indices to migrate
  --reset                  Reset destination Elasticsearch server
  --scroll=scroll          [default: 30s] Scroll duration for Elasticsearch scrolling
  --src=src                (required) Migration source provider

EXAMPLES
  kourou es:migrate --src http://elasticsearch:9200 --dest ./my-backup
  kourou es:migrate --src ./my-backup --dest http://elasticsearch:9200
  kourou es:migrate --src ./my-backup --dest http://username:password@elasticsearch:9200 --reset
  kourou es:migrate --src ./my-backup --dest http://nologin:api-key@elasticsearch:9200 --reset // nologin is a special 
  username that allows you to use an API key as password
  kourou es:migrate --src http://elasticsearch:9200 --dest ./my-backup --batch-size 2000 --pattern 
  '&myindexes.collection-*'
  kourou es:migrate --src ./my-backup --dest http://elasticsearch:9200 --reset --batch-size 2000 --no-interactive
  kourou es:migrate --src ./my-backup --dest http://elasticsearch:9200 --reset --batch-size 2000 --no-interactive 
  --esVersion 8
```

_See code: [lib/commands/es/migrate.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/es/migrate.js)_

`kourou es:snapshot:create REPOSITORY NAME`
-------------------------------------------

[](https://github.com/kuzzleio/kourou#kourou-essnapshotcreate-repository-name)
Create a snapshot repository inside an ES instance

```
USAGE
  $ kourou es:snapshot:create REPOSITORY NAME

ARGUMENTS
  REPOSITORY  ES repository name
  NAME        ES snapshot name

OPTIONS
  -n, --node=node  [default: http://localhost:9200] Elasticsearch server URL
  --help           show CLI help
```

_See code: [lib/commands/es/snapshot/create.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/es/snapshot/create.js)_

`kourou es:snapshot:create-repository REPOSITORY LOCATION`
----------------------------------------------------------

[](https://github.com/kuzzleio/kourou#kourou-essnapshotcreate-repository-repository-location)
Create a FS snapshot repository inside an ES instance

```
USAGE
  $ kourou es:snapshot:create-repository REPOSITORY LOCATION

ARGUMENTS
  REPOSITORY  ES repository name
  LOCATION    ES snapshot repository location

OPTIONS
  -n, --node=node  [default: http://localhost:9200] Elasticsearch server URL
  --compress       Compress data when storing them
  --help           show CLI help
```

_See code: [lib/commands/es/snapshot/create-repository.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/es/snapshot/create-repository.js)_

`kourou es:snapshot:list REPOSITORY`
------------------------------------

[](https://github.com/kuzzleio/kourou#kourou-essnapshotlist-repository)
List all snapshot from a repository acknowledge by an ES instance

```
USAGE
  $ kourou es:snapshot:list REPOSITORY

ARGUMENTS
  REPOSITORY  Name of repository from which to fetch the snapshot information

OPTIONS
  -n, --node=node  [default: http://localhost:9200] Elasticsearch server URL
  --help           show CLI help
```

_See code: [lib/commands/es/snapshot/list.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/es/snapshot/list.js)_

`kourou es:snapshot:restore REPOSITORY NAME`
--------------------------------------------

[](https://github.com/kuzzleio/kourou#kourou-essnapshotrestore-repository-name)
Restore a snapshot repository inside an ES instance

```
USAGE
  $ kourou es:snapshot:restore REPOSITORY NAME

ARGUMENTS
  REPOSITORY  ES repository name
  NAME        ES snapshot name

OPTIONS
  -n, --node=node  [default: http://localhost:9200] Elasticsearch server URL
  --help           show CLI help
```

_See code: [lib/commands/es/snapshot/restore.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/es/snapshot/restore.js)_

`kourou file:decrypt FILE`
--------------------------

[](https://github.com/kuzzleio/kourou#kourou-filedecrypt-file)
Decrypts an encrypted file.

```
USAGE
  $ kourou file:decrypt FILE

ARGUMENTS
  FILE  Encrypted file

OPTIONS
  -f, --force                    Overwrite the output file if it already exists
  -o, --output-file=output-file  Output file (default: remove ".enc")
  --vault-key=vault-key          Kuzzle Vault Key (or KUZZLE_VAULT_KEY)

EXAMPLES
  kourou file:decrypt books/cryptonomicon.txt.enc --vault-key <vault-key>
  kourou file:decrypt books/cryptonomicon.txt.enc -o books/cryptonomicon.txt --vault-key <vault-key>
```

_See code: [lib/commands/file/decrypt.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/file/decrypt.js)_

`kourou file:encrypt FILE`
--------------------------

[](https://github.com/kuzzleio/kourou#kourou-fileencrypt-file)
Encrypts an entire file.

```
USAGE
  $ kourou file:encrypt FILE

ARGUMENTS
  FILE  Filename

OPTIONS
  -f, --force                    Overwrite the output file if it already exists
  -o, --output-file=output-file  Output file (default: <filename>.enc)
  --vault-key=vault-key          Kuzzle Vault Key (or KUZZLE_VAULT_KEY)

EXAMPLES
  kourou file:encrypt books/cryptonomicon.txt --vault-key <vault-key>
  kourou file:encrypt books/cryptonomicon.txt -o books/cryptonomicon.txt.enc --vault-key <vault-key>
```

_See code: [lib/commands/file/encrypt.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/file/encrypt.js)_

`kourou file:test FILE`
-----------------------

[](https://github.com/kuzzleio/kourou#kourou-filetest-file)
Tests if an encrypted file can be decrypted.

```
USAGE
  $ kourou file:test FILE

ARGUMENTS
  FILE  Encrypted file

OPTIONS
  --vault-key=vault-key  Kuzzle Vault Key (or KUZZLE_VAULT_KEY)

EXAMPLE
  kourou file:test books/cryptonomicon.txt.enc --vault-key <vault-key>
```

_See code: [lib/commands/file/test.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/file/test.js)_

`kourou help [COMMAND]`
-----------------------

[](https://github.com/kuzzleio/kourou#kourou-help-command)
display help for kourou

```
USAGE
  $ kourou help [COMMAND]

ARGUMENTS
  COMMAND  command to show help for

OPTIONS
  --all  see all commands in CLI
```

_See code: [@oclif/plugin-help](https://github.com/oclif/plugin-help/blob/v3.2.18/src/commands/help.ts)_

`kourou import PATH`
--------------------

[](https://github.com/kuzzleio/kourou#kourou-import-path)
Recursively imports dump files from a root directory

```
USAGE
  $ kourou import PATH

ARGUMENTS
  PATH  Root directory containing dumps

OPTIONS
  --api-key=api-key        Kuzzle user api-key
  --as=as                  Impersonate a user
  --batch-size=batch-size  [default: 200] Maximum batch size (see limits.documentsWriteCount config)
  --help                   show CLI help
  --host=host              [default: localhost] Kuzzle server host
  --password=password      Kuzzle user password
  --port=port              [default: 7512] Kuzzle server port
  --preserve-anonymous     Preserve anonymous rights
  --protocol=protocol      [default: ws] Kuzzle protocol (http or websocket)
  --ssl                    Use SSL to connect to Kuzzle
  --username=username      [default: anonymous] Kuzzle username (local strategy)
```

_See code: [lib/commands/import.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/import.js)_

`kourou index:export INDEX`
---------------------------

[](https://github.com/kuzzleio/kourou#kourou-indexexport-index)
Exports an index (JSONL or Kuzzle format)

```
USAGE
  $ kourou index:export INDEX

ARGUMENTS
  INDEX  Index name

OPTIONS
  --api-key=api-key        Kuzzle user api-key
  --as=as                  Impersonate a user
  --batch-size=batch-size  [default: 2000] Maximum batch size (see limits.documentsFetchCount config)

  --format=format          [default: jsonl] "jsonl or kuzzle - kuzzle will export in Kuzzle format usable for internal
                           fixtures and jsonl allows to import that data back with kourou

  --help                   show CLI help

  --host=host              [default: localhost] Kuzzle server host

  --password=password      Kuzzle user password

  --path=path              Dump root directory

  --port=port              [default: 7512] Kuzzle server port

  --protocol=protocol      [default: ws] Kuzzle protocol (http or websocket)

  --query=query            [default: {}] Only dump documents in collections matching the query (JS or JSON format)

  --scrollTTL=scrollTTL    [default: 20s] The scroll TTL option to pass to the dump operation (which performs a
                           document.search under the hood),
                           expressed in ms format, e.g. '2s', '1m', '3h'.

  --ssl                    Use SSL to connect to Kuzzle

  --type=type              [default: all] Type of the export: all, mappings, data

  --username=username      [default: anonymous] Kuzzle username (local strategy)

EXAMPLES
  kourou index:export nyc-open-data
  kourou index:export nyc-open-data --query '{"range":{"_kuzzle_info.createdAt":{"gt":1632935638866}}}'
```

_See code: [lib/commands/index/export.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/index/export.js)_

`kourou index:import PATH`
--------------------------

[](https://github.com/kuzzleio/kourou#kourou-indeximport-path)
Imports an index (JSONL format)

```
USAGE
  $ kourou index:import PATH

ARGUMENTS
  PATH  Dump directory or file

OPTIONS
  --api-key=api-key        Kuzzle user api-key
  --as=as                  Impersonate a user
  --batch-size=batch-size  [default: 200] Maximum batch size (see limits.documentsWriteCount config)
  --help                   show CLI help
  --host=host              [default: localhost] Kuzzle server host
  --index=index            If set, override the index destination name
  --no-mappings            Skip collections mappings
  --password=password      Kuzzle user password
  --port=port              [default: 7512] Kuzzle server port
  --protocol=protocol      [default: ws] Kuzzle protocol (http or websocket)
  --ssl                    Use SSL to connect to Kuzzle
  --username=username      [default: anonymous] Kuzzle username (local strategy)

EXAMPLES
  kourou index:import ./dump/iot-data
  kourou index:import ./dump/iot-data --index iot-data-production --no-mappings
```

_See code: [lib/commands/index/import.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/index/import.js)_

`kourou instance:kill`
----------------------

[](https://github.com/kuzzleio/kourou#kourou-instancekill)
Stop and remove all the containers of a running kuzzle instance

```
USAGE
  $ kourou instance:kill

OPTIONS
  -a, --all                Kill all instances
  -i, --instance=instance  Kuzzle instance name [ex: stack-0]
```

_See code: [lib/commands/instance/kill.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/instance/kill.js)_

`kourou instance:list`
----------------------

[](https://github.com/kuzzleio/kourou#kourou-instancelist)
Lists the Kuzzle running instances

```
USAGE
  $ kourou instance:list
```

_See code: [lib/commands/instance/list.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/instance/list.js)_

`kourou instance:logs`
----------------------

[](https://github.com/kuzzleio/kourou#kourou-instancelogs)
Displays the logs of a running Kuzzle

```
USAGE
  $ kourou instance:logs

OPTIONS
  -f, --follow             Follow log output
  -i, --instance=instance  Kuzzle instance name
```

_See code: [lib/commands/instance/logs.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/instance/logs.js)_

`kourou instance:spawn`
-----------------------

[](https://github.com/kuzzleio/kourou#kourou-instancespawn)
Spawn a new Kuzzle instance

```
USAGE
  $ kourou instance:spawn

OPTIONS
  -v, --version=version  [default: 2] Core-version of the instance to spawn
  --check                Check prerequisite before running Kuzzle
  --help                 show CLI help
```

_See code: [lib/commands/instance/spawn.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/instance/spawn.js)_

`kourou paas:login`
-------------------

[](https://github.com/kuzzleio/kourou#kourou-paaslogin)
Login for a PaaS project

```
USAGE
  $ kourou paas:login

OPTIONS
  --help               show CLI help
  --only_npm           Only perform the login on the private NPM registry
  --project=project    Current PaaS project
  --username=username  PaaS username
```

_See code: [lib/commands/paas/login.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/paas/login.js)_

`kourou profile:export`
-----------------------

[](https://github.com/kuzzleio/kourou#kourou-profileexport)
Exports profiles

```
USAGE
  $ kourou profile:export

OPTIONS
  --api-key=api-key    Kuzzle user api-key
  --as=as              Impersonate a user
  --help               show CLI help
  --host=host          [default: localhost] Kuzzle server host
  --password=password  Kuzzle user password
  --path=path          [default: profiles] Dump directory
  --port=port          [default: 7512] Kuzzle server port
  --protocol=protocol  [default: ws] Kuzzle protocol (http or websocket)
  --ssl                Use SSL to connect to Kuzzle
  --username=username  [default: anonymous] Kuzzle username (local strategy)
```

_See code: [lib/commands/profile/export.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/profile/export.js)_

`kourou profile:import PATH`
----------------------------

[](https://github.com/kuzzleio/kourou#kourou-profileimport-path)
Imports profiles

```
USAGE
  $ kourou profile:import PATH

ARGUMENTS
  PATH  Dump file

OPTIONS
  --api-key=api-key    Kuzzle user api-key
  --as=as              Impersonate a user
  --help               show CLI help
  --host=host          [default: localhost] Kuzzle server host
  --password=password  Kuzzle user password
  --port=port          [default: 7512] Kuzzle server port
  --protocol=protocol  [default: ws] Kuzzle protocol (http or websocket)
  --ssl                Use SSL to connect to Kuzzle
  --username=username  [default: anonymous] Kuzzle username (local strategy)
```

_See code: [lib/commands/profile/import.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/profile/import.js)_

`kourou realtime:subscribe INDEX COLLECTION [FILTERS]`
------------------------------------------------------

[](https://github.com/kuzzleio/kourou#kourou-realtimesubscribe-index-collection-filters)
Subscribes to realtime notifications

```
USAGE
  $ kourou realtime:subscribe INDEX COLLECTION [FILTERS]

ARGUMENTS
  INDEX       Index name
  COLLECTION  Collection name
  FILTERS     Set of Koncorde filters

OPTIONS
  --api-key=api-key    Kuzzle user api-key
  --as=as              Impersonate a user

  --display=display    [default: result] Path of the property to display from the notification (empty string to display
                       everything)

  --editor             Open an editor (EDITOR env variable) to edit the filters before subscribing.

  --help               show CLI help

  --host=host          [default: localhost] Kuzzle server host

  --password=password  Kuzzle user password

  --port=port          [default: 7512] Kuzzle server port

  --protocol=protocol  [default: websocket] Kuzzle protocol (only websocket for realtime)

  --scope=scope        [default: all] Subscribe to document entering or leaving the scope (all, in, out, none)

  --ssl                Use SSL to connect to Kuzzle

  --username=username  [default: anonymous] Kuzzle username (local strategy)

  --users=users        [default: all] Subscribe to users entering or leaving the room (all, in, out, none)

  --volatile=volatile  [default: {}] Additional subscription information used in user join/leave notifications

EXAMPLES
  kourou realtime:subscribe iot-data sensors
  kourou realtime:subscribe iot-data sensors '{ range: { temperature: { gt: 0 } } }'
  kourou realtime:subscribe iot-data sensors '{ exists: "position" }' --scope out
  kourou realtime:subscribe iot-data sensors --users all --volatile '{ clientId: "citizen-kane" }'
  kourou realtime:subscribe iot-data sensors --display result._source.temperature
```

_See code: [lib/commands/realtime/subscribe.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/realtime/subscribe.js)_

`kourou redis:list-keys [MATCH]`
--------------------------------

[](https://github.com/kuzzleio/kourou#kourou-redislist-keys-match)
Lists keys stored in Redis

```
USAGE
  $ kourou redis:list-keys [MATCH]

ARGUMENTS
  MATCH  [default: *] Match Redis keys with a pattern

OPTIONS
  --api-key=api-key    Kuzzle user api-key
  --as=as              Impersonate a user
  --help               show CLI help
  --host=host          [default: localhost] Kuzzle server host
  --max=max            [default: -1] Maximum number of page to retrieve (-1 to retrieve everything)
  --password=password  Kuzzle user password
  --port=port          [default: 7512] Kuzzle server port
  --protocol=protocol  [default: ws] Kuzzle protocol (http or ws)
  --remove             Remove matching keys
  --size=size          [default: 100] Page size
  --ssl                Use SSL to connect to Kuzzle
  --username=username  [default: anonymous] Kuzzle username (local strategy)

EXAMPLES
  kourou redis:list-keys "*cluster*"
  kourou redis:list-keys "counters/*" --remove
```

_See code: [lib/commands/redis/list-keys.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/redis/list-keys.js)_

`kourou role:export`
--------------------

[](https://github.com/kuzzleio/kourou#kourou-roleexport)
Exports roles

```
USAGE
  $ kourou role:export

OPTIONS
  --api-key=api-key    Kuzzle user api-key
  --as=as              Impersonate a user
  --help               show CLI help
  --host=host          [default: localhost] Kuzzle server host
  --password=password  Kuzzle user password
  --path=path          [default: roles] Dump directory
  --port=port          [default: 7512] Kuzzle server port
  --protocol=protocol  [default: ws] Kuzzle protocol (http or websocket)
  --ssl                Use SSL to connect to Kuzzle
  --username=username  [default: anonymous] Kuzzle username (local strategy)
```

_See code: [lib/commands/role/export.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/role/export.js)_

`kourou role:import PATH`
-------------------------

[](https://github.com/kuzzleio/kourou#kourou-roleimport-path)
Import roles

```
USAGE
  $ kourou role:import PATH

ARGUMENTS
  PATH  Dump file

OPTIONS
  --api-key=api-key     Kuzzle user api-key
  --as=as               Impersonate a user
  --help                show CLI help
  --host=host           [default: localhost] Kuzzle server host
  --password=password   Kuzzle user password
  --port=port           [default: 7512] Kuzzle server port
  --preserve-anonymous  Preserve anonymous rights
  --protocol=protocol   [default: ws] Kuzzle protocol (http or websocket)
  --ssl                 Use SSL to connect to Kuzzle
  --username=username   [default: anonymous] Kuzzle username (local strategy)
```

_See code: [lib/commands/role/import.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/role/import.js)_

`kourou sdk:execute [CODE]`
---------------------------

[](https://github.com/kuzzleio/kourou#kourou-sdkexecute-code)
Executes arbitrary code.

```
USAGE
  $ kourou sdk:execute [CODE]

ARGUMENTS
  CODE  Code to execute. Will be read from STDIN if available.

OPTIONS
  -v, --var=var        Additional arguments injected into the code. (eg: --var 'index="iot-data"'
  --api-key=api-key    Kuzzle user api-key
  --as=as              Impersonate a user
  --editor             Open an editor (EDITOR env variable) to edit the code before executing it.
  --help               show CLI help
  --host=host          [default: localhost] Kuzzle server host
  --keep-alive         Keep the connection running (websocket only)
  --password=password  Kuzzle user password
  --port=port          [default: 7512] Kuzzle server port
  --print-raw          Print only the script result to stdout
  --protocol=protocol  [default: ws] Kuzzle protocol (http or ws)
  --ssl                Use SSL to connect to Kuzzle
  --username=username  [default: anonymous] Kuzzle username (local strategy)

DESCRIPTION
  Executes arbitrary code.

  Code Execution

    Provided code will be executed in an async method.
    You can access a connected and authenticated SDK with the "sdk" variable.
    Templated variable passed as the command arguments are also accessible within the same name.
    Returned value will be printed on the standard output (e.g. 'return await sdk.server.now();').
    Errors will be caught and printed on the error output (e.g. 'throw new Error("failure");').

  Provide code

    code can be passed as an argument
    code will be read from STDIN if available

    Examples:
      - kourou sdk:execute 'return await sdk.server.now()'
      - kourou sdk:execute 'return await sdk.index.exists(index)' --var 'index="iot-data"'
      - kourou sdk:execute < snippet.js
      - echo 'return await sdk.server.now()' | kourou sdk:execute

  Other

    use the --editor flag to modify the code before executing it

    Examples:
      - kourou sdk:execute 'return await sdk.server.now()' --editor
```

_See code: [lib/commands/sdk/execute.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/sdk/execute.js)_

`kourou sdk:query CONTROLLER:ACTION`
------------------------------------

[](https://github.com/kuzzleio/kourou#kourou-sdkquery-controlleraction)
Executes an API query.

```
USAGE
  $ kourou sdk:query CONTROLLER:ACTION

ARGUMENTS
  CONTROLLER:ACTION  Controller and action (eg: "server:now")

OPTIONS
  -a, --arg=arg                Additional argument. Repeatable. (e.g. "-a refresh=wait_for")
  -c, --collection=collection  Collection argument
  -i, --index=index            Index argument
  --api-key=api-key            Kuzzle user api-key
  --as=as                      Impersonate a user
  --body=body                  [default: {}] Request body in JS or JSON format. Will be read from STDIN if available.
  --body-editor                Open an editor (EDITOR env variable) to edit the body before sending.

  --display=display            [default: result] Path of the property to display from the response (empty string to
                               display the result)

  --editor                     Open an editor (EDITOR env variable) to edit the request before sending.

  --help                       show CLI help

  --host=host                  [default: localhost] Kuzzle server host

  --id=id                      ID argument (_id)

  --password=password          Kuzzle user password

  --port=port                  [default: 7512] Kuzzle server port

  --print-raw                  Print only the query result to stdout

  --protocol=protocol          [default: ws] Kuzzle protocol (http or ws)

  --ssl                        Use SSL to connect to Kuzzle

  --username=username          [default: anonymous] Kuzzle username (local strategy)

DESCRIPTION
  Executes an API query.

  Query arguments

    Arguments can be passed and repeated using the --arg or -a flag.
    Index and collection names can be passed with --index (-i) and --collection (-c) flags
    ID can be passed with the --id flag.

    Examples:
      - kourou sdk:query document:delete -i iot -c sensors -a refresh=wait_for

  Query body

    Body can be passed with the --body flag with either a JSON or JS string.
    Body will be read from STDIN if available

    Examples:
      - kourou sdk:query document:create -i iot -c sensors --body '{creation: Date.now())}'
      - kourou sdk:query admin:loadMappings < mappings.json
      - echo '{dynamic: "strict"}' | kourou sdk:query collection:create -i iot -c sensors

  Other

    Use the --editor flag to modify the query before sending it to Kuzzle
    Use the --display flag to display a specific property of the response

    Examples:
      - kourou sdk:query document:create -i iot -c sensors --editor
      - kourou sdk:query server:now --display 'result.now'

  Default fallback to API action

    It's possible to use the "sdk:query" command by only specifying the corresponding controller
    and action as first argument.

    Kourou will try to infer the first arguments to one the following pattern:
      - <command> <index>
      - <command> <body>
      - <command> <index> <collection>
      - <command> <index> <collection> <id>
      - <command> <index> <collection> <body>
      - <command> <index> <collection> <id> <body>

    If a flag is given (-i, -c, --body or --id), then the flag value has priority over
    argument infering.

    Examples:
      - kourou collection:list iot
      - kourou security:createUser '{ "content": { "profileIds": ["default"] } }' --id yagmur
      - kourou collection:delete iot sensors
      - kourou document:createOrReplace iot sensors sigfox-1 '{}'
      - kourou bulk:import iot sensors '{ bulkData: [...] }'
      - kourou admin:loadMappings < mappings.json
```

_See code: [lib/commands/sdk/query.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/sdk/query.js)_

`kourou user:export`
--------------------

[](https://github.com/kuzzleio/kourou#kourou-userexport)
Exports users to JSON.

```
USAGE
  $ kourou user:export

OPTIONS
  --api-key=api-key                        Kuzzle user api-key
  --as=as                                  Impersonate a user
  --batch-size=batch-size                  [default: 2000] Maximum batch size (see limits.documentsFetchCount config)
  --exclude=exclude                        Exclude users by matching their IDs with a regexp
  --generate-credentials                   Generate credentials with a random password for users
  --generated-username=generated-username  [default: _id] User content property used as a username for local credentials
  --help                                   show CLI help
  --host=host                              [default: localhost] Kuzzle server host
  --password=password                      Kuzzle user password
  --path=path                              [default: users] Dump directory
  --port=port                              [default: 7512] Kuzzle server port
  --protocol=protocol                      [default: ws] Kuzzle protocol (http or websocket)
  --ssl                                    Use SSL to connect to Kuzzle
  --username=username                      [default: anonymous] Kuzzle username (local strategy)

DESCRIPTION
  Exports users to JSON.

  The users will be exported WITHOUT their credentials since Kuzzzle can't access them.

  You can either:
    - Manually re-create credentials for your users
    - Use the "mustChangePasswordIfSetByAdmin" option Kuzzle password policies (see 
  https://github.com/kuzzleio/kuzzle-plugin-auth-passport-local/#optional-properties)
    - Use the "--generate-credentials" flag to auto-generate credentials for your users

  Auto-generation of credentials

    With the "--generate-credentials" flag, Kourou will add credentials for the "local" strategy.
    By default, the username will be the user ID.
    Use the "generated-username" flag to use an other property than the user ID for the generated username
    The password will be a strong random 40 characters string

  Examples:

    - kourou user:export
    - kourou user:export --exclude '.*admin.*' --exclude 'supervisor.*'
    - kourou user:export --generate-credentials
    - kourou user:export --generate-credentials --generated-username content.email
```

_See code: [lib/commands/user/export.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/user/export.js)_

`kourou user:export-mappings`
-----------------------------

[](https://github.com/kuzzleio/kourou#kourou-userexport-mappings)
Exports users collection mappings to JSON.

```
USAGE
  $ kourou user:export-mappings

OPTIONS
  --api-key=api-key    Kuzzle user api-key
  --as=as              Impersonate a user
  --help               show CLI help
  --host=host          [default: localhost] Kuzzle server host
  --password=password  Kuzzle user password
  --path=path          [default: users] Dump directory
  --port=port          [default: 7512] Kuzzle server port
  --protocol=protocol  [default: ws] Kuzzle protocol (http or websocket)
  --ssl                Use SSL to connect to Kuzzle
  --username=username  [default: anonymous] Kuzzle username (local strategy)
```

_See code: [lib/commands/user/export-mappings.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/user/export-mappings.js)_

`kourou user:import PATH`
-------------------------

[](https://github.com/kuzzleio/kourou#kourou-userimport-path)
Imports users

```
USAGE
  $ kourou user:import PATH

ARGUMENTS
  PATH  Dump file

OPTIONS
  --api-key=api-key    Kuzzle user api-key
  --as=as              Impersonate a user
  --help               show CLI help
  --host=host          [default: localhost] Kuzzle server host
  --password=password  Kuzzle user password
  --port=port          [default: 7512] Kuzzle server port
  --protocol=protocol  [default: ws] Kuzzle protocol (http or websocket)
  --ssl                Use SSL to connect to Kuzzle
  --username=username  [default: anonymous] Kuzzle username (local strategy)
```

_See code: [lib/commands/user/import.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/user/import.js)_

`kourou user:import-mappings PATH`
----------------------------------

[](https://github.com/kuzzleio/kourou#kourou-userimport-mappings-path)
Imports users collection mappings

```
USAGE
  $ kourou user:import-mappings PATH

ARGUMENTS
  PATH  Dump file

OPTIONS
  --api-key=api-key    Kuzzle user api-key
  --as=as              Impersonate a user
  --help               show CLI help
  --host=host          [default: localhost] Kuzzle server host
  --password=password  Kuzzle user password
  --port=port          [default: 7512] Kuzzle server port
  --protocol=protocol  [default: ws] Kuzzle protocol (http or websocket)
  --ssl                Use SSL to connect to Kuzzle
  --username=username  [default: anonymous] Kuzzle username (local strategy)
```

_See code: [lib/commands/user/import-mappings.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/user/import-mappings.js)_

`kourou vault:add SECRETS-FILE KEY VALUE`
-----------------------------------------

[](https://github.com/kuzzleio/kourou#kourou-vaultadd-secrets-file-key-value)
Adds an encrypted key to an encrypted secrets file.

```
USAGE
  $ kourou vault:add SECRETS-FILE KEY VALUE

ARGUMENTS
  SECRETS-FILE  Encrypted secrets file
  KEY           Path to the key (lodash style)
  VALUE         Value to encrypt

OPTIONS
  --vault-key=vault-key  Kuzzle Vault Key (or KUZZLE_VAULT_KEY)

DESCRIPTION
  Adds an encrypted key to an encrypted secrets file.

  A new secrets file is created if it does not yet exist.

  Encrypted secrets are meant to be loaded inside an application with Kuzzle Vault.

  See https://github.com/kuzzleio/kuzzle-vault/ for more information.

EXAMPLE
  kourou vault:add config/secrets.enc.json aws.s3.keyId b61e267676660c314b006b06 --vault-key <vault-key>
```

_See code: [lib/commands/vault/add.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/vault/add.js)_

`kourou vault:decrypt FILE`
---------------------------

[](https://github.com/kuzzleio/kourou#kourou-vaultdecrypt-file)
Decrypts an entire secrets file.

```
USAGE
  $ kourou vault:decrypt FILE

ARGUMENTS
  FILE  File containing encrypted secrets

OPTIONS
  -f, --force                    Overwrite the output file if it already exists
  -o, --output-file=output-file  Output file (default: remove ".enc")
  --vault-key=vault-key          Kuzzle Vault Key (or KUZZLE_VAULT_KEY)

DESCRIPTION
  Decrypts an entire secrets file.

  Decrypted secrets file must NEVER be committed into the repository.

  See https://github.com/kuzzleio/kuzzle-vault/ for more information.

EXAMPLES
  kourou vault:decrypt config/secrets.enc.json --vault-key <vault-key>
  kourou vault:decrypt config/secrets.enc.json -o config/secrets.json --vault-key <vault-key>
```

_See code: [lib/commands/vault/decrypt.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/vault/decrypt.js)_

`kourou vault:encrypt FILE`
---------------------------

[](https://github.com/kuzzleio/kourou#kourou-vaultencrypt-file)
Encrypts an entire secrets file.

```
USAGE
  $ kourou vault:encrypt FILE

ARGUMENTS
  FILE  File containing unencrypted secrets

OPTIONS
  -f, --force                    Overwrite the output file if it already exists
  -o, --output-file=output-file  Output file (default: <file>.enc.json)
  --vault-key=vault-key          Kuzzle Vault Key (or KUZZLE_VAULT_KEY)

DESCRIPTION
  Encrypts an entire secrets file.

  The secrets file must be in JSON format and it must contain only strings or objects.

  Example:
  {
    aws: {
      s3: {
        keyId: 'b61e267676660c314b006b06'
      }
    }
  }

  Encrypted secrets are meant to be loaded inside an application with Kuzzle Vault.

  See https://github.com/kuzzleio/kuzzle-vault/ for more information.

EXAMPLES
  kourou vault:encrypt config/secrets.json --vault-key <vault-key>
  kourou vault:encrypt config/secrets.json -o config/secrets_prod.enc.json --vault-key <vault-key>
```

_See code: [lib/commands/vault/encrypt.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/vault/encrypt.js)_

`kourou vault:show SECRETS-FILE [KEY]`
--------------------------------------

[](https://github.com/kuzzleio/kourou#kourou-vaultshow-secrets-file-key)
Prints an encrypted secrets file content.

```
USAGE
  $ kourou vault:show SECRETS-FILE [KEY]

ARGUMENTS
  SECRETS-FILE  Encrypted secrets file
  KEY           Path to a key (lodash style)

OPTIONS
  --vault-key=vault-key  Kuzzle Vault Key (or KUZZLE_VAULT_KEY)

DESCRIPTION
  Prints an encrypted secrets file content.

  This method can display either:
   - the entire content of the secrets file
   - a single key value

  See https://github.com/kuzzleio/kuzzle-vault/ for more information.

EXAMPLES
  kourou vault:show config/secrets.enc.json --vault-key <vault-key>
  kourou vault:show config/secrets.enc.json aws.s3.secretKey --vault-key <vault-key>
```

_See code: [lib/commands/vault/show.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/vault/show.js)_

`kourou vault:test SECRETS-FILE`
--------------------------------

[](https://github.com/kuzzleio/kourou#kourou-vaulttest-secrets-file)
Tests if an encrypted secrets file can be decrypted.

```
USAGE
  $ kourou vault:test SECRETS-FILE

ARGUMENTS
  SECRETS-FILE  Encrypted secrets file

OPTIONS
  --vault-key=vault-key  Kuzzle Vault Key (or KUZZLE_VAULT_KEY)

DESCRIPTION
  Tests if an encrypted secrets file can be decrypted.

  See https://github.com/kuzzleio/kuzzle-vault/ for more information.

EXAMPLE
  kourou vault:test config/secrets.enc.json --vault-key <vault-key>
```

_See code: [lib/commands/vault/test.js](https://github.com/kuzzleio/kourou/blob/master/lib/commands/vault/test.js)_

Where does this weird name come from?
-------------------------------------

[](https://github.com/kuzzleio/kourou#where-does-this-weird-name-come-from)
We liked the idea that this CLI is like a launchpad for the Kuzzle rocket. The place where you launch and pilot your Kuzzle instance. The place where the European Space Agency launches their rockets is in the country near the city of [Kourou](https://www.wikiwand.com/en/Kourou), in French Guiana, so we liked the idea that the Kuzzle rockets would take off from there.

Have fun with a quine
---------------------

[](https://github.com/kuzzleio/kourou#have-fun-with-a-quine)
[Quine](https://en.wikipedia.org/wiki/Quine_(computing)) are programs able to print their own source code.

$ kourou sdk:execute --print-raw '(
 function quine() {
 const quote = String.fromCharCode(39);
 const lparen = String.fromCharCode(40);
 const rparen = String.fromCharCode(41);

 console.log("kourou sdk:execute --print-raw " + quote + lparen + quine.toString() + rparen + lparen + rparen + ";" + quote)
 }
)()'

(Kuzzle must be accessible and running in local)

Telemetry
---------

[](https://github.com/kuzzleio/kourou#telemetry)
We use a custom Open Source analytics backend (you can check the code [here](https://github.com/kuzzleio/kepler)) to record the use of Kourou by users.

Collected metrics will allow us to study the use of our products in order to improve them. We do not collect any personal data about users.

You can disable usage metrics collection by setting the `KOUROU_USAGE` environment variable to `false`.
