const select_list = document.getElementById("status-select");
select_list.addEventListener('change', update);

const table_order = document.getElementById("order_table");


function update(event){
    const current_value = event.target.value;

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


}

function data_bind(data){
    const has_data = data[`has_data`];
    const size = data[`size`];
    console.log(size);
    const tbody = table_order.querySelector('tbody');
    tbody.innerHTML = ''; 

    if (has_data){

        const data_for_table = data[`content`];
     
        let html_code = '';
        /*<tbody>
            {% for order in orders %}
            <tr>
            <td>{{ order.id }}</td> 
            <td><a href="/{{ order.number }}/edit/">{{ order.number }}</a></td>                
            <td>{{ order.equipment }}</td>
            <td>{{ order.date|date:"Y-m-d" }}</td>
            </tr>
            {% endfor %}
        </tbody>*/ 
        
        
        for (let i = 1; i <= size;i++){
            const id = data_for_table[i][`ID`];
            const number = data_for_table[i][`Number`];


          html += `
              <tr>
                <td>${id}</td>
                <td>${number}</td>                                                         
              </tr>
            `;            
          
        }
        tbody.innerHTML = html;
    }
    else{
        tbody.innerHTML = '<p>Нет данных</p>';        
    }

}
