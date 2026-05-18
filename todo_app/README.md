# EasyToDo - Simple To-Do List Application

A beginner-friendly Python to-do list application with **dual storage** (JSON + SQLite) using tkinter for a simple Windows-style interface.

## 🎯 Features

✅ **Dual Storage System**
- Automatically saves to `todos.json` (human-readable)
- Automatically saves to `todos.db` (SQLite database)
- Both formats stay in sync

✅ **Simple Features**
- Add, edit, delete, and mark tasks as complete
- Organize tasks by categories (General, Work, Personal, Shopping, Other)
- Filter tasks (All, Pending, Completed)
- View task statistics (total, completed, pending, progress percentage)

✅ **Easy-to-Use Interface**
- Windows-style tkinter GUI
- No command line needed
- Beginner-friendly buttons and dialogs

✅ **No Dependencies**
- Uses only Python built-in modules
- Works on Windows, Mac, and Linux
- Just `python main.py` to start!

## 📦 Installation

1. Clone or download the repository
2. Ensure you have Python 3.6+ installed
3. No additional packages needed!

## 🚀 How to Run

```bash
cd todo_app
python main.py
```

The app will create a `data/` folder with both storage files automatically.

## 📂 File Structure

```
todo_app/
├── main.py                      # Start here!
├── gui/
│   ├── __init__.py
│   └── main_window.py          # Main GUI window
├── storage/
│   ├── __init__.py
│   └── storage_manager.py      # Dual storage manager
└── data/                        # Created automatically
    ├── todos.json              # JSON backup
    └── todos.db                # SQLite database
```

## 💡 How to Use

### Adding a Task
1. Click **➕ Add Task**
2. Enter task title (required)
3. Add description (optional)
4. Select category
5. Click **Save Task**

### Editing a Task
1. Select a task from the list
2. Click **✏️ Edit**
3. Modify the details
4. Click **Save Changes**

### Marking Tasks Complete
1. Select a task
2. Click **✓ Toggle Done**
- The task will show ✓ when completed, ○ when pending

### Deleting a Task
1. Select a task
2. Click **🗑️ Delete**
3. Confirm deletion

### Filtering Tasks
- **All**: Show all tasks
- **Pending**: Show incomplete tasks only
- **Completed**: Show completed tasks only

## 📊 Storage Details

### JSON Format (`todos.json`)
Human-readable format perfect for backups and manual editing:
```json
[
  {
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, bread, eggs",
    "category": "Shopping",
    "completed": false,
    "created_at": "2026-05-18T10:30:00.123456",
    "updated_at": "2026-05-18T10:30:00.123456"
  }
]
```

### SQLite Format (`todos.db`)
Database format for queries and advanced use:
```
Table: todos
- id (PRIMARY KEY)
- title (TEXT)
- description (TEXT)
- category (TEXT)
- completed (INTEGER: 0 or 1)
- created_at (TEXT)
- updated_at (TEXT)
```

## 🎨 Color Scheme

- **Dark Blue Header**: Application title
- **Green**: Add button (positive action)
- **Blue**: Edit button
- **Orange**: Toggle completion
- **Red**: Delete button (destructive)
- **Light Gray**: Background (non-intrusive)

## ⚙️ Troubleshooting

**Q: "No module named tkinter"**
- Windows: tkinter is included with Python
- Mac: `brew install python-tk`
- Linux: `sudo apt-get install python3-tk`

**Q: Where are my tasks saved?**
- Check `data/` folder in the same directory as `main.py`
- `todos.json` - text format
- `todos.db` - database format

**Q: Can I share my database?**
- Yes! Just share the `todos.db` file or `todos.json` file
- The app automatically syncs both

**Q: Can I edit the JSON directly?**
- Yes, but you must maintain the JSON structure
- After editing, restart the app to see changes

## 🔄 Dual Storage Workflow

1. **You add a task** → Saved to JSON + SQLite
2. **You edit a task** → Updated in JSON + SQLite
3. **You delete a task** → Removed from JSON + SQLite
4. **You restart app** → Both files stay in perfect sync

Perfect for backups and data reliability!

## 📝 Tips for Students

- Use categories to stay organized
- Check the progress bar to track your accomplishments
- Your data is saved instantly - no need to manually save!
- Share tasks with friends by exporting the JSON file

## 📄 License

Feel free to use, modify, and share this project!

---

**Made with ❤️ for students who want simple database applications**

Questions or issues? Check the repository on GitHub!
