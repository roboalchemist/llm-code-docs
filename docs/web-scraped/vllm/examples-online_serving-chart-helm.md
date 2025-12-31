# Source: https://docs.vllm.ai/en/stable/examples/online_serving/chart-helm/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/online_serving/chart-helm.md "Edit this page")

# Helm Charts[¶](#helm-charts "Permanent link")

Source <https://github.com/vllm-project/vllm/tree/main/examples/online_serving/chart-helm>.

This directory contains a Helm chart for deploying the vllm application. The chart includes configurations for deployment, autoscaling, resource management, and more.

## Files[¶](#files "Permanent link")

-   Chart.yaml: Defines the chart metadata including name, version, and maintainers.
-   ct.yaml: Configuration for chart testing.
-   lintconf.yaml: Linting rules for YAML files.
-   values.schema.json: JSON schema for validating values.yaml.
-   values.yaml: Default values for the Helm chart.
-   templates/\_helpers.tpl: Helper templates for defining common configurations.
-   templates/configmap.yaml: Template for creating ConfigMaps.
-   templates/custom-objects.yaml: Template for custom Kubernetes objects.
-   templates/deployment.yaml: Template for creating Deployments.
-   templates/hpa.yaml: Template for Horizontal Pod Autoscaler.
-   templates/job.yaml: Template for Kubernetes Jobs.
-   templates/poddisruptionbudget.yaml: Template for Pod Disruption Budget.
-   templates/pvc.yaml: Template for Persistent Volume Claims.
-   templates/secrets.yaml: Template for Kubernetes Secrets.
-   templates/service.yaml: Template for creating Services.

## Running Tests[¶](#running-tests "Permanent link")

This chart includes unit tests using [helm-unittest](https://github.com/helm-unittest/helm-unittest). Install the plugin and run tests:

    # Install plugin
    helm plugin install https://github.com/helm-unittest/helm-unittest

    # Run tests
    helm unittest .

## Example materials[¶](#example-materials "Permanent link")

.helmignore

    *.png
    .git/
    ct.yaml
    lintconf.yaml
    values.schema.json
    /workflows

Chart.yaml

    apiVersion: v2
    name: chart-vllm
    description: Chart vllm

    # A chart can be either an 'application' or a 'library' chart.
    #
    # Application charts are a collection of templates that can be packaged into versioned archives
    # to be deployed.
    #
    # Library charts provide useful utilities or functions for the chart developer. They're included as
    # a dependency of application charts to inject those utilities and functions into the rendering
    # pipeline. Library charts do not define any templates and therefore cannot be deployed.
    type: application

    # This is the chart version. This version number should be incremented each time you make changes
    # to the chart and its templates, including the app version.
    # Versions are expected to follow Semantic Versioning (https://semver.org/)
    version: 0.0.1

    maintainers:
      - name: mfournioux

ct.yaml

    chart-dirs:
      - charts
    validate-maintainers: false

lintconf.yaml

    ---
    rules:
      braces:
        min-spaces-inside: 0
        max-spaces-inside: 0
        min-spaces-inside-empty: -1
        max-spaces-inside-empty: -1
      brackets:
        min-spaces-inside: 0
        max-spaces-inside: 0
        min-spaces-inside-empty: -1
        max-spaces-inside-empty: -1
      colons:
        max-spaces-before: 0
        max-spaces-after: 1
      commas:
        max-spaces-before: 0
        min-spaces-after: 1
        max-spaces-after: 1
      comments:
        require-starting-space: true
        min-spaces-from-content: 2
      document-end: disable
      document-start: disable           # No --- to start a file
      empty-lines:
        max: 2
        max-start: 0
        max-end: 0
      hyphens:
        max-spaces-after: 1
      indentation:
        spaces: consistent
        indent-sequences: whatever      # - list indentation will handle both indentation and without
        check-multi-line-strings: false
      key-duplicates: enable
      line-length: disable              # Lines can be any length
      new-line-at-end-of-file: disable
      new-lines:
        type: unix
      trailing-spaces: enable
      truthy:
        level: warning

templates/\_helpers.tpl

    }
    }
    }
    }

    }
    }
    }
    }
    }
    "}-service"
    }
    }

    }
    }
    }
    }
    }
    }
    }
    }

    }
    }
    "service-port"
    }

    }
    }
    "container-port"
    }

    }
    }
    strategy:
    }
      rollingUpdate:
        maxSurge: 100%
        maxUnavailable: 0
    }
    }
    }
    }

    }
    }
    }
    }
    }
    }

    }
    }
    }
    }
    }
    }

    }
    }
    }
    readinessProbe:
    }
    }
    }
    }
    }
    livenessProbe:
    }
    }
    }
    }
    }

    }
    }
    requests:
      memory: }
      cpu: }
      }
      nvidia.com/gpu: }
      }
    limits:
      memory: }
      cpu: }
      }
      nvidia.com/gpu: }
      }
    }

    }
    }
    }
    runAsUser: 
    }
    }
    }
    }
    }

    }
    - name: S3_ENDPOINT_URL
      valueFrom:
        secretKeyRef:
          name: }-secrets
          key: s3endpoint
    - name: S3_BUCKET_NAME
      valueFrom:
        secretKeyRef:
          name: }-secrets
          key: s3bucketname
    - name: AWS_ACCESS_KEY_ID
      valueFrom:
        secretKeyRef:
          name: }-secrets
          key: s3accesskeyid
    - name: AWS_SECRET_ACCESS_KEY
      valueFrom:
        secretKeyRef:
          name: }-secrets
          key: s3accesskey
    }
    - name: S3_PATH
      value: "}"
    }
    }
    - name: AWS_EC2_METADATA_DISABLED
      value: "}"
    }
    }

    }
    }
    }
    }
    }
    }

