# -*- coding: utf-8 -*-
"""BD_.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XBwCwFn4dI1t9CQNhUtwQAyG7BY7B3o8
"""

import pandas as pd

dados = pd.read_excel('/content/infra.xlsx')
dados.head(3)

dados.tail(3)

dados['auinf_local_km'].notnull()

dados['auinf_local_km']= 0
dados.head(3)

dados['grav_tipo'].value_counts()

dados['descricao'].value_counts()

dados['tipo_veiculo'].value_counts()

dados['cometimento'].value_counts()

dados['auinf_local_rodovia'].value_counts()

! pip install https://Github.com/pandas-profiling/pandas-profiling/archive/master.zip