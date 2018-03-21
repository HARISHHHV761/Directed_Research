#IOT_TestBed_Enhancement

The main objective is to deploy the IOT devices (IoTSC) around the campus to collect data from various sensors wirelessly over MQTT protocol. It provides a very large scale infrastructure suitable for testing small wireless sensor devices and heterogeneous communicating objects. It also enables full control of network nodes and direct access to the gateways to which nodes are connected, allowing us to monitor nodes energy consumption and network-related metrics. Once the data is collected at the server, the runtime visualization of the data can be witnessed.

The current code focusses on the following implementations:
1. Setting up the database on the server and storing the configuration settings of all the MQTT clients.
2. Making the database event driven to enable the MQTT clients to read the configuration setting and applying it in run time.
