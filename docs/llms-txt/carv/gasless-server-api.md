# Source: https://docs.carv.io/carv-ecosystem/verifier-nodes/join-mainnet-verifier-nodes/operating-a-verifier-node/running-in-cli/gasless-server-api.md

# Gasless Server API

To minimize node operating costs, CARV offers official endpoints that assist node operators in batching operations and posting them on-chain. While gasless transactions still necessitate user signatures for specific operations, CARV ensures endpoint availability. However, if you are concerned about risks, you also have the option to independently send transactions to the smart contract.

**Base URLs: <https://interface.carv.io>**

### Message Construction

To make sure the gasless server still guarantee the authorization from the original node operater, it adopts the [EIP-712](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-712.md) standard to proof authorization through the signature.

For more details of message structure: <https://github.com/carv-protocol/verifier/blob/main/internal/worker/signature_server.go>

Example config: [#example-config](https://docs.carv.io/carv-ecosystem/verifier-nodes/join-mainnet-verifier-nodes/operating-a-verifier-node/using-docker#example-config "mention")

### POST ExplorerSendTxNodeEnter

`POST /explorer/send_tx_node_enter`

#### Message structure (Golang)

```json
typedData := apitypes.TypedData{
		Types: apitypes.Types{
			"EIP712Domain": {
				{
					Name: "name",
					Type: "string",
				},
				{
					Name: "version",
					Type: "string",
				},
				{
					Name: "chainId",
					Type: "uint256",
				},
			},
			"NodeEnterData": {
				{
					Name: "replacedNode",
					Type: "address",
				},
				{
					Name: "expiredAt",
					Type: "uint256",
				},
			},
		},
		PrimaryType: "NodeEnterData",
		Domain: apitypes.TypedDataDomain{
			Name:    c.cf.Signature.DomainName,
			Version: c.cf.Signature.DomainVersion,
			ChainId: (*math.HexOrDecimal256)(big.NewInt(c.cf.Chain.ChainId)),
		},
		Message: apitypes.TypedDataMessage{
			"replacedNode": replacedNode.String(),
			"expiredAt":    expiredAt,
		},
	}
```

#### Body Parameters

```json
{
  "signer": "0xb1878c4d1BAAbbB6abba3d77836cC85A80D5753B",
  "replaced_node": "0xb1878c4d1BAAbbB6abba3d77836cC85A80D5753B",
  "expired_at": 1000000000,
  "v": 27,
  "r": "ac0b5874f37c40838a33663da72cf90629a0164f98d7785736cc3fd96abeec67",
  "s": "10ba15d823cd831ef4061d474cc42d66933c6e45c2865b6d9c5f3646a2599b55",
  "version": "1.0.0"
}
```

#### Params

<table><thead><tr><th width="156">Name</th><th width="114">Location</th><th width="103">Type</th><th width="105">Required</th><th>Description</th></tr></thead><tbody><tr><td>Origin</td><td>header</td><td>string</td><td>yes</td><td></td></tr><tr><td>User-Agent</td><td>header</td><td>string</td><td>yes</td><td></td></tr><tr><td>x-app-id</td><td>header</td><td>string</td><td>yes</td><td></td></tr><tr><td>» signer</td><td>body</td><td>string</td><td>yes</td><td></td></tr><tr><td>» replaced_node</td><td>body</td><td>string</td><td>yes</td><td>The node to replace. There are 2000 active node limit. To join the active set you have to specify a node has lower delegation than you to replace with.</td></tr><tr><td>» expired_at</td><td>body</td><td>integer</td><td>yes</td><td></td></tr><tr><td>» v</td><td>body</td><td>integer</td><td>yes</td><td></td></tr><tr><td>» r</td><td>body</td><td>string</td><td>yes</td><td></td></tr><tr><td>» s</td><td>body</td><td>string</td><td>yes</td><td></td></tr></tbody></table>

#### Response Examples

200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {}
}
```

#### Responses

| HTTP Status Code | Meaning                                                          | Description     | Data schema |
| ---------------- | ---------------------------------------------------------------- | --------------- | ----------- |
| 200              | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)          | Success         | Inline      |
| 400              | [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1) | ResponseForFail | Inline      |

#### Responses Data Schema

HTTP Status Code **200**

| Name   | Type    | Required |
| ------ | ------- | -------- |
| » code | integer | true     |
| » msg  | string  | true     |
| » data | object  | true     |

HTTP Status Code **400**

| Name    | Type   | Required |
| ------- | ------ | -------- |
| » error | string | true     |

### POST ExplorerSendTxNodeExit

`POST /explorer/send_tx_node_exit`

#### Message structure (Golang)

```json
apitypes.TypedData{
		Types: apitypes.Types{
			"EIP712Domain": {
				{
					Name: "name",
					Type: "string",
				},
				{
					Name: "version",
					Type: "string",
				},
				{
					Name: "chainId",
					Type: "uint256",
				},
			},
			"NodeExitData": {
				{
					Name: "expiredAt",
					Type: "uint256",
				},
			},
		},
		PrimaryType: "NodeExitData",
		Domain: apitypes.TypedDataDomain{
			Name:    c.cf.Signature.DomainName,
			Version: c.cf.Signature.DomainVersion,
			ChainId: (*math.HexOrDecimal256)(big.NewInt(c.cf.Chain.ChainId)),
		},
		Message: apitypes.TypedDataMessage{
			"expiredAt": expiredAt,
		},
	}

	v, r, s, err := tools.SignTypedDataAndSplit(typedData, c.verifierPrivKey)
	if err != nil {
		return
	}

}
```

#### Body Parameters

```json
{
  "signer": "0xb1878c4d1BAAbbB6abba3d77836cC85A80D5753B",
  "expired_at": 1000000000,
  "v": 27,
  "r": "ac0b5874f37c40838a33663da72cf90629a0164f98d7785736cc3fd96abeec67",
  "s": "10ba15d823cd831ef4061d474cc42d66933c6e45c2865b6d9c5f3646a2599b55",
  "version": "1.0.0"
}
```

#### Params

| Name          | Location | Type    | Required |
| ------------- | -------- | ------- | -------- |
| Origin        | header   | string  | yes      |
| User-Agent    | header   | string  | yes      |
| x-app-id      | header   | string  | yes      |
| » signer      | body     | string  | yes      |
| » expired\_at | body     | integer | yes      |
| » v           | body     | integer | yes      |
| » r           | body     | string  | yes      |
| » s           | body     | string  | yes      |
| » version     | body     | string  | yes      |

#### Response Examples

200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {}
}
```

