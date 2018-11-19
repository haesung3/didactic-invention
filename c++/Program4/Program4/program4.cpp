//
//  program4.cpp
//  Program4
//
//  Created by HAE SUNG JEONG on 5/1/18.
//  Copyright © 2018 HAE SUNG JEONG. All rights reserved.
//

#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <math.h>
using namespace std;

static const int TABLESIZE = 10;

class Hash{
private:
    string names;
    int numbers;
    int scope;
public:
    Hash()
    {
        names = "";
        numbers = 0;
        scope = 0;
    }
    string getName()
    {
        return names;
    }
    int getScope()
    {
        return scope;
    }
    int getNumber()
    {
        return numbers;
    }
    void setName(string n)
    {
        names = n;
    }
    void setNumber(int n)
    {
        numbers = n;
    }
    void setScope(int s)
    {
        scope = s;
    }
};

int hashing(string n)
{
    int val = 0;
    int size = (int)n.length();
    for (int i = 0; i < size + 1; i++)
    {
        val += (int) n[i] * i;
    }
    return val % TABLESIZE;
}

bool checkOp(string oper)
{
    if (oper == "+")
        return true;
    else if (oper == "-")
        return true;
    else if (oper == "*")
        return true;
    else if (oper == "/")
        return true;
    else if (oper == "%")
       return true;
    else if (oper == "^")
        return true;
    else
        return false;
}

bool checkUni(string oper)
{
    if (oper == "++")
        return true;
    if (oper == "--")
        return true;
    else
        return false;
}

int math(string oper, int op1, int op2)
{
    if (oper == "+")
        return op1 + op2;
    else if (oper == "-")
        return op1 - op2;
    else if (oper == "*")
        return op1 * op2;
    else if (oper == "/")
        return op1 / op2;
    else if (oper == "%")
        return op1 % op2;
    else if (oper == "^")
        return pow(op1, op2);
    else
        return op1;
}

int uniMath(string oper, int op)
{
    if (oper == "++")
        return op + 1;
    else if (oper == "--")
        return op - 1;
    else
        return op;
}


int main(int argc, const char * argv[]) {
	int cScope = 0;
    Hash *table[TABLESIZE];
    
	for (int i = 0; i < TABLESIZE; i++)
        table[i] = new Hash();

	ifstream file("input.txt");
	string s;
	if (file.is_open())
	{
		while (getline(file, s))
		{
			stringstream line(s);
			line >> s;
			if (s == "START")
			{
				cScope++;
				while (line >> s);
			}
			else if (s == "FINISH")
			{
				cScope--;
				while (line >> s);
			}
			else if (s == "COM")
				while (line >> s);
			else if (s == "VAR")
			{
				Hash *temp = new Hash();
				line >> s;
				temp->setName(s);
				line >> s;
				if (s == "=")
				{
					line >> s;
					temp->setNumber(stoi(s));
					temp->setScope(cScope);
                    int index = hashing(temp->getName());
                    if (table[index]->getName() == "")
					{
                        table[index] = temp;
						while (line >> s);
					}
                    else if (table[index]->getName() != "")
					{
                        int newindex = index;
                        while (table[newindex]->getName() != "")
                        {
                            newindex++;
                        }
                        table[newindex] = temp;
                        while(line >> s);
					}
					else
					{
						cout << "FAILED TO ADD!";
						while (line >> s);
					}
				}
			}
			else if (s == "PRINT")
			{
				line >> s;
                int index = hashing(s);
                Hash *temp = table[index];
                
                if (temp == nullptr)
                {
                    cout << s << " IS UNDEFINED" << endl;
                    while(line >> s);
                }
                else if (s != temp->getName())
                {
                    index = 0;
                    while (s != table[index]->getName())
                    {
                        index++;
                        if (index == TABLESIZE)
                            break;
                    }
                    temp = table[index];
                    if (s != table[index]->getName())
                    {
                        cout << s << " IS UNDEFINED!" << endl;
                        while (line >> s);
                    }
                }
                if (temp == table[index] && temp->getName() != "")
				{
                    if (temp->getScope() <= cScope)
                    {
					line >> s;
					string oper = s;
					if (checkOp(oper))
					{
						line >> s;
						int op = stoi(s);
                        int res = math(oper, temp->getNumber(), op);
                        cout << temp->getName() << " " << oper << " " << op << " IS " << res << endl;
					}
					else if (checkUni(oper))
					{
                        int res = uniMath(oper, temp->getNumber());
                        temp->setNumber(res);
                        *table[hashing(s)] = *temp;
                        cout << temp->getName() << " " << oper << " " << " IS" << temp->getNumber() << endl;
					}
					else
					{
						cout << temp->getName() << " IS " << temp->getNumber() << endl;
						while (line >> s);
					}
				}
                    else
                    {
                        cout << temp->getName() << " IS UNDEFINED!" << endl;
                        while(line >> s);
                    }
                }
            }
			else
			{
                int index = hashing(s);
                Hash *temp = table[index];
				line >> s;
                if (temp->getScope() <= cScope)
				{
					string oper = s;
                    if (oper == "=")
                    {
                        line >> s;
                        temp->setNumber(stoi(s));
                    }
					else if (checkOp(oper))
					{
						line >> s;
						int op2 = stoi(s);
                        int res = math(oper, temp->getNumber(), op2);
                        temp->setNumber(res);
					}
					else if (checkUni(oper))
					{
                        int res = uniMath(oper, temp->getNumber());
                        temp->setNumber(res);
					}
				}
			}
		}
	}
	file.close();
	system("pause");
	return 0;
}

