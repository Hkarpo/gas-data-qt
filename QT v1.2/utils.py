
import  serial
import time
import threading
import inspect

import ctypes

class MSerialPort:
    #内存
    message = []
    _isopen=1

    def __init__(self, port, buand):
        self.port = serial.Serial(port, buand)
        if not self.port.isOpen():
            self.port.open()

    def port_open(self):
        if not self.port.isOpen():
            self._isopen=1
            self.port.open()

    def port_close(self):
        self._isopen=0
        self.port.close()


    def send_data(self, data):
        number = self.port.write(data)
        return number

    def read_data(self):
        if self._isopen==0:
            return("Sigkill")
        while self._isopen==1:
            data = self.port.readline().decode().split(',')
            # print(data)
            # d = time.localtime()
            # cur_time = time.strftime('"%m.%d.%H:%M:%S', d)
            # print(data)
            self.message = data

# automatic ports scanner
def scan_ports_info(Handle_print=0):
    print('start scanning')
    ''''''
    ports_list = list(serial.tools.list_ports.comports())
    # print(len(ports_list))
    if Handle_print:
        print("[info]ports number:",len(ports_list))

    if len(ports_list) <= 0:
        print("The Serial port can't find!")
    else:
        for i in range(len(ports_list)):
            port_list = list(ports_list[i])
            port_serialName = port_list[0]
            if Handle_print:
                # print('\n[info]port list', port_list)
                print('[info]port serial Name',port_serialName)
    return ports_list


# not mine:

def _async_raise(tid, exctype):

    """raises the exception, performs cleanup if needed"""

    tid = ctypes.c_long(tid)

    if not inspect.isclass(exctype):

        exctype = type(exctype)

    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))

    if res == 0:

        raise ValueError("invalid thread id")

    elif res != 1:

        # """if it returns a number greater than one, you're in trouble,

        # and you should call it again with exc=NULL to revert the effect"""

        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)

        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):

    _async_raise(thread.ident, SystemExit)