#### Responses

| HTTP Status Code | Meaning                                                          | Description     | Data schema |
| ---------------- | ---------------------------------------------------------------- | --------------- | ----------- |
| 200              | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)          | Success         | Inline      |
| 400              | [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1) | ResponseForFail | Inline      |

#### Responses Data Schema

HTTP Status Code **200**

| Name   | Type    | Required |
| ------ | ------- | -------- |
| » code | integer | true     |
| » msg  | string  | true     |
| » data | object  | true     |

HTTP Status Code **400**

| Name    | Type   | Required |
| ------- | ------ | -------- |
| » error | string | true     |

### POST ExplorerSendTxModifyCommissionRate

`POST /explorer/send_tx_modify_commission_rate`

#### Message structure (Golang)

```json
typedData := apitypes.TypedData{
		Types: apitypes.Types{
			"EIP712Domain": {
				{
					Name: "name",
					Type: "string",
				},
				{
					Name: "version",
					Type: "string",
				},
				{
					Name: "chainId",
					Type: "uint256",
				},
			},
			"NodeModifyCommissionRateData": {
				{
					Name: "commissionRate",
					Type: "uint32",
				},
				{
					Name: "expiredAt",
					Type: "uint256",
				},
			},
		},
		PrimaryType: "NodeModifyCommissionRateData",
		Domain: apitypes.TypedDataDomain{
			Name:    c.cf.Signature.DomainName,
			Version: c.cf.Signature.DomainVersion,
			ChainId: (*math.HexOrDecimal256)(big.NewInt(c.cf.Chain.ChainId)),
		},
		Message: apitypes.TypedDataMessage{
			"commissionRate": strconv.Itoa(int(commissionRate)),
			"expiredAt":      expiredAt,
		},
	}
```

