#define pb push_back
#define mp make_pair
#define fi first
#define se second 
#define all(...) begin(__VA_ARGS__) , end(__VA_ARGS__)
#define boost {ios_base::sync_with_stdio(false); cin.tie(); cout.tie();}

#include <bits/stdc++.h>
using namespace std;

mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
#define random_shuffle(...) shuffle(__VA_ARGS__, rng)
#define random(...) uniform_int_distribution<int>(__VA_ARGS__)(rng)

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef vector <int> vi;
typedef vector <ll> vll;
typedef pair<int,int> PII;
typedef pair<ll,ll> PLL;
constexpr ll INF = 2e18+6969;



int main()
{
	int n;
	scanf("%d", &n);
	
	vi v(n);
	ll cost = 0;
	for(int i=0;i<n;i++)
	{
		scanf("%d", &v[i]);
		cost += (v[i] - i) * (v[i] - i);
	}
	
	printf("%lld\n", cost);
	
	return 0;
}
