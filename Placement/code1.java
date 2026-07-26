import java.util.*;
class code1{
    public ArrayList<Integer> sol(int n,int key){
        int[] arr=new int[n];
        ArrayList<Integer> ans=new ArrayList<>();
        Scanner sc=new Scanner(System.in);
        for(int i=0;i<n;i++){
            System.out.print(i);
            arr[i]=sc.nextInt();
            if(arr[i]==key){
                ans.add(i);
            }
        }
        sc.close();
        return ans;
    }
    public static void main(String[] args) {
        code1 a=new code1();
        Scanner sc = new Scanner(System.in);    
        int n=sc.nextInt();
        int key=sc.nextInt();
        ArrayList<Integer> ans=a.sol(n,key);
        System.out.print(ans);
        sc.close();
    }
}