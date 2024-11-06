from napalm import get_network_driver
import pprint

# Define the device information
driver = get_network_driver('nxos_ssh')
device = driver(hostname='192.168.64.71', username='admin', password='adminadmin', optional_args={'port': 22})

# Connect to the device
device.open()

# Retrieve and print device facts
facts = device.get_facts()
#pprint.pprint(facts)

interfaces = device.get_interfaces()
#pprint.pprint(interfaces['Ethernet1/1']['mac_address'])

get_config =device.get_config()
#pprint.pprint(get_config)

config_str = 'interface Ethernet 1/1\ndescription configured_by_python2'
device.load_merge_candidate(config=config_str)
print ('diff before config :')
print (device.compare_config())
device.commit_config()

# Close the connection
device.close()
