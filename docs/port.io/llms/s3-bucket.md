# Source: https://docs.port.io/guides/all/s3-bucket.md

# Manage an S3 Bucket Lifecycle

In this example you are going to create an AWS S3 bucket and then report its information to Port as an S3 bucket entity.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

You will need to create a developer environment blueprint to follow this example:

* API
* Terraform

Create in Port

```
{
  "identifier": "s3Bucket",
  "description": "",
  "title": "S3 Bucket",
  "icon": "Bucket",
  "schema": {
    "properties": {
      "isPrivate": {
        "type": "boolean",
        "title": "Is private?"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "relations": {}
}
```

```
terraform {
  required_providers {
    port = {
      source  = "port-labs/port-labs"
      version = "~> 2.0.3"
    }
  }
}

provider "port" {
  client_id = "YOUR_CLIENT_ID"     # or set the environment variable PORT_CLIENT_ID
  secret    = "YOUR_CLIENT_SECRET" # or set the environment variable PORT_CLIENT_SECRET
  base_url  = "https://api.port.io"
}

resource "port_blueprint" "s3_bucket" {
  identifier = "s3Bucket"
  icon       = "Bucket"
  title      = "S3 Bucket"

  properties = {
    boolean_props = {
      isPrivate = {
        title      = "Is private?"
        required   = false
      }
    }
  }
}
```

Selecting a Port API URL by account region

The `port_region`, `port.baseUrl`, `portBaseUrl`, `port_base_url` and `OCEAN__PORT__BASE_URL` parameters select which Port API instance to use:

