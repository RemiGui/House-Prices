# House-Prices


<h3> To run the script, in terminal : </h3>

<p> python main.py -T train.csv -t test.csv -v sample_submission.csv -a decision tree </p>

<p> It will run the best accuracy </p>


<h3> Algorithms accuracy (average gap divided by average price) : </h3>

<ul>
<li> Decision tree : 0.175 </li>
<li> SVM : 0.279 </li>
<li> Linear regression : 0.309 </li>
</ul>



<h3> You can also do the -h command in terminal : </h3>

<p> python main.py -h </p>

<p> You will have the description of each option </p>

<h3> Used Libraries : </h3>
<ul>
<li> Pandas </li>
<li> Numpy </li>
<li> Argparse </li>
<li> Sklearn </li>
</ul>


<h3> Functions description : </h3>
<ul>
	<li> 
		main.py :
		<ul>
		<li> Used to execute the script </li>
		</ul>
	</li>
	<li> 
		accuracy.py : 
		<ul>
		<li> Gives the accuracy of used algorithm </li>
		<li> Used in main.py </li>
		</ul>
	</li>
	<li> 
		change_NA.py : 
		<ul>
		 <li> Changes non given data into '0' </li>
     <li> Used in main.py </li>
		</ul>
	</li>
	<li> 
		converting_data.py : 
		<ul>
		<li> Converts strings to ints in all train and test data </li> 
        	<li> Used in treating_data.py </li> 
		</ul>
	</li>
	<li> 
		data_preprocessing.py : 
		<ul>
		<li> Preprocess train and test data (without treating non given data) </li> 
        	<li> Used in converting_data.py </li> 
		</ul>
	</li>
	<li> 
		decision_tree.py : 
		<ul>
		<li> Performs decision tree algorithm </li> 
        	<li> Used in performing_algorithm.py </li> 
		</ul>
	</li>
  	<li> 
		index_strings.py :
		<ul>
		<li> Stores in an array all columns index data_preprocessing.py has to manage </li> 
		<li> Used in converting_data.py </li> 
		</ul>
	</li>
	<li> 
		input_data.py : 
		<ul>
		<li> Extracts data from csv files with pandas and converts them to numpy arrays </li> 
		</ul>
	</li>
	<li> 
		linear_regression.py : 
		<ul>
		<li> Performs linear regression algorithm </li> 
        	<li> Used in performing_algorithm.py </li> 
		</ul>
	</li>
	<li> 
		performing_algorithm.py : 
		<ul>
		<li> Performs algorithm chosen by user </li> 
		<li> Used in main.py </li> 
		</ul>
	</li>
	<li> 
		preparing_data.py :
		<ul>
		<li> Prepares the train and test data for algorithms </li> 
		<li> Used in main.py </li> 
		</ul>
	</li>
  <li> 
	  SVM.py : 
	  <ul>
	  <li> Performs SVM algorithm </li> 
    <li> Used in performing_algorithm.py </li> 
		</ul>
	</li>
	<li> 
		treating_data.py : 
		<ul>
		<li> Preprocessing the test and train data </li> 
		<li> Used in main.py </li> 
		</ul>
	</li>
</ul>
