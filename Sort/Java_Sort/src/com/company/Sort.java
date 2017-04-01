package com.company;

/**
 * Created by zhou on 2017/3/17.
 */
public class Sort {

    //比较元素间的大小关系
    public static boolean less(Comparable data1,Comparable data2)
    {
        return data1.compareTo(data2) < 0;
    }

    public static boolean more(Comparable data1,Comparable data2)
    {
        return data1.compareTo(data2) > 0;
    }

    public static boolean equals(Comparable data1,Comparable data2)
    {
        return data1.compareTo(data2) == 0;
    }

    //exchange the two elems 交换元素
    public static void exch(Comparable[] data,int i,int j)
    {
        Comparable t = data[i];
        data[i] = data[j];
        data[j] = t;
    }

    //validate if the array is arranged from smallest to largest 验证数组是否从小到大有序
    public static boolean isSorted(Comparable datas[])
    {
        for(int i = 0 ; i < datas.length - 1; i++)
        {
            if(!less(datas[i],datas[i+1]))
                return false;
        }
        return true;
    }

    public static void show(Comparable datas[])
    {
        System.out.println("The result after sorting : ");
        for(int i = 0 ; i < datas.length; i++)
        {
            System.out.print(datas[i]);
            System.out.print(" ");
        }
        System.out.println();
    }

    public static void Bubble_Sort(Comparable datas[])
    {
        for(int i = 0;i < datas.length - 1;i++)
            for(int j = 0;j < datas.length - i - 1;j++)
            {
                if(more(datas[j],datas[j+1]))
                    exch(datas,j,j+1);
            }
    }

    public static void Insertion_Sort(Comparable datas[])
    {
        for(int i = 1;i < datas.length;i++)
            for(int j = i; j > 0 && less(datas[j],datas[j - 1])  ;j--)
                exch(datas,j,j-1);
    }

    public static void Shell_Sort(Comparable datas[])
    {
        int h = datas.length / 3;
        while(h >= 1)
        {
            for(int i = h;i < datas.length;i++)
                for(int j = i;j >= h && less(datas[j],datas[j - h]);j -= h)
                    exch(datas, j,j-h);
            h --;
        }
    }

    public static void Selection_Sort(Comparable datas[])
    {
        for(int i = 0;i < datas.length;i++)
        {
            int min = i;
            for(int j = i + 1;j < datas.length;j++)
            {
                if(more(datas[min],datas[j]))
                    min = j;
            }
            //找到第i个到最后一个区间内的最小元素
            //并交换
            //这里到最后一个元素时也自己和自己交换了，所以交换了datas.length次
            exch(datas,min,i);
        }
    }

    public static void Quick_Sort(Comparable datas[])
    {

    }

    public static void Merge_Sort(Comparable datas[])
    {

    }

    public static void Heap_Sort(Comparable datas[])
    {

    }
}
