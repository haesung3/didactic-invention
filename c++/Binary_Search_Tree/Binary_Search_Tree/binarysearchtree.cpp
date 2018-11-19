//
//  binarysearchtree.cpp
//  Binary_Search_Tree
//
//  Created by HAE SUNG JEONG on 2/16/18.
//  Copyright © 2018 HAE SUNG JEONG. All rights reserved.
//

#include <iostream>
using namespace std;

class Node
{
public:
    int data;
    Node *left;
    Node *right;
    Node(int num)
    {
        data = num;
        left = nullptr;
        right = nullptr;
    }
};

class BtreeSearch
{
private:
    Node *root;
public:
    BtreeSearch()
    {
        root = 0;
    }
    void add(int data)
    {
        Node *temp = new Node(data);
        Node *cur = root;
        if (root == nullptr)
            root = temp;
        else if (root->data >= temp->data)
            temp->left = root;
        else
        {
            while (cur != nullptr)
            {
                if (cur->left == nullptr && cur->left->data < temp->data)
                {
                    cur->left = temp;
                    cur = cur->left;
                }
                else if (cur->right == nullptr && cur->right->data > temp->data)
                {
                    cur->right = temp;
                    cur = cur->right;
                }
            }
        }
    }
    void print()
    {
        Node *cur = root;
        int count = 0;
        if (cur->left == nullptr)
            cout << cur->data;
        else
        {
            while (cur->left != nullptr)
            {
                cur = cur->left;
                count++;
            }
            cout << cur->data;
        }
        
    }
};
int main(int argc, const char * argv[])
{
    BtreeSearch bst;
    int num = 0;
    cout << "Binary Search Tree" << endl;
    cout << "Please enter numbers (exit to -1): ";
    while (num != -1)
    {
        cin >> num;
        bst.add(num);
    }
    bst.print();
    cout << endl;
    system("pause");
    return 0;
}
