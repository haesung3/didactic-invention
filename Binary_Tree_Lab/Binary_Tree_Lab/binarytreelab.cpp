//
//  binarytreelab.cpp
//  Binary_Tree_Lab
//
//  Created by HAE SUNG JEONG on 2/14/18.
//  Copyright © 2018 HAE SUNG JEONG. All rights reserved.
//

#include <iostream>
using namespace std;

class Btree
{
private:
    int nums[10];
    int count;
public:
    Btree()
    {
        for (int i = 0; i < 10; i++)
            nums[i] = 0;
        count = 0;
    }
    void add(int data)
    {
        nums[count] = data;
        count++;
    }
    int getCount()
    {
        return count;
    }
    void preorder(int c)
    {
        cout << nums[c] << " ";
        if ((2*c +1) < count)
        {
            preorder(2*c +1);
        }
        if ((2*c + 2) < count)
        {
            preorder(2*c + 2);
        }
    }
};

int main(int argc, const char * argv[])
{
    Btree tree;
    cout << "Binary Tree Lab" << endl;
    int input = 0;
    cout << "Please enter 10 numbers: " << endl;
    while (tree.getCount() != 10)
    {
        cin >> input;
        tree.add(input);
    }
    cout << "Preorder: ";
    tree.preorder(0);
    cout << endl;
    system("pause");
    return 0;
}

/*OUTPUT
 Binary Tree Lab
 Please enter 10 numbers:
 1 2 3 4 5 6 7 8 9 10
 Preorder: 1 2 4 8 9 5 10 3 6 7
 */
