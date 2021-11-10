using System;
using System.Collections.Generic;
using System.Timers;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Threading;
using System.Diagnostics;
using System.IO;
namespace TestApp
{
    class Program
    {
        static void Main(string[] args)
        {
            FileStream f = new FileStream("AppData.txt", FileMode.OpenOrCreate);
            StreamReader s = new StreamReader(f);
            string updateText = s.ReadToEnd();
            s.Close();
            f.Close();

            Console.WriteLine(updateText);
            Console.WriteLine("Hello");
        }
    }
}
