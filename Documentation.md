# Data Science Project
## Phase 1 - Identifying & Defining
### Mindmap:
![Mind Map](image.png)
### Hypothesis
Students who take part in extracurricular activities overall enjoy school more than those who don’t, or do less.
### Requirements Outline
#### Functional
In order for my program to meet its functional goal it must adhere to a set of requirements. My program should be able to load in data in a format such as .csv, my program will not be required to handle errors in loading as my data will have already been corrected. For the same reason that my program will not have to handle file errors, my program won’t be required to handle missing or error values. My program will be required to find the mean of some aspects of the data to allow for data visualization. My program is required to use both PANDAS and MATPLOTLIB for easy visualization through data frames and graphs/charts, utilising dataframes, bar charts, and line graphs. My data will be stored as a .csv file which will allow me to easily access the data in my program.
#### Non-Functional
In order for my program to adhere to its non-functional requirements it must meet 2 main goals, usability and reliability. For usability my program will need a helpful and informative README, which outlines; installation instructions, required Libraries, how to run the program, example usage, and a troubleshooting section. The program itself must also have an intuitive menu, it isn’t required to have a graphical user interface, but an easy to use text based interface. For reliability, the program must be able to validate all user interfaces, prevent data corruption, provide clear error messages when any process or input fails, and make sure no change to the data occurs without user confirmation.

#### Use Case
Actor: User

Goal: To access and interact with existing data through the program’s user interface.

Preconditions:

The dataset has already been preloaded into the system by myself.

The user has access to the system.

Main Flow:

After launching the program, a text menu appears for the user to choose from

Using the text menu User selects one of the following options: 
- View & Sort Data
- View visualisation (e.g., chart or graph of selected data) 
- Search or filter data based on specific criteria 
- Veiw data Statistics
- Compare Fields
- Quit

The system carries out the selected action and displays the result to the user.

Postconditions:

Dataset is unaffected
User is returned to Main Flow (Repeated until user quits)

Information remains available for additional searching or review
## Phase 2 - Researching & Planning
### Research
Data or information available on my topic is very limited, and if their is any of it it's not easy processed down into usable data. This made it so I was required to make a survey, which although more work allowed me to pinpoint the specific information I need. 

Due to the fact of my data only collectable through a survey, I created a survey to collect the sufficient data to either prove or disprove my hypothesis. I collected data on Gosford High School students extracurriculars, extracuricular hours, opinion of school and opinion of break. These fields are essential to my hypotheses, as I am trying to observe the effect of extracuricular hours on opinion of school and opinion of break.

### Findings
As I did not conduct research for my project, there was not much information collected. Although there was nothing to be collected through research, I created a survey and the data collected has not revealed anything at this point. My system will allow me to take these findings and prove or disprove my hypothesis through visualisation or comparison of the data sets. As I continue analysing the data, clearer patterns may begin to emerge that will help guide my final evaluation.
### Data
100% of my data was collected by my survey.
#### Survey: https://forms.gle/78fqpbPkFroJuN8u7

### Planning
#### Data Dictionary
| Field | Data Type | Format | Description | Example | Validation |
| - | - | - | - | - | - |
| Extra Curriculars | str (categorical) | XX...XX | Voluntary, non-academic pursuits undertaken by students outside of regular school curriculum | Scouts;Swimming;Other | Any string, excluding numbers, each string separated by semicolons (;) |
| Extra Curricular Hours / Week | int64 (hours per week) | NN | Number of hours taking part in Extracurricular Activities | 20 | 1-2 digit(s) (0-20)
| School Opinion | int64 (1-10 rating) | N | Opinion on school overall, excluding breaktime | 6 | Single digit (0-9)
| Breaktime Opinion | int64 (1-10 rating) | N | Opinion on breaktime overall, including recess, lunch, before and after school, and free periods.  | 7 | Single digit (0-9)
## Phase 3 - Producing & Implementing
### Python Libaries & Files
Libraries
- Pandas (Python data analysis library)
- Matplotlib (Python data visualisation / plotting library)

Project Files
- Main.py (main Python script / program entry point)
- Data_Module.py (data‑handling functions / processing module)
- README.md (project overview + instructions)
- Documentation.md (detailed explanations / technical notes)
- Data Science Project.csv (dataset used for analysis)

### Version Control - (Missed Comit Summaries)
Some of my commits before I started apllying proper summaries & descriptions are still blank, and I can't change them so here is what I completed between each commit:

(Organized In Earliest to Most Recent Commit)

5c50639653b866a1034a5b0198703a355629e06d - Start of Markdown File (Structured entire markdown, paving the way for what I needed to do as well as allowing for me to see the scope of the project.)

6318119e5d662dd33a028531d0a3f20da1513b81 - CSV & Survey (Installed CSV from survey, as well as linking survey used to Markdown.)

d2a35a7d7d2f9a93360e14612dcf81ae4b5890aa -  Usecase (Added Usecase template to Markdown.)

e27588779983a46cef49cff98b6dd6883abadee3 - CSV Update & Main Function (Updated completed survey data. Created main loop, and planned function roles. Created README.)

62556a4de9560c633550d5dc4753148bee24777e -  Fucntion Groundwork (Installed most operators, and created clear_screen() function.)

cfe28e968cc65d653b7c26525d34ddc03c0a4051 - Finalised CSV file

574fcdc1dc888465e25681b8f562b2d391e32b5a - Phase 1 Documentation

29a9450e0c0c6584ccf7738395c5efddd77efad7 - Start of Code (I started proper coding, experimenting with matplotlib making sure that It could read/worked with my data frame.)

1d9c212ae63d7acdb128ba2da9c95543412fced4 - Pandas Instilation

Skip 4 Commits - (Some what summarised & described)

fc7c41479da972e7f58b36df5452e10415372259 - Empty

Start of Useful Commit Summarys & Descriptions

## Phase 4 - Testing & Evaluating
### Test
My analylasis works correctly, my algorythyms all provide accurate, useful results.
### Analysis
Based on the numerical evidence and visualisations created by my survey dataset and anylasis system, my original hypothesis was not supported. The data shows no significant relationship between extracurricular hours and students’ enjoyment of school or breaktime. While extracurricular activities may still provide personal benefits, they do not influence overall school satisfaction found in this dataset. Further research with a larger sample size or additional wellbeing factors may reveal more complex relationships. interactions.
### Peer Verification
Max Edmunds's PMI
| Plus | Minus | Implication |
| - | - | - |
| The program runs flawlessly and without error (with the exception of unnecessary spamming). UI looks really nice and options are clear and easy to understand. The code can be cycled through endlessly - you can't get stuck at any point. Data statistics all work and show exact measurements. The tables have good data and are in order. | There could be animations to add more flavour to the already good UI. There is no update data feature so data cannot be changed in any way. More data tables could be added for extra analysis and makes it more reliable and valid when in comparison to the hypothesis. README hasn't been done, however the data is easy enough to understand. | In the future, more data could be originally collected and visualised - there could be more choice in the tables and in comparing certain activities rather than set lists. More options can be added to enhance the data, and add-ons such as animations to go with the good-looking system. Overall it's not about what you included to break the code, but what you didn't include that would make it more effective. |
### Evaluation
- I didnt use data update
