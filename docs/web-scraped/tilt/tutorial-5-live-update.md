# Tilt Documentation
# Source: https://docs.tilt.dev/tutorial/5-live-update.html
# Path: tutorial/5-live-update.html

  * [ Getting Started ](/index.html) [ Getting Started ](/docs_nav_gettingstarted.html)
  * [ Guides ](/tiltfile_authoring.html) [ Guides ](/docs_nav_guides.html)
  * [ Tiltfile & CLI ](/api.html) [ Tiltfile & CLI ](/docs_nav_reference.html)
  * [ Tilt API ](https://api.tilt.dev) [ Tilt API ](https://api.tilt.dev)

Learn About Tilt

    

  * [ Getting Started ](/)
  * [ Is Tilt right for me? ](/product_faq.html)

First Look at Tilt

    

  * [ Overview ](/tutorial/index.html)
  * [ 1\. Preparation (optional) ](/tutorial/1-prerequisites.html)
  * [ 2\. Launching & Managing Resources ](/tutorial/2-tilt-up.html)
  * [ 3\. Tilt UI ](/tutorial/3-tilt-ui.html)
  * [ 4\. Code. Update. Repeat. ](/tutorial/4-code-update-repeat.html)
  * [ 5\. Smart Rebuilds with Live Update ](/tutorial/5-live-update.html)

Quick Links

    

  * [ Install ](/install.html)
  * [ Upgrade ](/upgrade.html)
  * [ Tiltfile Snippets ](/snippets.html)
  * [ Editor Support new ](/editor.html)

How Does Tilt Work?

    

  * [ The Control Loop ](/controlloop.html)
  * [ Choosing a Local Dev Cluster ](/choosing_clusters.html)
  * [ Local vs Remote Services ](/local_vs_remote.html)

FAQs

    

  * [ Frequently Asked Questions ](/faq.html)
  * [ Why is Tilt broken? ](/debug_faq.html)
  * [ What does Tilt send? ](/telemetry_faq.html)

#  Smart Rebuilds with Live Update

## Tilt Tutorial

Tiltâs deep understanding of your resources means the right things get
rebuilt at the right times.

Even with Docker layer caching, rebuilding a container image can be slow. For
unoptimized Kubernetes-based development, every code change requires:

  1. Rebuilding the container image (`docker build ...`)
  2. Pushing the built image to a registry (`docker push ...`)
  3. Updating the tag in YAML and applying the Deployment to the cluster (`kubectl apply -f ...`)
  4. Waiting for the roll out of new Pods using the updated image (open Reddit, ð´, etc.)

Live Update solves these challenges by performing an **in-place update of the
containers in your cluster**.

It works with frameworks that natively support hot reload (e.g. Webpack), as
well as compiled languages.

Time to try it out:

  1. Open `api/app.py` in your favorite editor
  2. Find the commented out line `# 'other': ['accessory']`
  3. Uncomment it (remove the leading `#`)
  4. Save the file
  5. Watch magic happen for the `api` resource in the Tilt UI
  6. Open the Tilt Avatars web app <http://localhost:5735/>
  7. Dress the character with some stylish glasses (this is important!!! ð)

![Tilt Live Updating a container after a code
change](/assets/docimg/tutorial/tilt-code-change-live-update.gif)

To understand what happened, letâs take a look at the `docker_build`
configuration for the `tilt-avatar-api` image:

    
    
    docker_build(
        'tilt-avatar-api',
        context='.',
        dockerfile='./deploy/api.dockerfile',
        only=['./api/'],
        live_update=[
            sync('./api/', '/app/api/'),
            run(
                'pip install -r /app/requirements.txt',
                trigger=['./api/requirements.txt']
            )
        ]
    )
    

It looks a lot like the `tilt-avatar-web` image configuration we saw in the
last section.

Whatâs not omitted this time is the `live_update` argument value, which
defines a series of steps to run (in-order) to Live Update a container.

## `sync()` Steps

We have a single sync step defined:

    
    
    sync('./api/', '/app/api/')
    

The first argument (`./api/`) is the path, relative to the `Tiltfile`, on our
machine that we want Tilt to watch for changes to (recursively). The
destination path (`/app/api/`) is the absolute path _inside the container_
where we want the files copied to.

> ðââï¸ Files you sync to the container _must_ match paths that Tilt
> is already watching for the image configuration

In practice, that results in what we saw in the âapiâ logs in Tilt:

    
    
    Will copy 1 file(s) to container: 4a9aac5527
    - '/Users/quixote/dev/tilt-avatars/api/app.py' --> '/app/api/app.py'
      â Container 4a9aac5527 updated!
    

Since Flask (Python web framework) provides a dev server with hot module
support, copying the file is all that was needed! Live Update also supports
situations where the framework does not support reloading code at runtime by
restarting your process with an updated version of the code in the container,
which saves the overhead of image build and deployment. For details, refer to
the full [Live Update Reference](/live_update_reference.html#restarting-your-
process).

## `run()` Steps

When modifying non-code files, itâs sometimes necessary to run additional
command(s) to process them.

For example, our project has a run step to install new or updated Python
dependencies using pip (Python package manager):

    
    
    run(
        'pip install -r /app/requirements.txt',
        trigger=['./api/requirements.txt']
    )
    

The first argument is a command to run _inside the container_. The `trigger`
argument defines a path, relative to the `Tiltfile`, on our machine that, when
changed, will result in the command being run in the container.

Now, when we change our projectâs dependencies in `./api/requirements.txt`,
the updated version of the file will first be synced to the container. Then,
because it matches the run stepâs `trigger` condition, the command will be
run in the container to install new/updated dependencies.

Go ahead and try it out by making a change to `./api/requirements.txt`. (Hint:
lines beginning with `#` will be ignored, so add a new line like `# hello from
Tilt tutorial!` and save the file.) Youâll see that not only is the file
copied as before when we modified `./api/app.py`, but that this time, the run
step executes as well:

    
    
    Will copy 1 file(s) to container: 4a9aac5527
    - '/Users/quixote/dev/tilt-avatars/api/requirements.txt' --> '/app/api/requirements.txt'
    [CMD 1/1] sh -c pip install -r /app/requirements.txt
       ...
      â Container 4a9aac5527 updated!
    

## But Waitâ¦Thereâs More

We think Live Update is part of what makes Tilt truly special. Its flexibility
makes it possible to use with both interpreted and compiled languages,
regardless of whether the framework supports hot module reload.

This tutorial has only scratched the surface of whatâs possible, and we know
it can be daunting, but youâve got this. Now that youâre familiar with how
Tilt works and have seen some `Tiltfile` snippets, youâre ready to follow
the [Write a Tiltfile Guide](/tiltfile_authoring.html) and start using Tilt in
your _own_ project!

Weâre also always excited to hear about how you are using Tilt or provide a
helping hand, so do [be in touch](/contact) â¤ï¸

[ â 4\. Code. Update. Repeat. ](/tutorial/4-code-update-repeat.html)

â Back to top  [ Edit on GitHub  ](https://github.com/tilt-
dev/tilt.build/tree/master/docs/5-live-update.md)







### Was this doc helpful?

Yes No

