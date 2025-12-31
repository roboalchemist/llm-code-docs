# Source: https://docs.upsun.com/languages/ruby.md

# Ruby


p:last-child]:mb-0 [&>h3]:mt-0 rounded-lg" >

### Note
You can now use composable image (BETA) to install runtimes and tools in your application container. To find out more, see the [dedicated documentation page](https://docs.upsun.com/create-apps/app-reference/composable-image.md).

Upsun supports deploying any Ruby application. Your application can use any Ruby application server such as Puma or Unicorn and deploying a Rails or a Sinatra app is very straight forward.

## Supported versions

You can select the major and minor version.

Patch versions are applied periodically for bug fixes and the like.
When you deploy your app, you always get the latest available patches.

### Ruby

   - 3.4

   - 3.3

   - 3.2

   - 3.1

   - 3.0

### Specify the language

To use Ruby, specify `ruby` as your [app's `type`](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#types):

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  <APP_NAME>:
    type: 'ruby:<VERSION_NUMBER>'
```

For example:

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'ruby:3.4'
```

### Deprecated versions

The following versions are [deprecated](https://docs.upsun.com/glossary.md#deprecated-versions).
They're available, but they don't receive security updates from upstream and aren't guaranteed to work.
They'll be removed in the future – consider migrating to a [supported version](#supported-versions).

   - 2.7

   - 2.6

   - 2.5

   - 2.4

   - 2.3

## Puma based Rails configuration

This example uses Puma to run a Ruby application.
You could use any Ruby application server such as Unicorn.

Configure the `.upsun/config.yaml` file with a few key settings as listed below.
A complete example is included at the end of this section.

1. Specify the language of your application (available versions are listed above):

    ```yaml  {location=".upsun/config.yaml"}
    applications:
      # The app's name, which must be unique within the project.
      myapp:
        type: 'ruby:3.4'
    ```

2. Setup environment variables.

   Rails runs by default on a preview environment.
   You can change the Rails/Bundler via those environment variables,
   some of which are defaults on Upsun.

    ```yaml  {location=".upsun/config.yaml"}
    applications:
      # The app's name, which must be unique within the project.
      myapp:
        type: 'ruby:3.4'
        variables:
          env:
            PIDFILE: "tmp/server.pid" # Allow to start puma directly even if `tmp/pids` directory is not created
            RAILS_ENV: "production"
            BUNDLE_WITHOUT: 'development:test'
            TARGET_RUBY_VERSION: '~>3.4' # this will allow to not fail on PATCH update of the image
    ```

   The `SECRET_KEY_BASE` variable is generated automatically based on the
   [`PLATFORM_PROJECT_ENTROPY`
   variable](https://docs.upsun.com../development/variables/use-variables.md#use-provided-variables) but you can change it.

   Based on TARGET_RUBY_VERSION, we recommand to set on your Gemfile so next
   PATCH release of ruby doesn't fail the build:

   ```ruby
   ruby ENV["TARGET_RUBY_VERSION"] || File.read(File.join(File.dirname(__FILE__), ".ruby-version")).strip
   ```

3. Build your application with the build hook.

    Assuming you have your dependencies stored in the `Gemfile` at [your app root](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#root-directory),
    create a hook like the following:

    ```yaml  {location=".upsun/config.yaml"}
    applications:
      # The app's name, which must be unique within the project.
      myapp:
        type: 'ruby:3.4'
        ...
        hooks:
          build: |
            set -e
            bundle install
            bundle exec rails assets:precompile
          deploy: bundle exec rake db:migrate
    ```

    These are installed as your project dependencies in your environment.
    You can also use the `dependencies` key to install global dependencies.
    These can be Ruby, Python, NodeJS, or PHP libraries.

    If you have assets, it's likely that you need NodeJS/yarn.

    ```yaml  {location=".upsun/config.yaml"}
    applications:
      # The app's name, which must be unique within the project.
      myapp:
        type: 'ruby:3.4'
        ...
        dependencies:
          nodejs:
            yarn: "*"
    ```

4. Configure the command to start serving your application (this must be a foreground-running process) under the `web` section:

    ```yaml  {location=".upsun/config.yaml"}
    applications:
      # The app's name, which must be unique within the project.
      myapp:
        type: 'ruby:3.4'
        ...
        web:
          upstream:
            socket_family: unix
          commands:
            # for puma
            start: "bundle exec puma -b unix://$SOCKET"
            # for unicorn
            # start: "bundle exec unicorn -l $SOCKET"
    ```

    This assumes you have Puma as a dependency in your Gemfile:

    ```ruby
    gem "puma", ">= 5.0"
    ```

5. Define the web locations your application is using:

    ```yaml  {location=".upsun/config.yaml"}
    applications:
      # The app's name, which must be unique within the project.
      myapp:
        type: 'ruby:3.4'
        ...
        web:
          locations:
            "/":
              root: "public"
              passthru: true
              expires: 1h
              allow: true
    ```
    This configuration sets the web server to handle HTTP requests at `/static`
    to serve static files stored in `/app/static/` folder.
    Everything else is forwarded to your application server.

6. Create any Read/Write mounts.

    The root file system is read only.
    You must explicitly describe writable mounts.

    ```yaml  {location=".upsun/config.yaml"}
    applications:
      # The app's name, which must be unique within the project.
      myapp:
        type: 'ruby:3.4'
        ...
        mounts:
          "/log":
            source: tmp
            source_path: log
          "/storage":
            source: storage
            source_path: storage
          "/tmp":
            source: tmp
            source_path: tmp
    ```
    This setting allows your application writing temporary files to `/app/tmp`,
    logs stored in `/app/log`, and active storage in `/app/storage`.

    You can define other read/write mounts (your application code itself being deployed to a read-only file system).
    Note that the file system is persistent and when you backup your cluster these mounts are also backed up.

7. Then, setup the routes to your application in `.upsun/config.yaml`.

    ```yaml  {location=".upsun/config.yaml"}
    applications:
      ...

    routes:
      "https://{default}/":
        type: upstream
        upstream: "myapp:http"
    ```
### Complete app configuration

Here is a complete `.upsun/config.yaml` file:

```yaml  {location=".upsun/config.yaml"}
# The name of the app, which must be unique within a project.
applications:
  myapp:
    type: 'ruby:3.4'

    dependencies:
      nodejs:
        yarn: "*"

    relationships:
      mysql:

    variables:
      env:
        BUNDLE_CACHE_ALL: '1' # Default, Cache all gems, including path and git gems.
        BUNDLE_CLEAN: '1' # /!\ if you are working with Ruby<2.7 this doesn't work well, but should be safe on modern Rubies.
        BUNDLE_DEPLOYMENT: '1' # Default, Disallow changes to the Gemfile.
        BUNDLE_ERROR_ON_STDERR: '1' # Default.
        BUNDLE_WITHOUT: 'development:test'
        PIDFILE: "tmp/server.pid" # Allow to start puma directly even if `tmp/pids` directory is not created
        DEFAULT_BUNDLER_VERSION: "2.5.14" # In case none is mentioned in Gemfile.lock
        EXECJS_RUNTIME: 'Node' # If you need one on your assets https://github.com/rails/execjs#readme
        NODE_ENV: 'production'
        NODE_VERSION: v14.17.6
        NVM_VERSION: v0.38.0
        RACK_ENV: 'production'
        RAILS_ENV: 'production'
        RAILS_LOG_TO_STDOUT: '1' # Default
        RAILS_TMP: '/tmp' # Default

    hooks:
      build: |
        set -e

        echo "Installing NVM $NVM_VERSION"
        unset NPM_CONFIG_PREFIX
        export NVM_DIR="$PLATFORM_APP_DIR/.nvm"
        # install.sh will automatically install NodeJS based on the presence of $NODE_VERSION
        curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/$NVM_VERSION/install.sh | bash
        [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

        # we install the bundled bundler version and fallback to a default (in env vars above)
        export BUNDLER_VERSION="$(grep -A 1 "BUNDLED WITH" Gemfile.lock | tail -n 1)" || "$DEFAULT_BUNDLER_VERSION"
        echo "Install bundler $BUNDLER_VERSION"
        gem install --no-document bundler -v $BUNDLER_VERSION

        echo "Installing gems"
        # We copy the bundle directory to the Upsun cache directory for
        # safe keeping, then restore from there on the next build. That allows
        # bundler to skip downloading code it doesn't need to.
        [ -d "$PLATFORM_CACHE_DIR/bundle" ] && \
            rsync -az --delete "$PLATFORM_CACHE_DIR/bundle/" vendor/bundle/
        mkdir -p "$PLATFORM_CACHE_DIR/bundle"
        bundle install
        # synchronize updated cache for next build
        [ -d "vendor/bundle" ] && \
            rsync -az --delete vendor/bundle/ "$PLATFORM_CACHE_DIR/bundle/"

        # precompile assets
        echo "Precompiling assets"
        # We copy the webpacker directory to the Upsun cache directory for
        # safe keeping, then restore from there on the next build. That allows
        # bundler to skip downloading code it doesn't need to.
        # https://guides.rubyonrails.org/asset_pipeline.html
        mkdir -p "$PLATFORM_CACHE_DIR/webpacker"
        mkdir -p "$RAILS_TMP/cache/webpacker"
        [ -d "$PLATFORM_CACHE_DIR/webpacker" ] && \
            rsync -az --delete "$PLATFORM_CACHE_DIR/webpacker/" $RAILS_TMP/cache/webpacker/
        # We dont need secret here https://github.com/rails/rails/issues/32947
        SECRET_KEY_BASE=1 bundle exec rails assets:precompile
        rsync -az --delete $RAILS_TMP/cache/webpacker/ "$PLATFORM_CACHE_DIR/webpacker/"
      deploy: bundle exec rake db:migrate

    mounts:
      "/log":
        source: tmp
        source_path: log
      "/storage":
        source: storage
        source_path: storage
      "/tmp":
        source: tmp
        source_path: tmp

    web:
      upstream:
        socket_family: unix
      commands:
        # for puma
        start: "bundle exec puma -b unix://$SOCKET"
        # for unicorn
        # start: "bundle exec unicorn -l $SOCKET"

      locations:
        "/":
          root: "public"
          passthru: true
          expires: 1h
          allow: true

routes:
  "https://{default}/":
    type: upstream
    upstream: "myapp:http"

services:
  ...
```

## Configuring services

This example assumes there is a MySQL instance.
To configure it, [create a service](https://docs.upsun.com../add-services.md) such as the following:

```yaml  {location=".upsun/config.yaml"}
applications:
  ...

routes:
  ...

services:
  mysql:
    type: mysql:11.8
```
## Connecting to services

Once you have a service, link to it in your [app configuration](https://docs.upsun.com../create-apps/_index.md):

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    type: 'ruby:3.4'
    relationships:
      mysql:
    [...]

routes:
  [...]

services:
  mysql:
    type: mysql:11.8
```
By using the following Ruby function calls, you can obtain the database details.

```ruby
require "base64"
require "json"
relationships= JSON.parse(Base64.decode64(ENV['PLATFORM_RELATIONSHIPS']))
```

This should give you something like the following:

```json
{
  "mysql" : [
    {
      "path" : "main",
      "query" : {
        "is_master" : true
      },
      "port" : 3306,
      "username" : "user",
      "password" : "",
      "host" : "mysql.internal",
      "ip" : "246.0.241.50",
      "scheme" : "mysql"
    }
  ]
}
```

For Rails, you can use the standard Rails `config/database.yml` with the values found with the snippet provided before.

## Other tips

- To speed up boot you can use the [Bootsnap gem](https://github.com/Shopify/bootsnap)
  and configure it with the local `/tmp`:

  ```ruby  {location="config/boot.rb"}
  Bootsnap.setup(cache_dir: "/tmp/cache")
  ```

- For garbage collection tuning, you can read [this article](https://shopify.engineering/17489064-tuning-rubys-global-method-cache)
  and look for [discourse configurations](https://github.com/discourse/discourse_docker/blob/b259c8d38e0f42288fd279c9f9efd3cefbc2c1cb/templates/web.template.yml#L8)
- New images are released on a regular basis to apply security patches. While the minor version will not change (as you are specifying it in the `type` property), the patch version will be updated. You may encounter this kind of error:

  ```
  bundler: failed to load command: puma (/app/vendor/bundle/ruby/3.2.0/bin/puma)
  /app/.global/gems/bundler-2.4.22/lib/bundler/definition.rb:447:in `validate_ruby!': Your Ruby version is 3.2.9, but your Gemfile specified 3.2.8 (Bundler::RubyVersionMismatch)
  ```

  To avoid issues when such updates are performed, use

  ```ruby
  ruby ENV["TARGET_RUBY_VERSION"] || File.read(File.join(File.dirname(__FILE__), ".ruby-version")).strip
  ```

  in your `Gemfile`, where `TARGET_RUBY_VERSION` has been defined as above.

## Troubleshooting

By default, deployments have `BUNDLE_DEPLOYMENT=1` to ensure projects have a `Gemfile.lock` file.
This is safer for version yank issues and other version upgrade breakages.

You may encounter an error like the following during a build:

```txt {no-copy="true"}
W: bundler: failed to load command: rake (/app/.global/bin/rake)
W: /app/.global/gems/bundler-2.3.5/lib/bundler/resolver.rb:268:in `block in verify_gemfile_dependencies_are_found!': Could not find gem 'rails (= 5.2.6)' in locally installed gems. (Bundler::GemNotFound)
```

To resolve this error:

1. Run `bundle install` with the same `ruby` and `bundler` versions defined in your `.upsun/config.yaml` file.
2. Push the `Gemfile.lock` to your repository.

