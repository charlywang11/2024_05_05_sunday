'''
module名稱:health.py
    class名稱:BMI
        property:name
        property:height
        property:weight
        method:bmi()
        method:status()

主程式index.py
    from health import BMI
        請輸入姓名:xxxx
        請輸入身高(cm):xxxx
        請輸入體重(kg):xxxx
        xxxxbmi值為:23.xxx
        您的體重:正常
'''
import pyinputplus as pypi
from health import BMI

def main()->None:
    name = pypi.inputStr("請輸入您的姓名:")
    height = pypi.inputInt("請輸入您的身高(cm):",min=1) 
    weight = pypi.inputInt("請輸入您的體重(kg):",min=1)

    bmi = BMI.cal_bmi(height, weight)
    status = BMI.get_status(bmi)

    print(f"{name} bmi值為:{round(bmi,3)}")
    print(f"您的體重:{status}")

if __name__ == '__main__':
    main()
