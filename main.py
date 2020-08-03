# python telegram bot
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# google api core 1.4.1
# DialogFlow 0.5.1
import os
import dialogflow
from google.api_core.exceptions import InvalidArgument

# habilita o registro de log
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# define uma mensagem padrão para ser enviado como resposta ao comando /start
def start(atualizacao, contexto):
    atualizacao.message.reply_text('Olá! É muito bom você estar aqui! Em que posso te ajudar?')

# define uma mensagem padrão para ser enviad como resposta ao comando /help
def help(atualizacao, contexto):
    atualizacao.message.reply_text('Sim, eu vou te ajudar! Posso lhe informar sobre taxas de juros, faturas, contas, empréstimos, financiamentos, entre outras coisas. Basta perguntar. O que não souber, serei sincero e direi que não compreendi')

def processa(atualizacao, contexto):
    # private_key.json forcece alguns tokens de autenticação para este código acessar o DialogFlow
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'private_key.json'
    # dados do agente do dialogflow
    idProjetoDialogflow = 'INSIRA AQUI O ID DO PROJETO DIALOGFLOW'
    codigoLinguagem = 'pt-BR'
    idSessao = 'me'

    # inicia o cliente DialogFlow
    sessaoDoCliente = dialogflow.SessionsClient()
    # inicia a sessão
    sessao = sessaoDoCliente.session_path(idProjetoDialogflow, idSessao)
    # envelopa a mensagem recebida pelo bot do telegram
    mensagem = dialogflow.types.TextInput(text=atualizacao.message.text, language_code=codigoLinguagem)
    # envia a mensagem para o DialogFlow processar a intenção do usuário
    envelope = dialogflow.types.QueryInput(text=mensagem)
    # tenta pegar a resposta enviada pelo agente DialogFlow, caso tenha um erro, lança uma exceção
    try:
        resposta = sessaoDoCliente.detect_intent(session=sessao, query_input=envelope)
    except InvalidArgument:
        raise
    # para debug, imprimir no console algumas informações, como por exemplo,
    # id do chat, mensagem do usuário recebida pelo bot do telegram,
    # intenção processada, e a resposta concluída pelo DialogFlow
    print("ID do CHAT:", atualizacao.message.chat_id)
    print("Mensagem:", resposta.query_result.query_text)
    print("Intenção processada:", resposta.query_result.intent.display_name)
    print("Resposta:", resposta.query_result.fulfillment_text)
    # envia resposta concluída pelo DialogFlow para o bot telegram, e o usuário recebe sua resposta.
    atualizacao.message.reply_text(resposta.query_result.fulfillment_text)

def main():
    # instancia o botTelegram com o token dado pelo botFather
    botTelegram = Updater("INSIRA AQUI O TOKEN DO BOT TELEGRAM QUE FOI CRIADO", use_context=True)
    # instancia um despanchante
    despachante = botTelegram.dispatcher
    # inicia manipuladores para comandos e e mensagens
    despachante.add_handler(CommandHandler("start", start))
    despachante.add_handler(CommandHandler("help", help))
    despachante.add_handler(MessageHandler(Filters.text & ~Filters.command, processa))
    # incia o bot telegram
    botTelegram.start_polling()
    # executa até ser dado um comando CTRL+C para finalizar aplicação.
    botTelegram.idle()

if __name__ == '__main__':
    main()