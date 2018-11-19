//
//  Reverse_Polish_Stack.cpp
//  Reverse_Polish_Stack
//
//  Created by HAE SUNG JEONG on 1/28/18.
//  Copyright © 2018 HAE SUNG JEONG. All rights reserved.
//

#include <iostream>
#include <string>
#include <sstream>
using namespace std;

// class for the divide by zero exception
class DivByZeroExp
{
private:
    const char *mes;
public:
    DivByZeroExp()
        : mes ("Error: Division by Zero") {}
    const char *print() const {return mes;}
};

//Linked List start
class Node
{
public:
    double num;
    class Node *next;
    Node(double data, Node *ptr = 0)
    {
        num  = data;
        next = ptr;
    }
};

class List
{
private:
    Node *top;
    int count;
public:
    List()
    {
        top = 0;
        count = 0;
    }
    bool isEmpty()
    {
        return top == 0;
    }
    void push(double data)
    {
        Node *temp = new Node(data);
        if (isEmpty())
            top = temp;
        else
        {
            temp->next = top;
            top = temp;
        }
        count++;
    }
    
    double pop()
    {
        if (isEmpty())
            return -999;
        double dreturn = top -> num;
        Node *temp;
        temp = top;
        top = top ->next;
        delete temp;
        count--;
        return dreturn;
    }
    
    void print()
    {
        cout << "The stack: ";
        
        for (Node *temp = top; temp != 0; temp=temp->next)
            cout << temp->num << " ";
        cout << endl << "There are " << count << " number of elements." << endl;
    }
    
    int getCount()
    {
        return count;
    }
};
// Linked list end

// check if the input is one of the operators
bool isOperator(string in)
{
    if (in == "+")
        return true;
    else if (in == "-")
        return true;
    else if (in == "*")
        return true;
    else if (in == "/")
        return true;
    else
        return false;
}

// divide two doubles
double divide(double a, double b)
{
    if (b == 0)
        throw DivByZeroExp();
    return a / b;
}

int main(int argc, const char * argv[]) {
    // declare the linked list and require variables
    List operation;
    string s, operators;
    double num, op1, op2, res = 0.0;
    cout << "Reverse Polish Notation Caclulator" << endl;
    cout << "Please Enter the expression: " << endl;
    
    // until the input is "=" the loop generates
    while (s != "=")
    {
        cin >> s;
        if (istringstream(s) >> num)
        {
            operation.push(num);
        }
        else if (isOperator(s))
        {
            if (operation.getCount() < 2)
            {
                cout << "Error: Too many operator" << endl;
                exit(0);
            }
            op2 = operation.pop();
            op1 = operation.pop();
            if (s == "+")
                res = op1 + op2;
            else if (s == "-")
                res = op1 - op2;
            else if (s == "*")
                res = op1 * op2;
            else if (s == "/")
                try{
                    res = divide(op1, op2);
                }
                catch (DivByZeroExp e){
                    cout << e.print() << endl;
                    exit(0);
                }
            operation.push(res);
        }
    }
    if (operation.getCount() >= 2)
    {
        cout << "Error: Too many operands" << endl;
        exit(0);
    }
    cout << res << endl;
    system("pause");
    return 0;
}
