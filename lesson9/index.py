'''
程式碼funcino化(功能)
    1.讓主程式變簡單
    2.讓程式碼可以重複呼叫
    3.簡化邏輯思考
'''
'''
lesson9 -> 專案
    index.py -> 主程式(index.py or main.py)
    tools.py -> 自訂的module
'''

#內建的變數__name__
import pyinputplus as pypi
import tools
def main()->None:
    name = pypi.inputStr("請輸入您的姓名: ")
    print(name)
    height = pypi.inputInt("請輸入您的身高(cm): ", min=50, max=250)
    print(height)
    weight = pypi.inputInt("請輸入您的體重(kg): ", min=0, max=200)
    print(weight)

    BMI = tools.cal_bmi(height=height, weight=weight)
    rate = tools.get_status(BMI)
    print(f"您的姓名為 {name}\n您的BMI值為 {BMI}\n您屬於 {rate} 範圍")


if __name__ == '__main__':
    '''
    print("我是被python執行的主程式")
    print(__name__)
    print(type(__name__))
    '''
    main()