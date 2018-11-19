//
//  graph_matrix.cpp
//  GraphMatrix
//
//  Created by HAE SUNG JEONG on 4/2/18.
//  Copyright © 2018 HAE SUNG JEONG. All rights reserved.
//

#include <iostream>
#include <string>
#include <sstream>
using namespace std;

class Vertex{
private:
    int num;
    string *label;
    int **matrix;
    string *edge;
public:
    Vertex(int n)
    {
        num = n;
        matrix = new int *[num];
        for (int i = 0; num != i; i++)
            matrix[i] = new int[num];
        for (int j = 0; j < num; j++)
            for (int k = 0; k < num; k++)
                matrix[j][k] = 0;
        edge = new string [num * num];
    }
    void addLabel(int n)
    {
        num = n;
        label = new string[n];
        for (int i = 0; i < n; i++)
        {
            cout << "What is the label for vertex " << (i + 1) << "? ";
            cin >> label[i];
        }
    }
    void addEdge()
    {
        string edges, n1, n2, token;
        int e1 = 0;
        int e2 = 0;
        cout << "From the vertex: ";
        cin >> n1;
        while (n1 != "-1")
        {
            cout << "To the vertex: ";
            cin >> n2;
            
            for(int i = 0; i < num; i++)
            {
                if (n1 == label[i])
                    e1 = i;
                if (n2 == label[i])
                    e2 = i;
            }
            matrix[e1][e2] += 1;
            cout << "Added Edge " << label[e1] << "->" << label[e2] << endl;
            cout << "From the vertex: ";
            cin >> n1;
        }
    }
    void list()
    {
        cout << "Your edges are: ";
        for(int i = 0; i < num; i++)
            for (int j = 0; j < num; j++)
            {
                if (matrix[i][j] != 0)
                    cout << label[i] << label[j] << " ";
            }
    }
};
int main(int argc, const char * argv[]) {
    Vertex *ver;
    int numVer;
    cout << "Graph Matrix" << endl;
    cout << "How many vertices? ";
    cin >> numVer;
    ver = new Vertex(numVer);
    ver->addLabel(numVer);
    cout << endl << "Define an edge by listing a pair of vertices (i.e. \"AB\", or -1 to stop.)" << endl;
    cin.ignore();
    ver->addEdge();
    ver->list();
    return 0;
}
