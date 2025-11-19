# Source: https://www.aptible.com/docs/how-to-guides/app-guides/integrate-aptible-with-ci/jenkins.md

# Jenkins

Once you've completed the steps for [CI Integration](/how-to-guides/app-guides/integrate-aptible-with-ci/overview), set up Jenkins using these steps:

1. In Jenkins, using the Git plugin, add a new repository to your build:

   1. For the Repository URL, use your App's Git Remote

   2. Upload the private key you created for your robot user as a credential.

   3. Under "Advanced...", name this repository `aptible`.
2. Then, add a post-build "Git Publisher" trigger, to deploy to the `master` branch of your newly-created `aptible` remote.
