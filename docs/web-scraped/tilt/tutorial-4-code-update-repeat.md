# Tilt Documentation
# Source: https://docs.tilt.dev/tutorial/4-code-update-repeat.html
# Path: tutorial/4-code-update-repeat.html

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

#  Code. Update. Repeat.

## Tilt Tutorial

We mentioned that Tilt embraces the concept of a [control loop](./2-tilt-
up.html#the-control-loop), so once youâve run `tilt up`, itâs a âhands
freeâ development experience.

As you edit your code, Tilt will automatically run update steps such as
building an updated container image and deploying it.

> ð¤ **Looking For the Project Code?**
>
> When `tilt demo` started, a path to the temporary directory with the sample
> project was written to the terminal output.

Letâs test it out:

  1. Navigate to the âwebâ resource in the Tilt UI and click âClear Logsâ
  2. Open `web/vite.config.js` in your favorite editor
  3. Find the `logLevel` line and change it from `'error'` to `'info'`
  4. Save the file
  5. Watch magic happen for the `web` resource in the Tilt UI

![Tilt updating a resource after a code change](/assets/docimg/tutorial/tilt-
code-change-full-rebuild.gif)

Whoa, a lot just happened - time to break it down!

## 1\. File Changed

First, Tilt saw a file change and associated it with the âwebâ resource:

    
    
    1 File Changed: [web/vite.config.js] â¢ web
    

Letâs take a peek into the `Tiltfile` to understand:

  * Why Tilt was watching for changes to `web/vite.config.js`
  * How it knew `web/vite.config.js` belonged to the âwebâ resource

For reference, hereâs an abbreviated file hierarchy for [Tilt
Avatars](https://github.com/tilt-dev/tilt-avatars):

    
    
    tilt-avatars/
    âââ api/
    â   âââ ...
    âââ deploy/
    â   âââ web.dockerfile
    â   âââ ...
    âââ web/
    â   âââ vite.config.js
    â   âââ ...
    âââ Tiltfile
    

Ready? Okay. In the Tilt Avatars `Tiltfile`, which is at the repo root, the
container image build for the âwebâ resource looks like this:

    
    
    docker_build(
        'tilt-avatar-web',
        context='.',
        dockerfile='./deploy/web.dockerfile',
        only=['./web/'],
        ignore=['./web/dist/'],
        live_update=[...]  # omitted for brevity
    )
    

> ð Path arguments for Tiltfile functions are relative to your
> `Tiltfile`âs path (refer back to the file hierarchy above if you get
> confused).

Aha! Several of these arguments include paths. Letâs go through them one-by-
one:

  * **`context`: build context for image build** (specified here as the current directory, which is the repo root)

Tilt watches for changes to any modified files in this directory or any
subdirectory, recursively. Perfect! We changed `./web/vite.config.js`, which
meets this criteria.

However, letâs keep looking at the other arguments to make sure they donât
negate or alter this somehowâ¦

  * **`dockerfile` (optional): path for the `Dockerfile` to be used**

This is optional and defaults to `./Dockerfile` to mimic `docker build ...`
CLI behavior. Tilt will watch this path (`./deploy/web.dockerfile` in our
case) and trigger an image re-build if it changes, but itâs not relevant
here because we didnât edit it, so letâs move onâ¦

  * **`only` (optional): filters paths included in build context and restricts file watching to the subset of paths**

Because we have a âmono-repoâ (multiple services in a single repository)
and the build context is the repo root (`.`), we set this to `['web/']` so
that unrelated changes, such as those to the backend (files under `api/`)
donât trigger a re-build of the âwebâ resource. Since
`./web/vite.config.js` _is_ under `./web/`, it hasnât been excluded, which
is what we want!

Just one more argument to goâ¦

  * **`ignore` (optional): excludes certain paths from the build context and ignores changes to them**

Weâve used this to exclude `./web/dist/` for our production web assets,
which otherwise match the rules defined by `context` and `only`. This is
supplementary to `.dockerignore`, but can be helpful for cases where you want
different ignore rules for local dev with Tilt, for example.

As `./web/vite.config.js` is _not_ under `./web/dist/`, it was not ignored,
which is what weâd expect.

If we put all this together, Tilt is watching for any file changes in the
`web/` directory or any of its subdirectories, recursively, EXCEPT for those
in `web/dist` (or any of its subdirectories, recursively). Phew!

When a matching file changes, such as `web/vite.config.js`, because itâs
watched by the `tilt-avatar-web` container image build configuration, Tilt
initiates an update for the âwebâ resource.

> **How does Tilt know the`tilt-avatar-web` image belongs to the âwebâ
> resource?**
>
> You might remember that a resource can be composed of multiple bits of work.
> In the case of the âwebâ resource, it has a container image build and a
> Kubernetes Deployment.
>
> Tilt associated the `tilt-avatar-web` container image with the âwebâ
> resource because the container image name is referenced in Kubernetes YAML
> loaded in the `Tiltfile` with `k8s_yaml`. (This is not the only way that
> container images can be assembled into a resource, and itâs possible to
> manually configure where auto-assembly is insufficient.)

## 2\. Resource Update

Now, the update process starts:

    
    
    STEP 1/3 â Building Dockerfile: [tilt-avatar-web]
      ...
    
    STEP 2/3 â Pushing localhost:44099/tilt-avatar-web:tilt-0b9fcdf9cfea47ba
      ...
    
    STEP 3/3 â Deploying
         Injecting images into Kubernetes YAML
         Applying via kubectl:
         â web:deployment
    

First, Tilt built an updated version of the container image. Then, it pushed
the image to our local registry so that it can be used by Kubernetes. (This
step could look different for you! Tilt adapts its workflow based on your
local cluster setup, which might not require image pushes.) Finally, it
deployed the updated image.

> ð· **Immutable Image Tags**
>
> Tilt tags every image it builds with a unique `:tilt-<hash>` tag. It then
> rewrites the Kubernetes YAML (or Helm chart) on the fly during deployment to
> use this tag.
>
> Why? Using a ârollingâ tag (such as `:latest`) can result in hard-to-
> debug issues depending on factors like image pull policy configuration. With
> an immutable tag, youâre guaranteed _exactly_ what got built is what will
> run.
>
> Itâs just one more thing Tilt takes care of without any extra
> configuration to save you a headache later!

## 3\. Resource Runtime Monitoring

Once deployed, Tilt starts tracking the updated version of the resource:

    
    
    Tracking new pod rollout (web-7f9b8b65f4-wt97k):
         â Scheduled       - <1s
         â Initialized     - <1s
         â Ready           - 1s
    

As Tilt waits for the resource to become ready, itâll pass along relevant
events, such as image pull status or container crashes, so you donât need to
resort to manually investigating a failed deploy with `kubectl`.

Once the container has started, Tilt will stream the logs. In our case, since
we enabled more verbose logging for Vite (the dev server that hosts the
frontend), we should see some messages as it starts up:

    
    
    yarn run v1.22.5
    $ vite
    Pre-bundling dependencies:
      react
      react-dom
    (this will be run only when your dependencies or config have changed)
    
        ...
    
      ready in 946ms.
    

If youâre a bit underwhelmed by changing a log level - you caught us! The
[Tilt Avatars](https://github.com/tilt-dev/tilt-avatars) project is configured
to use Live Update for regular development, so we purposefully made a change
in a config file that meant the full container would be rebuilt.

Letâs move on to the next section where weâll make more interesting code
changes with Live Update.

[ â 3\. Tilt UI ](/tutorial/3-tilt-ui.html) [ 5\. Smart Rebuilds with Live
Update â ](/tutorial/5-live-update.html)

â Back to top  [ Edit on GitHub  ](https://github.com/tilt-
dev/tilt.build/tree/master/docs/4-code-update-repeat.md)







### Was this doc helpful?

Yes No

