"""
Arquivo Main - Editor de PDF
Desenvolvido por: Victor Ladislau Viana

0) Biblioetcas Utilizadas:
                                        -Tkinter = Renderização da Interface Gráfica.
"""
#Importando as Bibliotecas:
import tkinter as tk


class PDF_EditorApp:
    
    # Métodos e Funções (Ações dos botões)
    def click_compactar(self):
        print("Botão clicado!")

    def click_mesclar(self):
        print("Os PDFS serão Mesclados")

    def click_sair(self):
        print("O programa será encerrado")
        self.root.quit()  # Encerra o programa adequadamente
    
    def __init__(self, root):
        self.root = root
        # Configurações da Janela Principal
        self.root.title("Invictor13 - Editor de PDF")
        self.root.state("zoomed")
        
        # Constrói a interface
        self.criar_cabecalho()
        self.criar_botoes()
        self.criar_rodape()

    def criar_cabecalho(self):
        # Cabeçalho
        self.L_titulo = tk.Label(self.root, text="Invictor13 - Editor de PDF")
        self.L_titulo.pack()
        
        self.L_subtitle = tk.Label(self.root, text="Escolha uma das opções para editar o PDF:")
        self.L_subtitle.pack()

    def criar_janelaprincipal(self):
        #Frame Principal para exibir mensagens do sistema:
        self.L_infor = tk.Label(self.root,text="")

    def criar_botoes(self):
        # Frame Principal e Botões de Navegação
        self.B_compactar = tk.Button(self.root, text="Compactar PDF", command=self.click_compactar, width="50", height="10")
        self.B_compactar.pack(pady=10)
        
        self.B_mesclar = tk.Button(self.root, text="Mesclar PDF", command=self.click_mesclar, width="50", height="10")
        self.B_mesclar.pack(pady=10)

        self.B_sair = tk.Button(self.root, text="Sair", command=self.click_sair, width="50", height="10")
        self.B_sair.pack(pady=10)

    def criar_rodape(self):
        # Rodapé
        self.L_titlefooter = tk.Label(self.root, text="Programa desenvolvido por Victor Viana - 2026")
        self.L_titlefooter.pack()
        
        self.L_subtitlefooter = tk.Label(self.root, text="MVP - Editor de PDF V0.1")
        self.L_subtitlefooter.pack()


# Inicialização do App
if __name__ == "__main__":
    janela = tk.Tk()
    app = PDF_EditorApp(janela)
    janela.mainloop()
