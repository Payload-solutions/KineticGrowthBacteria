from typing import Any, Tuple, Dict
from serial import Serial
import time
from pprint import pprint

class Arduino:
    """Arduino connection"""

    def __init__(self):
        self.port = "/dev/ttyACM0"
        self.baud_rate = 9600
        self.timeout = 2

    def _connection(self) -> Any:
        serial_conn = Serial(port=self.port,
                             baudrate=self.baud_rate,
                             timeout=self.timeout)
        return serial_conn

    def read_lines(self, readers=10) -> Tuple[Dict[int, Any], list]:
        conn = self._connection()
        stack_data = list()
        object_data = dict()
        counter = 1
        while readers > 1:
            data = str(conn.readline().decode("ascii", errors="replace"))
            stack_data.append(data)
            object_data[counter] = data
            counter += 1
            readers -= 1
            time.sleep(0.05)
            # print("Stack data => {} ".format(stack_data))
            # print("Dictionary data => {}".format(object_data))
        
        stack_data = [pos.replace("\r\n", "") for pos in stack_data]
        stack_data = [stack_data.remove(val)  if val == "" else val   for val in stack_data]
        # stack_data = [x.replace("\r\n", "") for x in stack_data]
        conn.close()
        pprint(stack_data)
        # return object_data, stack_data