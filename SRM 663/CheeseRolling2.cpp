#define bit_cnt(x) __builtin_popcount((unsigned)x)
#include <string>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

class CheeseRolling{
private:
    long long dp[1<<16][16];
    bool ok[1<<17];
    int c[1<<16];
    vector<int> vc[1<<16];
    vector<long long> ans;
public:
    vector<long long> waysToWin(vector<string> wins){
        int n=wins.size();
        for( int i = 0 ;i < (1<<n);i++){
            c[i]=bit_cnt(i);
            vc[i].clear();
            for( int j=0;j<n;j++)
                if((1<<j)&i){
                    vc[i].push_back(j);
                }
        }
        menset(dp,0,sizeof(dp));
        menset(ok,0,sizeof(ok));
        ok[1]=ok[2]=ok[4]=ok[8]=ok[16]=1;
        for( int i = 0 ; i< n ;i++)
            dp[1<<i][i]=1;
        for( int i = 0 ; i < (1<<n);i++){
            int bt=bit_cnt(i);
            if( bt<=1 || !ok[bt])continue;
            int status = i;
            for ( int s= status; s ; s=(s-1)&status) if(c[s]==(c[status]>>1)){
                int s1=s,s2=status-s1;
                for (int i = 0 ; i < vc[s1].size();i++)
                    for( int  j= 0 ; j < vc[s2].size();j++){
                        int p = vc[s1][i],p=vc[s2][j];
                        if(wins[p][q]=='Y'){
                            dp[status][p]+=dp[s1][p]*dp[s2][q];
                        }else{
                            dp[status][q]+=dp[s1][p]*dp[s2][q];
                        }
                    }
            }
        }
        ans.clear()
        for( int i = 0 ;i < n ;i++)
            ans.push_back(dp[(1<<n)-1][i]);
        return ans;
    }
}