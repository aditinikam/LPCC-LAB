import java.io.*;

public class task5{
    public static void main(String[] args) throws IOException 
    {
        File f1=new File("file.txt");
        String[] words=null; 
        FileReader fr = new FileReader(f1); 
        BufferedReader br = new BufferedReader(fr);
        FileWriter fout = new FileWriter("copyfile3.txt", true); 
        String s;   
        String in="MACRO";  
        while((s=br.readLine())!=null){
            words=s.split(" ");
            if(words[0].equals(in)){
                System.out.println(words[1]);
                continue;
            }
            fout.write(s+"\n"); 
        }
        fr.close();
        fout.close();
    }
}