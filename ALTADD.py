import os
import json

print("JD2014 ALT Cover By SquareJDBR")

# Solicitar o "codenome" ao usuário
codenome = input("Por favor, insira o 'codenome': ")

# Solicitar o "nome do artista" ao usuário
nome_artista = input("Por favor, insira o 'nome do artista': ")

# Solicitar o "nome da música" ao usuário
nome_musica = input("Por favor, insira o 'nome da música': ")

# Solicitar o "codenome da música original" ao usuário
codenome_original = input("Por favor, insira o 'codenome da música original': ")

# Atualizar o dicionário com as informações inseridas
data = {
    "__class": "Actor_Template",
    "WIP": 0,
    "LOWUPDATE": 0,
    "UPDATE_LAYER": 0,
    "PROCEDURAL": 0,
    "STARTPAUSED": 0,
    "FORCEISENVIRONMENT": 0,
    "COMPONENTS": [
        {
            "__class": "JD_SongDescTemplate",
            "MapName": codenome,
            "JDVersion": 2014,
            "OriginalJDVersion": 2014,
            "RelatedAlbums": [codenome_original],
            "Artist": nome_artista,
            "Title": nome_musica,
            "Credits": "Tool Made By SquareJDBR",
            "PhoneImages": {
                "coach1": f"world/maps/{codenome}/menuart/textures/{codenome}_coach_1_phone.png",
                "cover": f"world/maps/{codenome}/menuart/textures/{codenome}_cover_phone.jpg"
            },
            "NumCoach": 1,
            "MainCoach": -1,
            "Difficulty": 1,
            "SweatDifficulty": 1,
            "backgroundType": 0,
            "LyricsType": 0,
            "Tags": ["ALTERNATE"],
            "Status": 3,
            "LocaleID": 4294967295,
            "MojoValue": 0,
            "CountInProgression": 1,
            "DefaultColors": {
                "songcolor_2a": [1, 0.666667, 0.666667, 0.666667],
                "lyrics": [1, 1, 0, 0],
                "theme": [1, 1, 1, 1],
                "songcolor_1a": [1, 0.266667, 0.266667, 0.266667],
                "songcolor_2b": [1, 0.466667, 0.466667, 0.466667],
                "songcolor_1b": [1, 0.066667, 0.066667, 0.066667]
            },
            "VideoPreviewPath": ""
        }
    ]
}

# Crie o arquivo songdesc.tpl.ckd e salve o conteúdo JSON nele
with open('songdesc.tpl.ckd', 'w') as outfile:
    json.dump(data, outfile, indent=4)

print("Arquivo songdesc.tpl.ckd gerado com sucesso!")
