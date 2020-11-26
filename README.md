<h2>Installation:</h2>

<h3>1.) Install the following dependencies:</h3>
<ul>
	<li><b>Python 3.6</b></li>
	<li><ul><li>Download and follow install instructions from https://www.python.org/ <i>(If you're using 64-bit OBS, you must use 64-bit Python.)</i></li></ul></li>
	<li><b>pyWin32</b></li>
	<li><ul><li>Download and follow install instructions from https://github.com/mhammond/pywin32 for your version of python. <i>(That means both version number and 32/64-bit.)</i></li></ul></li>
	</ul>
	<h4>Optional Dependencies</h4>
	<ul>
	<li><b>foobar COM Automation Server</b> (http://foosion.foobar2000.org/0.9/) - enables the script communicating with foobar2000</li>
	</ul>
<h3>2.) Install Script</h3>
	<ul>
	<li>In OBS go to Tools -> Scripts</li>
	<li>In the "Python Settings" tab, make sure that your Python Install Path is pointing to your Python install directory <i>(Note: Versions of Python later than 3.6 are currently not supported by OBS.)</i></li>
	<li>In the "Scripts" tab, hit the "+" button to add a new script and point OBS to "corvinus-now-playing.py" To update/upgrade, simply replace the script and hit the third "refresh" button to load the, fresh, non-cached script.</li>
<h3>3.) Configuration Options</h3>
	Enabled: Turns the script on and off.
		
	Debug Mode: Shows debug messages in the Script Log.
		
	Check Frequency (ms): Sets the loop timer for querying titles in milliseconds.
		
	Display Text: How you would prefer non-YouTube sources to display their data.
		
	Target Text (GDI+) Name: The name of the Text (GDI+) source in your scene the script should replace with its text.
