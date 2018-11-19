//
//  program2.cpp
//  Program2
//
//  Created by HAE SUNG JEONG on 2/21/18.
//  Copyright © 2018 HAE SUNG JEONG. All rights reserved.
//

#include <iostream>
#include <string>
using namespace std;

class Node
{
public:
    Node *next;
    int wgt;
    string name;
    Node(string s, int num)
    {
        wgt = num;
        name = s;
        next = 0;
    }
};

class List
{
private:
    Node *nameFront;
    Node *weightFront;
public:
    void push(string n, int w)
    {
        Node *temp = new Node(n, w);
        Node *curName = nameFront;
        Node *curWeight = weightFront;
        if (nameFront == 0 && weightFront == 0)
        {
            nameFront = temp;
            weightFront = temp;
        }
        else if (temp->name.compare(nameFront->name) < 0)
        {
            temp->next = nameFront;
            nameFront = temp;
        }
        else if (temp->name.compare(nameFront->name) > 0)
        {
            while (curName->next != 0 && curName->next->name < temp->name)
                curName = curName->next;
            temp->next = curName->next;
            curName->next = temp;
        }
        else if (temp->wgt < weightFront->wgt)
        {
            temp->next = weightFront;
            weightFront = temp;
        }
        else if (temp->wgt > weightFront->wgt)
        {
            curWeight = weightFront;
            while (curWeight->next != 0 && curWeight->next->wgt < temp->wgt)
                curWeight = curWeight->next;
            temp->next = curWeight->next;
            curWeight->next = temp;
        }
    }
 
    void printbyName()
    {
        cout << "Names & weights sorted(ascending) by name. : ";
        for(Node *temp = nameFront; temp != 0; temp = temp->next)
            cout << temp->name << " - " << temp->wgt << " ";
        cout << endl;
    }
    void printbyWeight()
    {
        cout << "Names & weights sorted(ascending) by weight. : ";
        for (Node *temp = weightFront; temp != 0; temp = temp->next)
            cout << temp->name << " - " << temp->wgt << " ";
        cout << endl;
    }
    
};
int main(int argc, const char * argv[])
{
    List dll;
    int weights;
    string names;
    int count = 0;
    cout << "Program 2" << endl;
    cout << "Enter 3 sets of names and weights: " << endl;
    while (count < 3)
    {
        getline(cin, names);
        cin >> weights;
        dll.push(names, weights);
        cin.ignore();
        count++;
    }
    dll.printbyName();
    dll.printbyWeight();
    system("pause");
    return 0;
}
