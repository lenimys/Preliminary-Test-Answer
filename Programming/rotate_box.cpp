#include<bits/stdc++.h>
using namespace std;

#define pb push_back

int main() {
    
    unsigned n, k;
    vector<unsigned> v1, v2, res;

    cin >> n;

    for (unsigned i = 0; i < n; i++){
        unsigned item;
        cin >> item;
        v1.pb(item);
    }

    cin >> k;

    if(k % 2 == 1){
        while(v1.size() != 0){
            v2.push_back(v1.size());
            unsigned a = 0;
            for (auto i = v1.begin(); i != v1.end(); ++i) { 
                v1[a] = v1[a] - 1;
                if (*i == 0) { 
                    v1.erase(i); 
                    i--;
                }else{
                    a++;
                }
            } 
        }
        res = v2;
    }else{
        sort(v1.begin(), v1.end(), greater<int>());
        res = v1;
    }

    for (auto it = res.begin(); it != res.end(); ++it) 
        cout << *it << ' '; 
    
    cout << endl;

    return 0;
}