import eel
import pos_system

INPUT_CSV_FILE = "./item_list.csv"
OUTPUT_TEXT_PATH = "./receipt/{datetime}.txt"

@eel.expose
def py_master_register():
    global order
    item_master = pos_system.get_item_master_from_csv(INPUT_CSV_FILE)
    order = pos_system.Order(item_master)

@eel.expose
def py_item_input(item_code, item_amount):
    global order
    order.input_order(item_code, item_amount)

@eel.expose
def py_calc_sum():
    global order
    order.calc_sum()

eel.init("web")
eel.start("main.html")