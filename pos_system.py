import pandas as pd
import datetime
import sys
import eel
import unicodedata

INPUT_CSV_FILE = "./item_list.csv"
OUTPUT_TEXT_PATH = "./receipt/{datetime}.txt"

#商品クラス
class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    
    def get_price(self):
        return self.price

#オーダークラス
class Order:
    def __init__(self,item_master):
        self.order_code_list = []
        self.item_master = item_master
        self.set_datetime()
        self.display_init()
        
    def display_init(self):
        eel.js_add_list("{0}{1}{2}{3}".format(text_align("商品コード"),text_align("商品名"),text_align("値段"),text_align("個数")))
        line = ""
        for i in range(100):
            line += "-"
        eel.js_add_list(line)

    def count_zenkaku(self,text):
        count = 0
        for char in text:
            if unicodedata.east_asian_width(char) in 'FWA':
                count += 1
        return count

    def set_datetime(self):
        self.datetime=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    
    def add_order_list(self,item_code,amount):
        self.order_code_list.append([item_code,amount])

    def input_order(self,item_code,item_amount):
        if self.get_item_data(item_code)[0] == False:
            eel.js_pop_window("商品コードに対応するアイテムが見つかりませんでした")
        self.add_order_list(item_code,item_amount)
        item_name = self.get_item_data(item_code)[1]
        item_price = self.get_item_data(item_code)[2]
        eel.js_add_list("{0:20}{1}{2:<20}{3:20}".format(item_code,text_align(item_name),item_price,item_amount))

    def view_item_list(self):
        self.write_receipt("-----購入商品-----")
        for order_code in self.order_code_list:
            self.write_receipt(f"商品コード:{order_code[0]} 商品名:{self.get_item_data(order_code[0])[1]} 値段:{self.get_item_data(order_code[0])[2]} 個数:{order_code[1]}")
        self.write_receipt("------------------")

    def get_item_data(self,order_code):
        for item in self.item_master:
            if item.item_code == order_code:
                return True, item.item_name, item.price
        print("商品コードに対応するアイテムが見つかりませんでした")
        return False,"None","None"

    def input_money(self):
        money = input("お金を入力してください")
        self.write_receipt(f"お預かり金額:{money}")
        return money

    def calc_sum(self):
        self.sum = 0
        for order_code in self.order_code_list:
            self.sum += self.get_item_data(order_code[0])[2] * int(order_code[1])
        eel.js_update_sum(self.sum)

    def calc_change(self):
        money = int(self.input_money())
        change = money - self.sum
        self.write_receipt(f"お釣り:{change}")

    def write_receipt(self,text):
        print(text)
        with open(OUTPUT_TEXT_PATH.format(datetime=self.datetime),mode="a",encoding="utf-8_sig") as f:
            f.write(text+"\n")

#CSVファイルからマスタを読み込み
def get_item_master_from_csv(path):
    try:
        df = pd.read_csv(path,dtype={0:object})
        # マスタ登録
        item_master=[]
        for row in df.itertuples():
            item_master.append(Item(row[1],row[2],row[3]))
        print("-----商品リスト-----")
        for i in item_master:
            print(f"{i.item_code}  {i.item_name}  {i.price}")
        print("--------------------")
        return item_master
    except:
        print("登録失敗")
        sys.exit()

def get_han_count(text):
    count = 0
    for char in text:
        if unicodedata.east_asian_width(char) in 'FWA':
            count += 2
        else:
            count += 1
    return count

def text_align(text, width=20, align=-1, fill_char=' '):
    """ 
    width: 半角換算で文字数を指定
    align: -1 -> left, 0 -> center 1 -> right
    fill_char: 埋める文字を指定 
    """
    fill_count = width - get_han_count(text)
    if (fill_count <= 0): return text
    if align == -1:
        return text + fill_char*fill_count
    elif align == 1:
        return fill_char*fill_count + text
    else:
        return fill_char*(fill_count/2) + text + fill_char*(fill_count/2)
    
#メイン処理
def main():
    item_master = get_item_master_from_csv(INPUT_CSV_FILE)
    order = Order(item_master)
    order.input_order()
    order.view_item_list()
    order.calc_sum()

if __name__ == "__main__":
    main()