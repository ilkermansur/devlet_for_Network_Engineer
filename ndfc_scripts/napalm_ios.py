from napalm import get_network_driver
import pprint

ios_driver = get_network_driver('ios')
ios_config = {
    'hostname' : '192.168.71.183',
    'username' : 'cisco',
    'password' : 'cisco1',
    'optional_args' : {
        'port' : 22
    }
}

connection = ios_driver(**ios_config)

# Method of 'CLI' uses for SHOW commands
connection.open()

commands = ['show ip int brief', 'show version']
config_ios = connection.cli(commands)
connection.close()
#pprint.pprint (config_ios)

# For import Config, you should use ''
connection.open()
command_str = 'interface GigabitEthernet5\ndescription configured_by_PYTHON'
config_ios2 = connection.load_merge_candidate(config=command_str)
connection.commit_config()
output_config = connection.get_interfaces()
connection.close()
pprint.pprint(output_config)





