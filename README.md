# Conversor-de-JPEG-para-PNG
Este script utiliza a biblioteca Pillow (PIL) para converter imagens no formato JPEG para PNG, e vice-versa. O objetivo é permitir a conversão fácil entre esses dois formatos de imagem com uma interface simples em Python.


Requisitos
    Antes de executar o script, certifique-se de que você possui os seguintes requisitos:

1. Python instalado
    Este projeto foi desenvolvido usando Python 3.12. Você pode verificar a versão instalada em seu sistema executando o comando no terminal:

python --version

2. Instalar Pillow (PIL)
    Para que o script funcione corretamente, a biblioteca Pillow deve estar instalada. Você pode instalá-la com o seguinte comando no terminal:

    pip install Pillow


Como usar o script

1. Estrutura do código
    O script realiza as seguintes operações:

    Carrega uma imagem em formato JPEG.
    Converte a imagem para o formato PNG e a salva no diretório especificado.
    Converte uma imagem PNG para o formato JPEG (caso necessário).
   
2. Executando o script
    Clone o repositório ou baixe o script em seu ambiente local.

    Abra o script em um editor de texto ou IDE de sua preferência.

    No script, modifique os caminhos para os arquivos de imagem de acordo com o local onde suas imagens estão armazenadas. Exemplo de caminhos corretos:
   
    im1 = Image.open('C:\\Users\\SeuNome\\Caminho\\Para\\Imagem\\imagem.jpeg')
    im1.save('C:\\Users\\SeuNome\\Caminho\\Para\\Salvar\\imagem.png')
   
    Execute o script a partir do terminal ou do ambiente de desenvolvimento:
   
    python conversor_imagens.py
   
4. Conversão de JPEG para PNG
    O código converte automaticamente o arquivo JPEG especificado para o formato PNG. Certifique-se de ajustar os caminhos dos arquivos conforme necessário.

5. Conversão de PNG para JPEG
    O script também inclui um trecho para converter um arquivo PNG salvo para o formato JPEG. Os arquivos são automaticamente salvos no mesmo diretório com a extensão .jpeg.

Erros Comuns
    Caminhos de arquivo inválidos: Verifique se os caminhos dos arquivos de entrada e saída estão corretos e existem.
    Permissões de arquivo: Certifique-se de que você tem permissão para ler e gravar nos diretórios especificados.

Licença
    Este projeto é de código aberto e está disponível sob a licença MIT.
