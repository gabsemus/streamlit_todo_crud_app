import sqlite3
conn = sqlite3.connect('data.db',check_same_thread=False)
c = conn.cursor()


def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS pendencia(nome TEXT,quantidade TEXT,motivo TEXT)')

def inserir_pendencia(nome,quantidade,motivo):
	c.execute('INSERT INTO pendencia(nome,quantidade,motivo) VALUES (?,?,?)',(nome,quantidade,motivo))
	conn.commit()

def visualizar_todos():
	c.execute('SELECT * FROM pendencia')
	data = c.fetchall()
	return data

def pendencias_por_nome():
	c.execute('SELECT DISTINCT nome FROM pendencia')
	data = c.fetchall()
	return data

def excluir_pendencia(nome):
	c.execute('DELETE FROM pendencia WHERE nome="{}"'.format(nome))
	conn.commit()