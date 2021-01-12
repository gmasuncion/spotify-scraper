import local_settings

class settings():
    
    def __init__(self):
        self.settingsInfo = {}
        self.settingsInfo["PATH"] = local_settings.PATH

    def get_setting(self, key):
        #TODO check if key exists before accesing. otherwise return null
        return self.settingsInfo[key]

