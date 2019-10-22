#include<iostream>
#include<chrono>
using namespace std;
using namespace std::chrono;

#define clock_now high_resolution_clock::now

__global__ void minimum(int *a,int *b,int n)
{
	int block=256*blockIdx.x;
	int mini=7888888;

	for(int i=block;i<min(256+block,n);i++)
	{

		if(mini>a[i])
		{
			mini=a[i];
		}

	}
	b[blockIdx.x]=mini;
}

int find_min(int *a, int n){
    int min = INT_MAX;
    for(int i = 0;i<n;i++){
        if(min > a[i]){
            min = a[i];
        }
    }
    return min;
}
int main() {
    cout << "Enter the size of the array" << endl;
    int n;
    cin >> n;
    //int a[n]; //does not work in some cuda versions
    int *a = (int *)malloc(n * sizeof(int));
    for(int i = 0; i < n; i++) {
        //a[i] = i;
        a[i] = rand();
    }

    auto start = clock_now();
    int x = find_min(a, n);
    auto end = clock_now();

    cout<<"\nThe minimum element in CPU is: "<<x<<endl;
    auto time = end-start;
    cout<<"Time taken: "<<time.count()<<" microseconds";

    int *ad,*bd;
	int size=n*sizeof(int);
    int grids=ceil(n*1.0f/256.0f);

    cudaMalloc(&ad,size);
    cudaMalloc(&bd,grids*sizeof(int));

    cudaMemcpy(ad,a,size,cudaMemcpyHostToDevice);
    
    dim3 grid(grids,1);
    dim3 block(1,1);
    
    start = clock_now();

    while(n>1)
	{
		minimum<<<grids,block>>>(ad,bd,n);
		n=ceil(n*1.0f/256.0f);
		cudaMemcpy(ad,bd,n*sizeof(int),cudaMemcpyDeviceToDevice);
	}

    end = clock_now();

    int ans[2];
	cudaMemcpy(ans,ad,4,cudaMemcpyDeviceToHost);
    
    cout<<"\nThe minimum element in GPU is: "<<ans[0]<<endl;
    time = end-start;
    cout<<"Time taken: "<<time.count()<<" microseconds";

    
}