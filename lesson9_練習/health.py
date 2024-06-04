class BMI():
    def __init__(self,name:str,height:int,weight:int):
        self.__name = name
        self.__height = height
        self.__weight = weight
    @property
    def name(self)->str:
        return self.name
    @property
    def height(self)->int:
        return self.height
    @property
    def weight(self)->int:
        return self.weight

    @classmethod
    def cal_bmi(cls,height:int, weight:int)->float:
        bmi = weight / (height / 100) ** 2
        return bmi

    @classmethod
    def get_status(cls,bmi:float)->str:
        if bmi < 18.5:
            status = "過輕"
        elif bmi < 24:
            status = "正常"
        elif bmi < 27:
            status = "過重"
        elif bmi < 30:
            status = "輕度肥胖"
        elif bmi < 35:
            status = "中度肥胖"
        else:
            status = "重度肥胖"
        return status
    