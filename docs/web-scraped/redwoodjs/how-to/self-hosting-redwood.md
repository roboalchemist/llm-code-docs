# Source: https://docs.redwoodjs.com/docs/how-to/self-hosting-redwood

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [How To](/docs/how-to/index)
-   [Self-hosting Redwood (Serverful)]

[Version: 8.8]

On this page

<div>

# Self-hosting Redwood (Serverful)

</div>

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]warning

This doc has been deprecated in favor of the [Baremetal](/docs/deploy/baremetal) docs.

Do you prefer hosting Redwood on your own server, the traditional serverful way, instead of all this serverless magic? Well, you can! In this recipe we configure a Redwood app with PM2 and Nginx on a Linux server.

> A code example can be found at [https://github.com/njjkgeerts/redwood-pm2](https://github.com/njjkgeerts/redwood-pm2), and can be viewed live at [http://redwood-pm2.nickgeerts.com](http://redwood-pm2.nickgeerts.com).

## Requirements[​](#requirements "Direct link to Requirements") 

You should have some basic knowledge of the following tools:

-   [PM2](https://pm2.keymetrics.io/docs/usage/pm2-doc-single-page/)
-   [Nginx](https://nginx.org/en/docs/)
-   Linux
-   [Postgres](https://www.postgresql.org/docs/)

## Configuration[​](#configuration "Direct link to Configuration") 

To self-host, you\'ll have to do a bit of configuration both to your Redwood app and your Linux server.

### Adding Dependencies[​](#adding-dependencies "Direct link to Adding Dependencies") 

First add PM2 as a dev dependency to your project root:

``` 
yarn add -D pm2
```

Then create a PM2 ecosystem configuration file. For clarity, it\'s recommended to rename `ecosystem.config.js` to something like `pm2.config.js`:

``` 
yarn pm2 init
mv ecosystem.config.js pm2.config.js
```

Last but not least, change the API endpoint in `redwood.toml`:

``` 
- apiUrl = "/.redwood/functions"
+ apiUrl = "/api"
```

Optionally, add some scripts to your top-level `package.json`:

``` 
"scripts": 
```

We\'ll refer to these later, so even if you don\'t add them to your project, keep them in mind.

### Linux server[​](#linux-server "Direct link to Linux server") 

Your Linux server should have a user for deployment, configured with an SSH key providing access to your production environment. In this example, the user is named `deploy`.

### Nginx[​](#nginx "Direct link to Nginx") 

Typically, you keep your Nginx configuration file at `/etc/nginx/sites-available/redwood-pm2` and symlink it to `/etc/nginx/sites-enabled/redwood-pm2`. It should look something like this:

``` 
server 

  location /api/ 
}
```

Please note that the trailing slash in `proxy_pass` is essential to correctly map the API functions.

### PM2[​](#pm2 "Direct link to PM2") 

Let\'s configure PM2 with the `pm2.config.js` file we made earlier. The most important variables are at the top. Note that the port is only used locally on the server and should match the port in the Nginx config:

``` 
const name = 'redwood-pm2' // Name to use in PM2
const repo = 'git@github.com:njjkgeerts/redwood-pm2.git' // Link to your repo
const user = 'deploy' // Server user
const path = `/home/$/$` // Path on the server to deploy to
const host = 'example.com' // Server hostname
const port = 8911 // Port to use locally on the server
const build = `yarn install && yarn rw build && yarn rw prisma migrate deploy`

module.exports = /current/`,
      script: 'yarn rw serve api',
      args: `--port $`,
      env: ,
      env_production: ,
    },
  ],

  deploy:  && pm2 reload pm2.config.js --env production && pm2 save`,
    },
  },
}
```

If you need to seed your production database during your first deployment, `yarn redwood prisma migrate dev` will do that for you.

> **Caveat:** the API seems to only work in fork mode in PM2, not [cluster mode](https://pm2.keymetrics.io/docs/usage/cluster-mode/).

## Deploying[​](#deploying "Direct link to Deploying") 

First, we need to create the PM2 directories:

``` 
yarn install
yarn deploy:setup
```

Your server directories are now set, but we haven\'t configured the `.env` settings yet. SSH into your server and create an `.env` file in the `current` subdirectory of the deploy directory:

``` 
vim /home/deploy/redwood-pm2/current/.env
```

For example, add a `DATABASE_URL` variable:

``` 
DATABASE_URL=postgres://postgres:postgres@localhost:5432/redwood-pm2
```

Now we can deploy the app! Just run the following; it should update the code, take care of database migrations, and restart the app in PM2:

``` 
yarn deploy
```

Enjoy! 😁

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/how-to/self-hosting-redwood.md)