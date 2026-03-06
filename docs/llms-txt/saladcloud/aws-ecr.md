# Source: https://docs.salad.com/container-engine/how-to-guides/registries/aws-ecr.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Amazon Elastic Container Registry (ECR)

*Last Updated: October 15, 2024*

Amazon Elastic Container Service (Amazon ECS) is a highly scalable and fully managed container orchestration service
offered by Amazon Web Services (AWS). It is a platform that allows you to easily run, deploy, and manage Docker
containers and containerized applications. This guide will walk you through the process of deploying containers from
Amazon Elastic Container Registry to the SaladCloud Portal.

### Step 1: Generate Keys and Tokens

Generate keys and get your token in Amazon Elastic Container Service.Follow this
[official Amazon ECS ](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html)guide to generate
AWS keys and retrieve your token.

### Step 2: Configure Image in SaladCloud Container Environment (SCE)

Access the SaladCloud portal, Set up your SCE by selecting the private registry tab when setting the image source. In
the service dropdown option, choose "AWS Elastic Container Registry" and provide the following information:

* Image name (example: `docker.io/{username}/{my-container-image}:{version/latest}`)

<img src="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-ecr.png?fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=c3c910d9c2858db384d32e2d0d6d5baf" data-og-width="1835" width="1835" data-og-height="937" height="937" data-path="container-engine/images/configure-ecr.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-ecr.png?w=280&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=aed7b071f5a39332542eeedbb7db73ae 280w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-ecr.png?w=560&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=160e0769ef87a8d57461b21e47e333c2 560w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-ecr.png?w=840&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=6b662a0a173ed7e2c0268694a91a3700 840w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-ecr.png?w=1100&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=46b400545db108a722091504005bd6c7 1100w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-ecr.png?w=1650&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=43ad7cf9a3132990e02b106eb47031c1 1650w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-ecr.png?w=2500&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=ad8214e3da11aae4241ad5894591aa9d 2500w" />

Here is an example of what they look like:

* Access Key ID:`AKIAIOSFODNN7EXAMPLE`
* Secret Access Key: `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY` {/* cSpell:enable */}

Please note that these are just examples and not real credentials. When you generate your own Access Key ID and Secret
Access Key in AWS, they will be unique and randomly generated. You can refer to the
[official documentation ](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/get-set-up-for-amazon-ecs.html#get-set-up-ecs-iam-resources)guide
on how to get yours above.

> 👍 Congratulations!
>
> You have successfully configured the private container registry using Amazon Elastic Container Registry (ECR). Now,
> you can proceed to configure and deploy your container group.

Please refer to the AWS documentation for more information.
