# fibonacci-retracement
A simple Python program for calculating and presenting the Fibonacci Retracement of securities using historical market data.  Developed as part of college course research project focused on evaluating modern programming languages.


# More Information about this Project
This program was developed as part of a research project for a college course (CS 431: Principles of Programming Languages).  The project required a research paper to be written providing a comprehensive analysis and evaluation of a modern programming language.  Our team chose Python as the subject language for the project.  In addition to writing the paper, I wrote the code for this sample program as part of the project.  The sample program intends to highlight some of the features and capabilities which were analyzed and evaluated throughout our research.  If you would like to read the final paper, check back here soon for a link.


# Project files
The primary Python script is included in fibRetracement.py.  The fibRetracement_light.py script contains identical Python code, but without the expansive comments included as part of the research project.

All other files, exlcuding the LICENSE and README files, are sample data files (historical trading data) and reference images (from third-party charting source) that were collected and used during the project and presentation to demonstrate the program's performance and to validate its output.  I have included these files so that users have some samples to work with immediately, but be advised that no original project files have been modified since this project was completed, and therefore the data samples are relatively old.  See the Usage section below for information on how to add your own trading data.


# Usage
Simply run the Python script using: python fibRetracement.py

The program will prompt you for two pieces of input (other then awaiting input to proceed):

  (1) A ticker symbol.  The ticker symbol should reflect the name of an associated data file (in the same directory) containing the trading data to analyze.  Input should not include file extension.
  (2) A Fibonacci Sequence limit.  The sequence limit should be an integer, and it specifies the number of values in the Fibonacci Sequence to calculate.  Keep in mind that your system will have its own recursion limits set, and entering a value too high may cause the program to crash or hang.  The program will attempt to notify you of your system's current recursion limit.  Should the program hang up while calulating, you can terminate operation using Ctrl + C.

If the program is able to find and read your data, and can calculate the Fibonacci Sequence within your entered/system parameters, it will output relevant data (inlcuding asset levels of importance), followed by a basic price chart including the levels determined in the Sequence calculation.

To add your own data, you must obtain a file of historical price records substantially similar to those provided as examples.  It should be stored as a CSV file in the same directory as fibRetracement.py, and by convention named with the ticker symbol of the asset whose data it contains.  Once you have your data available to the script, simply run it again and enter the corresponding information to point it to your data file.


# License

Licensed under MIT license.  See accompanying LICENSE file.  Use, modify, or redistribute as you wish.
