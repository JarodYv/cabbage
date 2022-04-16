import time
from core.device import play_voice


class Qiang:
    def __init__(self, signal):
        self.is_running = False
        self.signal = signal
        self.count = 0

    def run(self, device_id: str):
        """ 执行抢菜程序

            :param device_id: 设备编号
            :return:
            """
        # play_voice("start")
        print("开始执行抢菜程序.....")
        self.is_running = True
        while self.is_running:
            try:
                self.qiang_cai(device_id)
            except Exception as e:
                print(e)
                self.signal.emit({"msg": str(e), "type": 4})
                play_voice("error")
                time.sleep(5)

    def qiang_cai(self, device_id: str):
        raise NotImplementedError

    def stop(self):
        self.is_running = False
