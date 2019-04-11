from my_devices import device_list
from commander import commander
import time
start_time = time.time()
for device in device_list:
    output = commander(device,'show version')
    print('#'*30)
    print('The version of {}'.format(device.get('host')))
    print('_'*30)
    print(output)
    print('#'*30)
end_time = time.time()
print("\n\n")
print(f"Finished in {end_time - start_time:.2f} seconds")
print("\n\n")
