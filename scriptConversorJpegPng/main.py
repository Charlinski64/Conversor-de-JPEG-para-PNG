import os, sys 
from PIL import Image


# Carrega a imagem do caminho especificado
im1 = Image.open('C:\\Users\\nomeDoUsuario\\caminho\\da\\sua\\imagem.jpeg')

# Salva a imagem como um arquivo PNG no caminho desejado
im1.save('C:\\Users\\nomeDoUsuario\\caminho\\para\\salvar\\nova_imagem.png')

# A imagem original ('nova_imagem.png') precisa estar no caminho/PATH correto
images = ['C:\\Users\\nomeDoUsuario\\caminho\\para\\salvar\\nova_imagem.png']


for infile in images:
    f, e = os.path.splitext(infile)
    outfile = f + '.jpeg'  # Converte para .jpeg
    if infile != outfile:
        try:
            with Image.open(infile) as image:
                in_rgb = image.convert('RGB')  # Converte para RGB
                in_rgb.save(outfile, 'JPEG')   # Salva como JPEG
        except OSError:
            print(f'ERRO: Não foi possível converter {infile}.')