//
//  chapter9.cpp
//  chapter9
//
//  Created by HAE SUNG JEONG on 4/17/18.
//  Copyright © 2018 HAE SUNG JEONG. All rights reserved.
//

#include <iostream>
using namespace std;

int main(int argc, const char * argv[]) {
    
    int items[5] = {40, 30, 10, 50, 20};
    cout << "Before: ";
    for (int k = 0; k < 5; k++)
        cout << items[k] << " ";
    int key;
    for (int i = 1; i < 5; i++)
    {
        key = items[i];
        int j = i-1;
        while (j >= 0 && items[j] > key)
        {
            items[j+1] = items[j];
            j = j-1;
        }
        items[j+1] = key;
    }
    cout << endl << "After: ";
    for (int o = 0; o < 5; o++)
        cout << items[o] << " ";
    cout << endl;
    return 0;
}
