//
//  finalproject.cpp
//  Final Project
//
//  Created by HAE SUNG JEONG on 12/8/17.
//  Copyright © 2017 HAE SUNG JEONG. All rights reserved.
//

#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include<iomanip>
using namespace std;

class Grade
{
public:
    Grade(const char *, const char *);
    ~Grade();
    virtual float calcGrade() = 0;
    virtual float calc(float *, float, int);
    virtual char letter();
    virtual void print();
private:
    char lettergrade;
    float gpa;
    float lab;
    float classroom;
    char *firstName;
    char *lastName;
};

Grade::Grade(const char *first, const char *last)
{
    firstName = new char[strlen(first) + 1];
    strcpy(firstName,first);
    lastName = new char[strlen(last) + 1];
    strcpy(lastName,last);
}


void Grade::print()
{
    cout << firstName << " " << lastName << endl;
}

char Grade::letter()
{
    gpa = calcGrade();
    if (gpa >= 90)
        lettergrade = 'A';
    else if (gpa >= 80)
        lettergrade = 'B';
    else if (gpa >= 70)
        lettergrade = 'C';
    else if (gpa >= 60)
        lettergrade = 'D';
    else
        lettergrade = 'F';
    return lettergrade;
}
Grade::~Grade()
{
    delete[] firstName;
    delete[] lastName;
}

float Grade::calc(float *grade, float max, int num)
{
    float sum = 0;
    for (int i = 0; i < num; i++)
    {
        sum += grade[i];
    }
    return lab = sum /(float)max * 100;
}


class Socio: public Grade
{
public:
    Socio(const char *, const char *, const int, float[], int, float, float[],int, float);
    float calcGrade();
    void print();
    float calclab(float[], float, int);
    float calcClass(float[], float, int);
private:
    float lab;
    float classroom;
    int course;
};

Socio::Socio(const char *first, const char *last, const int coursNum, float *labgrade, int numlab,float lab_max, float *classgrade,int numclass,float class_max)
: Grade(first, last)
{
    course = coursNum;
    lab = calclab(labgrade ,lab_max, numlab);
    classroom = calcClass(classgrade,class_max, numclass);
}

float Socio::calcGrade()
{
    return (lab + classroom) / (float)2;
}

void Socio::print()
{
    cout << course << " Sociology Course: " << endl;
    Grade::print();
    cout << "Lab Percentage: " << lab << endl << "Classroom Percentage: " << classroom << endl;
    cout << "Grade: " << Grade::letter() << endl << "Final Percentage: " << calcGrade() << endl << endl << endl;
}

float Socio::calclab(float *labgrade, float max, int numlab)
{
    return lab = Grade::calc(labgrade, max, numlab);
}

float Socio::calcClass(float *classgrade, float max, int numclass)
{
    return classroom = Grade::calc(classgrade, max, numclass);
}

 class Math :public Grade
 {
 public:
     Math(const char *, const char *, const int, float*, int, float, float *, int, float, float *, int, float);
     float calcGrade();
     void print();
     float calcgpa(float*,float,int);
 private:
     float lab;
     float classroom;
     float exam;
     int course;
};

Math::Math(const char *first, const char *last, const int coursNum, float *labgrade, int numlab,float lab_max, float *classgrade,int numclass,float class_max, float *examgrade,int numexam, float exam_max)
: Grade(first, last)
{
    course = coursNum;
    lab = calcgpa(labgrade ,lab_max, numlab);
    classroom = calcgpa(classgrade,class_max, numclass);
    exam = calcgpa(examgrade, exam_max, numexam);
}

float Math::calcGrade()
{
    return (lab + classroom + exam) / (float) 3;
}

void Math::print()
{
    cout << course << " Math Course: " << endl;
    Grade::print();
    cout << "Lab Percentage: " << lab << endl << "Quiz Percentage: " << classroom << endl << "Exam Percentage: " << exam << endl;
    cout << "Grade: " << Grade::letter() << endl << "Final Percentage: " << calcGrade() << endl << endl << endl;
}

float Math::calcgpa(float *grade, float max, int num)
{
    int lowest = grade[0];
    int index = 0;
    for (int i = 1; i < num; i++)
    {
        if (lowest > grade[i])
        {
            lowest = grade[i];
            index = i;
        }
    }
    if (lowest != grade[num-1])
    {
        float temp = grade[num-1];
        grade[num-1] = lowest;
        grade[index] = temp;
    }
    return Grade::calc(grade, max, num-1);
}

class CompSci: public Grade
{
public:
    CompSci(const char *, const char *, const int, float*, int, float, float *, int, float, float);
    float calcGrade();
    void print();
    float calclab(float*,float,int);
    float calcClass(float*,float, int);
private:
    float lab;
    float exam;
    float finals;
    int course;
};

CompSci::CompSci(const char *first, const char *last, const int coursenum, float *labs, int numlab, float maxlab, float *exams,int numexam, float maxexam, float finalgrade) : Grade(first, last)
{
    lab = calclab(labs, maxlab, numlab);
    finals = finalgrade;
    exam = calcClass(exams, maxexam, numexam);
    course = coursenum;
}

