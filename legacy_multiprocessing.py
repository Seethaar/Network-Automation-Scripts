from my_devices import device_list
import time
from multiprocessing import Process
from my_functions import ssh_command2
def commander_ssh(device,command,output_list):
   output_list.append({'name':device.get('host'),'version_data':ssh_command2(device,command)})
def main():
    start_time = time.time()
    processes = []
    output_list = []
    for device in device_list:
        process_instance = Process(target = commander_ssh,args = (device,'show version',output_list),name = device.get('host'))
        processes.append(process_instance)
        process_instance.start()

    for t in processes:
        print(t)
        t.join()

    end_time = time.time()
    for item in output_list:
        print('#'*30)
        print(item.get('name'))
        print('='*30)
        print(item.get('version_data'))
        print('#'*30+'\n')
    print(f"Finished execution in {end_time - start_time:.2f}")

if __name__=='__main__':
    main()
'''
This script fails as output_list cannot be shared amongst process. Saving this as it was a good lesson.
'''
