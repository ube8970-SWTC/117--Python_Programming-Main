# Product or service Selection

A working console demo of a completed capstone for **10-152-117 Python Programming**. The project follows the [Week 7 capstone proposal](../../Week_07_RBA_and_Project_Framing/05_capstone_proposal_example.md) and supports the Week 8 build justification and presentation activities.

## What the Application Does

Customers can see available products, their pricing and make a selection for what they would like. The summary shows the selected products, the total cost, and contact information if the custom work is selected. 

## Requirements and Running

Install Python 3.6 or later. The project uses only Python's standard library; no additional packages are required.

Open a terminal in this `Week_8` folder and run:

```powershell
capstone.py
this is the main presentation
or
capstone_optional_feature.py
this has all the optional features added and is better
```

Choose an option from the menu:

1. Cluster Lighting - $220
2. Cluster Rebuild - $250
3. Offroad Lighting - $400
Lower items are only in "capstone_optional_feature.py"
4. Alternative Switch Lighting - $150
5. Roof Rack Lighting - $300
6. Custom Work - $350

When selecting a product, enter its corresponding number ex. 1-6.

## Relationship Between the Python Files
Each file is independent of each other, they don't interact and hold all their code within themselves

## Project Files

| File | Purpose |
| --- | --- |
| [capstone.py] | Original capstone file before any added features  |
| [Capstone_optional_feature.py] | Capstone file with multiple added features |

## Suggested Demonstration

1. Open Capstone_optional_feature.py
2. Start the application and read the selected products
3. Select 1-6 products including #6
4. Deslection menu should appear, deselect 1-3 products
5. Type done after selection is made to see total billing
6. Show that when #6 custom work is selected, a Contact me line will appear. 
7. Run twice to show everything incase it's needed

## Scope and Limits

Deadlines, editing, deletion, and additional analytics remain backlog items. The first version focuses on lists, dictionaries, functions, loops, and input validation.

The loader handles a missing file, invalid JSON, and a top-level value that is not a list. It assumes each saved task contains the expected fields and types; it does not validate every record or handle all operating-system file errors.