templates/configmap.yaml

    }
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: "}-configs"
      namespace: }
    data:
      }
      }
      }
    }

templates/custom-objects.yaml

    }
    }
    }
    ---
    }
    }

templates/deployment.yaml

    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: "}-deployment-vllm"
      namespace: }
      labels:
      }
    spec:
      replicas: }
      }
      selector:                                                                                                                                  
        matchLabels:
          environment: "test"
          release: "test"
      progressDeadlineSeconds: 1200
      template:
        metadata:
          labels:
            environment: "test"
            release: "test"
        spec:
          containers:
            - name: "vllm"
              image: "}:}"
              }
              command :
                }
                }
                }
              }
              securityContext:
                }
                  }
                  }
                  }
                }
                runAsNonRoot: false
                  }
                }
              imagePullPolicy: IfNotPresent
              }
              env :
                }
                }
                }
              }
              env: []
              }
              }
              envFrom:
                }
                - configMapRef:
                    name: "}-configs"
                }
                }
                - secretRef:
                    name: "}-secrets"
                }
                }
              }          
              ports:
                - name: }
                  containerPort: }
                }
              }
              resources: }
              volumeMounts:
              - name: }-storage
                mountPath: /data

            }
            }
            }

          }
          initContainers:
          }
          - name: wait-download-model
            image: }:}
            imagePullPolicy: }
            command: }
            args:
            }
            env:
            }
            }
            }
            }
            }
            resources:
              requests:
                cpu: 200m
                memory: 1Gi
              limits:
                cpu: 500m
                memory: 2Gi
            volumeMounts:
            - name: }-storage
              mountPath: /data
          }
          }
          }
          }
          }
          volumes:
            - name: }-storage
              persistentVolumeClaim:
                claimName: }-storage-claim     

          }
          nodeSelector:
            }
          }
          }
          tolerations:
            }
          }
          }
          runtimeClassName: nvidia
          affinity:
            nodeAffinity:
              requiredDuringSchedulingIgnoredDuringExecution:
                nodeSelectorTerms:
                  - matchExpressions:
                    - key: nvidia.com/gpu.product
                      operator: In
                      }
                      values:
                        }
                      }
          } 

templates/hpa.yaml

    }
    apiVersion: autoscaling/v2
    kind: HorizontalPodAutoscaler
    metadata:
      name: "}-hpa"
      namespace: }
    spec:
      scaleTargetRef:
        apiVersion: apps/v1
        kind: Deployment
        name: vllm
      minReplicas: }
      maxReplicas: }
      metrics:
        }
        - type: Resource
          resource:
            name: cpu
            target:
              type: Utilization
              averageUtilization: }
        }
        }
        - type: Resource
          resource:
            name: memory
            target:
              type: Utilization
              averageUtilization: }
        }
    }

