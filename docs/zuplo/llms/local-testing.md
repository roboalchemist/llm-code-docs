# Source: https://www.zuplo.com/docs/articles/ci-cd-azure/local-testing.md

# Source: https://www.zuplo.com/docs/articles/ci-cd-bitbucket/local-testing.md

# Source: https://www.zuplo.com/docs/articles/ci-cd-circleci/local-testing.md

# Source: https://www.zuplo.com/docs/articles/ci-cd-github/local-testing.md

# Source: https://www.zuplo.com/docs/articles/ci-cd-gitlab/local-testing.md

# GitLab CI/CD: Local Testing in CI

Test against a local Zuplo server before deploying anywhere.

```yaml title=".gitlab-ci.yml"
image: node:20

stages:
  - test
  - deploy

local-test:
  stage: test
  script:
    - npm install
    - npx zuplo dev &
    - sleep 10
    - npx zuplo test --endpoint http://localhost:9000
    - kill %1

deploy:
  stage: deploy
  needs:
    - local-test
  script:
    - npm install
    - npx zuplo deploy --api-key "$ZUPLO_API_KEY"
  only:
    - main
```

Local tests run first. Only if they pass does deployment proceed.

## Next Steps

- Add [multi-stage deployment](./multi-stage-deployment.mdx) with staging
