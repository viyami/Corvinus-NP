Installation:
	1.) Install the following dependencies:
		- Python 3.6+
			- Download from https://www.python.org/

		- pyWin32
			- Download from https://github.com/mhammond/pywin32
			- Follow its install instructions for your verison of Python

	2.) Install Script
		- In OBS go to Tools -> Scripts

		- Under the "Python Settings" tab, make sure that your Python Install Path is pointing to your Python 3.6+ install directory
		
		- Under the "Scripts" tab, hit the "+" button to add a new script and point OBS to "corvinus-now-playing.py"
		
	3.) Configure Script
		Enabled: Turns the script on and off.
		
		YouTube as a source: Will query browser titles for those with YouTube in them and trim away irrelevant information to the best of its ability.
		
		foobar2000 as a source: Gets info from foobar2000 about the current song, if it's playing one.
		
		Debug Mode: Shows debug messages in the Script Log.
		
		Check Frequency (ms): Sets the loop timer for querying titles in milliseconds.
		
		Display Text: How you would prefer non-YouTube sources to display their data.
		
		Target Text (GDI+) Name: The name of the Text (GDI+) source in your scene the script should replace with its text.