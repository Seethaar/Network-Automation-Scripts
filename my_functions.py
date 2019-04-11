from netmiko import ConnectHandler

def ssh_command(device,command):
    instance  = ConnectHandler(**device)
    output = instance.send_command(command)
    instance.disconnect()
    print('#'*30)
    print('The version of {}'.format(device.get('host')))
    print('_'*30)
    print(output)
    print('#'*30)

def ssh_command2(device,command):
    instance  = ConnectHandler(**device)
    output = instance.send_command(command)
    instance.disconnect()
    return output
