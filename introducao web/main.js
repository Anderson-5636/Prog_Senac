function addNewTask(){
    var list = document.getElementById("list");
    var text = document.getElementById("task_name").value;

    if(text.length === 0){
        alert("Tarefa precisa de ao menos 1 caractere");
        return;
    }

    var listItem  = document.createElement("li");
    listItem.className = "list-item";

    const textElement  = document.createTextNode(text);
    listItem.appendChild(textElement);
    list.appendChild(listItem);
}

// usar o removeChild para remover a lista