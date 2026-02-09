# Source: https://www.aptible.com/docs/how-to-guides/app-guides/make-docker-deploys-faster.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to make Dockerfile Deploys faster

Make [Dockerfile Deploy](/how-to-guides/app-guides/deploy-from-git) faster by structuring your Dockerfile to maximize efficiency by leveraging the Docker build cache:

## Gems installed via Bundler

In order for the Docker build cache to cache gems installed via Bundler:

1. Add the Gemfile and Gemfile.lock files to the image.

2. Run `bundle install`, *before* adding the rest of the repo (via `ADD .`).

Here's an example of how that might look in a Dockerfile:

```ruby  theme={null}
FROM ruby

# If needed, install system dependencies here

# Add Gemfile and Gemfile.lock first for caching
ADD Gemfile /app/
ADD Gemfile.lock /app/
WORKDIR /app
RUN bundle install

ADD . /app

# If needed, add additional RUN commands here
```

## Packages installed via NPM

In order for the Docker build cache to cache packages installed via npm:

1. Add the `package.json` file to the image.

2. Run `npm install`, *before* adding the rest of the repo (via `ADD .`).

Here's an example of how that might look in a Dockerfile:

```node  theme={null}
FROM node

# If needed, install system dependencies here

# Add package.json before rest of repo for caching
ADD package.json /app/
WORKDIR /app
RUN npm install

ADD . /app

# If needed, add additional RUN commands here
```

## Packages installed via PIP

In order for the Docker build cache to cache packages installed via pip:

1. Add the `requirements.txt` file to the image.

2. Run `pip install`, *before* adding the rest of the repo (via `ADD .`).

Here's an example of how that might look in a Dockerfile:

```python  theme={null}
FROM python

# If needed, install system dependencies here

# Add requirements.txt before rest of repo for caching
ADD requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

ADD . /app
```
