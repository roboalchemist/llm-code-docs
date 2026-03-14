# Source: https://docs.mage.ai/production/ci-cd/local-cloud/gitlab-ci-cd.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# GitLab deployments

> Development (local) and production (cloud) using GitLab CI/CD.

## Mage project setup

Follow the [Mage project setup instructions](/production/ci-cd/local-cloud/repository-setup).

***

## GitLab CI/CD setup

1. Create a new repository on GitLab.
2. Open your repository on GitLab, then click the tab labeled **Settings**.
3. Click the section labeled **CI/CD**.
4. Under the section labeled **Variables**, click the button labeled **Expand**.
5. Click the button labeled **Add variable**.
6. Follow the instructions below for your specific cloud provider:

***

## AWS

1. If you haven’t already, create a new AWS ECR repository.

2. You’ll need AWS credentials with the following policy permissions:
   ```json  theme={"system"}
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Action": [
           "ecr:BatchCheckLayerAvailability",
           "ecr:CompleteLayerUpload",
           "ecr:GetAuthorizationToken",
           "ecr:InitiateLayerUpload",
           "ecr:PutImage",
           "ecr:UploadLayerPart",
           "ecs:DeregisterTaskDefinition",
           "ecs:DescribeClusters",
           "ecs:DescribeServices",
           "ecs:DescribeTaskDefinition",
           "ecs:RegisterTaskDefinition",
           "ecs:UpdateService",
           "iam:PassRole"
         ],
         "Resource": "*"
       }
     ]
   }
   ```

3. When adding a variable, in the field labeled **Key**, enter the value `AWS_ACCESS_KEY_ID`.

4. When adding a variable, in the field labeled **Value**, enter your AWS Access Key ID.

5. Check the box labeled **Mask variable**..

6. Click the button labeled **Add variable** to save.

7. Add a 2nd secret by clicking the button labeled **Add variable** in
   the top right corner.

8. In the field labeled **Key**, enter the value `AWS_SECRET_ACCESS_KEY`.

9. In the field labeled **Value**, enter your AWS Secret Access Key.

10. Check the box labeled **Mask variable**..

11. Click the button labeled **Add variable** to save.

12. In the field labeled **Key**, enter the value `AWS_DEFAULT_REGION`.

13. In the field labeled **Value**, enter your AWS default region.

14. Click the button labeled **Add variable** to save.

15. Create a new file in your repository and name it `.gitlab-ci.yml`.
    If you followed the [Mage project setup instructions](/production/ci-cd/local-cloud/repository-setup),
    then your current folder structure could look like this:
    ```
    my_team/
    |   demo_project/
    |   .gitlab-ci.yml
    |   Dockerfile
    ```

16. Copy the contents of this [GitLab CI/CD template file](https://github.com/mage-ai/mage-ai/blob/master/templates/gitlab_cicd/aws.gitlab-ci.yml)
    and paste it into the file named `.gitlab-ci.yml`.

17. Change the following values in the file named `.gitlab-ci.yml` under the key labeled `variables`:

    ```yaml  theme={"system"}
    variables:
      REPOSITORY_URL: ...
      CLUSTER_NAME: ...
      SERVICE_NAME: ...
      TASK_DEFINITION_NAME: ...
    ```

    | Key                    | Description                                                                                     | Sample value                                             |
    | ---------------------- | ----------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
    | `REPOSITORY_URL`       | The URL of the AWS ECR repository you created to store your Docker images.                      | `679812356111.dkr.ecr.us-west-2.amazonaws.com/mage-data` |
    | `CLUSTER_NAME`         | The name of your AWS ECS cluster.                                                               | `mage-production-cluster`                                |
    | `SERVICE_NAME`         | The name of your AWS ECS service.                                                               | `mage-production-ecs-service`                            |
    | `TASK_DEFINITION_NAME` | Go to your AWS ECS task definition for the above service. Use the name of that task definition. | `mage-production-task`                                   |

18. If you use a different branch than `main`, for example `master`,
    you must edit the value `only` under the `build` and `deploy` key in the file `.gitlab-ci.yml`.
    For example:
    ```yaml  theme={"system"}
    build:
      # other settings
      only:
        - master

    deploy:
      # other settings
      only:
        - master
    ```

19. Commit your changes with the new file `.gitlab-ci.yml`.

20. Push your commits to GitLab.

21. Every time you merge a pull request into the main or master branch, this GitLab
    CI/CD pipeline will run, building a Docker image using your GitLab code, then
    updating AWS ECS to use the new image with the updated code.

***

## GCP

*Coming soon...*

***

## Azure

*Coming soon...*


Built with [Mintlify](https://mintlify.com).