using System;
using System.Collections.Generic;
using System.Timers;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Threading;
using System.Diagnostics;
using System.Windows.Forms;
using System.IO;

namespace LexiRealInterface
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    /// 
    public partial class MainWindow : Window
    {
        System.Timers.Timer t;
        int s = 1;
        string updateText;
        string updatedText;


        public string AddQuotesIfRequired(string path)
        {
            return !string.IsNullOrWhiteSpace(path) ?
                path.Contains(" ") && (!path.StartsWith("\"") && !path.EndsWith("\"")) ?
                    "\"" + path + "\"" : path :
                    string.Empty;
        }

        public MainWindow()
        {
            InitializeComponent();
            this.DataContext = this;

        }

        private void OnTimeEvent(object sender, ElapsedEventArgs e)
        {
            this.Dispatcher.Invoke(() =>
            {
                if (s == 1)
                {

                    Console.WriteLine("okay");
                    FileStream f = new FileStream("AppData.txt", FileMode.OpenOrCreate);
                    StreamReader s = new StreamReader(f);
                    updateText = s.ReadToEnd();
                    updatedText = "";
                    s.Close();
                    f.Close();

                    if (updateText != updatedText)
                    {
                        updatedText = updateText;
                        Console.WriteLine(updateText);
                        timeText.Text = updatedText;
                    }


                }
            });
        }

        public void Start_Click(object sender, RoutedEventArgs e)
        {
            RunCmd(1);
            
            
        }
        

        public void Quit_Click(object sender, RoutedEventArgs e)
        {
            FileStream f = new FileStream("AppData.txt", FileMode.OpenOrCreate);
            StreamWriter s = new StreamWriter(f);
            RunCmd(2);
            s.WriteLine("close = True");
            s.Close();
            f.Close();
            Close();
        }

        

        private void RunCmd(int hello)
        {
            if (hello == 1 || hello == 2)
            {
                t = new System.Timers.Timer();
                t.Interval = 1000;//1s
                t.Elapsed += OnTimeEvent;
                t.Start();

                string strWorkPath = System.IO.Path.GetDirectoryName(System.Reflection.Assembly.GetExecutingAssembly().Location);

                string fileName = AddQuotesIfRequired(strWorkPath) + @"\AudioRecognition.py";

                Process p = new Process();
                p.StartInfo = new ProcessStartInfo(@"C:\WINDOWS\py.exe", fileName)
                {
                    //RedirectStandardOutput = true,
                    UseShellExecute = false,
                    CreateNoWindow = true
                };

                

                if (hello == 1)
                {
                    p.Start();
                    
                }
                
            }
        }

        
    }
}
