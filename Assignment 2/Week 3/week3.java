import java.io.*;
import java.util.*;

public class week3{
    public static void main(String[] args) throws IOException 
    {
        File file=new File("file.txt");
        FileWriter fout = new FileWriter("ic.txt", true);
        String s;
        Scanner sc = new Scanner(file);
        String[] words=null; 
        ArrayList<String> mnt_name= new ArrayList<String>();
        ArrayList<String> mdt= new ArrayList<String>();
        String[] reg = null;
        ArrayList<Integer> mnt_pointer= new ArrayList<Integer>();
        ArrayList<Integer> mnt_para = new ArrayList<Integer>();
        boolean flag=false;
        while(sc.hasNextLine()){
            s=sc.nextLine();
            words=s.split(" ");
            if(words[0].equals("MACRO")){
                flag=true;
                mnt_name.add(words[1]);
                mnt_pointer.add(mdt.size());
                if(words.length>2){
                    mdt.add(words[1]+" "+words[2]);
                    reg=words[2].split(",");
                    for(int i = 0; i < reg.length; i++){
                        if(reg[i].contains("=")){
                            String[] var = reg[i].split("=");
                            reg[i] = var[0];
                        }
                    }
                    mnt_para.add(reg.length);
                }
                else{
                    mnt_para.add(0);
                }
                continue;
            }
            if(flag){
                while(sc.hasNextLine()){
                    if(words.length > 1){
                        String[] var = words[1].split(",");
                        for(int i = 0; i < var.length; i++){
                            if(var[i].contains("&")){
                                List<String> list = Arrays.asList(reg); 
                                if(list.contains(var[i])){
                                    String replace = "#" + list.indexOf(var[i]);
                                    s = s.replace(var[i], replace);
                                }
                            }
                        }
                    }
                    if(mnt_name.contains(words[0])){
                        int in=mnt_name.indexOf(words[0]);
                        int start_index=mnt_pointer.get(in);
                        int last_index=mnt_pointer.get(in+1);
                        if(words.length>1){
                            String a=null;
                            for(int i=start_index+1;i<last_index-1;i++){
                                String[] act_para=words[1].split(",");
                                if(mdt.get(i).contains("#")){
                                    String[] index=mdt.get(i).split("#");
                                    int x=Integer.valueOf(index[1]);
                                    String replace = "#" + index[1];
                                    a = mdt.get(i);
                                    a = a.replace(replace,act_para[x]);
                                }
                                mdt.add(a);
                            }
                        }
                        else{
                            for(int i=start_index;i<last_index-1;i++){
                                mdt.add(mdt.get(i));
                            }
                        }
                    }
                    if(!mnt_name.contains(words[0]))
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
        System.out.println("Macro Parameter: ");
        for(int listItem : mnt_para){
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
        sc.close();
    }
}