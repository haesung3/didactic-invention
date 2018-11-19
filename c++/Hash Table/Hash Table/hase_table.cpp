//
//  hash_table.cpp
//  Hash Table
//
//  Created by HAE SUNG JEONG on 4/15/18.
//  Copyright © 2018 HAE SUNG JEONG. All rights reserved.
//

#include <iostream>
using namespace std;
const int SIZE = 27;
class HashTable{
private:
    int items[SIZE];
public:
    HashTable()
    {
        for(int i = 0; i < SIZE; i++)
            items[i] = -1;
    }
    int Hash(int n)
    {
        return n % SIZE;
    }
    
    void add(int n)
    {
        int count = 0;
        int hashNum = Hash(n);
        while (count < SIZE)
        {
            if (items[hashNum] == -1)
            {
                items[hashNum] = n;
                break;
            }
            else
            {
                hashNum = (hashNum + 1) % SIZE;
                count++;
            }
        }
    }
    
    int lookup(int n)
    {
        int index = -1;
        int count = 0;
        while (count < SIZE)
        {
            if(items[count] == n)
            {
                index = count;
                break;
            }
            else
                count++;
        }
        
        return index;
    }

};
int main(int argc, const char * argv[]) {
    cout << "HASH TABLE" << endl;
    cout << "Please add 27 integers: ";
    HashTable ht;
    int c = 0;
    int in;
    while (c < SIZE)
    {
        cin >> in;
        ht.add(in);
        c++;
    }
    int look;
    cout << "Please enter an integer you want to look up: ";
    cin >> look;
    if(ht.lookup(look) == -1)
        cout << "The integer is not in the table!" << endl;
    else
        cout << "The integer " << look << " is at the index " << ht.lookup(look) << endl;
    system("pause");
    return 0;
}
