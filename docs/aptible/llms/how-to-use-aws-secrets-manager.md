# Source: https://www.aptible.com/docs/how-to-guides/app-guides/how-to-use-aws-secrets-manager.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to use AWS Secrets Manager with Aptible Apps

> Learn how to use AWS Secrets Manager with Aptible Apps

# Overview

AWS Secrets Manager is a secure and centralized solution for managing sensitive data like database credentials and API keys. This guide provides an example of how to set up AWS Secrets Manager to store and retreive secrets into an Aptible App. This reference example uses a Rails app, but this can be used in conjunction with any app framework supported by AWS SDKs.

# **Steps**

### **Store Secrets in AWS Secrets Manager**

* Log in to the AWS Console.

* Navigate to `Secrets Manager`.

* Click Store a new secret.

* Select Other type of secret.

* Enter your key-value pairs (e.g., `DATABASE_PASSWORD`, `API_KEY`).

* Click Next and provide a Secret Name (e.g., `myapp/production`).

* Complete the steps to store the secret.

### **Set Up IAM Permissions**

Set up AWS Identity and Access Management (IAM) objects to grant access to the secret from your Aptible app.

***Create a Custom IAM Policy***: for better security, create a custom policy that grants only the necessary permissions.

* Navigate to IAM in the AWS Console, and click on Create policy

* In the Create Policy page, select the JSON tab.

* Paste the following policy JSON:

```json  theme={null}
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowSecretsManagerReadOnlyAccess",
      "Effect": "Allow",
      "Action": [
        "secretsmanager:GetSecretValue",
        "secretsmanager:DescribeSecret"
      ],
      "Resource": "*"
    }
  ]
}
```

* Click Review policy.

* Enter a Name for the policy (e.g., `SecretsManagerReadOnlyAccess`).

* Click Create policy.

***Note***: the example IAM policy above grants access to all secrets in the account via `"Resource": "*"`. You may additionally opt to restrict access to specific secrets for better security. An example of restricting access to a specific secret:

```yaml  theme={null}
"Resource": "arn:aws:secretsmanager:us-east-1:123456789012:secret:myapp/production"
```

***Create an IAM User***

* Log in to your AWS Management Console.

* Navigate to the IAM (Identity and Access Management) service.

* In the left sidebar, click on Users, then click Add users.

* Configure the following settings:

  * User name: Enter a username (e.g., secrets-manager-user).

  * Access type: Select Programmatic access.

* Click Next: Permissions.

* To attach an existing policy, search for your newly created policy (SecretsManagerReadOnlyAccess) and check the box next to it.

***Generate API Keys for the IAM User***

* In the IAM dashboard, click on "Users" in the left navigation pane.

* Click on the username of the IAM user for whom you want to generate API keys.

* Go to Security Credentials. Within the user's summary page, select the "Security credentials" tab.

* Scroll down to the "Access keys" section.

* Click on the "Create access key" button.

* Choose the appropriate access key type (typically "Programmatic access").

* Download the Credentials: After the access key is created, click on "Download .csv file" to save the Access Key ID and Secret Access Key securely. Important: This is the only time you can view or download the secret access key. Keep it in a secure place.

### **Set Up AWS Credentials on Aptible**

Aptible uses environment variables for configuration. Set the following AWS credentials:

```bash  theme={null}
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION (e.g., us-east-1)
```

To set environment variables in Aptible:

* Log in to your Aptible Dashboard.

* Select your app and navigate to the Configuration tab.

* Add the AWS credentials as environment variables.

### **Add AWS SDK to Your Rails App**

Add the AWS SDK gem to interact with AWS Secrets Manager:

```ruby  theme={null}
# Gemfile
gem 'aws-sdk-secretsmanager'
```

Run:

```bash  theme={null}
bundle install
```

### **Create a Service to Fetch Secrets**

Create a service object that fetches secrets from AWS Secrets Manager.

```ruby  theme={null}
# app/services/aws_secrets_manager_service.rb
require 'aws-sdk-secretsmanager'

class AwsSecretsManagerService
  def initialize(secret_name:, region:)
    @secret_name = secret_name
    @region = region
  end

  def fetch_secrets
    client = Aws::SecretsManager::Client.new(region: @region)
    secret_value = client.get_secret_value(secret_id: @secret_name)

    secrets = if secret_value.secret_string
                JSON.parse(secret_value.secret_string)
              else
                JSON.parse(Base64.decode64(secret_value.secret_binary))
              end

    secrets.transform_keys { |key| key.upcase }
  rescue Aws::SecretsManager::Errors::ServiceError => e
    Rails.logger.error "AWS Secrets Manager Error: #{e.message}"
    {}
  end
end
```

### **Initialize Secrets at Startup**

Create an initializer to load secrets when the app starts.

```ruby  theme={null}
# config/initializers/load_secrets.rb
if Rails.env.production?
  secret_name = 'myapp/production' # Update with your secret name
  region = ENV['AWS_REGION']

  secrets_service = AwsSecretsManagerService.new(secret_name: secret_name, region: region)
  secrets = secrets_service.fetch_secrets

  ENV.update(secrets) if secrets.present?
end
```

### **Use Secrets in Your App**

Access the secrets via ENV variables.

Example: Database Configuration

```yaml  theme={null}
# config/database.yml
production:
  adapter: postgresql
  encoding: unicode
  host: <%= ENV['DATABASE_HOST'] %>
  database: <%= ENV['DATABASE_NAME'] %>
  username: <%= ENV['DATABASE_USERNAME'] %>
  password: <%= ENV['DATABASE_PASSWORD'] %>
```

Example: API Key Usage

```ruby  theme={null}
# app/services/external_api_service.rb
class ExternalApiService
  API_KEY = ENV['API_KEY']

  def initialize
    # Use API_KEY in your requests
  end
end
```
