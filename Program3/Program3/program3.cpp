//
//  program3.cpp
//  Program3
//
//  Created by HAE SUNG JEONG on 3/26/18.
//  Copyright © 2018 HAE SUNG JEONG. All rights reserved.
//

#include <iostream>
#include <string>
using namespace std;

// creating a node of the tree
class Node
{
public:
    string name;
    int weight;
    Node *left, *right;
    Node(string n, int w)
    {
        name = n;
        weight = w;
        left = nullptr;
        right = nullptr;
    }
};

class Bst
{
private:
    Node *root;
public:
    // make the root as a null at first
    Bst()
    {
        root = nullptr;
    }
    // add the node to the tree at an appropriate position
	void add(string n, int w)
	{
		Node *temp = new Node(n, w);
		Node *cur = root;
        // if there is no node in the tree, then that node becomes root
		if (root == nullptr)
			root = temp;
        // find the right position for the node
		else
		{
			while (n < cur->name && cur->left != nullptr)
			{
				cur = cur->left;
				if (n > cur->name && cur->right != nullptr)
					cur = cur->right;
			}
			while (n > cur->name && cur->right != nullptr)
			{
				cur = cur->right;
				if (n < cur->name && cur->left != nullptr)
					cur = cur->left;
			}
			if (n < cur->name)
				cur->left = temp;
			else
				cur->right = temp;
		}
	}
    // preorder traverse
    void preorder(Node *ptr)
    {
        if (ptr != nullptr)
        {
            cout << ptr->name << " ";
            preorder(ptr->left);
            preorder(ptr->right);
        }
    }
    // inorder traverse
    void inorder(Node *ptr)
    {
        if (ptr != nullptr)
        {
            inorder(ptr->left);
            cout << ptr->name << " ";
            inorder(ptr->right);
        }
    }
    // postorder traverse
    void postorder(Node *ptr)
    {
        if (ptr != nullptr)
        {
            postorder(ptr->left);
            postorder(ptr->right);
            cout << ptr->name << " ";
        }
    }
    // search the node by looking at the weights
    int search(string n)
    {
        int w = -1;
        Node *ptr = root;
        while (ptr != nullptr && ptr->name != n)
        {
            if (n < ptr->name)
                ptr = ptr->left;
            else
                ptr = ptr->right;
        }
        w = ptr->weight;
        return w;
    }
    // find the first name in alphabetical order from the tree
    string first(Node *ptr)
    {
        while(ptr->left != nullptr)
            ptr = ptr->left;
        return ptr->name;
    }
    int leaves(Node *ptr)
    {
        if (ptr == nullptr)
            return 0;
        if (ptr->left == nullptr && ptr->right == nullptr)
            return 1;
        else
            return leaves(ptr->left) + leaves(ptr->right);
    }
    // find the height of the tree
    int height(Node *ptr)
    {
        int left, right;
        if (ptr == nullptr)
            return -1;
        left = height(ptr->left);
        right = height(ptr->right);
        if (left > right)
            return left + 1;
        else
            return right + 1;
    }
    // find the lowest weight from the tree
	int findlowest(Node *ptr)
	{
		if (ptr != nullptr)
		{
			int low = ptr->weight;
			int comp1 = findlowest(ptr->left);
			int comp2 = findlowest(ptr->right);
			if (low > comp1 && comp2 > comp1)
				return comp1;
			else if (low > comp2 && comp1 > comp2)
				return comp2;
			else
				return low;
		}
		return 98798;
	}
    // return the root
    Node* getRoot()
    {
        return root;
    }
};

int main(int argc, const char * argv[]) {
    Bst tree;
    int weights;
    string names;
    int count = 0;
    cout << "Program 3" << endl;
    cout << "Enter names and weights: " << endl;
    string searching;
    while (count < 6)
    {
        getline(cin, names);
        cin >> weights;
        tree.add(names, weights);
        cin.ignore();
        count++;
    }
    cout << endl << endl << "Preorder: ";
    tree.preorder(tree.getRoot());
    cout << endl << "Inorder: ";
    tree.inorder(tree.getRoot());
    cout << endl << "Postorder: ";
    tree.postorder(tree.getRoot());
    cout << endl << "Height: " << tree.height(tree.getRoot()) << endl;
	cout << "Number of leaves: " << tree.leaves(tree.getRoot()) << endl;
	cout << "Minimum weight: " << tree.findlowest(tree.getRoot()) << endl;
    cout << "First name in alphabetical order: " << tree.first(tree.getRoot()) << endl;
    cout << "Please enter the name of the person you are looking for: " << endl;
    getline(cin, searching);
    if (tree.search(searching) != -1)
        cout << "The weight of the person is " << tree.search(searching) << endl;
    else
        cout << "No match exists!" << endl;
    system("pause");
    return 0;
}

/*
 OUTPUT
 Program 3
 Enter names and weights:
 mike
 100
 tom
 75
 steve
 99
 carry
 58
 stephanie
 82
 george
 42
 
 
 Preorder: mike carry george tom steve stephanie
 Inorder: carry george mike stephanie steve tom
 Postorder: george carry stephanie steve tom mike
 Height: 3
 Number of leaves: 2
 Minimum weight: 42
 First name in alphabetical order: carry
 Please enter the name of the person you are looking for:
 carry
 The weight of the person is 58
 sh: pause: command not found
 Program ended with exit code: 0
 */
 
