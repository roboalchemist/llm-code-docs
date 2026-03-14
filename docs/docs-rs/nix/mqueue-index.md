nix

# Module mqueue

Source Available on **crate feature `mqueue`** only.

## Structs§

MQ_OFlagUsed with `mq_open`.MqAttrA message-queue attribute, optionally used with `mq_setattr` and
`mq_getattr` and optionally `mq_open`,MqdTIdentifies an open POSIX Message Queue

## Functions§

mq_closeClose a message queuemq_getattrGet message queue attributesmq_openOpen a message queuemq_receiveReceive a message from a message queuemq_remove_nonblockConvenience function.
Removes `O_NONBLOCK` attribute for a given message queue descriptor
Returns the old attributesmq_sendSend a message to a message queuemq_set_nonblockConvenience function.
Sets the `O_NONBLOCK` attribute for a given message queue descriptor
Returns the old attributesmq_setattrSet the attributes of the message queue. Only `O_NONBLOCK` can be set,
everything else will be ignored. Returns the old attributes.mq_timedreceive`time`Receive a message from a message queue with a timeoutmq_unlinkRemove a message queue

## Type Aliases§

mq_attr_member_tNot (x86-64 and 32-bit)Size of a message queue attribute member