templates/job.yaml

    }
    apiVersion: batch/v1
    kind: Job
    metadata:
      name: "}-init-vllm"
      namespace: }
    spec:
      ttlSecondsAfterFinished: 100
      template:
       metadata:
         name: init-vllm
       spec:
        containers:
        - name: job-download-model
          image: }:}
          imagePullPolicy: }
          command: }
          args:
          }
          env:
          }
          }
          }
          }
          }
          volumeMounts:
            - name: }-storage
              mountPath: /data
          resources:
            requests:
              cpu: 200m
              memory: 1Gi
            limits:
              cpu: 500m
              memory: 2Gi
        restartPolicy: OnFailure
        volumes:
        - name: }-storage
          persistentVolumeClaim:
            claimName: "}-storage-claim"
    }

templates/poddisruptionbudget.yaml

    apiVersion: policy/v1
    kind: PodDisruptionBudget
    metadata:
      name: "}-pdb"
      namespace: }
    spec:
      maxUnavailable: }

templates/pvc.yaml

    }
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: "}-storage-claim"
      namespace: }
    spec:
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: }
    }

templates/secrets.yaml

    apiVersion: v1
    kind: Secret
    metadata:
      name: "}-secrets"
      namespace: }
    type: Opaque
    data:
      }
      }: }
      }

templates/service.yaml

    apiVersion: v1
    kind: Service
    metadata:
      name: "}-service"
      namespace: }
    spec:
      type: ClusterIP
      ports:
        - name: }
          port: }
          targetPort: }
          protocol: TCP
      selector:
      }

tests/deployment_test.yaml

    suite: test deployment
    templates:
      - deployment.yaml
    tests:
      - it: should create wait-download-model init container when modelDownload is enabled
        set:
          extraInit:
            modelDownload:
              enabled: true
              image:
                repository: "amazon/aws-cli"
                tag: "2.6.4"
                pullPolicy: "IfNotPresent"
              waitContainer:
                command: [ "/bin/bash" ]
                args:
                  - "-eucx"
                  - "while aws --endpoint-url $S3_ENDPOINT_URL s3 sync --dryrun s3://$S3_BUCKET_NAME/$S3_PATH /data | grep -q download; do sleep 10; done"
              downloadJob:
                command: [ "/bin/bash" ]
                args:
                  - "-eucx"
                  - "aws --endpoint-url $S3_ENDPOINT_URL s3 sync s3://$S3_BUCKET_NAME/$S3_PATH /data"
            initContainers: [ ]
            pvcStorage: "1Gi"
            s3modelpath: "relative_s3_model_path/opt-125m"
            awsEc2MetadataDisabled: true
        asserts:
          - hasDocuments:
              count: 1
          - isKind:
              of: Deployment
          - isNotEmpty:
              path: spec.template.spec.initContainers
          - equal:
              path: spec.template.spec.initContainers[0].name
              value: wait-download-model
          - equal:
              path: spec.template.spec.initContainers[0].image
              value: amazon/aws-cli:2.6.4
          - equal:
              path: spec.template.spec.initContainers[0].imagePullPolicy
              value: IfNotPresent

      - it: should only create custom init containers when modelDownload is disabled
        set:
          extraInit:
            modelDownload:
              enabled: false
              image:
                repository: "amazon/aws-cli"
                tag: "2.6.4"
                pullPolicy: "IfNotPresent"
              waitContainer:
                command: [ "/bin/bash" ]
                args: [ "-c", "echo test" ]
              downloadJob:
                command: [ "/bin/bash" ]
                args: [ "-c", "echo test" ]
            initContainers:
              - name: llm-d-routing-proxy
                image: ghcr.io/llm-d/llm-d-routing-sidecar:v0.2.0
                imagePullPolicy: IfNotPresent
                ports:
                  - containerPort: 8080
                    name: proxy
            pvcStorage: "10Gi"
        asserts:
          - hasDocuments:
              count: 1
          - isKind:
              of: Deployment
          - lengthEqual:
              path: spec.template.spec.initContainers
              count: 1
          - equal:
              path: spec.template.spec.initContainers[0].name
              value: llm-d-routing-proxy
          - equal:
              path: spec.template.spec.initContainers[0].image
              value: ghcr.io/llm-d/llm-d-routing-sidecar:v0.2.0
          - equal:
              path: spec.template.spec.initContainers[0].ports[0].containerPort
              value: 8080

      - it: should create both wait-download-model and custom init containers when both are enabled
        set:
          extraInit:
            modelDownload:
              enabled: true
              image:
                repository: "amazon/aws-cli"
                tag: "2.6.4"
                pullPolicy: "IfNotPresent"
              waitContainer:
                command: [ "/bin/bash" ]
                args:
                  - "-eucx"
                  - "while aws --endpoint-url $S3_ENDPOINT_URL s3 sync --dryrun s3://$S3_BUCKET_NAME/$S3_PATH /data | grep -q download; do sleep 10; done"
              downloadJob:
                command: [ "/bin/bash" ]
                args:
                  - "-eucx"
                  - "aws --endpoint-url $S3_ENDPOINT_URL s3 sync s3://$S3_BUCKET_NAME/$S3_PATH /data"
            initContainers:
              - name: llm-d-routing-proxy
                image: ghcr.io/llm-d/llm-d-routing-sidecar:v0.2.0
                imagePullPolicy: IfNotPresent
                ports:
                  - containerPort: 8080
                    name: proxy
            pvcStorage: "10Gi"
        asserts:
          - hasDocuments:
              count: 1
          - isKind:
              of: Deployment
          - lengthEqual:
              path: spec.template.spec.initContainers
              count: 2
          - equal:
              path: spec.template.spec.initContainers[0].name
              value: wait-download-model
          - equal:
              path: spec.template.spec.initContainers[0].image
              value: amazon/aws-cli:2.6.4
          - equal:
              path: spec.template.spec.initContainers[1].name
              value: llm-d-routing-proxy
          - equal:
              path: spec.template.spec.initContainers[1].image
              value: ghcr.io/llm-d/llm-d-routing-sidecar:v0.2.0
          - equal:
              path: spec.template.spec.initContainers[1].ports[0].containerPort
              value: 8080

