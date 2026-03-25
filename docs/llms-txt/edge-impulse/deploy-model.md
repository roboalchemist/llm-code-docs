# Source: https://docs.edgeimpulse.com/tutorials/tools/apis/studio/deploy-model.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy a model

The [Edge Impulse API](/apis/studio) gives programmatic access to all features in the studio, and many tasks that might normally have to be performed manually can thus be automated. In this tutorial you'll create a job that deploys your model (as a ZIP file), you monitor the job status, and then finally download the deployed model. The tutorial uses Python, but you can use any environment capable of scripting HTTP requests.

To run this script you'll need:

* A recent version of Python 3.
* The `requests` module:

```
pip3 install requests
```

* Your project ID (can be found on **Dashboard** in the Edge Impulse Studio).
* An API Key (under **Dashboard > Keys**).

Then, create the following script **build-model.py**:

```py  theme={"system"}
import requests, json, datetime, time, re

project_id = 1 # YOUR PROJECT ID
api_key = "ei_..." # YOUR API KEY
deploy_type = "zip" # CAN CHANGE TO DIFFERENT TYPE

def build_model():
    url = f"https://studio.edgeimpulse.com/v1/api/{project_id}/jobs/build-ondevice-model"
    querystring = {"type": deploy_type}
    payload = {"engine": "tflite-eon"}
    headers = {
        "x-api-key": api_key,
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    response = requests.request("POST", url, json=payload, headers=headers, params=querystring)
    body = json.loads(response.text)
    if (not body['success']):
        raise Exception(body['error'])
    return body['id']

def get_stdout(job_id, skip_line_no):
    url = f"https://studio.edgeimpulse.com/v1/api/{project_id}/jobs/{job_id}/stdout"
    headers = {
        "x-api-key": api_key,
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    response = requests.request("GET", url, headers=headers)
    body = json.loads(response.text)
    if (not body['success']):
        raise Exception(body['error'])
    stdout = body['stdout'][::-1] # reverse array so it's old -> new
    return [ x['data'] for x in stdout[skip_line_no:] ]

def wait_for_job_completion(job_id):
    skip_line_no = 0

    url = f"https://studio.edgeimpulse.com/v1/api/{project_id}/jobs/{job_id}/status"
    headers = {
        "x-api-key": api_key,
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    while True:
        response = requests.request("GET", url, headers=headers)
        body = json.loads(response.text)
        if (not body['success']):
            raise Exception(body['error'])

        stdout = get_stdout(job_id, skip_line_no)
        for l in stdout:
            print(l, end='')
        skip_line_no = skip_line_no + len(stdout)

        if (not 'finished' in body['job']):
            # print('Job', job_id, 'is not finished yet...', body['job'])
            time.sleep(1)
            continue
        if (not body['job']['finishedSuccessful']):
            raise Exception('Job failed')
        else:
            break

def download_model():
    url = f"https://studio.edgeimpulse.com/v1/api/{project_id}/deployment/download"
    querystring = {"type": deploy_type}
    headers = {
        "x-api-key": api_key,
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    response = requests.request("GET", url, headers=headers, params=querystring)

    d = response.headers['Content-Disposition']
    fname = re.findall("filename\*?=(.+)", d)[0].replace('utf-8\'\'', '')

    return fname, response.content

if __name__ == "__main__":
    job_id = build_model()
    print('Job ID is', job_id)
    wait_for_job_completion(job_id)
    print('Job', job_id, 'is finished')
    bin_filename, bin_file = download_model()
    print('Output file is', len(bin_file), 'bytes')
    with open(bin_filename, 'wb') as f:
        f.write(bin_file)
    print('Written job output to', bin_filename)
```

When you now run `python3 download-model.py` you'll see something like:

```
Job ID is 1486148
Writing templates OK

Scheduling job in cluster...
Compiling EON model...
Job started
Compiling EON model OK
Removing clutter...
Removing clutter OK
Copying output...
Copying output OK

Job 1486148 is finished
Output file is 4824580 bytes
Written job output to myawesomeproject-v63.zip
```

:rocket:


Built with [Mintlify](https://mintlify.com).