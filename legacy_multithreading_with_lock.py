from my_devices import device_list
import threading,time
from my_functions import ssh_command2
def commander_ssh(device,command,output_list):
   hall_pass = threading.Lock()
   print("thread locked?: {}".format(hall_pass.locked()))
   with hall_pass:
       output_list.append({'name':device.get('host'),'version_data':ssh_command2(device,command)})
       time.sleep(1)
       print(len(output_list))
       print("thread locked?: {}".format(hall_pass.locked()))

def main():
    start_time = time.time()
    threads = []
    output_list = []
    for device in device_list:
        thread_instance = threading.Thread(target = commander_ssh,args = (device,'show version',output_list),name = device.get('host'))
        threads.append(thread_instance)
        thread_instance.start()

    for t in threads:
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
