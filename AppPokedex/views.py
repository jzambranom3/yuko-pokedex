from django.shortcuts import render
from .apiPokemon import *

# VISTAS
def view_index(request):
	datos = {
		'title': 'Pokedex | Yuko'
		}
	return render(request, 'pokemon.html', datos)

def view_buscarPokemon(request, nombrePokemon):
	try:
		objPokemon = apiPokemon(nombrePokemon, '')
		if objPokemon.obtenerInformacion():
			datos = {
				'title': 'Pokedex | Yuko',
				'imagen': objPokemon.imagen_principal_pokemon(),
				'nombre': objPokemon.nombre_pokemon(),
				'id': objPokemon.identificador_pokemon(),
				'descripcion': objPokemon.descripcion_pokemon(),
				'tipo': objPokemon.tipo_pokemon(),
				'nivel': objPokemon.niveles_base(),
				'altura': objPokemon.altura_pokemon(),
				'experiencia': objPokemon.experiencia_generada(),
				'peso': objPokemon.peso_pokemon(),
				'habilidad': objPokemon.habilidades(),
				'generacion': objPokemon.generaciones()
				}
			return render(request, 'pokemon.html', datos)
		else:
			datos = {
				'title': 'Pokedex | Yuko',
				'error': 'No encontrado'
				}
			return render(request, 'pokemon.html', datos)
	except:
		datos = {
			'title': 'Pokedex | Yuko',
			'error': 'No encontrado'
			}
		return render(request, 'pokemon.html', datos)
# Create your views here.
