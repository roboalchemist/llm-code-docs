# Source: https://developers.make.com/custom-apps-documentation/app-components/modules/action.md

# Action

Action modules are straightforward modules that make one or more requests and return a single bundle as result. Each execution is isolated, so they do not have a state like [polling triggers](https://developers.make.com/custom-apps-documentation/app-components/modules/trigger) and they can't be used to output multiple bundles like [search modules](https://developers.make.com/custom-apps-documentation/app-components/modules/search).\
\
You should use an action module when the API endpoint returns a single item in the response.\
\
Some examples of common action modules include:

* Create an object
* Update a user
* Delete an email
* Get a record (by its ID)
* Download/Upload a file
