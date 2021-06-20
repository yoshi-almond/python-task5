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

//会計ボタンを押すと預かり金額を取得、お釣りを計算
window.addEventListener('DOMContentLoaded',() => {
    document.getElementById('pay-btn').addEventListener('click', () => {
        pay_amount = document.getElementById('payment').value;
        change = eel.py_calc_change(pay_amount);
    },false);
},false);

//リセットボタンを押すと最初から
window.addEventListener('DOMContentLoaded',() => {
    document.getElementById('reset-btn').addEventListener('click', () => {
        window.location.reload();
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

eel.expose(js_show_change)
function js_show_change(text){
    document.getElementById('change').innerHTML = "   " + text + "円";
}



