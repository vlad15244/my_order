const select_list = document.getElementById("order-select");
select_list.addEventListener('change', update);

const table_order = document.getElementById("event_table");


function update(event){
    const order_for_request = event.target.value;

    fetch('/sorted_events/', 
        {
            method : 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body : JSON.stringify({"order" : order_for_request})
        }
    )
    .then(response => response.json())
    .then(data => data_bind(data))
    .catch(error => console.error('Ошибка:', error));


}

function data_bind(data){
    const has_data = data[`has_data`];
    const size = data[`size`];
    const content = data[`content`];
    const tbody = table_order.querySelector('tbody');
    tbody.innerHTML = ''; 

    if (has_data){

        let html_code = '';

        for (let i=0; i<size; i++){
            const row = content[i];
            
            html_code += `<tr>
                <td>${row.order}</td>
                <td>${row.type}</td>
                <td>${row.description}</td>                                
                <td>${row.date}</td>                
            `

        }
        
        tbody.innerHTML = html_code;
    }
    else{
        tbody.innerHTML = '<p>Нет данных</p>';        
    }

}
