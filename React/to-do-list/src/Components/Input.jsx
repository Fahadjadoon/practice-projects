import {useState} from "react";

const Input = ({taskList, setTaskList}) => {

const [input, setInput] = useState('');

const addTask = (e) => {
    e.preventDefault();
    setTaskList([...taskList, input]);
    setInput("");
}

    return(
        <>
            <form className="flex flex-row items-center gap-3">
                <input
                className="border rounded-lo py-1.5 px-2.5 text-lg"
                type="text"
                placeholder="Add a task"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                />
                <button 
                className="bg-violet-400 text-white py-2 px-3.5 rounded
                font-semibold hover:opacity-70"
                onClick={addTask}>Add</button>
            </form>
        </>
    )
}

export default Input;