from pathlib import Path
from src.download import Download
from src.dataAugmentation import DataAugmentation
import os
from src.preproceso import Preproceso

# PARAMETERS
DOWNLOAD_DATA = True
DOWNLOAD_PATH = Path("artifacts/sourceData")

AUGMENT_DATA = True
SOURCE_PATH = Path("artifacts\\sourceData")
FINAL_PATH = Path("artifacts\\workData")
ROOT_PATH = Path("C:\\Users\\agarc\\OneDrive\\Documentos\\GitHub\\Plant_Disease_Detection_for_ML")
NEW_PATH = Path("artifacts\\preprocesamiento")
NEDD_PATH=Path("artifacts\\workData\\images")
PREPROCESO = True

# DOWNLOAD DATA
if DOWNLOAD_DATA:
    download = Download(DOWNLOAD_PATH)
    download.main()

os.chdir(ROOT_PATH)  # Cambia el directorio de trabajo al directorio raíz del proyecto

# DATA AUGMENTATION
if AUGMENT_DATA:
    data_augmentation = DataAugmentation(SOURCE_PATH, FINAL_PATH)
    data_augmentation.main()

# PREPROCESO
if PREPROCESO:
    preproceso_n = Preproceso(NEDD_PATH, NEW_PATH, 150)
    preproceso_n.process_images()

print("Proceso completado.")


