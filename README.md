# RaceRender-GoPro-GPS-Data-Sanitizer

This might help to clean-up your GoPro GPS data for using with RaceRencer.

One frustration though comes from importing GoPro Hero 7 GPS data, because in each and every case there are errors in the GX******-RR_Data_Merged.csv file.
I use the GoPro Hero Black 7 with h.264 file format. I use the one button record mechanism that turns on the gopro and starts the video right away.

Two issues:

GoPro QuickCapture (turn-on and record with single button click): Video recording starts about 3 seconds after turning on GoPro. However as GPS reception takes 10-30 seconds, the resulting GPS data extract of RaceRender does not align the GPS data with the video properly. My workaround is to always need to use the side-by-side-sync and align the ends of the merged video and merged CSV. please fix this issue, you have the data to align GPS data automatically to each end of the video.

GPS data has errors. Either due to wrong import or due to wrong reception/writing by GoPro. However, such drastically false data can be easily detected and remediated. Simply replace by previous valid data or delete this data granted RaceRender users the timestamps properly to deal with gaps in GPS data.

Here is an example of bogus GPS data in the CSV:
1591962262.929570,47.943287,13.580780,513.803000,6 .928000
1591962262.985126,47.943290,13.580779,513.873000,6 .769000
1591962263.040681,47.943294,13.580778,513.891000,6 .749000
1591962263.096237,47.943297,13.580777,513.869000,6 .859000
1591962263.151792,47.943300,13.580776,513.891000,6 .837000
1591962263.207348,47.943304,13.580775,513.888000,6 .849000
1591962263.262903,47.943307,13.580774,513.875000,6 .639000
1591962263.318459,47.943309,13.580774,513.887000,6 .286000
1591962263.419570,47.943312,13.580773,513.922000,6 .158000
1591962263.475126,47.943315,13.580773,513.930000,6 .317000
1591962263.530681,0.000002,3.520828,141.736000,6.435000
1591962263.586237,47.943322,13.580771,513.895000,6 .594000
1591962263.641792,47.943325,13.580770,513.905000,6 .641000
1591962263.697348,47.943328,13.580769,513.949000,6 .565000
1591962263.752903,47.943331,13.580768,513.871000,6 .311000
1591962263.808459,47.943334,13.580768,513.879000,6 .149000
1591962263.864014,47.943337,13.580767,513.847000,6 .248000
1591962263.919570,47.943340,13.580766,513.794000,6 .418000
1591962263.975126,47.943344,13.580765,513.734000,6 .644000
1591962264.030681,47.943347,13.580763,513.782000,6 .609000
1591962264.086237,47.943350,13.580763,513.848000,6 .442000
1591962264.141792,47.943353,13.580762,513.874000,6 .292000

# How to use:

* load in RaceRender your gopro videos and let RaceRender extract the GPS data. click on edit the GPS data and export the file. This looks like e.g. GX010151-RR_Data.dat.
* rename this GX*.dat file to source.csv. 
* modify constants in the Python script to your needs. restrict max speed, geo-fence, and max distance between two datapoints
MAX_SPEED = 10.0 ## 15.433 m/s = 30kts
MAX_DISTANCE = 0.000010
SKIP_SECONDS = 60 ## skip seconds at the beginning with bogus coordinates when satellites are still searched
MIN_LATITUDE = 47.82
MAX_LATITUDE = 47.96 
MIN_LONGITUDE = 13.5 
MAX_LONGITUDE = 13.6 
* run the python script (i tested with Python 3.8)
* review the corrections and modify the input constants till you have the right level of fixups
* in the RaceRender GPS data edit mode, reload the GPS data and specify target.csv as the new GPS data input

