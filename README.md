Browser Tabs Automator
This is a simple Python application built using Tkinter for managing and opening website URLs. The application allows users to add URLs to predefined categories, create new categories, and open 
all URLs in a selected category in their default web browser.

Features
Add URL to Category: Add new URLs to existing categories.
Open URLs: Open all URLs in a selected category.
Add New Category: Create new categories for organizing URLs.

###Installation
1.Clone the repository:

git clone https://github.com/aryannate/browser-tabs-automator.git
cd browser-tabs-automator

2.Install the required dependencies:
-The only dependency required is Tkinter, which is included with Python. No additional packages are needed.

3.Run the application:

python browser_tabs_automator.py


##Usage
1.Add URL to Category:
-Select a category from the dropdown menu.
Enter the new URL in the text entry field.
Click the "Add URL" button to save the URL to the selected category.

2.Open URLs:
-Select a category from the dropdown menu.
Click the "Open URLs" button to open all URLs in the selected category in new browser tabs.

3.Add New Category:
-Enter the name of the new category in the text entry field.
Click the "Add Category" button to create the new category.

##File Structure
browser_tabs_automator.py: The main script containing the Tkinter application.
urls.json: A JSON file used to store the URLs and categories. This file is created automatically when the application runs for the first time.
