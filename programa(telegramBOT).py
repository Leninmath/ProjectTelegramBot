import logging
import json
import time
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
def rastreamento(code):
    code=str(code)
    url_base = "https://api.linketrack.com/track/json?user=teste&token=1abcd00b2731640e886fb41a8a9671ad1434c599dbaa0a0de9a5aa619f29a83f&codigo="
    # Loop para fazer solicitações até ser bem-sucedido
    while True:
        try:
            # Construir a URL completa com o código de rastreamento
            url = url_base + code
            
            # Fazendo a solicitação HTTP para a API de rastreamento
            response = requests.get(url)
            response.raise_for_status()  # Verifica se a solicitação foi bem-sucedida

            # Obter dados do primeiro evento
            data = response.json()
            eventos = data.get('eventos', [])

            if eventos:
                celula = eventos[0]
                del celula['subStatus']

                texto_formatado = ''
                for chave, valor in celula.items():
                    linha = f'{chave}: {valor}\n'
                    texto_formatado += linha

                print(texto_formatado)
                print(type(celula))
                return texto_formatado
                break  # Sair do loop se a solicitação for bem-sucedida
            else:
                print("Nenhum evento retornado pela API.")
                break  # Sair do loop se nenhum evento for retornado
        except requests.exceptions.RequestException as e:
            print(f"Falha na solicitação: {e}")
            time.sleep(10)  # Aguardar 8 segundos antes de tentar novamente

#comando start, da abertura e faz a solicitaçao do codigo d rastreio 
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Olá, me envia o codigo de rastreio : ")

#comando, faz a busca do codigo e retorna a atualizaçao
async def codigo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    code = ' '.join(context.args).upper()
    status = rastreamento(code)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=status)
    print(code) 

if __name__ == '__main__':
    application = ApplicationBuilder().token('6773006649:AAFboz1PSegJldWJK51OYVc9ilAu9E6nBMU').build()
    
    comando_iniciar = CommandHandler('start', start)
    captura_codigo=CommandHandler('codigo',codigo)
    application.add_handler(comando_iniciar)
    application.add_handler(captura_codigo)
    
    application.run_polling()
    
    
    