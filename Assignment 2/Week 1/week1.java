import java.io.*;
import java.util.*;
public class week1 {
    public static void main(String[] args) throws IOException 
    {
        File file=new File("file.txt");
        FileReader fr = new FileReader(file); 
        FileWriter fout = new FileWriter("ic.txt", true);
        String s;
        Scanner sc = new Scanner(file);
        String[] words=null; 
        ArrayList<String> mnt_name= new ArrayList<String>();
        ArrayList<String> mdt= new ArrayList<String>();
        ArrayList<Integer> mnt_pointer= new ArrayList<Integer>();
        boolean flag=false;
        while(sc.hasNextLine()){
            s=sc.nextLine();
            words=s.split(" ");
            if(words[0].equals("MACRO")){
                flag=true;
                mnt_name.add(words[1]);
                mnt_pointer.add(mdt.size());
                continue;
            }
            if(flag){
                while(sc.hasNextLine()){
                    mdt.add(s);
                    if(words[0].equals("MEND"))
                        break;
                    s=sc.nextLine();
                    words=s.split(" ");
                }
                flag=false;
                continue;
            }
            fout.write(s+"\n"); 
        }
        System.out.println("Macro Name: ");
        for(String listItem : mnt_name){
            System.out.println(listItem);
        }
        System.out.println("Macro Pointer: ");
        for(int listItem : mnt_pointer){
            System.out.println(listItem);
        }
        System.out.println("\n\nMDT: ");
        for(String listItem : mdt){
            System.out.println(listItem);
        }
        fout.close();
        fr.close();
        sc.close();
    }
}
