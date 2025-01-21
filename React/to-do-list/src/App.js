import './App.css';
import Input from './Components/Input';
import Board from './Components/Board';

import { useState } from "react";

function App() {
  const [taskList, setTaskList] = useState([]);

  return (
    <div className='px-12'>
    <div className="flex flex-col items-center justify-center py-8 gap-4">
     <h1 className="text-xl font-semibold">To Do List</h1>
     <Input taskList={taskList} setTaskList={setTaskList}/>
     </div>

      <div className='flex flex-col gap-4 sm:grid grid-cols-3 px-4 px-8 md:px-10 lg:px-12'>
        {taskList.map((task , index) => {
         return (
         <Board
         key={index}
         index={index}
         task={task}
         taskList={taskList}
         setTaskList={setTaskList}
         />
        )
        })}
      </div>
      </div>
  );
}

export default App;
