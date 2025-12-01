# Namecheap API: Domains Ns Update

Source: https://github.com/namecheap/go-namecheap-sdk/blob/master/namecheap/domains_ns_update.go



## Type: NameserversUpdateResponse

```go
type NameserversUpdateResponse struct {
	XMLName *xml.Name `xml:"ApiResponse"`
	Errors  *[]struct {
		Message *string `xml:",chardata"`
		Number  *string `xml:"Number,attr"`
	} `xml:"Errors>Error"`
	CommandResponse *NameserversCreateCommandResponse `xml:"CommandResponse"`
}

## Type: NameserversUpdateCommandResponse

```go
type NameserversUpdateCommandResponse struct {
	DomainNameserverUpdateResult *DomainsNSUpdateResult `xml:"DomainNSUpdateResult"`
}

## Type: DomainsNSUpdateResult

```go
type DomainsNSUpdateResult struct {
	Domain     *string `xml:"Domain,attr"`
	Nameserver *string `xml:"Nameserver,attr"`
	IsSuccess  *bool   `xml:"IsSuccess,attr"`
}

## Method: DomainsNSService.Update

```go
func (s *DomainsNSService) Update(sld, tld, nameserver, oldIP, ip string) (*NameserversCreateCommandResponse, error) {
	var response NameserversUpdateResponse

	params := map[string]string{
		"Command":    "namecheap.domains.ns.update",
		"SLD":        sld,
		"TLD":        tld,
		"Nameserver": nameserver,
		"OldIP":      oldIP,
		"IP":         ip,
	}

	_, err := s.client.DoXML(params, &response)
	if err != nil {
		return nil, err
	}

	if response.Errors != nil && len(*response.Errors) > 0 {
		apiErr := (*response.Errors)[0]
		return nil, fmt.Errorf("%s (%s)", *apiErr.Message, *apiErr.Number)
	}

	return response.CommandResponse, nil
}
