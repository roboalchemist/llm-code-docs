# Source: https://docs-v3.activeloop.ai/v3.2.22/storage-and-credentials/user-authentication.md

# Source: https://docs-v3.activeloop.ai/v3.4.0/storage-and-credentials/user-authentication.md

# Source: https://docs-v3.activeloop.ai/v3.4.1/storage-and-credentials/user-authentication.md

# Source: https://docs-v3.activeloop.ai/v3.6.0/storage-and-credentials/user-authentication.md

# Source: https://docs-v3.activeloop.ai/v3.6.1/storage-and-credentials/user-authentication.md

# Source: https://docs-v3.activeloop.ai/v3.6.2/storage-and-credentials/user-authentication.md

# Source: https://docs-v3.activeloop.ai/v3.6.3/storage-and-credentials/user-authentication.md

# Source: https://docs-v3.activeloop.ai/v3.6.8/storage-and-credentials/user-authentication.md

# Source: https://docs-v3.activeloop.ai/v3.6.9/storage-and-credentials/user-authentication.md

# Source: https://docs-v3.activeloop.ai/v3.6.18/storage-and-credentials/user-authentication.md

# Source: https://docs-v3.activeloop.ai/v3.7.0/storage-and-credentials/user-authentication.md

# Source: https://docs-v3.activeloop.ai/v3.7.1/storage-and-credentials/user-authentication.md

# Source: https://docs-v3.activeloop.ai/v3.7.2/storage-and-credentials/user-authentication.md

# Source: https://docs-v3.activeloop.ai/v3.7.3/storage-and-credentials/user-authentication.md

# Source: https://docs-v3.activeloop.ai/v3.8.2/storage-and-credentials/user-authentication.md

# Source: https://docs-v3.activeloop.ai/v3.8.16/storage-and-credentials/user-authentication.md

# Source: https://docs-v3.activeloop.ai/v3.8.19/storage-and-credentials/user-authentication.md

# Source: https://docs-v3.activeloop.ai/v3.8.27/storage-and-credentials/user-authentication.md

# User Authentication

## How to Register and Authenticate in Deep Lake

In order to use Deep Lake features that require authentication (Activeloop storage, connecting your cloud dataset to the Deep Lake UI, etc.) you should register and login with Deep Lake.

### Registration

You can[ register in the Deep Lake App](https://app.activeloop.ai/register/).

### Authentication in Programmatic Interfaces

After registering, you can create an API token in the [Deep Lake UI](https://app.activeloop.ai/) (top-right corner, user settings) and authenticate in programatic interfaces using 2 options:

#### Environmental Variable

Set the environmental variable `ACTIVELOOP_TOKEN` to your API token. In Python, this can be done using:

`os.environ['ACTIVELOOP_TOKEN'] = <your_token>`

#### Pass the Token to Individual Methods

You can pass your API token to individual methods that require authentication such as:

`ds = deeplake.load('hub://org_name/dataset_name', token = <your_token>)`
