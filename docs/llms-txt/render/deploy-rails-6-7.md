# Source: https://render.com/docs/deploy-rails-6-7.md

# Deploy a Rails 6 or 7 App on Render

This guide demonstrates how to set up a local [Ruby on Rails](https://rubyonrails.org/) environment, create an app with a simple view, and deploy that app to Render. It also shows how to connect the app to a Render PostgreSQL [database](postgresql). These same steps work for both Rails 6 and Rails 7.

> *Deploying Rails 8?* See [this quickstart](/deploy-rails-8).

## 1. Create a Rails project

> If you have an _existing_ Rails project that you want to deploy to Render, you can skip to [Update your app for Render](#3-update-your-app-for-render).

First, let's set up a local development environment with a basic project structure.

### Install Rails

Use the `gem install` command to install Rails if you haven't yet. Make sure you have the [required dependencies](https://guides.rubyonrails.org/getting_started.html#creating-a-new-rails-project-installing-rails) installed (Ruby, Node.js and Yarn 1.x).

```shell
gem install rails
```

We're using Rails 7.1 in this tutorial, so verify that you have the correct version installed:

```shell{outputLines:2}
rails --version
Rails 7.1.2
```

### Create a new project

> This tutorial creates a Rails project with the name `mysite`. You can replace this name with another name of your choosing.

1. In your terminal, navigate to the directory where you'll create your project. Then, run the following command to generate a new project that uses Bootstrap for styling:

   ```shell
   rails new mysite --database=postgresql -j esbuild --css bootstrap
   ```

> You can provide additional arguments to customize the generated project. Run `rails new -h` for details.

2. Create local PostgreSQL databases for your app:

   ```shell{outputLines:2-3}
   rails db:create
   Created database 'mysite_development'
   Created database 'mysite_test'
   ```

> If this command fails, make sure you've installed and started PostgreSQL locally, then check your project's `config/database.yml` file. You might need to specify your PostgreSQL username and/or password.

You should now have a functional foundation for your new Rails app! To verify, start your development server:

```shell
bin/dev
```

To see your app in action, go to `localhost:3000` in your browser. You should see the Rails default landing page:

[image: Rails Successful Installation]

Commit all of your project changes and push them to a repository on GitHub/GitLab/Bitbucket. You can deploy your app to Render from any of these.

## 2. Create the Hello World landing page

Next, let's add a simple static view to your app.

> See the official [Getting Started with Rails](https://guides.rubyonrails.org/getting_started.html) guide for more on creating Rails apps.

1. To create a new Rails controller, you run the _controller generator_. Set the controller's name to `Render` and set up an action named `index` by running the following command:

   ```shell
   rails g controller Render index
   ```

   The generator creates several files in your project:

   ```
   create  app/controllers/render_controller.rb
    route  get 'render/index'
   invoke  erb
   create    app/views/render
   create    app/views/render/index.html.erb
   invoke  test_unit
   create    test/controllers/render_controller_test.rb
   invoke  helper
   create    app/helpers/render_helper.rb
   invoke    test_unit
   ```

2. Open the `config/routes.rb` file and add the following line:

   ```ruby
   Rails.application.routes.draw do
      get 'render/index'
      # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

      # Reveal health status on /up that returns 200 if the app boots with no exceptions, otherwise 500.
      # Can be used by load balancers and uptime monitors to verify that the app is live.
      get "up" => "rails/health#show", as: :rails_health_check

      # Defines the root path route ("/")
      root "render#index" # highlight-line
   end
   ```

3. Open the `app/views/render/index.html.erb` file and replace its contents with the following:

   ```erb
   <main class="container">
     <div class="row text-center justify-content-center">
       <div class="col">
         <h1 class="display-4">Hello World!</h1>
       </div>
     </div>
   </main>
   ```

Verify your changes by returning to `localhost:3000` in your browser. If you stopped your local server, restart it first:

```shell
bin/dev
```

[image: Rails Hello World]

## 3. Update your app for Render

Let's prepare your Rails project for production on Render. We'll create a build script for Render to run with each deploy, and we'll update your project to use a [Render PostgreSQL database](postgresql) instead of SQLite (if necessary).

### Create a build script

Render builds your project before each deploy by running a *build command* that you specify. Let's create a script to use for this command.

Create a file named `render-build.sh` in your repo's `bin` directory. Paste the following into it and save:

```bash
#!/usr/bin/env bash
# exit on error
set -o errexit

bundle install
bundle exec rails assets:precompile
bundle exec rails assets:clean

# If you're using a Free instance type, you need to
# perform database migrations in the build command.
# Uncomment the following line:

# bundle exec rails db:migrate
```

Make sure the script is executable before committing it to Git:

```shell
chmod a+x bin/render-build.sh
```

We'll configure Render to call this script each time your app is deployed.

### Swap SQLite for PostgreSQL (if necessary)

> Skip this step if you created your app with the option `--database=postgresql`.

Update your project to use PostgreSQL with the following command:

```shell
rails db:system:change --to=postgresql
```

Alternatively, in your your `Gemfile`, swap the gem for your database driver from `sqlite3` to `pg`.

*Before:*

```ruby
gem 'sqlite3'
```

*After:*

```ruby
gem 'pg'
```

Run `bundle install` to update your `Gemfile.lock`, then commit your changes.

We'll connect to your Render database by setting the `DATABASE_URL` environment variable, so you don't need to make any other changes to your `config/database.yml` file.

Commit all changes and push them to your Git provider. Now your application is ready to be deployed on Render!

## 4. Deploy to Render

There are two ways to deploy your application on Render: by [declaring your services within your repository](infrastructure-as-code) in a `render.yaml` file, or by manually setting up each of your services in the [Render Dashboard](https://dashboard.render.com). The following subsections cover each option.

### Use `render.yaml` to deploy

1. Create a file named `render.yaml` at the root of your directory and paste in the YAML content below. This defines information about your Rails *web service*, along with the [*database*](postgresql) that it connects to:

   ```yaml
   databases:
     - name: mysite
       databaseName: mysite
       user: mysite
       plan: free

   services:
     - type: web
       name: mysite
       runtime: ruby
       plan: free
       buildCommand: './bin/render-build.sh'
       # preDeployCommand: "bundle exec rails db:migrate" # preDeployCommand only available on paid instance types
       startCommand: 'bundle exec rails server'
       envVars:
         - key: DATABASE_URL
           fromDatabase:
             name: mysite
             property: connectionString
         - key: RAILS_MASTER_KEY
           sync: false
         - key: WEB_CONCURRENCY
           value: 2 # sensible default
   ```

   Don't forget to commit and push this change to your remote repository.

> If you don't set `WEB_CONCURRENCY`, Rails determines a value based on the runtime's physical CPU count. This might result in your application running out of memory immediately on boot. We recommend setting this value to `2` as a default, but also optimizing this value for your own application.

2. In the Render Dashboard, go to the [Blueprint](https://dashboard.render.com/blueprints) page and click *New Blueprint Instance*. Select your repository (after giving Render the permission to access it, if you haven't already).

3. In the deploy window, set the value of the `RAILS_MASTER_KEY` to the contents of your `config/master.key` file. Then click *Approve*.

That's it! Your app will be live on your `.onrender.com` URL as soon as the build finishes.

### Deploy manually

If you don't want to deploy your Rails app through a Blueprint, follow these steps from the [Render Dashboard](https://dashboard.render.com) for a manual deploy:

1. Create a new [PostgreSQL database](postgresql) on Render. Note your database *internal database URL*—you'll need it later.

2. Create a new [web service](web-services) and point it to your application repository (make sure Render has a permission to access it).

3. Select Ruby for the web service's runtime and set the following properties:

   | Property                 | Value                    |
   | ------------------------ | ------------------------ |
   | *Build Command*        | `./bin/render-build.sh`  |
   | *Pre-deploy Command\** | `./bin/rails db:migrate` |
   | *Start Command*        | `./bin/rails server`     |

> \*The [pre-deploy command](/deploys#pre-deploy-command) requires a paid instance type. If you're running on the Free instance type, you can include a database migration step in your build command.

4. Set the following environment variables for the web service:

   | Key                | Value                                                            |
   | ------------------ | ---------------------------------------------------------------- |
   | `DATABASE_URL`     | The *internal database URL* for the database you created above |
   | `RAILS_MASTER_KEY` | Paste contents of the `config/master.key` file                   |
   | `WEB_CONCURRENCY`  | 2                                                                |

That's it! You can now finalize your service deployment. It will be live on your `.onrender.com` URL as soon as the initial build and deploy are complete.

## Additional actions

### Accessing the Rails console

> Only paid instance types can use the shell tab and SSH

You can access the Rails console by either using the shell tab in the [Render Dashboard](https://dashboard.render.com), or by connecting to your service using [SSH](ssh) and running `rails c`:

[image: Access Rails Console]

### Adding caching

If you want to speed up your Rails app with a cache, see [Rails caching with Redis](rails-caching-redis).

### Processing tasks in the background

If you want to process asynchronous tasks in the background, see [Deploy Rails with Sidekiq on Render](/deploy-rails-sidekiq).

### Setting a Ruby version

See [Setting your Ruby Version](ruby-version) if you need to customize the version of Ruby used for your app.