# **Python Applications**

## **Sections of a Python File**
While there is no one way to write a python file this will serve as a good starting point for those new to python.
### **Dependencies / Imports**
Every python file ***must*** begin with the require packages to be imported. This will also be the appropriate place to leave critical comments such as if a specific version of python is required.
```python
#python==3.8.10

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```
### **Local Imports**
Local imports are `.py` files meant to assist with the running of your current script. Perhaps you are analyzing historic financial data and you have already built a function called `adjust_4_inflation()` within `inflation_adjusted.py` that you would like to reuse. If the two files are in the same directory, you can import it as follows:
```python
from inflation_adjusted import adjust_4_inflation
```

### Variables
The variables defined here will be those which are use repeatedly within the rest of the file. Using the example above of inflation you could denote this rate in a several ways.
```python
inflation2021 = 0.07 #  Single stored value

inflation = {
  '2021':0.070,
  '2020':0.014,      #  Dictionary of stored values
  '2019':0.023,
  '2018':0.019
}
```

### Classes / Functions
Classes are one of the most fundamental aspects of python programing and are made up of attributes and methods. Classes define an object in python. To be instantiated each class must at contain the attribute `self`. Functions take `arguments` and use them to perform tasks.
```python
# Example of a class definition
class student:
    def __init__(self, name:str, grade:str, school:str, score1:float, score2:float):   ###
        self.name = name                                                                 #
        self.grade = grade                                                               #  This defines the attributes 
        self.school = school                                                             #
        self.score1 = score1                                                             #
        self.score2 = score2                                                           ###
    
    def avg_score(self):                         
        return (self.score1+self.score2)/2   # This is a method
 
 
# Example of a function definition
def score_avg(scores:list):
    return sum(scores)/len(scores)
```

### Code Body
This portion of the file is where the core data manipulations and transformation should take place. this will often start with reading and cleaning data and end with the eventual export of the data. In between those steps can include many tasks such as running functions and instantiating classes.
```python
 # Example of class instance, this would be referred to as a <class> object or in this case a student object.
tommy = student('tommy', '3', 'school', 95, 78)

tommy.grade          # Result: '3'

tommy.avg_score()    # Result: 86.5

score_avg([95, 78])  # Result: 86.5
```

## **Types of Python Files**
### **Traditional**
Traditional python files are those ending with the `.py` extension. These files are typically ran from a shell within a virtual environment. This is the predominant file type for production ready applications.

### **Notebooks**
Python notebooks allow a user to merge text, html, video, images, code, and other mediums into the same document. Jupyter notebooks will have the file extension `.ipynb`. For more information on Jupyter notebooks see the [docs](https://docs.jupyter.org/en/latest/).



## **Special Operators**
- `#` is a comments operator. When placed on a line, all code that comes after it becomes non-executable.
```python
example = 'This code will be executed' # example = 'This code will not'
```
- `''''''` denotes a multi-line string. It is often used for multiline comments.
```python
'''
This is all 
part of the 
same string 
'''
```
- `\` is an escape character. This is often used to denote a literal component of a string.
```python
'\'' # this is the string '
''' # this will throw an error
```

##  **Filling Out the Directory**

### requirements.txt
A requirements file is an essential part of maintaining code in python and should be written for all python projects regardless of whether the project uses `.py` , `.ipynb` files, or both. A requirements file allows a user to recreate the environment in which the program is designed to run.  Requirements files should only include packages used in the project as the inclusion of extraneous packages can bloat the size of the end product making it harder to deploy at scale.

```text
numpy==1.18.5  # This is a requirement with specified version
pandas==1.2.4   # It is recommended to specify version to reduce risk of incompatibility and anomalous behavior
pathlib        # In this case pathlib will package will use the most current available version
```

If you are unsure of the packge versions in you current development you can obtain a list by running the following commands in your terminal with the desired environment active:
```cmd
pip list
```
OR
```cmd
pip freeze
```


