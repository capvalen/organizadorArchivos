import os
import pathlib
import shutil
os.system('cls')

#obtenemos la ruta actual
ruta = "D:\Archivos\Programado\organizadorArchivos/archivos";
#str(pathlib.Path(__file__).parent.absolute()) + '/archivos/'

def crearSubCarpeta(tipo, archivo):
	moverDe = ruta+"/"
	moverA = ruta+"/"+tipo+"/"
	#print('mover de ',moverDe+archivo )
	#print('mover A ', moverA+archivo)
	match tipo:
		case 'documento':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'excel':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'powerpoint':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'pdf':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'Imágenes o fotos':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'photoshop':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'vector':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'icono':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'shockwave':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'audio':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'video':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'ejecutable':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'iso':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'comprimido':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'texto':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'basededatos':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'web':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'fuente':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'autocad':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case '3d':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
		case 'otros':
			if not os.path.exists(moverA):
				os.mkdir(moverA)
	shutil.move(moverDe+archivo, moverA+archivo)

def recorrerArchivo(formateado, archivo): 
	match formateado[1].lower():
		case '.doc' | '.docx':
			tipo= 'documento'
			pass
		case '.xlsx' | '.xls' | '.csv':
			tipo= 'excel'
			pass
		case '.ppt' | '.pptx':
			tipo= 'powerpoint'
			pass
		case '.pdf':
			tipo= 'pdf'
			pass
		case '.jpg' | '.jpeg' | '.png' | '.gif' | 'xcf' | '.raw' | '.bmp' | '.webp':
			tipo= 'Imágenes o fotos'
			pass
		case '.psd':
			tipo= 'photoshop'
			pass
		case '.svg' | '.cdr' | '.ai':
			tipo= 'vector'
			pass
		case '.ico':
			tipo= 'icono'
			pass
		case '.swf': #shockwave
			tipo= 'shockwave'
			pass
		case '.mp3' | '.wav' | '.aac' | '.ogg' | '.midi':
			tipo= 'audio'
			pass
		case '.mkv' | '.mp4' | '.avi' | '.mov' | '.rm':
			tipo= 'video'
			pass
		case '.exe':
			tipo= 'ejecutable'
			pass
		case '.iso':
			tipo= 'iso'
			pass
		case '.zip' | '.rar' | '.gzip':
			tipo= 'comprimido'
			pass
		case '.txt':
			tipo= 'texto'
			pass
		case '.mdb' | '.accdb' | '.sql':
			tipo= 'basededatos'
			pass
		case '.html' | '.htm' | '.php' | '.css' | '.js' | '.xml':
			tipo= 'web'
			pass
		case '.ttf' | '.opt':
			tipo= 'fuente'
			pass
		case '.dxf' | '.ifc' | '.rvt' | '.pln':
			tipo= 'autocad'
			pass
		case '.dwg' | '.stl': #3d
			tipo= '3d'
		case _: #otros
			tipo= 'otros'
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
	

	