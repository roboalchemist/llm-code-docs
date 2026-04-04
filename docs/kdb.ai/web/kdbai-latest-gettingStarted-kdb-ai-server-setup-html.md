# Source: https://code.kx.com/kdbai/latest/gettingStarted/kdb-ai-server-setup.html

Title: KDB.AI Server Setup - KDB.AI Documentation

URL Source: https://code.kx.com/kdbai/latest/gettingStarted/kdb-ai-server-setup.html

Markdown Content:
_This page details the steps to set up KDB.AI Server._

Hardware requirements
---------------------

KDB.AI Server works on Intel, AMD, ARM, and Apple CPUs that meet the below specifications:

*   Intel CPUs that support AVX2 instructions (Haswell architecture).
*   AMD CPUs that support AVX2 instructions (Zen architecture).
*   ARM (aarch64) CPUs that support NEON instructions.
*   Apple MX CPUs (M1, M2, and M3) that support NEON instructions.

KDB.AI Server supports Linux ARM-based CPUs via Docker and on Apple Silicon via Docker desktop or Rancher desktop.

For Rancher desktop on Apple Silicon, we recommend the following setup:

1.   Go to **Preferences**>**Virtual Machine**.
2.   In the **Volumes** tab > tick **`virtiofs`** as **Mount type**. 
3.   **Emulation tab**> select **`VZ`** as the **Virtual Machine Type**.

Software requirements
---------------------

You can run KDB.AI Server under [Docker](https://docs.docker.com/get-docker/) or [Rancher](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade).

For demonstration purposes, the following steps provide guidance for running the KDB.AI Server under [Docker](https://docs.docker.com/engine/install/):

1.   A Linux kernel of 4.18.0 or later is required to run the KDB.AI container. Examples of such distros include:

    *   CentOS 8 or later
    *   Red Hat Enterprise Linux (RHEL) 8 or later
    *   Ubuntu 18.04 or later

2.   If you run KDB.AI Server on Windows, we recommend using the Windows Subsystem for Linux (WSL) instead of running it directly on Windows. This way, the volume mounts are from a Linux filesystem (for example, `ext4`) and avoid any related errors.

System requirements
-------------------

The KDB.AI Server Standard Edition license is limited to 24 cores. When running the Docker container, if the machine contains more than 24 cores, adjust the Docker run command to include `--cpuset-cpus`, for example `--cpuset-cpus 1-24`. See step 3 of [Start the KDB.AI docker image](https://code.kx.com/kdbai/latest/gettingStarted/kdb-ai-server-setup.html#start-the-kdbai-docker-image) for more details. If you're using Rancher, make sure to tick `dockered(moby)` in **General**>**Preferences**>**Container Engine**>**General**.

Sign up
-------

Ensure you have [signed up](https://kx.com/kdb-ai-server-download/) for KDB.AI Server Edition.

Having trouble finding the **Welcome email**? Expand for more.
1.   Check your spam folder. The subject of the Welcome email is **Your KDB.AI Server: Standard Edition evaluation is ready**.
2.   Add **support@kdb.ai** to the **Safe senders** list to prevent your personal or corporate antivirus or email protection software to block the email from being delivered.
3.   Contact the [Support team](mailto:support@kdb.ai).

Start the KDB.AI docker image
-----------------------------

1.   Create a location on the local disk to write data:

```
mkdir vdbdata
``` 
2.   Set permissions to read and write to this directory:

```
chmod 0777 vdbdata
``` 
3.   Log into the KX Docker registry using the email you signed up with and the Bearer Token string from your Welcome email:

```
docker login portal.dl.kx.com -u <the email you signed up with> -p <long Bearer Token string from your Welcome email>
``` 
4.   Run the container in detached mode, including the `KDB_LICENSE_B64` string from your Welcome email. You can also use a `K4` license:

KDB_LICENSE KDB_K4LICENSE

```
export KDB_LICENSE_B64=<your-base64-license-string>
docker run -d \
    -p 8081:8081 \
    -p 8082:8082 \
    -e KDB_LICENSE_B64=$KDB_LICENSE_B64 \
    -e VDB_DIR="/tmp/kx/data/vdb" \
    -v "$PWD/vdbdata":/tmp/kx/data \
    -e THREADS="8" \
    portal.dl.kx.com/kdbai-db
``` ```
export KDB_K4LICENSE_B64=<your-base64-k4license-string>
docker run -d \
    -p 8081:8081 \
    -p 8082:8082 \
    -e KDB_K4LICENSE_B64=$KDB_K4LICENSE_B64 \
    -e VDB_DIR="/tmp/kx/data/vdb" \
    -v "$PWD/vdbdata":/tmp/kx/data \
    -e THREADS="8" \
    portal.dl.kx.com/kdbai-db
```   
The first port in the `-p` line is configurable, but the second port `8082` must not be changed.

The `THREADS` environment variable

The THREADS environment variable determines the number of threads utilized by each worker in multithreaded operations. Setting this variable helps optimize performance by allowing parallel execution of tasks.

    *   Syntax: `THREADS=<number_of_threads>`
    *   Example: `THREADS="8"`

We recommend setting `THREADS` to the number of CPU cores available on the machine running KDB.AI Server. For a comprehensive understanding of how multithreading works and how to optimize the `THREADS` variable, refer to the dedicated [multithreading](https://code.kx.com/kdbai/latest/reference/multithreading.html) page.

Troubleshooting tips. Expand for more.
    *   Didn't get a success message? Try removing `-d` from the above command to view the container logs and any potential errors.
    *   If you attempt to run the Docker container on a machine with more than 24 cores, the execution fails with a cores error. To work around it, add a `--cpuset-cpus` parameter to the Docker run command, for example `--cpuset-cpus 1-24`.

5.   Check if the KDB.AI container is running:

```
docker ps
``` Do you receive an error message while running docker using sudo? Expand for more.
Add the `-E` flag so environmental variables like `KDB_LICENSE_B64` are picked up. Therefore, the command becomes: `-E docker ps`. 

Install the KDB.AI client
-------------------------

1.   Install the latest version of KDB.AI client using pip from PyPI using the following command:

Python REST

```
pip install kdbai-client
``` ```
Ensure curl is installed, for example, `which curl`
```   
KDB.AI supports Python (versions 3.9 to 3.13).

2.   Establish and verify the connection with the KDB.AI Server:

Python REST

```
import kdbai_client as kdbai
session = kdbai.Session(endpoint='http://localhost:8082')
database = session.database('default')
print(database.tables)
# expected response should be an empty list [] because you haven't created any tables yet
``` ```
curl http://localhost:8081/api/v2/ready
# expected response 'OK'
```   

Export the KDB.AI docker logs
-----------------------------

If you encounter an issue, we recommend exporting your log file by running the following:

```
docker logs <your-container-name> > yourDocker.log 2>&1
```

Send your log file `yourDocker.log` to the [Support team](mailto:support@kdb.ai).

Stop the KDB.AI docker image
----------------------------

If you wish you stop the KDB.AI Server, stop the container by running:

```
docker stop <your-container-name>
```

KDB.AI Server License Validity

The KDB.AI Server setup is valid for 90 days. To continue using the server after this period, you need to update the license by following the steps in the email reminder and contacting Sales for the paid license.

Next steps
----------

Go to our [Quickstart Guide](https://code.kx.com/kdbai/latest/gettingStarted/quickstart.html) page to set up your table schema and start inserting data.
