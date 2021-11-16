import numpy as np
import vectorbt as vbt

dado = vbt.BinanceData.download('BTCBRL', start='2021-11-14', interval='1m').get()
preco_fechamento  = dado.get('Close')

indicador_rsi = vbt.RSI.run(preco_fechamento,window=5)

entrada = indicador_rsi.rsi_below(10, crossover=True)
saida= indicador_rsi.rsi_above(70, crossover=True)

portifolio = vbt.Portfolio.from_signals(preco_fechamento, entrada, saida, init_cash=10000)
portifolio.plot().show()

print(dado)