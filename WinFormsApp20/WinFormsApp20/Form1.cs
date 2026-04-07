namespace WinFormsApp20
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Visible = false;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            listBox1.Items.Add(textBox1.Text);
            textBox1.Clear();
            int s = listBox1.Items.Count;
            label1.Text = Convert.ToString(s);
            progressBar1.Visible = true;

            label2.Visible = true;
            progressBar1.Minimum = 0;
            progressBar1.Maximum = 100;
            progressBar1.Step = 1;
            for (int i = 0; i < 100; i++)
            {
                progressBar1.PerformStep();
                label2.Text = "Progres " + progressBar1.Value.ToString();
                this.Update();
                Thread.Sleep(100);

            }
            MessageBox.Show("задача выполнена");
            
        }

        private void button2_Click(object sender, EventArgs e)
        {

           
            
                listBox1.Items.RemoveAt(listBox1.SelectedIndex);
                int s = Convert.ToInt32(label1.Text);
                s = s - 1;

                label1.Text = Convert.ToString(s);
            

        }

        private void button3_Click(object sender, EventArgs e)
        {
           
                Form2 f2 = new Form2();
                string selectedTask = listBox1.SelectedItem.ToString();

                f2.Show(selectedTask);
                f2.ShowDialog();
            
        }
        

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void progressBar1_Click(object sender, EventArgs e)
        {

        }

        private void progressBar1_Click_1(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {
            

        }

        private void button5_Click(object sender, EventArgs e)
        {
            Form3 f3 = new Form3();
            f3.ShowDialog();
                listBox1.Items.Add(f3.TT);

            
        }
    }
}