#### Body Parameters

```json
{
  "signer": "0xb1878c4d1BAAbbB6abba3d77836cC85A80D5753B",
  "commission_rate": 100,
  "expired_at": 1000000000,
  "v": 27,
  "r": "ac0b5874f37c40838a33663da72cf90629a0164f98d7785736cc3fd96abeec67",
  "s": "10ba15d823cd831ef4061d474cc42d66933c6e45c2865b6d9c5f3646a2599b55",
  "version": "1.0.0"
}
```

#### Params

| Name               | Location | Type    | Required |
| ------------------ | -------- | ------- | -------- |
| Origin             | header   | string  | yes      |
| User-Agent         | header   | string  | yes      |
| x-app-id           | header   | string  | yes      |
| » signer           | body     | string  | yes      |
| » commission\_rate | body     | integer | yes      |
| » expired\_at      | body     | integer | yes      |
| » v                | body     | integer | yes      |
| » r                | body     | string  | yes      |
| » s                | body     | string  | yes      |

#### Response Examples

200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {}
}
```

#### Responses

| HTTP Status Code | Meaning                                                          | Description     | Data schema |
| ---------------- | ---------------------------------------------------------------- | --------------- | ----------- |
| 200              | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)          | Success         | Inline      |
| 400              | [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1) | ResponseForFail | Inline      |

#### Responses Data Schema

HTTP Status Code **200**

| Name   | Type    | Required |
| ------ | ------- | -------- |
| » code | integer | true     |
| » msg  | string  | true     |
| » data | object  | true     |

HTTP Status Code **400**

| Name    | Type   | Required |
| ------- | ------ | -------- |
| » error | string | true     |

### POST ExplorerSendTxSetRewardClaimer

`POST /explorer/send_tx_set_reward_claimer`

#### Message structure (Golang)

```json
typedData := apitypes.TypedData{
		Types: apitypes.Types{
			"EIP712Domain": {
				{
					Name: "name",
					Type: "string",
				},
				{
					Name: "version",
					Type: "string",
				},
				{
					Name: "chainId",
					Type: "uint256",
				},
			},
			"NodeSetRewardClaimerData": {
				{
					Name: "claimer",
					Type: "address",
				},
				{
					Name: "expiredAt",
					Type: "uint256",
				},
			},
		},
		PrimaryType: "NodeSetRewardClaimerData",
		Domain: apitypes.TypedDataDomain{
			Name:    c.cf.Signature.DomainName,
			Version: c.cf.Signature.DomainVersion,
			ChainId: (*math.HexOrDecimal256)(big.NewInt(c.cf.Chain.ChainId)),
		},
		Message: apitypes.TypedDataMessage{
			"claimer":   rewardClaimer.String(),
			"expiredAt": expiredAt,
		},
	}
```

#### Body Parameters

```json
{
  "signer": "0xb1878c4d1BAAbbB6abba3d77836cC85A80D5753B",
  "claimer": "0xb1878c4d1BAAbbB6abba3d77836cC85A80D5753B",
  "expired_at": 1000000000,
  "v": 27,
  "r": "ac0b5874f37c40838a33663da72cf90629a0164f98d7785736cc3fd96abeec67",
  "s": "10ba15d823cd831ef4061d474cc42d66933c6e45c2865b6d9c5f3646a2599b55",
  "version": "1.0.0"
}
```

#### Params

| Name          | Location | Type    | Required |
| ------------- | -------- | ------- | -------- |
| Origin        | header   | string  | yes      |
| User-Agent    | header   | string  | yes      |
| x-app-id      | header   | string  | yes      |
| body          | body     | object  | no       |
| » signer      | body     | string  | yes      |
| » claimer     | body     | string  | yes      |
| » expired\_at | body     | integer | yes      |
| » v           | body     | integer | yes      |
| » r           | body     | string  | yes      |
| » s           | body     | string  | yes      |

#### Response Examples

200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {}
}
```

