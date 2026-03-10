# Source: https://render.com/docs/deploy-rails-8.md

# Deploy a Rails 8 App on Render — Run Rails 8 on Render's native Ruby runtime.

Welcome! This guide walks you through creating a Rails 8 app and deploying it on Render. The app will use a Render Postgres database as its backing datastore.

> *Deploying an earlier version of Rails?* See [this quickstart](/deploy-rails-6-7).
>
> *Have an existing Rails 8 app you want to deploy?* Skip straight to [Update your app for Render](#2-update-your-app-for-render).

## 1. Create a Rails project

First, let's set up your local development environment and initialize a new Rails project.

### Install Rails

1. If you haven't yet, complete the steps in the official [Rails installation guide](https://guides.rubyonrails.org/install_ruby_on_rails.html) to install both Ruby and Rails on your development machine.

2. After you complete the final installation step (`gem install rails`), run the following in your terminal to verify that Rails installed successfully and that you installed the version you expect:

   ```shell{outputLines:2}
   rails --version
   Rails 8.0.2
   ```

### Create a new project

In this step, we'll create a Rails project with the name `mysite`. You can use a different name if you prefer.

1. In your terminal, navigate to the directory where you'll create your project (such as `~/Development`).

2. Run the following command to generate a new project:

   ```shell
   rails new mysite --skip-solid --database=postgresql --js=esbuild --css=tailwind
   ```

> The *`--skip-solid`* option instructs Rails to _omit_ automatic configuration for the new [Solid Cache](https://github.com/rails/solid_cache), [Solid Queue](https://github.com/rails/solid_queue), and [Solid Cable](https://github.com/rails/solid_cable) features in Rails 8.
>
>    To simplify your initial deployment, we recommend that you configure these features individually as needed after you're up and running on Render.

3. From your new project's root directory, create local PostgreSQL databases for your app:

   ```shell{outputLines:2-3}
   rails db:create
   Created database 'mysite_development'
   Created database 'mysite_test'
   ```

*Database creation failed?*

Make sure you've [installed and started PostgreSQL locally](https://www.postgresql.org/download/), then check your project's `config/database.yml` file. You probably need to provide values for your local PostgreSQL database's `username` and/or `password`:

   ```yaml
   development:
     <<: *default
     database: mysite_development
     username: postgres
     password: abc123

     # To provide a secure password via environment variable,
     # uncomment and use this format in place of the hardcoded
     # value above.
     #
     # password: <%= ENV["DATABASE_PASSWORD"] %>
   ```

Your Rails app is ready to run locally. To verify, start your development server:

```shell
bin/dev
```

To see your app in action, visit `localhost:3000` in your browser. You should see the default Rails landing page:

[image: The default Rails app landing page]

Commit all of your project changes and push them to a new repository on GitHub/GitLab/Bitbucket. You can deploy your app to Render from any of these.

### Add a basic homepage

Next, let's add a simple static homepage to your app.

1. In your project directory, create a new controller with the `rails generate controller` command:

   ```shell
   rails generate controller Homepage index
   ```

   This sets the controller's name to `Homepage` and sets up an action named `index`.

   The generator creates several files in your project:

   ```
   create  app/controllers/homepage_controller.rb
     route  get "homepage/index"
   invoke  erb
   create    app/views/homepage
   create    app/views/homepage/index.html.erb
   invoke  test_unit
   create    test/controllers/homepage_controller_test.rb
   invoke  helper
   create    app/helpers/homepage_helper.rb
   invoke    test_unit
   ```

2. Open the file `config/routes.rb` and add the highlighted line below:

   ```ruby
   Rails.application.routes.draw do
     get "homepage/index"
     # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

     # Reveal health status on /up that returns 200 if the app boots with no exceptions, otherwise 500.
     # Can be used by load balancers and uptime monitors to verify that the app is live.
     get "up" => "rails/health#show", as: :rails_health_check

     # Defines the root path route ("/")
     root "homepage#index" # highlight-line
   end
   ```

3. Open the file `app/views/homepage/index.html.erb` and *replace* its contents with the following:

   ```erb
   <main class="max-w-6xl mx-auto px-4">
     <div class="flex justify-center text-center">
       <h1 class="text-4xl font-bold mt-20">Hello World!</h1>
     </div>
   </main>
   ```

4. Verify your changes by returning to `localhost:3000` in your browser. If you stopped your local server, restart it first:

   ```shell
   bin/dev
   ```

   Your site's root path now displays the following:

   [image: Rails Hello World]

5. Commit your changes and push them to your Git provider.

Now that we have a basic Rails app, let's prepare it for production on Render.

## 2. Update your app for Render

Before we deploy your app, let's get it Render-ready. To achieve this, we will:

1. [Create a build script](#create-a-build-script) for Render to run with each deploy
2. [Swap SQLite for Postgres](#swap-sqlite-for-postgres) as your app's database (if you haven't already)

### Create a build script

Render builds your app before each deploy by running a *build command* that you specify. Rails apps usually run _multiple_ commands as part of a build, so let's create a script that combines them.

1. Create a file named `render-build.sh` in your repo's `bin` directory. Paste the following into it and save:

   ```bash
   #!/usr/bin/env bash

   # Exit on error
   set -o errexit

   bundle install
   bin/rails assets:precompile
   bin/rails assets:clean

   # If you have a paid instance type, we recommend moving
   # database migrations like this one from the build command
   # to the pre-deploy command:
   bin/rails db:migrate
   ```

   If your project performs additional build tasks, add them to this script as well.

2. Make sure the script is executable:

   ```shell
   chmod a+x bin/render-build.sh
   ```

3. Commit and push your changes to your Git provider.

We'll configure Render to execute this script each time your app is deployed.

### Swap SQLite for Postgres

> *Skip this step if your app is already configured to use Postgres.*
>
> For example, if you set up a basic starter app in [Create a Rails project](#1-create-a-rails-project) above, you're all set.

*Production Rails apps on Render should _not_ use SQLite.* Instead, they should connect to a separately hosted database, such as [Render Postgres](postgresql).

*Why not use SQLite?*

*Most importantly, because Render services have an [*ephemeral filesystem*](/deploys#ephemeral-filesystem).* This means that changes to local files (including SQLite databases) are lost after each deploy. You _can_ attach a [persistent disk](disks) to preserve local files, but this disables [zero-downtime deploys](/deploys#zero-downtime-deploys).

Additionally, you can't safely [scale your app](scaling) to multiple instances if it uses SQLite. Each instance uses its own local database, resulting in immediate data fragmentation.

A Render Postgres database provides a persistent, shared store that multiple apps and instances can use.

1. Update your project to use PostgreSQL with the following command:

   ```shell
   rails db:system:change --to=postgresql
   ```

   Alternatively, in your your `Gemfile`, swap the gem for your database driver from `sqlite3` to `pg`.

   Before:

   ```ruby
   gem 'sqlite3'
   ```

   After:

   ```ruby
   gem 'pg'
   ```

2. Run `bundle install` to update your `Gemfile.lock`, then commit and push your changes.

We’ll connect to your Render database by setting the `DATABASE_URL` environment variable, so you don’t need to make any other changes to your `config/database.yml` file.

Your app is now ready to deploy on Render.

## 3. Deploy on Render

To deploy your app on Render, we'll create two services:

[diagram]

- A [web service](web-services) that runs your Rails executable and receives incoming requests
- A [Render Postgres database](postgresql) that stores your app's data

Render provides a free instance type for each of these to help you get started.

### Create your Render services

You can create these services in either of the following ways:

- Create each service separately in the [Render Dashboard](https://dashboard.render.com)
  - Choose this if you prefer to configure your services in a web interface.
- Define both services in a `render.yaml` file and deploy them together using [Render Blueprints](infrastructure-as-code)
  - Choose this if you prefer to configure your services in your IDE.

*Use the tabs below to view instructions for each method:*

**Dashboard**

#### Creating services in the Render Dashboard

You'll complete all of these steps in the [Render Dashboard](https://dashboard.render.com):

1. Create a new Render Postgres database by following [these steps](postgresql-creating-connecting#create-your-database).

   - Feel free to start with the Free instance type. You can upgrade later.

2. After you deploy your database, note the following values:

   - The database's *region*
   - The database's *internal database URL*

3. Still in the Render Dashboard, click *+ New > Web Service*.

4. Connect your Git provider to Render if you haven't already.

5. Choose your Rails project's repo from the list.

6. Configure the rest of your web service's settings according to the table below:

| Property | Value |
| --- | --- |
| *Language* | Ruby |
| *Region* | Select the same region as your database. |
| *Build Command* | `bin/render-build.sh` |
| *Pre-deploy Command* | `bin/rails db:migrate` *The [*pre-deploy command*](/deploys#pre-deploy-command) requires a paid instance type.* If you're starting on the Free instance type, you can keep database migration logic in your [build script](#create-a-build-script). |
| *Start Command* | `bin/rails server` |
| *Environment Variables* | See the next step. |

7. Set the following environment variables for the web service:

| Key | Value |
| --- | --- |
| `DATABASE_URL` | The *internal database URL* for the database you created above |
| `RAILS_MASTER_KEY` | Paste the contents of your app's `config/master.key` file. |
| `WEB_CONCURRENCY` | `2` (If you don't set this value, Rails determines a value based on the runtime's physical CPU count. This might result in your application running out of memory. We recommend setting this value to `2` as a default, but also optimizing this value for your own application.) |

8. Click *Deploy Web Service*.

That's it! Your app will be live at its unique `.onrender.com` URL as soon as the initial build and deploy are complete.

**Blueprint (render.yaml)**

#### Creating services with a Blueprint

1. Create a file named `render.yaml` in your project's root directory and paste in the YAML content below:

   ```yaml
   services:
     - type: web
       name: mysite
       runtime: ruby
       plan: free
       buildCommand: './bin/render-build.sh'
       # preDeployCommand: "bundle exec rails db:migrate" # preDeployCommand only available on paid instance types
       startCommand: './bin/rails server'
       envVars:
         - key: DATABASE_URL
           fromDatabase:
             name: mysite-db
             property: connectionString
         - key: RAILS_MASTER_KEY
           sync: false # You'll provide this value on Blueprint creation
         - key: WEB_CONCURRENCY
           value: 2 # Recommended default
   databases:
     - name: mysite-db
       plan: free
   ```

   This file defines configuration for your Rails web service, along with the [Render Postgres database](postgresql) that it connects to.

   Don't forget to commit and push this change to your remote repository.

> If you don't set `WEB_CONCURRENCY`, Rails determines a value based on the runtime's physical CPU count. This might result in your application running out of memory immediately on boot. We recommend setting this value to `2` as a default, but also optimizing this value for your own application.

2. In the Render Dashboard, go to the [Blueprint](https://dashboard.render.com/blueprints) page and click *New Blueprint Instance*. Select your repository (after giving Render the permission to access it, if you haven't already).

3. In the deploy window, set the value of the `RAILS_MASTER_KEY` to the contents of your `config/master.key` file. Then click *Approve*.

That's it! Your app will be live on your `.onrender.com` URL as soon as the build finishes.

## Next steps

After your app is up and running, explore common architecture patterns and configuration options:

### Access the Rails console

> Only paid instance types support shell connections to your service.

You can access the Rails console in either of the following ways:

- Open your service's Shell page in the [Render Dashboard](https://dashboard.render.com) and run `rails c`:

  [image: Access Rails Console]

- Connect to your service using [SSH](ssh) and run `rails c`.

### Add caching

To speed up your Rails app with a cache, you have multiple options:

- Set up [Rails caching with Render Key Value](rails-caching-redis).
- Configure the Rails 8 [Solid Cache](https://github.com/rails/solid_cache?tab=readme-ov-file#solid-cache) to cache with your Render Postgres database.

### Process background tasks

Render [background workers](background-workers) are ideal for processing asynchronous tasks from a queue.

To set up your job queue, you have multiple options:

- Set up [Sidekiq](/deploy-rails-sidekiq) to process jobs with a Render Key Value cache.
- Configure the Rails 8 [Solid Queue](https://github.com/rails/solid_queue?tab=readme-ov-file#solid-queue) to process jobs with your Render Postgres database.

### Set a Ruby version

See [Setting your Ruby Version](ruby-version) to customize the version of Ruby used for your app.