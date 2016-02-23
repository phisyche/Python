int sum( int[], int n ){
    if ( n == 0) //base case
        return 0 ;
    else
    {
        itn small = sum( arr, n - 1) ; //solve smaller problem
        // use solution of smaller to solve larger
        return small + arr[ n - 1];
    }
}
