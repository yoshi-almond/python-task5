///起動時にマスタを読み込み、orderインスタンスを生成
window.addEventListener('DOMContentLoaded',() => {
    eel.py_master_register();
},false);

///登録ボタンクリック時に商品を追加
window.addEventListener('DOMContentLoaded',() => {
    document.getElementById('register-btn').addEventListener('click', () => {
        item_code = document.getElementById('item-code').value;
        item_amount = document.getElementById('item-amount').value;
        eel.py_item_input(item_code, item_amount);
        eel.py_calc_sum();
    },false);
},false);

eel.expose(js_pop_window)
function js_pop_window(text){
    window.alert(text);
}

eel.expose(js_add_list)
function js_add_list(text){
    document.getElementById('buy-list').value += text + "\n"
}

eel.expose(js_update_sum)
function js_update_sum(text){
    document.getElementById('sum-display-area').innerHTML = "   " + text + "円";
}



