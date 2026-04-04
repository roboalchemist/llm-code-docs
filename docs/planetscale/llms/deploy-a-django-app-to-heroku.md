# Source: https://planetscale.com/docs/vitess/tutorials/deploy-a-django-app-to-heroku.md

# Deploy a Django app to Heroku

## Overview

This article will describe how to deploy a Django app to Heroku, which includes the necessary setup in Heroku’s dashboard.

## Prerequisites

* A PlanetScale database — If you haven't created a database, refer to our [PlanetScale quickstart guide](/docs/vitess/tutorials/planetscale-quick-start-guide) to get started.

* A Heroku account.

* A project deployed to Heroku — If you're just poking around and don't already have an application to deploy, you can use our [Django sample](https://github.com/planetscale/django-example).

## Set up the project for Heroku

There are a few requirements for running a Django application in Heroku:

* The `gunicorn` and `django-heroku` packages as requirements.

* A properly setup [Procfile](https://devcenter.heroku.com/articles/procfile).

* Proper Config Var setup in Heroku.

<Note>
  This article will make use of the [django-example GitHub repository](https://github.com/planetscale/django-example) that is built for the [Connect a Django application to PlanetScale document](/docs/vitess/tutorials/connect-django-app)
</Note>

### Set up the Heroku Config Vars

It’s important to store the connection details for the PlanetScale database in **Config Vars** in Heroku so they are properly secured. These details can be obtained from the PlanetScale dashboard by clicking the "**Connect**" button.

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-a-django-app-to-heroku/database-2.png?fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=0b4894c8e34286d128feb2387541999b" alt="The location of the “Connect” button in the PlanetScale dashboard. priority" data-og-width="1864" width="1864" data-og-height="754" height="754" data-path="docs/images/assets/docs/tutorials/deploy-a-django-app-to-heroku/database-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-a-django-app-to-heroku/database-2.png?w=280&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=8288ad545d227e85740c52d52a4f352e 280w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-a-django-app-to-heroku/database-2.png?w=560&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=aa136d9a40d471ca75795a4166ce2fb6 560w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-a-django-app-to-heroku/database-2.png?w=840&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=33e931b771b359e426bb99813fe5b437 840w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-a-django-app-to-heroku/database-2.png?w=1100&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=c8cf2e0d26aed2085bc75ef050db4bef 1100w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-a-django-app-to-heroku/database-2.png?w=1650&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=1e5002335180ea99a9ede3b4ba42637e 1650w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-a-django-app-to-heroku/database-2.png?w=2500&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=3abafcbc67aaf6a910ce567bc2518e51 2500w" />
</Frame>

In the following modal, choose Django from the “Connect with” dropdown. The .env tab will show all of the Config vars that need to be set up in Heroku. Take note of these and head to the Heroku dashboard.

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-a-django-app-to-heroku/connect-2.png?fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=0e98ff1f01ab2a00cc56bf8c173d6d65" alt="The connection details for the project." data-og-width="1528" width="1528" data-og-height="1124" height="1124" data-path="docs/images/assets/docs/tutorials/deploy-a-django-app-to-heroku/connect-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-a-django-app-to-heroku/connect-2.png?w=280&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=e23af061118e7f8155838190344aad71 280w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-a-django-app-to-heroku/connect-2.png?w=560&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=986efce8184015ee468b4ede8df2aeb2 560w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-a-django-app-to-heroku/connect-2.png?w=840&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=d082bc162d033c1553163f7ab614bb05 840w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-a-django-app-to-heroku/connect-2.png?w=1100&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=e027f602562e061acc4ce51407f2f197 1100w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-a-django-app-to-heroku/connect-2.png?w=1650&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=cbcc3f52cb266802247f442e3a4f3348 1650w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-a-django-app-to-heroku/connect-2.png?w=2500&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=e5953ab88142d64855f855f4054d03eb 2500w" />
</Frame>

Select the **Settings** tab of your Heroku project and then “**Reveal Config Vars”** from the Config **Vars** section. You should see your current Config Vars or an empty set of inputs if there are none configured yet.

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-a-django-app-to-heroku/heroku.png?fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=6a61a50fe442d66e9b44a638ea19a75c" alt="The Settings tab of the Heroku dashboard." data-og-width="1229" width="1229" data-og-height="700" height="700" data-path="docs/images/assets/docs/tutorials/deploy-a-django-app-to-heroku/heroku.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-a-django-app-to-heroku/heroku.png?w=280&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=107b6cbc6f5340c44dfcb3caefdc2631 280w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-a-django-app-to-heroku/heroku.png?w=560&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=b0613154f4c3868940525004c4fc71b8 560w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-a-django-app-to-heroku/heroku.png?w=840&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=14fb3fe8bd6719531c4434c538f13a4a 840w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-a-django-app-to-heroku/heroku.png?w=1100&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=e1478e88a2832f51c2ed9397031754fd 1100w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-a-django-app-to-heroku/heroku.png?w=1650&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=c2456a24b569a41bb2cd72e8514ed56f 1650w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-a-django-app-to-heroku/heroku.png?w=2500&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=fe09bee918d5d45d4ffd7f5b46b62e47 2500w" />
</Frame>

Set up a separate **Config Var** for each line you captured from the PlanetScale dashboard. The one exception is the `MYSQL_ATTR_SSL_CA`, which should be set to `/etc/ssl/certs/ca-certificates.crt`

<Note>
  Heroku uses Ubuntu by default to run applications deployed to their systems, which is why the `MYSQL_ATTR_SSL_CA` value needs to be different than the default values provided by PlanetScale
</Note>

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-a-django-app-to-heroku/ssl.png?fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=3e1816d000f0ee63d5e1316bd191e40e" alt="The Config Vars setup for the project." data-og-width="811" width="811" data-og-height="410" height="410" data-path="docs/images/assets/docs/tutorials/deploy-a-django-app-to-heroku/ssl.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-a-django-app-to-heroku/ssl.png?w=280&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=8b10568b9c80c0b0d10cbb607f9a72ce 280w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-a-django-app-to-heroku/ssl.png?w=560&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=7552c338c9570d2e8a89772934e65bf1 560w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-a-django-app-to-heroku/ssl.png?w=840&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=91e7461b213a1d761cd29e33e51a07fc 840w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-a-django-app-to-heroku/ssl.png?w=1100&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=75301b698ee8e49211caec1696eb1b8a 1100w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-a-django-app-to-heroku/ssl.png?w=1650&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=93b4e6703a6e32147327524f94f0ce01 1650w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-a-django-app-to-heroku/ssl.png?w=2500&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=e5dc04689e8e94a4726337479fbf8d6e 2500w" />
</Frame>

### Update the requirements

Add `gunicorn` and `django-heroku` to your `requirements.txt` file. This will install the necessary packages when deploying to Heroku. If you are following along using the example provided, here is the updated `requirements.txt` file:

```
asgiref==3.4.1
Django==4.0.1
djangorestframework==3.13.1
mysqlclient==2.1.0
python-dotenv==0.19.2
pytz==2021.3
sqlparse==0.4.2
gunicorn
django-heroku
```

### Add a Procfile

The **Procfile** in your project tells Heroku how it should start up the project. The file must be in the root of the project and not in a subdirectory. Here is the **Procfile** used to deploy the **django-example** project to Heroku:

```
web: gunicorn --chdir ./mysite mysite.wsgi --log-file -
```

After these steps have been completed, you may redeploy your application to Heroku. To view a complete example, please refer to the [heroku-deployment branch](https://github.com/planetscale/django-example/tree/heroku-deployment) of the sample repository. This concludes the guide on deploying a Django application to Heroku.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt