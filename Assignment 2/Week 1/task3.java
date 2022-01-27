import java.io.*;  
import java.util.*;  
public class task3 {  
    public static void main(String arg[]) throws Exception {  
        Scanner sc = new Scanner(System.in);  
        FileReader fin = new FileReader("file.txt");  
        FileWriter fout = new FileWriter("copyfile.txt", true);  
        int c;  
        while ((c = fin.read()) != -1) {  
            fout.write(c);  
        }  
        System.out.println("Copy finish...");  
        fin.close();  
        fout.close();  
        sc.close();;
    }  
} 