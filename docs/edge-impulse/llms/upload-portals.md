# Source: https://docs.edgeimpulse.com/studio/organizations/upload-portals.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Upload portals

<Info>
  **Only available on the Enterprise plan**

  This feature is only available on the Enterprise plan. Review our [plans and pricing](https://edgeimpulse.com/pricing) or sign up for our free [expert-led trial](https://edgeimpulse.com/expert-led-trial) today.
</Info>

Upload portals are a secure way to let external parties upload data to your datasets. Through an upload portal they get an easy user interface to add data, but they have no access to the content of the dataset, nor can they delete any files. Data that is uploaded through the portal can be stored on-premise or in your own cloud infrastructure.

In this tutorial we'll set up an upload portal, show you how to add new data, and how to show this data in Edge Impulse for further processing.

### 1. Configuring a storage bucket

Data is stored in cloud storage. For details on how to connect a cloud storage provider to Edge Impulse, refer to the [Cloud data storage](/studio/organizations/data/cloud-data-storage) documentation.

### 2. Creating an upload portal

With your storage bucket configured you're ready to set up your first upload portal. In your organization go to **Data > Upload portals** and choose **Create new upload portal**. Here, select a name, a description, the storage bucket, and a path in the storage bucket.

<Frame caption="Creating an upload portal">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/320e70b-portal01.png?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=3d12f05e003cb9cff725d0f60ad2b677" width="840" height="540" data-path=".assets/images/320e70b-portal01.png" />
</Frame>

After your portal is created a link is shown. This link contains an authentication token, and can be shared directly with the third party.

<Frame caption="An active upload portal">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/4c556e2-screenshot_2021-02-09_at_221850.png?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=7f9ed41090c1f23056d3def9795895fe" width="826" height="429" data-path=".assets/images/4c556e2-screenshot_2021-02-09_at_221850.png" />
</Frame>

Click the link to open the portal. If you ever forget the link: no worries. Click the `⋮` next to your portal, and choose **View portal**.

### 3. Uploading data to the portal

<Frame caption="An upload portal with two folders.">
  <img src="https://mintcdn.com/edgeimpulse/mqaETyKntJOjsP_8/.assets/images/f2a915b-screenshot_2021-02-09_at_222156.png?fit=max&auto=format&n=mqaETyKntJOjsP_8&q=85&s=fd282a4adb441de54def239672f9d87e" width="1373" height="565" data-path=".assets/images/f2a915b-screenshot_2021-02-09_at_222156.png" />
</Frame>

To upload data you can now drag & drop files or folders to the drop zone on the right, or use **Create new folder** to first create a folder structure. There's no limit to the amount of files you can upload here, and all files are hashed, so if you upload a file that's already present the file will be skipped.

**Note:** Files with the same name but with a different hash are overwritten.

### 4. Using your portal in transformation blocks / clinical data

If you want to process data in a portal as part of a [Clinical Pipeline](/knowledge/guides/reference-designs/health-reference-design) you can either:

1. Mount the portal directly into a transformation block via **Custom blocks > Transformation blocks > Edit block**, and select the portal under mount points.
2. Mount the bucket that the portal is in, as a transformation block. This will also give you access to all other data in the bucket, very useful if you need to sync other data (see [Synchronizing clinical data](/knowledge/guides/reference-designs/health-reference-design/synchronizing-clinical-data)).

### 5. Adding the data to your project

If the data in your portal is already in the right format you can also directly import the uploaded data to your project. In your project view, go to [**Data Sources**](/studio/projects/data-acquisition/data-sources), \*\*\*\* select 'Upload portal' and follow the steps of the wizard:

<Frame caption="Data Sources - Upload portal method">
  <img src="https://mintcdn.com/edgeimpulse/sFtdfPhSpbLZ2-cz/.assets/images/studio-data-sources-upload-portal.png?fit=max&auto=format&n=sFtdfPhSpbLZ2-cz&q=85&s=9637ee2330a9a140f656d0148dce4541" width="1128" height="1000" data-path=".assets/images/studio-data-sources-upload-portal.png" />
</Frame>

### 6. Recap

If you need a secure way for external parties to contribute data to your datasets then upload portals are the way to go. They offer a friendly user interface, upload data directly into your storage buckets, and give you an easy way to use the data directly in Edge Impulse. :rocket:

Any questions, or interested in the enterprise version of Edge Impulse? [Contact us](https://edgeimpulse.com/contact) for more information.

### Appendix A: Programmatic access to portals

Here's a Python script which uploads, lists and downloads data to a portal. To upload data you'll need to authenticate with a JWT token, see below this script for more info.

```
# portal_api.py

import requests
import json
import os
import hashlib

PORTAL_TOKEN = os.environ.get('EI_PORTAL_TOKEN')
PORTAL_ID = os.environ.get('EI_PORTAL_ID')
JWT_TOKEN = os.environ.get('EI_JWT_TOKEN')

if not PORTAL_TOKEN:
    print('Missing EI_PORTAL_TOKEN environmental variable.')
    print('Go to a portal, and copy the part after "?token=" .')
    print('Then run:')
    print('    export EI_PORTAL_TOKEN=ec61e...')
    print('')
    print('You can add the line above to your ~/.bashrc or ~/.zshrc file to automatically load the token in the future.')
    exit(1)

if not PORTAL_ID:
    print('Missing EI_PORTAL_ID environmental variable.')
    print('Go to a portal, open the browser console, and look for "portalId" in the "Hello world from Edge Impulse" object to find it.')
    print('Then run:')
    print('    export EI_PORTAL_ID=122')
    print('')
    print('You can add the line above to your ~/.bashrc or ~/.zshrc file to automatically load the token in the future.')
    exit(1)

if not JWT_TOKEN:
    print('WARN: Missing EI_JWT_TOKEN environmental variable, you will only have write-only access to the portal')
    print('Run `python3 get_jwt_token.py` for instructions on how to set the token')
    print('(this requires access to the organization that owns the portal)')

def get_file_hash(path):
    with open(path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def create_upload_link(file_name_in_portal, path):
    url = "https://studio.edgeimpulse.com/v1/api/portals/" + PORTAL_ID + "/upload-link"

    payload = json.dumps({
        'fileName': file_name_in_portal,
        "fileSize": os.path.getsize(path),
        "fileHash": get_file_hash(path)
    })
    headers = {
        'accept': "application/json",
        'content-type': "application/json",
        'x-token': PORTAL_TOKEN
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    if (response.status_code != 200):
        raise Exception('status code was not 200, but ' + str(response.status_code) + ' - ' + response.text)

    j = response.json()
    if (not j['success']):
        raise Exception('api request did not succeed ' + str(response.status_code) + ' - ' + response.text)

    return j['url']

def upload_file_to_s3(signed_url, path):
    with open(path, 'rb') as f:
        response = requests.request("PUT", signed_url, data=f, headers={})

        if (response.status_code != 200):
            raise Exception('status code was not 200, but ' + str(response.status_code) + ' - ' + response.text)

def upload_file_to_portal(file_name_in_portal, path):
    print('Uploading', file_name_in_portal + '...')
    link = create_upload_link(file_name_in_portal, path)
    upload_file_to_s3(link, path)
    print('Uploading', file_name_in_portal, 'OK')
    print('')


def create_download_link(file_name_in_portal):
    url = "https://studio.edgeimpulse.com/v1/api/portals/" + PORTAL_ID + "/files/download"

    payload = json.dumps({
        'path': file_name_in_portal,
    })
    headers = {
        'accept': "application/json",
        'content-type': "application/json",
        'x-token': PORTAL_TOKEN,
        'x-jwt-token': JWT_TOKEN
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    if (response.status_code != 200):
        raise Exception('status code was not 200, but ' + str(response.status_code) + ' - ' + response.text)

    j = response.json()
    if (not j['success']):
        raise Exception('api request did not succeed ' + str(response.status_code) + ' - ' + response.text)

    return j['url']

def download_file_from_s3(signed_url):
    response = requests.request("GET", signed_url, headers={})

    if (response.status_code != 200):
        raise Exception('status code was not 200, but ' + str(response.status_code) + ' - ' + response.text)

    return response.content

def download_file_from_portal(file_name_in_portal):
    print('Downloading', file_name_in_portal + '...')
    link = create_download_link(file_name_in_portal)
    f = download_file_from_s3(link)
    print('Downloading', file_name_in_portal, 'OK')
    print('')
    return f


def list_files_in_portal(prefix):
    url = "https://studio.edgeimpulse.com/v1/api/portals/" + PORTAL_ID + "/files"

    payload = json.dumps({
        'prefix': prefix,
    })
    headers = {
        'accept': "application/json",
        'content-type': "application/json",
        'x-token': PORTAL_TOKEN
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    if (response.status_code != 200):
        raise Exception('status code was not 200, but ' + str(response.status_code) + ' - ' + response.text)

    j = response.json()
    if (not j['success']):
        raise Exception('api request did not succeed ' + str(response.status_code) + ' - ' + response.text)

    return j['files']

# this is how you upload files to a portal using the Edge Impulse API
# first argument is the path in the portal, second is the location of the file
upload_file_to_portal('test.jpg', '/Users/janjongboom/Downloads/test.jpg')

# uploading to a subdirectory
upload_file_to_portal('flowers/daisy.jpg', '/Users/janjongboom/Downloads/daisy-resized.jpg')

# listing files
print('files in root folder', list_files_in_portal(''))
print('files in "flowers/"', list_files_in_portal('flowers/'))

# downloading a file
if JWT_TOKEN:
    buffer = download_file_from_portal('flowers/daisy.jpg')
    with open('output.jpg', 'wb') as f:
        f.write(buffer)
else:
    print('Not downloading files, EI_JWT_TOKEN not set')

print('Done!')

```

And here's a script to generate JWT tokens:

```
# get_jwt_token.py

import requests
import json
import argparse

def get_token(username, password):
    url = "https://studio.edgeimpulse.com/v1/api-login"

    payload = json.dumps({
        'username': username,
        "password": password,
    })
    headers = {
        'accept': "application/json",
        'content-type': "application/json",
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    if (response.status_code != 200):
        raise Exception('status code was not 200, but ' + str(response.status_code) + ' - ' + response.text)

    j = response.json()
    if (not j['success']):
        raise Exception('api request did not succeed ' + str(response.status_code) + ' - ' + response.text)

    return j['token']


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get Edge Impulse JWT token')
    parser.add_argument('--username', type=str, required=True, help="Username or email address")
    parser.add_argument('--password', type=str, required=True)

    args, unknown = parser.parse_known_args()

    token = get_token(args.username, args.password)

    print('JWT token is:', token)
    print('')
    print('Use this in portal_api.py via:')
    print('    export EI_JWT_TOKEN=' + token)
    print('')
    print('You can add the line above to your ~/.bashrc or ~/.zshrc file to automatically load the token in the future.')
    print('Note: This token is valid for a limited time!')

```


Built with [Mintlify](https://mintlify.com).