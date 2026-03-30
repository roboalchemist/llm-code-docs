# Source: https://docs.salad.com/container-engine/tutorials/deployment/run-a-python-app.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Run a Python App

*Last Updated: October 15, 2024*

The your python application up and running is as simple as packaging up the application into a Docker container. Once
you have the Docker container uploaded to a container registry, you can easily deploy that container on 1-100s of fully
customizable (# CPUs, # RAM, GPU) instances.

In this guide, we will create a simple `Hello World` python application, but these steps can be used to deploy any new
or existing application on Salad.

<iframe src="https://player.vimeo.com/video/918054913?h=00416532b2&title=0&byline=0&portrait=0" width="640" height="360" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen />

# Creating the Python Container

## Requirements

You would normally have the package requirements for your application in some file.

It would depend mainly on the tool you use to install those requirements.

The most common way to do it is to have a file requirements.txt with the package names and their versions, one per line.

You would of course use the same ideas you read in About FastAPI versions to set the ranges of versions.

For example, your requirements.txt could look like:

```Text requirements.txt theme={null}
fastapi>=0.68.0,<0.69.0
pydantic>=1.8.0,<2.0.0
uvicorn>=0.15.0,<0.16.0
```

And you would normally install those package dependencies with pip, for example:

```Text Bash theme={null}
pip install -r requirements.txt
```

## Create the FastAPI Code

* Create a `main.py` file with:

```python  theme={null}
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

```

## Create the Dockerfile

Now in the same project directory create a file `Dockerfile` with:

```dockerfile  theme={null}
# Starts with the official python base image
FROM python:3.9

# Set the current working directory to /code.
# This is where we'll put the requirements.txt file and the app directory.
WORKDIR /app

# Copy the file with the requirements to the /app directory.
# Copy any python files into the /app directory
COPY ./requirements.txt *.py ./

# Install the package dependencies in the requirements file.
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Set the command to run the uvicorn server.
# CMD takes a list of strings, each of these strings is what you would type in the command line separated by spaces.
CMD ["uvicorn", "main:app", "--host", "::", "--port", "80"]

```

You should now have a directory structure like:

```
.
├── main.py
├── Dockerfile
└── requirements.txt

```

## Build the Docker Image

Now that all the files are in place, let's build the container image.

* Go to the project directory (in where your `Dockerfile` is, containing your `app` directory).
* Build your FastAPI image:

```Text Bash theme={null}
docker build -t my-image:latest .
```

## Test the Container Locally

### Run the Docker Container

Run a container based on your image on your local machine:

```Text Bash theme={null}
docker run -d --name my-container -p 80:80 my-image:latest
```

### Check the API

You should be able to check it in your Docker container's URL, for example:

* http\://localhost:80/
* http\://localhost/items/2

You will see something like:

```json  theme={null}
{ "item_id": 5, "q": "some-query" }
```

# Push Container to a Registry

Now that you have a container locally, you will need to push that container image up to a container registry so it can
be deployed on SaladCloud. You can push to any of the
[supported container registries](/container-engine/explanation/infrastructure-platform/container-registries), but for
this guide we will use Docker Hub.

## Tagging the Image

In order to push the container image to Docker Hub you will first need to tag your image with your Docker username and
an unique container name. The format of the image name is `{docker-hub-username}/{image-name}:{version}`

At SaladCloud we use the `saladtechnologies` username, but you will need to use your own username.

```Text Bash theme={null}
docker tag my-image saladtechnologies/run-python:0.1
```

## Pushing the Image

Now that your container has the proper naming convention, you can push the container to Docker Hub by running the `push`
command.

```Text Bash theme={null}
docker push saladtechnologies/run-python:0.1
```

Once the image is pushed to Docker Hub you can now deploy your container on Salad!

# Deploy Container to Salad

## Creating the Container Group

Now that you have a complete (yet basic) FastAPI application running you can deploy it to SaladCloud via the Portal or
the Public API.

When you are asked to specify the "Image Source" you simply need to provide the image name you used to push the
container up to the registry.

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/5047308-image.png?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=bb342ce9c3dab307dc08c06494378d3d" data-og-width="1362" width="1362" data-og-height="552" height="552" data-path="container-engine/images/5047308-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/5047308-image.png?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=7ec8fbea8a07da62ec75f0510ab0b147 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/5047308-image.png?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=1fb71855f20838e68cda966bf9405c76 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/5047308-image.png?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=25f64f5e464af9e05ffce27be27d84bd 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/5047308-image.png?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=f7552648828c8dc2944ee96060e61e5b 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/5047308-image.png?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=efa9a08f3c5d92d32c4d7ddb583903c2 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/5047308-image.png?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=6ef672d782853725aadede2c8a7ddb58 2500w" />

Since the FastAPI is listening to port 80, you will need to enable the Container Gateway and configure the port when
creating a new container group.

[Deployment Guide](/container-engine/explanation/container-groups/container-groups)

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/0d2e830-image.png?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=26e5fc3e2f5e806d14e0ba88ef68ab02" data-og-width="514" width="514" data-og-height="479" height="479" data-path="container-engine/images/0d2e830-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/0d2e830-image.png?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=cd6c12d19509ed456545d283f7595f5a 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/0d2e830-image.png?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=93cef2068882b1701dbf5a661e47c5a5 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/0d2e830-image.png?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=1fb25a8ffb80620ae34d3e9efc0ac5a4 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/0d2e830-image.png?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=c47e9c03e64a2f044c949818bf2a68b5 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/0d2e830-image.png?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=52ed73435e88a831b95ef491cac4d0fe 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/0d2e830-image.png?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=677c8cef412cb734ffb8b8ce3d02abb8 2500w" />

## Connecting to the Application

Once the container group is up and running, you will be given a static URL that load balances all http requests across
the instances of your applications. If you enabled authentication then you will need to include your API key in the
`'Salad-Api-Key` header of your http requests.

Example Request

```
GET https://caesar-lime-465054.salad.cloud/items/2
```

Congrats! You have successfully created, containerized, deployed and connected to your first application on Salad!
