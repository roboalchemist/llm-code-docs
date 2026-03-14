# Source: https://docs.edgeimpulse.com/tutorials/topics/lifecycle-management/deploy-github-actions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy using GitHub Actions

### Introduction

In today’s tech world, CI/CD (Continuous Integration/Continuous Deployment) is crucial for delivering fully tested and up-to-date software or firmware to your customers. This tutorial will guide you through integrating Edge Impulse Studio with [GitHub workflows](https://docs.github.com/en/actions/using-workflows), enabling seamless build and deployment of your Edge Impulse model into your workflow.

Edge Impulse provides a comprehensive [REST API](/apis/studio) for seamless integration with third-party services, allowing for the automation of tasks within Edge Impulse Studio. The GitHub Action we created [available here](https://github.com/edgeimpulse/build-deploy) simplifies the process of building and deploying models into your workflow.

This example was adapted from the [Edge Impulse Blog - Integrate Your GitHub Workflow with Edge Impulse Studio](https://www.edgeimpulse.com/blog/integrate-your-github-workflow-with-edge-impulse-studio/).

### Prerequisites

* GitHub repository for your firmware source code.
* Edge Impulse project created in the Studio.

### Steps

1. Obtain Project ID and API Key

* Navigate to your Edge Impulse project in the Studio.
* Select "Dashboard" from the left pane, then click on "Keys" at the top.

<Frame caption="GitHub Actions - Configure">
  <img src="https://mintcdn.com/edgeimpulse/j0k3ldYt05ndiX05/.assets/images/github-actions-configure.png?fit=max&auto=format&n=j0k3ldYt05ndiX05&q=85&s=10378653e670db3c402b0c8d6102c74d" width="1177" height="1000" data-path=".assets/images/github-actions-configure.png" />
</Frame>

* Note down the Project ID and Project API Key.

2. Add GitHub Action to Your Workflow

* Open your workflow YAML file in your GitHub repository.
* Add the following code to your workflow YAML file:

  ```yaml  theme={"system"}
  - name: Build and deploy Edge Impulse Model
   uses: edgeimpulse/build-deploy@v1
   id: build-deploy
   with:
    project_id: ${{ secrets.PROJECT_ID }}
    api_key: ${{ secrets.API_KEY }}
  ```

  Replace `${{ secrets.PROJECT_ID }}` and `${{ secrets.API_KEY }}` with your actual Edge Impulse Project ID and API Key.

3. Extract the Model and SDK

* After the build and deployment action, you may want to extract the model and SDK.
* Use the following example code in your workflow:

  ```yaml  theme={"system"}
  - name: Extract the Model and SDK
   run: |
    mkdir temp
    unzip -q "${{ steps.build-deploy.outputs.deployment_file_name }}" -d temp
    mv temp/edge-impulse-sdk/ .
    mv temp/model-parameters/ .
    mv temp/tflite-model/ .
    rm -rf "${{ steps.build-deploy.outputs.deployment_file_name }}"
    rm -rf temp/
  ```

4. Customize Deployment Type (Optional)

* By default, the GitHub Action downloads the C++ library. You can customize the deployment type using the deployment\_type input parameter. We can use a simple Python script [here](https://gist.github.com/mmajchrzycki/23e3cb6daf986b7ac1d0aeef08592228)

<Frame caption="GitHub Actions - Deploy Type">
  <img src="https://mintcdn.com/edgeimpulse/j0k3ldYt05ndiX05/.assets/images/github-actions-configure.png?fit=max&auto=format&n=j0k3ldYt05ndiX05&q=85&s=10378653e670db3c402b0c8d6102c74d" width="1177" height="1000" data-path=".assets/images/github-actions-configure.png" />
</Frame>

* Here's an example of downloading the Arduino library:

  ```yaml  theme={"system"}
  - name: Build and deploy Edge Impulse Model
   uses: edgeimpulse/build-deploy@v1
   id: build-deploy
   with:
    project_id: ${{ secrets.PROJECT_ID }}
    api_key: ${{ secrets.API_KEY }}
    deployment_type: "arduino"
  ```

5. Real-world Use Case

* Utilize the GitHub Action for CI/CD purposes.
* For example, testing public examples to prevent breaking changes.
* Here's an example of using the Action with Nordic Semiconductor/Zephyr inference [example](https://github.com/edgeimpulse/example-standalone-inferencing-zephyr/blob/master/.github/workflows/test-build.yml):

<Frame caption="GitHub Actions - IDE">
  <img src="https://mintcdn.com/edgeimpulse/j0k3ldYt05ndiX05/.assets/images/github-actions-ide.png?fit=max&auto=format&n=j0k3ldYt05ndiX05&q=85&s=bf4c09ec0d1457cdbb9a21b640a80540" width="1227" height="1000" data-path=".assets/images/github-actions-ide.png" />
</Frame>

```yaml  theme={"system"}
- name: Build and deploy EI Model
 uses: ./.github/actions/build-deploy
 id: build-deploy
 with:
  project_id: ${{ secrets.PROJECT_ID }}
  api_key: ${{ secrets.API_KEY }}
- name: Extract the EI Model
 run: |
  mkdir ei-model
  unzip -q "${{ steps.build-deploy.outputs.deployment_file_name }}" -d ei-model
  mv ei-model/edge-impulse-sdk/ .
  mv ei-model/model-parameters/ .
  mv ei-model/tflite-model/ .
  rm -rf "${{ steps.build-deploy.outputs.deployment_file_name }}"
  rm -rf ei-model/
- name: Build test app for nRF52840DK
 run: |
  docker run --rm -v $PWD:/app zephyr-ncs-1.9.1:latest west build -b nrf52840dk_nrf52840
```

6. Notification for Workflow Errors

* Thanks to GitHub Actions notification, the person responsible for the commit that created an error in workflow will be notified.

### Conclusion

Integrating Edge Impulse Studio with GitHub workflows enhances your CI/CD pipeline by automating the build and deployment process of your Edge Impulse models. This simplifies the development and testing of firmware, ensuring its accuracy and reliability.
GitHub repository for your firmware source code.
Edge Impulse project created in the Studio.


Built with [Mintlify](https://mintlify.com).