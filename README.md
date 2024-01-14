# ProjectTelegramBot

**Guia e Descrição do Código: Telegram Bot para Rastreamento de Encomendas**

Este código Python implementa um bot do Telegram para rastreamento de encomendas utilizando a API da LineTrack. Aqui estão as principais características e um guia passo a passo para entender o código:

### Características Principais:

1. Rastreamento de Encomendas:
   - Utiliza a API da LineTrack para obter informações de rastreamento de encomendas a partir de códigos fornecidos.

2. Cadastro de Códigos de Rastreamento:
   - Permite que os usuários do bot cadastrem códigos de rastreamento para receber atualizações automáticas.

3. **Atualizações Automáticas:**
   - Implementa uma funcionalidade de consulta periódica que verifica se há atualizações nos status das encomendas cadastradas e notifica os usuários.

4. **Comandos do Telegram:**
   - Inclui comandos do Telegram como `/start` para iniciar o bot e `/codigo` para cadastrar e consultar códigos de rastreamento.

### Guia Passo a Passo:

1. **Configuração Inicial:**
   - Importa as bibliotecas necessárias, como `logging`, `json`, `time`, e `requests`.requestse, python-telegram-bot

2. **Configuração de Logging:**
   - Configuração básica para logs, permitindo rastrear mensagens informativas, erros e detalhes de execução.

3. **Função de Rastreamento:**
   - `rastreamento(code)`: Realiza a consulta à API da LineTrack para obter informações sobre o status de uma encomenda com base no código fornecido.

4. **Comandos do Telegram:**
   - `start(update, context)`: Comando inicial que cumprimenta o usuário e solicita o código de rastreamento.
   - `codigo(update, context)`: Comando para cadastrar e consultar códigos de rastreamento.

5. **Atualizações Automáticas:**
   - `re_consulta(update, context)`: Função assíncrona que realiza consultas periódicas aos códigos cadastrados, notificando os usuários sobre atualizações.

6. **Configuração do Bot e Comandos:**
   - Configuração da aplicação usando `ApplicationBuilder` e adição de comandos utilizando `CommandHandler`.

7. **Execução Contínua:**
   - Inicia a aplicação e mantém a execução contínua com `application.run_polling()`.

### Como Utilizar:

1. **Iniciar o Bot:**
   - Inicie o bot no Telegram utilizando o comando `/start`.

2. **Cadastrar Códigos:**
   - Utilize o comando `/codigo` seguido do código de rastreamento para cadastrar encomendas.

3. **Receber Atualizações:**
   - O bot realizará atualizações automáticas e notificará os usuários sobre mudanças no status das encomendas cadastradas.

Lembre-se de configurar corretamente o token do bot do Telegram e a URL da API da LineTrack antes de executar o código. Certifique-se de ter as bibliotecas necessárias instaladas (`requests` e `python-telegram-bot`).
