//
//  linked_based_stack.cpp
//  Linked_Based_Stack
//
//  Created by HAE SUNG JEONG on 1/24/18.
//  Copyright © 2018 HAE SUNG JEONG. All rights reserved.
//

#include <iostream>
using namespace std;

class Node
{
public:
    int count;
    class Node *next;
    Node(int data, Node *ptr = 0)
    {
        count  = data;
        next = ptr;
    }
};

class List
{
private:
    Node *top;
public:
    List()
    {
        top = 0;
    }
    bool isEmpty()
    {
        return top == 0;
    }
    void push(int data)
    {
        Node *temp = new Node(data);
        if (isEmpty())
            top = temp;
        else
        {
            temp->next = top;
            top = temp;
        }
    }
    
    int pop()
    {
        if (isEmpty())
            return -999;
        int intreturn = top -> count;
        Node *temp;
        temp = top;
        top = top ->next;
        delete temp;
        return intreturn;
    }
    
    void print()
    {
        cout << "The stack (from the top): ";
        
        for (Node *temp = top; temp != 0; temp=temp->next)
            cout << temp->count << " ";
        cout << endl;
    }
};
int main(int argc, const char * argv[]) {
    List linkedtemplate;
    
    linkedtemplate.push(10);
    linkedtemplate.print();
    linkedtemplate.push(15);
    linkedtemplate.print();
    linkedtemplate.push(20);
    linkedtemplate.print();
    cout << "pop: " << linkedtemplate.pop() << endl;
    linkedtemplate.print();
    system("pause");
    return 0;
}
