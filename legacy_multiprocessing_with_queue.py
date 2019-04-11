from my_devices import device_list
import time
from multiprocessing import Process,Queue
from my_functions import ssh_command2
def commander_ssh(device,command,output_queue):
   output_queue.put({'name':device.get('host'),'version_data':ssh_command2(device,command)})
def main():
    start_time = time.time()
    processes = []
    output_queue = Queue()
    for device in device_list:
        process_instance = Process(target = commander_ssh,args = (device,'show version',output_queue),name = device.get('host'))
        processes.append(process_instance)
        process_instance.start()

    for t in processes:
        print(t)
        t.join()

    end_time = time.time()
    while not output_queue.empty():
        print('#'*30)
        item = output_queue.get()
        print(item.get('name'))
        print('='*30)
        print(item.get('version_data'))
        print('#'*30+'\n')
    print(f"Finished execution in {end_time - start_time:.2f}")

if __name__=='__main__':
    main()
