# Unibeautify Documentation
# Source: https://unibeautify.com/docs/cli

Install [Unibeautify's CLI](https://github.com/Unibeautify/unibeautify-cli):

    
    
    # Locally
    npm install --save-dev unibeautify-cli
    # Or globally
    npm install --global unibeautify-cli
    

And then install your beautifiers along with any prerequisites and
[`peerDependencies`](https://docs.npmjs.com/files/package.json#peerdependencies).

    
    
    # Locally
    npm install --save-dev beautifier-CHANGEME
    # Or globally
    npm install --global beautifier-CHANGEME
    

For example, locally installing [`beautifier-
prettier`](https://yarnpkg.com/en/package/@unibeautify/beautifier-prettier):

    
    
    npm install --save-dev beautifier-prettier
    

And [`prettier`](https://yarnpkg.com/en/package/prettier) is a peer
dependency:

    
    
    npm install --save-dev prettier --exact
    

See [`unibeautify-cli` repository](https://github.com/Unibeautify/unibeautify-
cli) for more information. [Click here for a list of published
beautifiers.](https://classic.yarnpkg.com/en/packages?q=beautifier-&p=1&keywords%5B0%5D=unibeautify)

