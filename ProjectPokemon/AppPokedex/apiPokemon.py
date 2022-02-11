import requests
class apiPokemon(object):
	"""docstring for apiPokemon"""
	def __init__(self, nombrePokemon, informacion_completa = ''):
		# super(apiPokemon, self).__init__()
		self.nombrePokemon = nombrePokemon
		self.informacion_completa = ''

	def obtenerInformacion(self):
		try:
			respuesta_api = requests.get('https://pokeapi.co/api/v2/pokemon/'+self.nombrePokemon.lower()+'/')
			self.informacion_completa = respuesta_api.json()
			return True
		except Exception as e:
			return False

	""" CARD PRINCIPAL """
	def imagen_principal_pokemon(self):
	    # Imagenes del Pokémon en base a generaciones
	    imagenes = self.informacion_completa['sprites']
	    return imagenes['other']['official-artwork']['front_default']

	def nombre_pokemon(self):
	    # Nombre del Pokémon (Serialize coloca la primera letra en mayúscula)
	    return self.informacion_completa['name'] 

	def identificador_pokemon(self):
	    # Identificador del Pokémon 
	    return self.informacion_completa['id']

	def descripcion_pokemon(self):
	    # Descripcion del pokemon
	    descripcion = ""
	    # Especie a la que pertenece este Pokémon y detalles de la especie.
	    especie = self.informacion_completa['species']
	    # nombre_especie = especie['name']
	    url_especie = especie['url']
	    
	    # Detalle de especie de Pokémon 
	    respuesta_api = requests.get(url_especie)
	    detalles_especie = respuesta_api.json()
	    for i in range(len(detalles_especie)):
	        if detalles_especie['flavor_text_entries'][i]['language']['name'] == 'es':
	            descripcion += detalles_especie['flavor_text_entries'][i]['flavor_text']
	    
	    return descripcion

	""" CARD TIPO """
	def tipo_pokemon(self):
	    # Lista de tipo de Pokémon 
	    lista_tipo = []
	    for i in range(len(self.informacion_completa['types'])):
	        # nombre_tipo = self.informacion_completa['types'][i]['type']['name']
	        url_tipo = self.informacion_completa['types'][i]['type']['url']
	        respuesta_api = requests.get(url_tipo)
	        detalles_tipo = respuesta_api.json()
	        
	        for j in range(len(detalles_tipo['names'])):
	            if detalles_tipo['names'][j]['language']['name'] == 'es':
	                lista_tipo.append(detalles_tipo['names'][j]['name'])
	    return lista_tipo

	""" CARD NIVELES """
	def niveles_base(self):
	    # Lista de niveles 
	    lista_niveles = []
	    # Valores de estadísticas base para este Pokémon.
	    estadisticas = self.informacion_completa['stats']
	    for i in range(len(estadisticas)):
	        base_estadistica = estadisticas[i]['base_stat']
	        # esfuerzo = estadisticas[i]['effort']
	        # nombre_estadistica = estadisticas[i]['stat']['name']
	        url_estadistica = estadisticas[i]['stat']['url']
	        respuesta_api = requests.get(url_estadistica)
	        detalle_nivel = respuesta_api.json()
	        
	        for j in range(len(detalle_nivel['names'])):
	            if detalle_nivel['names'][j]['language']['name'] == 'es':
	                lista_niveles.append([base_estadistica, detalle_nivel['names'][j]['name'], (base_estadistica/255*100)])
	    return lista_niveles

	""" CARD ASPECTO """
	def altura_pokemon(self):
	    # Altura de este Pokémon en decímetros.
	    return self.informacion_completa['height']

	def experiencia_generada(self):
	    # Experiencia base obtenida al derrotar a este Pokémon.
	    return self.informacion_completa['base_experience']

	def peso_pokemon(self):
	    # Peso de este Pokémon en hectogramos
	    return self.informacion_completa['weight']

	""" CARD HABILIDADES """
	def habilidades(self):
	    #Lista de habilidades
	    lista_habilidades = []
	    # Habilidades del Pokémon 
	    habilidades = self.informacion_completa['abilities']
	    for habilidad in habilidades:
	        # numero_habilidad = habilidad['slot']
	        # nombre_habilidad = habilidad['ability']['name']
	        url_habilidad = habilidad['ability']['url']
	        respuesta_api = requests.get(url_habilidad)
	        detalle_habilidad = respuesta_api.json()
	        for j in range(len(detalle_habilidad['names'])):
	            if detalle_habilidad['names'][j]['language']['name'] == 'es':
	                lista_habilidades.append(detalle_habilidad['names'][j]['name'])
	    
	    return lista_habilidades

	"""============::: PAGINA 2 :::============"""

	""" CARD HABILIDADES """
	def generaciones(self):
	    # Lista de generaciones 
	    lista_generaciones = []
	    # Índices de juegos relevantes para Pokémon por generación.
	    generaciones_videojuegos = self.informacion_completa['game_indices']
	    for generacion_videojuego in generaciones_videojuegos:
	        
	        """ Otros atributos"""
	        # indice_generacion_videojuego = generacion_videojuego['game_index']
	        # nombre_version_generacion_videojuego = generacion_videojuego['version']['name']
	        
	        """ Nombre de generacion en español"""
	        url_version_generacion_videojuego = generacion_videojuego['version']['url']
	        respuesta_api = requests.get(url_version_generacion_videojuego)
	        detalle_generaciones = respuesta_api.json()
	        
	        for i in range(len(detalle_generaciones['names'])):
	            if detalle_generaciones['names'][i]['language']['name'] == 'es':
	                generacion_videojuego = detalle_generaciones['names'][i]['name']
	                lista_generaciones.append(generacion_videojuego)
	                
	    return lista_generaciones

