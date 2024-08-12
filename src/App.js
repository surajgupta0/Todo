import { useState } from 'react';
import './App.css';
import ToDoList from './ToDoList';

function App() {
  var [todoList, addList] = useState([]);
  var [toDoText,setoTDoText] = useState("");

  var getText = (event) => {
    setoTDoText(event.target.value);
  }

  var addToDoList = () => {
    addList((oldVal)=>{
      return [...oldVal, toDoText];
    });
    setoTDoText('');  
  }

  const handleKeyDown = (event) => {
    if (event.key === 'Enter') {
      addToDoList();
    }
  }

  const removeList = (index) =>{  
    console.log("event called");    
    const newItems = todoList.filter((todoList, i) => i !== index);
    addList(newItems);
  }

  return (
    <>
      
      <div className ='card'>
        <h1 >ToDo list</h1>
        <hr/>
        <div className="input_container">
          <input type = "text" name = "todo" placeholder="Add a Item" value={toDoText} onChange={getText}  onKeyDown={handleKeyDown} /> 
          <span className="add_item" onClick={addToDoList}>+</span>
        </div>
        <div className='todo_list_container'>
          {todoList.map((val,index) => {
            return(<>
              <ToDoList text = {val} index = {index} functionName = {removeList}></ToDoList>
            </>);
          })}

        </div>
      </div>
    </>
  );
}

export default App;
