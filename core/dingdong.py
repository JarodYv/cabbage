import time
from core.device import connect_phone, play_voice
from core.qiang import Qiang


class QiangDingdong(Qiang):
    def __init__(self, signal):
        super(QiangDingdong, self).__init__(signal)

    @classmethod
    def is_five_o_clock(cls, the_time: str) -> bool:
        """ 判断是否到抢菜时间

        :return:
        """
        return time.strftime('%H:%M') >= the_time  # '05:59'

    @classmethod
    def get_current_hour(cls, d):
        """ 获取当前的时间

        :param d:
        :return:
        """
        info = d.xpath('//*[@resource-id="com.yaya.zone:id/rv_selected_hour"]').get(timeout=1).info
        return info.get("childCount", 0)

    def qiang_cai(self, device_id: str):
        """ 叮咚抢菜核心逻辑

        :param device_id: 设备id
        :return:
        """
        d = connect_phone(device_id)
        self.count = 1
        time_start = time.time()
        # 此处填设备编号
        while self.is_running:
            start = time.time()
            if d(textContains="结算(").exists:
                d(textContains="结算(").click()
                self.signal.emit({"msg": "点击结算", "type": 1})
            else:
                if d(text="全选").exists and d(textContains="结算").exists:
                    d(text="全选").click()
                    self.signal.emit({"msg": "点击全选", "type": 1})

            if d(text="我知道了").exists:
                print("点击我知道了")
                d(text="我知道了").click()
                self.signal.emit({"msg": "点击我知道了", "type": 1})

            # if d(text="返回购物车").exists:
            #     print("点击返回购物车")
            #     d(text="返回购物车").click()

            if d(text="重新加载").exists:
                d(text="重新加载").click()
                self.signal.emit({"msg": "点击重新加载", "type": 1})

            if d(text="下单失败").exists:
                self.signal.emit({"msg": "下单失败", "type": 3})
                if d(text="返回购物车").exists:
                    d(text="返回购物车").click()
                    self.signal.emit({"msg": "点击返回购物车", "type": 1})
            else:
                if d(text="立即支付").exists:
                    d(text="立即支付").click()
                    self.signal.emit({"msg": "点击立即支付", "type": 2})
                if d(text="选择送达时间").exists:
                    self.signal.emit({"msg": "选择送达时间", "type": 1})
                    hour_count = QiangDingdong.get_current_hour(d)
                    for i in range(hour_count):
                        info = d.xpath(
                            '//*[@resource-id="com.yaya.zone:id/rv_selected_hour"]'
                            '/android.view.ViewGroup[%s]' % str(i + 1)).get(timeout=1).info
                        if info.get("enabled", "") != "false":
                            self.signal.emit({"msg": "有运力了", "type": 2})
                            d.xpath(
                                '//*[@resource-id="com.yaya.zone:id/rv_selected_hour"]'
                                '/android.view.ViewGroup[%s]' % str(i + 1)).click_exists(timeout=1)
                            self.signal.emit({"msg": f"点击了第{i + 1}个", "type": 1})
                            if d(text="立即支付").exists:
                                if self.play_sound:
                                    play_voice("success")
                                d(text="立即支付").click()
                                self.signal.emit({"msg": "点击立即支付", "type": 2})
                        if i == hour_count - 1:
                            d.xpath('//*[@resource-id="com.yaya.zone:id/'
                                    'iv_dialog_select_time_close"]').click_exists(timeout=1)
                            d.xpath('//*[@resource-id="com.yaya.zone:id/'
                                    'iv_order_back"]').click_exists(timeout=1)
                            self.signal.emit({"msg": "没有运力了", "type": 3})

            if d(text="确认交易").exists:
                if self.play_sound:
                    play_voice("success")
                d(text="确认交易").click()
                self.signal.emit({"msg": "点击确认交易", "type": 2})

            if d(text="确认并支付").exists:
                if self.play_sound:
                    play_voice("success")
                d(text="确认并支付").click()
                self.signal.emit({"msg": "点击确认并支付", "type": 2})

            if d(resourceId="btn-line").exists:
                if self.play_sound:
                    play_voice("success")
                d(resourceId="btn-line").click()
                self.signal.emit({"msg": "确认支付", "type": 2})

            self.signal.emit({"msg": f"第<b>{self.count}</b>次抢菜", "type": 0})
            self.signal.emit({"msg": "本次花费时间: <b>{:.2f}秒</b>".format(time.time() - start), "type": 0})
            self.signal.emit({"msg": "总共花费时间: <b>{:.2f}分</b>".format((time.time() - time_start) / 60), "type": 0})
            self.count += 1
            if self.op_sleep > 0:
                time.sleep(self.op_sleep)