#### Responses

| HTTP Status Code | Meaning                                                          | Description     | Data schema |
| ---------------- | ---------------------------------------------------------------- | --------------- | ----------- |
| 200              | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)          | Success         | Inline      |
| 400              | [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1) | ResponseForFail | Inline      |

#### Responses Data Schema

HTTP Status Code **200**

| Name   | Type    | Required |
| ------ | ------- | -------- |
| » code | integer | true     |
| » msg  | string  | true     |
| » data | object  | true     |

HTTP Status Code **400**

| Name    | Type   | Required |
| ------- | ------ | -------- |
| » error | string | true     |

### POST ExplorerSendTxNodeReportVerification

`POST /explorer/send_tx_node_report_verification`

#### Message structure (Golang)

```json
typedData := apitypes.TypedData{
		Types: apitypes.Types{
			"EIP712Domain": {
				{
					Name: "name",
					Type: "string",
				},
				{
					Name: "version",
					Type: "string",
				},
				{
					Name: "chainId",
					Type: "uint256",
				},
			},
			"VerificationData": {
				{
					Name: "attestationID",
					Type: "bytes32",
				},
				{
					Name: "result",
					Type: "uint8",
				},
				{
					Name: "index",
					Type: "uint32",
				},
			},
		},
		PrimaryType: "VerificationData",
		Domain: apitypes.TypedDataDomain{
			Name:    c.cf.Signature.DomainName,
			Version: c.cf.Signature.DomainVersion,
			ChainId: (*math.HexOrDecimal256)(big.NewInt(c.cf.Chain.ChainId)),
		},
		Message: apitypes.TypedDataMessage{
			"attestationID": attestationId[:],
			"result":        strconv.Itoa(int(result)),
			"index":         strconv.Itoa(int(index)),
		},
	}
```

#### Body Parameters

```json
{
  "signer": "0xb1878c4d1BAAbbB6abba3d77836cC85A80D5753B",
  "attestation_id": "0x518c1c43067238438f81546f39623c49b09a8eeeb0ee14794aafefd9fa84c7ab",
  "result": 0,
  "index": 1,
  "v": 27,
  "r": "ac0b5874f37c40838a33663da72cf90629a0164f98d7785736cc3fd96abeec67",
  "s": "10ba15d823cd831ef4061d474cc42d66933c6e45c2865b6d9c5f3646a2599b55",
  "version": "1.0.0"
}
```

#### Params

| Name              | Location | Type    | Required |
| ----------------- | -------- | ------- | -------- |
| Origin            | header   | string  | yes      |
| User-Agent        | header   | string  | yes      |
| x-app-id          | header   | string  | yes      |
| » signer          | body     | string  | yes      |
| » attestation\_id | body     | string  | yes      |
| » result          | body     | integer | yes      |
| » index           | body     | integer | yes      |
| » v               | body     | integer | yes      |
| » r               | body     | string  | yes      |
| » s               | body     | string  | yes      |

#### Response Examples

200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": null
}
```

#### Responses

| HTTP Status Code | Meaning                                                          | Description     | Data schema |
| ---------------- | ---------------------------------------------------------------- | --------------- | ----------- |
| 200              | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)          | Success         | Inline      |
| 400              | [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1) | ResponseForFail | Inline      |

#### Responses Data Schema

HTTP Status Code **200**

<table><thead><tr><th>Name</th><th>Type</th><th>Required</th><th data-hidden>Restrictions</th></tr></thead><tbody><tr><td>» code</td><td>integer</td><td>true</td><td>none</td></tr><tr><td>» msg</td><td>string</td><td>true</td><td>none</td></tr><tr><td>» data</td><td>null</td><td>true</td><td>none</td></tr></tbody></table>

HTTP Status Code **400**

| Name    | Type   | Required |
| ------- | ------ | -------- |
| » error | string | true     |
