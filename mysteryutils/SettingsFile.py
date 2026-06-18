import json


class SettingsFile:
    def __init__(self, baseFilePath: str, outputFilePath: str):
        with open(baseFilePath, "r") as read_file:
            self.rawdata = json.load(read_file)
        
        self.baseFile = baseFilePath
        self.outputFile = outputFilePath
        self.name = outputFilePath[7:].removesuffix(".json")
        self.settings = {}

    def getBasicSetting(self, settingName: str):
        return self.settings[settingName]
    
    def setBasicSetting(self, settingName: str, settingValue):
        self.settings[settingName] = settingValue

    def addHintToTier(self, checkName: str, hintTier: int):
        pass

    def removeHintFromTier(self, checkName: str, hintTier: int):
        pass

    def getHintTierSize(self, hintTier: int) -> int:
        return 0
    
    def setHintTierSize(self, hintTier: int, newSize: int):
        pass

    def getBaseFilePath(self) -> str:
        return self.baseFile
    
    def getOutputFilePath(self) -> str:
        return self.outputFile
    
    def write(self):
        with open(self.outputFile, "w") as write_file:
            json.dump(self.rawdata,write_file,indent=4)
    
class DesktopSettingsFile(SettingsFile):
    def __init__(self, baseFilePath: str, outputFilePath: str):
        super().__init__(baseFilePath, outputFilePath)
        self.settings = self.rawdata["GameplaySettings"]

    def addHintToTier(self, checkName: str, hintTier: int):
        self.settings["OverrideHintPriorities"][hintTier].append(checkName)

    def removeHintFromTier(self, checkName: str, hintTier: int):
        if checkName in self.settings["OverrideHintPriorities"][hintTier]:
            self.settings["OverrideHintPriorities"][hintTier].remove(checkName)

    def getHintTierSize(self, hintTier: int) -> int:
        return self.settings["OverrideHintItemCaps"][hintTier]
    
    def setHintTierSize(self, hintTier: int, newSize: int):
        self.settings["OverrideHintItemCaps"][hintTier] = newSize

class WebSettingsFile(SettingsFile):
    def __init__(self, baseFilePath: str, outputFilePath: str):
        super().__init__(baseFilePath, outputFilePath)
        self.settings = self.rawdata["settings"]
        self.rawdata["name"] = self.name
    
    def getBasicSetting(self, settingName: str):
        webSettingName = "GameplaySettings." + settingName
        return super().getBasicSetting(webSettingName)
    
    def setBasicSetting(self, settingName: str, settingValue):
        webSettingName = "GameplaySettings." + settingName
        super().setBasicSetting(webSettingName, settingValue)
    
    def addHintToTier(self, checkName: str, hintTier: int):
        self.settings["GameplaySettings.OverrideHintPriorities"][hintTier].append(checkName)

    def removeHintFromTier(self, checkName: str, hintTier: int):
        if checkName in self.settings["GameplaySettings.OverrideHintPriorities"][hintTier]:
            self.settings["GameplaySettings.OverrideHintPriorities"][hintTier].remove(checkName)

    def getHintTierSize(self, hintTier: int) -> int:
        return self.settings["GameplaySettings.OverrideHintItemCaps"][hintTier]
    
    def setHintTierSize(self, hintTier: int, newSize: int):
        self.settings["GameplaySettings.OverrideHintItemCaps"][hintTier] = newSize