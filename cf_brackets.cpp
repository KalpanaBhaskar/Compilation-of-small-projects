#include<bits/stdc++.h>
using namespace std;

int find_pairs(string &s)
{
    int reserve = 0, pairs = 0;

    for(int i = 0; i < s.size(); i++)
    {
        if( s[i]=='*')
        {
            continue;
        }
        

        if(s[i] == '(')
        {
            reserve++;
        }
        else
        {
            if(reserve > 0)
            {
                reserve--;
                pairs++;
            }
        }
    }

    return 2 * pairs;
}

int main()
{
    int nc;
    cin >> nc;

    while(nc--)
    {
        int n, k;
        cin >> n >> k;

        string s;
        cin >> s;

        vector<int> open, close;

        for(int i = 0; i < n; i++)
        {
            if(s[i] == '(')
                open.push_back(i);
        }

        for(int i = n - 1; i >= 0; i--)
        {
            if(s[i] == ')')
                close.push_back(i);
        }

        int mini = INT_MAX;
        string final_ans(n, '0');

        for(int i = 0; i <= k; i++)
        {
            int open_del = i;
            int close_del = k - i;

            if(open_del > open.size() || close_del > close.size())
                continue;

            string form = s;
            string cur(n, '0');

            for(int j = 0; j < open_del; j++)
            {
                form[open[j]] = '*';
                cur[open[j]] = '1';
            }

            for(int j = 0; j < close_del; j++)
            {
                form[close[j]] = '*';
                cur[close[j]] = '1';
            }

            int val = find_pairs(form);

            if(val < mini)
            {
                mini = val;
                final_ans = cur;
            }
        }

        cout << final_ans << endl;
    }

    return 0;
}