* **EU** ([app.port.io](https://app.port.io)) â `https://api.port.io`
* **US** ([app.us.port.io](https://app.us.port.io)) â `https://api.us.port.io`

Here is the complete `main.tf` file:

Complete Terraform definition file

```
terraform {
  required_providers {
    port = {
      source  = "port-labs/port-labs"
      version = "~> 2.0.3"
    }
  }
}

provider "aws" {
  access_key = "YOUR_ACCESS_KEY_ID"
  secret_key = "YOUR_SECRET_ACCESS_KEY"
  region     = "eu-west-1"
}

provider "port" {
  client_id = "YOUR_CLIENT_ID"     # or set the environment variable PORT_CLIENT_ID
  secret    = "YOUR_CLIENT_SECRET" # or set the environment variable PORT_CLIENT_SECRET
  base_url  = "https://api.port.io"
}

resource "aws_s3_bucket" "port-terraform-example-bucket" {
  bucket = "my-port-terraform-example-bucket"
}

resource "aws_s3_bucket_acl" "port-terraform-example-bucket-acl" {
  bucket = aws_s3_bucket.port-terraform-example-bucket.id
  acl    = "private"
}

resource "port_entity" "s3_bucket" {
  depends_on = [
    aws_s3_bucket.port-terraform-example-bucket
  ]

  identifier = aws_s3_bucket.port-terraform-example-bucket.bucket
  title      = aws_s3_bucket.port-terraform-example-bucket.bucket
  blueprint  = "s3Bucket"

  properties = {
    string_props = {
      "isPrivate" = aws_s3_bucket_acl.port-terraform-example-bucket-acl.acl == "private" ? true : false
    }
  }
}
```

Selecting a Port API URL by account region

The `port_region`, `port.baseUrl`, `portBaseUrl`, `port_base_url` and `OCEAN__PORT__BASE_URL` parameters select which Port API instance to use:

* **EU** ([app.port.io](https://app.port.io)) â `https://api.port.io`
* **US** ([app.us.port.io](https://app.us.port.io)) â `https://api.us.port.io`

To use this example yourself, simply replace the placeholders for `access_key`, `secret_key`, `client_id` and `secret` and then run the following commands to setup your new backend, create the new infrastructure and update the software catalog:

```
# install modules and create an initial state
terraform init
# To view Terraform's planned changes based on your .tf definition file:
terraform plan
# To apply the changes and update the catalog
terraform apply
```

Let's break down the definition file and understand the different parts:

## Module imports[â](#module-imports "Direct link to Module imports")

This part includes importing and setting up the required Terraform providers and modules:

```
terraform {
  required_providers {
    port = {
      source  = "port-labs/port-labs"
      version = "~> 2.0.3"
    }
  }
}

provider "aws" {
  access_key = "YOUR_ACCESS_KEY_ID"
  secret_key = "YOUR_SECRET_ACCESS_KEY"
  region     = "eu-west-1"
}

provider "port" {
  client_id = "YOUR_CLIENT_ID"     # or set the environment variable PORT_CLIENT_ID
  secret    = "YOUR_CLIENT_SECRET" # or set the environment variable PORT_CLIENT_SECRET
  base_url  = "https://api.port.io"
}
```

Selecting a Port API URL by account region

The `port_region`, `port.baseUrl`, `portBaseUrl`, `port_base_url` and `OCEAN__PORT__BASE_URL` parameters select which Port API instance to use:

* **EU** ([app.port.io](https://app.port.io)) â `https://api.port.io`
* **US** ([app.us.port.io](https://app.us.port.io)) â `https://api.us.port.io`

## Defining the S3 bucket and bucket ACLs[â](#defining-the-s3-bucket-and-bucket-acls "Direct link to Defining the S3 bucket and bucket ACLs")

This part includes defining the S3 bucket and attaching an ACL policy:

```
resource "aws_s3_bucket" "port-terraform-example-bucket" {
  bucket = "my-port-terraform-example-bucket"
}

resource "aws_s3_bucket_acl" "port-terraform-example-bucket-acl" {
  bucket = aws_s3_bucket.port-terraform-example-bucket.id
  acl    = "public-read"
}
```

## Creating the S3 bucket entity matching the new bucket[â](#creating-the-s3-bucket-entity-matching-the-new-bucket "Direct link to Creating the S3 bucket entity matching the new bucket")

This part includes configuring the `s3Bucket` blueprint and creating an entity for our new bucket:

```
resource "port_entity" "s3_bucket" {
  depends_on = [
    aws_s3_bucket.port-terraform-example-bucket
  ]

  identifier = aws_s3_bucket.port-terraform-example-bucket.bucket
  title      = aws_s3_bucket.port-terraform-example-bucket.bucket
  blueprint  = "s3Bucket"

  properties = {
    string_props = {
      "isPrivate" = aws_s3_bucket_acl.port-terraform-example-bucket-acl.acl == "private" ? true : false
    }
  }
}
```

Terraform dependencies

Note how we use a `depends_on` block on the new s3 entity because the entity relies on values that will only be available after the S3 bucket is created.

## Result[â](#result "Direct link to Result")

After running `terraform apply` you will see the new S3 bucket in AWS, and the matching `s3Bucket` entity in Port.

Continue reading to learn how to make updates and how to cleanup.

## Updating the S3 bucket and the matching entity[â](#updating-the-s3-bucket-and-the-matching-entity "Direct link to Updating the S3 bucket and the matching entity")

Notice how we defined the `isPrivate` property of the bucket entity:

```
properties = {
    string_props = {
      "isPrivate" = aws_s3_bucket_acl.port-terraform-example-bucket-acl.acl == "private" ? true : false
    }
}
```

Since the initial bucket we created was configured as `private`, the value of the property is `true`.

Let's modify the bucket policy:

```
resource "aws_s3_bucket_acl" "port-terraform-example-bucket-acl" {
  bucket = aws_s3_bucket.port-terraform-example-bucket.id
  acl    = "public-read" # Changed from "private"
}
```

And now by running `terraform apply`, both the bucket policy will change, as well as the `isPrivate` property of the matching entity.

## Cleanup[â](#cleanup "Direct link to Cleanup")

To cleanup your environment, you can run the command `terraform destroy`, which will delete all of the resources you created in this example (including the S3 bucket and matching Port entity).
