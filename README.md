# techChallengeBancoCarrefourDIO
techChallengeBancoCarrefourDIO

Jairo Vinicius (viniciusvieira.eu@gmail.com)

1 - Para que este projeto funcione, você vai precisar das seguintes dependências:

python telegram bot

google api core 1.4.1

dialogflow 0.5.1

2 - no arquivo "main.py", na linha 56, você deve inserir o token do bot do telegram que foi criado (o trecho do código segue a abaixo):

botTelegram = Updater("INSIRA AQUI O TOKEN DO BOT TELEGRAM QUE FOI CRIADO", use_context=True)

3 - você vai precisar baixar as credencias de aplicativo google fornecida em formato JSON. Este arquivo deve estar na mesma pasta do arquivo "main.py". Depois você deve renomear o arquivo baixado para "private_key.json" para ser lido pelo comando que acontece na linha 25 do arquivo "main.py" (o trecho do código segue a abaixo):

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'private_key.json'

4 - no arquivo "main.py", na linha 27, você deve inserir o id do projeto no dialogflow (o trecho do código segue a abaixo):

idProjetoDialogflow = 'INSIRA AQUI O ID DO PROJETO DIALOGFLOW'

5 - basta executar o arquivo "main.py" pelo terminal ou na IDE de sua preferência, mas precisa estar conectado a internet para tudo funcionar.


