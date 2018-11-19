//
//  linked_based_queue.cpp
//  Linked_Based_Queue
//
//  Created by HAE SUNG JEONG on 2/6/18.
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
        count = data;
        next = ptr;
    }
};

class Queue
{
public:
    Queue();
    void enqueue(int n)
    {
        Node *temp->data = n;
        
    }
    int dequeue()
    {
        
    }
    bool isEmpty()
    {
        return
    }
private:
    
}
int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
