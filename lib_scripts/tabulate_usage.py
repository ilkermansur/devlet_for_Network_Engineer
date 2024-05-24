from tabulate import tabulate

devices = {
    'data' : [
        {
            'hostname' : 'RT_A',
            'ip_addr' : '1.1.1.1'
         },
         {
            'hostname' : 'RT_B',
            'ip_addr' : '1.1.1.2' 
         }
    ]
}
table = []
headers = ['Hostname', 'ip_addr']

for item in devices['data']:
    tab_row = [item['hostname'],item['ip_addr']]
    table.append(tab_row)

graph = tabulate (table,headers)

print (graph)