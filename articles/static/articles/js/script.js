console.log(111)

let subname = document.querySelector('#subname')
subname.addEventListener('click', function (e) {
	e.preventDefault()
	let formData = new FormData(document.forms.myformtest) // Получаем данные из формы
	let xhr = new XMLHttpRequest(); //создаем объект
	 xhr.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) { //проверяем ответ на ошибки
            	// если норм то выводим
                document.getElementById("result_output").innerHTML = this.responseText;
            }
            else
            {
            	// если нет сообщаем об ошибке
            	document.getElementById("result_output").innerHTML = "Error";
            }
        };
     xhr.open("POST", "/formtest/"); // post запрос на конкретный контроллер
     xhr.send(formData); //отпраляем данные

})