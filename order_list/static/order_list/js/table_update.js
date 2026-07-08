const select_list = document.getElementById("status-select");
select_list.addEventListener('change', update);


function update(event){
    const current_value = event.target.value;
    console.log(current_value);
    fetch('/sorted_orders/', 
        {
            method : 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body : JSON.stringify({"status" : current_value})
        }
    )
    .then(response => response.json())
    .then(data => console.log('Успех:', data))
    .catch(error => console.error('Ошибка:', error));    

}
