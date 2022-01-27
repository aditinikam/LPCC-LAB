import java.io.*;  
public class task1   
{  
    public static void main(String[] args)   
    {  
        try  
        {  
            File file = new File("file.txt");   
            FileInputStream fis=new FileInputStream(file); 
            System.out.println("file content: ");  
            int r=0;  
            while((r=fis.read())!=-1) {
                System.out.print((char)r); 
            } 
            fis.close();   
        }  
        catch(Exception e)  
        {  
            e.printStackTrace();  
        }  
    }  
}  