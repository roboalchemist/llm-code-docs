# Source: https://render.com/docs/deploy-jekyll.md

# Deploy a Jekyll Static Site

You can deploy a [Jekyll](https://jekyllrb.com/) static site on Render in under a minute. Your site is served over a *lightning-fast global CDN*, comes with *fully managed TLS* certificates, and supports *custom domains* out of the box.

The sample app for this quick start is deployed at https://jekyll.onrender.com.

1. Use your existing Jekyll repository, or fork our sample Jekyll repo on [GitHub](https://github.com/render-examples/jekyll) or [GitLab](https://gitlab.com/render-examples/jekyll).
2. Create a new *Static Site* on Render, and give Render permission to access your new repo.
3. Use the following values during creation:

   |                       |                            |
   | --------------------- | -------------------------- |
   | *Build Command*     | `bundle exec jekyll build` |
   | *Publish Directory* | `_site`                    |

That's it! Your app will be live on your Render URL as soon as the build finishes.

## Additional Notes

See [Specifying a Ruby Version](ruby-version) if you need to customize the version of Ruby used for your app.