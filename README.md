
# C++ Coding Style Guide
## Introduction
#### This document provides guidelines for writing C++ code using the K&R method. The K&R style is a popular coding style for C and C++ that emphasizes readability and simplicity. The style is named after the authors of "The C Programming Language," Brian Kernighan and Dennis Ritchie.

Naming Conventions
Use descriptive names for variables, functions, and classes. Avoid single-letter variable names.
Use camelCase for variable and function names.
Use PascalCase for class names.
Use UPPER_CASE for constants.
Prefix private member variables with an underscore.
```
cpp
int numStudents;
void calculateAverageScore();
class StudentRecord;
const int MAX_SCORE = 100;
private:
  int _grade;
```
## Indentation
Use 4 spaces for indentation.
Use spaces instead of tabs.
```
cpp
if (condition) {
    // do something
} else {
    // do something else
}
```
## Braces
Place opening braces on the same line as the statement or declaration.
Place closing braces on a new line.
```
cpp
if (condition) {
    // do something
} else {
    // do something else
}
```
## Line Length
Limit lines to 80 characters.
Break long lines at logical points, such as after a comma.
```
cpp
void displayStudentRecord(const StudentRecord& record, bool showDetails) {
    cout << "Name: " << record.getName()
         << ", Age: " << record.getAge()
         << ", Gender: " << record.getGender();
    if (showDetails) {
        cout << ", GPA: " << record.getGPA()
             << ", Major: " << record.getMajor();
    }
    cout << endl;
}
```
## Comments
Use comments to explain the purpose and behavior of code.
Place comments on a separate line above the code they describe.
Use a blank line before and after a block of comments.
```
cpp
// This function calculates the average score of a list of scores.
// It takes a vector of integers as input and returns a double value.
double calculateAverageScore(const vector<int>& scores) {
    // Calculate the sum of scores
    int sum = 0;
    for (int score : scores) {
        sum += score;
    }
    // Calculate the average score
    double average = static_cast<double>(sum) / scores.size();
    // Return the average score
    return average;
}
```
