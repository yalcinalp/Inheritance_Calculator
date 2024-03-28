# Inheritance_Calculator
<br />Automated Legacy Calculator Under Turkish Inheritance Law
<br />Program considers many different inheritance cases (Tested)
<br />You can review the cases and legacy rules in Implementation Details.pdf file 

![image](https://github.com/yalcinalp/Inheritance_Calculator/assets/95969634/927d49ad-09e9-4252-b6a3-497339e3d00d)

# How the descendants partake a share

![image](https://github.com/yalcinalp/Inheritance_Calculator/assets/95969634/0027ba0d-ceb9-4644-8869-b0f918711e16)

# Example Case

![image](https://github.com/yalcinalp/Inheritance_Calculator/assets/95969634/184630a7-c30c-4d10-a0c4-e75650df4bb3)

# SAMPLE RUN  
We will use the tree in Figure 2 for the sample run. 
 
```
Descriptions = [
"CHILD jale giray kaan",
"CHILD faika enes giray",
"CHILD banu ali enes",
"CHILD ahu ali halil mert",
"CHILD dilek celil faika",
"CHILD ayse mert ismet lutfi",
"MARRIED giray jale",
"MARRIED faika enes",
"MARRIED ali banu",
"MARRIED celil dilek",
"DEPARTED ali",
"DEPARTED mert",
"DEPARTED enes",
"DEPARTED faika",
"DEPARTED giray",
"DEPARTED kaan"
]

>>> Example1 = Descriptions + ["DECEASED mert 100"] # First PG
>>> inheritance(Example1)

[(’ismet’, 50.0), (’lutfi’, 50.0)]

>>> Example2 = Descriptions + ["DECEASED enes 120"] # Second PG
>>> inheritance(Example2)

[(’banu’, 60.0), (’halil’, 30.0), (’ismet’, 15.0), (’lutfi’, 15.0)]

>>> Example3 = Descriptions + ["DECEASED giray 480"] # Third PG
>>> inheritance(Example3)

[(’jale’, 360.0), (’dilek’, 30.0), (’celil’, 30.0), (’banu’, 30.0),
(’halil’, 15.0), (’ismet’, 7.5), (’lutfi’, 7.5)]
```
