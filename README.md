<h2>Installation:</h2>
	<h3>1.) Install the following dependencies:</h3>
		- Python 3.6+
			- Download from https://www.python.org/

		- pyWin32
			- Download from https://github.com/mhammond/pywin32
			- Follow its install instructions for your verison of Python
			
		Optional Dependencies
		- foobar COM Automation Server (https://hydrogenaud.io/index.php/topic,39946.0.html)
			- enables the script communicating with foobar2000

	<h3>2.) Install Script</h3>
		- In OBS go to Tools -> Scripts

		- Under the "Python Settings" tab, make sure that your Python Install Path is pointing to your Python install directory (Note: Versions of Python later than 3.6 are currently not supported by OBS.)
		
		- Under the "Scripts" tab, hit the "+" button to add a new script and point OBS to "corvinus-now-playing.py" To update/upgrade, simply replace the script and hit the third "refresh" button to load the, fresh, non-cached script.
		
	<h3>3.) Configure Script</h3>
		Enabled: Turns the script on and off.
		
		Debug Mode: Shows debug messages in the Script Log.
		
		Check Frequency (ms): Sets the loop timer for querying titles in milliseconds.
		
		Display Text: How you would prefer non-YouTube sources to display their data.
		
		Target Text (GDI+) Name: The name of the Text (GDI+) source in your scene the script should replace with its text.
