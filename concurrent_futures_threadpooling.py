from concurrent.futures import ThreadPoolExecutor,wait
from my_functions import ssh_command2
from my_devices import device_list
import time
starttime = time.time()
pool = ThreadPoolExecutor()
futures = []
for device in device_list:
    futures.append(pool.submit(ssh_command2,device,'show version'))
wait(futures)
for future in futures:
    print('#'*30)
    print(future.result())
    print('#'*30)
endtime = time.time()
print(f"Finished in {endtime - starttime}")
