# Source: https://docs.kubearmor.io/kubearmor/contribution/contribution_guide.md

# Contribution Guide

KubeArmor maintainers welcome individuals and organizations from across the cloud security landscape (creators and implementers alike) to make contributions to the project. We equally value the addition of technical contributions and enhancements of documentation that helps us grow the community and strengthen the value of KubeArmor. We invite members of the community to contribute to the project!

To make a contribution, please follow the steps below.

1. Fork this repository (KubeArmor)

   First, fork this repository by clicking on the Fork button (top right).

   ![fork button](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-31ace0e1ca9700fcd558c5dde76a069beb593d66%2Ffork_button.png?alt=media)

   Then, click your ID on the pop-up screen.

   ![fork screen](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-03b203bcc453969a1ac366ad67b15405739b2316%2Ffork_screen.png?alt=media)

   This will create a copy of KubeArmor in your account.

   ![fork repo](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-9db3c66b4f008c794300b55376e8163825aa140c%2Fforked_repo.png?alt=media)
2. Clone the repository

   Now clone Kubearmor locally into your dev environment.

   ```
    git clone https://github.com/[your GitHub ID]/KubeArmor
   ```

   This will clone a copy of Kubearmor installed in your dev environment.
3. Make changes

   First, go into the repository directory and make some changes.

   Please refer to [development guide](https://docs.kubearmor.io/kubearmor/contribution/development_guide) to set up your environment for KubeArmor contribution.
4. Check the changes

   If you have changed the core code of KubeArmor then please run tests before committing the changes

   ```
   cd tests
   ~/KubeArmor/tests$ make
   ```

   If you see any warnings or errors, please fix them first.

   If some tests are failing, then fix them by following [Testing Guide](https://docs.kubearmor.io/kubearmor/contribution/testing_guide)

   If you have made changes in Operator or Controller, then follow [this](https://github.com/kubearmor/KubeArmor/blob/main/contribution/testing_operator_controller_guide.md)
5. Commit changes

   Please see your changes using "git status" and add them to the branch using "git add".

   ```
    $ cd KubeArmor
    ~/KubeArmor$ git status
    ~/KubeArmor$ git add [changed file]
   ```

   Then, commit the changes using the "git commit" command.

   ```
    ~/KubeArmor$ git commit -s -m "Add a new feature by [your name]"
   ```

   Please make sure that your changes are properly tested on your machine.
6. Push changes to your forked repository

   Push your changes using the "git push" command.

   ```
    ~/KubeArmor$ git push
   ```

7. Create a pull request with your changes with the following steps

   First, go to your repository on GitHub.

   ![commit ahead](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-c4388730105d037655e5a51e66e2d31e0a43cb74%2Fcommit_ahead.png?alt=media)

   Then, click "Pull request" button.

   ![after pull request](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-5204f70a9714d1fbbb6a217c6d79b5756fef7f4a%2Fafter_pull_request.png?alt=media)

   After checking your changes, click 'Create pull request'.

   ![open pull request](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-25b346f45e6ebd876878a843615c6c5764869acd%2Fopen_pull_request.png?alt=media)

   A pull request should contain the details of all commits as specific as possible, including "Fixes: #(issue number)".

   Finally, click the "Create pull request" button.

   The changes would be merged post a review by the respective module owners. Once the changes are merged, you will get a notification, and the corresponding issue will be closed.
8. DCO Signoffs

   To ensure that contributors are only submitting work that they have rights to, we are requiring everyone to acknowledge this by signing their work. Any copyright notices in this repo should specify the authors as "KubeArmor authors".

   To sign your work, just add a line like this at the end of your commit message:

   ```
   Signed-off-by: FirstName LastName <email@address.com>
   ```

   This can easily be done with the `-s` or `--signoff` option to `git commit`.

   By doing this, you state that the source code being submitted originated from you (see <https://developercertificate.org>).