tests/job_test.yaml

    suite: test job
    templates:
      - job.yaml
    tests:
      - it: should create job when modelDownload is enabled
        set:
          extraInit:
            modelDownload:
              enabled: true
              image:
                repository: "amazon/aws-cli"
                tag: "2.6.4"
                pullPolicy: "IfNotPresent"
              waitContainer:
                command: [ "/bin/bash" ]
                args: [ "-c", "wait" ]
              downloadJob:
                command: [ "/bin/bash" ]
                args:
                  - "-eucx"
                  - "aws --endpoint-url $S3_ENDPOINT_URL s3 sync s3://$S3_BUCKET_NAME/$S3_PATH /data"
            pvcStorage: "1Gi"
            s3modelpath: "relative_s3_model_path/opt-125m"
            awsEc2MetadataDisabled: true
        asserts:
          - hasDocuments:
              count: 1
          - isKind:
              of: Job
          - equal:
              path: spec.template.spec.containers[0].name
              value: job-download-model
          - equal:
              path: spec.template.spec.containers[0].image
              value: amazon/aws-cli:2.6.4
          - equal:
              path: spec.template.spec.restartPolicy
              value: OnFailure

      - it: should not create job when modelDownload is disabled
        set:
          extraInit:
            modelDownload:
              enabled: false
              image:
                repository: "amazon/aws-cli"
                tag: "2.6.4"
                pullPolicy: "IfNotPresent"
              waitContainer:
                command: [ "/bin/bash" ]
                args: [ "-c", "wait" ]
              downloadJob:
                command: [ "/bin/bash" ]
                args: [ "-c", "download" ]
            initContainers:
              - name: llm-d-routing-proxy
                image: ghcr.io/llm-d/llm-d-routing-sidecar:v0.2.0
            pvcStorage: "10Gi"
        asserts:
          - hasDocuments:
              count: 0

tests/pvc_test.yaml

    suite: test pvc
    templates:
      - pvc.yaml
    tests:
      # Test Case: PVC Created When extraInit Defined
      - it: should create pvc when extraInit is defined
        set:
          extraInit:
            modelDownload:
              enabled: true
              image:
                repository: "amazon/aws-cli"
                tag: "2.6.4"
                pullPolicy: "IfNotPresent"
              waitContainer:
                command: ["/bin/bash"]
                args: ["-c", "wait"]
              downloadJob:
                command: ["/bin/bash"]
                args: ["-c", "download"]
            pvcStorage: "10Gi"
        asserts:
          - hasDocuments:
              count: 1
          - isKind:
              of: PersistentVolumeClaim
          - equal:
              path: spec.accessModes[0]
              value: ReadWriteOnce
          - equal:
              path: spec.resources.requests.storage
              value: 10Gi

