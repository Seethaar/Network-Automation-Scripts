from concurrent.futures import ThreadPoolExecutor
from my_functions import ssh_command2
from my_devices import device_list
import time
starttime = time.time()
pool = ThreadPoolExecutor()
def wrapper(device):
    output = ssh_command2(device,'show version')
    return output

cmd_list = []
for item in device_list:
    cmd_list.append('show version')

results_gen = pool.map(ssh_command2,device_list,cmd_list)

for result in results_gen:
    print('#'*30)
    print(result)
    print('#'*30)
endtime = time.time()
print(f"Finished in {endtime - starttime}")
