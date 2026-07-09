const select_list = document.getElementById("status-select");
select_list.addEventListener('change', update);

const table_order = document.getElementById("order_table");


function update(event){
    const current_value = event.target.value;
    table_order.innerHTML = '';
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
    .then(data => data_bind(data))
    .catch(error => console.error('Ошибка:', error));





    /*
    const has_data = data[`has_data`];

    const data_for_table = data[`content`];
    data_for_table.array.forEach(element => {
        const row = table_order.insertRow();
        const IDCell = row.insertCell();
        IDCell.textContent = data_for_table['ID'];

    });*/




}

function data_bind(data){
    const has_data = data[`has_data`];
    const size = data[`size`];
    console.log(size);
    
    if (has_data){

        const data_for_table = data[`content`];
  
        for (let i = 1; i <= size;i++){
            const tr = document.createElement('tr');

            
            const row =  table_order.insertRow();
            const IDCell = row.insertCell();
            IDCell.textContent = data_for_table['id'];
            const NumberCell = row.insertCell();
            NumberCell.textContent = data_for_table['number'];            
        }

    }
}
