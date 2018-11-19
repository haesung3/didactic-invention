//
//  dynamic_search.cpp
//  dynamic_search
//
//  Created by HAE SUNG JEONG on 1/21/18.
//  Copyright © 2018 HAE SUNG JEONG. All rights reserved.
//

#include <iostream>
using namespace std;

int main(int argc, const char * argv[]) {
    int size;
    cout << "Enter the size of the array ";
    cin >> size;
    int nums[size];
    int index = 0;
    cout << "Enter numbers into the array " << endl;
    int temp;
    cin >> temp;
    while (temp != -1 && index < size)
    {
        nums[index] = temp;
        index++;
        if (index == size)
            break;
        cin >> temp;
    }
    cout << "The numbers are ";
    for (int j = 0; j < size; j++)
        cout << nums[j] << " ";
    cout << endl;
    return 0;
}
