# Source: https://accesslint.com/help/github-permissions

[ Help ](/help)

#  What GitHub permissions does AccessLint require? 

AccessLint requires the following GitHub project permissions for installation: 

  * Read access to repository contents
  * Read access to metadata
  * Read and write access to commit statuses
  * Read and write access to issues
  * Read and write access to pull requests

##  Repository Contents (read only) 

AccessLint uses the [ Repository Contents permission ](https://developer.github.com/v3/apps/permissions/#permission-on-contents) to access files in your repository related to a Pull Request. We need to see contents of the change you've made in context of the surrounding code to help us identify accessibility issues. We access _only the files that you change in a Pull Request, and only during the lifecycle of that Pull Request_. 

##  Metadata (read only) 

All GitHub Apps require the [ Repository Metadata permission ](https://developer.github.com/v3/apps/permissions/#metadata-permissions). 

_These permissions are a collection of read only endpoints for accessing metadata for various resources that do not leak sensitive private repository information._

##  Commit Statuses (read & write) 

We use the [ Commit Status permission ](https://developer.github.com/v3/apps/permissions/#permission-on-statuses) to set and update status indicators for your Pull Requests. 

##  Issues (read & write) 

We use the [ Issues permission ](https://developer.github.com/v3/apps/permissions/#permission-on-issues) to create reviews and associated comments on your Pull Requests. 

##  Pull Requests (read & write) 

We use [ Pull Requests permission ](https://developer.github.com/v3/apps/permissions/#permission-on-pull-requests) to listen for new Pull Requests and assess those changes for accessibility issues. 

Visit [ GitHub’s developer documentation ](https://developer.github.com/v3/apps/permissions/) for more details on access these permissions give.