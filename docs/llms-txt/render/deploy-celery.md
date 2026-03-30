# Source: https://render.com/docs/deploy-celery.md

# Deploy a Celery Worker

While processing web requests in your application, you might want to offload long-running tasks to an asynchronous background process (often called a worker). Render provides the [background worker](background-workers) service type for this purpose.

This quickstart demonstrates using background workers with the [Celery](https://github.com/celery/celery/) task queue.

## Architecture

Our application's architecture will include the following components:

- A [Flask](https://flask.palletsprojects.com/) *web service* that lets users create new asynchronous tasks for Celery to process
- A [Celery](https://github.com/celery/celery/) *background worker* to process tasks
- A [Render Key Value](key-value) instance to act as the task broker between clients (Flask web service) and workers (Celery background worker)
- A [Flower](https://github.com/mher/flower) *web service* to monitor and administer Celery

## Deploying to Render

We can deploy these services to Render in any of the following ways:

- [Declaring services within your repository](infrastructure-as-code) with a `render.yaml` file
- Manually configuring services in the the [Render Dashboard](https://dashboard.render.com)

Each option is described below.

### Using `render.yaml`

1. Fork our [render-examples/celery](https://github.com/render-examples/celery) example on GitHub.

   This repo defines a `render.yaml` file that sets up the four services.

2. In the Render Dashboard, go your workspace's [Blueprints page](https://dashboard.render.com/blueprints) and click *New Blueprint Instance*.

3. Connect your repository fork.

4. In the deploy window, click *Deploy Blueprint*.

That's it! Your services will be live at their respective `.onrender.com` URLs as soon as the build finishes.
Try out the web services using their Render URLs and play around with the small application.

> Note that Flower's dashboard is not intended for public consumption. We recommend securing it by [adding authentication](https://flower.readthedocs.io/en/latest/auth.html) as described in the Flower docs.

### Deploying manually

1. Create a new Render Key Value instance with the settings below by following the [Key Value documentation](key-value#create-your-key-value-instance). Make a note of the instance's internal URL, which looks like `redis://red-xxxxxxxxxxxxxxxxxxxx:6379`.

   |                      |                                                   |
   | -------------------- | ------------------------------------------------- |
   | *Maxmemory Policy* | `noeviction (recommended for queues/persistence)` |
   | *Plan*             | `Starter`                                         |

   We choose the `noeviction` maxmemory policy to ensure our instance does not delete scheduled tasks upon reaching memory capacity by preventing the creation of new tasks. Choosing `allkeys-lru` instead would allow the creation of new tasks by discarding the oldest potentially incompleted tasks.

   We choose the `Starter` instance type as it is the smallest instance type with persistence, which ensures that we retain tasks when the instance restarts.

2. Fork [render-examples/celery](https://github.com/render-examples/celery) on GitHub and create a new *Background Worker* on Render using your fork.

   |                   |                                                             |
   | ----------------- | ----------------------------------------------------------- |
   | *Language*      | `Python 3`                                                  |
   | *Build Command* | `pip install -r requirements.txt`                           |
   | *Start Command* | `celery --app tasks worker --loglevel info --concurrency 4` |

   Add the following environment variable to the background worker:

   | Key                 | Value                                                     |
   | ------------------- | --------------------------------------------------------- |
   | `CELERY_BROKER_URL` | `<Internal Key Value URL>`, the internal URL from step 1. |

3. Create a new *Web Service* for Flask using the same repo you created in Step 2.

   |                   |                                   |
   | ----------------- | --------------------------------- |
   | *Language*      | `Python 3`                        |
   | *Build Command* | `pip install -r requirements.txt` |
   | *Start Command* | `gunicorn app:app`                |

   Add the following environment variable to the web service:

   | Key                 | Value                                                     |
   | ------------------- | --------------------------------------------------------- |
   | `CELERY_BROKER_URL` | `<Internal Key Value URL>`, the internal URL from step 1. |

4. Once the Flask web service is live, navigate to its URL. Fill out and submit the form to create a new Celery task.

5. Create a new *web service* for Flower using the same repo you created in Step 2.

   |                   |                                             |
   | ----------------- | ------------------------------------------- |
   | *Language*      | `Python 3`                                  |
   | *Build Command* | `pip install -r requirements.txt`           |
   | *Start Command* | `celery flower --app tasks --loglevel info` |

   Add the following environment variable for the web service:

   | Key                 | Value                                                     |
   | ------------------- | --------------------------------------------------------- |
   | `CELERY_BROKER_URL` | `<Internal Key Value URL>`, the internal URL from step 1. |

> Note that Flower's dashboard is not intended for public consumption. We recommend securing it by [adding authentication](https://flower.readthedocs.io/en/latest/auth.html) as described in the Flower docs.

6. Once the Flower web service is live, navigate to its URL and browse the tabs. You can view information such as how many worker processes are running and how many tasks have been completed.

You can also use a Celery background worker from Django. See our [Django quick start](/deploy-django) and the [Django integration guide](https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html) in Celery docs.

See [Specifying a Python Version](python-version) if you need to customize the version of Python used for your app.