# Source: https://docs.akeyless.io/reference/gatewaygetremoteaccess.md

# /gateway-get-remote-access

# OpenAPI definition

```json
{
  "openapi": "3.0.0",
  "info": {
    "description": "The purpose of this application is to provide access to Akeyless API.",
    "title": "Akeyless API",
    "contact": {
      "name": "Akeyless",
      "url": "http://akeyless.io",
      "email": "support@akeyless.io"
    },
    "version": "3.0"
  },
  "paths": {
    "/gateway-get-remote-access": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "gatewayGetRemoteAccess",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/gatewayGetRemoteAccess"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/gatewayGetRemoteAccessResponse"
          },
          "default": {
            "$ref": "#/components/responses/errorResponse"
          }
        }
      }
    }
  },
  "servers": [
    {
      "url": "https://api.akeyless.io"
    }
  ],
  "components": {
    "responses": {
      "errorResponse": {
        "description": "errorResponse wraps any error to return it as a JSON object with one \"error\"\nfield.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/JSONError"
            }
          }
        }
      },
      "gatewayGetRemoteAccessResponse": {
        "description": "gatewayGetRemoteAccessResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/BastionConfigReplyObj"
            }
          }
        }
      }
    },
    "schemas": {
      "AwsAuthType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/log"
      },
      "AwsS3LogForwardingConfig": {
        "type": "object",
        "properties": {
          "aws_access_id": {
            "type": "string",
            "x-go-name": "AwsAccessId"
          },
          "aws_access_key": {
            "type": "string",
            "x-go-name": "AwsAccessKey"
          },
          "aws_auth_type": {
            "$ref": "#/components/schemas/AwsAuthType"
          },
          "aws_region": {
            "type": "string",
            "x-go-name": "AwsRegion"
          },
          "aws_role_arn": {
            "type": "string",
            "x-go-name": "AwsRoleARN"
          },
          "aws_use_gateway_cloud_identity": {
            "description": "deprecated",
            "type": "boolean",
            "x-go-name": "AwsUseGatewayCloudIdentity"
          },
          "bucket_name": {
            "type": "string",
            "x-go-name": "BucketName"
          },
          "log_folder": {
            "type": "string",
            "x-go-name": "LogFolder"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "AwsStorage": {
        "type": "object",
        "properties": {
          "access_key_id": {
            "description": "creds",
            "type": "string",
            "x-go-name": "AccessKeyId"
          },
          "access_key_secret": {
            "type": "string",
            "x-go-name": "AccessKeySecret"
          },
          "auth_type": {
            "type": "string",
            "x-go-name": "AuthType"
          },
          "bucket": {
            "type": "string",
            "x-go-name": "Bucket"
          },
          "prefix": {
            "type": "string",
            "x-go-name": "Prefix"
          },
          "region": {
            "type": "string",
            "x-go-name": "Region"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "AzureLogAnalyticsForwardingConfig": {
        "type": "object",
        "properties": {
          "azure_enable_batch": {
            "type": "string",
            "x-go-name": "AzureEnableBatch"
          },
          "azure_workspace_id": {
            "type": "string",
            "x-go-name": "AzureWorkspaceId"
          },
          "azure_workspace_key": {
            "type": "string",
            "x-go-name": "AzureWorkspaceKey"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "AzureStorage": {
        "type": "object",
        "properties": {
          "auth_type": {
            "type": "string",
            "x-go-name": "AuthType"
          },
          "client_id": {
            "type": "string",
            "x-go-name": "ClientID"
          },
          "client_secret": {
            "type": "string",
            "x-go-name": "ClientSecret"
          },
          "storage_account": {
            "type": "string",
            "x-go-name": "StorageAccount"
          },
          "storage_container_name": {
            "type": "string",
            "x-go-name": "StorageContainerName"
          },
          "tenant_id": {
            "description": "creds",
            "type": "string",
            "x-go-name": "TenantID"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "BastionConfigReplyObj": {
        "type": "object",
        "properties": {
          "cluster_id": {
            "type": "string",
            "x-go-name": "ClusterId"
          },
          "desktop_app": {
            "$ref": "#/components/schemas/SraDesktopAppConf"
          },
          "gator_cluster_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "GatorClusterId"
          },
          "global": {
            "$ref": "#/components/schemas/BastionGlobalConf"
          },
          "ssh_bastion": {
            "$ref": "#/components/schemas/SshBastionConf"
          },
          "web_bastion": {
            "$ref": "#/components/schemas/WebBastionConf"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "BastionGlobalConf": {
        "type": "object",
        "properties": {
          "allowed_bastion_urls": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AllowedBastionUrls"
          },
          "allowed_ssh_url": {
            "type": "string",
            "x-go-name": "AllowedSSHURL"
          },
          "default_session_ttl_minutes": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "DefaultSessionTTLMinutes"
          },
          "legacy_signing_alg": {
            "type": "boolean",
            "x-go-name": "LegacySigningAlg"
          },
          "rdp_username_sub_claim": {
            "type": "string",
            "x-go-name": "RdpUsernameSubClaim"
          },
          "ssh_username_sub_claim": {
            "type": "string",
            "x-go-name": "SSHUsernameSubClaim"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "DatadogForwardingConfig": {
        "type": "object",
        "properties": {
          "datadog_api_key": {
            "type": "string",
            "x-go-name": "DatadogApiKey"
          },
          "datadog_host": {
            "type": "string",
            "x-go-name": "DatadogHost"
          },
          "datadog_log_service": {
            "type": "string",
            "x-go-name": "DatadogLogService"
          },
          "datadog_log_source": {
            "type": "string",
            "x-go-name": "DatadogLogSource"
          },
          "datadog_log_tags": {
            "type": "string",
            "x-go-name": "DatadogLogTags"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "ElasticsearchLogForwardingConfig": {
        "type": "object",
        "properties": {
          "elasticsearch_api_key": {
            "type": "string",
            "x-go-name": "ElasticsearchApiKey"
          },
          "elasticsearch_auth_type": {
            "type": "string",
            "x-go-name": "ElasticsearchAuthType"
          },
          "elasticsearch_cloud_id": {
            "type": "string",
            "x-go-name": "ElasticsearchCloudId"
          },
          "elasticsearch_enable_tls": {
            "type": "boolean",
            "x-go-name": "ElasticsearchEnableTLS"
          },
          "elasticsearch_index": {
            "type": "string",
            "x-go-name": "ElasticsearchIndex"
          },
          "elasticsearch_nodes": {
            "type": "string",
            "x-go-name": "ElasticsearchNodes"
          },
          "elasticsearch_password": {
            "type": "string",
            "x-go-name": "ElasticsearchPassword"
          },
          "elasticsearch_server_type": {
            "type": "string",
            "x-go-name": "ElasticsearchServerType"
          },
          "elasticsearch_tls_certificate": {
            "type": "string",
            "x-go-name": "ElasticsearchTlsCertificate"
          },
          "elasticsearch_user_name": {
            "type": "string",
            "x-go-name": "ElasticsearchUserName"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "GoogleChronicleForwardingConfig": {
        "type": "object",
        "properties": {
          "customer_id": {
            "type": "string",
            "x-go-name": "CustomerID"
          },
          "log_type": {
            "type": "string",
            "x-go-name": "LogType"
          },
          "region": {
            "type": "string",
            "x-go-name": "Region"
          },
          "service_account_key": {
            "type": "string",
            "x-go-name": "ServiceAccountKey"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "JSONError": {
        "type": "object",
        "title": "JSONError wraps an error with JSON object.",
        "properties": {
          "error": {
            "type": "string",
            "x-go-name": "Err"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client"
      },
      "LogForwardingConfigPart": {
        "type": "object",
        "properties": {
          "aws_s3_config": {
            "$ref": "#/components/schemas/AwsS3LogForwardingConfig"
          },
          "azure_analytics_config": {
            "$ref": "#/components/schemas/AzureLogAnalyticsForwardingConfig"
          },
          "datadog_config": {
            "$ref": "#/components/schemas/DatadogForwardingConfig"
          },
          "elasticsearch_config": {
            "$ref": "#/components/schemas/ElasticsearchLogForwardingConfig"
          },
          "google_chronicle_config": {
            "$ref": "#/components/schemas/GoogleChronicleForwardingConfig"
          },
          "json_output": {
            "type": "boolean",
            "x-go-name": "JsonOutput"
          },
          "logan_enable": {
            "type": "boolean",
            "x-go-name": "LoganEnable"
          },
          "logan_url": {
            "type": "string",
            "x-go-name": "LoganURLConfig"
          },
          "logstash_config": {
            "$ref": "#/components/schemas/LogstashLogForwardingConfig"
          },
          "logz_io_config": {
            "$ref": "#/components/schemas/LogzIoLogForwardingConfig"
          },
          "pull_interval_sec": {
            "type": "string",
            "x-go-name": "PullIntervalSec"
          },
          "splunk_config": {
            "$ref": "#/components/schemas/SplunkLogForwardingConfig"
          },
          "sumo_logic_config": {
            "$ref": "#/components/schemas/SumologicLogForwardingConfig"
          },
          "syslog_config": {
            "$ref": "#/components/schemas/SyslogLogForwardingConfig"
          },
          "target_log_type": {
            "type": "string",
            "x-go-name": "TargetLogType"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "LogstashLogForwardingConfig": {
        "type": "object",
        "properties": {
          "logstash_dns": {
            "type": "string",
            "x-go-name": "LogstashDns"
          },
          "logstash_enable_tls": {
            "type": "boolean",
            "x-go-name": "LogstashEnableTLS"
          },
          "logstash_protocol": {
            "type": "string",
            "x-go-name": "LogstashProtocol"
          },
          "logstash_tls_certificate": {
            "type": "string",
            "x-go-name": "LogstashTlsCertificate"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "LogzIoLogForwardingConfig": {
        "type": "object",
        "properties": {
          "target_logz_io_protocol": {
            "type": "string",
            "x-go-name": "TargetLogzIoProtocol"
          },
          "target_logz_io_token": {
            "type": "string",
            "x-go-name": "TargetLogzIoToken"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "RecordStorageType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "RecordingQuality": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "SplunkLogForwardingConfig": {
        "type": "object",
        "properties": {
          "splunk_enable_batch": {
            "type": "string",
            "x-go-name": "SplunkEnableBatch"
          },
          "splunk_enable_tls": {
            "type": "boolean",
            "x-go-name": "SplunkEnableTLS"
          },
          "splunk_index": {
            "type": "string",
            "x-go-name": "SplunkIndex"
          },
          "splunk_source": {
            "type": "string",
            "x-go-name": "SplunkSource"
          },
          "splunk_sourcetype": {
            "type": "string",
            "x-go-name": "SplunkSourcetype"
          },
          "splunk_tls_certificate": {
            "type": "string",
            "x-go-name": "SplunkTlsCertificate"
          },
          "splunk_token": {
            "type": "string",
            "x-go-name": "SplunkToken"
          },
          "splunk_url": {
            "type": "string",
            "x-go-name": "SplunkUrl"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "SraDesktopAppConf": {
        "type": "object",
        "properties": {
          "default_cert_issuer_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "DefaultCertIssuerId"
          },
          "secure_web_access_url": {
            "type": "string",
            "x-go-name": "SecureWebAccessUrl"
          },
          "secure_web_proxy_url": {
            "type": "string",
            "x-go-name": "SecureWebProxyUrl"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "SshBastionConf": {
        "type": "object",
        "properties": {
          "hide_session_recording": {
            "type": "boolean",
            "x-go-name": "HideSessionRecording"
          },
          "kexalgs": {
            "type": "string",
            "x-go-name": "Kexalgs"
          },
          "log_forwarding": {
            "$ref": "#/components/schemas/LogForwardingConfigPart"
          },
          "session_termination": {
            "$ref": "#/components/schemas/SshBastionSessionTermination"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "SshBastionSessionTermination": {
        "type": "object",
        "properties": {
          "api_password": {
            "type": "string",
            "x-go-name": "ApiPassword"
          },
          "api_token": {
            "type": "string",
            "x-go-name": "ApiToken"
          },
          "api_url": {
            "type": "string",
            "x-go-name": "ApiUrl"
          },
          "api_username": {
            "type": "string",
            "x-go-name": "ApiUsername"
          },
          "enabled": {
            "type": "boolean",
            "x-go-name": "Enabled"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "SumologicLogForwardingConfig": {
        "type": "object",
        "properties": {
          "sumo_logic_endpoint": {
            "type": "string",
            "x-go-name": "SumologicEndPointURL"
          },
          "sumo_logic_host": {
            "type": "string",
            "x-go-name": "SumologicHost"
          },
          "sumo_logic_tags": {
            "type": "string",
            "x-go-name": "SumologicTags"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "SyslogLogForwardingConfig": {
        "type": "object",
        "properties": {
          "syslog_enable_tls": {
            "type": "boolean",
            "x-go-name": "SyslogEnableTLS"
          },
          "syslog_formatter": {
            "type": "string",
            "x-go-name": "SyslogFormatter"
          },
          "syslog_host": {
            "type": "string",
            "x-go-name": "SyslogHost"
          },
          "syslog_network": {
            "type": "string",
            "x-go-name": "SyslogNetwork"
          },
          "syslog_target_tag": {
            "type": "string",
            "x-go-name": "SyslogTargetTag"
          },
          "syslog_tls_certificate": {
            "type": "string",
            "x-go-name": "SyslogTlsCertificate"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "WebBastionConf": {
        "type": "object",
        "properties": {
          "guacamole": {
            "$ref": "#/components/schemas/WebBastionGuacamole"
          },
          "rdp_record": {
            "$ref": "#/components/schemas/WebBastionRdpRecord"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "WebBastionGuacamole": {
        "type": "object",
        "properties": {
          "keyboard_layout": {
            "type": "string",
            "x-go-name": "KeyboardLayout"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "WebBastionRdpRecord": {
        "type": "object",
        "properties": {
          "aws": {
            "$ref": "#/components/schemas/AwsStorage"
          },
          "azure": {
            "$ref": "#/components/schemas/AzureStorage"
          },
          "compress": {
            "type": "boolean",
            "x-go-name": "Compress"
          },
          "encryption_key": {
            "type": "string",
            "x-go-name": "EncryptionKey"
          },
          "recording_quality": {
            "$ref": "#/components/schemas/RecordingQuality"
          },
          "storage_type": {
            "$ref": "#/components/schemas/RecordStorageType"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "gatewayGetRemoteAccess": {
        "description": "gatewayGetRemoteAccess is a command that returns remote access config",
        "type": "object",
        "properties": {
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "token": {
            "description": "Authentication token (see `/auth` and `/configure`)",
            "type": "string",
            "x-go-name": "Profile"
          },
          "uid-token": {
            "description": "The universal identity token, Required only for universal_identity authentication",
            "type": "string",
            "x-go-name": "UIDToken"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```