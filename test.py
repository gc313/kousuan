import streamlit as st
import streamlit.components.v1 as components

my_js = """
    function printer(){
    var newWin = window.open('printer', '', '');
    var xiaozhi = document.getElementById("xz").innerHTML;
    newWin.document.write(xiaozhi);
    newWin.document.location.reload();
    newWin.print();
    newWin.close();
}
    """

# Wrapt the javascript as html code
my_html = f"""<script>{my_js}</script>
    <p id="xz">This is Printer!</p>
    <button onclick="printer()">打印</button>
    """

# Execute your app
components.html(my_html)
