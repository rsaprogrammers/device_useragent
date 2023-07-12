
'''
# Code by Rana Shafaat Ali
'''


import subprocess
import random
import os



class UserAgentGenerator:
    def __init__(self, language="en_GB"):
        self.language = language

    def get_android_version(self):
        android_version = subprocess.check_output("getprop ro.build.version.release", shell=True).decode("utf-8").replace("\n", "")
        return android_version

    def get_model_device(self):
        model_device = subprocess.check_output("getprop ro.product.model", shell=True).decode("utf-8").replace("\n", "")
        return model_device

    def get_build_device(self):
        build_device = subprocess.check_output("getprop ro.build.id", shell=True).decode("utf-8").replace("\n", "")
        return build_device

    def generate_user_agent(self):
        android_version = self.get_android_version()
        model_device = self.get_model_device()
        build_device = self.get_build_device()
        versi_chrome = str(random.randint(300, 325)) + ".0.0." + str(random.randint(1, 8)) + "." + str(random.randint(40, 150))
        large_device = "{density=2.25,height=" + subprocess.check_output("getprop ro.hwui.text_large_cache_height", shell=True).decode("utf-8").replace("\n", "") + ",width=" + subprocess.check_output("getprop ro.hwui.text_large_cache_width", shell=True).decode("utf-8").replace("\n", "") + "}"
        merk_device = subprocess.check_output("getprop ro.product.manufacturer", shell=True).decode("utf-8").replace("\n", "")
        brand_device = subprocess.check_output("getprop ro.product.brand", shell=True).decode("utf-8").replace("\n", "")
        cpu_device = subprocess.check_output("getprop ro.product.cpu.abilist", shell=True).decode("utf-8").replace(",", ":").replace("\n", "")
        versi_app = str(random.randint(111111111, 999999999))

        try:
            simcard = subprocess.check_output("getprop gsm.operator.alpha", shell=True).decode("utf-8").split(",")[1].replace("\n", "")
        except:
            simcard = subprocess.check_output("getprop gsm.operator.alpha", shell=True).decode("utf-8").split(",")[0].replace("\n", "")

        user_agent = f"Davik/2.1.0 (Linux; U; Android {android_version}; {model_device} Build/{build_device}) [FBAN/MessengerLite;FBAV/{versi_chrome};FBPN/com.facebook.mlite;FBLC/{self.language};FBBV/{versi_app};FBCR/{simcard};FBMF/{merk_device};FBBD/{brand_device};FBDV/{model_device};FBSV/{android_version};FBCA/{cpu_device};FBDM/{large_device};]"

        return user_agent

generator = UserAgentGenerator(language="en")
user_agent = generator.generate_user_agent()
os.system('clear')
print("\n\n Code : Rana Shafaat Ali")
print("\n\n\tUser Agent:", user_agent)
