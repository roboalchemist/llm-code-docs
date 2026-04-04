# Source: https://content.nuxt.com/raw/docs/deploy/netlify.md

# Netlify

> Deploy your Content app to Netlify

<card>

Quick Setup

- Go go Netlify dashboard and create a new project using git repository.
- Go to `Site Configuration` under `Dependency management` and change Node Version to `20.x` or higher.
- Go to `deploys` and retry last deployment.

</card>

---

Nuxt Content projects can be deployed to Netlify with zero configuration. The module will automatically detects Netlify environment and prepare the necessary configuration for Netlify.

All you need to do is to go to Netlify dashboard and create a new project using git repository.

<note>

By default Netlify uses Node.js 18.x which is not supported by the module. You need to change the Node.js version in `Site Configuration` under `Dependency management`.

</note>

That's it 🎉

Checkout:

- [Nuxt Deploy documentation](https://nuxt.com/deploy/netlify)
- [Netlify documentation](https://www.netlify.com/blog/2016/09/29/a-step-by-step-guide-deploying-on-netlify/)
