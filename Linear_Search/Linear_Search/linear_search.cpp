//
//  linear_search.cpp
//  Linear_Search
//
//  Created by HAE SUNG JEONG on 1/19/18.
//  Copyright © 2018 HAE SUNG JEONG. All rights reserved.
//

#include <iostream>
using namespace std;

int main(int argc, const char * argv[]) {
    int nums[10] = {13,2,14,22,66,12,10,23,1,3};
    int targetNum;
    int index = -1;
    cout << "Enter the target number ";
    cin >> targetNum;
    for (int i = 0; i < 10; i++)
    {
        if (targetNum == nums[i])
            index = i;
    }
    cout << "The index of the position of the value is " << index+1 << endl;
    system("pause");
    return 0;
}
