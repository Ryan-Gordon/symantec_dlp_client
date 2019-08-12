# Symantec DLP Client

A Python package which can be used to interface with the Incident and Reporting API for Symantec DLP. 

The Incident and Reporting API for Symantec DLP is SOAP based, when I got started I could only find Java and C# clients. 

I wanted to open source this package as when I initially went looking there very little python resources for this project. Ideally, we will make this package great through PR's which solve 

# Installation 
Using this package should be fairly straightforward. Install it from pypi and import it like so : 

`from symantec_dlp_client.dlp_soap_client import DLPSoapClient`

From there you'll need to pass a few config values to the Init of DLPSoapClient. Check the bottom of the file for an example of what needs to be passed.
The project uses zeep to handle all the soap calls and returns a Zeep Object/Type which resembles the return type found in the docs. 

If you prefer to work with JSON, there is a part of zeep called serialize_object which you can use to convert the return type to JSON.

```
from zeep.helpers import serialize_object
serialize_object(response)
```

