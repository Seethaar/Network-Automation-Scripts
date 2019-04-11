from my_devices import device_list
import threading,time
from ssh_command import ssh_command
def main():
    start_time = time.time()
    threads = []
    for device in device_list:
        thread_instance = threading.Thread(target = ssh_command,args = (device,'show version'),name = device.get('host'))
        threads.append(thread_instance)
        thread_instance.start()

    for t in threads:
        print(t)
        t.join()

    end_time = time.time()
    print(f"Finished execution in {end_time - start_time:.2f}")

if __name__=='__main__':
    main()
