def analisar_sentimento(classificador, texto):
    mensagem = "<!> Esse texto é considerado"
    predicao = classificador.preditor_texto(texto)
    mensagem += (" positivo pelo classificadoe %s."%classificador.nome) if int(predicao[0]) > 0 else (" negativo pelo classificador %s." %classificador.nome)
    print(mensagem) 