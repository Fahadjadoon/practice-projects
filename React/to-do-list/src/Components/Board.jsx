const Board = ({task, index, taskList, setTaskList}) => {
    
    const handleDelete = () => {
        // Directly use the index from the props instead of finding the task index
        setTaskList(currentTasks => currentTasks.filter((_, idx) => idx !== index));
    };

    return (
        <>
            <div className="max-w-xl flex flex-col items-center justify-start border text-center text-lg pt-3 pb-4 px-4 md:px-6">
                <p>{task}</p>
                <button
                    className="bg-red-400 text-white rounded-lg py-1 px-2 mt-4"
                    onClick={handleDelete}
                >
                    Delete
                </button>
            </div>
        </>
    );
};

export default Board;
