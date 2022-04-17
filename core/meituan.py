import time
from core.device import connect_phone, play_voice
from core.qiang import Qiang


class QiangMeituan(Qiang):
    def __init__(self, signal):
        super(QiangMeituan, self).__init__(signal)

    def qiang_cai(self, device_id: str):
        """ 美团抢菜核心逻辑

        :param device_id:
        :return:
        """
        d = connect_phone(device_id)
        # d.app_start("com.sankuai.meituan")
        self.count = 1
        time_start = time.time()
        while self.is_running:
            start = time.time()
            if d(textContains="结算(").exists:
                d(textContains="结算(").click()
                self.signal.emit({"msg": "点击结算", "type": 1})
            else:
                if d(text="全选").exists:
                    d(text="全选").click()
                    self.signal.emit({"msg": "点击全选", "type": 1})

            if d(text="我知道了").exists:
                d(text="我知道了").click()
                self.signal.emit({"msg": "点击我知道了", "type": 1})

            if d(text="重新加载").exists:
                d(text="重新加载").click()
                self.signal.emit({"msg": "重新加载", "type": 1})

            if d(text="返回购物车").exists:
                d(text="返回购物车").click()
                self.signal.emit({"msg": "点击返回购物车", "type": 1})

            if d(text="立即支付").exists:
                if self.play_sound:
                    play_voice("success")
                d(text="立即支付").click()
                self.signal.emit({"msg": "点击立即支付", "type": 2})

            if d(text="确认并支付").exists:
                if self.play_sound:
                    play_voice("success")
                d(text="确认并支付").click()
                self.signal.emit({"msg": "确认并支付", "type": 2})

            if d(textContains="极速支付").exists:
                if self.play_sound:
                    play_voice("success")
                self.signal.emit({"msg": "极速支付", "type": 2})
                break

            if d(textContains="普通支付").exists:
                if self.play_sound:
                    play_voice("success")
                self.signal.emit({"msg": "普通支付", "type": 2})
                break

            if d(resourceId="btn-line").exists:
                if self.play_sound:
                    play_voice("success")
                d(resourceId="btn-line").click()
                self.signal.emit({"msg": "确认支付", "type": 2})
                break
            self.signal.emit({"msg": f"第<b>{self.count}</b>次抢菜", "type": 0})
            self.signal.emit({"msg": "本次花费时间: <b>{:.2f}秒</b>".format(time.time() - start), "type": 0})
            self.signal.emit({"msg": "总共花费时间: <b>{:.2f}分</b>".format((time.time() - time_start) / 60), "type": 0})
            self.count += 1
            if self.op_sleep > 0:
                time.sleep(self.op_sleep)
