# Source: https://docs.salad.com/container-engine/how-to-guides/imds/container-status-endpoint.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using IMDS to get the status of a replica

*Last Updated: October 15, 2024*

We can use the IMDS to retrieve the current status of the replica from inside the workload. This can be achieved using
either the IMDS SDK, or the JSON request endpoint. In this example, we'll create a Python script using the IMDS SDK to
check whether the container is ready, and start a bash script when it is.

## Using the SDK to retrieve the status

We'll start by using the IMDS SDK to retrieve the statuses of the currently running container.

<CodeGroup>
  ```python  theme={null}
  from salad_cloud_imds_sdk import SaladCloudImdsSdk, Environment

  sdk = SaladCloudImdsSdk( base_url=Environment.DEFAULT.value, timeout=10000 )

  result = sdk.metadata.get_container_status()

  print(result)

  ```

  ```c#  theme={null}
  using Salad.Cloud.IMDS.SDK;

  var client = new SaladCloudImdsSdkClient();

  var response = await client.Metadata.GetContainerStatusAsync();

  Console.WriteLine(response);

  ```

  ```go  theme={null}
  import (
    "fmt"
    "encoding/json"
    "github.com/saladtechnologies/salad-cloud-imds-sdk-go/pkg/saladcloudimdssdkconfig"
    "github.com/saladtechnologies/salad-cloud-imds-sdk-go/pkg/saladcloudimdssdk"
  )

  config := saladcloudimdssdkconfig.NewConfig()
  client := saladcloudimdssdk.NewSaladCloudImdsSdk(config)

  response, err := client.Metadata.GetContainerStatus(context.Background())
  if err != nil {
    panic(err)
  }

  fmt.Print(response)
  ```

  ```java  theme={null}
  import com.salad.cloud.imdssdk.SaladCloudImdsSdk;
  import com.salad.cloud.imdssdk.models.ContainerStatus;

  public class Main {

    public static void main(String[] args) {
      SaladCloudImdsSdk saladCloudImdsSdk = new SaladCloudImdsSdk();

      ContainerStatus response = saladCloudImdsSdk.metadataService.getContainerStatus();

      System.out.println(response);
    }
  }
  ```

  ```typescript  theme={null}
  import { SaladCloudImdsSdk } from '@saladtechnologies-oss/salad-cloud-imds-sdk'
  ;(async () => {
    const saladCloudImdsSdk = new SaladCloudImdsSdk({})

    const { data } = await saladCloudImdsSdk.metadata.getContainerStatus()

    console.log(data)
  })()
  ```

  ```php  theme={null}
  <?php

  $curl = curl_init();

  curl_setopt_array($curl, [
    CURLOPT_URL => "http://169.254.169.254/v1/status",
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_ENCODING => "",
    CURLOPT_MAXREDIRS => 10,
    CURLOPT_TIMEOUT => 30,
    CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
    CURLOPT_CUSTOMREQUEST => "GET",
  ]);

  $response = curl_exec($curl);
  $err = curl_error($curl);

  curl_close($curl);

  if ($err) {
    echo "cURL Error #:" . $err;
  } else {
    echo $response;
  }
  ```
</CodeGroup>

Now, if we run this on a container that has passed its
[startup probe](/container-engine/explanation/infrastructure-platform/startup-probes), but not completed its
[readiness probe](/container-engine/explanation/infrastructure-platform/readiness-probes), we'll see this:

```json  theme={null}
{
  "ready": false,
  "started": true
}
```

## Starting a script when its ready

Now we know the status of the container, we can use this to start a bash script when it reaches a ready state.

```python  theme={null}
import json
from subprocess import call
from salad_cloud_imds_sdk import SaladCloudImdsSdk, Environment

sdk = SaladCloudImdsSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.metadata.get_container_status()

#Get the ready status out of the JSON response
data = json.loads(result)

status = data['ready']

if status == True:
  subprocess.call("exampleScript.sh")
else: print("Not Ready Yet!")
```
