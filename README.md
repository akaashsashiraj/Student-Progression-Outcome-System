# Student Progression Outcome System

## Overview
This Python-based system determines students' progression outcomes based on their module credits. The program allows both students and staff to input credit values and provides appropriate progression results. Staff users also have access to a graphical representation of the collected data.

## Features
- **Student Mode**: Allows students to enter their credit details and receive a progression outcome (e.g., Progress, Module Retriever, Exclude, etc.).
- **Staff Mode**: Enables staff members to input multiple student records and view a graphical summary of the results.
- **Validation Checks**: Ensures that the total credits always sum up to 120 and provides error messages for incorrect inputs.
- **Graphical Output**: Staff members can visualize student progression trends using graphs.

## Technologies Used
- **Language**: Python 3
- **Libraries**: Matplotlib (for graphical output)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/Student-Progression-System.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Student-Progression-System
   ```
3. Run the program:
   ```sh
   python w2051998.py
   ```

## Usage
1. The system will prompt the user to select whether they are a **Student** or **Staff**.
2. Students can enter their module credits (Pass, Defer, Fail) and receive an immediate progression outcome.
3. Staff can enter multiple records and choose to view a **graphical summary** of the results.

## Example Output
```
Are you Staff or Student?
If you are a Staff enter 'staff' or Student enter 'student': student
Enter the number of credits at pass: 60
Enter the number of credits at defer: 40
Enter the number of credits at fail: 20
Progression outcome: Module Retriever
```

## Contributing
Contributions are welcome! Feel free to fork this repository and submit a pull request.



