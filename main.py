#
# dependencies
# win32gui
#

import obspython
import os, time, datetime, requests, codecs

import win32com.client
import win32gui
from pyfoobar import pyfoobar fb2k = foobar()

try:
	from HTMLParser import HTMLParser
except ImportError:
	from html.parser import HTMLParser

working = True
enabled = True
now_playing = ""
latency = 1000
display_text = ""
debug_mode = False

source_name = ""

#----------------------------------------------
# OBS Script Functions
#----------------------------------------------

def script_defaults(settings):
	global debug_mode
	if debug_mode: print("Calling defaults")
	
	global enabled
	global source_name
	global display_text
	global latency
	// potential sources
	global source_chrome
	global source_foobar
	
	obspython.obs_data_set_default_bool(settings, "enabled", enabled)
	obspython.obs_data_set_default_int(settings, "latency", latency)
	obspython.obs_data_set_default_string(settings, "source_name", source_name)
	obspython.obs_data_set_default_string(settings, "display_text", display_text)
	
	obspython.obs_data_set_default_bool(settings, "chrome", source_chrome)
	obspython.obs_data_set_default_bool(settings, "foobar", source_foobar)
	
def script_description():
	return "<b>Corvinus: Now Playing</b>" + \
		"<hr>" + \
		"Check the boxes of audio sources you wish to capture current data from.<br/><br/>" + \
		"Available services:<br/>" + \
		"Google Chrome: Will get current page title and parse out certain data for use with services like YouTube.<br/>" + \
		"Foobar2000: Will automatically obtain track data from Foobar.<br/><br/>" + \
		"Available Placeholder Strings:<br/>" + \
		"<code>%artist</code> to display current artist; <code>%title</code> to display the current track title; <code>%source</code> to display the current source name<br/><br/>" + \
		"<hr>"
		
def script_load(settings):	
	global debug_mode
	if debug_mode: print("Loaded script for Corvinus Now Playing")
	
def script_properties():
	global debug_mode
	if debug_mode: print("Loaded properties for Corvinus Now Playing")
	
	props = obspython.obs_properties_create()
	obspython.obs_properties_add_bool(props, "enabled", "Enabled")
	obspython.obs_properties_add_bool(props, "debug_mode", "Debug Mode")
	obspython.obs_properties_add_int(props, "latency", "Check Frequency (ms)")
	obspython.obs_properties_add_text(props, "display_text", "Display Text", obspython.OBS_TEXT_DEFAULT)
	obspython.obs_properties_add_text(props, "source_name", "Source Name", obspython.OBS_TEXT_DEFAULT)
	return props
	
def script_save(settings):
	global debug_mode
	if debug_mode: print("Saved properties for Corvinus Now Playing")
	script_update(settings)

def script_unload():
	global debug_mode
	if debug_mode: print("Unloaded script for Corvinus Now Playing")
	obspython.timer_remove(get_song_info)
	
def script_update(settings):
	global debug_mode
	if debug_mode: print("Updated properties for Corvinus Now Playing")
	
	global enabled
	global display_text
	global latency
	global source_name
	global source_chrome
	global source_foobar
	
	if obspython.obs_data_get_bool(settings, "enabled") is True:
		if (not enabled):
			if debug_mode: print("Enabled song timer for Corvinus Now Playing")
		enabled = True
		obspython.timer_add(get_song_info, latency)
	else:
		if(enabled):
			if debug_mode: print("Disabled song timer for Corvinus Now Playing")
			enabled = False
			obspython.timer_remove(get_song_info)
			
	debug_mode = obspython.obs_data_get_bool(settings, "debug_mode")
	display_text = obspython.obs_data_get_string(settings, "display_text")
	latency = obspython.obs_data_get_int(settings, "latency")
	source_name = obspython.obs_data_get_string(settings, "source_name")
	source_chrome = obspython.obs_data_get_bool(settings, "source_chrome")
	source_foobar = obspython.obs_data_get_bool(settings, "source_foobar")
	
#----------------------------------------------
# Corvinus Now Playing Functionality
#----------------------------------------------

def get_song_info():
	global debug_mode
	global working
	global now_playing
	global display_text
	global latency
	
	song_artist = ""
	song_title = ""
	song_album = ""
	song_length = ""
	now_playing = ""

# TODO: Actual original scripting crap here

	# populate artist field
	if(source_foobar == True && fb2k.isPlaying() == True):
		song_artist = fb2k.getCurrentArtist()
		song_title = fb2k.getCurrentTrack()
		song_album = fb2k.getCurrentAlbum()
		song_length = fb2k.lengthOfTrack()
	
	if(source_chrome == True):
		now_playing = ""			# TODO: connect with Window Title
	
	#if(source_firefox == True):
	#	now_playing = ""			# TODO: connect with Window Title
		
	#if(source_edge == True):
	#	now_playing = ""			# TODO: connect with Window Title
		