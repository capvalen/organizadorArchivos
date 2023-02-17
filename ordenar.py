#versión 1.0
import sys, os
import pathlib
import shutil
os.system('cls')

#obtenemos la ruta actual
if getattr(sys, 'frozen', False):
	ruta = os.path.dirname(sys.executable)
else:
	ruta = str(pathlib.Path(__file__).parent.absolute())
	#str(pathlib.Path(__file__).parent.absolute()) + '/archivos/'

#print ('nueva ruta ',ruta)
#file = open(ruta+"/logOrdenar.txt", "w")
#file.write(ruta)
#file.close()


def crearSubCarpeta(tipo, archivo):
	moverDe = ruta+"/"
	moverA = ruta+"/"+tipo+"/"
	#print('mover de ',moverDe+archivo )
	#print('mover A ', moverA+archivo)
	match tipo:
		case 'Words':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'Excels':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'Power Points':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'Pdfs':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'Imágenes o fotos':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'Photoshop':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'Vectores':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'Íconos':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'Shockwave':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'Audios':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'Videos':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'Ejecutables':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'Imágenes ISO':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'Comprimidos':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'Textos planos':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'Base de datos':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'Programación Web':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'Fuentes':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'Autocads':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'Modelado 3ds':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'Otros':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
	shutil.move(moverDe+archivo, moverA+archivo)

def recorrerArchivo(formateado, archivo): 
	match formateado[1].lower():
		case '.doc' | '.docx':
			tipo= 'Words'
			pass
		case '.xlsx' | '.xls' | '.csv':
			tipo= 'Excels'
			pass
		case '.ppt' | '.pptx':
			tipo= 'Power Points'
			pass
		case '.pdf':
			tipo= 'Pdfs'
			pass
		case '.jpg' | '.jpeg' | '.png' | '.gif' | 'xcf' | '.raw' | '.bmp' | '.Programación Webp':
			tipo= 'Imágenes o fotos'
			pass
		case '.psd':
			tipo= 'Photoshop'
			pass
		case '.svg' | '.cdr' | '.ai':
			tipo= 'Vectores'
			pass
		case '.ico':
			tipo= 'Íconos'
			pass
		case '.swf': #Shockwave
			tipo= 'Shockwave'
			pass
		case '.mp3' | '.wav' | '.aac' | '.ogg' | '.midi':
			tipo= 'Audios'
			pass
		case '.mkv' | '.mp4' | '.avi' | '.mov' | '.rm':
			tipo= 'Videos'
			pass
		case '.exe':
			tipo= 'Ejecutables'
			pass
		case '.Imágenes ISO':
			tipo= 'Imágenes ISO'
			pass
		case '.zip' | '.rar' | '.gzip' | '.tar' | '.gz' | '.tar.gz':
			tipo= 'Comprimidos'
			pass
		case '.txt':
			tipo= 'Textos planos'
			pass
		case '.mdb' | '.accdb' | '.sql':
			tipo= 'Base de datos'
			pass
		case '.html' | '.htm' | '.php' | '.css' | '.js' | '.xml':
			tipo= 'Programación Web'
			pass
		case '.ttf' | '.opt':
			tipo= 'Fuentes'
			pass
		case '.dxf' | '.ifc' | '.rvt' | '.pln':
			tipo= 'Autocads'
			pass
		case '.dwg' | '.stl': #Modelado 3ds
			tipo= 'Modelado 3ds'
		case _: #Otros
			tipo= 'Otros'
	#print(tipo, archivo)
	crearSubCarpeta(tipo, archivo)
			
	

if os.path.exists( ruta ) :
	#obtener listado de archivos
	archivos = os.listdir(ruta)
	for archivo in archivos:
		if( os.path.isfile(ruta+"/"+archivo) ):
			#print ('soy archivo')
			formateado = os.path.splitext(archivo)
			recorrerArchivo(formateado, archivo)
	#renombrar las carpetas que se movio
	

	