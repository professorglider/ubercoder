# Ubercoder and Create Project Script

This documentation describes the Ubercoder JSON format and the `create_project.py` script, which automates the process of setting up projects based on the Ubercoder JSON format.

You may ask GPT-4 to answer using this format if you're tired of the programmer's last resort: copy-pasting :P

## Ubercoder JSON Format

The Ubercoder JSON format is a universal, computer-readable format for project declaration. It specifies the folder structure, commands, and files required for a project.

The format consists of the following main keys:

- `project_name` (string): The name of the project.
- `folders` (array): An array of folder objects that represent the folder structure.
- `commands` (array): An array of command objects that are required to set up or run the project.
- `files` (array): An array of file objects that define the project files and their contents.

### Folder Object

A folder object has the following keys:

- `name` (string): The name of the folder.
- `subfolders` (array, optional): An array of folder objects representing subfolders.

### Command Object

A command object has the following keys:

- `description` (string): A short description of the command's purpose.
- `command` (string): The command to execute.

### File Object

A file object has the following keys:

- `name` (string): The file path relative to the project root.
- `content` (string): The content of the file.

## Create Project Script

The `create_project.py` script reads an Ubercoder JSON file and automatically creates the project folder structure, files, and executes the specified commands.

### Usage

1. Save your Ubercoder JSON file, for example, as `my_project.json`.
2. Update the `create_project.py` script to reference your JSON file: json_file = "my_project.json"
3. Run python create_project.py

## Tic Tac Toe example
tic_tac_toe_project.json:
```json
{
  "project_name": "tic_tac_toe",
  "folders": [
    {
      "name": "app",
      "subfolders": [
        {
          "name": "static",
          "subfolders": [
            {
              "name": "css"
            },
            {
              "name": "js"
            }
          ]
        }
      ]
    }
  ],
  "commands": [],
  "files": [
    {
      "name": "app/index.html",
      "content": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>Tic Tac Toe</title>\n    <link rel=\"stylesheet\" href=\"static/css/style.css\">\n</head>\n<body>\n    <h1>Tic Tac Toe</h1>\n    <div id=\"game-board\">\n        <div class=\"cell\" data-cell></div>\n        <div class=\"cell\" data-cell></div>\n        <div class=\"cell\" data-cell></div>\n        <div class=\"cell\" data-cell></div>\n        <div class=\"cell\" data-cell></div>\n        <div class=\"cell\" data-cell></div>\n        <div class=\"cell\" data-cell></div>\n        <div class=\"cell\" data-cell></div>\n        <div class=\"cell\" data-cell></div>\n    </div>\n    <script src=\"static/js/script.js\"></script>\n</body>\n</html>"
    },
    {
      "name": "app/static/css/style.css",
      "content": "body {\n    font-family: Arial, sans-serif;\n    text-align: center;\n}\n\n#game-board {\n    display: grid;\n    grid-template-columns: repeat(3, 100px);\n    grid-template-rows: repeat(3, 100px);\n    gap: 5px;\n    margin: 50px auto;\n    width: 320px;\n}\n\n.cell {\n    background-color: lightgray;\n    border: 1px solid black;\n    display: flex;\n    align-items: center;\n    justify-content: center;\n    font-size: 24px;\n    font-weight: bold;\n    height: 100px;\n    width: 100px;\n}\n\n.cell[data-player=\"X\"] {\n    color: red;\n}\n\n.cell[data-player=\"O\"] {\n    color: blue;\n}"
    },
    {
      "name": "app/static/js/script.js",
            "content": "const cells = document.querySelectorAll('[data-cell]');\nlet currentPlayer = 'X';\n\ncells.forEach(cell => {\n    cell.addEventListener('click', handleClick, { once: true });\n});\n\nfunction handleClick(e) {\n    const cell = e.target;\n    cell.textContent = currentPlayer;\n    cell.setAttribute('data-player', currentPlayer);\n    if (checkWin(currentPlayer) || checkDraw()) {\n        setTimeout(() => {\n            resetBoard();\n        }, 2000);\n    } else {\n        currentPlayer = currentPlayer === 'X' ? 'O' : 'X';\n    }\n}\n\nfunction checkWin(player) {\n    const winningCombinations = [\n        [0, 1, 2], [3, 4, 5], [6, 7, 8],\n        [0, 3, 6], [1, 4, 7], [2, 5, 8],\n        [0, 4, 8], [2, 4, 6]\n    ];\n\n    return winningCombinations.some(combination => {\n        return combination.every(index => {\n            return cells[index].getAttribute('data-player') === player;\n        });\n    });\n}\n\nfunction checkDraw() {\n    return [...cells].every(cell => {\n        return cell.getAttribute('data-player') !== null;\n    });\n}\n\nfunction resetBoard() {\n    cells.forEach(cell => {\n        cell.textContent = '';\n        cell.removeAttribute('data-player');\n        cell.addEventListener('click', handleClick, { once: true });\n    });\n    currentPlayer = 'X';\n}"
    }
  ]
}
```

