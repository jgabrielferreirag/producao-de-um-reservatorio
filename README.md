# Produção de um reservatório com fluxo unidimensional

Este é um projeto que fiz para a disciplina de Engenharia de Reservatório, onde o objetivo era simular a produção de um reservatório de hidrocarbonetos hipotético, dividido em grids (blocos), com fluido levemente compressível e sendo o fluxo unidimensional e constante. Os métodos utilizados são os descritos no livro Basic Applied Reservoir Simulation by T. Ertekin, capitulo 5 que para efeitos de aproximação, estabelece que os parametros são constantes e iguais em todos os blocos.

Utilizei as bibliotecas matplotlib, pandas e numpy.

## Formulação explícita

Este método é direto, e estabelece que a Pressão no bloco N+1 no tempo T só depende das pressões nos blocos anteriores (N ou N-1) ou no tempo anterior (T-1). Ou seja, para calcular Pn(t), utilizamos valores que já são conhecidos.

![image](https://user-images.githubusercontent.com/67394387/156939348-f69d73ea-0029-4582-84ee-265d15a7146e.png)

### Exemplo de reservatório

![image](https://user-images.githubusercontent.com/67394387/156939420-82f5b957-ee8e-41a2-b6cd-6d407458ef98.png)

![image](https://user-images.githubusercontent.com/67394387/156939388-95fa5e8e-7b7c-475d-9b2d-fdf240f965d8.png)

#### Resultado esperado pelo exércicio proposto para intervalo de medições de 10 dias

![image](https://user-images.githubusercontent.com/67394387/156939479-e6222c7d-ade3-4561-90d7-56092af98382.png)

#### Resultado utilizando o simulador

![image](https://user-images.githubusercontent.com/67394387/156939668-bfe138c4-21e6-4b87-8d71-8f9f705dda24.png)

![image](https://user-images.githubusercontent.com/67394387/156939677-e06a2b0d-0306-41fd-bada-dacd855c3b03.png)


## Formulação Implícita

Este método utiliza valores desconhecidos para calcular a pressão do bloco N no tempo atual. Sendo assim, é necessário montar aa equações para todos os blocos no tempo atual, e resolver um sistema de equações. Para este método, tive que utilizar o numpy e seus arrays, para lidar com os sistemas de equações de forma matricial.

![image](https://user-images.githubusercontent.com/67394387/156939839-d8e0106b-6d9f-4b1d-909e-3c49ee99e1a5.png)

![image](https://user-images.githubusercontent.com/67394387/156939855-51e821ba-d5d0-4df0-a7a4-5c98d69d8fad.png)

Utilizando o reservatório anterior como exemplo:

#### Resultado esperado pelo exércicio proposto para intervalo de medições de 15 dias

![image](https://user-images.githubusercontent.com/67394387/156939904-88651cd9-73be-4128-9ab1-5bf19b991d2f.png)

#### Resultado utilizando o simulador

![image](https://user-images.githubusercontent.com/67394387/156940030-b4971ef5-33be-4fd9-8566-2dd2a9d49ac8.png)

![image](https://user-images.githubusercontent.com/67394387/156940054-8ad6135e-b79c-4604-ab2f-ae0643d5a1df.png)

## Ambiente Virtual

Recomendo a utilização de um ambiente virtual para instalar as dependências do projeto de forma local

```bash
python -m venv .venv
cd .\.venv\Scripts\
.\activate.ps1
```

## Instalação

Use o [pip](https://pip.pypa.io/en/stable/) para instalar as dependências do projeto

```bash
pip install requirements.txt
```


## Utilização

Basta escolher qual método utilizar e executar o código no terminal

```bash
python simuladorexplicito.py
```
ou
```bash
python simuladorimplicito.py
```

O programa perguntará ao usuário quais o valores dos parâmetros a serem utilizados, com suas unidades de medida apropriadas. Caso todos os valores sejam fornecidos, o script retornará um plot da pressão de cada bloco no tempo fornecido, e um arquivo .xslx com uma tabela dos dados.
