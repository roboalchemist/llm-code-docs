# Source: https://docs.jit.io/docs/code-samples.md

# Test Jit's Detection: Code Samples and Targets

Test out Jit's detection capabilities using the code samples and test targets below.

## Scan code for vulnerabilities (Python)

File name: test.py

```python test.py
import yaml

def exploitable_yaml_load(**kwargs):
    """
    The string `!!python/object/new:os.system` is a YAML tag that tells the parser
    to create a new Python object by calling 'os.system' with 'echo EXPLOIT!' as its argument.
    When using 'yaml.unsafe_load', this can lead to arbitrary command execution.
    """
    yaml.unsafe_load("!!python/object/new:os.system [echo EXPLOIT!]", **kwargs)
```

Expected output:

![](https://files.readme.io/717cdf5d93cf71e91e6a5b883a363d36ec8cb70db649303518d01055c267ab79-image.png)

## Scan code for vulnerabilities (Javascript)

File name: test.js

```python test.js
const { exec } = require('child_process');
const http = require('http');
const url = require('url');

http.createServer((req, res) => {
  const query = url.parse(req.url, true).query;
  const fileName = query.file;

  // ⚠️ Vulnerability: User-controlled input passed to exec without sanitization
  exec(`cat ${fileName}`, (err, stdout, stderr) => {
    if (err) {
      res.writeHead(500);
      res.end(`Error: ${stderr}`);
      return;
    }
    res.writeHead(200);
    res.end(stdout);
  });
}).listen(3000);

console.log('Server running on http://localhost:3000');

```

Expected output:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7b710eda65033dfe7194ebde336615e0f7b70291b40f703e8b81b4376ed87dc3-Screenshot_2025-04-14_at_15.38.22.png",
        null,
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

## Scan code for vulnerabilities (GO)

File name: test.go

```go py
package testutil // import "github.com/docker/docker/testutil"

import "math/rand"

// GenerateRandomAlphaOnlyString generates an alphabetical random string with length n.
func GenerateRandomAlphaOnlyString(n int) string {
	// make a really long string
	letters := []byte("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
	b := make([]byte, n)
	for i := range b {
		b[i] = letters[rand.Intn(len(letters))] //nolint: gosec // G404: Use of weak random number generator (math/rand instead of crypto/rand)
	}
	return string(b)
}
```

Expected output:

![](https://files.readme.io/cd37fa2-Screen_Shot_2022-07-15_at_9.37.07.png)

## Scan code dependencies for vulnerabilities (Node)

File name: package.json

```json package.json
{
  "name": "dependencygoat2",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "minimist": "0.0.8"
  }
}
```

Expected output:

![](https://files.readme.io/e3b940c-Screen_Shot_2022-07-15_at_8.50.11.png)

## Scan code dependencies for vulnerabilities (Python)

File name: requirements.txt

```Text requirements.txt
requests==2.18.2
urllib3==1.26.4

```

Expected output:

![](https://files.readme.io/6471dab-Screen_Shot_2022-08-08_at_11.27.57.png)

## Scan code for hard-coded secrets (Multi-languages)

File name: secret.txt

```json secret.txt
MY_AWS_SECRET="AKIAIOSFODNN7EXAMPLE"
```

Expected output:

![](https://files.readme.io/3fa2374-Screen_Shot_2022-07-15_at_8.52.19.png)

## Scan IaC for static misconfigurations

### S3 Bucket ACL allows Read or Write to all users (Terraform)

File name: test.tf

```json test.tf
resource "aws_s3_bucket" "positive1" {
  bucket = "my-tf-test-bucket"
  acl    = "public-read"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }

  versioning {
    enabled = true
  }
}
```

Expected output:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a4394a8df21380da7ae55776285ed7f1309ee5baa15b8ffa0c2e1f7fc0dea0f0-Screenshot_2025-04-14_at_15.50.37.png",
        null,
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

### ECR Repository Is Publicly Accessible (CloudFormation)

File Name: test.json

```json test.json
{
  "Resources": {
    "MyRepository4": {
      "Type": "AWS::ECR::Repository",
      "Properties": {
        "RepositoryName": "test-repository",
        "RepositoryPolicyText": {
          "Version": "2008-10-17",
          "Statement": [
            {
              "Sid": "AllowPushPull",
              "Effect": "Allow",
              "Principal": "*",
              "Action": [
                "ecr:GetDownloadUrlForLayer",
                "ecr:BatchGetImage",
                "ecr:BatchCheckLayerAvailability",
                "ecr:PutImage",
                "ecr:InitiateLayerUpload",
                "ecr:UploadLayerPart",
                "ecr:CompleteLayerUpload"
              ]
            }
          ]
        }
      }
    }
  }
}

```

Expected output:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a38db53e8346effb3ba2f3f06054c959b1e8b8a1fdc14ce07cb3b6ae096a535c-Screenshot_2025-04-14_at_16.04.42.png",
        null,
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

<br />

## Run a Web Application Scanner / Ensure Your APIs are Secure (ZAP-based security requirements)

Use the following tests to verify that your security requirements based on ZAP (which include *Run a Web Application Scanner* and *Ensure Your APIs are Secure*) are functional.

### Test target: Google Firing Range

<https://www.zaproxy.org/docs/scans/firingrange/>

### Test target: Google Security Crawl Maze

<https://www.zaproxy.org/docs/scans/crawlmaze/>

### Test target: OWASP Benchmark

<https://www.zaproxy.org/docs/scans/benchmark/>

### Test target: Websites Vulnerable to SSTI

<https://www.zaproxy.org/docs/scans/ssti/>

### Test target: Yahoo Webseclab

<https://www.zaproxy.org/docs/scans/webseclab/>

```
name: Sync Jit Teams
on:
  schedule:
    - cron: "0 3 * * *"
  workflow_dispatch:

jobs:
  sync-teams:
    runs-on: ubuntu-latest
    steps:
    - name: Check out code
      uses: actions/checkout@v3
    - name: Call action
      uses: jitsecurity/jit-sync-teams-github-action@v1.1.0
      with:
        JIT_CLIENT_ID: ${{ secrets.JIT_CLIENT_ID }}
        JIT_CLIENT_SECRET: ${{ secrets.JIT_CLIENT_SECRET }}
        ORGANIZATION_NAME: ${{ github.repository_owner }}
        GITHUB_API_TOKEN: ${{ secrets.MY_GITHUB_API_TOKEN }}
        TEAM_WILDCARD_TO_EXCLUDE: "*dev*, *test*"
```