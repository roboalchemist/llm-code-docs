# Source: https://kreya.app/docs/cli/integrations/gitlab.md

# GitLab CI/CD

The Kreya CLI can be used in GitLab CI/CD to automatically test APIs with the kreyac docker image.

```
stages:
  - test

api-test:
  stage: test
  image: riok/kreyac:1
  script:
    - kreyac info
    - kreyac environment set-active Production
    - kreyac operation invoke "REST/Get books.krop" # invoke a single REST operation by name
    - kreyac operation invoke "gRPC/Say hello.krop" # invoke a single gRPC operation by name
    - kreyac operation invoke "WebSocket/Echo.krop" # invoke a single WebSocket operation by name
    - kreyac collection invoke "Kreya features/Collection/Collection.krcol" --test-report-junit junit.xml # invoke a collection and generate a JUnit report
  # include JUnit report output
  artifacts:
    when: always
    paths:
      - junit.xml
    reports:
      junit: junit.xml
```

Secrets can be stored as CI/CD variables prefixed with `KREYA_ENV_`. Environment variables prefixed with `KREYA_ENV_` are imported into the active Kreya environment with the prefix stripped. See also [process environment data](/docs/environments.md#process--system-environment-variables).
