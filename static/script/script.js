// Credit to https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_mobile_navbar

function menuFunction() {
  var x = document.getElementById("myLinks");
  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}

// Credit to https://www.geeksforgeeks.org/how-to-make-html-table-expand-on-click-using-javascript/?fbclid=IwAR1hVkf9KzZjewn6agXULtWcXnuknO4pAtlW11MqNG2FVz4O6JVx_SdzHvA 

function showHideRow(hidden_row) {
  var x = document.getElementById(hidden_row);
  if (x.style.display === 'none') {
    x.style.display = 'table-row';
  } else {
    x.style.display = 'none';
  }
}

setTimeout(function () {
  let messages = document.getElementById("msg");
  let alert = new bootstrap.Alert(messages);
  alert.close();
}, 3000);

