package com.company;

import sun.jvm.hotspot.jdi.IntegerTypeImpl;

public class Main {

    public static void main(String[] args) {
	// write your code here
        /*
            Test
         */
        /*
        Integer[] data = {1,3,45,2,4,-1,343};
        Sort.Bubble_Sort(data);
        Sort.show(data);
        */
        Integer[] data = {5,4,2,21,1,3};
        //Sort.Selection_Sort(data);
        Sort.Shell_Sort(data);
        Sort.show(data);
    }
}
