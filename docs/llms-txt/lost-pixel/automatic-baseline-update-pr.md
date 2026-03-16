# Source: https://docs.lost-pixel.com/docs/recipes/lost-pixel-oss/automatic-baseline-update-pr.md

# Automatic baseline update PR

Lost Pixel offers and easy GitHub action integration that will help you to automate the baseline update process by creating the PR with updated images. You will just need to accept it and merge into the original branch.

Assuming you are using [Ladle example](https://docs.lost-pixel.com/docs/guides/getting-started/getting-started), in the root of your repo let's add a new action file that runs on demand:\
`.github/workflows/update-baselines.yml`

{% hint style="info" %}
You need to [create a new personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) to use it in the workflow and you can extend the automatic pr action by following guides [in the original repo](https://github.com/peter-evans/create-pull-request) of **create-pull-request**
{% endhint %}

```yaml
on: workflow_dispatch

jobs:
  lost-pixel-update:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Setup Node
        uses: actions/setup-node@v2
        with:
          node-version: 18.x
          cache: 'npm'

      - name: Install dependencies
        run: npm install

      - name: Build ladle
        run: npm run build

      - name: Serve ladle
        run: npm run serve &

      - name: Lost Pixel
        id: lp
        uses: lost-pixel/lost-pixel@v3.22.0
        env:
          LOST_PIXEL_MODE: update
      - name: Create Pull Request
        uses: peter-evans/create-pull-request@v4
        if: ${{ failure() && steps.lp.conclusion == 'failure' }}
        with:
          token: ${{ secrets.GH_TOKEN }}
          commit-message: update lost-pixel baselines
          delete-branch: true
          branch: 'lost-pixel-update/${{ github.ref_name }}'
          title: 'Lost Pixel update - ${{ github.ref_name }}'
          body: Automated baseline update PR created by Lost Pixel
```

![Run the action this way](https://354517992-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2tpFIKHmNw4YdppgU75t%2Fuploads%2Fgit-blob-cd87a8718f957045155a99b0c61f3388b3cae2e8%2Fimage%20\(1\).png?alt=media)

The action run will generate a new PR against the original branch that will contain updated baselines, merge it and expect your tests to be **green again**:green\_circle:

![Automatically generated PR](https://354517992-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2tpFIKHmNw4YdppgU75t%2Fuploads%2Fgit-blob-fcfdcbd661c2beae13273af8463bd2f865a46f8d%2Fimage.png?alt=media)
