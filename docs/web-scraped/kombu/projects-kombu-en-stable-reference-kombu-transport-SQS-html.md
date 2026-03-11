# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html

Title: Amazon SQS Transport - kombu.transport.SQS — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.transport.SQS.html).

Amazon SQS transport module for Kombu.

This package implements an AMQP-like interface on top of Amazons SQS service, with the goal of being optimized for high performance and reliability.

The default settings for this module are focused now on high performance in task queue situations where tasks are small, idempotent and run very fast.

[SQS Features supported by this transport](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#id3)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#sqs-features-supported-by-this-transport "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Long Polling](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#id4)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#long-polling "Link to this heading")

[https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-long-polling.html](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-long-polling.html)

Long polling is enabled by setting the wait_time_seconds transport option to a number > 1. Amazon supports up to 20 seconds. This is enabled with 10 seconds by default.

### [Batch API Actions](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#id5)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#batch-api-actions "Link to this heading")

[https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-batch-api.html](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-batch-api.html)

The default behavior of the SQS Channel.drain_events() method is to request up to the ‘prefetch_count’ messages on every request to SQS. These messages are stored locally in a deque object and passed back to the Transport until the deque is empty, before triggering a new API call to Amazon.

This behavior dramatically speeds up the rate that you can pull tasks from SQS when you have short-running tasks (or a large number of workers).

When a Celery worker has multiple queues to monitor, it will pull down up to ‘prefetch_count’ messages from queueA and work on them all before moving on to queueB. If queueB is empty, it will wait up until ‘polling_interval’ expires before moving back and checking on queueA.

### [Message Attributes](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#id6)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#message-attributes "Link to this heading")

[https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-metadata.html](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-metadata.html)

SQS supports sending message attributes along with the message body. To use this feature, you can pass a ‘message_attributes’ as keyword argument to basic_publish method.

[Other Features supported by this transport](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#id7)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#other-features-supported-by-this-transport "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Predefined Queues](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#id8)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#predefined-queues "Link to this heading")

The default behavior of this transport is to use a single AWS credential pair in order to manage all SQS queues (e.g. listing queues, creating queues, polling queues, deleting messages).

If it is preferable for your environment to use multiple AWS credentials, you can use the ‘predefined_queues’ setting inside the ‘transport_options’ map. This setting allows you to specify the SQS queue URL and AWS credentials for each of your queues. For example, if you have two queues which both already exist in AWS) you can tell this transport about them as follows:

transport_options = {
  'predefined_queues': {
    'queue-1': {
      'url': 'https://sqs.us-east-1.amazonaws.com/xxx/aaa',
      'access_key_id': 'a',
      'secret_access_key': 'b',
      'backoff_policy': {1: 10, 2: 20, 3: 40, 4: 80, 5: 320, 6: 640}, # optional
      'backoff_tasks': ['svc.tasks.tasks.task1'] # optional
    },
    'queue-2.fifo': {
      'url': 'https://sqs.us-east-1.amazonaws.com/xxx/bbb.fifo',
      'access_key_id': 'c',
      'secret_access_key': 'd',
      'backoff_policy': {1: 10, 2: 20, 3: 40, 4: 80, 5: 320, 6: 640}, # optional
      'backoff_tasks': ['svc.tasks.tasks.task2'] # optional
    },
  }
'sts_role_arn': 'arn:aws:iam::<xxx>:role/STSTest', # optional
'sts_token_timeout': 900, # optional
'sts_token_buffer_time': 0, # optional, added in 5.6.0
}

Note that FIFO and standard queues must be named accordingly (the name of a FIFO queue must end with the .fifo suffix).

backoff_policy & backoff_tasks are optional arguments. These arguments automatically change the message visibility timeout, in order to have different times between specific task retries. This would apply after task failure.

AWS STS authentication is supported, by using sts_role_arn, and sts_token_timeout. sts_role_arn is the assumed IAM role ARN we are trying to access with. sts_token_timeout is the token timeout, defaults (and minimum) to 900 seconds. After the mentioned period, a new token will be created.

Added in version 5.6.0: sts_token_buffer_time (seconds) is the time by which you want to refresh your token earlier than its actual expiration time, defaults to 0 (no time buffer will be added), should be less than sts_token_timeout.

If you authenticate using [Okta](https://www.okta.com/) (e.g. calling [`gimme-aws-creds`](https://github.com/Nike-Inc/gimme-aws-creds#readme)), you can also specify a ‘session_token’ to connect to a queue. Note that those tokens have a limited lifetime and are therefore only suited for short-lived tests.

### [Client config](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#id9)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#client-config "Link to this heading")

In some cases you may need to override the botocore config. You can do it as follows:

transport_option = {
  'client-config': {
      'connect_timeout': 5,
   },
}

For a complete list of settings you can adjust using this option see [https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html](https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html)

[Features](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#id10)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#features "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   Type: Virtual

*   Supports Direct: Yes

*   Supports Topic: Yes

*   Supports Fanout: Yes

*   Supports Priority: No

*   Supports TTL: No

*   [SQS Features supported by this transport](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#sqs-features-supported-by-this-transport)

    *   [Long Polling](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#long-polling)

    *   [Batch API Actions](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#batch-api-actions)

    *   [Message Attributes](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#message-attributes)

*   [Other Features supported by this transport](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#other-features-supported-by-this-transport)

    *   [Predefined Queues](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#predefined-queues)

    *   [Client config](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#client-config)

*   [Features](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#features)

*   [Transport](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#transport)

*   [Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#channel)

*   [Back-off policy](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#back-off-policy)

*   [Message Attributes](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#id2)

[Transport](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#id11)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#transport "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.SQS.Transport(_client_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/SQS.html#Transport)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport "Link to this definition")
SQS Transport.

Additional queue attributes can be supplied to SQS during queue creation by passing an `sqs-creation-attributes` key in transport_options. `sqs-creation-attributes` must be a dict whose key-value pairs correspond with Attributes in the [CreateQueue SQS API](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_CreateQueue.html#API_CreateQueue_RequestParameters).

For example, to have SQS queues created with server-side encryption enabled using the default Amazon Managed Customer Master Key, you can set `KmsMasterKeyId` Attribute. When the queue is initially created by Kombu, encryption will be enabled.

from kombu.transport.SQS import Transport

transport = Transport(
    ...,
    transport_options={
        'sqs-creation-attributes': {
            'KmsMasterKeyId': 'alias/aws/sqs',
        },
    }
)

Added in version 5.6.

Queue tags can be applied to SQS queues during creation by passing an `queue_tags` key in transport_options. `queue_tags` must be a dict of tag key-value pairs.

from kombu.transport.SQS import Transport

transport = Transport(
    ...,
    transport_options={
        'queue_tags': {
            'Environment': 'production',
            'Team': 'backend',
        },
    }
)

The `ApproximateReceiveCount` message attribute is fetched by this transport by default. Requested message attributes can be changed by setting `fetch_message_attributes` in the transport options.

from kombu.transport.SQS import Transport

transport = Transport(
    ...,
    transport_options={
        'fetch_message_attributes': ["All"],  # Get all of the MessageSystemAttributeNames (formerly AttributeNames)
    }
)
# Preferred - A dict specifying system and custom message attributes
transport = Transport(
    ...,
    transport_options={
        'fetch_message_attributes': {
            'MessageSystemAttributeNames': ["SenderId", "SentTimestamp"],
            'MessageAttributeNames': ['S3MessageBodyKey']
        },
    }
)

_class_ Channel(_*args_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.Channel "Link to this definition")
SQS Channel.

B64_REGEX _=re.compile(b'^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$')_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.Channel.B64_REGEX "Link to this definition")_class_ QoS(_channel_, _prefetch\_count=0_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.Channel.QoS "Link to this definition")
Quality of Service guarantees implementation for SQS.

apply_backoff_policy(_routing\_key_, _delivery\_tag_, _backoff\_policy_, _backoff\_tasks_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.Channel.QoS.apply_backoff_policy "Link to this definition")extract_task_name_and_number_of_retries(_delivery\_tag_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.Channel.QoS.extract_task_name_and_number_of_retries "Link to this definition")reject(_delivery\_tag_, _requeue=False_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.Channel.QoS.reject "Link to this definition")
Remove from transactional state and requeue message.

asynsqs(_queue=None_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.Channel.asynsqs "Link to this definition")basic_ack(_delivery\_tag_, _multiple=False_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.Channel.basic_ack "Link to this definition")
Acknowledge message.

basic_cancel(_consumer\_tag_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.Channel.basic_cancel "Link to this definition")
Cancel consumer by consumer tag.

basic_consume(_queue_, _no\_ack_, _*args_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.Channel.basic_consume "Link to this definition")
Consume from queue.

canonical_queue_name(_queue\_name_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.Channel.canonical_queue_name "Link to this definition")close()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.Channel.close "Link to this definition")
Close channel.

Cancel all consumers, and requeue unacked messages.

_property_ conninfo[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.Channel.conninfo "Link to this definition")default_region _='us-east-1'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.Channel.default_region "Link to this definition")default_visibility_timeout _=1800_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.Channel.default_visibility_timeout "Link to this definition")default_wait_time_seconds _=10_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.Channel.default_wait_time_seconds "Link to this definition")domain_format _='kombu%(vhost)s'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.Channel.domain_format "Link to this definition")drain_events(_timeout=None_, _callback=None_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.Channel.drain_events "Link to this definition")
Return a single payload message from one of our queues.

Raises:
**Queue.Empty** – if no messages available.:

_property_ endpoint_url[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.Channel.endpoint_url "Link to this definition")entity_name(_name_, _table={33:95,34:95,35:95,36:95,37:95,38:95,39:95,40:95,41:95,42:95,43:95,44:95,46:45,47:95,58:95,59:95,60:95,61:95,62:95,63:95,64:95,91:95,92:95,93:95,94:95,96:95,123:95,124:95,125:95,126:95}_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.Channel.entity_name "Link to this definition")
Format AMQP queue name into a legal SQS queue name.

_property_ fetch_message_attributes[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.Channel.fetch_message_attributes "Link to this definition")generate_sts_session_token(_role\_arn_, _token\_expiry\_seconds_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.Channel.generate_sts_session_token "Link to this definition")generate_sts_session_token_with_buffer(_role\_arn_, _token\_expiry\_seconds_, _token\_buffer\_seconds=0_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.Channel.generate_sts_session_token_with_buffer "Link to this definition")
Generate STS session credentials with an optional expiration buffer.

The buffer is only applied if it is less than token_expiry_seconds to prevent an expired token.

_property_ get_message_attributes _:[dict](https://docs.python.org/dev/library/stdtypes.html#dict "(in Python v3.15)")[[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)"),[Any](https://docs.python.org/dev/library/typing.html#typing.Any "(in Python v3.15)")]_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.Channel.get_message_attributes "Link to this definition")
Get the message attributes to be fetched from SQS.

Ensures ‘ApproximateReceiveCount’ is included in system attributes if list is provided. - The number of retries is managed by SQS /

> (specifically by the `ApproximateReceiveCount` message attribute)

*   See: class QoS(virtual.QoS):
(method) def extract_task_name_and_number_of_retries

Returns:
A dictionary with SQS message attribute fetch config.

_property_ is_secure[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.Channel.is_secure "Link to this definition")new_sqs_client(_region_, _access\_key\_id_, _secret\_access\_key_, _session\_token=None_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.Channel.new_sqs_client "Link to this definition")_property_ port[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.Channel.port "Link to this definition")_property_ predefined_queues[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.Channel.predefined_queues "Link to this definition")
Map of queue_name to predefined queue settings.

_property_ queue_name_prefix[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.Channel.queue_name_prefix "Link to this definition")_property_ region[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.Channel.region "Link to this definition")_property_ regioninfo[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.Channel.regioninfo "Link to this definition")sqs(_queue=None_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.Channel.sqs "Link to this definition")_property_ sqs_base64_encoding[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.Channel.sqs_base64_encoding "Link to this definition")_property_ supports_fanout[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.Channel.supports_fanout "Link to this definition")
bool(x) -> bool

Returns True when the argument x is true, False otherwise. The builtins True and False are the only two instances of the class bool. The class bool is a subclass of the class int, and cannot be subclassed.

_property_ transport_options[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.Channel.transport_options "Link to this definition")_property_ visibility_timeout[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.Channel.visibility_timeout "Link to this definition")_property_ wait_time_seconds _:[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.Channel.wait_time_seconds "Link to this definition")channel_errors _=(<class'amqp.exceptions.ChannelError'>,<class'botocore.exceptions.BotoCoreError'>)_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.channel_errors "Link to this definition")
Tuple of errors that can happen due to channel/method failure.

connection_errors _=(<class'amqp.exceptions.ConnectionError'>,<class'botocore.exceptions.BotoCoreError'>,<class'OSError'>)_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.connection_errors "Link to this definition")
Tuple of errors that can happen due to connection failure.

_property_ default_connection_params[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.default_connection_params "Link to this definition")default_port _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.default_port "Link to this definition")
port number used when no port is specified.

driver_name _='sqs'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.driver_name "Link to this definition")
Name of driver library (e.g. ‘py-amqp’, ‘redis’).

driver_type _='sqs'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.driver_type "Link to this definition")
Type of driver, can be used to separate transports using the AMQP protocol (driver_type: ‘amqp’), Redis (driver_type: ‘redis’), etc…

implements _={'asynchronous':True,'exchange\_type':frozenset({'direct'}),'heartbeats':False}_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.implements "Link to this definition")polling_interval _=1_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.polling_interval "Link to this definition")
Time to sleep between unsuccessful polls.

wait_time_seconds _=0_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Transport.wait_time_seconds "Link to this definition")
[Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#id12)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#channel "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.SQS.Channel(_*args_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/SQS.html#Channel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Channel "Link to this definition")
SQS Channel.

B64_REGEX _=re.compile(b'^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$')_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Channel.B64_REGEX "Link to this definition")_class_ QoS(_channel_, _prefetch\_count=0_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Channel.QoS "Link to this definition")
Quality of Service guarantees implementation for SQS.

apply_backoff_policy(_routing\_key_, _delivery\_tag_, _backoff\_policy_, _backoff\_tasks_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Channel.QoS.apply_backoff_policy "Link to this definition")extract_task_name_and_number_of_retries(_delivery\_tag_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Channel.QoS.extract_task_name_and_number_of_retries "Link to this definition")reject(_delivery\_tag_, _requeue=False_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Channel.QoS.reject "Link to this definition")
Remove from transactional state and requeue message.

asynsqs(_queue=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/SQS.html#Channel.asynsqs)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Channel.asynsqs "Link to this definition")basic_ack(_delivery\_tag_, _multiple=False_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/SQS.html#Channel.basic_ack)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Channel.basic_ack "Link to this definition")
Acknowledge message.

basic_cancel(_consumer\_tag_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/SQS.html#Channel.basic_cancel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Channel.basic_cancel "Link to this definition")
Cancel consumer by consumer tag.

basic_consume(_queue_, _no\_ack_, _*args_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/SQS.html#Channel.basic_consume)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Channel.basic_consume "Link to this definition")
Consume from queue.

canonical_queue_name(_queue\_name_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/SQS.html#Channel.canonical_queue_name)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Channel.canonical_queue_name "Link to this definition")close()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/SQS.html#Channel.close)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Channel.close "Link to this definition")
Close channel.

Cancel all consumers, and requeue unacked messages.

_property_ conninfo[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Channel.conninfo "Link to this definition")default_region _='us-east-1'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Channel.default_region "Link to this definition")default_visibility_timeout _=1800_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Channel.default_visibility_timeout "Link to this definition")default_wait_time_seconds _=10_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Channel.default_wait_time_seconds "Link to this definition")domain_format _='kombu%(vhost)s'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Channel.domain_format "Link to this definition")drain_events(_timeout=None_, _callback=None_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/SQS.html#Channel.drain_events)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Channel.drain_events "Link to this definition")
Return a single payload message from one of our queues.

Raises:
**Queue.Empty** – if no messages available.:

_property_ endpoint_url[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Channel.endpoint_url "Link to this definition")entity_name(_name_, _table={33:95,34:95,35:95,36:95,37:95,38:95,39:95,40:95,41:95,42:95,43:95,44:95,46:45,47:95,58:95,59:95,60:95,61:95,62:95,63:95,64:95,91:95,92:95,93:95,94:95,96:95,123:95,124:95,125:95,126:95}_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/SQS.html#Channel.entity_name)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Channel.entity_name "Link to this definition")
Format AMQP queue name into a legal SQS queue name.

_property_ fetch_message_attributes[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Channel.fetch_message_attributes "Link to this definition")generate_sts_session_token(_role\_arn_, _token\_expiry\_seconds_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/SQS.html#Channel.generate_sts_session_token)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Channel.generate_sts_session_token "Link to this definition")generate_sts_session_token_with_buffer(_role\_arn_, _token\_expiry\_seconds_, _token\_buffer\_seconds=0_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/SQS.html#Channel.generate_sts_session_token_with_buffer)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Channel.generate_sts_session_token_with_buffer "Link to this definition")
Generate STS session credentials with an optional expiration buffer.

The buffer is only applied if it is less than token_expiry_seconds to prevent an expired token.

_property_ get_message_attributes _:[dict](https://docs.python.org/dev/library/stdtypes.html#dict "(in Python v3.15)")[[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)"),[Any](https://docs.python.org/dev/library/typing.html#typing.Any "(in Python v3.15)")]_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Channel.get_message_attributes "Link to this definition")
Get the message attributes to be fetched from SQS.

Ensures ‘ApproximateReceiveCount’ is included in system attributes if list is provided. - The number of retries is managed by SQS /

> (specifically by the `ApproximateReceiveCount` message attribute)

*   See: class QoS(virtual.QoS):
(method) def extract_task_name_and_number_of_retries

Returns:
A dictionary with SQS message attribute fetch config.

_property_ is_secure[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Channel.is_secure "Link to this definition")new_sqs_client(_region_, _access\_key\_id_, _secret\_access\_key_, _session\_token=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/SQS.html#Channel.new_sqs_client)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Channel.new_sqs_client "Link to this definition")_property_ port[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Channel.port "Link to this definition")_property_ predefined_queues[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Channel.predefined_queues "Link to this definition")
Map of queue_name to predefined queue settings.

_property_ queue_name_prefix[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Channel.queue_name_prefix "Link to this definition")_property_ region[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Channel.region "Link to this definition")_property_ regioninfo[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Channel.regioninfo "Link to this definition")sqs(_queue=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/SQS.html#Channel.sqs)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Channel.sqs "Link to this definition")_property_ sqs_base64_encoding[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Channel.sqs_base64_encoding "Link to this definition")_property_ supports_fanout[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Channel.supports_fanout "Link to this definition")
bool(x) -> bool

Returns True when the argument x is true, False otherwise. The builtins True and False are the only two instances of the class bool. The class bool is a subclass of the class int, and cannot be subclassed.

_property_ transport_options[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Channel.transport_options "Link to this definition")_property_ visibility_timeout[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Channel.visibility_timeout "Link to this definition")_property_ wait_time_seconds _:[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#kombu.transport.SQS.Channel.wait_time_seconds "Link to this definition")
[Back-off policy](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#id13)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#back-off-policy "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Back-off policy is using SQS visibility timeout mechanism altering the time difference between task retries. The mechanism changes message specific `visibility timeout` from queue `Default visibility timeout` to policy configured timeout. The number of retries is managed by SQS (specifically by the `ApproximateReceiveCount` message attribute) and no further action is required by the user.

Configuring the queues and backoff policy:

broker_transport_options = {
    'predefined_queues': {
        'my-q': {
            'url': 'https://ap-southeast-2.queue.amazonaws.com/123456/my-q',
            'access_key_id': 'xxx',
            'secret_access_key': 'xxx',
            'backoff_policy': {1: 10, 2: 20, 3: 40, 4: 80, 5: 320, 6: 640},
            'backoff_tasks': ['svc.tasks.tasks.task1']
        }
    }
}

`backoff_policy` dictionary where key is number of retries, and value is delay seconds between retries (i.e SQS visibility timeout) `backoff_tasks` list of task names to apply the above policy

The above policy:

**Attempt****Delay**
`2nd attempt`20 seconds
`3rd attempt`40 seconds
`4th attempt`80 seconds
`5th attempt`320 seconds
`6th attempt`640 seconds

[Message Attributes](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#id14)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SQS.html#id2 "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

SQS supports sending message attributes along with the message body. To use this feature, you can pass a ‘message_attributes’ as keyword argument to basic_publish method.
