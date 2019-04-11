from concurrent.futures import ThreadPoolExecutor,as_completed
from my_functions import ssh_command2
from my_devices import device_list
import time
starttime = time.time()
pool = ThreadPoolExecutor()
futures = []
for device in device_list:
    futures.append(pool.submit(ssh_command2,device,'show version'))
for future in as_completed(futures):
    print('#'*30)
    print(future.result())
    print('#'*30)
endtime = time.time()
print(f"Finished in {endtime - starttime}")