values.schema.json

    ,
                    "tag": ,
                    "command": 
                    }
                },
                "required": [
                    "command",
                    "repository",
                    "tag"
                ]
            },
            "containerPort": ,
            "serviceName": ,
            "servicePort": ,
            "extraPorts": ,
            "replicaCount": ,
            "deploymentStrategy": ,
            "resources": ,
                            "memory": ,
                            "nvidia.com/gpu": 
                        },
                        "required": [
                            "cpu",
                            "memory",
                            "nvidia.com/gpu"
                        ]
                    },
                    "limits": ,
                            "memory": ,
                            "nvidia.com/gpu": 
                        },
                        "required": [
                            "cpu",
                            "memory",
                            "nvidia.com/gpu"
                        ]
                    }
                },
                "required": [
                    "limits",
                    "requests"
                ]
            },
            "gpuModels": 
            },
            "autoscaling": ,
                    "minReplicas": ,
                    "maxReplicas": ,
                    "targetCPUUtilizationPercentage": 
                },
                "required": [
                    "enabled",
                    "maxReplicas",
                    "minReplicas",
                    "targetCPUUtilizationPercentage"
                ]
            },
            "configs": ,
            "secrets": ,
            "externalConfigs": ,
            "customObjects": ,
            "maxUnavailablePodDisruptionBudget": ,
            "extraInit": ,
                            "image": ,
                                    "tag": ,
                                    "pullPolicy": 
                                },
                                "required": ["repository", "tag", "pullPolicy"]
                            },
                            "waitContainer": 
                                    },
                                    "args": 
                                    },
                                    "env": 
                                    }
                                },
                                "required": ["command", "args"]
                            },
                            "downloadJob": 
                                    },
                                    "args": 
                                    },
                                    "env": 
                                    }
                                },
                                "required": ["command", "args"]
                            }
                        },
                        "required": ["enabled", "image", "waitContainer", "downloadJob"]
                    },
                    "initContainers": 
                    },
                    "s3modelpath": ,
                    "pvcStorage": ,
                    "awsEc2MetadataDisabled": 
                },
                "required": [
                    "modelDownload",
                    "initContainers",
                    "pvcStorage"
                ]
            },
            "extraContainers": ,
            "readinessProbe": ,
                    "periodSeconds": ,
                    "failureThreshold": ,
                    "httpGet": ,
                            "port": 
                        },
                        "required": [
                            "path",
                            "port"
                        ]
                    }
                },
                "required": [
                    "failureThreshold",
                    "httpGet",
                    "initialDelaySeconds",
                    "periodSeconds"
                ]
            },
            "livenessProbe": ,
                    "failureThreshold": ,
                    "periodSeconds": ,
                    "httpGet": ,
                            "port": 
                        },
                        "required": [
                            "path",
                            "port"
                        ]
                    }
                },
                "required": [
                    "failureThreshold",
                    "httpGet",
                    "initialDelaySeconds",
                    "periodSeconds"
                ]
            },
            "labels": ,
                    "release": 
                },
                "required": [
                    "environment",
                    "release"
                ]
            }
        },
        "required": [
            "autoscaling",
            "configs",
            "containerPort",
            "customObjects",
            "deploymentStrategy",
            "externalConfigs",
            "extraContainers",
            "extraInit",
            "extraPorts",
            "gpuModels",
            "image",
            "labels",
            "livenessProbe",
            "maxUnavailablePodDisruptionBudget",
            "readinessProbe",
            "replicaCount",
            "resources",
            "secrets",
            "servicePort"
        ]
    }

