import java.io.*;

public class task2{
    public static void main(String[] args) throws IOException 
    {
        File f1=new File("file.txt");
        String[] words=null; 
        FileReader fr = new FileReader(f1); 
        BufferedReader br = new BufferedReader(fr);
        String s;   
        String in="MACRO";  
        while((s=br.readLine())!=null){
            words=s.split(" ");
            if(words[0].equals(in))
                continue;
            System.out.println(s);
        }
        fr.close();
    }
}