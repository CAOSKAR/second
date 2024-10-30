import os
import datetime,time
from datetime import timedelta
from pathlib import Path
#path = r"C:\Users\oezka\AppData\Local\Programs\Python\programdir"

def compfile(path):
  for file in os.listdir(path):
    
    print('####################ANFANG#######################################')
    #file_name = os.path.join(path, file)
    file_name = Path(os.path.join(path, file))
    if file_name.is_file():
        # aktuelle Zeit unformatiert
      dt_c = datetime.datetime.now()#.strftime("%d.%m.%Y %H:%M:%S")

      # Zeit der Dateierstellung unformatiert
      dt_b = os.path.getctime(file_name)
      dt_bdt = datetime.datetime.fromtimestamp(dt_b)
   

      # aktuelles Datum + Zeit um 90 Tage zurückdatieren 
      dt_end = dt_c + timedelta(days=-90) 
      dt_endf = dt_end.strftime("%d.%m.%Y %H:%M:%S")
      dt_bdtf = dt_bdt.strftime("%d.%m.%Y %H:%M:%S")
      print('Der Tag der Dateierstellung formatiert:', dt_bdtf)
      print('Der Tag -90:', dt_endf)
   

      # Vergleich ob Datei aelter oder juenger ist
      if dt_bdt <  dt_end :
       print('Datei ist aelter als 90 Tage:', file)
      else: 
       print('Datei ist juenger als 90 Tage:', file)
    else:
      print('Objekt ist keine Datei',file)   
    print('##########################ENDE####################################')