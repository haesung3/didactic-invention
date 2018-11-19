//
//  chapter10.cpp
//  chapter10
//
//  Created by HAE SUNG JEONG on 4/17/18.
//  Copyright © 2018 HAE SUNG JEONG. All rights reserved.
//

#include <iostream>
using namespace std;

int main(int argc, const char * argv[]) {
    int n10 = 2987;
    int k = 1;
    int nb = 0;
    int a;
    int b = 6;
    cout << "Convert 2987 to N6" << endl;
    while (n10 > 0)
    {
        a = n10 % b;
        nb = nb + a*k;
        n10 = n10/b;
        k=10*k;
    }
    cout << nb << endl;
    return 0;
}
