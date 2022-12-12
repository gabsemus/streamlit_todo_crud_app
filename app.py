import streamlit as st
import pandas as pd 
from db_fxns import * 
import streamlit.components.v1 as stc


HTML_BANNER = """
    <div style="background-color:#464e5f;padding:10px;border-radius:10px">
    <h1 style="color:white;text-align:center;">Planejando o Rolê</h1>
    <p style="color:white;text-align:center;">Gato e Gata em São Paulo</p>
    </div>
    """

def main():
	stc.html(HTML_BANNER)


	menu = ["Inserir","Visualizar","Excluir"]
	choice = st.sidebar.selectbox("Menu",menu)
	create_table()

	if choice == "Inserir":
		st.subheader("Adicionar a Lista: ")

		nome = st.text_input("Não esquecer de: ")

		quantidade = st.number_input("Quantidade: ", min_value=1, max_value= 50, value = 1, step = 1)

		motivo = st.text_area("Observação (opcional) : ")

		if st.button("Adicionar"):
			inserir_pendencia(nome,quantidade,motivo)
			st.success("Boa seu noia!")

	elif choice == "Visualizar":
		st.subheader("Visualizar Pendências")
		result = visualizar_todos()
		# st.write(result)
		df = pd.DataFrame(result,columns=["Pendência","Quantidade","Motivo"])
		st.dataframe(df)

	elif choice == "Excluir":
		st.subheader("Excluir")

		lista_pendencias = [i[0] for i in pendencias_por_nome()]
		pendencia_nome =  st.selectbox("Selecione a Pendência",lista_pendencias)
		if st.button("Excluir"):
			excluir_pendencia(pendencia_nome)
			st.warning("Excluido: '{}'".format(pendencia_nome))

if __name__ == '__main__':
	main()

