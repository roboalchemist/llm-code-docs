# Source: https://docs.safetycli.com/safety-docs/safety-cli/scanning-for-vulnerable-and-malicious-packages/scanning-in-ci-cd.md

# Scanning in CI/CD

## Using Safety as a GitHub Action

Safety can be integrated into your existing GitHub CI pipeline as an Action. Just add the following as a step in your workflow YAML file after setting your `SAFETY_API_KEY` secret on GitHub under Settings -> Secrets -> Actions:

```
      - uses: pyupio/safety-action@v1
        with:
          api-key: ${{ secrets.SAFETY_API_KEY }}
```

(Don't have an API Key? You can sign up for one with <https://safetycli.com/resources/plans>.)

This will run Safety scan and will fail your CI pipeline if any vulnerable packages are found.

If you have something more complicated such as a monorepo; or once you're finished testing, read the [Documentation](https://docs.safetycli.com/) for more details on configuring Safety as an action.

Link to GitHub Action: <https://github.com/marketplace/actions/pyupio-safety-action>

For more information, visit the [GitHub Action](https://docs.safetycli.com/safety-docs/installation/securing-git-repositories/github/github-actions) documentation below:

{% content-ref url="../../installation/securing-git-repositories/github/github-actions" %}
[github-actions](https://docs.safetycli.com/safety-docs/installation/securing-git-repositories/github/github-actions)
{% endcontent-ref %}
