import random
import time

class ServicoDeNotificacao:
    def __init__(self):
        self.logs = []

    def enviar(self, usuario, canal, mensagem):
        if canal not in ["email", "sms"]:
            raise ValueError("Canal não suportado.")

        # Simulando envio com chance de falha
        sucesso = random.random() > 0.1  # 90% chance de sucesso
        status = "✅ Sucesso" if sucesso else "❌ Falha"

        # Simulando retentativa simples
        if not sucesso:
            time.sleep(1)
            sucesso = random.random() > 0.3
            status = "🔁 Retentativa com sucesso" if sucesso else "❌ Falha permanente"

        # Logging
        self.logs.append({
            "usuario": usuario,
            "canal": canal,
            "mensagem": mensagem,
            "status": status
        })