float CompSci::calcGrade()
{
    return (lab + exam + finals) / (float) 3;
}

void CompSci::print()
{
    cout << course << " Computer Science Course: " << endl;
    Grade::print();
    cout << "Lab Percentage: " << lab << endl << "Exam Percentage: " << exam << endl << "Final Exam Percentage: " << finals << endl;
    if (finals > 40)
        cout << "Grade: " << Grade::letter() << endl << "Final Percentage: " << calcGrade() << endl << endl << endl;
    else
         cout << "Grade: F" << endl << "Final Percentage: " << calcGrade() << endl << endl << endl;
}

float CompSci::calclab(float *grades, float max, int num)
{
    return Grade::calc(grades, max, num);
}

float CompSci::calcClass(float *grades, float max, int num)
{
    float lowest = grades[0];
    int index = 0;
    for (int i = 0; i < num; i++)
        if (lowest > grades[i])
        {
            lowest = grades[i];
            index = i;
        }
    if (lowest < finals)
        grades[index] = finals;
    return Grade::calc(grades, max, num);
}

class Accounting: public Grade
{
public:
    Accounting(const char*, const char *, const int, float*, int, float, float);
    float calcGrade();
    void print();
    float calclab(float*, float, int);
private:
    float lab;
    float finalgrade;
    int course;
};

Accounting::Accounting(const char *first, const char *last, const int coursenum, float *labs, int numlab, float maxlab, float finals):Grade(first, last)
{
    lab = calclab(labs, maxlab, numlab);
    finalgrade = finals;
    course = coursenum;
}

void Accounting::print()
{
    cout << course << " Accounting Course: " << endl;
    Grade::print();
    cout << "Lab Percentage: " << lab << endl << "Final Exam Percentage: " << finalgrade << endl;
    cout << "Grade: " << Grade::letter() << endl << "Final Percentage: " << calcGrade() << endl << endl << endl;
}

float Accounting::calcGrade()
{
    return (lab + finalgrade) / (float) 2;
}

float Accounting::calclab(float * labs, float max, int num)
{
    return Grade::calc(labs, max, num);
}

int main()
{
    cout << fixed << showpoint << setprecision(2);
    float socio_lab[3] = {100.0,100.0,100.0};
    float socio_class[5] = {50.0,50.0,50.0,200,200};
    Socio sociology ("Joe", "Smith",62506, socio_lab,3, 300, socio_class,5, 550);
    float math_lab[3] = {80,90,100};
    float math_quiz[7] = {30,40,50};
    float math_exam[4] = {80,70,90,100};
    Math mathematics ("John", "Johnson", 62018 , math_lab,3,200,math_quiz,3,100, math_exam, 4, 300);
    float comp_lab[4] = {20,20,25,25};
    float comp_exam[2] = {70,50};
    float comp_final = 30;
    CompSci computer("Mark","Strong", 62719, comp_lab, 4, 100, comp_exam, 2, 200, comp_final);
    float acc_lab[5] = {100,70,80,81,93};
    float acc_final = 80;
    Accounting acc("Mary", "Jane", 62812,acc_lab,5,500,acc_final);
    sociology.print();
    mathematics.print();
    computer.print();
    acc.print();
    system("PAUSE");
    return 0;
}
/*
 62506 Sociology Course:
 Joe Smith
 Lab Percentage: 100.00
 Classroom Percentage: 100.00
 Grade: A
 Final Percentage: 100.00
 
 
 62018 Math Course:
 John Johnson
 Lab Percentage: 95.00
 Quiz Percentage: 90.00
 Exam Percentage: 90.00
 Grade: A
 Final Percentage: 91.67
 
 
 62719 Computer Science Course:
 Mark Strong
 Lab Percentage: 90.00
 Exam Percentage: 80.00
 Final Exam Percentage: 90.00
 Grade: B
 Final Percentage: 86.67
 
 
 62812 Accounting Course:
 Mary Jane
 Lab Percentage: 84.80
 Final Exam Percentage: 80.00
 Grade: B
 Final Percentage: 82.40                    When csi final exam score is above 40 points
*/

/*
 62506 Sociology Course:
 Joe Smith
 Lab Percentage: 100.00
 Classroom Percentage: 100.00
 Grade: A
 Final Percentage: 100.00
 
 
 62018 Math Course:
 John Johnson
 Lab Percentage: 95.00
 Quiz Percentage: 90.00
 Exam Percentage: 90.00
 Grade: A
 Final Percentage: 91.67
 
 
 62719 Computer Science Course:
 Mark Strong
 Lab Percentage: 90.00
 Exam Percentage: 60.00
 Final Exam Percentage: 30.00
 Grade: F
 Final Percentage: 60.00
 
 
 62812 Accounting Course:
 Mary Jane
 Lab Percentage: 84.80
 Final Exam Percentage: 80.00
 Grade: B
 Final Percentage: 82.40                       When csi final exam score is under 40 points
 */

