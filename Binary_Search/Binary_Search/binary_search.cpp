//
//  binary_search.cpp
//  Binary_Search
//
//  Created by HAE SUNG JEONG on 2/10/18.
//  Copyright © 2018 HAE SUNG JEONG. All rights reserved.
//

#include <iostream>
using namespace std;

int bsearch(int *ar, int min, int max, int num)
{
    if (min <= max)
    {
        int mid = (min + max) /2;
        if (num == ar[mid])
            return mid;
        else if (num < ar[mid])
            return bsearch(ar, min, mid-1, num);
        else
            return bsearch(ar,mid+1,max,num);
    }
    else
        return -1;
}

int main(int argc, const char * argv[]) {
    
    int num[10] = {2,4,6,8,10,12,14,16,18,20};
    int target;
    int temp;
    cout << "Binary Search" << endl;
    cout << "Enter the target number from 2 to 20 (even only): ";
    cin >> target;
    cout << "your number is ";
    temp = num[bsearch(num,0,9,target)];
    if (temp == target)
        cout << temp << endl;
    else
        cout << "not in the array!" << endl;
    system("pause");
    return 0;
}

/* OUTPUT
 Binary Search
 Enter the target number from 2 to 20 (even only): 8
 your number is 8
 */
