import './ToDoList.css';
import React, { useState } from 'react';

const ToDoList = (props) => {
    var [isChecked,setChecked] = useState(false);

    var toggleChecked = () => {
        setChecked(!isChecked);
    }

    return (
        <>
            <div className='Todolist'>
                <span className='Todoicon' onClick={() => props.functionName(props.index)}>X</span>
                <span className="Todotext">{props.text}  + {props.index}</span>
                <span className={`glyphicon ${isChecked ? 'glyphicon-check':'glyphicon-unchecked'}`} onClick={toggleChecked}></span>
            </div>
        </>
    );
}

export default ToDoList;