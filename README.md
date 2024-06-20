### README.md

# ToDo App using Tkinter and ttkthemes

Welcome to the ToDo App project! This application is built using Python's Tkinter library and ttkthemes to create a beautiful and functional to-do list. 

## Features

- **Add Tasks:** Easily add new tasks to your to-do list.
- **Complete Tasks:** Mark tasks as completed.
- **Remove Tasks:** Remove tasks from your list.
- **Save Tasks:** Save your tasks to a JSON file to maintain your progress.
- **Load Tasks:** Load your tasks from a JSON file when you start the application.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/gitnayandas/ToDo-App.git
    ```
2. Navigate to the project directory:
    ```sh
    cd todo-app
    ```
3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Requirements

- Python 3.x
- `ttkthemes` package
- `tkinter` package (usually included with Python)

You can install the required Python packages using:
```sh
pip install ttkthemes
```

## Usage

Run the application using:
```sh
python todo_app.py
```

## Code Overview

### Main Components

1. **TodoApp Class:** This is the main class that initializes the application, sets up the UI, and handles task operations.
2. **add_task Method:** Adds a new task to the list.
3. **remove_task Method:** Removes a specified task from the list.
4. **complete_task Method:** Toggles the completion status of a task.
5. **show_tasks Method:** Displays the tasks in the UI.
6. **save_tasks Method:** Saves the current tasks to a JSON file.
7. **load_tasks Method:** Loads tasks from a JSON file.
8. **update_tasks Method:** Periodically updates the tasks display.

### Custom Styles

The application uses custom styles for completed and pending tasks:
```python
style = ttk.Style(root)
style.configure("Completed.TLabel", foreground="green")
style.configure("Pending.TLabel", foreground="black")
```

## Contributing

Feel free to fork this repository and make changes. Pull requests are welcome!


## Contact

If you have any questions or suggestions, please feel free to contact me at [nayanchandradas@hotmail.com].

---

Thank you for using this ToDo App! Don't forget to star the repository if you found it useful! 🌟

Happy coding!
