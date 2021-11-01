using System;
using System.IO;
using System.Text;
class Program
{
    static void Main(string[] args)
    {
        // File name  
        string strWorkPath = System.IO.Path.GetDirectoryName(System.Reflection.Assembly.GetExecutingAssembly().Location);

        string fileName = AddQuotesIfRequired(strWorkPath) + @"AppData.yaml";
        try
        {
            // Create a StreamReader  
            using (StreamReader reader = new StreamReader(fileName))
            {
                string line;
                // Read line by line  
                while ((line = reader.ReadLine()) != null)
                {
                    Console.WriteLine(line);
                }
            }
        }
        catch (Exception exp)
        {
            Console.WriteLine(exp.Message);
        }
        Console.ReadKey();
    }
}