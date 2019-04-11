from my_devices import device_list
import threading,time
from queue import Queue
from my_functions import ssh_command2
def commander_ssh(device,command,output_queue):
   output_queue.put({'name':device.get('host'),'version_data':ssh_command2(device,command)})
def main():
    start_time = time.time()
    threads = []
    output_queue = Queue()
    for device in device_list:
        thread_instance = threading.Thread(target = commander_ssh,args = (device,'show version',output_queue),name = device.get('host'))
        threads.append(thread_instance)
        thread_instance.start()

    for t in threads:
        print(t)
        t.join()

    end_time = time.time()
    while not output_queue.empty():
        print('#'*30)
        item = output_queue.get(block=True)
        print(item.get('name'))
        print('='*30)
        print(item.get('version_data'))
        print('#'*30+'\n')
    print(f"Finished execution in {end_time - start_time:.2f}")

if __name__=='__main__':
    main()
