from mysteryutils.Definitions import ShuffleNames
import random

class Shuffle:
    def __init__(self, name: str):
        self.shuffleName = name
        self.itemString = ""
        self.weight = 0
    
    def getName(self) -> str:
        return self.shuffleName
    
    def setWeight(self, newWeight: int):
        if newWeight < 0:
            newWeight = 0
        if newWeight > 100:
            newWeight = 100
        self.weight = newWeight
    
    def getWeight(self) -> int:
        return self.weight
    
    def modifyWeight(self, weightMod: int):
        self.weight += weightMod
        if self.weight < 0:
            self.weight = 0
        if self.weight > 100:
            self.weight = 100

    def setItemString(self, item: str):
        self.itemString = item

    def getItemString(self) -> str:
        return self.itemString

class Category:
    def __init__(self, name: str, description: str):
        self.categoryName = name
        self.description = description
        self.shuffles: dict[str, Shuffle] = {}
        self.activeShuffle = ShuffleNames.GENERIC_OFF
        self.hidden = False

    def defineShuffle(self, newShuffle: Shuffle):
        self.shuffles[newShuffle.getName()] = newShuffle
    
    def setActiveShuffle(self, s: str):
        self.activeShuffle = s
        
    def getActiveShuffle(self) -> str:
        return self.activeShuffle
    
    def isActive(self) -> bool:
        return self.activeShuffle != ShuffleNames.GENERIC_OFF
        
    def setWeights(self, weightDict: dict[str, int]):
        for s in weightDict:
            self.shuffles[s].setWeight(weightDict[s])

    def setWeight(self, shuffle: str, newWeight: int):
        self.shuffles[shuffle].setWeight(newWeight)
    
    def getWeight(self, shuffle: str) -> int:
        return self.shuffles[shuffle].getWeight()
    
    def setHidden(self, val: bool):
        self.hidden = val
    
    def isHidden(self) -> bool:
        return self.hidden
    
    def modifyWeight(self, shuffle: str, weightMod: int):
        self.shuffles[shuffle].modifyWeight(weightMod)

    def guaranteeShuffle(self, shuffle: str):
        if (shuffle == ShuffleNames.GENERIC_OFF):
            self.zeroAllShuffles()
        else:
            for s in self.shuffles:
                self.shuffles[s].setWeight(100 if (self.shuffles[s].getName() == shuffle) else 0)

    def zeroAllShuffles(self):
        for s in self.shuffles:
            self.shuffles[s].setWeight(0)
    
    def roll(self):
        rollShuffles = [ShuffleNames.GENERIC_OFF]
        rollWeights = [100]
        for s in self.shuffles:
            w = self.shuffles[s].getWeight()
            rollShuffles.append(s)
            rollWeights[0] -= w
            if rollWeights[0] < 0:
                rollWeights[0] = 0
            rollWeights.append(w)
        self.activeShuffle = random.choices(rollShuffles, rollWeights)[0]

    def spoil(self) -> str:
        a = self.activeShuffle
        if a == "Off":
            a = "---"
        return f"{self.categoryName:>28}:  {a}"