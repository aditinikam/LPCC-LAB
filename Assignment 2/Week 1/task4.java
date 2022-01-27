import java.io.*;

public class task4{
    public static void main(String[] args) throws IOException 
    {
        File f1=new File("file.txt");
        String[] words=null; 
        FileReader fr = new FileReader(f1); 
        BufferedReader br = new BufferedReader(fr);
        FileWriter fout = new FileWriter("copyfile2.txt", true); 
        String s;   
        String in="MACRO";  
        while((s=br.readLine())!=null){
            words=s.split(" ");
            if(words[0].equals(in))
                continue;
            fout.write(s+"\n"); 
        }
        fr.close();
        fout.close();
    }
}