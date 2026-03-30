# Source: https://www.zuplo.com/docs/articles/ci-cd-azure/tag-based-releases.md

# Source: https://www.zuplo.com/docs/articles/ci-cd-bitbucket/tag-based-releases.md

# Source: https://www.zuplo.com/docs/articles/ci-cd-circleci/tag-based-releases.md

# Source: https://www.zuplo.com/docs/articles/ci-cd-github/tag-based-releases.md

# Source: https://www.zuplo.com/docs/articles/ci-cd-gitlab/tag-based-releases.md

# GitLab CI/CD: Tag-Based Releases

Deploy only when tags are pushed for controlled releases.

```yaml title=".gitlab-ci.yml"
image: node:20

stages:
  - deploy

deploy:
  stage: deploy
  script:
    - npm install
    - npx zuplo deploy --api-key "$ZUPLO_API_KEY" --environment "$CI_COMMIT_TAG"
  only:
    - tags
```

This pipeline triggers only on tags and creates an environment named after the
tag (e.g., `v1.0.0`).

## Next Steps

- Add [multi-stage deployment](./multi-stage-deployment.mdx) with approval