values.yaml

    # -- Default values for chart vllm
    # -- Declare variables to be passed into your templates.

    # -- Image configuration
    image:
      # -- Image repository
      repository: "vllm/vllm-openai"
      # -- Image tag
      tag: "latest"
      # -- Container launch command
      command: ["vllm", "serve", "/data/", "--served-model-name", "opt-125m", "--enforce-eager", "--dtype", "bfloat16", "--block-size", "16", "--host", "0.0.0.0", "--port", "8000"]

    # -- Container port
    containerPort: 8000
    # -- Service name
    serviceName:
    # -- Service port
    servicePort: 80
    # -- Additional ports configuration
    extraPorts: []

    # -- Number of replicas
    replicaCount: 1

    # -- Deployment strategy configuration
    deploymentStrategy: 

    # -- Resource configuration
    resources:
      requests:
        # -- Number of CPUs
        cpu: 4
        # -- CPU memory configuration
        memory: 16Gi
        # -- Number of gpus used
        nvidia.com/gpu: 1
      limits:
        # -- Number of CPUs
        cpu: 4
        # -- CPU memory configuration
        memory: 16Gi
        # -- Number of gpus used
        nvidia.com/gpu: 1

    # -- Type of gpu used
    gpuModels:
      - "TYPE_GPU_USED"

    # -- Autoscaling configuration
    autoscaling:
      # -- Enable autoscaling
      enabled: false
      # -- Minimum replicas
      minReplicas: 1
      # -- Maximum replicas
      maxReplicas: 100
      # -- Target CPU utilization for autoscaling
      targetCPUUtilizationPercentage: 80
      # targetMemoryUtilizationPercentage: 80

    # -- Configmap
    configs: 

    # -- Secrets configuration
    secrets: 

    # -- External configuration
    externalConfigs: []

    # -- Custom Objects configuration
    customObjects: []

    # -- Disruption Budget Configuration
    maxUnavailablePodDisruptionBudget: ""

    # -- Additional configuration for the init container
    extraInit:
      # -- Model download functionality (optional)
      modelDownload:
        # -- Enable model download job and wait container
        enabled: true
        # -- Image configuration for model download operations
        image:
          # -- Image repository
          repository: "amazon/aws-cli"
          # -- Image tag
          tag: "2.6.4"
          # -- Image pull policy
          pullPolicy: "IfNotPresent"
        # -- Wait container configuration (init container that waits for model to be ready)
        waitContainer:
          # -- Command to execute
          command: ["/bin/bash"]
          # -- Arguments for the wait container
          args:
            - "-eucx"
            - "while aws --endpoint-url $S3_ENDPOINT_URL s3 sync --dryrun s3://$S3_BUCKET_NAME/$S3_PATH /data | grep -q download; do sleep 10; done"
          # -- Environment variables (optional, overrides S3 defaults entirely if specified)
          # env:
          #   - name: HUGGING_FACE_HUB_TOKEN
          #     value: "your-token"
          #   - name: MODEL_ID
          #     value: "meta-llama/Llama-2-7b"
        # -- Download job configuration (job that actually downloads the model)
        downloadJob:
          # -- Command to execute
          command: ["/bin/bash"]
          # -- Arguments for the download job
          args:
            - "-eucx"
            - "aws --endpoint-url $S3_ENDPOINT_URL s3 sync s3://$S3_BUCKET_NAME/$S3_PATH /data"
          # -- Environment variables (optional, overrides S3 defaults entirely if specified)
          # env:
          #   - name: HUGGING_FACE_HUB_TOKEN
          #     value: "your-token"
          #   - name: MODEL_ID
          #     value: "meta-llama/Llama-2-7b"

      # -- Custom init containers (appended after wait-download-model if modelDownload is enabled)
      initContainers: []
      # Example for llm-d sidecar:
      # initContainers:
      #   - name: llm-d-routing-proxy
      #     image: ghcr.io/llm-d/llm-d-routing-sidecar:v0.2.0
      #     imagePullPolicy: IfNotPresent
      #     ports:
      #       - containerPort: 8080
      #         name: proxy
      #     securityContext:
      #       runAsUser: 1000

      # -- Path of the model on the s3 which hosts model weights and config files
      s3modelpath: "relative_s3_model_path/opt-125m"
      # -- Storage size for the PVC
      pvcStorage: "1Gi"
      # -- Disable AWS EC2 metadata service
      awsEc2MetadataDisabled: true

    # -- Additional containers configuration
    extraContainers: []

    # -- Readiness probe configuration
    readinessProbe:
      # -- Number of seconds after the container has started before readiness probe is initiated
      initialDelaySeconds: 5
      # -- How often (in seconds) to perform the readiness probe
      periodSeconds: 5
      # -- Number of times after which if a probe fails in a row, Kubernetes considers that the overall check has failed: the container is not ready
      failureThreshold: 3
       # -- Configuration of the Kubelet http request on the server
      httpGet:
        # -- Path to access on the HTTP server
        path: /health
        # -- Name or number of the port to access on the container, on which the server is listening
        port: 8000

    # -- Liveness probe configuration
    livenessProbe:
     # -- Number of seconds after the container has started before liveness probe is initiated
      initialDelaySeconds: 15
      # -- Number of times after which if a probe fails in a row, Kubernetes considers that the overall check has failed: the container is not alive
      failureThreshold: 3
      # -- How often (in seconds) to perform the liveness probe
      periodSeconds: 10
      # -- Configuration of the Kubelet http request on the server
      httpGet:
        # -- Path to access on the HTTP server
        path: /health
        # -- Name or number of the port to access on the container, on which the server is listening
        port: 8000

    labels:
      environment: "test"
      release: "test"