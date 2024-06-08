#請讀取lesson10資料夾內的-個股日成交資訊.csv

import csv
import pyinputplus as pyip
from random import choices
from pprint import pprint

def main():
    with open('個股日成交資訊.csv',encoding='utf-8',newline='') as file:
        reader = csv.DictReader(file)
        stocks = list(reader)
        total = len(stocks)
        print(f"個股日成交資訊共有{total}筆證券資料")
        
        num_str:str = pyip.inputMenu(['1筆','2筆','3筆','4筆','5筆'],
                            prompt="請輸入隨機顯示的證券資料筆數(請選擇1,2,3,4,5):\n",
                            numbered=True)
        num:int = int(num_str[0])
        selected_name:list[str] = choices(stocks,k=num)
        for name in selected_name:
            pprint(name)

if __name__ == '__main__':
    main()
