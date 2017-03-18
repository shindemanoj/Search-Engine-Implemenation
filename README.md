# Search-Engine-Implemenation

**************************************************************************************************
How to setup and run Project:

**************************************************************************************************
How to setup and run Java code:

1. Download Eclipse
2. Create new project and Java file named Lucen_Results.java in Eclipse and copy code to this file.
3. Add Following three jars
	* lucene-core-4.7.2.jar
	* lucene-queryparser-4.7.2.jar
	* lucene-analyzers-common-4.7.2.jar
4. Run it and follow the instructions to get output

******************************************************************************************************
How to setup and run Python code:

Libraries required - 
re
os
math
numpy
ast

Language used - 
Python 2.7

Installation guide - 
Install python 2.7
import all the libraries required
1. Download Python 2.7 from https://www.python.org/downloads/
2. Download Pycharm Community edition from https://www.jetbrains.com/pycharm/download/#section=windows
3. Create new project and file and copy code to this file.
4. Extract CleanData zip data and copy to python project
5. Run Python Code to create file of Inverted Index for Unigram
6. Run RetrievalModel code which will give Cosine Similarity results for input query

********************************************************************************************************
How to run (Task 1) Four Baseline Runs (IRProjectTask1.py):

Run IRProjectTask1.py to get top 100 retrieved ranked list for four different retrieval models.
No command line arguments needed.
All result files will get added to 'Task1Results' folder

***********************************************************************************************************
How to run Task 2 (Task-2.py):

Install all dependencies. 
Run the source code using a terminal with the command - python "Task-2.py"
Alternatively, you can also use IDLE to open the python file and run the module.
No command line arguments needed.
Results will get added to file named "BM25_PseudoRelevance_Result.txt" in same directory.

******************************************************************************************************
How to run Task 3 (Task-3_stopping.py, Stem_Retrieval.py and Non_Stemmed_Run.py):

Part A -->
Run "Task-3_stopping.py" which is in Task 3 folder to get BM25 Stopping results.
Results will get stored in file named "BM25_Stopped_Result.txt" in same directory.

Part B -->
Run "Stem_Retrieval.py" which is in IR folder to get results of stemmed queries through stemmed corpus
Results will get stored in Task3Results named BM25_Stem.txt file
To get results of non-stemmed run, run "Non_Stemmed_Run.py". Results will get stored in Task3Results folder as file named "BM25_Non_Stemmed_Run"
 

**********************************************************************************************************
How to run Phase-2 Evaluation (Task-4_BM25.py and Evaluator.py):

Seventh run (Task-4_BM25.py):
To get results for seventh run that is Query Expansion technique using BM25 with stopping run "Task-4_BM25.py".
Results will get added to file named "BM25_PseudoRelevance_Stopped_Result.txt" in same directory.

Evaluation of Search Engines (Evaluator.py):
Run "Evaluator.py" which is in Evaluation folder to get evaluation of all distinct seven runs
Results will get added to respective folders in same directory

************************************************************************************************************
Snippet Generation (Snippet_Generation.py):

Run "Snippet_Generation.py" file which is in Snippet Generation folder to get result of snippet generation.
Result will get stored as "google.html" file in same directory

************************************************************************************************************



