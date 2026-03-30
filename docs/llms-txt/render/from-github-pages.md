# Source: https://render.com/docs/from-github-pages.md

# Migrating from GitHub Pages

Migrating from GitHub Pages to Render is a quick and easy process and gives you much more control over your static site builds and deploys.

1. Create a new *Static Site* on Render and select your GitHub Pages repository.
2. Use the following values during creation:
   - *Build Command:* `bundle exec jekyll build`
   - *Publish Directory:* `_site`

That's it! Your site will be live on your Render URL as soon as the build finishes.

Follow our [custom domains](custom-domains) guide to add your own domains to your site.

## A note on Ruby versions

By default, Render uses the latest LTS version of Ruby.

It can also automatically detect and install the version of Ruby specified in `.ruby-version` at the root of your project, or in your Gemfile. At the time of writing, GitHub Pages uses ruby version `2.5.3`; you can check the current dependency version on [GitHub Pages' Dependency versions page](https://pages.github.com/versions/).