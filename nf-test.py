import os
import threading
import time


class FileThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        create_mtime = os.path.getmtime('/mnt/config/config.json')
        print('Read config : ' + str(create_mtime))

        while True:
            mtime = os.path.getmtime('/mnt/config/config.json')
            if create_mtime != mtime:
                create_mtime = mtime
                print('modified : ' + str(create_mtime))
            time.sleep(1)  # 1 sec


def main():
    thread = FileThread()
    thread.daemon = True
    thread.run()
    print('Done.')


if __name__ == '__main__':
    main()
